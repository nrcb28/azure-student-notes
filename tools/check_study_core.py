#!/usr/bin/env python3
"""Structural parity checks; not a linguistic or factual correctness proof."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def check(root):
    manifest = json.loads((root/"tools/study_core.json").read_text(encoding="utf-8"))
    errors = []
    command_source = re.findall(r"```bash\n(.*?)```",
                                (root/"en/17-advanced-labs.md").read_text(encoding="utf-8"), re.S)
    for lang in manifest["languages"]:
        core = root/lang/"16-common-core.md"
        if not core.is_file():
            errors.append(f"{lang}: missing common core")
        else:
            text = core.read_text(encoding="utf-8")
            actual = re.findall(r'<a id="core-([^"]+)"></a>', text)
            if actual != manifest["core_units"]:
                errors.append(f"{lang}: missing or reordered core unit")
        for exam, expected in manifest["exams"].items():
            document = root/"certifications"/lang/f"{exam}-workbook.md"
            if not document.is_file():
                errors.append(f"{lang}/{exam}: missing workbook")
                continue
            text = document.read_text(encoding="utf-8")
            actual = re.findall(r'<a id="([^"]+)"></a>', text)
            if actual != expected:
                errors.append(f"{lang}/{exam}: missing or reordered certification unit")
            sections = re.split(r'<a id="[^"]+"></a>', text)[1:]
            if any(len(section.strip()) < 120 or "\n\n" not in section for section in sections):
                errors.append(f"{lang}/{exam}: empty or underspecified section")
        labs = root/lang/"17-advanced-labs.md"
        if not labs.is_file():
            errors.append(f"{lang}: missing advanced labs")
        else:
            text = labs.read_text(encoding="utf-8")
            actual = re.findall(r'<a id="([^"]+)"></a>', text)
            if actual != manifest["labs"]:
                errors.append(f"{lang}: missing lab step")
            if re.findall(r"```bash\n(.*?)```", text, re.S) != command_source:
                errors.append(f"{lang}: advanced lab commands differ")
    scripts = list((root/"labs").glob("*.sh"))
    bash = shutil.which("bash")
    if scripts and not bash:
        errors.append("Bash is required: standalone lab shell syntax was not checked")
    else:
        for script in scripts:
            result = subprocess.run([bash, "-n", str(script)], text=True, capture_output=True)
            if result.returncode:
                errors.append(f"{script.name}: {result.stderr}")
    for error in errors:
        print(error, file=sys.stderr)
    certification_units = sum(len(units) for units in manifest['exams'].values())
    print(f'{len(manifest["languages"])} languages: {len(manifest["core_units"])} core units, '
          f'{certification_units} certification units across {len(manifest["exams"])} routes, '
          f'{len(manifest["labs"])} advanced-lab sections.')
    return bool(errors)


if __name__ == "__main__":
    sys.exit(check(ROOT))
