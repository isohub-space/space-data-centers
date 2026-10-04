---
type: intel
tags: [sdc, intel/raw, market/incumbents, market/sceptics, space/orbital-compute]
source: NPR (syndicated via KPBS)
url: https://www.kpbs.org/news/science-technology/2026/10/01/google-launches-project-suncatcher-a-step-towards-ai-data-centers-in-space
author: John Ruwitch, Geoff Brumfiel (NPR)
published: 2026-10-01
captured: 2026-10-04
primary: none
---
# NPR — "Google launches Project Suncatcher, a step towards AI data centers in space"

## Reported (what the source says)
- Prototype is **refrigerator-sized**, carries **four TPUs**, built with **Planet Labs**.
- Runs Google's open-weight **Gemma** model "for 15 minutes at a time" answering simple queries; cooling via **heat pipes and radiators**; Google calls cooling "a crucial research challenge".
- 2027: two more satellites to test **laser** inter-satellite links.
- 2028: **SpaceX** expects to deploy "orbital AI compute satellites" per its SEC filing.
- Travis Beals (Google): *"I don't see this being something where it's cheaper to do this in the next five years."*
- Brandon Lucia (Carnegie Mellon): complexities in orbit are "amplified by a factor of 10, maybe a factor of 100", stressing the impossibility of routine maintenance.

## Primary (where the underlying document differs or adds)
- not checked

## Derived (our arithmetic — formula shown)
- Duty cycle: 15 min bursts implies the bus cannot sustain the TPU load thermally; if bursts are hourly, duty ≈ 15/60 = **25%** — the thermal envelope, not radiation, is the binding constraint on this first flight.

## Relevance to the Entrant
- Google's own lead puts cost parity **beyond 5 years**; the orbital-compute "race" is a 2030s story. The Entrant's window is the next 5 years with workloads that are valuable *because* they are in orbit (EO time-to-insight), not because they are cheaper.
- A 1 kW-class bus running inference in 15-minute bursts is close to the Entrant's operating regime — Google is effectively publishing the Entrant's thermal problem.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
