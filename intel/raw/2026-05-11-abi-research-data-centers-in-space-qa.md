---
type: intel
tags: [sdc, intel/raw, market/sizing, market/sceptics, space/thermal, space/orbital-compute]
source: ABI Research (blog)
url: https://www.abiresearch.com/blog/data-centers-in-space
author: Andrew Cavalier (Principal Analyst, ABI Research)
published: 2026-05-11
captured: 2026-10-04
primary: "ABI Research orbital data centre TCO model and forecast (paywalled)"
---
# ABI Research — "Data Centers in Space: Analyst Q&A on Commercial Feasibility and Market Reality"

## Reported (what the source says)
- Forecast: **18,600 active orbital data centres by 2035**, effective orbital compute **1.5 GW** by 2035. Total funding into the sector **> US$3B as of April 2026**.
- US AI compute demand: **8.2 GW** active IT capacity (2026) → **26.4 GW** (2031).
- Solar energy density advantage in orbit: **10–40×** terrestrial solar.
- TCO: an orbital data centre can cost **up to 78×** a terrestrial equivalent.
- Per H100: **1.1 m²** radiator; a DGX H100 system needs **~16 m²** radiator and **~33 m²** solar.
- Example 2,000 kg satellite: **~670 kg** of that is solar panels, leaving little for compute.
- Workloads that make sense near-term (2026–2029): defence/ISR, EO/SAR, **kW-scale compute-as-a-service**. 2030s: AI inference, secure backup, hyperscale CaaS, training.
- Orbital $/W parity with terrestrial not before **2035**; hardware cannot be upgraded post-launch so value must be extracted within **3–5 years**; **SSO already congested**.

## Primary (where the underlying document differs or adds)
- not checked (model proprietary). Same analyst's IEEE Spectrum piece assumes Starship at $44/kg and still gets ≥10× cost disadvantage.

## Derived (our arithmetic — formula shown)
- Average size implied: 1.5 GW ÷ 18,600 = **~80 kW per "data centre"** — these are hosted payloads/smallsats, not data centres.
- Radiator density implied: 700 W ÷ 1.1 m² = **636 W/m²** (more optimistic than Spectrum's 500 W/m² and Turyshev's 400 W/m²).
- Solar mass fraction in the example: 670 ÷ 2,000 = **33.5%**.

- *(merged from the startup lane's duplicate capture, 2026-10-04)* ABI report code **MD-SATODC-101 (2Q 2026)**; its chart page states **1.54 GW** on-orbit capacity by 2035; the Q&A also cites the **Anthropic–SpaceX "multiple GW orbital" agreement** as a demand signal.

## Relevance to the Entrant
- ABI's near-term list — EO/SAR, ISR, kW-scale CaaS — is exactly the Entrant's offering; the analyst consensus places the Entrant's segment as the only one that exists before 2030.
- The 3–5 year value window and no-upgrade constraint favour the Entrant's software-defined, fast-refresh approach over monolithic hardware.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
- [[intel/wiki/orbital-compute-launch-economics]]
