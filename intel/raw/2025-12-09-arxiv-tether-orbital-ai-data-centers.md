---
type: intel
tags: [sdc, intel/raw, research/paper, space/orbital-compute, space/thermal, space/power, space/radiation, space/downlink, economics/carbon]
source: arXiv (AIAA-style preprint)
url: https://arxiv.org/abs/2512.09044
author: Igor Bargatin, Dengge Jin, Zaini Alansari, Jordan R. Raney (University of Pennsylvania)
published: 2025-12-09
captured: 2026-10-04
primary: self
---
# Tether-Based Architecture for Solar-Powered Orbital AI Data Centers

## Reported (what the paper claims)
- Architecture: thousands of identical ~10 kg nodes on a **gravity-gradient-stabilised vertical tether**
  (three Zylon/CFRP tethers for redundancy), in **dawn-dusk SSO at ~1,600 km / 102.5°** (chosen as the
  lowest altitude with zero eclipse year-round). Two variants: **~2 MW** (Falcon-9 class, few km tether) and
  **~20 MW** (Starship, tens of km). Target workload: **AI inference only** — "training demands… ultra-high
  bandwidth links that are currently impractical in orbit".
- **Node:** two 3 m CdTe thin-film discs (3 µm CdTe on 25 µm polyimide, < 0.7 kg/m², ~10 % efficient) →
  **~2 kW** electrical; PV + hoop + power electronics **~2 kg**; GPU/CPU/HBM; closed-loop **water cooling** whose
  20 mm water + Al housing doubles as radiation shield; radiator **~5 kg, 2 m × 3 m**, electronics at **~80 °C**.
  Node ≈ 9–10 kg, spacing 5 m.
- **Radiation:** SPENVIS dose **~10 Gy (1 krad)/yr** at 1,600 km behind the shield — ~1000× ground level;
  cites NASA COTS GPU tests (no permanent failure to 6 krad, but functional interrupts) and Google's TPU
  results (HBM irregularities at 2 krad, workloads fine to 15 krad "≈ 15 years on orbit").
- **Comms:** fibre along the tether, one optical router node per ~100 nodes; downlink via relay (Starlink:
  ~20 Gb/s downlink/sat, ~100 Gb/s ISL, ~100 Tb/s aggregate backbone). A 20 MW inference centre needs "at
  most ~10–20 Tb/s", typically **~0.02 Tb/s per 2 MW**.
- **Dynamics:** 0.1 g micrometeoroid at 11 km/s → yaw deflections 0.3° (101 nodes) / 0.05° (1,001 nodes);
  passive solar-pressure yaw stabilisation via chevron panels; critical damping β ≈ 10⁻⁵ N·m·s.
- **End of life:** 5-yr life (obsolescence); de-orbit by thrusters (days–months) or solar sailing (~1 yr);
  ballistic coefficient ~2 m²/kg gives natural re-entry within ~30 yr even from 1,600 km.
- **CO₂:** one 10 kg node costs ~650 kg propellant / **630 kg CO₂** on Falcon 9 (330 kg on Starship) vs
  **~8,000 kg CO₂/yr** running the same 2 kW node on a gas grid (17,500 kWh × 0.5 kg/kWh) → "an order of
  magnitude" less over 5 years.

## Primary (method / assumptions a sceptic would attack)
- 2 kg for 14 m² of PV plus hoops plus electronics (**~1,000 W/kg**) is far beyond any flown array
  (iROSA ~60 W/kg; ISCR paper claims 506 W/kg as a stretch). 10 % CdTe on polyimide at 90 °C is unqualified.
- 1,600 km is inside the inner proton belt's rising edge; 1 krad/yr behind 20 mm water+Al is 7× Google's
  150 rad/yr at 650 km, and SEU rates (not just TID) scale with it — the paper has no SEE rate.
- "Compute hardware ~5 kg per 2 kW node" — a 2 kW GPU node's mass (board, HBM, pumps, shielding) is not
  budgeted; the ~10 kg/node total looks like PV + radiator only.
- CO₂ comparison counts only propellant combustion (not stage production, re-entry NOₓ) and compares against
  a gas grid — [[intel/raw/2025-08-08-arxiv-dirty-bits-leo-carbon]] does the lifecycle version and gets the
  opposite result.
- Starlink as the downlink is asserted, not negotiated.

## Derived (our arithmetic — formula shown)
- Specific mass: 10 kg / 2 kW = **5 kg/kW** (the most aggressive figure in the literature; ISCR 8.9,
  Starlink proxy 20.5, Turyshev 34–59).
- Radiator: 5 kg / 2 kW = **2.5 kg/kW**; 6 m² / 2 kW = **3 m²/kW** (two-sided panel at 353 K). Ideal two-sided
  ε = 0.9 at 353 K radiates 2 × 0.9 × 5.67e-8 × 353⁴ ≈ **1,585 W/m²**, so 2 kW needs 1.3 m²; their 3 m²/kW
  implies ~56 % margin for solar/Earth IR load and fin efficiency — reasonable.
- PV: 2 kg / 2 kW = **1 kg/kW** vs ISCR's 1.5 kg/kW and Turyshev's 6–33 kg/kW (30–165 W/kg).
- Launch CO₂ per kW: 630 / 2 = 315 kg CO₂/kW on F9; 1 krad/yr × 5 yr = 5 krad — **above** Google's 2 krad
  HBM-irregularity onset, which the paper does not reconcile.

## Relevance to the Entrant
- Another independent architecture study concluding **inference-only, single-node compute, ~2 kW
  granularity, relay-based downlink** — the same product envelope the Entrant occupies.
- The ~0.02 Tb/s per 2 MW downlink estimate (10 bit/s per W of inference) is a useful order-of-magnitude for
  sizing the Entrant's downlink: EO inference outputs are far below raw-image downlink needs.
- Warns against very high SSO altitudes: 1,600 km buys zero eclipse at the price of ~7× dose.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]] (5 kg/kW claim, radiator 2.5 kg/kW & 3 m²/kW, 1 krad/yr at 1,600 km)
- [[intel/wiki/orbital-data-center-landscape]] (UPenn tether concept; cites ASCEND/Thales)
