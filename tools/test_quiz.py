"""Behavioural tests for grading, reports, timing and multilingual coverage."""
import contextlib
import copy
from datetime import datetime, timezone
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import render_quiz_docs as quiz_docs

SPEC = importlib.util.spec_from_file_location('azure_quiz', Path(__file__).with_name('quiz.py'))
quiz = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(quiz)
NOW = datetime(2026, 1, 1, tzinfo=timezone.utc)


class QuizTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)/'report.json'
        self.full_bank = quiz.load_bank()
        # Keep session/grading regressions on the original eight-question fixture.
        self.bank = copy.deepcopy([card for card in self.full_bank
                                   if card['id'] in {f'q{number:02d}' for number in range(1, 9)}])
        self.exams = ('AZ-900', 'AZ-104', 'AZ-305', 'AZ-400')
        self.texts = quiz.text_for('en')
        self.questions = quiz.select_questions(self.bank, 'en', self.exams, 8, 42)

    def session(self, replies, questions=None, mode='exam', **kwargs):
        replies = iter(replies)
        return quiz.run_session(questions or self.questions, 'en', mode, kwargs.pop('minutes', None),
                                self.texts, input_fn=lambda _: next(replies), output=kwargs.pop('output', lambda _: None),
                                clock=kwargs.pop('clock', lambda: 0), utcnow=lambda: NOW, **kwargs)

    def answer(self, question, correct=True):
        index = question['variant']['correct']
        if not correct:
            index = (index + 1) % 4
        return quiz.LETTERS[question['order'].index(index)]

    def test_all_eight_languages_have_matching_complete_scenarios_and_ui(self):
        self.assertEqual(len(self.bank), 8)
        self.assertEqual(len(self.full_bank), 34)
        self.assertEqual({q['id'] for q in self.full_bank}, {f'q{number:02d}' for number in range(1, 35)})
        for lang in quiz.LANGUAGES:
            texts = quiz.text_for(lang)
            self.assertEqual(set(texts), set(self.texts))
            self.assertEqual({q['exam'] for q in self.full_bank}, set(quiz.EXAMS))
            self.assertEqual(set(texts['topics']), {q['topic'] for q in self.full_bank})
            for card in self.full_bank:
                self.assertEqual(card['variants'][lang]['correct'], card['variants']['en']['correct'])
        self.assertEqual(sum(len(q['variants']) for q in self.full_bank), 272)

    def test_invalid_ui_templates_are_rejected_before_questions_or_input(self):
        bundle = json.loads((quiz.ROOT/'tools/quiz_ui.json').read_text(encoding='utf-8'))
        question = quiz.select_questions(self.bank, 'en', self.exams, 1, 42)[0]
        templates = ('Incorrect {letter:{0}}', 'Incorrect {letter:{letter}}',
                     'Incorrect {letter:>10}', 'Incorrect {letter:}', 'Incorrect {letter!s}',
                     'Incorrect {}', 'Incorrect {0}', 'Incorrect {letter.real}',
                     'Incorrect {letter[0]}', 'Incorrect {letter',
                     'Incorrect {unknown}', 'Incorrect.')
        for index, template in enumerate(templates):
            # Corrupting English and every translation alike must not change the schema.
            for texts in bundle.values():
                texts['incorrect'] = template
            destination = self.path.with_name(f'invalid-ui-{index}.json')
            output, errors = io.StringIO(), io.StringIO()
            with self.subTest(template=template), \
                    patch.object(Path, 'read_text', return_value=json.dumps(bundle)), \
                    patch.object(quiz, 'load_bank', return_value=self.bank), \
                    patch('builtins.input', return_value=self.answer(question, False)) as input_fn, \
                    contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
                self.assertEqual(quiz.main(['run', '--lang', 'en', '--count', '1', '--seed', '42',
                                            '--report', str(destination)]), 1)
                input_fn.assert_not_called()
                self.assertEqual(output.getvalue(), '')
                self.assertIn('Invalid quiz translation placeholders:', errors.getvalue())
                self.assertFalse(destination.exists())

    def test_malformed_ui_is_reported_cleanly_before_input(self):
        bundle = json.loads((quiz.ROOT/'tools/quiz_ui.json').read_text(encoding='utf-8'))
        malformed = ['{broken', '[]']
        for value in (None, {}, {**bundle['en'], 'topics': None},
                      {**bundle['en'], 'statuses': []}):
            # Validate another language before the malformed English reference.
            broken = {'es': bundle['es'], **bundle, 'en': value}
            malformed.append(json.dumps(broken))
        for raw in malformed:
            errors = io.StringIO()
            with self.subTest(ui=raw[:60]), patch.object(Path, 'read_text', return_value=raw), \
                    patch('builtins.input') as input_fn, contextlib.redirect_stderr(errors):
                with self.assertRaises(ValueError):
                    quiz.text_for('en')
                self.assertEqual(quiz.main(['run', '--lang', 'en', '--report', str(self.path)]), 1)
                input_fn.assert_not_called()
                self.assertTrue(errors.getvalue().startswith('Error:'))
                self.assertFalse(self.path.exists())

    def test_missing_status_in_every_translation_is_rejected_before_input(self):
        messages = json.loads((quiz.ROOT/'tools/quiz_ui.json').read_text(encoding='utf-8'))
        for texts in messages.values():
            del texts['statuses']['quit']
        original_read = Path.read_text
        def read_text(path, *args, **kwargs):
            if path.name == 'quiz_ui.json':
                return json.dumps(messages, ensure_ascii=False)
            return original_read(path, *args, **kwargs)
        with patch.object(Path, 'read_text', read_text), patch('builtins.input', return_value='q') as prompt, contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(quiz.main(['run', '--report', str(self.path)]), 1)
        prompt.assert_not_called()
        self.assertFalse(self.path.exists())

    def test_bank_rejects_missing_variant_duplicate_id_and_invalid_answer(self):
        for change in ('missing', 'duplicate', 'boolean', 'reason', 'reference'):
            with self.subTest(change=change):
                bank = copy.deepcopy(self.full_bank)
                if change == 'missing':
                    del bank[0]['variants']['ja']
                elif change == 'duplicate':
                    bank[1]['id'] = bank[0]['id']
                elif change == 'boolean':
                    bank[0]['variants']['en']['correct'] = True
                elif change == 'reason':
                    bank[0]['variants']['en']['distractors'] = ['', '', '', '']
                else:
                    bank[0]['variants']['en']['source'] = 'https://learn.microsoft.com.attacker.invalid/example'
                with self.assertRaises(ValueError):
                    quiz.validate_bank(bank)

    def test_reference_resolver_supports_legacy_and_certification_guides(self):
        for lang in quiz.LANGUAGES:
            self.assertEqual(quiz.resolve_study_reference('03-compute.md', lang, 'AZ-900'),
                             f'{lang}/03-compute.md')
            self.assertEqual(quiz.resolve_study_reference('certifications/DP-900.md', lang, 'DP-900', quiz.ROOT),
                             f'certifications/{lang}/DP-900.md')

    def test_reference_resolver_rejects_traversal_unregistered_routes_and_mismatch(self):
        invalid = ('../03-compute.md', '/03-compute.md', 'en/03-compute.md',
                   'certifications/en/DP-900.md', 'certifications/../DP-900.md',
                   'certifications/DP-900.md/../AZ-900.md', 'certifications/SC-999.md',
                   'certifications/DP-900.md#section', 'certifications/DP-900.md?x=1',
                   'certifications\\DP-900.md', 'certifications/%2e%2e/DP-900.md')
        for chapter in invalid:
            with self.subTest(chapter=chapter), self.assertRaises(ValueError):
                quiz.resolve_study_reference(chapter, 'en')
        for language, exam in (('../en', 'DP-900'), ('en', 'SC-999'), ('en', 'AZ-104')):
            with self.subTest(language=language, exam=exam), self.assertRaises(ValueError):
                quiz.resolve_study_reference('certifications/DP-900.md', language, exam)

    def test_bank_requires_existing_guides_and_rejects_symlinks_outside_root(self):
        root = self.path.parent/'repository'
        root.mkdir()
        with self.assertRaisesRegex(ValueError, 'Missing local study chapter'):
            quiz.validate_bank(self.full_bank, root=root)
        guide = root/'certifications'/'en'/'DP-900.md'
        guide.parent.mkdir(parents=True)
        self.path.write_text('outside repository', encoding='utf-8')
        guide.symlink_to(self.path)
        with self.assertRaisesRegex(ValueError, 'inside the repository'):
            quiz.resolve_study_reference('certifications/DP-900.md', 'en', 'DP-900', root)

    def test_bank_rejects_exam_mismatch_and_different_translated_references(self):
        bank = copy.deepcopy(self.full_bank)
        for variant in bank[0]['variants'].values():
            variant['chapter'] = 'certifications/DP-900.md'
        with self.assertRaisesRegex(ValueError, 'match the question exam'):
            quiz.validate_bank(bank)
        for field, reference in (('chapter', 'certifications/AZ-900.md'),
                                 ('source', 'https://learn.microsoft.com/en-us/azure/')):
            bank = copy.deepcopy(self.full_bank)
            bank[0]['variants']['ja'][field] = reference
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'references differ'):
                quiz.validate_bank(bank)
        incomplete = [card for card in self.full_bank if card['exam'] != 'DP-900']
        with self.assertRaisesRegex(ValueError, 'all registered exam routes'):
            quiz.validate_bank(incomplete)

    def test_feedback_and_markdown_use_resolved_guides_and_actual_bank_count(self):
        question = copy.deepcopy(self.questions[0])
        question['exam'] = 'DP-900'
        question['variant']['chapter'] = 'certifications/DP-900.md'
        messages = []
        quiz.show_feedback(question, 'en', self.texts, messages.append)
        self.assertIn(self.texts['study'] + ' certifications/en/DP-900.md', messages)
        for lang in quiz.LANGUAGES:
            with self.subTest(language=lang):
                rendered = quiz_docs.render(self.full_bank, lang)
                self.assertIn('34', rendered.splitlines()[0])
                self.assertEqual(rendered.count('<a id="quiz-'), 34)
                self.assertIn(f'](../certifications/{lang}/DP-900.md)', rendered)
                self.assertIn('](03-compute.md)', rendered)
                fixture = quiz_docs.render(self.bank, lang)
                self.assertIn('8', fixture.splitlines()[0])
                self.assertEqual(fixture.count('<a id="quiz-'), 8)

    def test_selection_is_balanced_unique_and_reproducible(self):
        for count in range(1, 9):
            chosen = quiz.select_questions(self.bank, 'es', self.exams, count, 19)
            self.assertEqual(chosen, quiz.select_questions(self.bank, 'es', self.exams, count, 19))
            counts = [sum(q['exam'] == exam for q in chosen) for exam in self.exams]
            self.assertLessEqual(max(counts)-min(counts), 1)
            self.assertEqual(len({q['id'] for q in chosen}), count)
        self.assertNotEqual(self.questions, quiz.select_questions(self.bank, 'en', self.exams, 8, 90))

    def test_full_bank_sampling_is_balanced_and_includes_every_route(self):
        for count in range(1, 35):
            chosen = quiz.select_questions(self.full_bank, 'en', quiz.EXAMS, count, 19)
            self.assertEqual(chosen, quiz.select_questions(self.full_bank, 'en', quiz.EXAMS, count, 19))
            self.assertEqual(len({q['id'] for q in chosen}), count)
            counts = [sum(q['exam'] == exam for q in chosen) for exam in quiz.EXAMS]
            self.assertLessEqual(max(counts)-min(counts), 1)
        self.assertEqual(counts, [2]*17)

    def test_all_seventeen_routes_have_two_distinct_questions_in_every_language(self):
        for lang in quiz.LANGUAGES:
            for exam in quiz.EXAMS:
                with self.subTest(language=lang, exam=exam):
                    chosen = quiz.select_questions(self.full_bank, lang, [exam, exam], 2, 7)
                    self.assertEqual({q['exam'] for q in chosen}, {exam})
                    self.assertEqual(len({q['id'] for q in chosen}), 2)
                    with self.assertRaises(ValueError):
                        quiz.select_questions(self.full_bank, lang, [exam], 3)

    def test_cli_accepts_all_routes_and_defaults_to_two_distinct_questions(self):
        for exam in quiz.EXAMS:
            with self.subTest(exam=exam), patch('builtins.input', return_value='q'), \
                    contextlib.redirect_stdout(io.StringIO()):
                destination = self.path.with_name(f'{exam}.json')
                self.assertEqual(quiz.main(['run', '--lang', 'en', '--exam', exam,
                                            '--report', str(destination)]), 0)
                report = quiz.validate_report(json.loads(destination.read_text(encoding='utf-8')))
                self.assertEqual({q['exam'] for q in report['questions']}, {exam})
                self.assertEqual(len({q['id'] for q in report['questions']}), 2)

    def test_cli_keeps_eight_question_default_and_accepts_explicit_full_bank(self):
        for options, count in (([], 8), (['--count', '34'], 34)):
            with self.subTest(count=count), patch('builtins.input', return_value='q'), \
                    contextlib.redirect_stdout(io.StringIO()):
                destination = self.path.with_name(f'count-{count}.json')
                self.assertEqual(quiz.main(['run', '--lang', 'en', *options,
                                            '--report', str(destination)]), 0)
                report = quiz.validate_report(json.loads(destination.read_text(encoding='utf-8')))
                self.assertEqual(len(report['questions']), count)

    def test_exam_filter_and_explicit_count_never_repeat_questions(self):
        questions = quiz.select_questions(self.bank, 'en', ['AZ-104', 'AZ-104'], 2, 1)
        self.assertEqual({q['exam'] for q in questions}, {'AZ-104'})
        with self.assertRaises(ValueError):
            quiz.select_questions(self.bank, 'en', ['AZ-104'], 3)

    def test_shuffled_letters_are_graded_against_content(self):
        report = self.session([self.answer(q) for q in self.questions])
        self.assertEqual(quiz.summarize(report['questions']),
                         {'correct':8, 'total':8, 'incorrect':0, 'unanswered':0})
        self.assertTrue(any(q['order'] != list(range(4)) for q in self.questions))

    def test_skip_and_quit_keep_unseen_questions_in_denominator(self):
        report = self.session([self.answer(self.questions[0]), 's', self.answer(self.questions[2], False), 'q'])
        self.assertEqual(report['status'], 'quit')
        self.assertEqual(quiz.summarize(report['questions']),
                         {'correct':1, 'total':8, 'incorrect':1, 'unanswered':6})

    def test_empty_reply_skips_without_invalidating_input(self):
        report = self.session(['', 'q'])
        self.assertIsNone(report['questions'][0]['choice'])
        self.assertEqual(quiz.summarize(report['questions'])['unanswered'], 8)

    def test_invalid_input_reprompts_without_losing_current_question(self):
        messages = []
        report = self.session(['Z', 'AA', self.answer(self.questions[0]), 'q'], output=messages.append)
        self.assertEqual(messages.count(self.texts['invalid']), 2)
        self.assertEqual(quiz.summarize(report['questions'])['correct'], 1)

    def test_exam_defers_feedback_while_practice_explains_immediately(self):
        for mode, expected in (('exam', False), ('practice', True)):
            messages = []
            self.session([self.answer(self.questions[0]), 'q'], mode=mode, output=messages.append)
            self.assertEqual(any(self.texts['explanation'] in message for message in messages), expected)

    def test_wrong_answer_feedback_identifies_chosen_option_and_reason(self):
        question = copy.deepcopy(self.questions[0])
        question['choice'] = (question['variant']['correct'] + 1) % 4
        messages = []
        quiz.show_feedback(question, 'en', self.texts, messages.append)
        self.assertTrue(any(question['variant']['options'][question['choice']] in m for m in messages))
        self.assertTrue(any(question['variant']['distractors'][question['choice']] in m for m in messages))

    def test_late_answer_is_rejected_after_input_returns(self):
        elapsed = [0]
        def input_fn(_):
            elapsed[0] = 60
            return self.answer(self.questions[0])
        report = quiz.run_session(self.questions, 'en', 'exam', 1, self.texts,
                                  input_fn=input_fn, output=lambda _: None,
                                  clock=lambda: elapsed[0], utcnow=lambda: NOW)
        self.assertEqual(report['status'], 'timeout')
        self.assertEqual(quiz.summarize(report['questions'])['unanswered'], 8)

    def test_time_limit_also_applies_after_invalid_reply(self):
        elapsed = [0]
        calls = [0]
        def input_fn(_):
            calls[0] += 1
            elapsed[0] += 31
            return 'Z' if calls[0] == 1 else self.answer(self.questions[0])
        report = quiz.run_session(self.questions, 'en', 'exam', 1, self.texts,
                                  input_fn=input_fn, output=lambda _: None,
                                  clock=lambda: elapsed[0], utcnow=lambda: NOW)
        self.assertEqual(report['status'], 'timeout')
        self.assertEqual(calls[0], 2)
        self.assertEqual(quiz.summarize(report['questions'])['correct'], 0)

    def test_keyboard_interrupt_and_eof_keep_completed_choices(self):
        for interrupt in (KeyboardInterrupt(), EOFError()):
            with self.subTest(interrupt=type(interrupt).__name__):
                replies = iter([self.answer(self.questions[0]), interrupt])
                def input_fn(_):
                    reply = next(replies)
                    if isinstance(reply, BaseException):
                        raise reply
                    return reply
                report = quiz.run_session(self.questions, 'en', 'exam', None, self.texts,
                                          input_fn=input_fn, output=lambda _: None,
                                          clock=lambda: 0, utcnow=lambda: NOW)
                self.assertEqual(report['status'], 'interrupted')
                self.assertEqual(quiz.summarize(report['questions'])['correct'], 1)

    def test_snapshots_are_independent_of_bank_and_session_input(self):
        questions = quiz.select_questions(self.bank, 'ja', self.exams, 1, 1)
        report = self.session(['q'], questions=questions)
        original = report['questions'][0]['variant']['question']
        questions[0]['variant']['question'] = 'changed selection'
        for card in self.bank:
            card['variants']['ja']['question'] = 'changed bank'
        self.assertEqual(report['questions'][0]['variant']['question'], original)

    def test_report_unicode_roundtrip_and_exclusive_creation(self):
        questions = quiz.select_questions(self.bank, 'zh', self.exams, 1, 1)
        report = self.session(['q'], questions=questions)
        report['language'] = 'zh'
        quiz.save_report(report, self.path)
        original = self.path.read_bytes()
        self.assertEqual(quiz.validate_report(json.loads(original)), report)
        self.assertIn(questions[0]['variant']['question'], original.decode('utf-8'))
        with self.assertRaises(FileExistsError):
            quiz.save_report(report, self.path)
        self.assertEqual(original, self.path.read_bytes())

    def test_invalid_report_versions_choices_order_and_durations_are_rejected(self):
        report = self.session(['q'])
        changes = [('version', True), ('version', 1.0), ('elapsed_seconds', float('nan')),
                   ('elapsed_seconds', 10**400), ('elapsed_seconds', True), ('limit_seconds', -1)]
        for field, value in changes:
            broken = copy.deepcopy(report)
            broken[field] = value
            with self.subTest(field=field, value=str(value)[:40]), self.assertRaises(ValueError):
                quiz.validate_report(broken)
        for field, value in [('choice', True), ('choice', 4), ('order', [0, 0, 2, 3]), ('order', [False, 1, 2, 3])]:
            broken = copy.deepcopy(report)
            broken['questions'][0][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                quiz.validate_report(broken)

    def test_extreme_or_invalid_timer_is_rejected_before_input(self):
        for minutes in (1e308, float('nan'), float('inf'), -1, 0):
            with self.subTest(minutes=minutes), patch('builtins.input') as input_fn, contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(quiz.main(['run', '--minutes', str(minutes), '--report', str(self.path)]), 1)
                input_fn.assert_not_called()
        self.assertFalse(self.path.exists())

    def test_existing_custom_report_is_rejected_before_questions(self):
        self.path.write_text('preserve me')
        with patch('builtins.input') as input_fn, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(quiz.main(['run', '--report', str(self.path)]), 1)
            input_fn.assert_not_called()
        self.assertEqual(self.path.read_text(), 'preserve me')

    def test_dangling_report_symlink_is_rejected_before_questions(self):
        target = self.path.with_name('missing-report.json')
        self.path.symlink_to(target)
        output, errors = io.StringIO(), io.StringIO()
        with patch('builtins.input', return_value='q') as input_fn, \
                contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            self.assertEqual(quiz.main(['run', '--report', str(self.path)]), 1)
            input_fn.assert_not_called()
        self.assertEqual(output.getvalue(), '')
        self.assertIn('Report already exists:', errors.getvalue())
        self.assertTrue(self.path.is_symlink())
        self.assertEqual(self.path.readlink(), target)
        self.assertFalse(target.exists())

    def test_practice_wrong_answer_feedback_keeps_the_saved_report(self):
        question = quiz.select_questions(self.full_bank, 'en', quiz.EXAMS, 1, 42)[0]
        output = io.StringIO()
        with patch('builtins.input', return_value=self.answer(question, False)), \
                contextlib.redirect_stdout(output):
            self.assertEqual(quiz.main(['run', '--lang', 'en', '--count', '1', '--seed', '42',
                                        '--report', str(self.path)]), 0)
        report = quiz.validate_report(json.loads(self.path.read_text(encoding='utf-8')))
        self.assertEqual(report['status'], 'completed')
        self.assertEqual(quiz.summarize(report['questions']),
                         {'correct': 0, 'total': 1, 'incorrect': 1, 'unanswered': 0})
        letter = quiz.LETTERS[question['order'].index(question['variant']['correct'])]
        self.assertIn(self.texts['incorrect'].format(letter=letter), output.getvalue())

    def test_completed_report_is_saved_before_final_corrections(self):
        with patch('builtins.input', return_value='q'), patch.object(quiz, 'show_summary', side_effect=KeyboardInterrupt), contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(KeyboardInterrupt):
                quiz.main(['run', '--mode', 'exam', '--report', str(self.path)])
        self.assertEqual(quiz.validate_report(json.loads(self.path.read_text()))['status'], 'quit')

    def test_review_recomputes_totals_without_loading_changed_bank(self):
        report = self.session([self.answer(self.questions[0]), 'q'])
        report['score'] = {'correct':999}
        quiz.save_report(report, self.path)
        output = io.StringIO()
        with patch.object(quiz, 'load_bank', side_effect=AssertionError('must use snapshots')), contextlib.redirect_stdout(output):
            self.assertEqual(quiz.main(['review', '--report', str(self.path), '--lang', 'ja', '--json']), 0)
        self.assertEqual(json.loads(output.getvalue()), {'correct':1,'total':8,'incorrect':0,'unanswered':7})

    def test_review_supports_legacy_and_certification_snapshots_without_current_guides_or_bank(self):
        for chapter, exam, expected in (('99-retired-guide.md', 'AZ-900', 'en/99-retired-guide.md'),
                                        ('certifications/DP-900.md', 'DP-900', 'certifications/en/DP-900.md')):
            report = self.session(['q'])
            report['questions'] = report['questions'][:1]
            report['questions'][0]['exam'] = exam
            report['questions'][0]['variant']['chapter'] = chapter
            destination = self.path.with_name(f'{exam}-snapshot.json')
            quiz.save_report(report, destination)
            output = io.StringIO()
            with self.subTest(chapter=chapter), \
                    patch.object(quiz, 'load_bank', side_effect=AssertionError('must use snapshots')), \
                    patch.object(Path, 'is_file', side_effect=AssertionError('saved reports do not require current guides')), \
                    contextlib.redirect_stdout(output):
                self.assertEqual(quiz.main(['review', '--report', str(destination), '--lang', 'ja', '--all']), 0)
                self.assertIn(expected, output.getvalue())

    def test_report_rejects_unsafe_and_mismatched_references(self):
        for chapter in ('../03-compute.md', 'certifications/SC-999.md', 'certifications/DP-900.md'):
            report = self.session(['q'])
            report['questions'][0]['exam'] = 'AZ-900'
            report['questions'][0]['variant']['chapter'] = chapter
            with self.subTest(chapter=chapter), self.assertRaises(ValueError):
                quiz.validate_report(report)

    def test_corrupt_review_report_is_preserved_and_reports_error(self):
        self.path.write_text('{broken')
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(quiz.main(['review', '--report', str(self.path)]), 1)
        self.assertEqual(self.path.read_text(), '{broken')

    def test_demo_and_doctor_are_read_only_in_every_language(self):
        default_dir = quiz.ROOT/'.study-reports'
        before = set(default_dir.glob('*'))
        for lang in quiz.LANGUAGES:
            for command in ('demo', 'doctor'):
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(quiz.main([command, '--lang', lang]), 0)
        self.assertEqual(set(default_dir.glob('*')), before)


if __name__ == '__main__':
    unittest.main()
