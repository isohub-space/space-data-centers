---
type: intel
tags: [sdc, intel/raw, research/paper, space/eo-edge, onboard-inference, phisat]
source: arXiv
url: https://arxiv.org/abs/2609.12744
author: Pietro Di Stasio, F. Razzano, E. Liparulo, Gabriele Meoni (ESA Φ-lab), N. Longépé (ESA), D. Tapete (ASI), P. Gamba, G. Schirinzi, S. L. Ullo (Univ. of Sannio et al.)
published: 2026-09-11
captured: 2026-10-04
primary: self
---
# AquaCubeAI — Powered Monitoring of Turbidity on-board Φsat-2

## Reported (what the paper claims)
- Motivation stated bluntly: conventional EO workflows "rely on downlink and ground processing, introducing
  latency"; CMEMS-style bulk daily processing "further restricts responsiveness" to turbidity events.
- Model: compact **MLP regressor** on the channel-wise mean of a 20×20×8-band simulated Φsat-2 L1C patch →
  turbidity (FNU); reformulated with 1×1 convolutions for dense maps and a **TUR > 100 FNU anomaly mask** for
  "onboard decision logic… prioritised for downlink". Labels from CMEMS HR-OC products over four European
  marine macro-regions; leakage-aware spatial block split.
- Accuracy (5 seeds): test **RMSE 2.70 ± 0.17 FNU, MAE 1.25**, bias −0.55; external 2024 hold-out
  **RMSE 1.59 ± 0.15 FNU**. A lightweight CNN did *worse* (3.51 vs 2.47 test RMSE).
- **Onboard hardware: Intel Myriad 2 VPU** (the Φsat-2 flight accelerator) via OpenVINO: **8.51 ms per 20×20
  patch (117 inferences/s)**; all valid patches of a 4,096 × 4,096 scene in **215.6 s**; CPU and Myriad outputs
  agree.
- Scope limits acknowledged: simulated Φsat-2 imagery only ("validation on real in-orbit Φsat-2
  observations remains future work"); CMEMS labels are themselves model products; L1C (no atmospheric
  correction) inputs; weaker in the > 100 FNU tail.
- Cites the Φ-lab/ESA heritage line: Φsat-1 cloud filtering, Φsat-2 multi-app framework, onboard vessel
  detection on raw Sentinel-2, volcanic eruption and HAB detection; ref [16] (Barretta et al. 2026, IEEE GRSM)
  is a review of onboard-AI processing toward "real-time Earth system intelligence".

## Primary (method / assumptions a sceptic would attack)
- A pixel-mean 8-band MLP is tiny; the 8.5 ms/patch figure says more about Myriad 2's per-call overhead
  than about model cost (215 s per scene is slow for a trivially parallel map).
- Simulated-data training with simulated-data evaluation; real sensor noise, misregistration and atmospheric
  variability untested.
- No downlink-savings number is measured; the "anomaly mask for selective downlink" is asserted as the
  benefit.

## Derived (our arithmetic — formula shown)
- Patches per scene: 215.6 s / 8.51 ms ≈ **25,300 patches** ≈ 10 M pixels evaluated (of 16.8 M), i.e. the
  onboard pass covered ~60 % of the scene (water-masked). At 117 patches/s a full 4k² scene is ~3.6 min on
  Myriad 2 — acceptable for turbidity, too slow for anything per-frame.
- Anomaly-mask payload vs scene: a 205×205 binary mask ≈ 5 kB vs 4,096² × 8 × 12 bit ≈ 200 MB raw → ~4 × 10⁴×
  reduction when only the mask is sent (derived, not in paper).

## Relevance to the Entrant
- Shows what ESA's **flagship onboard-AI platform actually runs**: a Myriad 2 at ~100 inferences/s on 20×20
  patches. The Entrant's "orbital data centre" differentiation is the gap between this and GPU-class inference
  (minutes → seconds per scene, VLM-class models).
- Water-quality alerts for European coastal regulators (CMEMS users) is a concrete, latency-sensitive EO
  product line with an existing institutional customer base.
- ESA Φ-lab (Meoni, Longépé) is the European gatekeeper for onboard-AI credibility; this paper is a map of
  who to talk to.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]] (Φsat-2 compute baseline; latency-sensitive marine products)
- [[intel/wiki/orbital-data-center-landscape]] (ESA Φ-lab)
