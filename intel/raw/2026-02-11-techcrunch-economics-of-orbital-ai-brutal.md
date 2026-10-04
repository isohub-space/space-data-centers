---
type: intel
tags: [sdc, intel/raw, market/sceptics, space/launch, space/orbital-compute]
source: TechCrunch
url: https://techcrunch.com/2026/02/11/why-the-economics-of-orbital-ai-are-so-brutal/
author: Tim Fernholz
published: 2026-02-11
captured: 2026-10-04
primary: "Andrew McCalip (Varda Space Industries) public orbital data-centre cost calculator; SpaceX FCC filing (Jan 2026); Google arXiv:2511.19468"
---
# TechCrunch — "Why the economics of orbital AI are so brutal"

## Reported (what the source says)
- McCalip calculator: a **1 GW** orbital data centre ≈ **$42.4B**, ~**3×** a ground equivalent.
- Satellite manufacturing today ≈ **$1,000/kg**; launch must fall to **$200/kg** from Falcon 9's **$3,600/kg** — an **18-fold** reduction.
- Power cost: ground data centres **$570–3,000/kW/yr**; Starlink satellites imply **$14,700/kW/yr**.
- Space solar **5–8×** more productive than ground; sun visibility up to **90%** of the time; silicon panels last **~5 years** in orbit.
- Inter-satellite laser links today **~100 Gbps** max vs terrestrial TPU fabrics at hundreds of Gbps.
- SpaceX FCC filing implies **~100 kW per tonne**, about double today's Starlink.
- AWS CEO Matt Garman (rendered "Gorman" in the extract): *"There are not enough rockets to launch a million satellites yet… the cost of getting a payload in space today, it's massive. It is just not economical."*

## Primary (where the underlying document differs or adds)
- Google's preprint claims $810/kW/yr at $200/kg — the gap between $14,700 (Starlink today) and $810 (Google 2035) is the entire thesis.
- McCalip's calculator not opened; figures as reported.

## Derived (our arithmetic — formula shown)
- $14,700 ÷ $810 = **18×** improvement in launched-power price required — consistent with the 18× launch-cost reduction quoted.
- At 100 kW/t, 1 GW = **10,000 t** = **50 Starship flights at 200 t** — before replacement.

## Relevance to the Entrant
- Amazon's CEO publicly rejecting near-term orbital compute means one of the three hyperscalers is **not** coming for the small-payload market; the field is Google (research), SpaceX (Starlink-adjacent), and startups.
- The 100 Gbps ISL ceiling matters for the Entrant: on-orbit processing value is largest precisely where you *avoid* moving raw data at all.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]]
