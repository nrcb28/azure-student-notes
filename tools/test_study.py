import contextlib
import csv
from datetime import datetime, timedelta, timezone
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parent / 'study.py'
spec = importlib.util.spec_from_file_location('study_trainer', SCRIPT)
trainer = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = trainer
spec.loader.exec_module(trainer)
NOW = datetime(2026, 1, 1, 12, tzinfo=timezone.utc)


class TrainerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)/'progress.json'
        self.cards = trainer.load_cards(language='es', exams=('AZ-104',))

    def test_all_banks_have_unique_complete_questions_and_ui(self):
        cards = [card for lang in trainer.LANGUAGES for card in trainer.load_cards(language=lang)]
        self.assertEqual(len(cards), 320)
        self.assertEqual(len({card.id for card in cards}), 320)
        expected = set(trainer.text_for('en'))
        for lang in trainer.LANGUAGES:
            self.assertEqual(set(trainer.text_for(lang)), expected)

    def test_forgotten_answer_returns_in_ten_minutes(self):
        record = trainer.schedule(None, 0, NOW)
        self.assertEqual(trainer.parse_time(record['due']), NOW+timedelta(minutes=10))
        self.assertEqual(record['lapses'], 1)
        self.assertEqual(record['repetitions'], 0)

    def test_successful_reviews_increase_interval_and_hard_resets(self):
        first = trainer.schedule(None, 2, NOW)
        second = trainer.schedule(first, 2, NOW+timedelta(days=1))
        third = trainer.schedule(second, 2, NOW+timedelta(days=4))
        self.assertEqual([first['interval_days'], second['interval_days'], third['interval_days']], [1,3,6])
        hard = trainer.schedule(third, 1, NOW+timedelta(days=10))
        self.assertEqual(hard['repetitions'], 0)
        self.assertEqual(hard['interval_days'], 1)

    def test_due_mode_prioritises_overdue_and_excludes_future(self):
        overdue = trainer.schedule(None, 0, NOW-timedelta(days=1))
        future = trainer.schedule(None, 2, NOW)
        state = {'version':1,'cards':{self.cards[0].id:overdue,self.cards[1].id:future}}
        selected = trainer.select_cards(self.cards[:3], state, NOW)
        self.assertEqual([c.id for c in selected], [self.cards[0].id,self.cards[2].id])

    def test_weak_mode_uses_rated_mistakes_only(self):
        state = {'version':1,'cards':{self.cards[0].id:trainer.schedule(None,0,NOW),
                                    self.cards[1].id:trainer.schedule(None,3,NOW)}}
        self.assertEqual(trainer.select_cards(self.cards[:3],state,NOW,'weak'),[self.cards[0]])

    def test_atomic_round_trip_preserves_non_latin_text(self):
        progress = trainer.Progress(self.path)
        key = 'ja/AZ-104/01'
        progress.state['cards'][key] = trainer.schedule(None, 2, NOW)
        progress.save()
        self.assertEqual(trainer.Progress(self.path).state,progress.state)
        self.assertFalse(self.path.with_name('progress.json.lock').exists())

    def test_corrupt_file_is_never_replaced(self):
        raw = b'{"version":'
        self.path.write_bytes(raw)
        with self.assertRaises(ValueError):
            trainer.Progress(self.path)
        self.assertEqual(self.path.read_bytes(),raw)

    def test_concurrent_session_does_not_lose_saved_reviews(self):
        first = trainer.Progress(self.path)
        second = trainer.Progress(self.path)
        first.state['cards'][self.cards[0].id] = trainer.schedule(None,2,NOW)
        first.save()
        with self.assertRaisesRegex(ValueError,'another session'):
            second.save()
        self.assertEqual(trainer.Progress(self.path).state,first.state)

    def test_existing_lock_is_not_removed_by_another_session(self):
        lock = self.path.with_name('progress.json.lock')
        lock.write_text('existing')
        with self.assertRaises(ValueError):
            trainer.Progress(self.path).save()
        self.assertEqual(lock.read_text(),'existing')
        self.assertFalse(self.path.exists())

    def test_anki_export_escapes_html_and_preserves_unicode(self):
        card = trainer.Card('ja','AZ-104',1,'質問 <script>','答え & details\nnext','certifications/ja/AZ-104-cases.md')
        path = Path(self.temp.name)/'deck.tsv'
        self.assertEqual(trainer.export_anki([card],path),1)
        lines = path.read_text(encoding='utf-8').splitlines()
        rows = list(csv.reader([line for line in lines if not line.startswith('#')],delimiter='\t'))
        self.assertEqual(len(rows),1)
        self.assertEqual(len(rows[0]),3)
        self.assertIn('質問 &lt;script&gt;',rows[0][0])
        self.assertIn('答え &amp; details<br>next',rows[0][1])
        with self.assertRaises(FileExistsError):
            trainer.export_anki([card],path)
        self.assertEqual(len(path.read_text().splitlines()),4)

    def test_interactive_review_saves_one_rating(self):
        with patch('builtins.input',side_effect=['','2']), contextlib.redirect_stdout(io.StringIO()):
            result = trainer.main(['study','--lang','es','--exam','AZ-104','--limit','1','--progress',str(self.path)])
        self.assertEqual(result,0)
        state = trainer.Progress(self.path).state
        self.assertEqual(len(state['cards']),1)
        self.assertEqual(next(iter(state['cards'].values()))['last_grade'],2)

    def test_quitting_before_grading_does_not_create_progress(self):
        with patch('builtins.input',return_value='q'), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(trainer.main(['study','--limit','1','--progress',str(self.path)]),0)
        self.assertFalse(self.path.exists())

    def test_demo_and_stats_are_read_only(self):
        for command in ('demo','stats','plan'):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(trainer.main([command,'--lang','zh','--progress',str(self.path)]),0)
            self.assertFalse(self.path.exists())

    def test_utc_display_works_without_system_timezone_database(self):
        output = io.StringIO()
        with patch.object(trainer, 'ZoneInfo', side_effect=trainer.ZoneInfoNotFoundError), contextlib.redirect_stdout(output):
            self.assertEqual(trainer.main(['demo','--timezone','UTC']),0)
        self.assertIn('UTC',output.getvalue())

    def test_published_decks_match_current_source_cases(self):
        for language in trainer.LANGUAGES:
            target = Path(self.temp.name)/(language+'.tsv')
            trainer.export_anki(trainer.load_cards(language=language),target)
            self.assertEqual(target.read_bytes(),(trainer.ROOT/'flashcards'/(language+'.tsv')).read_bytes())


if __name__ == '__main__':
    unittest.main()
