---
type: intel
tags: [sdc, intel/raw, research/paper, space/orbital-compute, space/optical-isl, space/formation-flight]
source: arXiv (AAS 26-754)
url: https://arxiv.org/abs/2605.15335
author: Jules Pénot, Hamsa Balakrishnan (MIT AeroAstro)
published: 2026-05-14
captured: 2026-10-04
primary: self
---
# Designing Dense Satellite Clusters for Distributed Space-based Datacenters

## Reported (what the paper claims)
- Takes Suncatcher's constraints (R_min = 100 m spacing, R_max = 1,000 m cluster radius, 650 km SSO at
  98° inclination, unobstructed sun, stable ISL neighbours) and asks how many satellites fit.
- **Suncatcher planar design: 81 sats.** Inefficiencies: relative orbits of eccentricity √3/2 (2:1 ellipses)
  waste the disk, along-track spacing must be 2·R_min, square not hexagonal lattice.
- **Optimal planar cluster: 367 sats** (4.5×) — tilt the plane 60° (i_d = √3·e_d) so all relative orbits
  are *circular*; the cluster rotates rigidly, inter-satellite distances are constant, ISLs are permanent
  by construction, hexagonal packing. Scaling N ≈ 3.63 (R_max/R_min)².
- **3D cluster:** stacked inclined planes, N ≈ 0.27 (R_max/R_min)³; beats planar only for
  R_max/R_min ≥ 13.5 (264 sats at the Suncatcher parameters, i.e. *worse* than optimal planar there).
- Solar occlusion: Suncatcher design full exposure for satellite radius R_sat < 50 m; optimal planar < 19 m;
  3D only < 3 m (at R_sat = 15 m, half a Starlink V2-mini wingspan, some core 3D nodes are "almost
  permanently shadowed").
- **Network:** a naive mesh scales badly (planar bisection ∝ N^½, 3D ∝ N^⅔). Instead dedicate some
  satellites as switches and map a **VL2-like Clos fabric** by integer programming (Gurobi): feasible for
  L ≥ 3 layers across R_max 500–2,000 m, k = 4–12 ISLs per switch satellite, R_sat 0–15 m. Fraction of
  compute (ToR) satellites r = k/(k + 4L − 6).
- Explicitly out of scope: launch cost, radiation, link data rates, relative cost vs terrestrial.

## Primary (method / assumptions a sceptic would attack)
- Pure Keplerian + J2-free geometry; no differential drag, SRP, or station-keeping Δv budget — the same gap
  as Google's paper.
- Satellites modelled as points (then spheres); real deployed arrays of 30 m span break the 3D design and
  nibble at the planar one (occlusion from R_sat ≥ 19 m).
- Clos mapping proves *topological* feasibility only; each switch satellite must sustain k = 4–12
  simultaneous optical links with the Google-class 1 µrad pointing — mass/power of such a node is not sized.
- The paper is an orbital-mechanics result; it does not establish that 367 compute satellites can also
  radiate their heat without mutual IR heating (see [[intel/raw/2026-06-23-arxiv-hot-ai-cold-space-thermal-crosstalk]]).

## Derived (our arithmetic — formula shown)
- Compute fraction for k = 10, L = 3: r = 10 / (10 + 12 − 6) = **62.5 %** — 37.5 % of a cluster's
  satellites would be pure switches carrying no compute. For k = 12, L = 3: 66.7 %.
- Density gain vs Suncatcher at fixed R_max: 367 / 81 = **4.5×** more satellites, i.e. ~4.5× cluster
  power for the same debris cross-section and the same ISL range.
- This directly answers [[intel/raw/2026-07-15-arxiv-van-berkel-cost-network-limits]]'s torus assumption:
  a Clos fabric is mappable, so his 12,880× bisection penalty is an upper bound on the problem, not a limit.

## Relevance to the Entrant
- Not directly applicable (the Entrant is single-satellite / small-constellation inference), but the **rigidly
  rotating circular-relative-orbit formation** is the cleanest published recipe for permanent ISLs between
  a handful of co-orbiting satellites — relevant if the Entrant ever pairs a sensor sat with a compute sat.
- The switch-satellite overhead (≥ 1/3 of nodes) is a quantitative reason small operators should avoid
  cluster architectures.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]] (formation-flight state of the art; MIT as academic player)
- [[intel/wiki/orbital-compute-launch-economics]] (switch-node overhead as a hidden cost of clusters)
