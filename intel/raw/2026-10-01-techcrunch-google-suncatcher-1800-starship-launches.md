---
type: intel
tags: [sdc, intel/raw, space/orbital-compute, space/launch]
source: TechCrunch
url: https://techcrunch.com/2026/10/01/google-thinks-spacexs-starship-has-to-launch-1600-times-before-space-data-centers-get-off-the-ground/
author: Tim Fernholz
published: 2026-10-01
captured: 2026-10-04
primary: "Agüera y Arcas, Beals, et al. (Google), 'Towards a future space-based, highly scalable AI infrastructure system design', arXiv:2511.19468; peer-reviewed version to appear in Joule"
---
# TechCrunch — Google thinks Starship has to launch 1,800 times before space data centres get off the ground

> **Headline correction.** The URL and original headline say **1,600**; TechCrunch
> corrected it to **1,800** launches. Use 1,800.

## Reported (what the article says)

**The launch event**
- Google's first orbital-compute prototype (**Project Suncatcher**) launched 2026-10-01 on a
  SpaceX rideshare from California — the first Google TPU in space.
- Satellite **built by Planet Labs** on a standard Planet platform. Goal: prove a TPU works in
  orbit — **1 kW continuous power**, chip cooling, run models and look for faults.
- Once commissioned, the TPU runs in **15-minute bursts** to stay inside the bus's power and
  thermal envelope.
- Next: a **two-satellite demo next year**, purpose-built for compute, linked by **laser
  communications**.
- Same rideshare: **100+ payloads**, including space-AI missions from **Satlyt** and
  **Cowboy Space Company**.
- Target architecture: **81 satellites in close formation**, processing in parallel.
  Travis Beals (Suncatcher lead): *"The bandwidth and the latency between TPUs really,
  really matters when you're trying to run a multi-rack workload… we're trying to look ahead
  to not just what workloads exist today, but where they will be in five years."*
- Framed as a **"long-term moonshot"** — the rockets needed to scale cost-effectively don't
  exist yet.

**The paper's launch-economics argument** (peer-reviewed white paper, to appear in *Joule*;
explicitly *not* an economic-feasibility study)
- SpaceX price "learning curve" of **~20%** since Falcon 1 → launch prices **≈ $200/kg by
  2035**.
- Reaching that needs Starship to fly **370,000 t** of payload ≈ **1,800 launches over 10
  years (180/yr)**, assuming **200 t per flight**.
- Starship has **never flown more than 5 times in a year**. Musk has suggested an hourly
  flight rate by 2029 ("Musk says a lot of things").
- Google is a major SpaceX investor.

**Radiation**
- Accelerator tests were redone after Google found the test configuration gave **more
  shielding** than flight would; re-test showed slightly more logic errors.
- Still confident in **large inference workloads for a 5-year satellite life**.
- Beals: *"The error rate is very low if you're thinking about typical inference operations,
  right? Like one in a million… On the other hand, it was already problematic for doing, say,
  some mega-scale training run where you're going to have many thousands of chips running for
  months."*

## Primary (arXiv:2511.19468 — where it differs from the press)

- **Learning rate is per doubling of cumulative launched mass (Wright's law), not "20% a
  year".** The article's "about 20% a year" is a mis-paraphrase; the time dimension enters
  only through the assumed launch cadence.
- Paper: < $200/kg by ~2035 at ~180 Starship launches/yr; **with 70% fewer launches, still
  ≈ $300/kg**. Independent Starship-4 bottom-up: internal cost ≲ $60/kg at 10× reuse,
  ≲ $15/kg at 100× reuse; customer price < $250/kg even with margin.
- Launched power price at $200/kg for a Starlink-v2-class bus ≈ **$810/kW/y** (≈ $1,200 at
  $300/kg) vs terrestrial data-centre power spend **$570–3,000/kW/y**.
- Cluster: 81 sats, **1 km radius, 650 km mean altitude, dawn-dusk SSO**; nearest-neighbour
  spacing oscillates **~100–200 m**; J2 drift trimmed to < 3 m/s/yr per km.
- ISL: bench demo **800 Gbps unidirectional (1.6 Tbps bidir)** with COTS DWDM; ~10 Tbps
  aggregate feasible at short range with spatial multiplexing.
- Radiation (TPU v6e Trillium, 67 MeV protons): HBM irregularities at **2 krad(Si)** vs
  5-yr mission dose **750 rad(Si)** (~150 rad/yr, 10 mm Al-eq); no TID failures to 15 krad;
  SDC ≈ **1 per 17 rad** → ~1 per 3 M inferences over 5 yr at 1 inf/s.
- (Press figures not yet cross-checked against the *Joule* version — the 370,000 t /
  1,800-launch figure is from the press piece; confirm when *Joule* publishes.)

## Derived (our arithmetic — formula shown)
- 370,000 t ÷ 200 t per flight = 1,850 ≈ 1,800 flights → 180/yr → one launch every ~2.0 days for 10 years; best year to date 5 flights → ×36.
- Learning-curve doublings to $200/kg: n = log(P₀/200)/log(1.25) — see [[intel/wiki/orbital-compute-launch-economics]] §1.

## Relevance to the Entrant
- The Entrant's segment (EO time-to-insight, kW-class) does not need Starship at 180/yr; its value is latency and bytes not downlinked, not $/kW.
- Radiation evidence favours inference workloads — the Entrant's class.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]] (done 2026-10-04)
- [[intel/wiki/orbital-data-center-landscape]] — Planet Labs, Satlyt, Cowboy Space Company
