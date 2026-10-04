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
  tables[]       every markdown table in the wiki: note, section heading,
                 columns, rows (cells with wikilinks reduced to their label)
  sweeps[]       one row per sweep (ISO week of the captures' `captured`
                 date): sources added, cumulative total, added by theme
  latest_sweep   the most recent sweep's ISO week label, e.g. "2026-W40"
  indicators[]   time series from intel/wiki/indicators.md (Observations
                 table): id, unit, points sorted by date with a decimal
                 year `x` for plotting

Everything is derived from the files alone (no git, no clock except the
`generated` stamp), so CI can rebuild it and compare.
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


def clean_cell(cell: str) -> str:
    cell = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", cell)
    cell = re.sub(r"\[\[([^\]|#]+)(#[^\]]*)?\]\]", lambda m: m.group(1).split("/")[-1], cell)
    cell = cell.replace("**", "").replace("\\|", "|")
    return cell.strip()


def tables_in(text: str, note: str) -> list[dict]:
    out = []
    heading = ""
    rows: list[list[str]] = []

    def flush():
        if len(rows) >= 2 and re.match(r"^\s*:?-{2,}", rows[1][0] or "-"):
            cols = rows[0]
            body = [r for r in rows[2:] if any(c for c in r)]
            out.append({"note": note, "section": heading, "columns": cols,
                        "rows": [dict(zip(cols, r + [""] * (len(cols) - len(r)))) for r in body]})

    for line in text.splitlines():
        if line.startswith("#"):
            flush(); rows = []
            heading = re.sub(r"^#+\s*", "", line).strip()
            continue
        if line.strip().startswith("|"):
            cells = [clean_cell(c) for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
            rows.append(cells)
        else:
            flush(); rows = []
    flush()
    return out


def iso_week(date: str) -> str:
    try:
        y, w, _ = dt.date.fromisoformat(date[:10]).isocalendar()
        return f"{y}-W{w:02d}"
    except ValueError:
        return ""


def decimal_year(date: str) -> float | None:
    """YYYY -> mid-year, YYYY-MM -> mid-month, YYYY-MM-DD -> that day."""
    parts = date.strip().split("-")
    try:
        y = int(parts[0])
        if len(parts) == 1:
            return y + 0.5
        m = int(parts[1])
        if len(parts) == 2:
            return y + (m - 0.5) / 12
        d = dt.date(y, m, int(parts[2]))
        start = dt.date(y, 1, 1)
        days = (dt.date(y + 1, 1, 1) - start).days
        return y + (d - start).days / days
    except (ValueError, IndexError):
        return None


def indicator_series(tables: list[dict]) -> list[dict]:
    series: dict[str, dict] = {}
    for t in tables:
        if t["note"] != "indicators" or not t["section"].startswith("Observations"):
            continue
        for r in t["rows"]:
            try:
                value = float(r.get("Value", "").replace(",", ""))
            except ValueError:
                continue
            x = decimal_year(r.get("Date", ""))
            if x is None:
                continue
            key = r.get("Indicator", "").strip()
            s = series.setdefault(key, {"id": key, "unit": r.get("Unit", "").strip(), "points": []})
            s["points"].append({"date": r["Date"].strip(), "x": round(x, 4), "value": value,
                                "kind": r.get("Kind", "").strip(), "note": r.get("Note", "").strip(),
                                "source": r.get("Source", "").strip()})
    for s in series.values():
        s["points"].sort(key=lambda p: p["x"])
    return [series[k] for k in sorted(series)]


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
            "captured": d.get("captured", ""),
            "sweep": iso_week(d.get("captured", "")),
        }
        sources.append(row)
        for t in row["tags"]:
            if t in THEMES:
                by_theme[t] += 1
        by_pub[row["publisher"]] += 1
        by_month[row["date"][:7]] += 1

    wiki = []
    open_items = []
    tables = []
    for p in sorted(WIKI.glob("*.md")):
        if p.name == "_index.md":
            continue
        text = p.read_text(errors="ignore")
        d = fm(text)
        title = re.search(r"^# (.+)$", text, re.M)
        tables.extend(tables_in(text, p.stem))
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

    sweep_rows: dict[str, dict] = {}
    for r in sources:
        if not r["sweep"]:
            continue
        sw = sweep_rows.setdefault(r["sweep"], {"week": r["sweep"], "added": 0, "by_theme": Counter(),
                                                "first_captured": r["captured"], "last_captured": r["captured"]})
        sw["added"] += 1
        sw["first_captured"] = min(sw["first_captured"], r["captured"])
        sw["last_captured"] = max(sw["last_captured"], r["captured"])
        for t in r["tags"]:
            if t in THEMES:
                sw["by_theme"][t] += 1
    sweeps, total = [], 0
    for wk in sorted(sweep_rows):
        sw = sweep_rows[wk]
        total += sw["added"]
        sweeps.append({**sw, "cumulative": total, "by_theme": dict(sorted(sw["by_theme"].items()))})

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
        "tables": tables,
        "sweeps": sweeps,
        "latest_sweep": sweeps[-1]["week"] if sweeps else "",
        "indicators": indicator_series(tables),
    }, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(sources)} sources, {len(wiki)} wiki notes, {len(open_items)} open items, {len(tables)} tables, {len(sweeps)} sweeps, {len(indicator_series(tables))} indicators")


if __name__ == "__main__":
    main()
