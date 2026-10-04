---
type: intel
tags: [sdc, intel/raw, space/eo-edge, market/downlink, research/arxiv]
source: arXiv (TU Wien et al.)
url: https://arxiv.org/html/2403.16677v3
author: Alireza Furutanpey, Qiyang Zhang, Philipp Raith, Tobias Pfandzelter, Shangguang Wang, Schahram Dustdar
published: 2025-05-01
captured: 2026-10-04
primary: "this is the primary (arXiv:2403.16677v3)"
---
# FOOL: Addressing the downlink bottleneck in satellite computing with neural feature compression

## Reported (what the source says)
- Per-pass data volumes: **~12 GB (Planet Dove)**, **90 GB (WorldView-3)**, **40 GB (Sentinel-3A/B)**; worked example **410 GB per pass** for a Sentinel-2-configured satellite.
- Pass duration: **120–600 s** depending on constellation/station.
- Downlink rates: **Planet Dove 160 Mbps**, **WorldView-3 1,200 Mbps**, **Sentinel-3 560 Mbps**, **Landsat-8 440 Mbps**.
- FOOL (task-agnostic learned feature compression): up to **2.1× lower bitrate** than prior split-computing methods; **46–77% lower bitrate** than mid-quality learned image codecs; prediction-lossless (≤1% mAP@50 drop) at **0.18–0.24 bits/pixel**; claims enabling "downlinking over **100×** the data volume" vs raw.
- Onboard testbed power cap **15 W**; devices: Jetson Nano Orin (512 CUDA), TX2 (256), Xavier NX (384).

## Primary (where the underlying document differs or adds)
- this is the primary

## Derived (our arithmetic — formula shown)
- Sentinel-3 pass: 560 Mbps × 600 s ÷ 8 = **42 GB per 10-min pass** — matches the paper's 40 GB; a 10-min pass is the long end, so many passes move far less.
- Planet Dove: 160 Mbps × 600 s ÷ 8 = **12 GB** — consistent. If a Dove images ~1–2 TB/day (industry figure quoted in search summaries, not opened), one pass clears **<1%** of the daily take; multiple passes/day and store-and-forward are mandatory.
- Raw 12-bit multispectral at ~2 bits/pixel after compression → **6× reduction**; FOOL's 0.2 bpp → **~60×**. The 100× claim is the right order of magnitude for task-agnostic feature compression at the edge.

## Relevance to the Entrant
- Gives **citable, per-satellite numbers** for the downlink bottleneck (Mbps, GB/pass, seconds/pass) — exactly what the Entrant's deck lacks if it relies on "terabytes per day" hand-waves.
- Shows the low-power path: **15 W Jetson-class** compute is enough for 100× effective downlink gain. The compute need not be a data centre; the *coordination and latency* layer is where the Entrant can add value above commodity compression.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]]
