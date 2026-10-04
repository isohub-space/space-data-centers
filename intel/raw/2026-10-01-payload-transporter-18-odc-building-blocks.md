---
type: intel
tags: [sdc, intel/raw, market/startups, company/cowboy-space, company/google, company/star-catcher, space/launch, space/power-beaming, hardware/tpu]
source: Payload
url: https://payloadspace.com/transporter-18-tests-the-building-blocks-of-orbital-data-centers/
author: Victoria Woodburn
published: 2026-10-01
captured: 2026-10-04
primary: none
---
# Payload — Transporter-18 tests the building blocks of orbital data centers

## Reported (what the source says)

**Mission**: SpaceX **Transporter-18** rideshare, Vandenberg, launched **2026-10-01**.

**Cowboy Space — Reason-1**
- Goal: beam solar power to Earth by laser; first beam attempt **late Oct 2026**; target **30–100 W**
  delivered; ground spot **10–20 m**. Future use: **optical data links for ODCs**.
- **Reason-2 (H1 2027): H200 GPUs** + data beaming.
- Company rocket with **1 MW data-center upper stage**, launch targeted **December 2028**.
- COO/CLO Joseph Yaffe: *"We're an orbital energy infrastructure company that's delivering power,
  computing power, and the ability to connect all of those things through laser infrared
  technology."*

**Google — Project Suncatcher MVP** (built by Planet Labs)
- Fridge-sized sat; **four Trillium TPUs** (≈ one server); **~1 kW** solar; chips power down every
  **15–20 min** to avoid overheating.
- Radiation: TPUs survived a 5-year-equivalent dose; silent errors **~1 per 3M queries**.
- Concept constellation: **50–100 kW per satellite**, **81-sat clusters within 1 km**.
- Cost projection: **$810/yr per kW** of solar at **$200/kg** launch (mid-2030s, ~180 Starship
  flights/yr). Follow-up sats **2027** with continuous operation.

**Star Catcher — Protostar**
- End-to-end in-space **power-beaming** demo to COTS solar panels; customers named: **Starcloud,
  Aethero**.

## Primary (where the underlying document differs or adds)
- Google figures match the arXiv paper already captured in
  [[intel/raw/2026-10-01-techcrunch-google-suncatcher-1800-starship-launches]].

## Derived (our arithmetic — formula shown)
- Reason-1 beam: 30–100 W delivered from a smallsat is **≤0.1 kW** — three orders of magnitude from
  anything that powers compute; it is a pointing/safety demo.
- Suncatcher duty cycle: if TPUs run 15 min then cool, effective compute availability ≈ **≤50%**
  on a 1 kW bus — thermal, not power, is the limiter at this scale.

## Relevance to the Entrant
- Oct 2026 is the month the **1 kW class** got real: Google (4 TPUs), Satlyt (software on
  TakeMe2Space), Cowboy (laser demo) all on one rideshare. The Entrant's first node will be judged
  against **~1 kW / fridge-size / 15-min duty cycle** as the public baseline.
- Google's 15-min thermal duty cycle shows **radiator design is the differentiator** for small
  EO-processing nodes; a node that runs continuously at 1 kW already beats Google's MVP.
- Star Catcher's beamed-power demo (customers Starcloud, Aethero) hints at a future where small
  compute nodes buy power from a beaming utility instead of carrying big arrays.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
- [[intel/wiki/orbital-compute-launch-economics]]
