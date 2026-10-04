---
type: intel
tags: [sdc, intel/raw, market/startups, company/starcloud, funding, space/launch, hardware/nvidia]
source: TechCrunch
url: https://techcrunch.com/2026/08/21/starcloud-raises-200-million-for-orbital-data-centers-as-launch-options-dry-up/
author: Tim Fernholz
published: 2026-08-21
captured: 2026-10-04
primary: none (company announcement; Aviation Week ran the same day "Orbital Data Center Startups Each Unveil $250M Venture Rounds" — Starcloud + Muon Space — paywalled, headline only)
---
# TechCrunch — Starcloud raises $250M for orbital data centers "as launch options dry up"

> **Headline/URL discrepancy.** The URL slug says **$200 million**; the article body says a
> **$250M Series A extension**. Use $250M (confirmed by SpaceNews headline 2026-08-21 and
> Interesting Engineering 2026-08-23).

## Reported (what the source says)

**Round**
- **$250M Series A extension**, led by **Manhattan West**; post-money valuation **$2.3B**.
- Nvidia put in **$25M** specifically. Other participants: Benchmark, EQT, Soma, NFX, 776,
  Cedar Capital, Goanna Capital, Standard Capital, Cisco.
- Prior: **$170M Series A, March 2026**. TechCrunch sums **total raised = $420M**.
  *(Cross-check: Interesting Engineering 2026-08-23 and GeekWire snippet say **$450M** total
  since 2024 founding — the two outlets disagree by $30M, presumably seed/YC money counted or
  not.)*

**Launch constraint — the article's angle**
- CEO Philip Johnston: *"launch is pretty constrained right now."* SpaceX's **Falcon 9 program is
  scheduled to end in 2028**; Starship is unproven; New Glenn, Vulcan, Neutron are not flying
  regularly.
- Johnston: *"Obviously if we can't book any SpaceX launch capacity in 2029, that will be
  challenging for us."*
- Starcloud has asked the FCC for permission to operate **88,000 spacecraft**.

**Hardware / roadmap**
- Operating an **Nvidia H100 in orbit** today (Starcloud-1); first to train a model with an H100
  in space.
- **Starcloud-2**: new generation of **8 kW compute satellites**; **two rideshare launches planned
  in 2027**; intended for **US government agency customers doing orbital inference**.
- **Starcloud-3**: largest orbital data-center spacecraft, designed for **Starship**.
- Future chip: **Nvidia Vera Rubin Space-1** (space-specific GPU, expected **late 2028**).
- Design concerns listed: chip operating temperature, radiator sizing, radiation shielding,
  launch ruggedization.

**Company**
- **25 employees**; **100,000 sq ft facility in Woodinville, WA** (manufacturing expansion for
  Starcloud-3 production lines per IE 2026-08-23).

## Primary (where the underlying document differs or adds)
- not checked (no filing/press release opened; Aviation Week piece paywalled — headline confirms
  the second $250M round the same week was **Muon Space**, see
  [[intel/raw/2026-08-20-viasatellite-muon-space-250m-series-c]])

## Derived (our arithmetic — formula shown)
- Nvidia's share of the round = 25 / 250 = **10%** of the extension.
- Implied valuation step-up: $2.3B post (Aug) vs $1.1B post (Mar) = **2.1× in ~5 months**.
- 8 kW per Starcloud-2 satellite × 88,000 (FCC ask) = **704 MW** — far below the "20 GW" ambition
  quoted elsewhere (IE 2026-08-23), so the 88k constellation must be assumed to carry much larger
  Starcloud-3-class buses.

## Relevance to the Entrant
- Even the best-funded ODC startup names **launch availability 2028–2029**, not capital, as its
  binding constraint. A small European EO-processing player hosting on rideshare/ESPA class is
  in the same queue; book early or design for hosted-payload slots on others' buses.
- The near-term Starcloud-2 product is **8 kW inference nodes for government customers** — this
  is exactly the kW-class edge tier (ABI) where EO time-to-insight competes; it is not GW AI.
- Nvidia's $25M is a signal that COTS-GPU-in-orbit is now the vendor-backed default; rad-hard
  compute is being positioned as niche.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
