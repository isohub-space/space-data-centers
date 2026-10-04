---
type: intel
tags: [sdc, intel/raw, market/europe, space/eo-edge, space/onboard-ai, vendor/ubotica, market/maritime]
source: Ubotica Technologies (company blog interview)
url: https://www.ubotica.com/news/interview-sean-mitchell-ubotica-cognisat-6-mission
author: Ubotica (interview with Sean Mitchell, COO)
published: 2024-03-12
captured: 2026-10-04
primary: none (company interview; Open Cosmos/Ubotica joint release not opened)
---
# Ubotica: "CogniSAT-6 is one of the most intelligent satellites sent into space"

## Reported (what the source says)
- Ubotica founded **2016** (Dublin); CogniSAT-6 launched **4 Mar 2024** on Transporter-10 (Exolaunch dispenser); built/operated by **Open Cosmos**; hyperspectral imaging co-funded by **UK Catapult**; expected life **3+ years**.
- Onboard AI functions: cloud removal, **6–10× image compression**, "Live Earth Intelligence" insight extraction, autonomous retargeting, **tip-and-cue** to trailing satellites, and a first-of-kind **bidirectional mobile-app link**.
- Latency claim: insights **"within 5 minutes of image capture"**.
- Applications listed: maritime security, illegal fishing, oil spills, disaster response, illegal logging, agriculture, pipelines, emergency services.
- No chip model, TOPS, power or customer names.

## Primary (where the underlying document differs or adds)
- not checked. Later funding (SpaceNews, 23 Jun 2026, paywalled — see [[2026-06-23-spacenews-ubotica-11m-series-a]]): **$11 M Series A** to scale the **maritime-intelligence** platform. ESA InCubed page (opened) credits Ubotica's "Orbital AI" with "hundreds of thousands of AI inferences in orbit" and "more than 30 Earth observation models on board satellites". Ubotica is also a tenant on Planetek's AI-eXpress (see [[2025-11-28-planetek-ai-express-third-satellite]]).

## Derived (our arithmetic — formula shown)
- 6–10× compression on a CubeSat X-band link is equivalent to 6–10× more usable scenes per pass; combined with cloud removal (global cloud fraction ~60–70%, our general assumption), useful-data-per-pass rises **~15–30×** vs raw downlink.
- "5 minutes" is only achievable if a link exists within 5 min — i.e. it presumes a relay (Ubotica's app link, Kepler, IRIS²) or a pass; the number is a **best-case with connectivity**, not an orbit-average.

## Relevance to the Entrant
- Ubotica is the **most direct European competitor** to the Entrant's "EO time-to-insight" service: Myriad-based edge AI, own satellite, maritime vertical, VC-funded ($4 M seed → $11 M Series A).
- Its pivot from chips to a **vertical maritime-intelligence product** is the lesson: the market pays for a domain answer (vessel detections), not for compute.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]]
- [[intel/wiki/orbital-data-center-landscape]]
