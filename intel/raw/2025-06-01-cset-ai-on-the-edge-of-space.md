---
type: intel
tags: [sdc, intel/raw, market/defence, space/onboard-ai, research/policy, market/us]
source: CSET (Georgetown Center for Security and Emerging Technology)
url: https://cset.georgetown.edu/wp-content/uploads/CSET-AI-on-the-Edge-of-Space.pdf
author: Christopher Huynh
published: 2025-06-01
captured: 2026-10-04
primary: "this is the primary (issue brief PDF, pp. 1–11 and 19–21 read)"
---
# CSET issue brief — "AI on the Edge of Space: Securing Space Superiority and Avoiding Surprise in Orbit"

> Dated "June 2025" on the cover; day approximated to 01.

## Reported (what the source says)
- Focus: US Space Force **space domain awareness (SDA)** and **orbital warfare**; recommends "procuring upgradeable satellite systems with **sufficient onboard compute**" and defining boundaries for on-orbit autonomy.
- Context numbers: >**10,000** active satellites in 2024 (>60% Starlink); conjunction "near misses" up **>250%** 2020–2023; USSF tracks **>47,000** objects; record **2,895** objects launched in 2023; it took **up to seven days** to forensically reconstruct a 2023 debris event.
- Onboard hardware: rad-hard **BAE RAD5545** ("1,000× the floating-point performance" of the Curiosity-era predecessor) vs COTS **AMD Versal XQR, NVIDIA Jetson Orin NX / AGX Orin** "at a fraction of the RAD5545's cost"; "barriers to deploying AI-driven autonomy in space are rapidly falling".
- Latency framing: in orbital warfare "**milliseconds** can determine the life or death of a satellite"; onboard AI lets a satellite act when ground telemetry is disrupted; models should be **retrained on the ground and uplinked** to re-program behaviour in flight.
- Recommendations: deploy mature AI for orbit determination/conjunction triage; **digital-twin CI/CD testbeds**; explainability (LIME); TEVV; "ample compute headroom" as an acquisition requirement.
- No European players and no EO data-volume figures.

## Primary (where the underlying document differs or adds)
- this is the primary

## Derived (our arithmetic — formula shown)
- none

## Relevance to the Entrant
- The **defence rationale for onboard compute is autonomy and survivability, not downlink savings** — a different value proposition from EO time-to-insight, but it is why governments (70–80% of optical-comms revenue per SatNews) will pay for compute in orbit. European MoDs (DALO's BIFROST, EDF-backed Edge Aerospace) follow the same logic.
- "Uplink retrained models" = the **software-update business model** for an orbital compute node; the Entrant's product should be designed as a re-programmable hosted platform, not a fixed-function processor.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]]
