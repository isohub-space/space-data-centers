---
type: intel
tags: [sdc, intel/raw, market/startups, market/sizing, aggregator, low-trust, economics/unit-cost]
source: Introl (vendor blog — aggregator, ~65 cited references; treat figures as pointers, not facts)
url: https://introl.com/blog/orbital-data-centers-space-computing-race-2026
author: Blake Crosley
published: 2026-02-21
captured: 2026-10-04
primary: none — secondary compilation; each figure below needs its own primary before promotion
---
# Introl — "Orbital Data Center Race 2026" (aggregator; useful for pointers and sceptic figures)

**Trust level: low.** A GPU-infrastructure vendor's blog that compiles trade press. Several of its
figures are superseded by later primary sources captured in this folder. Kept because it is the only
place that gathers the **sceptic numbers** and the **BIS Research market size** in one view.

## Reported (what the source says)
**Company table (as of Feb 2026)**
- Kepler: **$233M+** raised over 7 rounds; 10 operational sats (300 kg); optical 2.5–10 Gbps → 100 Gbps.
- Starcloud: "$21M seed", Starcloud-1 **60 kg**, Starcloud-2 "**Oct 2026**" with several H100 + Blackwell.
  *(Superseded: $170M Series A Mar 2026, $250M Aug 2026; Starcloud-2 now 2027 per TechCrunch.)*
- Aetherflux: $50M Series A, demo sat 2026, node Q1 2027. *(Superseded by Cowboy $275M / end-2028.)*
- Lonestar: $5M seed; "LEO service Q4 2026". OrbitsEdge: undisclosed; orbital demo 2026.
- SpaceX/xAI merger closed **2026-02-02** at **$1.25T**; FCC filing **2026-01-30** (1M sats, comments due
  2026-03-06); Starcloud FCC filing **2026-02-03** (88,000).

**Market size**
- **BIS Research**: ODC market **$1.77B (2029) → $39.09B (2035)**, **67.4% CAGR**. *(ABI, by contrast,
  gives units/GW not revenue — the two analyst houses measure different things.)*

**Cost claims (optimistic)**
- Starcloud "**$0.005/kWh**, 15× lower than wholesale" — *contradicts the white paper itself
  ($0.002/kWh, 22×) and the company's 2026 Starcloud-3 number ($0.05/kWh).*
- 40 MW / 10 yr: **$8.2M space vs $167M terrestrial** (= white paper Table 1, verified).
- Lonestar: "97% lower operating costs, ~0.1 ¢/kWh".

**Cost claims (sceptical)**
- **Andrew McCalip (Varda)**: orbital compute ≈ **3× more per watt** than ground.
- Parity needs **<$100/kg** launch vs **~$2,700/kg Falcon 9 today**; Starship target <$100/kg = 27×
  reduction. Parity window **2028–2030** if Starship delivers; **2035+** if >$500/kg.
- **ESPI**: Starship cost assumptions "unrealistic in the near-term".

**Physics / EO**
- Orbital solar constant 1,361 W/m²; dawn-dusk SSO capacity factor "up to 99%"; **5–13× more energy
  per panel-year** than Earth.
- On-board processing cuts downlink **up to 85%** (AI) / **90–95%** (imagery & sensor fusion);
  use cases: wildfire, maritime, deforestation, defence, disaster.

## Primary (where the underlying document differs or adds)
- Not checked individually. Where this blog overlaps with primaries captured here (Starcloud white
  paper, Google paper, FCC filing dates) it is **consistent on dates and the Table 1 figures** but
  **wrong on the $/kWh** attribution.

## Derived (our arithmetic — formula shown)
- BIS $39.09B by 2035 vs ABI 1.54 GW by 2035 → implied **~$25,000/kW-year** revenue — about **6%**
  of Atomic-6's list price ($420k/kW-yr) and ~100× terrestrial colo. Internally plausible only if
  most 2035 revenue is kW-class edge/government service, as ABI also argues.

## Relevance to the Entrant
- The **85–95% downlink reduction** range is the headline KPI the Entrant should measure and publish for
  EO workloads (Satlyt has published >60%).
- Sceptic anchors to pre-empt in a pitch: McCalip's **3×/W**, ESPI's Starship critique, Gartner's
  "peak insanity" — all target GW AI, none target kW-class EO processing.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]] (pointers only; verify each before citing)
