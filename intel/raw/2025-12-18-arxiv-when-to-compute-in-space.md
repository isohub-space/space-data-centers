---
type: intel
tags: [sdc, intel/raw, research/paper, space/orbital-compute, space/eo-edge, workload-placement, economics/cost-model]
source: arXiv (AIAA SciTech 2026)
url: https://arxiv.org/abs/2512.17054
author: Rajiv Thummala, Gregory Falco (Cornell University)
published: 2025-12-18
captured: 2026-10-04
primary: self
---
# When to compute in space

## Reported (what the paper claims)
- Compute-tier selection as a scalarised multi-criteria optimisation over four tiers — onboard flight
  computer (FC), orbital data centre (ODC), ground-station edge (GSE), terrestrial data centre (TDC) — with
  ~15 metrics (p99 latency, success probability, quality, energy/task, peak power, power margin, thermal
  margin, link availability, contact duty cycle, data-reduction ratio, cost/task, ops burden, availability,
  altitude, mass) normalised to [0,1], weighted, penalised for missing data (U_eff = U_base − λ(1−φ)), and
  gated by hard constraints (latency, reliability, quality, cost, regulatory).
- **Case 1 — onboard intrusion detection:** FC vs ODC vs GSE vs TDC with 250 ms p99 limit; GSE (600 ms) and
  TDC (320 ms) infeasible; **ODC 0.745 vs FC 0.742** — ODC wins on energy (90 vs 150 J/task), ops and link
  availability despite 180 vs 90 ms latency.
- **Case 2 — Suncatcher-style training:** hypothetical metrics; **ground TPU DC 0.784 > LEO TPU cluster
  0.675 > hybrid split 0.352**; ground GPU DC infeasible on cost ($15 > $14/unit). LEO credited with 20×
  data reduction, 150 kW power margin, 575 kg compute mass vs 2,000 kg ground.
- Relays a SpaceNews-sourced claim (Callison & Minafra, Dec 2025): 1,000 kg of arrays at $2,500/kg =
  $2.5 M → "500 kW of capacity at roughly $5,000 per kW" and "zero opex post-deployment".
- Future work: Pareto fronts instead of scalar utility; security/ITAR as hard gates; temporal design-phase
  effects.

## Primary (method / assumptions a sceptic would attack)
- All metric values are **notional** ("hypothetical and should not be conflated with a genuine Google
  Suncatcher system"); results demonstrate the method, not any conclusion about orbit vs ground.
- The relayed "$5,000/kW" PV claim implies **2 kg/kW for a complete power system** — ~10× better than any
  anchor in [[intel/raw/2026-04-29-arxiv-turyshev-odc-economic-viability]] (PV alone 6–33 kg/kW) and is
  press, not primary. Do not propagate.
- Equal treatment of an ODC as an existing tier with measured latency/cost is premature.

## Derived (our arithmetic — formula shown)
- The relayed PV figure: 500 kW / 1,000 kg = 500 W/kg *system-level* — matches only the ISCR paper's
  *array-level* 506 W/kg aspiration and exceeds flown arrays (~60 W/kg) by ~8×.

## Relevance to the Entrant
- Provides a ready-made, citable **decision framework** the Entrant can populate with real numbers to show customers
  when on-board/ODC inference beats ground processing (latency gates kill ground tiers for alerting
  workloads — exactly the Entrant's pitch).
- Cornell (Falco) is working the orbital-compute placement/security problem; potential academic ally.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]] (placement framework; latency-gate argument)
