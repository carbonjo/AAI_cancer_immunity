#!/usr/bin/env python3
"""Lint the RESEARCH/wiki OKF bundle: type required, links resolve, orphans listed."""

from __future__ import annotations

import re
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
RESERVED = {"index.md", "log.md"}
FM = re.compile(r"^---\n(.*?)\n---", re.S)
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def concepts() -> dict[Path, str]:
    pages = {}
    for path in WIKI.rglob("*.md"):
        rel = path.relative_to(WIKI)
        if path.name in RESERVED:
            continue
        pages[rel] = path.read_text(encoding="utf-8")
    return pages


def frontmatter_type(text: str) -> str | None:
    match = FM.match(text)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if line.startswith("type:"):
            value = line.split(":", 1)[1].strip()
            return value or None
    return None


def resolve(src: Path, href: str) -> Path | None:
    if href.startswith(("http://", "https://", "mailto:")):
        return None
    href = href.split("#", 1)[0].split("?", 1)[0]
    if not href.endswith(".md"):
        return None
    target = (WIKI / src.parent / href).resolve()
    try:
        return target.relative_to(WIKI.resolve())
    except ValueError:
        return Path(href)


def main() -> int:
    pages = concepts()
    errors: list[str] = []
    inbound: dict[str, int] = {str(p): 0 for p in pages}

    for rel, text in pages.items():
        if frontmatter_type(text) is None:
            errors.append(f"missing type: {rel}")
        for href in LINK.findall(text):
            target = resolve(rel, href)
            if target is None:
                continue
            if target.name in RESERVED:
                if not (WIKI / target).exists():
                    errors.append(f"broken link: {rel} -> {href}")
                continue
            if target in pages:
                inbound[str(target)] += 1
            elif not (WIKI / rel.parent / href).resolve().is_file():
                errors.append(f"broken link: {rel} -> {href}")

    index = (WIKI / "index.md").read_text(encoding="utf-8") if (WIKI / "index.md").exists() else ""
    for href in LINK.findall(index):
        target = resolve(Path("index.md"), href)
        if target is not None and target in pages:
            inbound[str(target)] += 1

    orphans = [p for p, n in sorted(inbound.items()) if n == 0]
    print(f"concepts: {len(pages)}")
    print(f"errors: {len(errors)}")
    for item in errors:
        print(f"  {item}")
    print(f"orphans (no inbound links, including index): {len(orphans)}")
    for item in orphans:
        print(f"  {item}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
