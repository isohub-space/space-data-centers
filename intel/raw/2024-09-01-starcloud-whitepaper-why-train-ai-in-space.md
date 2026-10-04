---
type: intel
tags: [sdc, intel/raw, market/startups, company/starcloud, economics/unit-cost, space/thermal, space/launch, primary]
source: Starcloud (Lumen Orbit) white paper
url: https://starcloudinc.github.io/wp.pdf
author: Ezra Feilden, Adi Oltean, Philip Johnston
published: 2024-09-01
captured: 2026-10-04
primary: this is the primary (White Paper v1.03, September 2024; exact day not given — 01 used)
---
# Starcloud — "Why we should train AI in space" (White Paper v1.03, Sept 2024)

Company's own founding economics. Read as a **2024 position**; the company's 2026 public
numbers are far more conservative (see Derived).

## Reported (what the source says)

**Energy**
- Terrestrial solar median capacity factor **24%** (US), **<10%** northern Europe; >50% impossible on
  Earth. Proposed space array capacity factor **>95%**; peak irradiance **~40% higher** than ground.
- Assumption chain: **40 MW data center per $5M launch**, solar cells at **$0.03/W**, amortized over
  **10 years** → **~$0.002/kWh** equivalent energy cost.
- Compared against wholesale **$0.045/kWh** (US), **$0.06** (UK), **$0.17** (Japan) → "**22× lower
  cost**".
- Cell degradation **0.15%/yr** demonstrated.

**Thermal**
- Deep space sink ~**-270 °C** (2.7 K). A 1 m² black plate at 20 °C radiates more than solar panels
  generate per m² → radiators "**less than half the size** of the solar arrays". Two-phase loops;
  optional heat pumps.
- Radiator case: inlet 35 °C, outlet 5 °C, mean 20 °C; absorptivity 0.09, view factor 0.25, albedo
  0.3 used in the net-radiation calc.

**Table 1 — 40 MW cluster, 10 years, space vs land**
| Item | Terrestrial | Space |
|---|---|---|
| Energy | **$140M** @ $0.04/kWh | **$2M** solar array |
| Launch | — | **$5M** (one launch) |
| Cooling | $7M (5% of power) | "more efficient" |
| Water | 1.7M t @ 0.5 L/kWh | none |
| Backup power | $20M | none |
| Radiation shielding | — | **$1.2M** @ 1 kg shielding per kW compute and **$30/kg** launch |
| **Total** | **$167M** | **$8.2M** |

**Scale / architecture**
- **5 GW** cluster → solar array **~4 km × 4 km** (90% fill factor, 22% BOL silicon). Thin-film cells
  <25 µm, **>1,000 W/kg** power density. Orbit: **dawn-dusk Sun-synchronous**.
- Launch assumptions: reusable heavy-lift at **~$5M per launch**, **100 t to SSO** → **~$30/kg**
  ("could drop to $10/kg"). Payload bay ≈ **300 racks at 50%**; with GB200 NVL72 one launch ≈
  **40 MW** of compute; **5 GW in <100 launches** + similar number for solar/radiator modules;
  vehicles "designed to launch up to three times per day".
- Design life **≥10 years**; ISS thermal systems cited at **15 yr** design life.
- Radiation: budgeted as **1 kg shielding per kW** of compute.

## Primary (where the underlying document differs or adds)
- This *is* the primary. Note the authors' quoted $30/kg is a long-term Starship aspiration, not a
  price list; Google's Nov 2025 paper independently lands at **<$200/kg by ~2035** and the
  company's own March 2026 Starcloud-3 pitch uses **$500/kg**
  ([[intel/raw/2026-03-30-techcrunch-starcloud-170m-series-a]]).

## Derived (our arithmetic — formula shown)
- Sensitivity of Table 1 to launch price: at **$500/kg** instead of $30, the launch line becomes
  100 t × $500 = **$50M** and shielding (40 MW × 1 kg/kW × $500) = **$20M** → space total
  ≈ 8.2 − 5 − 1.2 + 50 + 20 = **$72M** vs $167M terrestrial: still cheaper on paper, but the 20× gap
  shrinks to ~2.3× and the terrestrial side omits GPU cost on both sides anyway.
- Energy price implied at $500/kg (launch only, 10 yr, 95% CF): 100 t launch $50M / (40,000 kW ×
  8,760 h × 0.95 × 10) ≈ **$0.015/kWh** before solar/radiator hardware — consistent with the
  company's later $0.05/kWh all-in number.

## Relevance to the Entrant
- The paper never addresses **what workload** justifies orbit beyond cheap power; EO "process
  where the data is" (latency/downlink savings) is a *different* value proposition and does not
  depend on $30/kg launch. The Entrant's case survives the launch-cost walk-back; Starcloud's 2024 case
  does not.
- Thermal rule of thumb to reuse: radiator area ≈ **≤0.5× solar area** at ~20 °C coolant; "1 kg
  shielding per kW" as a budgeting prior for COTS GPU payloads.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
- [[intel/wiki/orbital-compute-launch-economics]]
