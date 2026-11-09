#!/usr/bin/env python3
"""Audit Markdown image references and committed SVG files (Python stdlib only)."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET

HTML_IMAGE = re.compile(r'<img\b[^>]*?\bsrc\s*=\s*["\']([^"\']+)["\']', re.I | re.S)
MD_IMAGE = re.compile(r'!\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+["\'][^"\']*["\'])?\s*\)', re.S)
EXTERNAL = re.compile(r'^(?:https?:|data:|mailto:|//)', re.I)


def extract_image_links(source: str):
    for match in HTML_IMAGE.finditer(source):
        yield match.group(1).strip()
    for match in MD_IMAGE.finditer(source):
        yield (match.group(1) or match.group(2) or "").strip()


def destination(root: pathlib.Path, document: pathlib.Path, ref: str) -> pathlib.Path | None:
    if not ref or EXTERNAL.match(ref) or ref.startswith("#"):
        return None
    target = urllib.parse.unquote(urllib.parse.urlsplit(ref).path)
    if not target:
        return None
    if target.startswith("/"):
        return root / target.lstrip("/")
    return document.parent / target


def check(root: pathlib.Path):
    markdown = sorted(root.rglob("*.md"))
    vectors = sorted(root.rglob("*.svg"))
    errors = []
    local_checked = 0
    remote_skipped = 0

    for doc in markdown:
        text = doc.read_text(encoding="utf-8", errors="replace")
        for ref in extract_image_links(text):
            target = destination(root, doc, ref)
            if target is None:
                remote_skipped += 1
                continue
            local_checked += 1
            resolved = target.resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append((doc, f"Image reference escapes repository: {ref}"))
                continue
            if not resolved.is_file():
                errors.append((doc, f"Missing local image: {ref}"))
            elif resolved.stat().st_size == 0:
                errors.append((doc, f"Empty image: {ref}"))

    for graphic in vectors:
        try:
            root_element = ET.parse(graphic).getroot()
            if not root_element.tag.endswith("svg"):
                raise ValueError("Root element is not svg")
        except (ET.ParseError, ValueError) as exc:
            errors.append((graphic, f"Invalid SVG XML: {exc}"))

    print(f"Audited {len(markdown)} Markdown files and {len(vectors)} SVG files.")
    print(f"Checked {local_checked} local image references; skipped {remote_skipped} external/data refs.")
    if errors:
        for doc, issue in errors:
            print(f"ERROR {doc.relative_to(root)}: {issue}")
        print(f"FAILED: {len(errors)} image issues.")
        return 1

    print("PASSED: All local Markdown image files exist and all SVG XML parses.")
    print("NOTE: This does not guarantee remote URLs load or that GitHub's renderer displays every SVG.")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path("."))
    args = parser.parse_args()
    return check(args.root.resolve())


if __name__ == "__main__":
    sys.exit(main())
