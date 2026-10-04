---
type: intel
tags: [sdc, intel/raw, market/sceptics, space/thermal, space/orbital-compute]
source: IEEE Spectrum
url: https://spectrum.ieee.org/orbital-data-centers-heat
author: Andrew Cavalier (ABI Research), for IEEE Spectrum
published: 2026-06-11
captured: 2026-10-04
primary: "ABI Research TCO model (not public); see 2026-05-11 ABI Research note"
---
# IEEE Spectrum — "Why Thermodynamics Rules Future Orbital Data Centers"

## Reported (what the source says)
- "Free cooling" is a misconception: no conduction or convection in vacuum, only radiation (Stefan–Boltzmann, ∝ area × T⁴).
- Radiator area for one **700 W** H100: **~3 m² at 20 °C**, **1.4 m² at 60 °C**, **1 m² at 85 °C**.
- After **5 years** in orbit, ionising radiation degrades emissivity so required area rises **~40%**.
- A **40 kW** rack (32 GPUs) needs an **80 m²** radiator ("pickleball court"); a **100 MW** data centre needs **≥ 2,500** such radiators.
- Solar generation ≈ **400 W/m²**, heat rejection ≈ **450 W/m²** — roughly one m² of radiator per m² of solar array.
- Radiators + solar arrays are **65–70% of satellite mass**.
- ABI model: launching and running a GPU in space for a year costs **at least an order of magnitude** more than terrestrial, even assuming Starship at **$44/kg**.

## Primary (where the underlying document differs or adds)
- not checked (ABI model proprietary)

## Derived (our arithmetic — formula shown)
- Radiator power density implied: 40,000 W ÷ 80 m² = **500 W/m²**; 100 MW ÷ (2,500 × 80 m²) = 500 W/m² → **2,000 m² of radiator per MW**.
- Compare Turyshev (arXiv 2604.27197): 2,500 m²/MW (400 W/m²); TNW/Ars: 1,200 m²/MW. Range **1,200–2,500 m²/MW** depending on assumed radiator temperature.
- A GitHub critique cited in search results notes ISS radiators achieve ~215 W/m², i.e. Spectrum's 500 W/m² is **2.3× better than flown hardware**.

## Relevance to the Entrant
- For a ~1 kW EO-processing payload, 500 W/m² → **~2 m²** of radiator; at ISS-class 215 W/m² → **~4.7 m²**. Both fit a smallsat; the thermal tax that kills GW data centres is survivable at the Entrant scale.
- The 40% five-year emissivity degradation is a design-life argument: plan radiator margin or a shorter refresh cycle.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]]
