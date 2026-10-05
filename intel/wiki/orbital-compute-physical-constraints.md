---
type: concept
tags: [sdc, intel/wiki, space/orbital-compute, space/thermal, space/radiation, space/debris]
updated: 2026-10-05
sources: literature lane + sceptics lane, 2026-10-04 — see [[intel/raw/_index]]
---
# Orbital compute — physical constraints

What limits a compute satellite before money does: **mass per kilowatt**, **heat
rejection**, **radiation**, **obsolescence**, and the **environment** it leaves behind. The
economics in [[intel/wiki/orbital-compute-launch-economics]] inherit every number here.

## 1 · Specific mass — the swing term is the radiator

Specific mass $\alpha$ (kg/kW delivered to compute) spans an order of magnitude in the 2026
literature, and the gap *is* the optimist/sceptic divide:

| Design | $\alpha$ (kg/kW) | Status | Source |
|---|---:|---|---|
| Tether architecture (10 kg node / 2 kW; PV at 1,000 W/kg) | **5** | paper | [[intel/raw/2025-12-09-arxiv-tether-orbital-ai-data-centers]] |
| Integrated solar-compute-radiator panels (ISCR): 148.8 t / 16.4 MW = 112.5 kW/t | **8.9** | paper | [[intel/raw/2026-04-09-arxiv-iscr-integrated-solar-compute-radiator]] |
| SpaceX FCC filing ("100 kW/t"); AI1 sat 150 kW peak, 70 m span | **~10** | filing | [[intel/raw/2026-02-02-via-satellite-spacex-xai-fcc-million-satellites]] |
| Google's Starlink-v2-mini proxy (575 kg / 28 kW), **no compute radiator** | **20.5** | paper | [[intel/raw/2025-11-22-arxiv-google-suncatcher-system-design]] |
| Turyshev (JPL) full node incl. structure, shielding, comms | **34–59** | paper | [[intel/raw/2026-04-29-arxiv-turyshev-odc-economic-viability]] |
| Turyshev with servicing, spares | 50–75 | paper | [[intel/raw/2026-08-27-arxiv-turyshev-odc-operations-maintenance]] |

Flown specific power: Cowboy 44 W/kg, Starcloud-3 67 W/kg, ABI 50 W/kg, SpaceX claim 100
W/kg. The two lowest $\alpha$ figures assume **500–1,000 W/kg PV** vs ~60 W/kg flown (iROSA).
Radiators + arrays are **65–70% of satellite mass**
([[intel/raw/2026-06-11-ieee-spectrum-thermodynamics-orbital-data-centers]]).

## 2 · Heat rejection

Radiation is the only sink: $Q = \varepsilon \sigma A T^4$ (plus view-factor losses to Earth
IR and albedo that every simple model ignores). Area per kW is set almost entirely by the
assumed radiator temperature — which is why sources differ 10×:

| Source | Assumption | m²/kW |
|---|---|---:|
| van Berkel | 370 K, two-sided ideal ("GPUs are designed to operate at 370 K" — Musk) | **0.95** |
| This vault, derived | 330 K, ε = 0.9, two-sided, 0 K sink | 0.83 |
| IEEE Spectrum / ABI (Cavalier) | 700 W H100: 3 m² @ 20 °C, 1.4 m² @ 60 °C, 1 m² @ 85 °C | 1.4–4.3 |
| Turyshev | 2,500 m²/MW IT | **2.5** |
| ISCR | 25–35 °C single-sided; radiator 2.4 kg/m² → **7.0 kg/kW**, 76% of mass | 2.9 |
| Space-CIM | 100 W/m² at 85 °C (starved; its 10–40× CIM-over-GPU result is an artefact) | 10 |

Sources: [[intel/raw/2026-07-15-arxiv-van-berkel-cost-network-limits]],
[[intel/raw/2026-06-11-ieee-spectrum-thermodynamics-orbital-data-centers]],
[[intel/raw/2026-06-04-arxiv-space-cim]]. Emissivity degradation adds **+40% area after 5
years**. SpaceX's filing claims **1,400 W/m²** radiators vs ABI's implied ~640 W/m² — a 2.3×
gap on the single most important thermal number.

**Running cold is also an efficiency lever:** ISCR claims > 30% energy per token from
operating silicon at 35 °C instead of 105 °C junction — the design lever a small operator
can pull without Starship.

### Thermal binds first on flown COTS hardware

BUPT-1 (12U, 490 km SSO, ~4 months, [[intel/raw/2026-08-21-arxiv-bupt-ai-infrastructure-in-space]]):
one accelerator reaches the 30 °C structural limit in ~9 h; two co-located in ~40 min;
continuous compute drives battery DoD to 35% vs a 30% limit; a 2B-parameter VLM hits the
55 °C shutdown in **48 s**. Google's first Suncatcher runs its TPU in **15-minute bursts**
([[intel/raw/2026-10-01-npr-google-suncatcher-launch-sceptics]]); Starcloud-1's radiator was
too weak for full GPU power. **Duty cycle, not TOPS, is the spec that matters for an EO
node.**

## 3 · Radiation — inference yes, training no, and silent corruption is the failure mode

Google's TPU v6e under 67 MeV protons (dawn-dusk SSO ≈ 150 rad(Si)/yr behind 10 mm Al-eq):
HBM irregularities at **2 krad** vs 750 rad 5-yr dose (2.7× margin); SDC ≈ **1 per 17 rad**;
host SEFI 1 per 400–450 rad ([[intel/raw/2025-11-22-arxiv-google-suncatcher-system-design]]).

*Derived — why workload class decides viability:*

| Workload | Dose | Expected silent corruptions |
|---|---|---|
| One chip, 5-yr life, 1 inf/s | 750 rad | ≈ 44 → **1 per ~3.6 M inferences** (local, retry/vote) |
| Training, 4,096 chips × 3 months | 37.5 rad/chip | ≈ 2.2/chip → **~9,000 per run**, propagated into every weight |

Independent COTS data ([[intel/raw/2026-09-04-arxiv-tensil-proton-irradiation]],
[[intel/raw/2025-03-05-arxiv-linux-under-radiation-cots-socs]],
[[intel/raw/2024-07-16-arxiv-rednet-application-aware-radiation]]):
- Unmitigated Zynq + LPDDR4 ResNet-20: one event returned a class **absent from the input
  set for 39 consecutive inferences while every liveness monitor stayed green**. Output
  checking, not watchdogs, is the mitigation.
- 40 nm COTS SoCs σ 3–8e-9 cm²; 14 nm FinFET ~10× lower, 90% of its failures via the eMMC
  path (storage, not logic).
- Derived from JASON-2 rates (1,336 km): a 2 GB weight set takes ~7,600 flips/day →
  periodic weight reload from protected storage is the dominant design item for large
  onboard models. BUPT-1 at 490 km saw zero observable SEE in months — altitude matters more
  than process node, and "zero" was uninstrumented.

Conclusion across van Berkel, ISCR, tether, Turyshev and the workload-matrix paper
([[intel/raw/2026-03-19-arxiv-which-workloads-belong-in-orbit]]): **inference only, single
node**. Training in orbit is proposed only by Sheffield's semantic-offload paper
([[intel/raw/2026-05-12-arxiv-communication-efficient-space-data-centers]]) and by Bezos.

## 4 · Networking inside a cluster

van Berkel: a torus of 100 Gb/s ISLs is **12,880× worse** in bisection than a terrestrial
pod → training 2–3 orders of magnitude slower. MIT
([[intel/raw/2026-05-14-arxiv-mit-dense-satellite-clusters]]) shows a Clos fabric *can* be
mapped onto a dense cluster (367 sats in 1 km) at the cost of ≥ 1/3 of satellites being pure
switches — van Berkel's figure is an upper bound on the problem, not a limit. Optical ISL
channel model ([[intel/raw/2026-09-15-arxiv-oisl-pointing-jitter-channel-model]]): 10 Gbps /
1 W / 10 cm / 1,000 km / 2 µrad jitter → outage 1.9e-10. Google's bench: 800 Gbps
unidirectional with COTS DWDM at short range.

## 5 · Obsolescence and servicing

GPU generations turn over in 1–2 years against a 5–7 year satellite life (2.5–5 generations
per spacecraft); hardware cannot be upgraded post-launch, so value must be extracted in
3–5 years ([[intel/raw/2026-06-09-jll-data-centers-in-space]]). Turyshev's O&M model puts
servicing logistics at 5.3–9 t/(MW·yr). CMU's Lucia: complexity "amplified by a factor of
10, maybe 100" ([[intel/raw/2026-10-01-npr-google-suncatcher-launch-sceptics]]).

## 6 · Environment and regulation

- Proposed: 1.23 M satellites vs ~14,000 active (88×); > 50,000 debris ≥ 10 cm; CRASH clock
  164 days (2018) → 3.8 days (Jan 2026); 6 of 16 modelled constellations cross the runaway
  threshold ([[intel/raw/2026-02-18-phys-org-conversation-megaconstellation-catastrophe]]).
- Re-entry particulates 366 → 887 t/yr (2020–24); a 1 Mt/yr constellation implies ~200,000
  t/yr re-entering ([[intel/raw/2026-03-11-mongabay-space-ai-data-centers-dangers]]).
- Carbon flips sign with the comparator: tether paper counts propellant only (orbit 10×
  cleaner than gas); Dirty Bits counts stage production + re-entry NOₓ (178.8 kgCO₂e/kg
  Falcon 9, re-entry = 10× launch) against solar+battery ground (orbit up to 10× dirtier)
  ([[intel/raw/2025-08-08-arxiv-dirty-bits-leo-carbon]]). Derived middle case: 36–163
  gCO₂e/kWh for 8.9–40 kg/kW.
- EU Space Act (proposed 2025-06-25, effective ~2028–30) brings data-service providers in
  scope and mandates debris plans ([[intel/raw/2025-06-25-noerr-eu-space-act-proposal]],
  [[intel/raw/2026-04-08-ep-thinktank-ai-data-centres-in-space]]).
- US: four data-centre constellations (1,239,600 satellites in total) are under FCC review;
  the FCC's July 2026 Space Modernization Order found large-constellation standards
  "premature"; the Office of Space Commerce certification pilot (opened 2026-08-20) names
  orbital data centres. GDPR still reaches EU-subject data processed in orbit; the US CLOUD Act
  reaches data a US provider holds wherever it is
  ([[intel/raw/2026-10-01-wilmerhale-orbital-data-centers-legal-reality]]).

## 7 · What this means for the Entrant

- Design to **duty cycle and radiator area**, not peak TOPS. Publish a measured
  sustained-compute figure (W continuous at X °C) — nobody in the market has one.
- **Output-level integrity checks** (redundant inference, voting, periodic weight reload
  from protected storage) are a credible, cheap differentiator against "we flew a Jetson".
- A kW-class EO node at ~500 km, 5-year life, on COTS silicon is **inside the envelope the
  literature supports**; a MW-class or training node is not.
- Small European operators sit on the right side of the EU Space Act's debris and
  environmental rules; GW-scale constellations do not.
