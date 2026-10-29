#!/usr/bin/env python3
"""Small, original Azure MCQ practice; standard library, no network or Azure calls."""
import argparse
import copy
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import random
import re
import string
import sys
import time
from urllib.parse import urlsplit
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ('es', 'en', 'it', 'de', 'fr', 'ru', 'ja', 'zh')
EXAMS = ('AZ-900', 'AZ-104', 'AZ-305', 'AZ-400')
LETTERS = 'ABCD'
TEXT_KEYS = ('intro', 'question', 'answer_prompt', 'invalid', 'late', 'correct',
             'incorrect', 'skipped', 'explanation', 'reason', 'source', 'study',
             'summary', 'topic', 'report_saved', 'report_notice', 'timer_notice',
             'empty', 'doctor', 'demo', 'error', 'interrupted', 'status')


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def finite_number(value):
    if type(value) not in (int, float):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def validate_variant(value):
    if not isinstance(value, dict):
        raise ValueError('Invalid question variant')
    for key in ('question', 'explanation', 'source', 'chapter'):
        if not nonempty(value.get(key)):
            raise ValueError(f'Missing question field: {key}')
    options = value.get('options')
    if (not isinstance(options, list) or len(options) != 4 or
            not all(nonempty(option) for option in options) or
            len({option.strip().casefold() for option in options}) != 4):
        raise ValueError('Each question needs four distinct nonempty options')
    correct = value.get('correct')
    if type(correct) is not int or not 0 <= correct < 4:
        raise ValueError('The answer index must be an integer from zero to three')
    reasons = value.get('distractors')
    if (not isinstance(reasons, list) or len(reasons) != 4 or
            not all(isinstance(reason, str) for reason in reasons) or
            any(not nonempty(reason) for index, reason in enumerate(reasons) if index != correct)):
        raise ValueError('Each incorrect option needs its own reason')
    url = urlsplit(value['source'])
    if (url.scheme != 'https' or url.netloc != 'learn.microsoft.com' or
            not url.path.startswith('/en-us/') or url.fragment or url.query):
        raise ValueError('Sources must be direct HTTPS Microsoft Learn pages')
    if not re.fullmatch(r'\d{2}-[a-z-]+\.md', value['chapter']):
        raise ValueError('Invalid local study chapter')
    return value


def validate_bank(bank, root=ROOT):
    if not isinstance(bank, list) or not bank:
        raise ValueError('Question bank must be a nonempty list')
    found = set()
    for card in bank:
        if not isinstance(card, dict):
            raise ValueError('Invalid question')
        key = card.get('id')
        if not isinstance(key, str) or not re.fullmatch(r'q\d{2,}', key) or key in found:
            raise ValueError('Question IDs must be valid and unique')
        found.add(key)
        if (card.get('exam') not in EXAMS or not isinstance(card.get('topic'), str) or
                not re.fullmatch(r'[a-z]+(?:-[a-z]+)*', card['topic'])):
            raise ValueError('Invalid exam or topic')
        variants = card.get('variants')
        if not isinstance(variants, dict) or set(variants) != set(LANGUAGES):
            raise ValueError(f'{key}: all eight language variants are required')
        for lang, variant in variants.items():
            validate_variant(variant)
            if not (root/lang/variant['chapter']).is_file():
                raise ValueError(f'{key}: missing local study chapter for {lang}')
        base = variants['en']
        for variant in variants.values():
            if any(variant[field] != base[field] for field in ('correct', 'source', 'chapter')):
                raise ValueError(f'{key}: translated answer order or references differ')
    if set(card['exam'] for card in bank) != set(EXAMS):
        raise ValueError('The bank must cover all four exam routes')
    return bank


def load_bank():
    return validate_bank(json.loads((ROOT/'tools/quiz_bank.json').read_text(encoding='utf-8')))


def placeholders(value):
    return {name for _, name, _, _ in string.Formatter().parse(value) if name is not None}


def text_for(language):
    bundle = json.loads((ROOT/'tools/quiz_ui.json').read_text(encoding='utf-8'))
    if not isinstance(bundle, dict) or set(bundle) != set(LANGUAGES):
        raise ValueError('Incomplete quiz interface translations')
    for lang, texts in bundle.items():
        if (not isinstance(texts, dict) or set(texts) != set(TEXT_KEYS) | {'topics', 'statuses'} or
                any(not nonempty(texts[key]) for key in TEXT_KEYS)):
            raise ValueError(f'Incomplete quiz interface: {lang}')
        for field in ('topics', 'statuses'):
            if (not isinstance(texts[field], dict) or
                    set(texts[field]) != set(bundle['en'][field]) or
                    not all(nonempty(value) for value in texts[field].values())):
                raise ValueError(f'Incomplete quiz labels: {lang}/{field}')
        for key in TEXT_KEYS:
            if placeholders(texts[key]) != placeholders(bundle['en'][key]):
                raise ValueError(f'Invalid quiz translation placeholders: {lang}/{key}')
    return bundle[language]


def select_questions(bank, language, exams, count, seed=None):
    """Round-robin sampling balances exam routes; options are shuffled independently."""
    rng = random.Random(seed)
    exams = list(dict.fromkeys(exams))
    if language not in LANGUAGES or not exams or any(exam not in EXAMS for exam in exams):
        raise ValueError('Choose a supported language and exam route')
    pools = {exam: [card for card in bank if card['exam'] == exam] for exam in exams}
    available = sum(len(pool) for pool in pools.values())
    if type(count) is not int or not 1 <= count <= available:
        raise ValueError(f'--count must be between 1 and {available} for the selected routes')
    for pool in pools.values():
        rng.shuffle(pool)
    rng.shuffle(exams)
    chosen = []
    while len(chosen) < count:
        for exam in exams:
            if pools[exam] and len(chosen) < count:
                chosen.append(pools[exam].pop())
    rng.shuffle(chosen)
    snapshots = []
    for card in chosen:
        order = list(range(4))
        rng.shuffle(order)
        snapshots.append(dict(id=card['id'], exam=card['exam'], topic=card['topic'],
                              variant=copy.deepcopy(card['variants'][language]), order=order, choice=None))
    return snapshots


def parse_reply(reply, order):
    reply = reply.strip().upper()
    if reply in LETTERS and len(reply) == 1:
        return order[LETTERS.index(reply)]
    if reply in ('S', ''):
        return None
    if reply == 'Q':
        return 'quit'
    raise ValueError('Choose A, B, C, D, S, or Q')


def summarize(questions):
    correct = sum(q['choice'] is not None and q['choice'] == q['variant']['correct'] for q in questions)
    unanswered = sum(q['choice'] is None for q in questions)
    return dict(correct=correct, total=len(questions), incorrect=len(questions)-correct-unanswered,
                unanswered=unanswered)


def show_question(question, number, total, texts, output=print):
    output('\n' + texts['question'].format(number=number, total=total, exam=question['exam']))
    output(question['variant']['question'])
    for letter, index in zip(LETTERS, question['order']):
        output(f"{letter}. {question['variant']['options'][index]}")


def show_feedback(question, language, texts, output=print):
    variant = question['variant']
    choice = question['choice']
    correct_letter = LETTERS[question['order'].index(variant['correct'])]
    if choice is None:
        output(texts['skipped'])
    elif choice == variant['correct']:
        output(texts['correct'])
    else:
        output(texts['incorrect'].format(letter=correct_letter))
        chosen_letter = LETTERS[question['order'].index(choice)]
        output(f"{texts['reason']} {chosen_letter}. {variant['options'][choice]} — {variant['distractors'][choice]}")
    output(f"{correct_letter}. {variant['options'][variant['correct']]}")
    output(texts['explanation'] + ' ' + variant['explanation'])
    output(texts['source'] + ' ' + variant['source'])
    output(texts['study'] + f' {language}/{variant["chapter"]}')


def show_summary(report, texts, output=print):
    output('\n' + texts['summary'].format(**summarize(report['questions'])))
    output(texts['status'].format(status=texts['statuses'][report['status']]))
    for topic in dict.fromkeys(q['topic'] for q in report['questions']):
        rows = [q for q in report['questions'] if q['topic'] == topic]
        output(texts['topic'].format(topic=texts['topics'].get(topic, topic), **summarize(rows)))
    output(texts['report_notice'])


def run_session(questions, language, mode, minutes, texts, input_fn=None,
                output=print, clock=time.monotonic, utcnow=None):
    input_fn = input if input_fn is None else input_fn
    utcnow = (lambda: datetime.now(timezone.utc)) if utcnow is None else utcnow
    if mode not in ('practice', 'exam'):
        raise ValueError('Choose practice or exam mode')
    if minutes is not None and (not finite_number(minutes) or minutes <= 0 or
                                not finite_number(minutes * 60)):
        raise ValueError('--minutes must yield a positive finite duration')
    started_at, started = utcnow(), clock()
    limit = minutes * 60 if minutes is not None else None
    report = dict(version=1, language=language, mode=mode, started_at=started_at.isoformat(),
                  limit_seconds=limit, questions=copy.deepcopy(questions), status='completed')
    output(texts['intro'].format(count=len(questions)))
    if limit is not None:
        output(texts['timer_notice'])
    try:
        for number, question in enumerate(report['questions'], 1):
            if limit is not None and clock() - started >= limit:
                report['status'] = 'timeout'
                break
            show_question(question, number, len(questions), texts, output)
            while True:
                raw = input_fn(texts['answer_prompt'] + ' ')
                # A synchronous terminal input cannot interrupt a blocked read.
                if limit is not None and clock() - started >= limit:
                    output(texts['late'])
                    report['status'] = 'timeout'
                    break
                try:
                    reply = parse_reply(raw, question['order'])
                except ValueError:
                    output(texts['invalid'])
                    continue
                if reply == 'quit':
                    report['status'] = 'quit'
                else:
                    question['choice'] = reply
                    if mode == 'practice':
                        show_feedback(question, language, texts, output)
                break
            if report['status'] != 'completed':
                break
    except (EOFError, KeyboardInterrupt):
        report['status'] = 'interrupted'
        output('\n' + texts['interrupted'])
    report['finished_at'] = utcnow().isoformat()
    report['elapsed_seconds'] = max(0, round(clock()-started, 3))
    return validate_report(report)


def parse_time(value):
    if not isinstance(value, str):
        raise ValueError('Invalid report timestamp')
    result = datetime.fromisoformat(value)
    if result.tzinfo is None:
        raise ValueError('Report timestamps require timezone offsets')
    return result


def validate_report(report):
    if (not isinstance(report, dict) or type(report.get('version')) is not int or report['version'] != 1 or
            report.get('language') not in LANGUAGES or report.get('mode') not in ('practice', 'exam') or
            report.get('status') not in ('completed', 'quit', 'timeout', 'interrupted')):
        raise ValueError('Unsupported or invalid quiz report')
    # Wall-clock adjustments need not match monotonic elapsed time.
    parse_time(report.get('started_at'))
    parse_time(report.get('finished_at'))
    for field in ('elapsed_seconds', 'limit_seconds'):
        value = report.get(field)
        if field == 'limit_seconds' and value is None:
            continue
        if not finite_number(value) or value < 0:
            raise ValueError(f'Invalid report duration: {field}')
        if field == 'limit_seconds' and value == 0:
            raise ValueError('Report time limit must be positive')
    questions = report.get('questions')
    if not isinstance(questions, list) or not questions:
        raise ValueError('Report has no question snapshots')
    found = set()
    for question in questions:
        if not isinstance(question, dict):
            raise ValueError('Invalid report question')
        key = question.get('id')
        if not isinstance(key, str) or not re.fullmatch(r'q\d{2,}', key) or key in found:
            raise ValueError('Invalid or duplicate report question ID')
        found.add(key)
        if (question.get('exam') not in EXAMS or
                not isinstance(question.get('topic'), str) or
                not re.fullmatch(r'[a-z]+(?:-[a-z]+)*', question['topic'])):
            raise ValueError('Invalid report exam or topic')
        validate_variant(question.get('variant'))
        order = question.get('order')
        if (not isinstance(order, list) or len(order) != 4 or
                any(type(index) is not int for index in order) or set(order) != set(range(4))):
            raise ValueError('Invalid report option ordering')
        if 'choice' not in question:
            raise ValueError('Missing report choice')
        choice = question['choice']
        if choice is not None and (type(choice) is not int or not 0 <= choice < 4):
            raise ValueError('Invalid report choice')
    return report


def save_report(report, destination):
    validate_report(report)
    raw = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation also protects a report created after the preflight check.
    descriptor = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, 'w', encoding='utf-8') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return destination


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    commands = result.add_subparsers(dest='command', required=True)
    for name in ('run', 'review', 'doctor', 'demo'):
        command = commands.add_parser(name)
        command.add_argument('--lang', choices=LANGUAGES, default='es', help='Interface/question language; review keeps the saved question language')
        if name in ('run', 'demo'):
            command.add_argument('--exam', action='append', choices=EXAMS)
            command.add_argument('--seed', type=int, help='Reproducible question and option order')
        if name == 'run':
            command.add_argument('--mode', choices=('practice', 'exam'), default='practice')
            command.add_argument('--count', type=int, help='Number of distinct questions; defaults to up to eight available')
            command.add_argument('--minutes', type=float, help='Optional session limit, checked after terminal input')
            command.add_argument('--report', type=Path, help='New report path; existing files are never replaced')
        if name == 'review':
            command.add_argument('--report', required=True, type=Path)
            command.add_argument('--all', action='store_true', help='Include correct answers')
            command.add_argument('--json', action='store_true', help='Print recomputed summary without question text')
    return result


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        texts = text_for(args.lang)
        if args.command == 'review':
            # Review uses snapshots and remains usable if the current bank changes.
            report = validate_report(json.loads(args.report.read_text(encoding='utf-8')))
            if args.json:
                print(json.dumps(summarize(report['questions'])))
                return 0
            show_summary(report, texts)
            selected = [q for q in report['questions'] if args.all or q['choice'] != q['variant']['correct']]
            for number, question in enumerate(selected, 1):
                show_question(question, number, len(selected), texts)
                show_feedback(question, report['language'], texts)
            if not selected:
                print(texts['empty'])
            return 0
        bank = load_bank()
        if any(card['topic'] not in texts['topics'] for card in bank):
            raise ValueError('Missing translated topic labels')
        if args.command == 'doctor':
            print(texts['doctor'].format(scenarios=len(bank), variants=len(bank)*len(LANGUAGES)))
            return 0
        exams = args.exam or EXAMS
        available = sum(card['exam'] in exams for card in bank)
        count = 1 if args.command == 'demo' else (min(8, available) if args.count is None else args.count)
        questions = select_questions(bank, args.lang, exams, count, args.seed)
        if args.command == 'demo':
            print(texts['demo'])
            show_question(questions[0], 1, 1, texts)
            show_feedback(questions[0], args.lang, texts)
            return 0
        if args.minutes is not None and (not finite_number(args.minutes) or args.minutes <= 0 or
                                          not finite_number(args.minutes * 60)):
            raise ValueError('--minutes must be a positive finite number')
        destination = args.report or ROOT/'.study-reports'/('quiz-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8]+'.json')
        if destination.exists():
            raise FileExistsError(f'Report already exists: {destination}')
        report = run_session(questions, args.lang, args.mode, args.minutes, texts)
        save_report(report, destination)
        print(texts['report_saved'].format(path=destination))
        show_summary(report, texts)
        if args.mode == 'exam':
            for question in report['questions']:
                print('\n' + question['variant']['question'])
                show_feedback(question, args.lang, texts)
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        label = locals().get('texts', {}).get('error', 'Error:')
        print(f'{label} {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
