---
type: intel
tags: [sdc, intel/raw, market/europe, market/funding, vendor/unibap, space/eo-edge]
source: Investing.com (earnings-call transcript summary)
url: https://www.investing.com/news/transcripts/earnings-call-transcript-unibap-q3-2025-sees-revenue-growth-amid-challenges-93CH-4333336
author: Investing.com
published: 2025-11-05
captured: 2026-10-04
primary: "Unibap iX10 product page (https://unibap.com/solutions/hardware/ix10/), opened; Unibap Q3 2025 interim report not opened"
---
# Unibap Q3 2025: revenue +27% YoY, still loss-making, ~100 computers/yr capacity

## Reported (what the source says)
- Q3 2025 **net sales SEK 17.3 M**, **+27% YoY**; trailing-twelve-month growth **26%**; guidance "30–50% growth" but "may be on the lower end".
- **Operating result −SEK 13 M**; operating cash flow **−SEK 11.6 M**; share fell 11.4% to SEK 8.08 on the day.
- Orders/backlog named: **€1.39 M from Loft Orbital** (first call-off under a frame agreement); **€2 M minimum volume from Ergotech** (no call-off yet); **$0.9 M from a US research institute** (delivered Q3); **SEK 14 M order from UAE** (export licence received Q4, delivery delayed).
- Deployment: "more than **30** computers planned for orbit in **2025**"; **two iX10 units launched with JAXA** in spring 2025 and operational; first standalone software (pre-processing tool) deployed on an **Italian constellation**.
- Production capacity: **~100 computers annually**.

## Primary (iX10 product page — adds)
- iX10: **AMD Ryzen V1000** CPU with 8 Radeon GPU CUs, configurable VPU (**Intel Myriad X** or **Hailo-8**); **<40 W** depending on load; **1,400 g**; 125×125×75 mm; TID **>20 krad with enclosure**; Linux-based Unibap OS; dual 10 GbE, dual Camera Link, SpaceWire. "First launch Q1 2025", "in serial production", TRL 9 claimed. Earlier iX10-100 datasheet (search summary) states **4 TOPS** from the Myriad X.
- Customers logos: NASA, ReOrbit, Moog. Other opened sources: Unibap iX computer is the onboard AI on Denmark's **BIFROST** — see [[2025-06-23-spacenews-space-inventor-bifrost-arctic]].

## Derived (our arithmetic — formula shown)
- SEK 17.3 M/quarter × 4 ≈ **SEK 69 M/yr ≈ €6 M/yr** run-rate for the most-flown European space edge computer vendor — the whole "sell the box" market is small.
- 4 TOPS / 40 W = **~0.1 TOPS/W** (Myriad X variant); Hailo-8 variant would be ~26 TOPS at a few W, so **~0.5 TOPS/W** system-level — an order of magnitude below the ≥100 TOPS Jetson-class units EDGX is qualifying (see [[2024-10-08-esa-artes-edgx-ascend-dpu-family]]).
- 100 units/yr × ~€100 k (our assumption, no public price) ≈ **€10 M/yr** theoretical hardware ceiling; consistent with the run-rate.

## Relevance to the Entrant
- Shows the **unit economics of hardware-only edge compute**: ~30 flight units a year, €6 M revenue, still burning cash. A startup selling boxes will not reach escape velocity; the value has to be in the service/latency layer.
- Unibap is the obvious **off-the-shelf processor** for a first the Entrant demo (rad-tolerant, Linux, flown on ION, JAXA, BIFROST, Loft) and the obvious partner/acquirer for a software-centric the Entrant.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
- [[intel/wiki/eo-edge-compute-value-chain]]
