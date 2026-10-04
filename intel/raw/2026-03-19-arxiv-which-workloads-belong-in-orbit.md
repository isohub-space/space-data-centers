---
type: intel
tags: [sdc, intel/raw, research/paper, space/eo-edge, space/downlink, space/orbital-compute, workload-placement]
source: arXiv
url: https://arxiv.org/abs/2603.20317
author: Durgendra Narayan Singh (independent researcher, Twin Falls ID)
published: 2026-03-19
captured: 2026-10-04
primary: self
---
# Which Workloads Belong in Orbit? A Workload-First Framework for Orbital Data Centers Using Semantic Abstraction

## Reported (what the paper claims)
- Workload-suitability matrix, five criteria scored 1–5 (latency tolerance, bandwidth intensity = raw→output
  reduction, fault tolerance, data locality, compute intensity), heuristic
  Suitability ∝ Compute × Bandwidth-reduction / Latency-sensitivity.
- **Scores (Table VII):** space RF signal processing **4.4**; 3D reconstruction from satellite imagery **4.2**;
  **EO preprocessing 4.2**; orbital nav/timing 3.4; batch LLM inference 3.2; **LLM training 3.0**; satellite
  telemetry analytics 2.6; comms infrastructure 2.8. Tier-1 (> 4.0) "should define product positioning for
  early space compute companies".
- Constraints stated: fibre latency ~5 µs/km (20–30 ms US cross-continent); LEO downlink/uplink asymmetry
  "often 10:1 or higher" (illustrative 100 Mbps down / 5 Mbps up); dawn-dusk SSO ~90–95 % annual sunlight.
- **EO prototype (Sentinel-2 L2A, Seattle & Bengaluru, 2025):** SCL-derived cloud mask → vector cloud
  polygons / grid "patch polygons". Ten-scene batch raw ≈ **31.46 MB**; patch-polygon payload
  **0.001–0.098 MB** by cloud regime → **99.69–99.996 % reduction**. At 50 Mbps: 5.03 s raw vs 0.014 s
  polygons. In cloudy scenes (~80 % cover) the largest connected deck holds 95–97 % of cloudy pixels.
- **3D reconstruction prototype (Maxar/Vantor open data, Los Angeles):** two 3,500 × 3,500 pan tiles
  (305.99 MB) → 1.57 MB of depth/DSM products (**99.49 %**), with only 11.45 % usable disparity coverage;
  6,517 ORB matches, 1,219 RANSAC inliers.
- Three-phase roadmap: P1 GPU + intermittent downlink (EO preprocessing, RF classification); P2 + cheap
  sustained power (full MVS/3D, batch LLM inference "economical for summarisation/alerting on down-selected
  data"); P3 + laser ISLs (constellation-level fusion). LLM training rated × / × / △ across all phases.

## Primary (method / assumptions a sceptic would attack)
- Scores are qualitative, equal-weighted, single-author judgements; no cost model.
- The EO "99.7–99.99 %" is for a *deterministic* cloud mask on resampled AOI crops, output as polygons —
  it measures the compression of a cloud map, not the value of the discarded clear pixels. A customer
  who wants imagery still needs the imagery (compare the clear-pixel-deletion finding in
  [[intel/raw/2026-08-02-arxiv-clear-weighted-bit-allocation]]).
- No learned inference, no operational overheads (packetisation, encryption, FEC), no energy model.

## Derived (our arithmetic — formula shown)
- Downlink time ratio: 5.03 s / 0.014 s ≈ **360×** effective throughput gain at the mixed/cloudy regimes;
  up to 31.46 / 0.001 ≈ 3 × 10⁴× for clear scenes where the artefact is nearly empty.
- Semantic-reduction ratios compared across the literature: cloud polygons 10²–10⁴× (this paper), VLM
  text summary ~2 × 10² vs preview / 10⁵ vs full image
  ([[intel/raw/2026-08-07-arxiv-summarize-first-onboard-vlm]]), clear-weighted codec 1.4–2.6× at equal
  clear-region PSNR ([[intel/raw/2026-08-02-arxiv-clear-weighted-bit-allocation]]). The spread is the
  difference between "send a decision" and "send the picture".

## Relevance to the Entrant
- Independent ranking that puts **EO preprocessing/inference in the top tier of orbital workloads and LLM
  training at the bottom** — a citable third-party framing for the Entrant's positioning.
- Reinforces that the Entrant's product is the *semantic artefact* (mask, polygon, alert, DSM) and that the
  value scales with cloud fraction and revisit — most of the bytes an EO constellation captures are clouds.
- Phase model gives a sensible staging: single-satellite EO inference now; cross-satellite fusion only
  once ISLs are on the bus.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]] (suitability tiers; semantic-reduction ratio table)
- [[intel/wiki/orbital-data-center-landscape]]
