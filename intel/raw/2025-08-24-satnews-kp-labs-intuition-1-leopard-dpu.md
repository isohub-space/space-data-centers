---
type: intel
tags: [sdc, intel/raw, market/europe, space/eo-edge, space/onboard-ai, vendor/kp-labs]
source: SatNews
url: https://satnews.com/2025/08/24/intuition-1-satellite-plays-games-and-captures-the-world-from-orbit/
author: SatNews
published: 2025-08-24
captured: 2026-10-04
primary: "KP Labs Intuition-1 mission page (https://www.kplabs.space/projects-and-missions/intuition-1) and Orbital Transports Leopard catalogue entry (https://catalog.orbitaltransports.com/leopard/), both opened"
---
# KP Labs' Intuition-1: Leopard DPU runs Doom and 192-band hyperspectral AI after 647 days in orbit

## Reported (what the source says)
- Intuition-1 launched **11 Nov 2023** (Transporter-9); by the article **647 days** in orbit, ~**9,807 orbits** (~15/day).
- On **12 Aug 2025** KP Labs (Gliwice, Poland) ran the 1993 game *Doom* on the **Leopard DPU** as a demonstration of general-purpose compute; the satellite continued delivering hyperspectral images (Mexico, China, USA, Myanmar, Brazil, New Zealand, Poland).
- KP Labs operates two DPUs: Leopard on Intuition-1 and **LeopardISS** on the ISS (Polish astronaut Sławosz Uznański-Wiśniewski's mission).
- No TOPS, band count, funding or customer numbers in the article.

## Primary (KP Labs mission page + Leopard catalogue — adds)
- **6U CubeSat**, bus by **AAC Clyde Space**; funded by Poland's **National Centre for Research and Development (NCBR)**; mission 2023–2027.
- Imager: **192-band** hyperspectral, 465–940 nm, **25 m GSD at 600 km**, 340 fps.
- Leopard: **"up to 3 TOPS"**, achieved **3 TOPS in orbit**, **0.3 TOPS/W**; two redundant nodes on **AMD Zynq UltraScale+ ZU9EG**; 16 GiB DDR4 ECC, 4 GiB SLC NAND, 2 × 240 GiB pSLC SSD per node.
- Links: S-band uplink **256 kbps**; **X-band downlink 3–50 Mbps**.
- Catalogue: Leopard family on ZU6EG/ZU9EG/ZU15EG; **5–20 W** (20 W peak); **725 g**; PC/104; SpaceWire + PUS-C; TMR boot flash, EDAC NAND. Radiation figures not published.
- Result claimed: "terabytes of hyperspectral data processed", downlinking "only relevant insights".

## Derived (our arithmetic — formula shown)
- Raw cube rate: 192 bands × (e.g.) 1 Mpx × 12 bit ≈ 2.3 Gbit per frame; at **50 Mbps** max downlink one such cube takes **~46 s** of pass time — a 6U hyperspectral sat **cannot** downlink raw cubes at scale, which is the whole reason for Leopard.
- 3 TOPS / 10 W typical = 0.3 TOPS/W as stated; vs EDGX Sterna (≥100 TOPS, Jetson Orin NX ~15–25 W) ≈ **4–7 TOPS/W** — FPGA-class units are ~10–20× less efficient but radiation-mitigated by design (TMR/EDAC).

## Relevance to the Entrant
- KP Labs is the **Polish incumbent for ESA onboard AI** (Φsat-2 cloud detection app, OPS-SAT VOLT, Leopard) with public-funded heritage; a competitor for ESA work and a likely subcontractor.
- Intuition-1 is the clearest **European quantified case** of why onboard processing exists: a 3–50 Mbps link against a 192-band sensor.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]]
- [[intel/wiki/orbital-data-center-landscape]]
