---
type: intel
tags: [sdc, intel/raw, market/sceptics, space/launch, space/orbital-compute]
source: IEEE Spectrum
url: https://spectrum.ieee.org/orbital-data-center-hype
author: Harry Goldstein (Editor in Chief, IEEE Spectrum)
published: 2026-07-01
captured: 2026-10-04
primary: none
---
# IEEE Spectrum — "Orbital Data Centers: Why the Hype Outpaces Reality"

## Reported (what the source says)
- **~14,500** active satellites in orbit (Starlink ≈ two-thirds); **~7,000** orbital launches in all of history.
- One million satellites at **60 per Starship** = **16,666 launches**. At SpaceX's 2025 record of **165 launches/yr**, even **10× that cadence takes a decade**.
- Starlink builds **~4,000 satellites/yr**; a tenfold increase would still take **~25 years** to build a million.
- Thermal: 700 W H100 → **1.4 m² at 60 °C**; 40 kW rack → **80 m²**; 100 MW → **2,500** such radiators.
- Starcloud's first test: "Their radiator was too weak to let the chip run at full power."
- Musk's timeline record cited (self-driving 2017, Mars 2024, robotics 2025); orbital cost parity "won't make sense for several years, if ever."

## Primary (where the underlying document differs or adds)
- not checked

## Derived (our arithmetic — formula shown)
- 1,000,000 sats ÷ 60 per flight = 16,667 flights; at 1,650 flights/yr (10× 2025) → **10.1 years**. Matches article.
- Contrast with SpaceX's own FCC framing (100 kW/t, 1 Mt/yr): 1 Mt/yr ÷ 200 t = **5,000 Starship flights/yr** — 30× the 2025 all-vehicle record.

## Relevance to the Entrant
- The manufacturing and launch-cadence ceiling means GW-scale orbital compute cannot arrive before the 2030s; the Entrant's "compute where the sensor is" pitch is not competing with that supply.
- The Starcloud radiator anecdote is a concrete warning: size radiators for sustained, not peak, load.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]]
