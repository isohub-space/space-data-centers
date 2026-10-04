---
type: intel
tags: [sdc, intel/raw, space/optical-isl, market/europe, vendor/tesat]
source: Via Satellite
url: https://www.satellitetoday.com/technology/2025/10/27/tesat-delivers-optical-terminals-for-lockheed-martin-gps-demonstration/
author: Via Satellite
published: 2025-10-27
captured: 2026-10-04
primary: none (Tesat press release at tesat.de not opened; search snippets give SCOT20 ≤1 Gbps, TOSIRIS 1.25–10 Gbps)
---
# Tesat delivers SCOT80 terminals for Lockheed Martin GPS demo; 62 SCOT80 already in orbit

## Reported (what the source says)
- Tesat Government delivered **SCOT80** optical terminals to Lockheed Martin for a GPS IIIF-related optical crosslink demonstration (delivery completed Oct 2025).
- SCOT80: **up to 100 Gbps**; compatible with **SDA OCT Standard 3.1** with a "path for compatibility" to **Standard 4.0**.
- **62 SCOT80 units are in orbit** across multiple primes (SpaceX, York Space Systems, Lockheed Martin named).
- Lockheed context: 10 GPS III built (8 launched), up to 22 GPS IIIF under construction.
- No pricing, production capacity or headcount.

## Primary (where the underlying document differs or adds)
- Search snippets (tesat.de / SatNews, not opened): first **SCOT20** flight model (≤**1 Gbps**, CubeSat-class) delivered to **Planetek Hellas** for the **OptiSat** mission, Oct 2025; **TOSIRIS** direct-to-earth terminal **1.25–10 Gbps**.

## Derived (our arithmetic — formula shown)
- 62 flying SCOT80 is the **largest European OCT flight heritage** — vs Mynaric's committed but largely unflown SDA volumes. For a European buyer, Tesat (Backnang, Airbus-owned) is the de-risked option.
- Product ladder for an EO edge node: SCOT20 (1 Gbps, small sat) → TOSIRIS (10 Gbps DTE) → SCOT80 (100 Gbps ISL). A 10 Gbps optical DTE moves ~**75 GB per 60 s pass** (10 Gbps × 60 s ÷ 8) — enough to empty a Sentinel-class daily take in a handful of passes if clouds cooperate.

## Relevance to the Entrant
- Optical DTE at 10 Gbps **weakens the "downlink bottleneck" argument** for onboard processing on big satellites — but it is weather-dependent and needs optical ground stations, so the latency argument (insight in minutes, independent of a pass) survives.
- Tesat's SCOT20 on a Greek CubeSat (Planetek Hellas) shows OCTs are reaching the **small-sat class a startup would actually fly**.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]]
