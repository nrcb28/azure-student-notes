"""Regression tests for failure propagation and inconsistent route registries."""
import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('repository_verify', Path(__file__).with_name('verify.py'))
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class VerificationTests(unittest.TestCase):
    def test_earlier_failure_survives_later_success_and_every_check_runs(self):
        calls = []
        def runner(command, **kwargs):
            calls.append((command, kwargs))
            return subprocess.CompletedProcess(command, 7 if len(calls) == 1 else 0)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = verify.run_checks(checks=(('first', ('first.py',)), ('later', ('later.py',))), runner=runner)
        self.assertEqual(code, 1)
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[0][0], [sys.executable, 'first.py'])
        for _, kwargs in calls:
            self.assertEqual(kwargs['cwd'], verify.ROOT)
            self.assertEqual(kwargs['env']['PYTHONDONTWRITEBYTECODE'], '1')
        self.assertIn('FAIL first', output.getvalue())
        self.assertIn('PASS later', output.getvalue())
        self.assertNotIn('Verification passed', output.getvalue())

    def test_missing_command_is_a_failure_and_does_not_skip_later_checks(self):
        calls = []
        def runner(command, **kwargs):
            calls.append(command)
            if len(calls) == 1:
                raise FileNotFoundError('fixture executable missing')
            return subprocess.CompletedProcess(command, 0)
        with contextlib.redirect_stdout(io.StringIO()):
            result = verify.run_checks(checks=(('missing', ('one.py',)), ('valid', ('two.py',))), runner=runner)
        self.assertEqual(result, 1)
        self.assertEqual(len(calls), 2)

    def test_registry_drift_is_rejected_but_intentionally_smaller_quiz_is_valid(self):
        args = ({'exams': {'AZ-900': [], 'DP-900': []}, 'languages': ['es', 'en']},
                ('AZ-900', 'DP-900'), ('AZ-900', 'DP-900'), ('es', 'en'), ('AZ-900',), ('es', 'en'))
        self.assertEqual(verify.registry_errors(*args), [])
        for index, broken in ((2, ('AZ-900',)), (4, ('SC-999',)),
                              (5, ('en', 'es')), (1, ('AZ-900', 'AZ-900'))):
            changed = list(args)
            changed[index] = broken
            with self.subTest(index=index):
                self.assertTrue(verify.registry_errors(*changed))

    def test_missing_bash_fails_before_claiming_complete_validation(self):
        error = io.StringIO()
        with patch.object(verify.shutil, 'which', return_value=None), patch.object(verify, 'run_checks') as run, contextlib.redirect_stderr(error):
            self.assertEqual(verify.main([]), 1)
        run.assert_not_called()
        self.assertIn('Bash is required', error.getvalue())

    def test_damaged_manifest_fails_cleanly_without_starting_checks(self):
        error = io.StringIO()
        with patch.object(verify, 'check_registries', side_effect=ValueError('invalid JSON')), patch.object(verify, 'run_checks') as run, patch.object(verify.shutil, 'which', return_value='/bin/bash'), contextlib.redirect_stderr(error):
            self.assertEqual(verify.main([]), 1)
        run.assert_not_called()
        self.assertIn('Registry check failed: invalid JSON', error.getvalue())


if __name__ == '__main__':
    unittest.main()
