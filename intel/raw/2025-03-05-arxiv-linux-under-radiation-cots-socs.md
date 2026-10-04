---
type: intel
tags: [sdc, intel/raw, research/paper, space/radiation, hardware/cots-soc, software]
source: arXiv (v1 2025-03-05; v4 2026-05-20)
url: https://arxiv.org/abs/2503.03722
author: Saad Memon, Rafal Graczyk, Tomasz Rajkowski, Jan Swakoń, Damian Wróbel, Sebastian Kusyk, Seth Roffe (NASA GSFC), Mike Papadakis (Univ. of Luxembourg SnT / IFJ PAN / NCBJ)
published: 2025-03-05
captured: 2026-10-04
primary: self
---
# Where Linux Breaks Under Radiation: A Cross-Architecture Kernel-Level Characterization of Proton-Induced Failures in COTS SoCs

## Reported (what the paper claims)
- Three Linux platforms under **20–58 MeV protons** (IFJ PAN, 40 mm field, flux 3 × 10⁶–1 × 10⁸ p/cm²/s,
  stress workload): **Raspberry Pi Zero 2W** (BCM2710A1, 40 nm, stacked LPDDR2 in-beam), **NXP i.MX 8M Plus**
  (14 nm FinFET Cortex-A53, LPDDR4 *outside* the beam), **OrangeCrab ECP5 FPGA** with VexRiscV RV32I soft-core
  (40 nm). **133 Linux-SEFI events** traced to originating kernel handlers.
- **Linux-SEFI cross-sections (cm², per system):** RPi Zero 2W **2.84–6.95 × 10⁻⁹** (every run failed);
  i.MX 8M Plus **1.98 × 10⁻¹⁰ – 1.13 × 10⁻⁹** (~10× lower; not all runs failed); ECP5 soft-core
  **1.11–7.63 × 10⁻⁹**. Mean Linux uptime 5–8× longer on the 14 nm part. No statistically significant energy
  dependence 20–58 MeV.
- **Failure origin:** 40 nm platforms — memory-management + driver handlers **67–78 %** of events; 14 nm
  i.MX — **~90 % funnel through the eMMC storage path** (56 % filesystem + 34 % driver): "a SEFI-susceptible
  peripheral can dictate system reliability". Faults cascade through up to **six kernel subsystems**; in 3 of
  133 events PID 1 recovery required the very eMMC subsystem the fault had disabled — a reproducible
  circular dependency that blocks autonomous recovery.
- Mitigation table (Table 6): hardware SECDED ECC (~12 % bandwidth, misses multi-bit), PANIC_ON_OOPS,
  scrubbing, dm-verity (~10 % read latency; read-only root), FPGA TMR (3× resources, memory unprotected),
  external watchdog, read-only root + tmpfs.
- Context: SpaceX reportedly runs tens of thousands of Linux COTS nodes in Starlink; Ingenuity (Snapdragon
  801 + Linux) did 72 flights on a 5-flight design.

## Primary (method / assumptions a sceptic would attack)
- Workload-conditioned cross-sections under stress tests — upper-bound-ish for idle systems, and not
  device-intrinsic SEU rates (authors say so; heavy ions needed for Weibull/LET).
- The 10× FinFET advantage is confounded with DRAM-in-beam geometry and packaging; the authors decline to
  attribute it to process node alone.
- 60 MeV-class protons degraded to 20–58 MeV; no GCR/heavy-ion component, so GEO/deep-space extrapolation
  is unsupported.
- Consumer boards (SD card, eMMC, no ECC); flight-style boards with ECC DRAM would move the numbers.

## Derived (our arithmetic — formula shown)
- Orbit projection (our flux assumption, ~10³ p/cm²/s > 10 MeV orbit-average at 500–600 km SSO behind thin
  shielding): RPi-class σ ≈ 5 × 10⁻⁹ → 5 × 10⁻⁶/s ≈ **one Linux crash per ~2.3 days**; i.MX-class
  σ ≈ 5 × 10⁻¹⁰ → **one per ~23 days**. Behind 10 mm Al-eq (Google's assumption) the flux drops several-fold,
  stretching these to weeks/months. Order-of-magnitude only.
- Relative to Google's host SEFI (1 per 450 rad(Si) ≈ 0.33/yr at 150 rad/yr): the unshielded 40 nm RPi is
  ~50× worse, the shielded 14 nm part within ~10× — consistent with the TPU host being a shielded server-class
  board.

## Relevance to the Entrant
- The payload OS and **storage path** (eMMC/SD) are as much a reliability item as the accelerator; pick 14 nm-
  or-better SoCs, ECC DRAM, read-only root with dm-verity, external watchdog, and never let recovery depend
  on the subsystem most likely to fail.
- Supports the BUPT finding that thermal binds before radiation at ~500 km *for well-chosen hardware* — but
  shows a 40 nm hobby-board stack would crash every few days.
- Same Luxembourg/IFJ PAN team as [[intel/raw/2026-09-04-arxiv-tensil-proton-irradiation]]; one European
  test partner covers both OS- and accelerator-level characterisation.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]] (COTS SoC SEFI cross-sections; OS hardening checklist)
- [[intel/wiki/orbital-compute-launch-economics]] (radiation: process node and peripherals matter more than ISA)
