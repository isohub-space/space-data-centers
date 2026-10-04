---
type: intel
tags: [sdc, intel/raw, research/paper, space/eo-edge, space/optical-isl, space/downlink, economics/cost-model]
source: arXiv
url: https://arxiv.org/abs/2609.05427
author: Andrija Stanisic, Milos Gravara, Juan Luis Herrera, Stefan Nastic (TU Wien, Distributed Systems Group)
published: 2026-06-08
captured: 2026-10-04
primary: self
---
# Constella: A Novel Framework for Cost-Efficient Distributed AI Inference in LEO Space Data Centers

## Reported (what the paper claims)
- Use case is **Earth observation** (wildfire/disaster detection for rural regions without ground networks),
  not LLMs. Satellites split into **processors** (sensor + accelerator + ISL + downlink, price α) and
  **communicators** (ISL + downlink only, price β ≤ α), after SpaceDataHighway/EDRS role-splitting.
- Key physics asserted: ISLs reach **100 Gbps** and cost "significantly less energy than downlink
  transmission", so processors forward intermediate DNN tensors over ISL to whichever communicator has the
  earliest ground contact rather than waiting for their own pass.
- **OCRI** (offline MILP) jointly picks the DNN split layer l and the number of processors/communicators
  (X, Y) to minimise cost subject to per-orbit energy budgets; search space 2^N·|L| (Iridium N = 66,
  ResNet-50 182 layers → 1.35 × 10²²). Solves in 3.9–23.4 ms.
- **LIA** (online, gossip-based) picks the eligible communicator with minimum time-to-ground; 0.5–4 µs per
  decision.
- **Results** (real-constellation dataset, 5 scenario sizes; orbit T = 6,300 s, missed tasks penalised one
  orbit): cost down **1–2 orders of magnitude** vs "all satellites, midpoint split" (NB) and a traditional
  baseline (TB); success rate ≥ **81.9 %** (100 % in small scenarios); mean latency −1.1 to −2.7×
  (medium: **1,541 s vs 4,129 s NB / 3,518 s TB**; median 991 s); energy 3.5–45.5× below TB, up to 74× below
  NB (large: 23 satellites, **43.0 Wh vs 3,183.6 Wh**).
- Failure mode of naive design: a midpoint split of the DNN emits an **8.96 Mbit** intermediate tensor per
  image that overwhelms communicator buffers (NB success 10 % in the small scenario).

## Primary (method / assumptions a sceptic would attack)
- Costs α, β are abstract units; nothing is in dollars, so "two orders of magnitude cheaper" is relative to
  an over-provisioned strawman that activates every satellite.
- Inference time is assumed to fit within the capture interval Δt (excluded from optimisation); hardware
  heterogeneity and thermal duty cycles ignored.
- Single shared area-of-interest, uniformly interleaved roles, one ground station; full multi-hop ISL
  connectivity assumed.
- Energy figures (tens of Wh per orbit) describe CubeSat-class payloads; not transferable to kW compute.

## Derived (our arithmetic — formula shown)
- Latency floor: an orbit is 6,300 s, so the 991 s median means **most results reach ground within ~16 % of
  an orbit** after capture — the ISL-forwarding gain over "wait for your own pass" (~half an orbit, 3,150 s).
- 8.96 Mbit intermediate tensor vs a few kB of detections: the split point *is* the downlink product
  decision; a late split (full on-board inference) is what makes communicators cheap.

## Relevance to the Entrant
- Directly models the Entrant's value proposition: **time-to-insight for EO via on-board inference + ISL
  forwarding to the first available downlink**, and shows the role-split constellation is the cost-efficient
  shape.
- The result "split late, forward small" is an argument for full on-board inference (mask/alert output)
  rather than feature-compression splits.
- TU Wien's DSG (Nastic, Dustdar) is an active European academic group on exactly the Entrant's problem — a
  partnership/hiring pool.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]] (processor/communicator split; latency arithmetic; split-layer as product decision)
- [[intel/wiki/orbital-data-center-landscape]] (TU Wien DSG)
