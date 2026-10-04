#!/usr/bin/env python3
"""Build intel/output/derived/dashboard.json from the vault.

Derived, regenerable, never authoritative: the notes are the record. The
dashboard page fetches this one file instead of parsing 100+ captures.

Contents
  generated      ISO timestamp
  counts         captures by theme tag, by publisher, by month
  sources[]      one row per raw capture: date, publisher, title, url,
                 tags, primary (verified?) flag, relevance bullets
  wiki[]         one row per wiki note: title, updated, headline bullets
                 (first bullet list), open items (unchecked boxes)
  open_items[]   every "- [ ]" line across the wiki, with its note
"""
from __future__ import annotations

import datetime as dt
import json
import pathlib
import re
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "intel" / "raw"
WIKI = ROOT / "intel" / "wiki"
OUT = ROOT / "intel" / "output" / "derived" / "dashboard.json"
FM = re.compile(r"^---\n(.*?)\n---", re.S)
THEMES = [
    "market/startups", "market/incumbents", "space/launch", "market/sceptics", "market/sizing",
    "market/esa", "market/europe", "space/eo-edge", "space/optical-isl", "research/paper",
    "space/thermal", "space/radiation", "economics/cost-model",
]


def fm(text: str) -> dict:
    m = FM.match(text)
    d: dict = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1)
                d[k.strip()] = v.strip().strip('"')
    d["tags"] = re.findall(r"[\w/.-]+", d.get("tags", "[]"))
    return d


def section(text: str, heading: str) -> str:
    m = re.search(rf"^## {re.escape(heading)}[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else ""


def bullets(block: str, limit: int = 6) -> list[str]:
    out = []
    for line in block.splitlines():
        if line.startswith("- "):
            out.append(re.sub(r"\[\[([^\]|]+)(\|[^\]]+)?\]\]", lambda m: m.group(1).split("/")[-1], line[2:]).strip())
    return out[:limit]


def main() -> None:
    sources = []
    by_theme: Counter = Counter()
    by_pub: Counter = Counter()
    by_month: Counter = Counter()
    for p in sorted(RAW.glob("*.md")):
        if p.name == "_index.md":
            continue
        text = p.read_text(errors="ignore")
        d = fm(text)
        title = re.search(r"^# (.+)$", text, re.M)
        primary = d.get("primary", "")
        row = {
            "id": p.stem,
            "date": d.get("published", ""),
            "publisher": d.get("source", ""),
            "title": title.group(1).strip() if title else p.stem,
            "url": d.get("url", ""),
            "tags": [t for t in d["tags"] if t not in ("intel/raw",)],
            "primary": primary,
            "primary_checked": not re.search(r"not checked|not verified|unverified|snippet|403|paywall", primary + section(text, "Primary"), re.I),
            "relevance": bullets(section(text, "Relevance"), 3),
        }
        sources.append(row)
        for t in row["tags"]:
            if t in THEMES:
                by_theme[t] += 1
        by_pub[row["publisher"]] += 1
        by_month[row["date"][:7]] += 1

    wiki = []
    open_items = []
    for p in sorted(WIKI.glob("*.md")):
        if p.name == "_index.md":
            continue
        text = p.read_text(errors="ignore")
        d = fm(text)
        title = re.search(r"^# (.+)$", text, re.M)
        items = [ln[6:].strip() for ln in text.splitlines() if ln.startswith("- [ ] ")]
        for it in items:
            open_items.append({"note": p.stem, "item": it})
        first_para = re.search(r"\n\n([^#\n][^\n]+(?:\n[^\n#][^\n]+)*)", text.split("---", 2)[-1])
        wiki.append({
            "id": p.stem,
            "title": title.group(1).strip() if title else p.stem,
            "updated": d.get("updated", ""),
            "lede": re.sub(r"\s+", " ", first_para.group(1)) if first_para else "",
            "open_items": items,
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "generated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "counts": {
            "sources": len(sources),
            "by_theme": dict(by_theme.most_common()),
            "by_publisher": dict(by_pub.most_common(25)),
            "by_month": dict(sorted(by_month.items())),
        },
        "sources": sources,
        "wiki": wiki,
        "open_items": open_items,
    }, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(sources)} sources, {len(wiki)} wiki notes, {len(open_items)} open items")


if __name__ == "__main__":
    main()
