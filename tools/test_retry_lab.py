import importlib.util
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[1] / "labs/retry_lab.py"
spec = importlib.util.spec_from_file_location("retry_lab", path)
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)


class RetryBehaviourTests(unittest.TestCase):
    def test_lost_response_repeats_business_effect_without_idempotency(self):
        result = lab.exercise(idempotent=False, attempts=3)
        self.assertTrue(result["completed"])
        self.assertEqual(result["stored_documents"], 2)
        self.assertEqual(result["requests"], 2)

    def test_unique_request_prevents_duplicate_after_committed_write(self):
        result = lab.exercise(idempotent=True, attempts=3)
        self.assertTrue(result["completed"])
        self.assertEqual(result["stored_documents"], 1)

    def test_exhausted_retry_does_not_imply_no_write(self):
        result = lab.exercise(idempotent=True, attempts=1)
        self.assertFalse(result["completed"])
        self.assertEqual(result["stored_documents"], 1)

    def test_permanent_failure_is_not_retried_or_written(self):
        result = lab.exercise(idempotent=True, attempts=5, permanent=True)
        self.assertEqual(result["requests"], 1)
        self.assertEqual(result["stored_documents"], 0)
        self.assertEqual(result["planned_waits"], [])

    def test_invalid_attempt_budget_is_rejected(self):
        with self.assertRaises(ValueError):
            lab.exercise(idempotent=True, attempts=0)


if __name__ == "__main__":
    unittest.main()
