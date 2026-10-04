---
type: intel
tags: [sdc, intel/raw, market/incumbents, space/orbital-compute]
source: Tom's Hardware (syndicated on Yahoo Tech)
url: https://tech.yahoo.com/science/articles/jeff-bezos-envisions-space-based-174729430.html
author: Anton Shilov
published: 2025-10-03
captured: 2026-10-04
primary: "Bezos on stage at Italian Tech Week, Turin (2025-10-03) with John Elkann; no transcript opened. Later context: Interesting Engineering 2025-12-11 (https://interestingengineering.com/space/orbital-ai-data-centers) reporting WSJ that Blue Origin has worked on orbital data-centre tech for over a year."
---
# Tom's Hardware — "Jeff Bezos envisions space-based data centers in 10 to 20 years"

## Reported (what the source says)
- Bezos: *"One of the things that is going to happen in the next — it is hard to know exactly when, it is 10+ years, and I bet it is not more than 20 years — we are going to start building these giant gigawatt data centers in space."*
- Cooling rationale as stated by Bezos: temperatures "from −120 °C in direct sunlight to −270 °C in the shadow, which greatly simplifies cooling."
- Tom's Hardware's own back-of-envelope for a GW-class facility: **2.4–3.3 million m²** of solar array; launch cost **$13.7–17.1B** (optimistic) to **$25B+** (conservative); **150+ launches** with current vehicles; radiators "tens of billions more". Verdict: commercially unfeasible today.

## Primary (where the underlying document differs or adds)
- Interesting Engineering (2025-12-11, Chris Young): Bezos — *"We will be able to beat the cost of terrestrial data centers in space in the next couple of decades"*; *"These giant training clusters … will be better built in space, because we have solar power there, 24/7."* WSJ reported Blue Origin has been working on orbital data-centre technology for > 1 year; Bezos also founded AI startup Project Prometheus.
- Note the physics error in the quote: the −120 °C/−270 °C figures describe radiative equilibrium of passive bodies, not a heat sink; vacuum has no convective cooling (see IEEE Spectrum thermodynamics note).

## Derived (our arithmetic — formula shown)
- 2.4–3.3 M m² for ~1 GW → **2,400–3,300 m²/MW** of PV — vs Turyshev's 5,640 m²/MW (BOL) and Google's implicit higher efficiency; Tom's assumes ~300–400 W/m² of array.
- Bezos's window (2035–2045) is consistent with Google's (<$200/kg "by mid-2030s") and inconsistent with Musk's (2–3 years).

## Relevance to the Entrant
- Bezos explicitly talks about **training clusters**, which no technical analysis supports (radiation SDC, ISL bandwidth) — a tell that the founder narrative is ahead of the engineering.
- Blue Origin's own launcher (New Glenn) is grounded after the May 2026 pad explosion (see New Glenn note); Bezos's timeline has no near-term launch supply behind it.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
