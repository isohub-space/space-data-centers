---
type: intel
tags: [sdc, intel/raw, research/paper, space/orbital-compute, space/reliability, space/servicing, economics/cost-model]
source: arXiv
url: https://arxiv.org/abs/2608.27499
author: Slava G. Turyshev (JPL / Caltech)
published: 2026-08-27
captured: 2026-10-04
primary: self
---
# Operations, Maintenance, and Industrial Scaling of MW-Class Orbital Data Centers

## Reported (what the paper claims)
- Sequel to [[intel/raw/2026-04-29-arxiv-turyshev-odc-economic-viability]]: assumes an ODC is justified and
  asks what **sustainment** it needs. An ODC "behaves simultaneously as a spacecraft constellation, a
  repairable production system, an automated warehouse, a high-availability network, and an orbital
  logistics customer."
- **Reference 1 MW cluster:** 10 active 100 kW nodes + 1 reserve node, ~200 × 5 kW compute cartridges
  (20–35 kg each), α_OH 1.25, 550–700 km high-sunlight LEO, bus life 10–15 yr, **compute refresh 3–5 yr
  (4-yr reference)**, target capacity availability 0.9995–0.9999, resupply lead time 180 days.
- **Mass allocation:** active hardware 34–59 kg/kW (+ maintainability hardware **3–7.5 kg/kW** + first-line
  spares **2–2.5 kg/kW** + reserve node 4–6 t) → **49 / 61.25 / 75 t per MW** (≈ 50–75 kg/kW).
- **Work and mass flow per MW-year:** 70.2 random/life-limited interventions + **323–349 planned refresh
  operations = 393–419 operations**; random replacement 1.3–2.0 t; planned refresh 2.88–3.98 t (compute +
  storage = 190 ops, 1.46 t); plus node loss, consumables, packaging → **5.3–9.0 t/(MW·yr), nominal 6.6**;
  560–700 productive robot-hours; 3–4 robots per MW.
- **Reliability targets (Table XVIII):** catastrophic 100 kW node hazard ≤ 0.01–0.03/yr; large-domain event
  ≲ 10⁻³/yr; robotic exception after internal recovery ≤ 10⁻³ (goal 10⁻⁴); terminal-unresolved ≤ 1.07 × 10⁻⁵
  per op; L1 cartridge exchange < 4 h; reserve-node activation < 24 h; connector ≥ 20 mate cycles; coolant
  leak ≲ 10⁻⁸ kg/s per loop.
- **Scale ladder:** 1 MW (50–75 t, 5–9 t/yr, no crew) → 10 MW (pooled servicer, contingency crew visit
  possible) → 100 MW (5–7.5 kt, 0.5–0.9 kt/yr, automated warehouse, crew campaigns) → 1 GW (50–75 kt,
  **14.5–24.7 t/day** of upmass, 250–350 robots, resident workforce "may be admissible").
- Planned refresh exceeds random failure replacement — obsolescence, not reliability, drives logistics.

## Primary (method / assumptions a sceptic would attack)
- All hazards, refresh intervals and service times are declared *allocations* ("not a closed spacecraft bill
  of materials"); the paper is a framework with a worked example, not measured data.
- Assumes robotic servicing at 10⁻³–10⁻⁴ exception rates that no orbital robot has demonstrated; the author
  flags "the most speculative items".
- A disposable-node architecture (Starlink-style: never service, re-launch every 5 yr) is the obvious
  alternative; the paper argues it fails at tens of MW because refresh would discard radiators and PV, but
  does not price the two paths against each other.

## Derived (our arithmetic — formula shown)
- Annual replenishment fraction: 6.6 t / 61.25 t ≈ **11 %/yr of deployed mass**, i.e. over a 10-yr bus life
  the logistics mass ≈ the original deployment. Launch cost of sustainment at $200/kg: 6,600 kg × 200 =
  **$1.3 M/MW·yr = $1,320/kW·yr** — larger than Google's $810/kW/yr "launched power price" for the
  initial deployment.
- Operations density: ~400 ops / 8,760 h ≈ one robotic maintenance action every **22 h per MW**.

## Relevance to the Entrant
- Shows the hyperscale ODC path requires an orbital-servicing industry that does not exist; a small
  disposable-satellite operator carries none of this overhead — a structural advantage worth stating.
- The 3–5 yr compute refresh assumption applies to the Entrant too: design the payload for **≤ 4-yr useful life** and
  price the business on that, or carry the obsolescence cost.
- The stage-gate list (node hazard ≤ 1–3 %/yr, defined fault domains, signed-update rollback ≤ one 5–10 %
  domain) is a usable reliability checklist for any orbital compute product.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]] (sustainment ≈ 11 %/yr mass; refresh dominates; $1,320/kW·yr at $200/kg)
- [[intel/wiki/orbital-data-center-landscape]]
