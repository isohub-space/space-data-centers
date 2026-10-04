---
type: intel
tags: [sdc, intel/raw, market/startups, company/atomic-6, economics/unit-cost, pricing, space/power]
source: Payload
url: https://payloadspace.com/atomic-6-launches-orbital-data-center-marketplace/
author: Douglas Gorman
published: 2026-04-13
captured: 2026-10-04
primary: Atomic-6 press release (PR Newswire, "Atomic-6 Launches ODC.space") — not opened
---
# Payload — Atomic-6 launches ODC.space, a marketplace for orbital data-center capacity

The only **public price list** for orbital compute capacity found in this lane.

## Reported (what the source says)
- **Atomic-6** (Georgia, composites maker) launched **ODC.space**, a marketplace selling orbital
  data-center capacity from **1U shared** up to a **sovereign 42U rack**.
- **Sovereign 42U rack ≈ $3.5M per month**, **100 kW**.
- Delivery: **2–3 years** after purchase initially; target **4–6 weeks** once production scales.
- Atomic-6 hardware: **Light Wing** deployable solar array; **Hot Wing** deployable radiator
  (announced here). *(Sidus Space PR 2025-06-23, opened: Light Wing delivers **up to 200 W/kg**,
  "4× comparable systems".)*
- CEO Trevor Smith: a terrestrial DC waits "five years" to turn on a new chip; "**$10B per gigawatt
  per year** [in] lost revenue… you can get up in six weeks."

## Primary (where the underlying document differs or adds)
- not checked.

## Derived (our arithmetic — formula shown)
- $3.5M/month / 100 kW = **$35,000 per kW-month** = **$420,000/kW-year** ≈ **$48/kWh** of delivered
  power-equivalent (3.5e6 / (100 × 730 h)). Terrestrial colocation is ~$150–300/kW-month → the
  orbital list price is **~100–200× terrestrial colo**, consistent with ABI's "78× TCO".
- Per GPU-hour (if 100 kW ≈ 70 Blackwell-class GPUs): $3.5M / (70 × 730) ≈ **$68/GPU-hour** vs
  ~$3–6 terrestrial.

## Relevance to the Entrant
- Gives a **defensible ceiling for what sovereign/defence buyers may pay** for orbital capacity
  today ($35k/kW-month). The Entrant's EO-processing pricing can be anchored *below* this while
  still 50× terrestrial — the margin exists if the latency/sovereignty value is real.
- Atomic-6's Light Wing (200 W/kg) and Hot Wing are **buyable power/thermal modules** for a small
  node — a shortcut past the two hardest subsystems.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
