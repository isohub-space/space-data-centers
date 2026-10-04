---
type: index
tags: [sdc, dashboard]
---
# dashboard/

- `index.html` — the Orbital Compute Atlas: a single-file page that reads
  `intel/output/derived/dashboard.json` (relative when served from the repo, from
  raw.githubusercontent.com otherwise) and draws the vault's own tables. Charts are plain
  SVG; nothing numeric is typed into the page. Serve the repo root (or enable GitHub Pages)
  and open `dashboard/`.
