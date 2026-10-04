---
type: intel
tags: [sdc, intel/raw, research/paper, space/radiation, space/eo-edge, onboard-inference, hardware/gpu]
source: arXiv
url: https://arxiv.org/abs/2407.11853
author: Meiqi Wang, Han Qiu, Longnv Xu, Di Wang, Yuanjie Li, Tianwei Zhang, Jun Liu, Hewu Li (Tsinghua / BUPT / NTU)
published: 2024-07-16
captured: 2026-10-04
primary: self
---
# A Case for Application-Aware Space Radiation Tolerance in Orbital Computing (RedNet)

## Reported (what the paper claims)
- In-flight memory upset data cited: CARMEN-2 on **JASON-2** (1,336 km) ≈ **4.76 × 10⁻⁷ bit⁻¹ day⁻¹** → a 40 MB
  application image sees **~150+ bit errors per day**; SEU probability generally 10⁻⁷–10⁻⁶ /bit/day in LEO;
  > 5 % of upsets are spatially correlated **multi-cell upsets** (2–8 bits, 80 % along a wordline); SAA
  dominates and is larger at 1,336 km than at 657 km (CARMEN/MEX).
- Argument: hardware (rad-hard CPUs at 180–216 MHz / 2 MB; TMR triples energy; ECC not in COTS SoCs) and
  OS protections (watchdog reboots, SoftECC +62.5 % memory) are "expensive and overwhelming" for COTS
  nanosats, and DNN inference under bit flips **does not crash — it silently degrades**.
- **RedNet:** exploit uneven layer sensitivity (shallow layers critical, deep layers tolerant) with a
  renovated activation that bounds error propagation, plus **multi-exit early inference** to skip corrupted
  deep layers. Built on NVIDIA TensorRT for the **Jetson Xavier NX payload flown on Chaohu-1 SAR (2022)**;
  hardware-in-the-loop DRAM radiation emulator (LPDDR4 hierarchy-aware) released.
- **Results** (3 EO datasets, 3 model families, 5–500 injected bit errors): RedNet "suppresses the influence
  of radiation errors to ≈ 0" and **speeds inference 8.4–33.0 %** (early exits) at negligible memory. Worst
  case 500 bit flips, object detection: **mAP 72.6 % (RedNet) vs 60.6 % (clean model, −17.7 pts)**; 100 errors
  placed in the sensitive memory region → **93 % model crash** for the unprotected model; output clipping
  alone does not help.

## Primary (method / assumptions a sceptic would attack)
- No beam test; errors are *emulated* from in-flight statistics into a Jetson's memory map. Real GPU
  SEE behaviour (SRAM, register file, TensorRT engine) is not characterised.
- The 150 errors/day headline uses JASON-2 at 1,336 km; at 500–650 km SSO the rate is substantially lower
  (BUPT-1 saw zero observable SEE in months — [[intel/raw/2026-08-21-arxiv-bupt-ai-infrastructure-in-space]]).
- "≈ 0" error influence is measured on classification/detection accuracy, not on silent wrong *outputs*
  per inference; early exit also trades accuracy on clean inputs (not quantified in the pages read).
- Model-level hardening does nothing for control-flow, OS or driver state
  ([[intel/raw/2025-03-05-arxiv-linux-under-radiation-cots-socs]]).

## Derived (our arithmetic — formula shown)
- Expected flips in a 2 GB INT8 VLM weight set at JASON-2 rates: 1.6 × 10¹⁰ bit × 4.76 × 10⁻⁷ ≈
  **7,600 flips/day** — weights must be scrubbed from protected storage daily, or the model drifts; at a
  10× lower 600 km rate still ~760/day. Weight integrity, not compute SDC, becomes the dominant radiation
  design item for large onboard models.

## Relevance to the Entrant
- Establishes **application-aware tolerance** (layer-sensitivity, early exit, periodic weight reload) as the
  cheap, COTS-compatible alternative to TMR for EO inference payloads — exactly the Entrant's cost class.
- Tsinghua's released radiation emulator is a free tool to qualify the Entrant's models before any beam time.
- Chaohu-1 (Spacety) flying a Jetson Xavier NX is a 2022 Chinese precedent for GPU-class EO edge compute.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]] (in-flight upset rates; weight-scrub arithmetic; application-aware hardening)
- [[intel/wiki/orbital-data-center-landscape]] (Chaohu-1 / Spacety GPU payload)
