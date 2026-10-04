---
type: intel
tags: [sdc, intel/raw, market/esa, market/europe, space/eo-edge, space/onboard-ai, vendor/edgx]
source: ESA Connectivity & Secure Communications (ARTES project page)
url: https://resilience.esa.int/archives/projects/neuromorphic-ai-onboard
author: ESA CSC
published: 2024-10-08
captured: 2026-10-04
primary: none (ESA project page is the record; EDGX company material not opened)
---
# ESA ARTES "ASCEND" (EDGX, Belgium): ≥100 / ≥250 TOPS Jetson-based DPUs for satellite edge cloud

> Name clash: this ESA ARTES project **"ASCEND — AI-powered Satellite Cloud via Edge Nodes of DPUs"** is unrelated to the Thales/Horizon-Europe **ASCEND** orbital-data-centre study. The page shows status "ongoing as of 08/10/2024" while the contract period reads **Jan 2026 – Mar 2028**; recorded as reported.

## Reported (what the source says)
- Prime: **EDGX** (Belgium); programme **ARTES 4.0 Industrial Competitiveness**; contract **Jan 2026 – Mar 2028**.
- **Sterna** (CubeSat–microsat): **≥100 TOPS INT8** via **NVIDIA Jetson Orin NX**; **<500 g**; PC/104; **first flight Q2 2026**.
- **Morus** (mini/small sats): **≥250 TOPS (goal ~1,000 TFLOPS FP8)** on **Jetson AGX Orin or Jetson Thor T5000**; **ECC memory** for higher-LEO/MEO; **In-Orbit Demonstration 2027**.
- Claim: "**10–100× higher AI inference throughput** while maintaining a compact SWaP envelope" vs existing onboard processors; **≥90% of BoM from EU suppliers**.
- Rad-tolerance approach implied: COTS GPU + ECC + system-level mitigation (no TID/SEL numbers given).

## Primary (where the underlying document differs or adds)
- not checked

## Derived (our arithmetic — formula shown)
- Orin NX is a 10–25 W module → Sterna ≈ **4–10 TOPS/W**; vs KP Labs Leopard **0.3 TOPS/W** and Unibap iX10 **~0.1–0.5 TOPS/W** (see those notes) — a **10–30× efficiency jump** from COTS GPU adoption, which is the "quickly changing" hardware curve CSET also notes ([[2025-06-01-cset-ai-on-the-edge-of-space]]).
- Morus at ~1,000 TFLOPS FP8 on Jetson Thor (~100 W class) puts **a single 2027 ESA-funded DPU at ~1/3 of the compute of one Google Suncatcher TPU-class payload** (1 kW, 2026) — the "edge" and "orbital DC" classes are converging at the 100 W–1 kW level.

## Relevance to the Entrant
- The processor the Entrant would want in 2027 **is being ESA-funded in Belgium right now**; there is no need to build silicon — buy Morus/Sterna (or Unibap/KP Labs for flight-proven) and compete on software, orchestration and relay integration.
- ESA ARTES (telecom side) is funding compute for "satellite cloud" in parallel with EOP's EOCognitiveLab — two ESA directorates, two funding doors for the Entrant.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
- [[intel/wiki/eo-edge-compute-value-chain]]
