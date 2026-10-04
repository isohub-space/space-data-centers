---
type: intel
tags: [sdc, intel/raw, market/sceptics, space/launch, market/sizing, space/orbital-compute]
source: JLL (research insight)
url: https://www.jll.com/en-us/insights/data-centers-in-space
author: Ben Hamley, Andrew Batson, Daniel Thorpe (JLL)
published: 2026-06-09
captured: 2026-10-04
primary: none
---
# JLL — "Data centers in space"

## Reported (what the source says)
- Launch cost: Falcon 9 **$2,700/kg** today; Starship target **$200/kg**; JLL's cost-competitiveness threshold **$500/kg**.
- Global data-centre electricity 2025 ≈ **415 TWh**; installed capacity **~100 GW**, another **~100 GW** to be added by 2030. Cooling is **10–30%** of terrestrial opex; modern sites use **< 600,000 gallons** of water/yr.
- Orbit: **324** orbital launches in 2025; **17,000+** active satellites; **~44,000** tracked debris objects > 10 cm; Starcloud target **88,000** satellites; SpaceX FCC target **1,000,000**.
- Grid-connection waits: Mumbai ~2 years; Amsterdam/Tokyo up to **10 years**.
- Tech cycles: GPU generations **1–2 years** vs satellite life **5–7 years**.
- Conclusion: "functional specialization" — orbit for energy-intensive batch, ground for latency-sensitive. Caveats: Kessler risk, obsolescence, radiator capex, debris management unproven at scale.

## Primary (where the underlying document differs or adds)
- not checked

## Derived (our arithmetic — formula shown)
- Threshold spread across sources: JLL **$500/kg**, McKinsey (search snippet) **$500/kg**, ESPI (via TechCrunch) **< $400/kg**, Google **$200/kg**, Turyshev **$250–1,000/kg combined launch+build**, BCG target **$100/kg**. Today's rideshare list is **$7,000/kg** → **14× to 70×** above the thresholds.
- Obsolescence: a 5-year satellite spans **2.5–5 GPU generations**.

## Relevance to the Entrant
- The 10-year grid-connection queue in Amsterdam is a European terrestrial pain point the Entrant can cite — but the honest reading is that orbit solves EO latency, not Europe's grid.
- JLL's "functional specialization" framing is the sober version of the thesis; the Entrant fits the "data already in orbit" specialisation rather than batch AI.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]]
