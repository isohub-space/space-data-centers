# space-data-centers
Data centers for space applications

A public, weekly-updated intelligence vault on **orbital data centres** — launch economics,
in-orbit compute, EO edge processing, competitors, programmes, funding — written to answer
one question for a *fictitious* European entrant: **where is a defensible position in this
market?**

- Start at [`_index.md`](_index.md); read the four wiki notes in `intel/wiki/`.
- Every figure is labelled *reported / primary / derived* and linked to its capture in
  `intel/raw/` (one note per source).
- `intel/output/derived/dashboard.json` is regenerated from the notes by
  `scripts/build_dashboard.py`; `dashboard/index.html` (the Orbital Compute Atlas) draws it.
- Maintained by `.github/workflows/weekly-intel.yml` (Claude Code sweeps the week's sources
  and opens a PR); gated by `.github/workflows/validate.yml`.

Agent rules: [`CLAUDE.md`](CLAUDE.md).
