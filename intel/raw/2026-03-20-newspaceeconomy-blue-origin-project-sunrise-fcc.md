---
type: intel
tags: [sdc, intel/raw, market/startups, company/blue-origin, regulatory/fcc, space/orbit-sso, space/launch]
source: New Space Economy
url: https://newspaceeconomy.ca/2026/03/20/blue-origin-project-sunrise-the-race-to-build-data-centers-in-orbit/
author: New Space Economy
published: 2026-03-20
captured: 2026-10-04
primary: Blue Origin FCC filing 2026-03-19 (Kaitlyn Mahoney, Ryan Henry) — not opened; mlq.ai 2026-03-21 (citing The Register) opened as cross-check
---
# New Space Economy — Blue Origin "Project Sunrise": FCC filing for 51,600 data-center satellites

## Reported (what the source says)
- Filed **2026-03-19** from Kent, WA. Up to **51,600 satellites**, **500–1,800 km**, inclination
  **97–104°** (sun-synchronous), **300–1,000 sats per plane**.
- Comms: optical mesh; **Ka-band** 18.8–19.3 GHz down / 28.6–29.1 GHz up (TT&C per mlq.ai).
- Backhaul via Blue Origin's **TeraWave** constellation: **5,408 sats** (5,280 LEO + 128 MEO); up to
  **6 Tbps** MEO optical, **144 Gbps** LEO; **first 5,000+ TeraWave sats planned by end 2027**, none
  launched yet (mlq.ai).
- Launcher: **New Glenn** — **45,000 kg** to LEO standard; **9×4 super-heavy variant 70,000+ kg**;
  flights: 2025-01-16 (first orbital), 2025-11-13 (booster recovered). Only **2 launches** to date.
- Competitive context: SpaceX filing late Jan 2026 (1M), **Starcloud filing 2026-02-03 (88,000)**,
  China announced **200,000+**.
- Cost reference used: Google's Nov 2025 study — competitive at **~$200/kg** around **2035** with ~180
  Starship launches/yr.
- Blue Origin's stated claim: ODCs "enable U.S. companies developing and using AI to flourish".
- **No power-per-satellite, GW total, or hardware disclosed.** No ITU filing yet. Gartner and
  others sceptical (mlq.ai).
- *(Bezos "gigawatt-scale data centers in space within 10–20 years" appears only in search
  snippets (AI Magazine, 403 on fetch) — not verified from an opened page.)*

## Primary (where the underlying document differs or adds)
- not checked.

## Derived (our arithmetic — formula shown)
- If each Sunrise sat matched SpaceX's AI1 (150 kW), 51,600 × 150 kW = **7.7 GW**; at Starcloud-2
  class (8 kW) = **0.4 GW**. The filing's power ambition is **indeterminate by a factor of ~20**
  without a per-sat figure.
- 51,600 sats on New Glenn at 45 t: unknown sat mass, but at even 1 t each = **1,150 launches** vs.
  2 flown so far.

## Relevance to the Entrant
- Fourth US filer in SSO (SpaceX, Starcloud, Blue Origin, Cowboy) — **SSO slot/debris politics**
  will reach ITU/ESA; a European EO-processing node benefits from being an *early, small,
  compliant* SSO filer before these arrive.
- TeraWave (6 Tbps MEO optical relay) is a possible future **backhaul** for small EO-compute nodes
  — same role Kepler plays today for Axiom.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
