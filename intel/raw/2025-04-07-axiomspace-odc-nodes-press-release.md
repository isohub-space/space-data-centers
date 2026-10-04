---
type: intel
tags: [sdc, intel/raw, market/startups, company/axiom-space, company/kepler, edge/eo, sovereign-data, primary]
source: Axiom Space (press release) + Axiom ODC product page
url: https://www.axiomspace.com/release/axiom-space-to-launch-orbital-data-center-nodes-to-support-national-security-commercial-international-customers
author: Axiom Space
published: 2025-04-07
captured: 2026-10-04
primary: this is the primary; product page https://www.axiomspace.com/orbital-data-center (undated, opened) adds the Jan 2026 launch
---
# Axiom Space — ODC nodes on Kepler satellites (press release, 38th Space Symposium) + ODC product page

## Reported (what the source says)

**Press release, 2025-04-07**
- Axiom to launch **two initial Orbital Data Center (ODC) nodes** on **Kepler Communications'**
  optical relay constellation; target **end of 2025**.
- Optical links **2.5 Gbps** now, **10 Gbps+** planned for future nodes; terminals compatible with
  **SDA Tranche 1** optical standards. LEO.
- Scaling roadmap: "**kilowatts to megawatts** of on-orbit processing power".
- Lineage: **2022** AWS Snowcone on Ax-1 to ISS; **2023** ODC Tranche 1 plans for Axiom Station;
  **March 2025** AxDCU-1 prototype with **Red Hat** (Device Edge / MicroShift) to ISS.
- Use cases: real-time **PED** for national-security and commercial satellites; low-latency
  **multi-sensor fusion**; AI/ML and LLMs for autonomous decisions; Earth-independent **EDR
  cybersecurity**.
- CEO Kam Ghaffarian: *"We have agreements in place with users around the world to deploy
  initial, space-based cloud services."*

**ODC product page (opened 2026-10-04)**
- "**The first two orbital data center nodes successfully launched to low-Earth orbit on January
  11, 2026**" — i.e. the end-2025 target slipped ~1 month.
- AxDCU-1 "deployed to the ISS **Fall 2025**" (press release said launch March 2025; search
  snippets say Aug 2025 — dates of launch vs. deployment differ across Axiom's own copy).
- Partners: Kepler (optical relay), Red Hat (Device Edge), **Quantinuum** (quantum security).
- Services: cloud/edge processing, AI/ML, data fusion, space cybersecurity, real-time satellite
  data processing; targets national-security, government, commercial customers. Expansion "through
  2030 and beyond". No pricing, GPU type or storage figure on the page.

**Not verified from an opened page (search snippets only, flagged):** carrier sats ~**300 kg**,
"multi-GPU compute modules, terabytes of storage, four optical terminals"; Kepler's on-orbit
compute = **40 Nvidia Jetson Orin modules across 10 satellites** (Kepler statement quoted in
GTC-2026 coverage); altitude ~400 km. Treat as plausible but unconfirmed.

## Primary (where the underlying document differs or adds)
- This is the primary. Note the press release never says "GPU"; the Jetson Orin claim comes from
  Kepler via third parties.

## Derived (our arithmetic — formula shown)
- Jetson Orin class modules are **~15–60 W** each; 40 of them ≈ **0.6–2.4 kW** fleet-wide — this
  is the actual power class of the only *operational* commercial ODC service in Oct 2026, versus
  the MW–GW filings.

## Relevance to the Entrant
- Axiom/Kepler is the **closest live competitor/partner** for in-orbit EO processing: SDA-compatible
  optical ISLs, kW-class Jetson compute, PED/multi-sensor fusion marketed to government. An
  EO-processing startup can either **rent** this (hosted app) or must beat 2.5 Gbps-linked Orin
  nodes on latency or model quality.
- Red Hat Device Edge/MicroShift on-orbit is a de-facto software baseline — the Entrant's stack should
  be container-portable to it.
- Launch slip of only ~1 month vs plan is unusually good for this sector; Axiom is executing.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
