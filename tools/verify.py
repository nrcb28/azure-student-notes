#!/usr/bin/env python3
"""Run the complete offline repository checks without modifying study data.

Requires Python 3.9+ and Bash. No network, Azure deployment, Bicep compilation,
progress-file updates, deck exports or question-sheet generation.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECKS = (
    ('documentation and local links', ('tools/check_docs.py',)),
    ('common core and workbooks', ('tools/check_study_core.py',)),
    ('trainer case banks and interface', ('tools/study.py', 'doctor', '--lang', 'en')),
    ('quiz bank and interface', ('tools/quiz.py', 'doctor', '--lang', 'en')),
    ('generated quiz sheets', ('tools/render_quiz_docs.py', '--check')),
    ('behavioural tests and Anki consistency',
     ('-m', 'unittest', 'discover', '-s', 'tools', '-p', 'test_*.py', '-q')),
)


def registry_errors(manifest, study_routes, document_routes, study_languages,
                    quiz_routes, quiz_languages):
    """Keep independently used allowlists aligned while retaining quiz scope."""
    if (not isinstance(manifest, dict) or not isinstance(manifest.get('exams'), dict) or
            not isinstance(manifest.get('languages'), list)):
        return ['Invalid study_core.json exam/language registry']
    errors = []
    for label, sequence in (('trainer routes', study_routes), ('required document routes', document_routes),
                            ('trainer languages', study_languages), ('quiz routes', quiz_routes),
                            ('quiz languages', quiz_languages), ('manifest languages', manifest['languages'])):
        if (not isinstance(sequence, (tuple, list)) or not sequence or
                any(not isinstance(item, str) or not item for item in sequence) or
                len(set(sequence)) != len(sequence)):
            errors.append(f'Invalid or duplicated {label}')
    if errors:
        return errors
    if tuple(manifest['exams']) != tuple(study_routes):
        errors.append('Trainer route order and workbook manifest differ')
    if set(document_routes) != set(study_routes):
        errors.append('Required document routes and trainer routes differ')
    if tuple(manifest['languages']) != tuple(study_languages) or tuple(quiz_languages) != tuple(study_languages):
        errors.append('Manifest, trainer and quiz language registries differ')
    # The mini quiz intentionally covers only four of the sixteen trainer routes.
    if not set(quiz_routes) <= set(study_routes):
        errors.append('Quiz refers to an unregistered trainer route')
    return errors


def check_registries(root=ROOT):
    import check_docs
    import quiz
    import study
    manifest = json.loads((root/'tools/study_core.json').read_text(encoding='utf-8'))
    return registry_errors(manifest, study.EXAMS, check_docs.CERTIFICATION_EXAMS,
                           study.LANGUAGES, quiz.EXAMS, quiz.LANGUAGES)


def run_checks(root=ROOT, checks=CHECKS, runner=None, output=print):
    """Run every check and retain earlier failures even if later checks pass."""
    runner = subprocess.run if runner is None else runner
    environment = os.environ.copy()
    environment['PYTHONDONTWRITEBYTECODE'] = '1'
    failures = []
    for label, arguments in checks:
        output(f'Checking {label}...', flush=True)
        try:
            result = runner([sys.executable, *arguments], cwd=root, env=environment, check=False)
            failed = result.returncode != 0
        except OSError as error:
            output(f'FAIL {label}: {error}')
            failed = True
        if failed:
            failures.append(label)
            output(f'FAIL {label}')
        else:
            output(f'PASS {label}')
    if failures:
        output(f'Verification failed: {len(failures)}/{len(checks)} checks failed.')
        return 1
    output(f'Verification passed: {len(checks)}/{len(checks)} checks, plus registry consistency.')
    return 0


def main(argv=None):
    argparse.ArgumentParser(description=__doc__).parse_args(argv)
    # Imports used for registry checks should not leave local bytecode files.
    sys.dont_write_bytecode = True
    if not shutil.which('bash'):
        print('Bash is required for complete shell checks and lab tests.', file=sys.stderr)
        return 1
    try:
        errors = check_registries()
    except (OSError, ValueError, TypeError, ImportError, AttributeError, SyntaxError) as error:
        print(f'Registry check failed: {error}', file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f'Registry check failed: {error}', file=sys.stderr)
        return 1
    print('PASS route and language registries', flush=True)
    return run_checks()


if __name__ == '__main__':
    sys.exit(main())
