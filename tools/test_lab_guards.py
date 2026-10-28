import os
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LabGuardTests(unittest.TestCase):
    def test_recovery_rejects_non_lab_group_before_any_cloud_operation(self):
        env = os.environ.copy()
        env.update(LAB_SUBSCRIPTION="test", LAB_RG="production", LAB_STORAGE="unused")
        result = subprocess.run(["bash", str(ROOT/"labs/blob-recovery.sh")],
                                env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("dedicated", result.stderr)

    def test_access_inspection_rejects_invalid_principal_before_cloud_operation(self):
        env = os.environ.copy()
        env.update(LAB_SUBSCRIPTION="test", LAB_SCOPE="/subscriptions/test/resourceGroups/lab",
                   LAB_PRINCIPAL_ID="not-a-principal-object-id")
        result = subprocess.run(["bash", str(ROOT/"labs/inspect-access.sh")],
                                env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("UUID", result.stderr)


if __name__ == "__main__":
    unittest.main()
