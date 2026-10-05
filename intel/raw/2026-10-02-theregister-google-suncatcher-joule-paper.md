---
type: intel
tags: [sdc, intel/raw, market/incumbents, company/google, space/launch, economics/cost-model]
source: The Register
url: https://theregister.com/systems/2026/10/02/google-launches-first-datacenter-satellite-and-research-that-finds-orbiting-bit-barns-can-work/5300721
author: The Register (staff)
published: 2026-10-02
captured: 2026-10-05
primary: "Joule paper 'Toward a future space-based, highly scalable AI infrastructure system design' (cell.com/joule/fulltext/S2542-4351(26)00362-4) — HTTP 403 again on 2026-10-05, not read. arXiv preprint 2511.19468 is in the vault."
---
# The Register — Google launches first datacenter satellite, and research that finds orbiting bit barns can work

## Reported (what the source says)
- Reports the Suncatcher prototype launch alongside the **peer-reviewed paper in *Joule***,
  "Toward a future space-based, highly scalable AI infrastructure system design".
- Figures attributed to the paper: viability threshold **$200/kg** launch; SpaceX price falls
  **20% per doubling of cumulative mass**; **370,000 t** additional cumulative mass needed ≈
  **~1,800 Starship launches**; components reused **100 times**.
- Starlink v2 (mini) mass **575 kg** used as the bus proxy; the paper identifies formation flight
  tighter than any current constellation and inter-satellite networking as unsolved; cites
  NASA's TBIRD reaching **200 Gbps** LEO-to-ground.

## Primary (what the underlying paper / filing says — where it differs)
- Joule page not readable (403). The arXiv preprint
  ([[intel/raw/2025-11-22-arxiv-google-suncatcher-system-design]]) gives the Starship bottom-up
  cost "≲ $60/kg at **10×** reuse"; The Register's **100×** reuse may be a different scenario in the
  Joule version or a misreport — unresolved.

## Derived (our arithmetic — formula shown)
- 370,000 t / 1,800 launches ≈ **206 t per launch** — consistent with the 200 t Starship payload
  assumption already in [[intel/wiki/orbital-compute-launch-economics]].
- Against demonstrated tonnage (~115 t in 2026 to date,
  [[intel/raw/2026-09-28-wikipedia-starship-launch-list-cadence]]): 370,000 / 115 ≈ **3,200 years**
  at 2026 pace (our arithmetic; illustrates the gap, not a forecast).

## Relevance to the Entrant
- Second independent outlet now reports 370,000 t / ~1,800 launches from the peer-reviewed
  version — the figure is stable between preprint coverage and journal, though still not read
  at source.
- Nothing here moves the kW-class EO case; it reinforces that the $200/kg world is a 2035+
  world.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]]
