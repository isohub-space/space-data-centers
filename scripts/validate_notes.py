#!/usr/bin/env python3
"""Schema gate for the intel vault.

Checks, over every markdown note under intel/:
  * front-matter present, with `type:` and `tags:`;
  * raw captures (`type: intel`) carry source, url, published (YYYY-MM-DD),
    captured, primary, and the four required sections;
  * raw filenames start with their `published` date;
  * every folder has an `_index.md`;
  * every raw capture is listed in intel/raw/_index.md;
  * every [[wikilink]] resolves to a file in the repo.
Exit 1 on any failure. Run after any edit; CI runs it on every push.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "intel" / "raw"
REQUIRED_SECTIONS = ["## Reported", "## Primary", "## Derived", "## Relevance", "## Promote to"]
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FM = re.compile(r"^---\n(.*?)\n---", re.S)
LINK = re.compile(r"\[\[([^\]|#\\]+)")


def front_matter(text: str) -> dict[str, str] | None:
    m = FM.match(text)
    if not m:
        return None
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def main() -> int:
    errors: list[str] = []
    md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    stems = {str(p.relative_to(ROOT).with_suffix("")) for p in md_files}
    basenames = {p.stem for p in md_files}

    # folders have an index
    for d in {p.parent for p in md_files}:
        if not (d / "_index.md").exists():
            errors.append(f"{d.relative_to(ROOT)}/: missing _index.md")

    raw_index = (RAW / "_index.md").read_text() if (RAW / "_index.md").exists() else ""

    for p in md_files:
        rel = p.relative_to(ROOT)
        text = p.read_text(errors="ignore")
        fm = front_matter(text)
        if fm is None:
            if p.parent == ROOT and p.name in ("CLAUDE.md", "README.md"):
                continue  # repo contracts, not vault notes
            errors.append(f"{rel}: no front-matter")
            continue
        for k in ("type", "tags"):
            if k not in fm:
                errors.append(f"{rel}: front-matter lacks {k}")
        if p.parent == RAW and p.name != "_index.md":
            for k in ("source", "url", "published", "captured", "primary"):
                if not fm.get(k):
                    errors.append(f"{rel}: raw capture lacks {k}")
            pub = fm.get("published", "")
            if not DATE.match(pub):
                errors.append(f"{rel}: published not YYYY-MM-DD")
            elif not p.name.startswith(pub):
                errors.append(f"{rel}: filename does not start with published date {pub}")
            for sec in REQUIRED_SECTIONS:
                if sec not in text:
                    errors.append(f"{rel}: missing section '{sec}'")
            if f"intel/raw/{p.stem}" not in raw_index:
                errors.append(f"{rel}: not listed in intel/raw/_index.md")
        # wikilinks resolve (vault-root path or shortest basename)
        for target in LINK.findall(text):
            t = target.strip()
            if t.endswith("/..."):
                continue  # template placeholder
            if t in stems or f"{t}/_index" in stems or t.split("/")[-1] in basenames:
                continue
            errors.append(f"{rel}: dangling link [[{t}]]")

    for e in errors:
        print(e)
    if errors:
        print(f"{len(errors)} problem(s)", file=sys.stderr)
        return 1
    print(f"validated {len(md_files)} notes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
