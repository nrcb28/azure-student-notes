import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
PRINCIPAL = "12345678-abcd-1234-abcd-123456789abc"

# Every shell test uses this local stand-in, even when testing rejection before
# the first CLI call. A broken guard must never contact an installed Azure CLI.
FAKE_AZ = r'''
import json
import os
from pathlib import Path
import shutil
import sys

args = sys.argv[1:]
with open(os.environ["LAB_TEST_AZ_LOG"], "a") as log:
    log.write(json.dumps(args) + "\n")

def option(name):
    return args[args.index(name) + 1]

def boolean(value):
    if os.environ.get("LAB_TEST_BOOL_CASE") == "title":
        return str(value)
    return str(value).lower()

def setting(name, default):
    value = os.environ.get(name, default)
    return boolean(value == "true") if value in ("true", "false") else value

blob = Path(os.environ["LAB_TEST_BLOB"])
deleted_blob = blob.with_suffix(".deleted")

if args[:2] == ["group", "show"]:
    print(os.environ.get("LAB_TEST_ENVIRONMENT", "lab"))
elif args[:3] == ["storage", "account", "show"]:
    if option("--query") == "isHnsEnabled":
        print(setting("LAB_TEST_HNS", "false"))
    else:
        print("/subscriptions/test/resourceGroups/rg-notes-recovery-test/providers/Microsoft.Storage/storageAccounts/labstorage")
elif args[:4] == ["storage", "account", "blob-service-properties", "show"]:
    if option("--query") == "deleteRetentionPolicy.enabled":
        print(setting("LAB_TEST_SOFT_DELETE", "true"))
    else:
        print(setting("LAB_TEST_VERSIONING", "false"))
elif args[:3] == ["storage", "container", "create"]:
    print(boolean(os.environ.get("LAB_TEST_CONTAINER_EXISTS") != "true"))
elif args[:3] == ["storage", "blob", "upload"]:
    shutil.copyfile(option("--file"), blob)
elif args[:3] == ["storage", "blob", "delete"]:
    blob.rename(deleted_blob)
elif args[:3] == ["storage", "blob", "undelete"]:
    deleted_blob.rename(blob)
elif args[:3] == ["storage", "blob", "download"]:
    if os.environ.get("LAB_TEST_CORRUPT_DOWNLOAD") == "true":
        Path(option("--file")).write_text("corrupt download")
    else:
        shutil.copyfile(blob, option("--file"))
elif args[:3] == ["storage", "container", "delete"]:
    blob.unlink(missing_ok=True)
    deleted_blob.unlink(missing_ok=True)
elif args[:2] == ["account", "show"]:
    pass
elif args[:3] == ["role", "assignment", "list"]:
    if "principalId=='" + os.environ["LAB_TEST_PRINCIPAL"] + "'" in option("--query"):
        print("Reader  /subscriptions/test/resourceGroups/lab")
else:
    sys.exit("Unexpected fake az command: " + repr(args))
'''


class LabGuardTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self.scratch.cleanup)
        directory = Path(self.scratch.name)
        cli = directory / "az"
        cli.write_text(f"#!{sys.executable}\n" + FAKE_AZ)
        cli.chmod(0o700)
        self.log = directory / "commands.jsonl"
        self.blob = directory / "blob"
        self.env = os.environ.copy()
        self.env.update(
            PATH=str(directory) + os.pathsep + self.env.get("PATH", ""),
            LAB_SUBSCRIPTION="test", LAB_RG="rg-notes-recovery-test",
            LAB_STORAGE="labstorage", LAB_SCOPE="/subscriptions/test/resourceGroups/lab",
            LAB_PRINCIPAL_ID=PRINCIPAL, LAB_TEST_PRINCIPAL=PRINCIPAL,
            LAB_TEST_AZ_LOG=str(self.log), LAB_TEST_BLOB=str(self.blob),
        )

    def run_lab(self, script, **environment):
        return subprocess.run(
            ["bash", str(ROOT / "labs" / script)],
            env={**self.env, **environment}, capture_output=True, text=True,
        )

    def commands(self):
        if not self.log.exists():
            return []
        return [json.loads(line) for line in self.log.read_text().splitlines()]

    def assert_no_data_operations(self):
        for command in self.commands():
            self.assertNotIn(command[:2], [["storage", "container"], ["storage", "blob"]])

    def test_recovery_rejects_non_lab_group_before_any_cloud_operation(self):
        result = self.run_lab("blob-recovery.sh", LAB_RG="production")
        self.assertEqual(result.returncode, 2)
        self.assertIn("dedicated", result.stderr)
        self.assertEqual(self.commands(), [])

    def test_recovery_requires_lab_tag_before_data_operations(self):
        result = self.run_lab("blob-recovery.sh", LAB_TEST_ENVIRONMENT="production")
        self.assertEqual(result.returncode, 2)
        self.assertIn("environment=lab", result.stderr)
        self.assert_no_data_operations()

    def test_recovery_accepts_both_cli_boolean_spellings(self):
        for spelling in ("lower", "title"):
            with self.subTest(spelling=spelling):
                self.log.unlink(missing_ok=True)
                result = self.run_lab("blob-recovery.sh", LAB_TEST_BOOL_CASE=spelling)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("RECOVERY_OK", result.stdout)
                operations = [command[:3] for command in self.commands()
                              if command[:2] in (["storage", "container"], ["storage", "blob"])]
                self.assertEqual(operations, [
                    ["storage", "container", "create"],
                    ["storage", "blob", "upload"],
                    ["storage", "blob", "delete"],
                    ["storage", "blob", "undelete"],
                    ["storage", "blob", "download"],
                    ["storage", "container", "delete"],
                ])
                self.assertFalse(self.blob.exists())

    def test_recovery_rejects_hierarchical_namespace_before_data_operations(self):
        for hns in ("true", "", "unknown"):
            with self.subTest(hns=hns):
                self.log.unlink(missing_ok=True)
                result = self.run_lab("blob-recovery.sh", LAB_TEST_HNS=hns)
                self.assertEqual(result.returncode, 2)
                self.assertIn("hierarchical namespace", result.stderr)
                self.assert_no_data_operations()

    def test_recovery_requires_explicit_protection_settings_before_data_operations(self):
        for setting, value in (("LAB_TEST_SOFT_DELETE", "false"),
                               ("LAB_TEST_SOFT_DELETE", ""),
                               ("LAB_TEST_VERSIONING", "true"),
                               ("LAB_TEST_VERSIONING", "")):
            with self.subTest(setting=setting, value=value):
                self.log.unlink(missing_ok=True)
                result = self.run_lab("blob-recovery.sh", **{setting: value})
                self.assertEqual(result.returncode, 2)
                self.assertIn("Requires soft delete", result.stderr)
                self.assert_no_data_operations()

    def test_recovery_does_not_touch_a_preexisting_container(self):
        self.blob.write_bytes(b"existing data")
        result = self.run_lab("blob-recovery.sh", LAB_TEST_CONTAINER_EXISTS="true")
        self.assertEqual(result.returncode, 2)
        self.assertIn("already existed", result.stderr)
        operations = [command[:3] for command in self.commands()]
        self.assertNotIn(["storage", "blob", "upload"], operations)
        self.assertNotIn(["storage", "container", "delete"], operations)
        self.assertEqual(self.blob.read_bytes(), b"existing data")

    def test_recovery_preserves_synthetic_data_when_verification_fails(self):
        result = self.run_lab("blob-recovery.sh", LAB_TEST_CORRUPT_DOWNLOAD="true")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("RECOVERY_OK", result.stdout)
        self.assertIn("Created synthetic recovery container: lab-recovery-", result.stdout)
        self.assertEqual(self.blob.read_bytes(), b"Synthetic university notes: recovery exercise.\n")
        self.assertNotIn(["storage", "container", "delete"],
                         [command[:3] for command in self.commands()])

    def test_access_inspection_rejects_invalid_principal_before_cloud_operation(self):
        result = self.run_lab("inspect-access.sh", LAB_PRINCIPAL_ID="not-a-principal-object-id")
        self.assertEqual(result.returncode, 2)
        self.assertIn("UUID", result.stderr)
        self.assertEqual(self.commands(), [])

    def test_access_inspection_accepts_uppercase_principal(self):
        result = self.run_lab("inspect-access.sh", LAB_PRINCIPAL_ID=PRINCIPAL.upper())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Reader", result.stdout)

    def test_access_inspection_rejects_different_subscription_before_cloud_operation(self):
        result = self.run_lab("inspect-access.sh", LAB_SCOPE="/subscriptions/other/resourceGroups/lab")
        self.assertEqual(result.returncode, 2)
        self.assertIn("supplied subscription", result.stderr)
        self.assertEqual(self.commands(), [])


if __name__ == "__main__":
    unittest.main()
