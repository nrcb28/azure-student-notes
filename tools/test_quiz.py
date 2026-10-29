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

SPEC = importlib.util.spec_from_file_location('azure_quiz', Path(__file__).with_name('quiz.py'))
quiz = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(quiz)
NOW = datetime(2026, 1, 1, tzinfo=timezone.utc)


class QuizTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)/'report.json'
        self.bank = quiz.load_bank()
        self.texts = quiz.text_for('en')
        self.questions = quiz.select_questions(self.bank, 'en', quiz.EXAMS, 8, 42)

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
        for lang in quiz.LANGUAGES:
            texts = quiz.text_for(lang)
            self.assertEqual(set(texts), set(self.texts))
            self.assertEqual({q['exam'] for q in self.bank}, set(quiz.EXAMS))
            self.assertEqual(set(texts['topics']), {q['topic'] for q in self.bank})
            for card in self.bank:
                self.assertEqual(card['variants'][lang]['correct'], card['variants']['en']['correct'])
        self.assertEqual(sum(len(q['variants']) for q in self.bank), 64)

    def test_bank_rejects_missing_variant_duplicate_id_and_invalid_answer(self):
        for change in ('missing', 'duplicate', 'boolean', 'reason', 'reference'):
            with self.subTest(change=change):
                bank = copy.deepcopy(self.bank)
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

    def test_selection_is_balanced_unique_and_reproducible(self):
        for count in range(1, 9):
            chosen = quiz.select_questions(self.bank, 'es', quiz.EXAMS, count, 19)
            self.assertEqual(chosen, quiz.select_questions(self.bank, 'es', quiz.EXAMS, count, 19))
            counts = [sum(q['exam'] == exam for q in chosen) for exam in quiz.EXAMS]
            self.assertLessEqual(max(counts)-min(counts), 1)
            self.assertEqual(len({q['id'] for q in chosen}), count)
        self.assertNotEqual(self.questions, quiz.select_questions(self.bank, 'en', quiz.EXAMS, 8, 90))

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
        questions = quiz.select_questions(self.bank, 'ja', quiz.EXAMS, 1, 1)
        report = self.session(['q'], questions=questions)
        original = report['questions'][0]['variant']['question']
        questions[0]['variant']['question'] = 'changed selection'
        for card in self.bank:
            card['variants']['ja']['question'] = 'changed bank'
        self.assertEqual(report['questions'][0]['variant']['question'], original)

    def test_report_unicode_roundtrip_and_exclusive_creation(self):
        questions = quiz.select_questions(self.bank, 'zh', quiz.EXAMS, 1, 1)
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
