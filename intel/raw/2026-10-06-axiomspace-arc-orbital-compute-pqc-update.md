---
type: intel
tags: [sdc, intel/raw, market/incumbents, company/axiom-space, company/kepler, edge/odc-nodes, space/optical-isl, security/pqc]
source: Axiom Space (press release)
url: https://www.axiomspace.com/release/axiom-space-kepler-ready-orbital-computing-for-quantum-era
author: Axiom Space
published: 2026-10-06
captured: 2026-10-12
primary: this release is the operator's own statement (primary for operational status; no independent telemetry)
---
# Axiom Space — "Axiom Space, Kepler ready orbital computing for quantum era" (ARC platform update)

## Reported (what the source says)
- The orbital data-centre nodes are now branded **Axiom Resilient Compute (ARC)**. **ARC 1 and ARC 2 are
  operating on orbit**, flying as part of Kepler Communications' optical relay network *(reported, operator)*.
- **ARC-to-ARC and ARC-to-ground communication confirmed** — the first operator statement of node-to-node
  traffic between the two nodes *(reported)*.
- Optical links **2.5 Gbps**, compatible with **SDA Tranche 1** optical standards *(reported; same figure as the
  2025 announcement)*.
- Post-quantum cryptography (PQC) is built into silicon and software; a **PQC-encrypted workload migration was
  demonstrated on the ground**. Next milestone: **on-orbit PQC demonstration** (no date given) *(reported)*.
- Policy hook: a June 2026 US Executive Order and OMB guidance require agencies to move high-value systems to
  PQC keys by **end-2030** and PQC signatures by **end-2031** *(reported; EO not opened)*.
- Kepler customers can run orchestration and AI/ML workloads on the in-orbit compute. Terrestrial analogues
  named: oil and gas, mining, subsea, maritime energy (disconnected sites) *(reported)*.
- "Kepler has launched **33 satellites** to date"; Axiom and Kepler have worked on optical ISLs since 2023
  *(reported)*.
- Long-term aim: scale from prototype to a "global, sovereign, PQC-capable orbital processing network"
  *(reported, no dates or node counts)*.

## Primary (what the underlying paper / filing says — where it differs)
- The release is itself primary for operational status. No compute hardware, power, or workload metrics are
  disclosed (the "40 Jetson Orin" figure in third-party coverage remains unconfirmed).
- **Count discrepancy to resolve:** the vault records Kepler's *first tranche* as **10 optical relay
  satellites** with 33 planned ([[intel/raw/2026-01-11-kepler-first-tranche-optical-relay-satellites]]). "33
  satellites launched to date" most likely counts Kepler's earlier non-optical nanosatellites as well — not
  confirmed by the release.

## Derived (our arithmetic — formula shown)
- Months of continuous operation claimed: 2026-01-11 (launch) → 2026-10-06 ≈ **9 months** for two nodes
  (date difference, *derived*).
- No price, revenue, or utilisation figure → the commercial status remains "operational", not "revenue
  disclosed".

## Relevance to the Entrant
- The only flying commercial ODC is moving its pitch from "compute in orbit" to **sovereign + post-quantum
  secure processing**. That is a defence/government security pitch, not an EO time-to-insight pitch — the
  Entrant's lane (EO-specific models, measured latency) is still not claimed by this competitor.
- PQC is becoming table stakes for government buyers on a 2030–31 clock; an Entrant selling to defence buyers
  should plan PQC in its ground–space link from the first flight.
- Still no published workload metrics from the incumbent → the Entrant's "publish measured orbit-average
  latency and duty cycle" differentiator stands.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
- [[intel/wiki/eo-edge-compute-value-chain]]
