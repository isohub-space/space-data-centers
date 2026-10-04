---
type: intel
tags: [sdc, intel/raw, research/paper, space/eo-edge, space/downlink, onboard-inference, vlm]
source: arXiv
url: https://arxiv.org/abs/2608.06959
author: Junghwan Park, Sangcheol Sim, Woojin Cho, Darongsae Kwon (TelePIX, Seoul)
published: 2026-08-07
captured: 2026-10-04
primary: self
---
# Summarize First, Download Later: Onboard VLMs for Bandwidth-Efficient Earth Observation

## Reported (what the paper claims)
- Protocol: (1) onboard quantised VLM emits a natural-language scene summary as a small JSON packet;
  (2) ground operators ask targeted VQA questions over the low-rate link; (3) full-resolution imagery or crops
  are downlinked only after relevance is confirmed. Downlink becomes "an active, semantics-aware dialogue".
- **Bandwidth (Table III):** Phase-1 text packet **≈ 485 B**; RSICD/NWPU preview PNGs 97–105 kB
  (**≈ 2 × 10²×**); illustrative full-res EO image 50 MB (**≈ 1 × 10⁵×**).
- **Models on Jetson Orin Nano:** Gemma-3 4B (4-bit), LFM 2.5 VL 1.6B (8-bit), Qwen3-VL 2B (8-bit), no
  fine-tuning. **VQA accuracy:** RSVQA-LR 69.3–73.6 %, RSVQA-HR 52.8–62.5 % (Qwen3-VL best). Captioning
  BERTScore-F1 0.886–0.901; CLIPScore 0.28–0.31.
- **Runtime (Table IV):** LFM2.5 **29.1 s wall, 1.6 GB peak RSS, 3.4 s load, 19.9 tok/s**; Qwen3-VL 51.6 s,
  2.2 GB, 14.3 s load, 16.5 tok/s; Gemma-3 **106.8 s, 3.5 GB, 43.2 s load**, 15.5 tok/s. "Fast loading and
  low memory footprint are critical."
- Positions itself against image-centric selective downlink (Φ-Sat-1 cloud filter, WorldFloods masks,
  RAVÆN change detection, CubeSat prioritisation) as adding operator-interpretable semantics and uncertainty.
- Open challenges: domain shift, uncertainty-aware generation, energy-efficient multimodal inference.

## Primary (method / assumptions a sceptic would attack)
- Wall-clock **30–107 s per image** on a Jetson is dominated by model load — fine for a persistent service,
  but the per-image inference still runs at 15–20 tok/s, i.e. several seconds per summary; a 10-scene pass
  is a minute of GPU time at ~15 W.
- VQA accuracy ~60–74 % on benchmark datasets; a wrong "no smoke" answer suppresses the download of the only
  image that mattered. No calibration/uncertainty reported.
- Bandwidth savings assume the ground *trusts* the summary; the human-in-the-loop VQA round trip itself costs
  a contact window (minutes to hours), eroding the time-to-insight gain.
- Datasets (RSICD, NWPU, RSVQA) are RGB aerial/low-res; no multispectral or SAR.

## Derived (our arithmetic — formula shown)
- Power-energy per summary (Orin Nano ~15 W, LFM2.5 ~26 s post-load): ≈ **390 J ≈ 0.11 Wh per image** — a
  10-scene pass ≈ 1.1 Wh, i.e. the VLM costs ~4× the clear-weighted *encoder* of
  [[intel/raw/2026-08-02-arxiv-clear-weighted-bit-allocation]] per scene-equivalent, still small on a kW bus.
- Ratio vs the BUPT thermal finding ([[intel/raw/2026-08-21-arxiv-bupt-ai-infrastructure-in-space]]): a
  2 B VLM tripped a 55 °C shutdown in **48 s** on a CubeSat radiator; LFM2.5's 29 s wall time fits inside
  that window, Qwen3-VL's 52 s does not. Model choice is a thermal decision.

## Relevance to the Entrant
- Working demonstration of the **"send meaning, then pixels on demand"** product that a GPU-class orbital
  node enables and a Myriad-class one cannot ([[intel/raw/2026-09-11-arxiv-aquacubeai-phisat2]]).
- Quantifies the realistic small-VLM envelope on Jetson-class hardware (1.6–3.5 GB, 15–20 tok/s, 60–74 % VQA)
  — a baseline for the Entrant's own payload benchmarks.
- TelePIX (Korean EO analytics company) is a commercial competitor/partner moving onto the same ground.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]] (text-first downlink ratios; small-VLM onboard envelope)
- [[intel/wiki/orbital-data-center-landscape]] (TelePIX)
