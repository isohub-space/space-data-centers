---
type: intel
tags: [sdc, intel/raw, research/paper, space/orbital-compute, space/thermal, space/power, space/radiation, economics/cost-model]
source: arXiv
url: https://arxiv.org/abs/2604.07760
author: Stephen Gaalema, Samuel Indyk, Clinton Staley (University of Austin)
published: 2026-04-09
captured: 2026-10-04
primary: self
---
# Reduced-Mass Orbital AI Inference via Integrated Solar, Compute, and Radiator Panels (ISCR)

## Reported (what the paper claims)
- **Headline: > 100 kW compute per launched tonne** — Table 7 gives **112.5 kW/t** for a 148.8 t,
  ~16 MW single-Starship satellite (20 m × 2,200 m roll-out array of ~16,000 panels, 45,000 m²), "within the
  SpaceX goal of 100–150 kW/ton". Includes deployment and station-keeping mass.
- Architecture: each 1 kW panel (1.7 m × 1.7 m, **2.9 m²**) = thin perovskite/Si solar cells on the front,
  vacuum gap, compute module (70 mm × 200 mm) sandwiched, **water vapour-chamber radiator** (2 mm, 0.04 bar)
  as the *only* structure, radiating single-sided at **~25–35 °C**. Total thickness 6.4 mm.
- **Mass budget (kg/m²):** solar 0.52, compute 0.23, radiator **2.40**, total **3.15 kg/m²**; distributed mass
  141.8 t + 5 % comms/control; 4 % power overhead. Stow limit would allow 197 t / 22 MW.
- **Solar:** perovskite/50 µm-Si tandem, 27 % at 70 °C, 363 W/m² in SSO, **506 W/kg** array-level specific
  power ("five times the < 100 W/kg of existing satellites"); ISS iROSA quoted at 61.5 W/kg, Starlink V3 est.
  50 W/kg / 18 % cells. Future cost 5–15 $/W.
- **Thermal:** back-face equilibrium 17–24 °C (deep space to 600 km SSO) under near-ideal assumptions
  (ε 0.92, insulated faces). Vapour chamber ΔT ~5 °C from a 1 kW module to the 1.7 m panel; heat flux
  ~60 W/cm² vs 700 W/cm² demonstrated capability.
- **Compute efficiency argument:** extrapolating a 3 nm Rubin GPU (1.8 kW TDP) from its 45 °C-coolant /
  85–90 °C-junction point: at 35 °C vapour-chamber the LVT bin runs 0.74 V / 2.6 GHz, **0.204 J/token** vs
  0.213 (baseline) vs **0.322 at 85 °C coolant / 105 °C junction** — ">30 % energy/token" penalty for
  high-temperature radiator designs, and >25 % clock gain at 35 °C vs 60 °C.
- **Inference mapping:** 512-panel sub-array runs a 500k-context, 128-block LLM at **553 tok/s/session,
  256 concurrent sessions**; 100 GB/s duplex copper between adjacent panels (< 10 W/panel); abstract claims
  31 sub-arrays / > 7,900 inferences per satellite (body says 16 / > 4,000 — internal inconsistency).
- Radiation: **3 mm HDPE** top shield "may be marginal", can go to 5 mm; lifetime may be < 5 yr by choice
  (obsolescence). Orbit 1000 km SSO baseline. Propulsion: two Busek BHT-600 (39 mN) Hall thrusters.
- Explicitly inference-only; "training requires tight synchronisation incompatible with inter-panel latency"
  (disagreeing with the Vicinanza survey that put training in space).

## Primary (method / assumptions a sceptic would attack)
- Every component is **custom and unbuilt**: perovskite/Si space cells (LEO qualification unknown), 2 mm
  water vapour chambers surviving launch-to-vacuum transition, thinned custom inference ASICs, pneumatic
  argon deployment of a 2.2 km array. The authors list "FEA of torsional statics… highest-priority
  structural risk" and admit numbers are "best-estimate".
- Table 4 temperature/efficiency values are "extrapolated from a single operating point and require
  experimental validation".
- Radiator mass 2.4 kg/m² is 76 % of distributed mass — the whole > 100 kW/t result hinges on that number
  for a 2 mm copper-wick vapour chamber (wick alone 0.56 kg/m²).
- Uses *solar* power (16.4 MW) as "compute power"; 4 % overhead for 16,000 panels' comms, control and ion
  propulsion is thin.
- 1000 km SSO sits in a harsher proton environment than 550–650 km (Google uses 650 km).

## Derived (our arithmetic — formula shown)
- Specific mass: 1,000 kg / 112.5 kW = **8.9 kg/kW** — vs 20.5 kg/kW Starlink-v2-mini proxy in
  [[intel/raw/2025-11-22-arxiv-google-suncatcher-system-design]] and 34–59 kg/kW in
  [[intel/raw/2026-04-29-arxiv-turyshev-odc-economic-viability]].
- Radiator: 2.40 kg/m² × 2.9 m²/kW = **7.0 kg/kW**; area **2.9 m²/kW single-sided** at ~30 °C; flux
  1 kW / 2.9 m² = **345 W/m²**. Sanity: εσT⁴ at 308 K, ε 0.92 = 0.92 × 5.67e-8 × 9.0e9 = 469 W/m² before
  Earth IR/leak — consistent.
- Solar: 0.52 × 2.9 = **1.5 kg/kW**; compute 0.67 kg/kW. So the low-temperature radiator, not the array, is
  the mass driver — the opposite of the Google note's section 4 assumption that arrays dominate.
- Launched-power price at $200/kg, 5-yr life: 8.9 × 200 / 5 = **$356/kW/yr** (vs Google's $810).


### Also captured by the press/sceptics lane (merged from a thinner duplicate, 2026-10-04)
*Reported:*
- Proposes integrating solar cell, radiator and compute into small panels arrayed in large SSO structures, inference-only LLM workloads.
- Claimed compute density **> 100 kW per tonne**; specific power **~500 W/kg** vs **< 100 W/kg** for conventional spacecraft.
- Reference design: **16 MW**, **150 t**, **20 m × 2,200 m** array, **16,000 panels**; junction temperature **~40 °C**.
- Throughput: **553 tokens/s per session**, **256 sessions per 512-panel sub-array**, **> 7,900** concurrent inferences per satellite; 500k-token context.
- No radiator/solar mass fractions and no cost estimate given.
*Derived:*
- 16 MW ÷ 150 t = **107 kW/t** — matches SpaceX's FCC-filing figure (~100 kW/t) and is **~3× better** than Turyshev's 34–59 kg/kW (= 17–29 kW/t). The optimist and sceptic literature differ by ~3× on mass per kW; the difference is architectural (integrated panels vs. conventional bus).
- 2,200 m array length: comparable to Starcloud's "4 km per side" claim for 5 GW (EP Think Tank note).

## Relevance to the Entrant
- Demonstrates the design lever the Entrant can actually pull at small scale: **run silicon cold** (vapour-chamber
  or heat-pipe to a large, light, low-T radiator) and bank the >30 % energy/token gain, rather than chasing
  exotic launch prices.
- 1 kW/panel modularity with copper links is a credible unit for a small EO-inference satellite; the
  2.9 m²/kW radiator figure is a useful sizing anchor for a 1–5 kW payload.
- Treat 112 kW/t as an *aspiration* in any pitch — it is a paper design with no hardware.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]] (specific-mass frontier 8.9 kg/kW; radiator 2.9 m²/kW, 7 kg/kW; cold-silicon efficiency)
- [[intel/wiki/orbital-data-center-landscape]] (Sophia Space TILE cited as commercial analogue)
