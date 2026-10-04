---
type: intel
tags: [sdc, intel/raw, research/paper, space/orbital-compute, space/thermal, space/scheduling]
source: arXiv (ACM SIGENERGY Energy Informatics Review 6(2), 2026)
url: https://arxiv.org/abs/2606.26150
author: Shuyi Chen, Zhengchang Hua, Nikos Tziritas, Georgios Theodoropoulos (SUSTech / Univ. of Thessaly)
published: 2026-06-23
captured: 2026-10-04
primary: self
---
# Hot AI in Cold Space: Thermal-Crosstalk-Aware Scheduling for Sustainable Orbital AI Clusters

## Reported (what the paper claims)
- **"Proximity-Thermal Paradox":** synchronous training (tensor parallelism) needs sub-10 µs links → nodes
  at metres-to-hundreds-of-metres spacing → thermal crosstalk. Two forms: **thermal-fluid** (monolithic
  structure, shared coolant loop: downstream nodes get pre-heated fluid) and **thermal-radiative** (proximity
  swarm: neighbours occlude radiator view factor ρ_i and radiate heat at each other).
- Model: P_in = P_idle + (P_max − P_idle)(S/S_max)^γ; radiative P_out ∝ ρ_i (T⁴ − T_amb⁴); soft/hard throttle
  thresholds; Arrhenius MTTF ∝ exp(E_a/k_B T), E_a = 0.685 eV. Exogenous solar/Earth IR/eclipse deliberately
  **excluded** ("conservative baseline").
- Simulation: monolithic 64 nodes on 8 coolant pipes; swarm 36 satellites in a 6 × 6 planar grid with
  dynamic view-factor shadowing. Baseline = uniform DDP sharding; TLB = proportional thermal-load balancing
  with an event-driven evacuation safety net.
- **Results:** monolithic downstream row saturates at **354.4 K (81.3 °C)**; swarm core nodes reach
  **357.2 K (84.1 °C)** while periphery sits at **344.5 K (71.4 °C)** — a 12.7 K gradient from occlusion alone.
  TLB flattens the swarm to 351.9–353.9 K. **MFU: monolithic 75.1 % → 82.7 %; swarm 90.0 % → 90.2 %.**
  MTTF of the hottest node **+6.15 % (swarm core), +1.71 % (monolithic outlet)**.
- Argues the correct ODC optimisation target is hardware lifespan (to amortise launch embodied carbon,
  citing [[intel/raw/2025-08-08-arxiv-dirty-bits-leo-carbon]]), not instantaneous throughput.

## Primary (method / assumptions a sceptic would attack)
- Position paper with a proof-of-concept simulator; no radiator area, kg/kW, or absolute power per node is
  given — only relative temperatures. The crosstalk magnitudes depend on an un-specified view-factor model
  and node spacing (3 m is mentioned for tensor parallelism; Google uses 100–200 m).
- Swarm MFU gain of 0.2 points is within noise; the authors reframe to lifespan, where a 6 % MTTF gain is
  modest.
- No eclipse/solar transients — which would dominate thermal variance in reality.

## Derived (our arithmetic — formula shown)
- Radiative penalty of a 12.7 K core/periphery gap at ~350 K: P_out ∝ T⁴, so the core radiator must run
  hotter by (357.2/344.5)⁴ − 1 ≈ **+15 %** flux to reject the same heat — equivalently a core node with
  the same radiator loses ~15 % of its rejection capacity to occlusion before any IR exchange.
- Confirms the warning in [[intel/raw/2025-11-22-arxiv-google-suncatcher-system-design]] about "occlusion
  of outgoing rejected-heat IR radiation between satellites" and bounds it for a 6×6 planar grid.

## Relevance to the Entrant
- Mostly a cluster problem the Entrant avoids; but the general rule applies to any multi-payload satellite:
  **shared radiating surfaces create stragglers**, and the fix is thermal-aware scheduling, not more
  hardware. Pairs with the BUPT-1 co-location result (9 h → 110 min window).
- Lifespan-first scheduling (keep peak die temperature down to extend MTTF) is the right objective for a
  solar-powered inference satellite whose cost is embodied, not operational.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]] (thermal crosstalk magnitude; lifespan-first objective)
