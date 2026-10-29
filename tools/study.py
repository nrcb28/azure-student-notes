#!/usr/bin/env python3
"""Offline Azure study trainer. Uses the repository's original case banks."""
import argparse
import csv
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import hashlib
import html
import json
import os
from pathlib import Path
import random
import re
import sys
import tempfile
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ('es', 'en', 'it', 'de', 'fr', 'ru', 'ja', 'zh')
EXAMS = ('AZ-900', 'AZ-104', 'AZ-305', 'AZ-400')
UTC = timezone.utc


@dataclass(frozen=True)
class Card:
    language: str
    exam: str
    number: int
    question: str
    answer: str
    source: str

    @property
    def id(self):
        return f'{self.language}/{self.exam}/{self.number:02d}'


def load_cards(root=ROOT, language='es', exams=EXAMS):
    cards = []
    for exam in exams:
        path = root/'certifications'/language/f'{exam}-cases.md'
        text = path.read_text(encoding='utf-8')
        sections = re.findall(r'^## (\d+)\.\s+([^\n]+)\n(.*?)(?=^## |\Z)', text, re.M | re.S)
        found = []
        for number, question, body in sections:
            answer = re.search(r'<details>\s*<summary>.*?</summary>\s*(.*?)\s*</details>', body, re.S)
            if not answer or not answer.group(1).strip():
                raise ValueError(f'Missing answer: {path.name}, {number}')
            found.append(int(number))
            cards.append(Card(language, exam, int(number), question.strip(), answer.group(1).strip(),
                              str(path.relative_to(root))))
        if found != list(range(1, 11)):
            raise ValueError(f'Expected ten ordered cases: {path}')
    return cards


def stamp(value):
    return value.astimezone(UTC).isoformat(timespec='seconds')


def parse_time(value):
    if not isinstance(value, str):
        raise ValueError('Progress timestamps must be ISO-formatted strings')
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise ValueError('Progress timestamps require a timezone')
    return parsed.astimezone(UTC)


def validate_state(state):
    if (not isinstance(state, dict) or type(state.get('version')) is not int or
            state['version'] != 1 or not isinstance(state.get('cards'), dict)):
        raise ValueError('Unsupported or invalid progress file; it was not overwritten')
    for key, record in state['cards'].items():
        if not isinstance(key, str) or not re.fullmatch(r'(es|en|it|de|fr|ru|ja|zh)/AZ-(900|104|305|400)/(0[1-9]|10)', key):
            raise ValueError('Invalid progress card ID')
        if not isinstance(record, dict):
            raise ValueError('Invalid progress record')
        for field in ('reviews', 'repetitions', 'lapses', 'interval_days', 'last_grade'):
            if type(record.get(field)) is not int or record[field] < 0:
                raise ValueError(f'Invalid progress field: {field}')
        if record['last_grade'] > 3:
            raise ValueError('Invalid grade')
        if (record['reviews'] < 1 or record['repetitions'] > record['reviews'] or
                record['lapses'] > record['reviews'] or record['interval_days'] > 365):
            raise ValueError('Invalid progress counters or interval')
        grade = record['last_grade']
        if ((grade == 0 and (record['repetitions'] != 0 or record['interval_days'] != 0)) or
                (grade == 1 and (record['repetitions'] != 0 or record['interval_days'] != 1)) or
                (grade >= 2 and (record['repetitions'] < 1 or record['interval_days'] < 1))):
            raise ValueError('Progress rating and review interval disagree')
        if parse_time(record.get('due')) < parse_time(record.get('last_review')):
            raise ValueError('Progress due time precedes its last review')
    return state


class Progress:
    """Atomic, permission-restricted writes with concurrent-session protection."""
    def __init__(self, path):
        self.path = Path(path)
        raw = self.path.read_bytes() if self.path.exists() else None
        self.fingerprint = hashlib.sha256(raw).hexdigest() if raw is not None else None
        self.state = validate_state(json.loads(raw)) if raw is not None else {'version': 1, 'cards': {}}

    def save(self):
        validate_state(self.state)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        lock = self.path.with_name(self.path.name + '.lock')
        try:
            descriptor = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        except FileExistsError as error:
            raise ValueError(f'Another session or stale lock exists: {lock}') from error
        os.close(descriptor)
        temporary = None
        try:
            current = self.path.read_bytes() if self.path.exists() else None
            fingerprint = hashlib.sha256(current).hexdigest() if current is not None else None
            if fingerprint != self.fingerprint:
                raise ValueError('Progress changed in another session; reload before continuing')
            raw = (json.dumps(self.state, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
            with tempfile.NamedTemporaryFile(dir=self.path.parent, prefix='.study-', delete=False) as stream:
                temporary = Path(stream.name)
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, self.path)
            temporary = None
            self.fingerprint = hashlib.sha256(raw).hexdigest()
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
            lock.unlink(missing_ok=True)


def schedule(previous, grade, now):
    if type(grade) is not int or grade not in (0, 1, 2, 3):
        raise ValueError('Grade must be 0, 1, 2 or 3')
    old = previous or {'reviews': 0, 'repetitions': 0, 'lapses': 0, 'interval_days': 0}
    repetitions = old['repetitions']
    if grade == 0:
        interval, repetitions = 0, 0
        due = now + timedelta(minutes=10)
    elif grade == 1:
        interval, repetitions = 1, 0
        due = now + timedelta(days=interval)
    else:
        repetitions += 1
        if grade == 3:
            interval = 4 if repetitions == 1 else max(4, round(old['interval_days'] * 2.5))
        else:
            interval = 1 if repetitions == 1 else (3 if repetitions == 2 else max(3, old['interval_days'] * 2))
        interval = min(365, interval)
        due = now + timedelta(days=interval)
    return {'reviews': old['reviews'] + 1, 'repetitions': repetitions,
            'lapses': old['lapses'] + int(grade == 0), 'interval_days': interval,
            'last_grade': grade, 'last_review': stamp(now), 'due': stamp(due)}


def select_cards(cards, state, now, mode='due', limit=10, seed=None):
    records = state['cards']
    if mode == 'random':
        selected = list(cards)
        random.Random(seed).shuffle(selected)
    elif mode == 'weak':
        selected = [card for card in cards if card.id in records and
                    (records[card.id]['last_grade'] < 2 or records[card.id]['lapses'] > 0)]
        selected.sort(key=lambda c: (-records[c.id]['lapses'], records[c.id]['last_grade'], c.id))
    else:
        selected = [card for card in cards if card.id not in records or parse_time(records[card.id]['due']) <= now]
        selected.sort(key=lambda c: (c.id not in records,
                                    parse_time(records[c.id]['due']) if c.id in records else now,
                                    c.id))
    return selected[:limit]


def statistics(cards, state, now):
    rows = []
    for exam in EXAMS:
        bank = [c for c in cards if c.exam == exam]
        if not bank:
            continue
        seen = [state['cards'][c.id] for c in bank if c.id in state['cards']]
        rows.append({'exam': exam, 'total': len(bank), 'new': len(bank) - len(seen),
                     'due': sum(parse_time(r['due']) <= now for r in seen),
                     'consolidated': sum(r['repetitions'] >= 2 and r['last_grade'] >= 2 for r in seen),
                     'lapses': sum(r['lapses'] for r in seen)})
    return rows


def export_anki(cards, destination):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation prevents accidental replacement of personal exports.
    with destination.open('x', encoding='utf-8', newline='') as stream:
        stream.write('#separator:Tab\n#html:true\n#tags column:3\n')
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        clean = lambda value: html.escape(value.replace('\t', ' ')).replace('\n', '<br>')
        for card in cards:
            url = 'https://github.com/nrcb28/azure-student-notes/blob/main/' + card.source
            back = clean(card.answer) + f'<hr><small><a href="{html.escape(url, quote=True)}">{card.id}</a></small>'
            writer.writerow([clean(card.exam + ' · ' + card.question), back,
                             card.language + ' ' + card.exam.lower().replace('-', '')])
    return len(cards)


def text_for(language):
    messages = json.loads((ROOT/'tools/study_ui.json').read_text(encoding='utf-8'))
    required = {'doctor', 'exported', 'next', 'demo', 'stats_header', 'assessment',
                'plan_notice', 'plan_day', 'empty', 'reveal', 'grade', 'source',
                'invalid', 'saved', 'error', 'interrupted'}
    language_messages = messages.get(language) if isinstance(messages, dict) else None
    if (not isinstance(language_messages, dict) or not required <= language_messages.keys() or
            any(not isinstance(language_messages[key], str) for key in required)):
        raise ValueError(f'Incomplete or invalid study interface: {language}')
    return language_messages


def positive(value):
    number = int(value)
    if not 1 <= number <= 100:
        raise argparse.ArgumentTypeError('Choose a number between 1 and 100')
    return number


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    commands = result.add_subparsers(dest='command', required=True)
    for name in ('study', 'stats', 'export', 'plan', 'demo', 'doctor'):
        command = commands.add_parser(name)
        command.add_argument('--lang', choices=LANGUAGES, default='es')
        command.add_argument('--exam', choices=EXAMS, action='append')
        command.add_argument('--progress', type=Path, default=ROOT/'.study-progress.json')
        command.add_argument('--timezone', default='Europe/Madrid')
        if name in ('study', 'demo'):
            command.add_argument('--limit', type=positive, default=10)
            command.add_argument('--mode', choices=('due', 'weak', 'random'), default='due')
            command.add_argument('--seed', type=int)
        if name == 'stats':
            command.add_argument('--json', action='store_true')
        if name == 'export':
            command.add_argument('--output', type=Path, required=True)
        if name == 'plan':
            command.add_argument('--days', type=positive, default=7)
            command.add_argument('--minutes', type=positive, default=20)
    return result


def main(argv=None):
    args = parser().parse_args(argv)
    ui = {'error': 'Unable to load the study interface'}
    try:
        ui = text_for(args.lang)
        zone = UTC
        if args.command in ('study', 'demo') and args.timezone != 'UTC':
            zone = ZoneInfo(args.timezone)
        cards = load_cards(language=args.lang, exams=tuple(dict.fromkeys(args.exam or EXAMS)))
        now = datetime.now(UTC)
        if args.command == 'doctor':
            count = sum(len(load_cards(language=lang)) for lang in LANGUAGES)
            print(ui['doctor'].format(count=count))
            return 0
        if args.command == 'export':
            count = export_anki(cards, args.output)
            print(ui['exported'].format(count=count, path=args.output))
            return 0
        if args.command == 'demo':
            card = cards[0]
            print(f'{card.exam}: {card.question}\n\n{card.answer}\n')
            due = parse_time(schedule(None, 2, now)['due']).astimezone(zone).strftime('%Y-%m-%d %H:%M %Z')
            print(ui['next'].format(value=due))
            print(ui['demo'])
            return 0
        progress = Progress(args.progress)
        if args.command == 'stats':
            rows = statistics(cards, progress.state, now)
            if args.json:
                print(json.dumps(rows, ensure_ascii=False, indent=2))
            else:
                print(ui['stats_header'])
                for row in rows:
                    print('{exam}: {new} / {due} / {consolidated} / {lapses}'.format(**row))
                print(ui['assessment'])
            return 0
        if args.command == 'plan':
            quota = min(10, max(1, args.minutes // 4))
            rows = statistics(cards, progress.state, now)
            exam_order = [r['exam'] for r in sorted(rows, key=lambda r: (-r['lapses'], r['exam']))]
            pools = {exam: [c for c in cards if c.exam == exam] for exam in exam_order}
            used = set()
            print(ui['plan_notice'])
            for day in range(args.days):
                exam = exam_order[day % len(exam_order)]
                pending = [c for c in pools[exam] if c.id not in used]
                selected = select_cards(pending, progress.state, now, mode='weak', limit=quota)
                selected += [c for c in pending if c not in selected][:max(0, quota-len(selected))]
                if not selected:
                    selected = pools[exam][:quota]
                used.update(c.id for c in selected)
                print(ui['plan_day'].format(day=day+1, exam=exam, cards=', '.join(str(c.number) for c in selected)))
            return 0
        selected = select_cards(cards, progress.state, now, args.mode, args.limit, args.seed)
        if not selected:
            print(ui['empty'])
            return 0
        completed = 0
        print(ui['assessment'])
        for card in selected:
            print(f'\n{completed+1}/{len(selected)} · {card.exam} · {card.question}')
            if input(ui['reveal']).strip().lower() == 'q':
                break
            print('\n' + card.answer + '\n' + ui['source'] + ': ' + card.source)
            while True:
                answer = input(ui['grade']).strip().lower()
                if answer == 'q':
                    print(ui['saved'].format(count=completed))
                    return 0
                if answer in ('0', '1', '2', '3'):
                    break
                print(ui['invalid'])
            now = datetime.now(UTC)
            record = schedule(progress.state['cards'].get(card.id), int(answer), now)
            progress.state['cards'][card.id] = record
            progress.save()
            completed += 1
            local_due = parse_time(record['due']).astimezone(zone).strftime('%Y-%m-%d %H:%M %Z')
            print(ui['next'].format(value=local_due))
        print(ui['saved'].format(count=completed))
        return 0
    except (OSError, ValueError, KeyError, TypeError, ZoneInfoNotFoundError) as error:
        print(ui['error'] + ': ' + str(error), file=sys.stderr)
        return 2
    except (EOFError, KeyboardInterrupt):
        print('\n' + ui['interrupted'])
        return 0


if __name__ == '__main__':
    sys.exit(main())
