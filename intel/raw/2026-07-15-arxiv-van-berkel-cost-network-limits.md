---
type: intel
tags: [sdc, intel/raw, research/paper, space/orbital-compute, space/optical-isl, space/thermal, economics/cost-model, critique]
source: arXiv
url: https://arxiv.org/abs/2607.14172
author: Kees van Berkel (TU Eindhoven; consultant to Snap)
published: 2026-07-15
captured: 2026-10-04
primary: self
---
# The Cost and Network Limits of Space-Based AI Compute

## Reported (what the paper claims)
- Scope: relative CapEx/OpEx factors for a **1 GW orbital** vs **1 GW terrestrial** AI data centre; based on an
  MPSoC'26 talk "AI in The Sky =? Pie in The Sky?". Explicitly *not* absolute $/token.
- **Launch is not the problem.** 1 GW ≈ 10,000 t (Musk's 100 kW/t) ≈ 50 Starship V3 flights; at $200/kg
  = **$2 B**, "modest compared to the CapEx of a terrestrial AI data center" (servers ≈ 60 % of TCO, Epoch AI).
- **Power:** 1,300 W/m² × 30 % → 400 W/m². Starlink V1 300 kg / 25 m² / 10 kW; V2 mini 800 kg / 100 m² /
  40 kW; **V3 2,000 kg / 250 m² / 100 kW** — "close to a 120 kW Blackwell rack", so one satellite ≈ one rack.
- **Cooling:** P = AσT⁴ (emissivity, absorbed heat, transport ignored). 40 kW at **T = 370 K** ("GPUs are
  designed to operate at 370 K" — Musk, X, 2026-01-20) → **A ≈ 38 m²** two sides combined (19 m² panel).
  Visual inspection of V2 mini suggests radiators **2–3× smaller** than this → either efficiency < 30 % or
  power banked to batteries. Passive cooling to 100 kW "looks plausible".
- **Radiation:** rad-hard parts (STM32V8 18 nm SOI, Versal 7 nm) "multiple generations behind… not an
  option" for cost-effective compute; relies on Google's 150 rad/yr, 750 rad/5 yr result.
- **Externalities:** LOFAR unintended emission 110–188 MHz from Starlink; NOAA re-entry study (10⁴ t/yr of
  Al₂O₃ aerosol → 1.5 K mesospheric anomaly) vs Musk's 10⁶–10⁷ t/yr target.
- **Network (core result).** 8,000 satellites × 100 kW. Terrestrial Clos (72-port ToR, 100 GB/s links, 2:1
  oversubscription): bisection **28,800 TB/s**, latency 4 µs. Orbital 2D torus (89×90): **2.25 TB/s**,
  1,800 µs; 3D torus (20³): **10 TB/s**, 600 µs — with Starlink-V2-class 12.5 GB/s (100 Gb/s) ISLs.
  Relative T_bandwidth: **12,880× (2D)**, **2,880× (3D)** worse; T_latency 450× / 150× worse.
- Bisection intensity for 1T-param training ≈ 500 kFLOP/B (k=6 FLOP/param/token, c=12 B/param, 1 M-token
  batch). Roofline: orbital training **2–3 orders of magnitude** slower; torus all-reduce crosses the
  bisection once per dimension, making it worse. Even at Google's 10 Tbps FSO links (dotted line) the torus
  stays inferior to Clos.
- **Inference:** confine to a single satellite/rack — "no need for the complex, dense satellite
  constellations". Prospects "promising".
- Conclusion: "cost-effective frontier-LLM training in space within the next 2–3 years is not credible
  and even a 10-year horizon appears optimistic".

## Primary (method / assumptions a sceptic would attack)
- Topology is *assumed* (2D/3D torus with 100 Gb/s links); the author concedes "they do not offer specifics
  on the network topology". [[intel/raw/2026-05-14-arxiv-mit-dense-satellite-clusters]] shows a VL2-style
  Clos fabric *can* be mapped onto a dense cluster, directly undercutting the torus premise.
- "Rather crude model": roofline on bisection bandwidth only; ignores pipeline/tensor parallelism inside
  a satellite and communication-reducing optimisers.
- Cost side takes Musk's 100 kW/t and $200/kg at face value — the opposite of the cautious network side.
  Compare [[intel/raw/2026-04-29-arxiv-turyshev-odc-economic-viability]] (34–59 kg/kW, i.e. 17–29 kW/t).
- Radiator estimate ignores emissivity and absorbed solar/Earth IR, which make it optimistic, then notes
  Starlink radiators are 2–3× *smaller* than even that.

## Derived (our arithmetic — formula shown)
- Radiator area per kW at 370 K: 38 m² / 40 kW = **0.95 m²/kW** (two sides combined; ideal).
- Specific mass implied by Starlink V3: 2,000 kg / 100 kW = **20 kg/kW** — 2× the 10 kg/kW (100 kW/t) that
  the $2 B launch figure assumes. At 20 kg/kW the launch bill doubles to $4 B; still "modest" vs 1 GW
  terrestrial CapEx (~$40–50 B at Epoch AI's numbers).
- Launch capital per kW at $200/kg and 10 kg/kW: **$2,000/kW**; at 20 kg/kW: $4,000/kW.
- Bisection ratio check: 28,800 / 2.25 = 12,800 ✓.

## Relevance to the Entrant
- Strongest independent argument that **orbital training is off the table this decade** and orbital
  **single-node inference is the viable product** — aligns the Entrant's EO-inference positioning with the
  critical literature, not just with Google's optimism.
- "One satellite ≈ one rack" framing is useful: the Entrant's unit of sale is a satellite's worth of inference,
  not a cluster.
- The externality section (radio-astronomy leakage, re-entry aerosols) is a regulatory risk for any
  European LEO operator; worth tracking for ESA/EU licensing.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]] (training infeasibility via bisection bandwidth; 20 kg/kW Starlink V3)
- [[intel/wiki/orbital-data-center-landscape]] (critical-literature column)
