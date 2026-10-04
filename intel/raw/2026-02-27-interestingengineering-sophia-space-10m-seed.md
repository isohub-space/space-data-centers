---
type: intel
tags: [sdc, intel/raw, market/startups, company/sophia-space, funding, space/thermal, hardware/nvidia]
source: Interesting Engineering
url: https://interestingengineering.com/space/sophia-space-seed-round-orbital-compute
author: Mrigakshi Dixit
published: 2026-02-27
captured: 2026-10-04
primary: none (company press release 2026-02-24; SpaceNews/GeekWire/DCD coverage paywalled or 403)
---
# Interesting Engineering — Sophia Space raises $10M seed for TILE orbital compute

## Reported (what the source says)
- **$10M seed**, led by **Alpha Funds, KDDI Green Partners Fund, Unlock Venture Partners**.
  *(GeekWire snippet: builds on **$3.5M pre-seed**; founded **2023**, Pasadena — not verified from an
  opened page.)*
- Founders: **Dr. Leon Alkalai** (CTO, ex-NASA/JPL Fellow), **Rob DeMillo** (CEO).
- Product **TILE** ("Thermal-Integrated LEO Edge"): modular, **meter-wide server racks/tiles**
  integrating solar generation and **passive radiative cooling**; claim **92% of generated power
  goes to processing**. Ruggedized for radiation/thermal extremes.
- Roadmap: flight test on an **Apex Space bus by late 2027**; "thousands of TILE modules" and a
  **1 MW** target in the **2030s**. *(GeekWire snippet: first TILE deliveries to customers 2028.)*
- Applications: AI inference and data processing in orbit, **EO data processing**, defence,
  disaster response, maritime awareness, energy-infrastructure monitoring.
- Named by Nvidia (GTC 2026) as a Vera Rubin Space-1 ecosystem partner
  ([[intel/raw/2026-03-17-theregister-nvidia-vera-rubin-space-1]]).
- DeMillo: *"Moving high-performance compute into orbit isn't just growth. It's a separator."*

## Primary (where the underlying document differs or adds)
- not checked.

## Derived (our arithmetic — formula shown)
- "92% of power to processing" implies an **8% overhead** for bus, pointing, comms and thermal —
  extremely aggressive versus typical smallsat payload fractions of 30–50%. Treat as a design goal.

## Relevance to the Entrant
- Sophia is the **thermal-architecture** play: passive radiator-integrated tiles. If TILE works,
  the "radiator problem" becomes a buyable module — relevant to the Entrant's node design choices
  (build vs buy thermal).
- Explicitly lists **EO processing, maritime awareness, disaster response** — same verticals as
  the Entrant's time-to-insight pitch — but first flight is **late 2027** and product **2028+**: a
  European EO-processing node flying 2027 would be ahead of them.
- KDDI's involvement shows Asian telcos are seeding this; European telcos (Orange was in ASCEND)
  are the analogous funders to approach.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
