import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('study_core_checker', Path(__file__).with_name('check_study_core.py'))
core = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(core)


class CorePrerequisiteTests(unittest.TestCase):
    def test_missing_bash_reports_unchecked_scripts_instead_of_crashing_or_passing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'tools').mkdir()
            (root/'en').mkdir()
            (root/'labs').mkdir()
            (root/'tools/study_core.json').write_text(json.dumps(
                {'languages': [], 'core_units': [], 'exams': {}, 'labs': []}), encoding='utf-8')
            (root/'en/17-advanced-labs.md').write_text('# Reference\n', encoding='utf-8')
            (root/'labs/example.sh').write_text('#!/bin/bash\ntrue\n', encoding='utf-8')
            output = io.StringIO()
            with patch.object(core.shutil, 'which', return_value=None), patch.object(core.subprocess, 'run') as run, contextlib.redirect_stderr(output), contextlib.redirect_stdout(io.StringIO()):
                self.assertTrue(core.check(root))
            run.assert_not_called()
            self.assertIn('standalone lab shell syntax was not checked', output.getvalue())


if __name__ == '__main__':
    unittest.main()
