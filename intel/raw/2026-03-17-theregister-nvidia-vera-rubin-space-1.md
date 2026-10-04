---
type: intel
tags: [sdc, intel/raw, market/startups, company/nvidia, hardware/nvidia, hardware/cots, ecosystem]
source: The Register
url: https://www.theregister.com/special-features/2026/03/17/nvidia-rolls-out-rubin-module-for-space-based-computing/5221345
author: Brandon Vigliarolo
published: 2026-03-17
captured: 2026-10-04
primary: Nvidia GTC 2026 keynote / announcement (2026-03-16) — not opened; SiliconANGLE 2026-03-16 opened as cross-check
---
# The Register — Nvidia rolls out Vera Rubin "Space-1" module for space-based computing (GTC 2026)

## Reported (what the source says)
- **Vera Rubin Space-1 module**: "up to **25× the AI compute of an H100**"; designed for size-,
  weight-, power-constrained environments; for space inferencing, orbital data centers, GEOINT,
  autonomous space ops.
- Related Nvidia space products: **IGX Thor** (rugged edge), **Jetson Orin** (vision/nav on
  spacecraft), **RTX Pro 6000 Blackwell Server** (ground GEOINT).
- **Partners deploying Nvidia in orbit: Aetherflux, Axiom Space, Kepler Communications, Planet,
  Sophia Space, Starcloud.** Aetherflux first data-center sat **Q1 2027** (as stated then).
- Gartner's **Bill Ray**: "prohibitive costs of launching hardware", cooling challenges — calls the
  sector "**peak insanity**".
- *(SiliconANGLE 2026-03-16: Vera Rubin = 2 Rubin GPUs + 1 Vera CPU (88 cores), LPDDR5X; Rubin GPU
  **336B transistors, 3 nm**; **50 PFLOPS NVFP4** vs 10 PFLOPS predecessor; render suggests two Vera
  Rubin chips per Space-1 device. Huang: "In space there's no conduction, there's no convection.
  There's just radiation." No ship date given.)*
- TechCrunch 2026-08-21: Space-1 expected **late 2028**.

## Primary (where the underlying document differs or adds)
- not checked. **No radiation-tolerance spec, power rating or price** disclosed anywhere opened —
  "space module" here means SWaP-optimized packaging of a COTS die, not a rad-hard part.

## Derived (our arithmetic — formula shown)
- 25× H100 at roughly 2× H100 power (if ~1.4 kW) → **~12× perf/W** improvement — this, not launch
  cost, is the lever that most changes kW-class orbital inference economics between 2026 and 2029.

## Relevance to the Entrant
- Nvidia has **standardized the stack** for orbital compute (Jetson Orin now → Space-1 2028). An EO
  processing node should be CUDA-first; rad-hard alternatives (Ramon.Space) are a niche.
- Being on Nvidia's partner slide is now a credibility marker: six names, **zero European**
  (Kepler is Canadian). A European EO-processing node entering the Nvidia space ecosystem is an
  open position.
- Space-1 arrives **late 2028** — any the Entrant node before then flies Orin/IGX-class or a COTS
  data-center GPU with shielding, like Starcloud-1.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
