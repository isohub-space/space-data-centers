---
type: intel
tags: [sdc, intel/raw, research/paper, space/orbital-compute, space/thermal, space/radiation, space/optical-isl, space/launch, economics/cost-model]
source: arXiv
url: https://arxiv.org/abs/2511.19468
author: Agüera y Arcas, Beals, Biggs, Bloom, Fischbacher, Gromov, Köster, Pravahan, Manyika (Google)
published: 2025-11-22
captured: 2026-10-04
primary: self
---
# Towards a future space-based, highly scalable AI infrastructure system design (Project Suncatcher)

> Supplement to [[intel/raw/2026-10-01-techcrunch-google-suncatcher-1800-starship-launches]], which already
> carries the learning-curve, ISL and TID/SDC headline numbers. This note records only what that capture
> lacks. v1 2025-11-22; v2 2026-06-17 ("re-ran radiation test with improved methods, improved rough
> estimates"). Numbers below are from v2.

## Reported (what the paper claims)

**Thermal / radiator model — there is none.** Thermal management is listed as an *open* challenge, not a
solved input: "Effective thermal management is a critical optimization challenge for power-dense TPUs
operating in a vacuum… heat pipes and radiators… preferably passive." No radiator area, temperature,
emissivity or kg/kW figure is given anywhere in the paper. The Starlink-v2-mini bus is used as the
mass/power proxy *including* whatever radiator it carries.

**Specific mass (kg/kW) — proxy-based, not designed.**
- Starlink v2 mini: 575 kg, ~105 m² solar array, 22 % cells, 1.361 kW/m², 90 % packing → **~28 kW/sat**.
- Launched-power price at current $3,600/kg (reusable Falcon 9): **$14,700/kW/yr**; at $200/kg: **$810/kW/yr**
  (5-year amortisation). Across Starlink v1, OneWeb, Iridium NEXT the $200/kg range is **$810–7,500/kW/yr**
  — "extremely large range… driven by differences in use case and optimisation priorities".
- Explicitly excluded from the comparison: spacecraft build, infrastructure/buildings, chips, ground segment.
  The paper calls it "not a full economic analysis".

**Ground link.** Pilot missions use **radio**; scaled operation needs optical downlink, with
atmospheric turbulence, relative-motion and beam-tracking cited as unsolved. State of the art quoted:
NASA TBIRD **200 Gbps** LEO→ground (2023). Dawn-dusk SSO "will increase latency to some ground locations".

**Debris / collision.** No debris-flux or Kessler analysis. Collision avoidance is delegated to an
"ML-enhanced flight control model"; passive safety option = per-satellite out-of-plane oscillation
superimposed on the planar Keplerian formation. J2 drift for the 81-sat/1 km cluster is reduced to
**< 3 m/s/yr per km** of max distance by trimming the ellipse axis ratio to 2:1.0037. Satellite count
scales **N ~ R²** for fixed minimum spacing; beating that needs non-Keplerian (e.g. electromagnetic)
formation flight and attention to mutual occlusion of radiated heat.

**ISL budget details.** 5 W EDFA, 10 cm aperture, gain 105.1 dB each end, λ 1.55 µm, −3 dB other losses;
coherent 400G PM-16QAM needs ≈ −20 dBm/channel → **0.24 mW** for 24 channels on a 100 GHz grid = **9.6 Tbps
bidirectional per aperture** (12.8 Tbps on 75 GHz). Confocal near-field limit L = πa²/λ ≈ **5 km** for
a 10 cm beam; pointing requirement **~1.0 µrad** at 5 km. Photons-per-bit: OOK ~71, PM-16QAM ~196,
Shannon limit 1.39.

**Radiation — host side (new vs. earlier capture).** Host CPU SEFI ≈ **1 per 450 rad(Si)**, host RAM
≈ **1 per 400 rad(Si)**. Beam: UC Davis 76-inch cyclotron, 67 MeV protons, 8 cm aperture, 2 pA–1 nA
(2 rad/min – 1 krad/min); chips irradiated from the underside through chassis + PCB.

**Paper's own open-problem list.** (1) thermal management; (2) high-bandwidth optical ground comms;
(3) on-orbit reliability and repair — "simplest solution is redundant provisioning"; (4) SEE impact on
*training* and system-level mitigations; (5) moving from discrete bus/radiator/array/compute to an
integrated compute-radiator-power design ("the floor on fuel price means there will always be an
incentive to minimise mass"), including neural-cellular-automata substrates.

## Primary (method / assumptions a sceptic would attack)
- The $/kW/yr "comparability" result compares **launch-only cost of a comms bus** to **terrestrial
  power opex**. Build cost, ground segment, radiators sized for compute heat and 5-yr replacement are all
  outside the boundary. [[intel/raw/2026-04-29-arxiv-turyshev-odc-economic-viability]] rebuilds the
  comparison with those terms and reaches the opposite sign.
- A Starlink bus radiates a few kW of RF/avionics heat, not 28 kW of compute heat. Using its kg/kW as the
  compute-satellite proxy silently assumes the radiator problem is free.
- SDC rate "1 per 3 M inferences" assumes 1 inference/s per chip; the per-rad rate (1/17 rad) is the
  transferable number.
- Formation-flight feasibility rests on "a simplistic numerical calculation" and a cited D'Amico thesis;
  no propellant budget for 81 satellites is given.

## Derived (our arithmetic — formula shown)
- Specific mass proxy: α = 575 kg / 28 kW = **20.5 kg/kW** (Starlink v2 mini). Check: 20.5 × 3,600 / 5 =
  $14,760/kW/yr ✓.
- The $810–7,500/kW/yr range at $200/kg over 5 yr ⇒ α = C·L/P = **20–188 kg/kW** across the four buses.
- Launch-only capital at $200/kg: 20.5 × 200 = **$4,100/kW** (vs Turyshev's 10–40 k$/kW terrestrial
  infrastructure benchmark — see that note).
- Host reboots: 150 rad/yr ÷ 450 + 150 ÷ 400 ≈ **0.7 host SEFIs per host-year** — small, but each one is a
  full inference-service interruption.

## Relevance to the Entrant
- The hyperscaler paper leaves *exactly* the subsystems a small EO-edge operator must get right — thermal,
  downlink, reliability — as open problems. Nothing in it reduces the Entrant's engineering risk; its value is
  the TPU radiation dataset and the ISL link-budget method.
- Google's own pilot uses **radio** downlink and bursts the TPU on a Planet bus; the near-term product
  shape is "small inference payload, duty-cycled" — the same regime as EO edge compute.
- The 1 µrad / 5 km / 10 cm ISL design point is the number to compare against any ISL vendor the Entrant talks to.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]] (add: boundary of the $810/kW/yr claim; α = 20.5 kg/kW; no thermal model)
- [[intel/wiki/orbital-data-center-landscape]]
