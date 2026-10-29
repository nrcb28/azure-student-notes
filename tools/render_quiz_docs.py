#!/usr/bin/env python3
"""Render the eight read-in-GitHub question sheets from the quiz's source bank."""
import argparse
import sys

from quiz import LANGUAGES, LETTERS, ROOT, load_bank, text_for

TITLES = {
    'es': 'Ocho escenarios para practicar',
    'en': 'Eight scenarios to practise',
    'it': 'Otto scenari per esercitarsi',
    'de': 'Acht Szenarien zum Üben',
    'fr': 'Huit scénarios pour s’entraîner',
    'ru': 'Восемь сценариев для практики',
    'ja': '8 つのシナリオで練習',
    'zh': '八个场景练习',
}


def render(bank, language):
    texts = text_for(language)
    lines = [f'# {TITLES[language]}', '', '[←](19-mini-quiz.md) · [CLI](../QUIZ.md)', '',
             texts['report_notice'], '']
    for card in bank:
        variant = card['variants'][language]
        lines.extend([f'<a id="quiz-{card["id"]}"></a>', '',
                      f'## {card["exam"]} · {texts["topics"][card["topic"]]}', '',
                      variant['question'], ''])
        for letter, option in zip(LETTERS, variant['options']):
            lines.append(f'- **{letter}.** {option}')
        correct = variant['correct']
        lines.extend(['', '<details>', f'<summary>{texts["explanation"]}</summary>', '',
                      f'**{LETTERS[correct]}. {variant["options"][correct]}**', '', variant['explanation'], ''])
        for index, reason in enumerate(variant['distractors']):
            if index != correct:
                lines.append(f'- **{LETTERS[index]}.** {reason}')
        lines.extend(['', f'[{texts["source"]}]({variant["source"]}) · '
                          f'[{texts["study"]}]({variant["chapter"]})', '', '</details>', ''])
    return '\n'.join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if generated sheets differ; do not write')
    args = parser.parse_args(argv)
    bank = load_bank()
    stale = []
    for language in LANGUAGES:
        path = ROOT/language/'20-quiz-cases.md'
        expected = render(bank, language)
        if args.check:
            if not path.is_file() or path.read_text(encoding='utf-8') != expected:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(expected, encoding='utf-8')
    if stale:
        print('Regenerate with python tools/render_quiz_docs.py: ' + ', '.join(stale), file=sys.stderr)
        return 1
    print('Eight quiz sheets match the source bank.' if args.check else 'Rendered eight quiz sheets.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
