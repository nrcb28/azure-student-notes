#!/usr/bin/env python3
"""Check repository documents without network access or Azure execution.

Checks local file links and Markdown fragments, balanced fenced blocks,
eight-language file parity, required certification material, and Bash syntax.
Does not validate remote URLs, Bicep compilation, or Azure deployment behaviour.
"""
from pathlib import Path
from html import unescape
from html.parser import HTMLParser
import re
import json
import shutil
import subprocess
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def prose_lines(text):
    """Keep line positions while hiding fenced blocks from links and headings."""
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence is None and marker:
            fence = marker.group(1)
            yield ""
        elif fence is not None:
            if (marker and marker.group(1)[0] == fence[0]
                    and len(marker.group(1)) >= len(fence)
                    and not marker.group(2).strip()):
                fence = None
            yield ""
        else:
            yield line


class _ExplicitAnchors(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value and (name == "id" or (tag == "a" and name == "name")):
                self.anchors.add(value)

    handle_startendtag = handle_starttag


def heading_slug(heading):
    """GitHub-style slug for ordinary Markdown headings, including Unicode."""
    heading = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", heading)
    heading = re.sub(r"<[^>]*>", "", heading)
    heading = re.sub(r"(?<!\w)_{1,2}(.+?)_{1,2}(?!\w)", r"\1", heading)
    heading = unescape(heading).strip().lower()
    heading = "".join(char for char in heading if char in "-_" or
                      unicodedata.category(char)[0] not in "PSC")
    return re.sub(r"\s", "-", heading)


def markdown_anchors(text):
    lines = list(prose_lines(text))
    parser = _ExplicitAnchors()
    parser.feed("\n".join(lines))
    anchors = set(parser.anchors)
    generated = set()
    for index, line in enumerate(lines):
        match = re.match(r"^ {0,3}#{1,6}(?:[ \t]+|$)(.*)$", line)
        if match:
            title = re.sub(r"[ \t]+#+[ \t]*$", "", match.group(1))
        elif (line.strip() and index + 1 < len(lines)
              and re.fullmatch(r" {0,3}(?:=+|-+)[ \t]*", lines[index + 1])):
            title = line.strip()
        else:
            continue
        base = heading_slug(title)
        slug, suffix = base, 0
        while slug in generated:
            suffix += 1
            slug = f"{base}-{suffix}"
        generated.add(slug)
        anchors.add(slug)
    return anchors


def check_local_links(document, text, anchor_cache=None):
    """Validate ordinary inline local destinations; never fetch remote links."""
    anchor_cache = {} if anchor_cache is None else anchor_cache
    errors = []
    count = 0
    prose = "\n".join(prose_lines(text))
    pattern = r'''!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+["'][^"']*["'])?\s*\)'''
    for angled, bare in re.findall(pattern, prose):
        target = angled or bare
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        count += 1
        path = unquote(parsed.path)
        destination = (document.parent / path).resolve() if path else document.resolve()
        if not destination.exists():
            errors.append(f"missing linked file: {target}")
            continue
        fragment = unquote(parsed.fragment)
        if not fragment or destination.suffix.lower() not in (".md", ".markdown"):
            continue
        if not destination.is_file():
            errors.append(f"missing linked file: {target}")
            continue
        if destination not in anchor_cache:
            anchor_cache[destination] = markdown_anchors(destination.read_text(encoding="utf-8"))
        if fragment not in anchor_cache[destination]:
            errors.append(f"missing local fragment: {target}")
    return count, errors


def check(root):
    errors = []
    links = 0
    shell_blocks = 0
    documents = list(root.rglob("*.md"))
    anchor_cache = {}
    bash = shutil.which("bash")
    for document in documents:
        text = document.read_text(encoding="utf-8")
        relative = document.relative_to(root)
        if "[object Object]" in text:
            errors.append(f"{relative}: unresolved generated label")
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
        count, link_errors = check_local_links(document, text, anchor_cache)
        links += count
        errors.extend(f"{relative}: {error}" for error in link_errors)
    languages = ("es", "en", "it", "de", "fr", "ru", "ja", "zh")
    for parent in (root, root / "certifications"):
        expected = {p.name for p in (parent / "en").glob("*.md")}
        for lang in languages:
            actual = {p.name for p in (parent / lang).glob("*.md")}
            for name in sorted(expected - actual):
                errors.append(f"Missing {lang} counterpart: {parent.relative_to(root)}/{name}")
            for name in sorted(actual - expected):
                errors.append(f"Unexpected {lang} file without English counterpart: {name}")
    for lang in languages:
        for exam in ("AZ-900", "AZ-104", "AZ-305", "AZ-400"):
            for suffix in ("", "-cases"):
                path = root / "certifications" / lang / f"{exam}{suffix}.md"
                if not path.is_file():
                    errors.append(f"Missing certification file: {path.relative_to(root)}")
    # Newly adapted editions preserve English command blocks, including comments.
    # Existing Spanish examples have their own localised comments.
    for lang in ("it", "de", "fr", "ru", "ja", "zh"):
        for path in ("en/13-laboratorios.md", "certifications/en/network-lab.md"):
            source = root / path
            target = root / path.replace("/en/", f"/{lang}/") if "/en/" in path else root / path.replace("en/", f"{lang}/", 1)
            if not source.is_file() or not target.is_file():
                continue
            pattern = r"```bash\n(.*?)```"
            expected = re.findall(pattern, source.read_text(encoding="utf-8"), re.S)
            actual = re.findall(pattern, target.read_text(encoding="utf-8"), re.S)
            if actual != expected:
                errors.append(f"{target.relative_to(root)}: lab commands differ from English")
    # Verify the new source-backed topic set in every edition.
    manifest_path = root / "tools/learn_topics.json"
    if not manifest_path.is_file():
        errors.append("Missing Learn topic manifest")
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for lang in languages:
            module = root / lang / "15-microsoft-learn.md"
            if not module.is_file():
                errors.append(f"Missing Learn expansion: {lang}")
                continue
            text = module.read_text(encoding="utf-8")
            for topic in manifest["topics"]:
                anchor = f'learn-{topic["id"]}'
                if f'id="{anchor}"' not in text or topic["url"] not in text:
                    errors.append(f"{lang}: missing Learn topic or source: {topic['id']}")
                for chapter in topic["chapters"]:
                    target = root / lang / f"{chapter}.md"
                    if not target.is_file() or f"15-microsoft-learn.md#{anchor}" not in target.read_text(encoding="utf-8"):
                        errors.append(f"{lang}: topic not integrated into {chapter}: {topic['id']}")
                for exam in topic["exams"]:
                    target = root / "certifications" / lang / f"{exam}.md"
                    if not target.is_file() or f"15-microsoft-learn.md#{anchor}" not in target.read_text(encoding="utf-8"):
                        errors.append(f"{lang}: topic not integrated into {exam}: {topic['id']}")
    if not bash:
        print("Bash not installed: shell syntax checks skipped.")
    print(f"{len(documents)} Markdown files, {links} relative links, {shell_blocks} Bash blocks.")
    for error in errors:
        print(error, file=sys.stderr)
    return bool(errors)


if __name__ == "__main__":
    sys.exit(check(ROOT))
