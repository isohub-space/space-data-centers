#!/usr/bin/env python3
"""Fail if any forbidden token appears anywhere in the repository.

This repo is public and describes a *fictitious* entrant. Real people, real
negotiations and private-estate identifiers must never appear, not even by
mistake. The forbidden list is stored as SHA-256 digests of lower-cased
tokens so the list itself never carries the words. Add a token with:

    python3 scripts/check_public_safe.py --add "<token>"

The check tokenises every tracked text file on word boundaries (letters,
digits, hyphen) and also tests a few multi-word phrases over a sliding
window, so "foo-bar" and "foo bar" are both caught. Commit messages are
checked by the CI workflow with the same digests via --stdin.
"""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
DIGESTS = HERE / "forbidden.sha256"
TEXT_EXT = {".md", ".yml", ".yaml", ".json", ".py", ".html", ".css", ".js", ".txt", ".toml"}
WORD = re.compile(r"[a-z0-9][a-z0-9\-]*", re.I)
MAX_PHRASE = 3


def digest(token: str) -> str:
    return hashlib.sha256(token.strip().lower().encode()).hexdigest()


def load_digests() -> set[str]:
    if not DIGESTS.exists():
        return set()
    return {ln.strip() for ln in DIGESTS.read_text().splitlines() if ln.strip() and not ln.startswith("#")}


def tracked_files() -> list[pathlib.Path]:
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout
    return [pathlib.Path(p) for p in out.splitlines() if pathlib.Path(p).suffix in TEXT_EXT]


def scan_text(text: str, bad: set[str]) -> list[tuple[int, str]]:
    hits = []
    for lineno, line in enumerate(text.splitlines(), 1):
        words = [w.lower() for w in WORD.findall(line)]
        for n in range(1, MAX_PHRASE + 1):
            for i in range(len(words) - n + 1):
                phrase = " ".join(words[i : i + n])
                if digest(phrase) in bad:
                    hits.append((lineno, phrase))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--add", metavar="TOKEN", help="append a token's digest to the list")
    ap.add_argument("--stdin", action="store_true", help="scan stdin instead of tracked files")
    args = ap.parse_args()

    if args.add:
        existing = load_digests()
        d = digest(args.add)
        if d not in existing:
            with DIGESTS.open("a") as fh:
                fh.write(d + "\n")
        print("added")
        return 0

    bad = load_digests()
    if not bad:
        print("no forbidden digests configured", file=sys.stderr)
        return 2

    failed = False
    if args.stdin:
        for lineno, phrase in scan_text(sys.stdin.read(), bad):
            print(f"<stdin>:{lineno}: forbidden token ({'*' * len(phrase)})")
            failed = True
    else:
        for path in tracked_files():
            if path == DIGESTS.relative_to(HERE.parent):
                continue
            try:
                text = path.read_text(errors="ignore")
            except OSError:
                continue
            for lineno, phrase in scan_text(text, bad):
                # never print the token itself
                print(f"{path}:{lineno}: forbidden token ({'*' * len(phrase)})")
                failed = True
    if failed:
        print("public-safety check FAILED", file=sys.stderr)
        return 1
    print("public-safety check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
