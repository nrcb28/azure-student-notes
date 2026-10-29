import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from urllib.parse import quote


PATH = Path(__file__).resolve().parent / 'check_docs.py'
SPEC = importlib.util.spec_from_file_location('check_docs_under_test', PATH)
docs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(docs)


class FragmentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.document = self.root/'index.md'

    def inspect(self, text):
        self.document.write_text(text, encoding='utf-8')
        return docs.check_local_links(self.document, text)

    def test_missing_same_file_anchor_is_rejected(self):
        count, errors = self.inspect('# Intro\n\n[wrong](#absent)\n')
        self.assertEqual(count, 1)
        self.assertEqual(errors, ['missing local fragment: #absent'])

    def test_explicit_html_anchors_and_legacy_names(self):
        count, errors = self.inspect('<a id="Custom-ID"></a>\n<a name="legacy"></a>\n'
                                     '[a](#Custom-ID) [b](#legacy) [c](#custom-id)')
        self.assertEqual(count, 3)
        self.assertEqual(errors, ['missing local fragment: #custom-id'])

    def test_translated_headings_and_percent_encoded_unicode(self):
        for heading in ('設計と復旧', '恢复与验证', 'Восстановление данных', 'Résumé et données'):
            slug = docs.heading_slug(heading)
            with self.subTest(heading=heading):
                _, errors = self.inspect(f'## {heading}\n\n[raw](#{slug}) [encoded](#{quote(slug)})')
                self.assertEqual(errors, [])

    def test_duplicate_heading_suffixes_handle_collisions(self):
        text = '# Recovery\n# Recovery\n# Recovery-1\n'
        text += '[a](#recovery) [b](#recovery-1) [c](#recovery-1-1)'
        _, errors = self.inspect(text)
        self.assertEqual(errors, [])

    def test_fenced_links_and_headings_do_not_count(self):
        text = '# Real\n```markdown\n# Fake\n[broken](missing.md#no)\n```\n[bad](#fake)'
        count, errors = self.inspect(text)
        self.assertEqual(count, 1)
        self.assertEqual(errors, ['missing local fragment: #fake'])

    def test_tilde_fence_and_longer_closing_fence(self):
        count, errors = self.inspect('~~~\n[broken](missing.md)\n~~~~\n# Visible\n[ok](#visible)')
        self.assertEqual((count, errors), (1, []))

    def test_non_markdown_fragment_does_not_require_markdown_anchor(self):
        (self.root/'image.svg').write_text('<svg/>')
        self.assertEqual(self.inspect('[image](image.svg#layer)')[1], [])

    def test_missing_file_reports_file_not_fragment(self):
        self.assertEqual(self.inspect('[missing](absent.md#part)')[1],
                         ['missing linked file: absent.md#part'])

    def test_encoded_path_query_and_angle_destination(self):
        (self.root/'guide français.md').write_text('# Résumé\n', encoding='utf-8')
        _, errors = self.inspect('[encoded](guide%20fran%C3%A7ais.md?raw=1#r%C3%A9sum%C3%A9)\n'
                                 '[angle](<guide français.md#résumé>)')
        self.assertEqual(errors, [])

    def test_formatted_and_setext_headings(self):
        text = '## **Bold** [guide](https://example.com) `code` &amp; data\n\n'
        text += 'Setext title\n============\n\n'
        text += '[a](#bold-guide-code--data) [b](#setext-title)'
        self.assertEqual(self.inspect(text)[1], [])

    def test_remote_and_protocol_relative_urls_are_not_local_files(self):
        self.assertEqual(self.inspect('[a](https://example.com/a#b) [b](//example.com/c#d)'), (0, []))

    def test_full_checker_reports_fragment_defect_in_minimal_repo(self):
        for language in ('es','en','it','de','fr','ru','ja','zh'):
            folder = self.root/language
            folder.mkdir()
            (folder/'15-microsoft-learn.md').write_text('# Learn\n')
            (folder/'README.md').write_text('# Index\n[bad](#missing)\n' if language == 'es' else '# Index\n')
            certs = self.root/'certifications'/language
            certs.mkdir(parents=True)
            for exam in ('AZ-900','AZ-104','AZ-305','AZ-400'):
                for suffix in ('','-cases'):
                    (certs/f'{exam}{suffix}.md').write_text('# Guide\n')
        (self.root/'tools').mkdir()
        (self.root/'tools/learn_topics.json').write_text(json.dumps({'topics':[]}))
        errors = io.StringIO()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(errors):
            result = docs.check(self.root)
        self.assertTrue(result)
        self.assertIn('es/README.md: missing local fragment: #missing', errors.getvalue())


if __name__ == '__main__':
    unittest.main()
