---
type: intel
tags: [sdc, intel/raw, research/paper, space/eo-edge, onboard-inference, image-quality]
source: arXiv (OBPDC 2026)
url: https://arxiv.org/abs/2609.38265
author: Adrien Dorise, Marjorie Bellizzi, Stéphane May (CNES / IRT Saint-Exupéry, Toulouse)
published: 2026-09-29
captured: 2026-10-04
primary: self
---
# Raw Imagery Impacting Your AI: Should You Care?

## Reported (what the paper claims)
- Question: how much Level-1 ground processing (restoration, resampling, radiometric correction) does an
  onboard detector actually need? Simulated raw-like degradations of **Maxar 50 cm** pansharpened imagery
  (47 scenes, 24,000+ ships, 53 classes): MTF at Nyquist 0.25 → 0.005, signal-dependent SNR (100,250) →
  (5,10), GSD 100 and 200 cm. Detectors: **YOLOv5s, YOLOX-S, NanoDet**, 100 epochs each.
- **GSD is the consistent driver:** 100 → 200 cm costs **3.9–7.8 AP50 points** (mean −6.7 YOLOv5s, −5.0
  YOLOX-S; NanoDet same trend in 22/23 cases). Best AP50 ≈ 0.41 (YOLOv5s, MTF 0.25, GSD 100).
- **MTF / SNR alone are tolerated over a wide range:** at 100 cm, SNR sweeps are "relatively stable… small
  and non-monotonic"; MTF harms only at very low values. Severe **combined blur + noise** is the worst regime
  (e.g. YOLOv5s AP50 0.412 → 0.230 at 100 cm; 0.311 → 0.166 at 200 cm).
- Conclusion: "small-to-moderate degradations do not cause a sudden breakdown… some optical requirements
  could potentially be relaxed"; sensor/processing/AI should be co-designed from task-level curves, and
  onboard restoration (their ConvBEERS) or degradation-aware detectors (TriCCOT) chosen per mission.

## Primary (method / assumptions a sceptic would attack)
- **Single training run per operating point**; no seeds/confidence intervals — the authors flag this as the
  main limitation, and many neighbouring points reverse order.
- Simulated degradation of already-processed Level-2A imagery, not true Level-0; geometric artefacts
  (smile, misregistration, stripe noise) absent.
- Ship detection only; cloud/wildfire tasks have different spectral sensitivities.
- 50 cm commercial imagery; most onboard-AI missions fly 3–10 m sensors where GSD is fixed by the optics.

## Derived (our arithmetic — formula shown)
- Doubling GSD halves linear resolution and quarters pixels per ship; the measured ~6-point AP50 drop (≈ 15 %
  relative) is mild compared with the 4× data reduction, suggesting **onboard inference on binned imagery**
  is a cheap way to cut compute 4× when the target class is large (ships), not for small objects.
- Compute saving from skipping restoration ≈ one full-frame deconvolution/resampling pass per scene — on
  Jetson-class hardware comparable to the detector itself, so "infer on raw" can roughly halve the onboard
  pipeline.

## Relevance to the Entrant
- Supports the design choice of **inferring directly on minimally processed data** on board (as ESA's raw
  Sentinel-2 vessel-detection line also does), avoiding a full L1 processing chain in orbit — fewer FLOPs,
  less latency, same product quality for mid-size targets.
- CNES / IRT Saint-Exupéry are the French institutional centre of gravity for onboard-AI image-quality
  trade-offs; relevant for any ESA/CNES-funded demonstration.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]] (raw-vs-restored inference trade; GSD sensitivity)
