---
type: intel
tags: [sdc, intel/raw, research/paper, space/orbital-compute, space/thermal, space/power, space/downlink, economics/cost-model, critique]
source: arXiv
url: https://arxiv.org/abs/2604.27197
author: Slava G. Turyshev (JPL / Caltech)
published: 2026-04-29
captured: 2026-10-04
primary: self
---
# Orbital Data Centers: Spacecraft Constraints and Economic Viability

## Reported (what the paper claims)
- Physics-based competitiveness bound: an orbital cluster must *simultaneously* close
  (L$/kg + B$/kg)·m_kW + C_link + C_ops ≲ C_terr **and** Γ ≤ Γ_max, where m_kW = deployed kg per delivered IT kW,
  Γ = space-to-ground bits per joule of compute, Γ_max = sustained comms ceiling, plus utilisation U_eff and
  lifetime penalty Π_life. Three regimes: **C1** space-native processing (reduce downlink / act locally),
  **C2** comms-integrated edge compute, **C3** terrestrial-user general compute.
- **1 MW IT base case (high-sunlight LEO, α_OH = 1.25 overhead):** BOL PV area **5.64 × 10³ m²**, radiator
  **2.50 × 10³ m²**, PV + storage + radiator **29.4 kg/kW**; with structure, propulsion, comms terminals,
  avionics, shielding and compute packaging **m_kW = 34–59 kg/kW**.
- Technology anchors (Table V): PV 30–165 W/kg; batteries 150–265 Wh/kg, DoD 0.3–0.8; radiator ε 0.8–0.95,
  view factor 0.7–0.9, **T_rad 300–400 K, areal density 2–10 kg/m²**; demonstrated optical downlink
  100–200 Gb/s peak.
- **Economics:** terrestrial AI-ready *infrastructure* (power delivery, cooling, building, site electrical —
  excluding servers) C_terr ≈ **10–40 k$/kW**. At m_kW ≈ 40, this leaves only **250–1,000 $/kg for launch
  *plus* spacecraft build**, before link, ops, utilisation and lifetime. Falcon 9 list price 74 M$ / 22,000 kg
  = **3,360 $/kg** → the allowance is **3.4–13.5× below today's launch price alone**. Sensitivity: each
  100 $/kg of (L+B) = 4,000 $/kW; each 1 k$/kW of link/ops burden removes 25 $/kg of allowance.
- Lifetime penalty Π_life = λT/(1−e^(−λT)): **1.27** for λ = 0.10/yr, T = 5 yr; **1.58** for λ = 0.20/yr —
  "a node close to capital break-even can be pushed 27–58 % higher in delivered-cost terms".
- Conclusion: C3 (competing with terrestrial DCs for Earth users) "is not a generally closed replacement…
  under baseline assumptions"; **C1/C2 — space-native preprocessing and comms-integrated edge compute — are
  the credible early regimes** because location creates intrinsic value and they tolerate duty-cycling.

## Primary (method / assumptions a sceptic would attack)
- Benchmarks are U.S.-calibrated (LBNL 176→325–580 TWh/yr); applying elsewhere needs local C_terr, χ, etc.
  (the author says so).
- C_terr excludes servers/accelerators on both sides — fair — but the 10–40 k$/kW facility figure is for
  Tier-redundant, liquid-cooled AI campuses; a cheaper comparator (e.g. 5 k$/kW) halves the allowance.
- m_kW fixed-mass term (structure, GNC, shielding) is bracketed from "two reference architectures", not a
  closed design; the 34–59 range is wide.
- Radiator sized from Stefan–Boltzmann with absorbed environmental flux; no credit for the cold-silicon
  efficiency gains ISCR claims. Advocates of < 10 kg/kW designs (ISCR 8.9, tether 5) would say m_kW = 40 is
  the problem, not the physics — but those designs are unbuilt.

## Derived (our arithmetic — formula shown)
- Radiator per kW: 2,500 m² / 1,000 kW_IT = **2.5 m²/kW_IT** (= 2.0 m²/kW of total bus power at α_OH 1.25);
  PV **5.64 m²/kW_IT** BOL. Radiator mass at 2–10 kg/m² → **5–25 kg/kW** — the single largest swing term.
- **Reconciling with Google:** Google's $810/kW/yr at $200/kg ⇔ launch capital 20.5 × 200 = $4,100/kW. In
  Turyshev's frame at m_kW = 40: launch alone 40 × 200 = **$8,000/kW**; under the 10 k$/kW low benchmark
  that leaves ≤ $2,000/kW = **≤ $50/kg for spacecraft build** — i.e. Google's $200/kg target closes only
  with a near-free spacecraft, or against the 40 k$/kW high benchmark (≤ $800/kg build). The two papers do
  not contradict on numbers; they differ on what is inside the boundary (launch-vs-opex vs
  launch+build-vs-capex).
- At the Entrant scale (say 2 kW IT, m_kW 40 → 80 kg; at F9 rideshare ~$6,000/kg → $480k launch; build dominates).


### Also captured by the press/sceptics lane (merged from a thinner duplicate, 2026-10-04)
*Reported:*
- Feasibility "is not set by orbital solar flux alone, but by simultaneous closure of photovoltaic generation, eclipse recharge, radiative heat rejection, sustained space-to-ground communications" and mission longevity.
- Representative **1 MW** facility: **5,640 m²** PV (beginning of life), **2,500 m²** radiator.
- Mass efficiency: **29.4 kg/kW** for PV + storage + radiator alone; **34–59 kg/kW** total including fixed spacecraft mass.
- Cost closure: at **40 kg/kW**, a terrestrial benchmark of **$10–40k/kW** allows only **$250–1,000/kg** for *combined* launch + spacecraft build. Current Falcon 9 launch cost alone is **3.4–13.5×** above that ceiling before any operations cost.
- Credible near-term niches: **space-native preprocessing** and communications-integrated **edge computing**.
*Derived:*
- Radiator density: 1,000,000 W ÷ 2,500 m² = **400 W/m²**. PV density: 1,000,000 W ÷ 5,640 m² = **177 W/m²** of array.
- Launch mass per MW: 34–59 kg/kW × 1,000 = **34–59 t/MW**. At $7,000/kg rideshare → **$238–413M/MW launch alone**; at Google's $200/kg → **$6.8–11.8M/MW**; at $500/kg (JLL/McKinsey threshold) → **$17–30M/MW**.
- 1 GW → **34,000–59,000 t** → **170–295 Starship flights** at 200 t, before replacements.

## Relevance to the Entrant
- **The clearest academic endorsement of the Entrant's regime:** C1 "space-native processing that reduces
  space-to-ground data or enables local action" is named as *the* credible early market; C3 (orbital cloud
  for Earth users) is shown to need 3–13× cheaper launch *and* build than today.
- Gives a defensible investor narrative: the Entrant is not betting on $200/kg; it is monetising Γ (bits saved per
  joule) where location has intrinsic value.
- The Π_life result (27–58 % penalty for 10–20 %/yr hazard) means reliability engineering is worth as much as
  launch price to a small operator's unit economics.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]] (m_kW 34–59; 250–1,000 $/kg allowance; reconciliation with Google's $810/kW/yr; Π_life)
- [[intel/wiki/eo-edge-compute-value-chain]] (C1/C2/C3 taxonomy)
- [[intel/wiki/orbital-data-center-landscape]] (JPL critical analysis)
