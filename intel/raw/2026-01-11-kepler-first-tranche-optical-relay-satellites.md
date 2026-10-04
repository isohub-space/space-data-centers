---
type: intel
tags: [sdc, intel/raw, space/optical-isl, space/orbital-compute, vendor/kepler, market/relay]
source: Kepler Communications (company news)
url: https://kepler.space/kepler-successfully-launches-first-tranche-of-optical-relay-satellites/
author: Kepler Communications
published: 2026-01-11
captured: 2026-10-04
primary: "SatNews 'Kepler Communications' next-generation optical data relay constellation launched' (https://satnews.com/2026/02/09/63641/), opened — dates the Falcon 9 'Twilight-1' rideshare launch 9 Feb 2026"
---
# Kepler launches first tranche of 10 optical data-relay satellites with onboard GPUs

## Reported (what the source says)
- **10 satellites**, **~300 kg** each, Falcon 9 from Vandenberg; Kepler's total launched to date **33 satellites**.
- Each carries **SDA-compatible optical terminals** and **"multi-GPU on-orbit compute modules with terabytes of storage"** for low-latency transfer, secure routing and **edge processing in space**.
- Future tranches add capacity and **100-gigabit optical** technology, backward-compatible.
- Customers: EO payload customers, **Axiom Space** collaboration (orbital data-centre nodes); a separate item references **Maverick Space Systems** taking capacity on a future 10-satellite tranche.
- Network promise (web-search summary of Kepler's own material): "gigabit, sub-second internet connectivity anywhere in LEO".

## Primary (SatNews — adds / differs)
- Launch dated **9 Feb 2026** (Twilight-1 rideshare, SLC-4E) into **SSO**; "Aether" series; new batches planned **every two years**; applications: EO, defence, science. Kepler's page carries an **11 Jan 2026** date — the discrepancy is probably a pre-announcement vs actual-launch date; use **9 Feb 2026** for the launch.
- Web-search summary (not opened) of Kepler's earlier release: the 10 satellites host **40 SDA-T1-compatible OCTs** in total (4 per satellite); the Nov-2023 pathfinders each flew one **Tesat SCOT80** (SDA standard v2.1.2) and demonstrated space-to-ground optical to a **Cailabs** station in France.
- Kepler is also ESA's **HydRON Element 1 and Element 3** prime — see [[2026-04-17-via-satellite-esa-hydron-element-3-kepler]].

## Derived (our arithmetic — formula shown)
- 4 OCTs/sat × 10 sats = 40 OCTs; at SDA-standard ~2.5 Gbps per link (our assumption from the standard's baseline), aggregate ISL fabric ≈ **100 Gbps** for tranche 1 — modest; the "100 Gb" per-link generation is what makes a relay-to-ground path for raw EO data meaningful.
- A ~300 kg bus with multi-GPU compute is the **first commercial "relay + compute" node class** — power likely several hundred W to ~1 kW (our estimate; not disclosed).

## Relevance to the Entrant
- Kepler is the **most concrete in-orbit "data centre" actually flying**: relay + GPUs + storage. For the Entrant it is either the backbone to buy latency from (sub-second LEO connectivity) or the competitor that bundles compute with its relay.
- The Axiom/Kepler pairing shows the likely industry structure: **relay operator provides the pipe and hosts compute nodes**; application players (EO insight) sit on top. The Entrant fits the top layer.
- Canadian-owned but ESA-funded (HydRON) — Kepler is "European enough" for ESA procurement, which narrows the sovereign-relay gap the Entrant might otherwise claim.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
- [[intel/wiki/eo-edge-compute-value-chain]]
