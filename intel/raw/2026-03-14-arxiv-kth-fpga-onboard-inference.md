---
type: intel
tags: [sdc, intel/raw, research/paper, space/eo-edge, hardware/fpga, onboard-inference]
source: arXiv
url: https://arxiv.org/abs/2603.14091
author: Pedro Antunes, M. I. Al Hafiz, J. Ekelund, E. Dineva, G. Miloshevich, P. Gonidakis, Artur Podobas (KTH / KU Leuven)
published: 2026-03-14
captured: 2026-10-04
primary: self
---
# Evaluating Four FPGA-accelerated Space Use Cases based on Neural Network Algorithms for On-board Inference

## Reported (what the paper claims)
- Platform: AMD **ZCU104** (Zynq UltraScale+ ZU7EV MPSoC, 504k logic cells, 38 Mb BRAM, 1,728 DSP) — chosen
  because its fabric size matches rad-tolerant Kintex UltraScale XQR parts. Two toolchains: Vitis AI (DPU
  B4096, INT8) and Vitis HLS (FP32, naive dataflow, 100 MHz).
- Four heliophysics/space-science NNs (24 to 3.06 M parameters): VAE encoder for solar magnetograms
  (128×256 → 6 floats, **1:16,384 compression**), CNetPlusScalar X-ray flux regressor (918 MFLOP), multi-
  ESPERTA SEP predictor (24 params), MMS plasma-region classifiers with 3D convolutions.
- **Vitis AI:** VAE **606.65 FPS, 24.06× over the ARM A53**, 5.75 W MPSoC, **9.48 mJ/inference** (CPU 109 mJ);
  CNetPlusScalar **163.5 FPS, 34.16×**, 6.75 W, **41.28 mJ** (CPU 574 mJ). DPU uses 82 % of DSPs, 95 % URAM.
- **HLS:** ESPERTA 37,231 inferences/s at 1.5 W (0.04 mJ, 7.3× energy gain); LogisticNet 2.03× speed;
  deeper 3D nets *slower* than CPU (ReducedNet 0.16×, BaselineNet 0.01×) because naive HLS serialises.
- **Power envelope:** MPSoC 1.5–6.75 W; whole board 10.5–16 W; bitstream download is the peak-power event —
  relevant to configuration scrubbing cadence.
- Vitis AI lacks sigmoid, comparators, 3D conv/pool; PTQ INT8 caused noticeable degradation (QAT suggested);
  HLS matched CPU to ≤ 1e-10. FINN export failed on unsupported ops.
- Comparison table of other space FPGA NN work: LD-UNet 632 FPS/14.1 W, cloud-detection Pixel/Patch-Net on
  Ultra96 at ~0.05 FPS/2.4 W, YOLOv4-MobileNetv3 on KV260 48 FPS/7.2 W.

## Primary (method / assumptions a sceptic would attack)
- Non-EO workloads (solar physics, magnetospheric plasma) — transferable only as a hardware benchmark.
- No radiation testing; the rad-tolerant equivalence is argued from fabric size.
- HLS results are deliberately unoptimised (no pragmas), so the FPGA-vs-CPU picture for 3D nets is a
  toolchain artefact.
- Energy counts MPSoC rail only; board peripherals excluded, which flatters the FPGA figure.

## Derived (our arithmetic — formula shown)
- Throughput per watt: CNetPlusScalar 150 GOP/s / 6.75 W ≈ **22 GOP/s/W** INT8; VAE 50.6 GOP/s / 5.75 W ≈
  8.8 GOP/s/W. A Jetson Orin Nano (15 W) reaches ~40–67 INT8 TOPS nominal, i.e. ~3–4 TOPS/W, so the
  rad-tolerant-class FPGA path is **~2 orders of magnitude** below COTS GPU efficiency on dense CNNs.
- Energy per 1,000 inferences of the heaviest model: 41.28 J ≈ 11 mWh — negligible against any satellite
  bus; latency and tooling, not energy, are the FPGA constraints.

## Relevance to the Entrant
- Benchmarks the **rad-tolerant fallback tier** (Kintex UltraScale XQR-class FPGA): good enough for
  classifier/compressor-scale models at < 7 W, not for VLM-class inference — frames the COTS-GPU vs FPGA
  payload decision.
- The 1:16,384 VAE compression use case is a template for "send the latent, not the image" products.
- KTH/Podobas group is a Nordic academic resource for FPGA onboard-AI engineering near the Entrant.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]] (onboard accelerator benchmark table: FPGA vs Jetson vs Myriad)
