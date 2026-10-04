---
type: intel
tags: [sdc, intel/raw, market/esa, space/eo-edge, space/onboard-ai, market/europe]
source: UN-SPIDER (UNOOSA), relaying ESA
url: https://un-spider.org/news-and-events/news/esa-launched-%CF%86sat-2-harnessing-ai-advanced-earth-observation
author: UN-SPIDER
published: 2024-07-11
captured: 2026-10-04
primary: "eoPortal mission page 'PhiSat-1 & -2' (https://www.eoportal.org/satellite-missions/phisat-1), opened; ESA Φsat-2 pages (esa.int) returned HTTP 403 and were not opened"
---
# ESA launched Φsat-2: harnessing AI for advanced Earth observation

## Reported (what the source says)
- Article dated 11 July 2024, updated 19 Aug 2024 after launch. Φsat-2 launched **16 Aug 2024** on a SpaceX Falcon 9 (Transporter-11) from Vandenberg; deployed 21:50 CEST, first signal 23:47 CEST.
- CubeSat with a **multispectral camera**; successor to Φsat-1 (2020).
- **Six onboard AI applications**: Cloud Detection; Street Map Generation; Maritime Vessel Detection; Onboard Image Compression and Reconstruction; Marine Anomaly Detection; Wildfire Detection.
- No developers, funding or data-reduction percentages given.

## Primary (eoPortal mission page — adds)
- Φsat-1: launched 3 Sep 2020, ~6 kg, 540 km; Φsat-2: launched 16 Jun 2024 per eoPortal (**conflicts** with the 16 Aug 2024 actual launch — eoPortal carried the pre-slip date), ~**9 kg**, 480–510 km SSO at 97.4°, battery ~46 Wh, lifetime ~14 months minimum (+3–8 months extension).
- Both use the **Intel Movidius Myriad 2** VPU for inference.
- Φsat-1's HyperScout-2: swath 310 km, 75 m VNIR / 390 m TIR GSD, 12 nm spectral resolution; global revisit ~15 days.
- Φsat-2 pre-selected apps per eoPortal: Sat2Map, Cloud Detection, Vessel Detection, Compression (four); the UN-SPIDER/ESA list has six — two were added later (ESA "Φsat-2 gets two new AI apps", not opened).
- Web-search summaries (not opened) attribute the Φsat-2 cloud-detection app to **KP Labs** and say Φsat-2 "entered its science phase in **July 2025**" after **nine months commissioning**; treat as unverified until the ESA page is opened.

## Derived (our arithmetic — formula shown)
- Power class: a 46 Wh battery on a ~9 kg 6U-class bus implies an orbit-average payload budget of a few watts; Myriad 2 is a ~1 W, ~1 TOPS-class part. **Φsat-class edge AI is a 1 W / 1 TOPS problem**, not a data-centre problem.

## Relevance to the Entrant
- Φsat-1/-2 are the **reference ESA proof that onboard AI filtering works** (cloud masking, vessel detection, compression) — any the Entrant pitch to ESA/Φ-lab will be measured against them.
- The hardware lineage (Myriad 2 → Ubotica CogniSAT, KP Labs Leopard) defines the incumbent European supplier set.
- ESA is now moving to **EOCognitiveLab** (multi-satellite, ISL, onboard processing) — see [[2026-09-29-esa-indico-eocognitivelab-info-day]]; that is the procurement the Entrant should track.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]]
