---
type: intel
tags: [sdc, intel/raw, research/paper, space/eo-edge, space/downlink, compression]
source: arXiv
url: https://arxiv.org/abs/2608.01457
author: Alireza Furutanpey, Qiyang Zhang, Yujie Huang, Philipp Raith, Schahram Dustdar (TU Wien / Coovally / PKU / BUPT)
published: 2026-08-02
captured: 2026-10-04
primary: self
---
# Clear-Weighted Bit Allocation for Satellite Downlinks

## Reported (what the paper claims)
- **Detect-then-drop cloud filtering loses clear ground.** On AllClear (Sentinel-2) the **CloudScout 70 %
  frame rule deletes 5.36 %** of captured clear pixels (3.08 pts from detector false positives, 2.28 pts
  "clear slivers" inside correctly-discarded cloudy frames); the **Earth+ 50 % rule deletes 9.76 %**; a
  pixel-removal codec 7.36 %. On expert-labelled **CloudSEN12+: 21.19 % (CloudScout) and 28.74 % (Earth+)**,
  mostly false positives (16.95 / 17.80 pts). At 90 % mean cloud cover: 21.4 ± 1.7 % / 30.4 ± 1.8 %.
- **Fix:** train a learned codec with reconstruction loss weighted by (1 − cloud probability), so bits
  flow to clear ground without any onboard cloud detector or transmitted cloud map. Results at matched
  clear-region PSNR: **−39.0 % bytes vs the same codec cloud-agnostic, −47.8 % vs ELIC, −42.0 % vs
  Minnen-2018, −62.2 % vs JPEG 2000**; 5.09× more image-latent bits per clear pixel than per cloudy pixel.
  Transfer to CloudSEN12+ without retraining: −26.4 %. Progressive two-layer stream: 21 % fewer bytes.
- **Scheduler (DPMW):** causal ranking of base/refinement layers by estimated clear content, residual bytes
  and two deadlines, over orbit-derived Sentinel-2B contacts to Svalbard (5° mask). In interrupted-contact
  cohorts deadline-full clear-content delivery rises **38.1 % → 83.5 %**, reaching **83.6 % of a certified
  clairvoyant bound**.
- **Onboard cost (Jetson Orin Nano Super, 15 W, FP16, no TensorRT):** optimised full encoder **19.9 ms p99,
  103 mJ per 256×256 frame** (reference 47 ms / 148 mJ); AGX Orin 6.0 ms / 18 mJ. The standalone cloud
  detector that the drop rules need costs **2.2–6.8× the encoder's energy**. Code released (RANSKit).

## Primary (method / assumptions a sceptic would attack)
- 256 × 256 RGB crops with machine-generated AllClear masks; real missions are 12-bit multispectral at
  10,000+ pixel swath — encoder cost scales with pixels (~1,500× more per Sentinel-2 granule).
- Clear-region PSNR is the quality metric; downstream task accuracy (the authors' own FOOL line) is deferred.
- Deletion percentages depend on the frozen detector's false-positive rate; a better detector shrinks the
  argument.
- One ground station (Svalbard); multi-station networks relax deadlines.

## Derived (our arithmetic — formula shown)
- Energy per Sentinel-2-scale granule (10,980² px ≈ 1,840 crops): 1,840 × 103 mJ ≈ **190 J ≈ 53 mWh** per
  scene on Orin Nano — trivial against a kW-class payload, meaningful on a 10 W CubeSat budget.
- Loss from naive frame dropping on expert labels: ~21–29 % of clear pixels ≈ **one in four–five
  sellable pixels thrown away** by the heritage Φ-Sat-1/CloudScout approach.

## Relevance to the Entrant
- **Direct warning:** the canonical "AI cloud filter on board" story (Φ-Sat-1) destroys 5–29 % of clear
  imagery through false positives. The Entrant's time-to-insight pitch must not be "drop cloudy frames"; it should
  be content-aware allocation + inference products.
- The TU Wien/PKU/BUPT group (Furutanpey, Dustdar, Zhang, Xu) is the leading academic team on EO downlink
  bottlenecks; their released tooling is a head start.
- Gives measured Jetson-class encoder energy/latency numbers for payload sizing.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]] (clear-pixel deletion rates; codec savings; Orin energy numbers)
