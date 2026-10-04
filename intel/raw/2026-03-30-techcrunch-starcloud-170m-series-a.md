---
type: intel
tags: [sdc, intel/raw, market/startups, company/starcloud, funding, economics/unit-cost, hardware/nvidia]
source: TechCrunch
url: https://techcrunch.com/2026/03/30/starcloud-raises-170-million-series-ato-build-data-centers-in-space/
author: Tim Fernholz
published: 2026-03-30
captured: 2026-10-04
primary: none (company announcement; HPCwire carried the press release — 403 on fetch)
---
# TechCrunch — Starcloud raises $170M Series A to build data centers in space

## Reported (what the source says)

**Round**
- **$170M Series A at $1.1B valuation**, led by **Benchmark and EQT Ventures**; **total raised $200M**.
- Unicorn **17 months after YC demo day** (Futurum 2026-04-02: "fastest startup in Y Combinator
  history to achieve unicorn status").

**Starcloud-1 (launched Nov 2025)**
- Payload: one **Nvidia H100**. Ran analysis on **Capella Space** radar data; "trained an AI model
  in orbit"; ran "a version of Gemini" *(other outlets say **Gemma**, Google's open model — likely
  the correct name)*.
- **One Nvidia A6000 GPU failed during launch.**

**Starcloud-2**
- Launch "later this year" (**2026**). Multiple GPUs incl. an **Nvidia Blackwell** chip and an
  **AWS server blade**; also a **Bitcoin-mining computer**. "Largest deployable radiator flown on a
  private satellite."
  *(Contradiction: TechCrunch 2026-08-21 later describes Starcloud-2 as **8 kW satellites with two
  rideshare launches in 2027**; introl 2026-02-21 said Oct 2026; Crusoe partnership says satellite
  launch late 2026, GPU capacity early 2027.)*

**Starcloud-3**
- **200 kW, three-ton spacecraft**, launched on **Starship**.
- Target: **$0.05 per kWh** of power, assuming **$500/kg** commercial launch cost; commercial
  Starship access expected **2028–2029**.

**Context numbers quoted**
- "Dozens" of advanced GPUs on orbit vs **~4M** terrestrial GPUs sold in 2025.
- Starlink constellation power output **~200 MW**; US data-center construction **25+ GW**.
- Competitors named: Aetherflux, Google Project Suncatcher, Aethero, SpaceX (seeking 1M sats).
  Johnston on SpaceX: *"They're mainly planning on serving Grok and Tesla workloads."*

**Customers (per Futurum 2026-04-02 analysis of the same round)**
- Crusoe, AWS, Google Cloud named as customers. Futurum: break-even launch cost **~$500/kg**,
  moving toward **~$1,000/kg** as terrestrial land costs rise; cost-competitive **mid-to-late 2028**.

## Primary (where the underlying document differs or adds)
- See [[intel/raw/2024-09-01-starcloud-whitepaper-why-train-ai-in-space]] — the 2024 white paper
  assumed **$30/kg** launch and **$0.002/kWh** energy; by March 2026 the company's own public
  numbers are **$500/kg** and **$0.05/kWh**: a **17× launch-cost** and **25× energy-cost** walk-back.

## Derived (our arithmetic — formula shown)
- Starcloud-3 specific power: 200 kW / 3,000 kg ≈ **67 W/kg** whole-spacecraft (vs. ABI's 2,000 kg
  / 100 kW example = 50 W/kg).
- Launch cost per kW at $500/kg: 3,000 kg × $500 / 200 kW = **$7,500/kW** one-off — comparable to
  terrestrial DC construction cost per kW, before the compute is paid for.

## Relevance to the Entrant
- The one hard $/kWh number Starcloud publishes ($0.05) is **roughly European wholesale power
  price**, i.e. the pitch is no longer "22× cheaper energy" but parity plus siting/latency
  advantages — the same argument the Entrant makes for EO processing in orbit.
- Starcloud-1 doing **Capella SAR analytics** is a direct precedent for the Entrant's workload class
  (EO edge inference on a COTS GPU).
- An A6000 lost at launch on a 60 kg bus is a reminder that COTS GPU ruggedization, not
  radiation, is the first-flight risk.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
