---
type: scenario
tags: [sdc, scenario/entrant, space/orbital-compute]
updated: 2026-10-04
---
# The Entrant — a fictitious positioning case

> **Fictitious by design.** *The Entrant* is not a company. It is a modelling device: an
> early-stage European new-space entrant with ground-segment heritage, no flight hardware
> yet, and a decision to make — *where in the orbital-compute market is there a defensible
> position in 2026–2029?* Every "what this means for the Entrant" section in this vault is
> advice to that device. Any resemblance to a real company is coincidental and unintended.

## The hypothesis under test

The Entrant's candidate product is **in-orbit processing for Earth-observation
time-to-insight**: collection → optical links → compute in orbit → insight delivery, with
processing *inside* the chain rather than after downlink. The figure of merit is
**minutes from acquisition to actionable output**, not downlink volume or $/kW.

## Decision factors the vault tracks

| Factor | Where it is analysed |
|---|---|
| Launch price and cadence — can the plan close at today's rideshare prices? | [[intel/wiki/orbital-compute-launch-economics]] |
| Specific mass, heat rejection, radiation, duty cycle — what a kW-class node can physically do | [[intel/wiki/orbital-compute-physical-constraints]] |
| Who else is in the segment, what they raised, what is flying | [[intel/wiki/orbital-data-center-landscape]] |
| The bottleneck, the latency bar, who pays, what onboard processing actually saves | [[intel/wiki/eo-edge-compute-value-chain]] |

## Positioning questions still open

- [ ] Funding path: grant-first (ESA InCubed, national defence R&D) or seed-first?
- [ ] First mission: own satellite, hosted payload (D-Orbit ION, AI-eXpress), or software-only
  on partners' compute (the Satlyt model)?
- [ ] Anchor customer class: defence/ISR, maritime, civil protection
- [ ] Relay strategy: own ground segment, partner (Kepler/HydRON/Tesat), or both
- [ ] EUMETSAT's position on onboard processing (nothing public found)
