---
type: intel
tags: [sdc, intel/raw, market/europe, market/esa, space/orbital-compute, space/eu-programmes]
source: Thales Alenia Space (company news page)
url: https://www.thalesaleniaspace.com/en/news/ascend-new-alternative-terrestrial-datacenters
author: Thales Alenia Space
published: 2023-12-12
captured: 2026-10-04
primary: none (study kick-off communication; the study itself is Horizon Europe-funded)
---
# ASCEND: a new alternative to terrestrial datacenters (study kick-off framing)

## Reported (what the source says)
- Thales Alenia Space "has been coordinating a consortium of **11 partners** since **January 2023**" under the **Horizon Europe** framework programme (2021–2027).
- Sizing assumptions: **"10 MW per space datacenter is envisaged"**; overall target **10 TWh**; solar array **"about 35,000 square meters"** per data centre (vs ISS ~7,500 m²).
- Framing: European terrestrial data centres projected to emit **"20 million tonnes of CO₂ equivalent a year between now and 2050"**; ASCEND's stated goal is to "cut the energy requirements of Earth-based datacenters by **10%**".
- Results were "due in **April 2024**" (actually released 27 June 2024 — see [[2024-06-27-thales-alenia-ascend-feasibility-results]]).
- No orbit, module count, or budget stated.

## Primary (where the underlying document differs or adds)
- not checked (no public study report)

## Derived (our arithmetic — formula shown)
- 10 TWh/yr ÷ 8,760 h ≈ **1.14 GW average** — consistent with the 1 GW headline in the June-2024 results.
- 35,000 m² × ~200 W/m² (typical triple-junction array at EOL, our assumption) ≈ **7 MW** — i.e. the 10 MW module implies either higher-efficiency cells or the array figure is end-of-life-padded. Order of magnitude holds.
- 10 MW per module is **~1,000× the power class** of today's EO edge-compute payloads (Unibap iX10 <40 W; KP Labs Leopard 5–20 W; EDGX Morus class ~100s of W). The gap between "edge processing on an EO satellite" and "ASCEND" is three orders of magnitude.

## Relevance to the Entrant
- Establishes the **power-class vocabulary**: ASCEND = 10 MW modules; EO edge = tens of watts. The Entrant's "in-orbit data centre for EO time-to-insight" sits at the small end and should not borrow ASCEND's gigawatt rhetoric.
- The 10%-of-terrestrial-energy ambition is the European policy hook (Green Deal); a startup can cite it, but the credible near-term value is latency and downlink relief, not carbon.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
