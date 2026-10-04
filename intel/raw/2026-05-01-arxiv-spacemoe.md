---
type: intel
tags: [sdc, intel/raw, research/paper, space/orbital-compute, space/optical-isl, space/distributed-inference]
source: arXiv
url: https://arxiv.org/abs/2605.00515
author: Zhanwei Wang, Huiling Yang, Min Sheng, Khaled B. Letaief, Kaibin Huang (HKU / Xidian / HKUST)
published: 2026-05-01
captured: 2026-10-04
primary: self
---
# SpaceMoE: Realizing Distributed Mixture-of-Experts Inference over Space Networks

## Reported (what the paper claims)
- Problem: a large MoE LLM cannot fit one satellite, so experts and gateways are *placed* across a
  constellation; token generation latency = propagation over laser ISLs + per-satellite compute.
- **Two-level placement:** (1) partition the constellation along the orbit into ring-ordered subnets, one MoE
  layer each (last layer feeds first layer around the ring); (2) within a layer, prove that the optimal
  mapping sorts experts by activation probability against satellites by expected path latency (frequent
  experts on low-latency satellites).
- **Setup:** polar constellation 33 planes × 32 sats = **1,056 sats at 550 km, 87°**; up to 4 duplex ISLs
  per sat; ISL ≥ 100 Gbps so latency is propagation-dominated; ISL feasible only if angular rate < 0.12 rad/s;
  space-weather link survival probability 0.95 (Bernoulli).
- **Compute per satellite:** rad-tolerant SBC class — RAD5545 (4 GB / **3.7 GFLOPS**), Frontgrade SBC-2A72
  (8 GB / **10 GFLOPS**, used at 70 % → 7.28 GFLOPS "to avoid overheating"), SpaceCloud iX10 (24 GB /
  ≤ 26 TOPS). One expert per satellite (Switch Transformer 70 B params needs 140 GB FP16).
- **Result:** LLaMA-MoE-3.5B (32 layers × 8 experts, top-2, 36.3 TFLOP/forward at 4,096 tokens) on 8
  reasoning datasets: **1.02–1.07 s/token** for SpaceMoE vs 3.34–3.37 (random intra-layer + central
  gateway), 4.13–4.16 (random intra-layer), **5.28–5.30 s/token (random)** — "at least threefold" reduction.
- Latency rises monotonically with altitude; SpaceMoE improves with constellation size while baselines get
  worse; better link survival and ISL tracking reduce latency.

## Primary (method / assumptions a sceptic would attack)
- **~1 s per token** is two to three orders of magnitude off any commercial inference service; the paper
  demonstrates a placement principle on hardware that is irrelevant to orbital-data-centre economics
  (GFLOPS-class rad-hard SBCs).
- Model spread over 288 satellites spanning the globe: per-token round-trips of thousands of km are built
  into the architecture. This is the *opposite* of the single-satellite inference that
  [[intel/raw/2026-07-15-arxiv-van-berkel-cost-network-limits]] and
  [[intel/raw/2025-12-09-arxiv-tether-orbital-ai-data-centers]] argue is the only viable regime.
- Thermal and power enter only as a flat 70 % utilisation factor; no radiator or energy model.
- Link outage modelled as i.i.d. Bernoulli p = 0.95 "space weather" — not physical.

## Derived (our arithmetic — formula shown)
- Compute per satellite 7.28 GFLOPS vs one H100 (~2 PFLOPS dense FP16): ratio ≈ 2.7 × 10⁵ — i.e. the
  whole 1,056-satellite constellation has **~0.4 % of one H100** of compute. The latency floor is
  propagation (≈ 2.3 ms per 700 km hop) × ~32 layers × multi-hop ≈ hundreds of ms, consistent with ~1 s/token.

## Relevance to the Entrant
- Negative example: distributing a model across a sparse constellation turns light-speed latency into the
  product bottleneck. The Entrant's inference should **fit on one satellite** (or a co-flying pair with short ISLs).
- Useful catalogue of rad-tolerant compute options with memory/TOPS (RAD5545, SBC-2A72, SpaceCloud iX10
  ≤ 26 TOPS) for the "hardened fallback" tier of a payload trade.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]] (academic distributed-inference line; HKU/HKUST)
- [[intel/wiki/eo-edge-compute-value-chain]] (rad-tolerant compute catalogue)
