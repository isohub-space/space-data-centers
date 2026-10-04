---
type: intel
tags: [sdc, intel/raw, market/startups, company/cowboy-space, company/aetherflux, funding, space/launch, hardware/nvidia]
source: TechCrunch
url: https://techcrunch.com/2026/05/11/there-arent-enough-rockets-for-space-data-centers-cowboy-space-raised-275-million-to-build-them/
author: Tim Fernholz
published: 2026-05-11
captured: 2026-10-04
primary: none (company announcement; FCC filing "Stampede" of 2026-05-14 covered in [[intel/raw/2026-05-18-satnews-cowboy-stampede-fcc-20000]])
---
# TechCrunch — "There aren't enough rockets for space data centers" — Cowboy Space (ex-Aetherflux) raises $275M Series B

## Reported (what the source says)

**Round**
- **$275M Series B**, **$2B post-money**, led by **Index Ventures**; also Breakthrough Energy
  Ventures, Construct Capital, IVP, **SAIC**. Prior investors: Index, BEV, a16z, NEA.
- **Previous funding: $80M** (Series A $50M Apr 2025 + ~$30M; founder Baiju Bhatt seeded $10M).
  *(Satnews 2026-05-18: total disclosed equity ≈ **$325M**. WSJ via DCD/OODAloop 2026-03-31
  had reported the raise as **$250–300M at $2B** — closed at $275M, within range.)*

**Company**
- Founded **2024 as Aetherflux** (space solar power beaming); **rebranded Cowboy Space
  Corporation**. Founder/CEO **Baiju Bhatt** (Robinhood co-founder). Hires: Warren Lamont (ex-Blue
  Origin propulsion), Tyler Grinnell (ex-SpaceX launch director).

**Architecture — vertically integrated rocket + data center**
- Satellite/node: **20,000–25,000 kg**, **1 MW** power, **~800 GPUs** on board.
- Own rocket: payload "slightly exceeds Falcon 9 capability; smaller than Starship". The rocket's
  **second stage and the compute payload are one integrated vehicle** (Satnews).
- **First launch target: before end of 2028.**
- Rationale (Bhatt): insufficient commercial launch capacity **3–4 years forward**, so ODC scaling
  requires in-house rockets.

## Primary (where the underlying document differs or adds)
- not checked (FCC filing covered in the Satnews note).

## Derived (our arithmetic — formula shown)
- Specific power: 1,000 kW / 22,500 kg ≈ **44 W/kg** whole-vehicle (incl. upper stage) — in the
  same band as ABI's 50 W/kg example and Starcloud-3's 67 W/kg.
- 1 MW / 800 GPUs = **1.25 kW per GPU** all-in (solar, thermal, structure) — ~1.3–1.7× a Blackwell
  TDP, so the design assumes very lean overhead.
- Capital per MW on orbit (if the first node consumes the whole $355M raised): **~$355M/MW** — vs
  terrestrial ~$10–15M/MW; the business only works at fleet scale.

## Relevance to the Entrant
- Second well-funded player (after Starcloud) to say **launch, not capital or chips, is the
  bottleneck through ~2029**. Expect rideshare prices to firm, not soften, for small EO
  payloads in that window.
- Cowboy's **laser power/data beaming** heritage (Reason-1/-2, see Transporter-18 note) could become
  an optical-downlink service for small EO-compute nodes — a potential supplier rather than a rival.
- SAIC in the cap table signals the **US defence demand** pull; European sovereignty is the
  unaddressed mirror market.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
