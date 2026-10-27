#!/usr/bin/env python3
"""Check repository documents without network access or Azure execution.

Checks relative file links, balanced fenced blocks, ES/EN file parity,
required certification material, and Bash syntax. Does not validate remote URLs,
Markdown anchor fragments, Bicep compilation, or Azure deployment behaviour.
"""
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def check(root):
    errors = []
    links = 0
    shell_blocks = 0
    documents = list(root.rglob("*.md"))
    bash = shutil.which("bash")
    for document in documents:
        text = document.read_text(encoding="utf-8")
        relative = document.relative_to(root)
        lines = text.splitlines()
        fence = None
        prose = []
        code = []
        language = ""
        for line in lines:
            marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
            if marker and fence is None:
                fence = marker.group(1)
                language = marker.group(2).strip()
                code = []
            elif marker and fence is not None and marker.group(1)[0] == fence[0] and len(marker.group(1)) >= len(fence) and not marker.group(2).strip():
                if language == "bash":
                    shell_blocks += 1
                    if bash:
                        result = subprocess.run(
                            [bash, "-n"], input="\n".join(code),
                            text=True, capture_output=True, check=False,
                        )
                        if result.returncode:
                            errors.append(f"{relative}: Bash syntax: {result.stderr.strip()}")
                fence = None
            elif fence is not None:
                code.append(line)
            else:
                prose.append(line)
        if fence is not None:
            errors.append(f"{relative}: unclosed code fence")
        for target in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", "\n".join(prose)):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            links += 1
            path = unquote(target.split("#", 1)[0])
            if path and not (document.parent / path).exists():
                errors.append(f"{relative}: missing linked file: {target}")
    for parent in (root, root / "certifications"):
        for lang, other in (("es", "en"), ("en", "es")):
            for document in (parent / lang).glob("*.md"):
                if not (parent / other / document.name).exists():
                    errors.append(f"Missing {other} counterpart: {document.relative_to(root)}")
    for lang in ("es", "en"):
        for exam in ("AZ-900", "AZ-104", "AZ-305", "AZ-400"):
            for suffix in ("", "-cases"):
                path = root / "certifications" / lang / f"{exam}{suffix}.md"
                if not path.is_file():
                    errors.append(f"Missing certification file: {path.relative_to(root)}")
    if not bash:
        print("Bash not installed: shell syntax checks skipped.")
    print(f"{len(documents)} Markdown files, {links} relative links, {shell_blocks} Bash blocks.")
    for error in errors:
        print(error, file=sys.stderr)
    return bool(errors)


if __name__ == "__main__":
    sys.exit(check(ROOT))
