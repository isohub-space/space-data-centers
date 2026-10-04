---
type: intel
tags: [sdc, intel/raw, market/competitors, market/sceptics, space/orbital-compute]
source: IEEE Spectrum
url: https://spectrum.ieee.org/orbital-inference-data-center
author: Aaron Mok
published: 2026-05-10
captured: 2026-10-04
primary: none
---
# IEEE Spectrum — "Orbital Inference Data Center Bets On Space GPUs" (Orbital Inc.)

## Reported (what the source says)
- Orbital Inc. plans **up to 10,000** satellites at **100 kW** each; solar array "roughly tennis court" size, radiative cooler of comparable size; latency to LEO "tens of milliseconds".
- Timeline: design final **2026**, prototype launch **2027**, factory **2028**.
- Caveats raised: radiation bit-flips, radiative-only cooling, no repair/replacement, reliability at scale "an open question". Andrew Côté: space data centres won't operate for "at least another 10 to 20 years"; Amit Verma: "failure risk with limited repair options", feasibility "depends on applications".

## Primary (where the underlying document differs or adds)
- not checked

## Derived (our arithmetic — formula shown)
- A tennis court ≈ 261 m²; 100 kW ÷ 261 m² ≈ **383 W/m²** of array — consistent with Spectrum's 400 W/m² figure. 10,000 × 100 kW = **1 GW** constellation.
- The 100 kW node recurs across SpaceX (FCC), Orbital Inc. and Gaalema — **100 kW/~1 t** is the industry's convergent design point for general-purpose orbital compute.

## Relevance to the Entrant
- Another general-compute entrant with 2027–28 prototypes; none target EO-adjacent insight. The Entrant's differentiation remains the sensor-to-insight loop, not watts.
- "Feasibility depends on applications" is the sceptics' own door for the Entrant: applications where the data originates in orbit.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
