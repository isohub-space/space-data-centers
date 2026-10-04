---
type: intel
tags: [sdc, intel/raw, research/paper, space/radiation, hardware/fpga, onboard-inference]
source: arXiv (submitted to IEEE TNS)
url: https://arxiv.org/abs/2609.05249
author: Saad Memon, Rafal Graczyk, Jan Swakoń, Leszek Grzanka, Sebastian Kusyk, Mike Papadakis (Univ. of Luxembourg SnT / IFJ PAN Kraków)
published: 2026-09-04
captured: 2026-10-04
primary: self
---
# Proton Irradiation Characterization of an Open-Source ML Accelerator on a Zynq UltraScale+ MPSoC

## Reported (what the paper claims)
- DUT: Avnet **Ultra96-V2** (XCZU3EG, 16 nm FinFET) + 2 GB LPDDR4 (no ECC), PYNQ Linux 2.7, open-source
  **Tensil TCU** (16×16 systolic array, 100 MHz, FP16BP8) running **ResNet-20 / CIFAR-10** in blocks of 100
  inferences with PL reload each block. No watchdog, scrubbing or redundancy — an *unmitigated baseline*.
- Beam: IFJ PAN AIC-144 cyclotron, nominal **20 / 40 / 58 MeV** protons; **4.29 × 10¹⁰ p/cm²** in monitored
  windows (6.19 × 10¹⁰ total); two fields — ~25 mm (SoC-centred) and ~40 mm (SoC + LPDDR4 + board).
- **Events:** 7 Linux-level workload interruptions (2 process restarts, 4 reboots/resets, 1 power cycle) and
  **2 silent output-corruption events** without loss of service. In the longer one the accelerator returned
  the class **"bird" — absent from the 10-image pool — for 39 consecutive inputs** at normal 23–24 ms cadence
  while kernel log, memory test and power rails stayed nominal; it ended only with scheduled reconfiguration.
- **Cross-sections (per system):** Linux-SEFI 1.3 × 10⁻¹⁰ (20 MeV wide) to **6.9 × 10⁻¹⁰ cm²** (40 MeV wide),
  4.7 × 10⁻¹⁰ at 58 MeV; < 2.5 × 10⁻¹⁰ upper limits under the small field. Output-corruption σ_FE
  **1.6 × 10⁻¹⁰ cm²** (wide field), < 1.8 × 10⁻¹⁰ (small). **All nine onsets occurred under the wide field** that
  included the LPDDR4 — "a field association" but confounded with run order and dose.
- OCM ECC corrected-error at one address recurred across nine blocks and a reboot; EXT4 directory corruption
  observed on the SD root filesystem.
- Recommendations: count events by onset; match denominators to the monitor; liveness and timing do **not**
  establish inference correctness → "end-to-end content-aware checks and staged recovery" (known-answer
  probes, class-histogram checks, model-buffer checksums).

## Primary (method / assumptions a sceptic would attack)
- Top-1-class oracle only: class-preserving numerical corruption is invisible; so σ_FE is a *lower* bound on
  SDC.
- Two output events → wide Poisson intervals (2 × 10⁻¹¹ to 5.9 × 10⁻¹⁰ cm²); energy dependence not
  established.
- Ten fixed CIFAR images, 16 nm Zynq + consumer LPDDR4; not flight hardware, not EO models.
- Field size confounded with order and accumulated dose; the paper refuses to attribute to LPDDR4.

## Derived (our arithmetic — formula shown)
- LEO rate estimate (order of magnitude only): trapped-proton flux > 10 MeV at ~500–600 km SSO behind modest
  shielding is ~10²–10³ p/cm²/s orbit-averaged (SAA-dominated). At 10³ p/cm²/s, σ_SEFI = 5 × 10⁻¹⁰ cm² →
  5 × 10⁻⁷/s ≈ **one Linux-SEFI per ~23 days**; σ_FE = 1.6 × 10⁻¹⁰ → one silent-corruption *episode* per
  ~70 days. A stuck-class episode of 39 inferences at EO frame rates could silently mislabel a full pass.
  (Flux assumption is ours; the paper gives no orbit projection.)
- Consistency with Google's TPU: 1 SDC per 17 rad ≈ 1 per 150 rad/yr / 17 ≈ **9 per chip-year**; this
  FPGA+LPDDR4 stack gives ~5 episodes per year at the flux above — same order, but here each episode
  persists across many inferences rather than flipping one output.

## Relevance to the Entrant
- **Persistent silent corruption is the failure mode that matters for an inference service**: the system
  stayed "up" and produced plausible-cadence garbage. The Entrant's reliability design needs output-content checks
  (known-answer inputs, class/mask histograms, redundant inference on a sample) and staged recovery that
  reaches DRAM and model buffers, not just a watchdog.
- Luxembourg SnT + IFJ PAN is a European proton-test pipeline (EURO-LABS/RADNEXT funded) that the Entrant could use
  to characterise its own payload cheaply.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]] (silent-corruption cross-sections; reliability checklist)
- [[intel/wiki/orbital-compute-launch-economics]] (radiation section: beyond Google's TPU data)
