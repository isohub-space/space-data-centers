---
type: intel
tags: [sdc, intel/raw, research/paper, space/orbital-compute, space/thermal, hardware/accelerator]
source: arXiv (ISLPED '26)
url: https://arxiv.org/abs/2606.05741
author: Sohan Salahuddin Mugdho, Md. Shahedul Hasan, Cheng Wang (Iowa State University)
published: 2026-06-04
captured: 2026-10-04
primary: self
---
# Space-CIM: Enabling Compute-In-Memory Accelerators for Thermally-Constrained Space Platforms

## Reported (what the paper claims)
- "Radiator-in-the-loop" co-design: achievable TOPS is bounded by radiator **Thermal Rejection Power (TRP)**.
  Radiator modelled as a flat panel rejecting **100 W/m² at 85 °C** (cites Gilmore handbook), T_ext = 140 K,
  so **1 m² ↔ 100 W, 3 m² ↔ 300 W**.
- FEM (COMSOL) thermal maps of an A100-class GPU+HBM (400 W peak, 624 INT8 TOPS, HBM 80 W / 1.9 TB/s, 7 nm)
  vs an ISAAC-like RRAM/STT-MRAM CIM on a 2,700 mm² interposer (16 nm, 160–240 W, 2,658–5,755 TOPS
  simulated via CiMLoop).
- GPU core must throttle when the logic die exceeds **95 °C**; HBM above **85 °C** raises refresh and cuts
  effective bandwidth to ~73 %. Under a 200 W TRP the GPU core needs **> 50 % clock reduction**. CIM has a
  uniform thermal profile and no hotspot.
- **Result:** CIM delivers **10–40× higher effective TOPS** than GPU+HBM under tight radiator budgets
  (≈ 40× at 1 m² / 100 W); the gap narrows at 3 m² because the GPU can clock up. RRAM-CIM keeps running at
  power budgets where the GPU must shut down (below its 100 W / 165 MHz minimum).
- Workloads: GEMM-128/4096, Llama-3.2-3B prefill/decode at batch 1–16, 512–2,048 tokens; CIM wins on all at
  1 m², most at 3 m².
- Positions itself as the first CIM-for-space study with radiator constraints in the loop; notes Starcloud's
  H100 flight and Google's TPU radiation tests as context; radiation is explicitly *out of scope*.

## Primary (method / assumptions a sceptic would attack)
- **100 W/m² at 85 °C is extremely conservative.** εσT⁴ at 358 K, ε 0.9, one side = 0.9 × 5.67e-8 × 1.64e10
  ≈ **840 W/m²**; even with Earth IR/albedo and fin inefficiency a real radiator at 85 °C does 300–500 W/m².
  The 10–40× CIM advantage is largely an artefact of starving the GPU with a radiator 5–8× too small.
- CIM TOPS are CiMLoop *simulations* of an ISAAC-style architecture at 16 nm with 4-bit ADCs and 1–2 bits per
  cell; accuracy loss from analog crossbars is not evaluated, nor is RRAM/MRAM radiation response (RRAM is
  generally rad-tolerant; peripheral CMOS is not).
- A100 (2020) is the GPU baseline; Blackwell/Rubin-class parts have different power maps.
- Iso-area comparison fixes the chip footprint, not mass or cost.

## Derived (our arithmetic — formula shown)
- Radiator area per kW implied by the paper's assumption: 1 kW / 100 W/m² = **10 m²/kW** — vs 2.9 m²/kW
  (ISCR at 30 °C, single-sided), 2.5 m²/kW (Turyshev), 0.95 m²/kW (van Berkel, 370 K two-sided), 0.65–1.2 m²/kW
  (ideal, existing wiki section 4). Space-CIM is the pessimistic outlier by ~4–10×.
- At a realistic 400 W/m² the GPU's 400 W needs 1 m², and the paper's own curves show the CIM advantage
  shrinking toward its raw TOPS/W ratio (≈ 4–10×) once the GPU is unthrottled.

## Relevance to the Entrant
- Real lesson for a small payload: **the HBM–GPU hotspot, not average power, triggers throttling under
  radiative cooling**; spreading heat (vapour chamber, as in the ISCR note) or choosing architectures with
  flat power maps matters as much as total radiator area.
- Non-volatile CIM (RRAM/MRAM) is worth watching for EO inference: low static power, no DRAM refresh, and
  thermal uniformity suit a duty-cycled, radiator-limited satellite. Not procurable today.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]] (radiator-flux assumptions table; hotspot-driven throttling)
- [[intel/wiki/eo-edge-compute-value-chain]] (accelerator-architecture watch list)
