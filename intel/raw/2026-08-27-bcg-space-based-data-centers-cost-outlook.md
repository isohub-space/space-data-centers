---
type: intel
tags: [sdc, intel/raw, market/sizing, market/sceptics, space/launch, space/orbital-compute]
source: Boston Consulting Group
url: https://www.bcg.com/publications/2026/space-based-data-centers-cost-outlook
author: Val Elbert, Thibault Werlé, Marc Nasr, Clark O'Niell (BCG)
published: 2026-08-27
captured: 2026-10-04
primary: none
---
# BCG — "Space-Based Data Centers: More Than Hype, but Not a Revolution" (cost outlook to 2040)

## Reported (what the source says)
- **20-year TCO per MW today:** space **$660–750M/MW** vs terrestrial **$230–300M/MW** → **2.5–3× premium**.
- 5–10 year trajectory: realistic **1.6–1.8×** premium (depends on failure rates); aggressive **1.1–1.2×** at lowest failure rates. Cost parity "unlikely this decade."
- Launch cost assumptions: current **~$1,500/kg**; target **~$100/kg** (Starship-class reuse).
- "1 GW of compute ≈ **$30 billion** at current costs" (deployment scenario).
- Technical feasibility at scale "within the next five to ten years"; launch readiness 0–2 years; **cooling maturation 5–10 years — the primary bottleneck**.
- Market: by **2040**, orbit-advantaged workloads could take **10–15% of the global AI data-centre market = $240–320B/yr**. Latency-tolerant inference ≈ **40–45%** of the AI data-centre market by 2030.
- Three viable use cases: latency-tolerant inference, sovereign AI workloads, **processing of space-generated data**. Space "complements" terrestrial.

## Primary (where the underlying document differs or adds)
- not checked (no methodology appendix on the page)

## Derived (our arithmetic — formula shown)
- Internal tension: $30B per GW = **$30M/MW** capex, vs $660–750M/MW 20-yr TCO → TCO/capex ≈ 22–25×, implying replacement/ops dominate. Not reconcilable from the page; flag.
- BCG's 2040 revenue figure ($240–320B) is **~10× MarketsandMarkets' $28B for the same year** — different definitions (share of AI compute revenue vs. a "space-based data-centre" product market).

## Relevance to the Entrant
- BCG names "processing of space-generated data" as one of only three use cases that clear the economics — this is the Entrant's category, endorsed by a top-tier consultancy.
- The 1.6–1.8× realistic premium means orbital compute wins only where the data is already in orbit or where latency/sovereignty is worth the premium; EO time-to-insight is the cleanest case.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]]
- [[intel/wiki/orbital-data-center-landscape]]
