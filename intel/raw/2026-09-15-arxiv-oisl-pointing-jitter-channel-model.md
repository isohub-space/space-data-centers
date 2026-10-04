---
type: intel
tags: [sdc, intel/raw, research/paper, space/optical-isl, space/comms]
source: arXiv
url: https://arxiv.org/abs/2609.17431
author: Hossein Safi, Ziheng Wang, Stijn Mast (ESA), Harald Haas, Iman Tavakkolnia (Univ. of Cambridge LiFi R&D Centre)
published: 2026-09-15
captured: 2026-10-04
primary: self
---
# Analytical Channel Modeling and Stability-Aware Optimization of Optical Inter-Satellite Links

## Reported (what the paper claims)
- Closed-form channel-gain PDF, outage probability and ergodic-capacity penalty for an OISL with
  **independent Rayleigh pointing jitter at both terminals**, parametrised by stability ratios
  φ_tx = (beam divergence / jitter)² and φ_rx = (receiver FOV / jitter)². Validated by Monte Carlo and against
  exact Klein–Degnan/Airy diffraction.
- **Weakest-link principle:** outage decays with exponent d = min(φ_tx, φ_rx); improving the already-stable
  terminal only shifts a power offset. Ergodic-capacity penalty depends instead on the *sum* 1/φ_tx + 1/φ_rx.
- **Reference 10 Gbps IM/DD OOK link (Table II):** λ 1550 nm, z = **1,000 km**, 10 cm apertures both ends,
  divergence 14.6 µrad, FOV 25 µrad, **jitter σ = 2 µrad** each end, P_tx = **30 dBm (1 W)**, APD receiver
  sensitivity −31.6 dBm at BER 10⁻³, path gain −53.65 dB, link margin **+7.95 dB**, φ_tx 13.3, φ_rx 39.1 →
  outage **1.87 × 10⁻¹⁰**.
- Design rule for asymmetric terminals: balance stability by scaling divergence with jitter
  (θ_A/θ_B = σ_A/σ_B); the jittery terminal then pays a **(σ_A/σ_B)² transmit-power penalty**. Example: LEO
  (5 µrad) ↔ GEO (1 µrad) with equal 10 µrad beams gives φ_LEO = 1 and a ~3 bit/s/Hz (≈ 9 dB equivalent-SNR)
  capacity penalty; balancing requires a 50 µrad LEO beam and **25× (14 dB)** more LEO transmit power —
  "may be prohibitive for a small satellite".
- Cites 100G Starlink-class ISL fleets achieving ≥ 99 % uptime (Brashears, SPIE 2024) and Chinese 400 Gbps
  demos as the operational state of the art; multi-gigabit to Tbps framed as the OISL promise.

## Primary (method / assumptions a sceptic would attack)
- Zero-mean Rayleigh jitter only; bias drift, correlated/anisotropic jitter, acquisition phase and tracking
  dynamics left to future work.
- Gaussian main-lobe approximation is tight only within the nominal pointing range (φ ≳ a few); low-stability
  cases need the offset calibration in their Table III.
- Design example is 10 Gbps OOK with an APD — far from the coherent DWDM 400G channels Google assumes.
  The jitter sensitivity is, however, *worse* for coherent detection (needs higher SNR, ~196 photons/bit).

## Derived (our arithmetic — formula shown)
- Google's Suncatcher ISL (5 W, 10 cm, 5 km, ~1 µrad pointing requirement for 10 % beam wander) has
  divergence ≈ 1.22 λ/D = 18.9 µrad; at σ = 1 µrad, φ_tx ≈ (18.9/1)² ≈ 357 — deep in the stable regime, so
  jitter is not the limiter *at 5 km*. At 1,000 km the same terminal would need the full link budget above;
  the paper's 10 Gbps / 1 W / 10 cm point sits roughly where Google's Figure 1 puts single-channel OOK at
  that range.
- Power penalty rule for a small-sat with 5 µrad jitter talking to a 1 µrad relay: (5/1)² = 25× — a 1 W
  terminal becomes 25 W, which on a 2 kW inference satellite is a 1 %-class overhead, i.e. tolerable;
  on a CubeSat it is not.

## Relevance to the Entrant
- Pointing stability, not laser power, decides whether the Entrant can use a Tbps-class ISL to a neighbour or a
  Gbps-class downlink to a relay; the paper gives a **closed-form way to turn ADCS/PAT specs into link
  availability** during bus selection.
- ESA co-authorship (Stijn Mast) and the ESA OISL-terminal grant make this the European reference model to
  cite when talking to Mynaric/TESAT/Cailabs-class vendors.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]] (ISL section: jitter-limited regime, 10 Gbps/1 W/10 cm/1,000 km reference)
- [[intel/wiki/eo-edge-compute-value-chain]] (downlink/relay link design)
