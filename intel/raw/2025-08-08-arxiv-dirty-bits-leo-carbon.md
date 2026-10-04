---
type: intel
tags: [sdc, intel/raw, research/paper, space/orbital-compute, space/launch, economics/carbon, critique]
source: arXiv (ACM SIGENERGY Energy Informatics Review 5(2), 2025)
url: https://arxiv.org/abs/2508.06250
author: Robin Ohs, Gregory F. Stock, Andreas Schmidt, Juan A. Fraire, Holger Hermanns (Saarland University)
published: 2025-08-08
captured: 2026-10-04
primary: self
---
# Dirty Bits in Low-Earth Orbit: The Carbon Footprint of Launching Computers

## Reported (what the paper claims)
- Software-Carbon-Intensity-style model (ESpaS tool, Rust) splitting orbital compute emissions into
  operational (O) and embodied (M), where embodied includes **launch and re-entry**.
- **Falcon 9:** fuel 233.7 tCO₂e, first stage 423.0 tCO₂e (÷20 reuses), second stage 108.5 tCO₂e, payload
  17.5 t → **I_launch ≈ 20.8 kgCO₂e/kg**. Re-entry of second stage + payload produces NOₓ at 0.4 kg/kg →
  119.2 kgCO₂e/kg of re-entering mass → **I_re-entry ≈ 158 kgCO₂e/kg of payload**. Total
  **≈ 178.8 kgCO₂e/kg**. "Re-entry causes one order of magnitude more emissions than the launch."
  (Al₂O₃ ozone effects deliberately *excluded* for lack of a CO₂e conversion.)
- **Starship (best case, fully reusable, green methane):** ≈ 15.8 launch + 119.2 re-entry = **≈ 135 kgCO₂e/kg**;
  with fossil methane the fuel term alone is 202.8 kgCO₂e/kg.
- Energy intensity (solar + battery, 5-yr mission): Earth **34 gCO₂e/kWh**, F9-launched **165**, Starship
  **134** — the orbital solar array itself is nearly carbon-neutral (14–16 g/kWh) but the launched battery
  mass is not.
- **Workload intensities (Table 1):** CPU full load **283 µgCO₂e/s Earth vs 1,412 (F9) / 1,148 (Starship)**;
  DRAM 3.2 vs 4.9 / 4.5 µgCO₂e/(GB·s); SSD 0.047 vs 0.090 / 0.080; transceiver 7.1 vs 26.9 / 22.4 µgCO₂e/pkt.
- Headline: "even under optimistic assumptions, in-orbit systems incur… up to an order of magnitude more
  [carbon] than terrestrial equivalents". Longer missions amortise embodied carbon; in-orbit aggregation
  (discarding cloudy images) is a trade of compute carbon against network carbon that must be computed per
  flow.

## Primary (method / assumptions a sceptic would attack)
- Back-of-envelope by design ("detailed lifecycle data… difficult to obtain"); stage production emissions
  from a forum thread; Starship stage emissions linearly scaled from Falcon 9 by mass.
- The NOₓ re-entry conversion (0.4 kg NOₓ per kg, 119 kgCO₂e/kg) dominates the result and is the least
  certain input; it also assumes the whole payload burns up, which de-orbit-by-design satellites do.
- Terrestrial comparator is a *solar+battery-powered* ground system (34 g/kWh), not a grid data centre
  (300–500 g/kWh). [[intel/raw/2025-12-09-arxiv-tether-orbital-ai-data-centers]] uses a gas grid (500 g/kWh)
  and only propellant CO₂ (63 kgCO₂/kg launched) and concludes orbit is 10× *cleaner* — the two papers
  bracket the answer entirely through comparator choice.
- Configuration is a 28 W CPU, 2 m² array, 4 kWh battery — a CubeSat, not a kW-class compute node.

## Derived (our arithmetic — formula shown)
- Embodied launch+re-entry carbon for a compute satellite at 20 kg/kW (Starlink proxy): 20 × 178.8 =
  **3.6 tCO₂e/kW**; over 5 yr at 8,760 kWh/kW·yr → 3,576 / 43,800 = **82 gCO₂e/kWh** — below a fossil grid
  (400–500) but above European grid averages for renewables-heavy mixes and above the paper's 34 g/kWh
  Earth-solar case. At ISCR's 8.9 kg/kW: 36 g/kWh; at Turyshev's 40 kg/kW: 163 g/kWh.
- Per-flow break-even for EO: orbital processing wins on carbon when the downlink bytes avoided × (I_GSL +
  n_hops·I_ISL) exceed the extra compute carbon — i.e. exactly when the semantic reduction ratio is large.

## Relevance to the Entrant
- A "green orbital compute" narrative is **contestable**: the honest line is that embodied launch/re-entry
  carbon is amortised only by (a) long mission life and (b) high data-reduction ratios — both of which EO
  edge inference has, hyperscale orbital training does not.
- Expect EU/ESA sustainability scrutiny (re-entry aerosols, NOₓ) to reach licensing; design for
  controlled de-orbit and publish a lifecycle number before a critic does.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]] (carbon: 179 kgCO₂e/kg F9, 135 Starship; comparator sensitivity vs tether paper)
