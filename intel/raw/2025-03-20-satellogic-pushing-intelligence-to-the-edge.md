---
type: intel
tags: [sdc, intel/raw, space/eo-edge, space/onboard-ai, market/latency, vendor/satellogic]
source: Satellogic (company blog)
url: https://satellogic.com/2025/03/20/pushing-intelligence-to-the-edge-satellogics-vision-for-ai-powered-earth-observation/
author: Satellogic
published: 2025-03-20
captured: 2026-10-04
primary: none
---
# Satellogic: "Pushing intelligence to the edge" — AI-first EO constellation

## Reported (what the source says)
- Claims a **13-year track record of flying GPUs in space**; announces "the industry's first **AI First** satellite constellation".
- Onboard pipeline: a **real-time analysis pipeline examines every frame as it's captured**; a **rolling onboard archive of several days** of imagery; aggressive compression of non-critical areas; selective transmission.
- Latency: time-sensitive responses cut **"from days to minutes"**; alerts/priority data sent **over low-bandwidth channels** while full imagery follows later.
- Use cases: deforestation, resource management, infrastructure, disaster damage assessment.
- No GPU model, satellite count, customer names or measured numbers.

## Primary (where the underlying document differs or adds)
- not checked

## Derived (our arithmetic — formula shown)
- "Alert over low-bandwidth channel" implies an always-available narrowband link (e.g., Iridium/IoT-class or relay) — the **alert path and the imagery path are decoupled**. That is the architecture pattern: tiny insight now, big pixels later.

## Relevance to the Entrant
- A vertically integrated operator (Satellogic) is doing in-orbit insight on its own fleet; the Entrant's addressable market is the **operators who cannot** (small/national/institutional fleets) — or the cross-fleet layer no single operator can build.
- "Days to minutes" is the standard claim across Satellogic, Ubotica, Little Place Labs, Planet; **nobody publishes a measured orbit-average latency**. A credible measured number would differentiate the Entrant.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]]
