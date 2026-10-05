---
type: concept
tags: [sdc, intel/wiki, space/orbital-compute, market/competitors, market/funding, market/europe]
updated: 2026-10-05
sources: startup, incumbent and Europe lanes, 2026-10-04 — see [[intel/raw/_index]]
---
# Orbital data-centre landscape

Who is building orbital compute, by **workload class** — because the class, not the logo,
decides whether a player is in the Entrant's market. Three tiers: (A) GW-scale AI compute bets,
(B) kW-class edge / space-native processing (the only tier with revenue), (C) the enabling
layers (relay, bus, chips, programmes). Economics in
[[intel/wiki/orbital-compute-launch-economics]]; the EO segment in detail in
[[intel/wiki/eo-edge-compute-value-chain]].

## A · GW-scale AI compute — the 2030s bet

| Player | Plan | Funding / scale | First hardware | Source |
|---|---|---|---|---|
| **SpaceX / xAI** | AI1 sat 150 kW peak, 70 m span, 600–800 km; FCC: 1M sats, 100 kW/t, 1 Mt/yr | merger Feb 2026; IPO raised $86B (Jun 2026), stock −50% by Jul | prototypes early 2027; "1 GW/yr end-2027" | [[intel/raw/2026-02-02-via-satellite-spacex-xai-fcc-million-satellites]], [[intel/raw/2026-04-22-tnw-spacex-ipo-orbital-dc-risk-disclosure]] |
| **Starcloud** (ex-Lumen Orbit) | SC-2 8 kW (2027) → SC-3 200 kW / 3 t on Starship (2028–29); FCC 88,000 sats; next sat mines Bitcoin | $170M A @ $1.1B (Mar 2026) + $250M A-ext @ $2.3B (Aug 2026); Nvidia $25M | SC-1 flown Nov 2025 (H100, Capella SAR) | [[intel/raw/2026-08-21-techcrunch-starcloud-250m-series-a-extension]], [[intel/raw/2026-10-04-wikipedia-starcloud]] |
| **Cowboy Space** (ex-Aetherflux) | 1 MW nodes, 20–25 t, ~800 GPUs, all-optical, own rocket; FCC "Stampede" 20,000 sats | $50M A (2025) + $275M B @ $2B (May 2026); DoD OECIF multi-year support | Reason-1 launched 2026-10-01 (power-beaming + optics/thermal demo, no compute); Reason-2 optical downlink 2027; first MW node end-2028 | [[intel/raw/2026-05-11-techcrunch-cowboy-space-275m-series-b]], [[intel/raw/2026-05-18-satnews-cowboy-stampede-fcc-20000]], [[intel/raw/2026-10-01-businesswire-cowboy-reason-1-power-beaming]] |
| **Blue Origin "Project Sunrise"** | FCC 51,600 sats, 500–1,800 km SSO; TeraWave backhaul; no per-sat power disclosed (ambition indeterminate ~20×) | corporate | 0 flown; New Glenn pad out > 1 yr | [[intel/raw/2026-03-20-newspaceeconomy-blue-origin-project-sunrise-fcc]] |
| **Google Suncatcher** | 81-sat formation, TPUs, dawn-dusk SSO; R&D "moonshot" | corporate; Planet builds | MVP flown 2026-10-01 (4 Trillium TPUs, ~1 kW, 15-min bursts); 2-sat laser demo 2027 | [[intel/raw/2026-10-01-google-blog-suncatcher-prototype-in-orbit]], [[intel/raw/2025-11-04-planet-build-operate-suncatcher-platform]] |
| **Orbital (LA) + Reflex Aerospace (Munich)** | up to 100,000 sats × ~250 kW; Reflex exclusive bus | $5M pre-seed; Reflex €59M | none | [[intel/raw/2026-09-16-exterra-orbital-reflex-aerospace-german-bus]] |
| **Thales Alenia ASCEND** (EU, Horizon Europe) | 10 MW modules, 35,000 m² PV each; **1 GW before 2050**; needs 10× cleaner launcher, in-orbit robotic assembly | undisclosed study budget | PoC architecture 2031 | [[intel/raw/2024-06-27-thales-alenia-ascend-feasibility-results]] |

Demand signals: Anthropic–SpaceX "multiple GW orbital" agreement
([[intel/raw/2026-05-06-anthropic-spacex-compute-deal-orbital-gigawatts]]); Eric Schmidt's
grid rationale (29 GW → 67 GW) behind the Relativity purchase — the ODC link is press
inference, not a stated plan ([[intel/raw/2025-05-05-techspot-schmidt-relativity-space-data-centers]]).
All of tier A depends on Starship at 200 t × 180/yr; none has orbital-compute revenue.
Regulatory queue: the FCC has accepted **four** data-centre constellations for review —
1M, ~88,000, ~51,600 and ~100,000 satellites, 1,239,600 in total — and declined to set
large-constellation standards yet; the US Office of Space Commerce opened a certification
pilot that names orbital data centres
([[intel/raw/2026-10-01-wilmerhale-orbital-data-centers-legal-reality]]).

## B · kW-class edge and space-native processing — the tier with revenue

| Player | Offer | Status | Funding | Source |
|---|---|---|---|---|
| **Axiom Space + Kepler** | 2 ODC nodes on Kepler relay sats; 2.5 Gbps SDA optical; Red Hat Device Edge; EO/PED, sovereign cloud | **operational since 2026-01-11** — the only commercial ODC flying | corporate | [[intel/raw/2025-04-07-axiomspace-odc-nodes-press-release]], [[intel/raw/2026-01-11-kepler-first-tranche-optical-relay-satellites]] |
| **Satlyt** | software-only multi-tenant orbital compute; Gemma onboard cut EO downlink > 60% | 3 missions flown; NASA, SDA customers; Transporter-18 Oct 2026 | $8M seed (Oct 2026) | [[intel/raw/2026-10-01-techcrunch-satlyt-8m-seed]] |
| **Satellogic Merlin** | vertically integrated EO: 1 m, 10-band, 170 km swath; onboard-AI alerts "within 30 min"; ISL cues 50 cm follow-up without a ground station | Merlin.01 launched 2026-10-01; FOC H2 2027 | listed (NASDAQ) | [[intel/raw/2026-10-02-globenewswire-satellogic-merlin-first-launch]] |
| **Atomic-6** | capacity marketplace + solar/radiator modules | **$3.5M/month per 100 kW rack** — the only public price | — | [[intel/raw/2026-04-13-payload-atomic-6-odc-space-marketplace]] |
| **Sophia Space** | thermal-integrated TILE racks, "92% power to compute"; Nvidia partner | flight test late 2027 | $10M seed (Feb 2026) | [[intel/raw/2026-02-27-interestingengineering-sophia-space-10m-seed]] |
| **Lonestar** | sovereign storage / DRaaS, lunar → LEO (StarVault) | Freedom on IM-2 (lander tipped); StarVault Oct 2026 | $6.6M (Jan 2026) | [[intel/raw/2026-04-15-lonestar-starvault-sovereign-storage-leo]] |
| **Edge Aerospace** (LU) | orbital DC architecture; "only SpaceX could do what ODC folks claim" — positions on downlink relief | **ESA Space Cloud study (May 2026)**; demo payload Mar 2026 | ESA + LU MoD contracts | [[intel/raw/2026-05-05-payload-esa-edge-aerospace-space-cloud]] |
| **Planetek + AIKO (IT)** | AI-eXpress multi-tenant onboard AI (PolarFire SoC); tenants Eni, IBM, Ubotica | 3 sats, last 2025-11-28 | ESA InCubed | [[intel/raw/2025-11-28-planetek-ai-express-third-satellite]] |
| **Ubotica (IE)** | CogniSAT platform; Φsat-1 heritage; "insight within 5 min" when a link exists | CogniSAT-6 (2024); NASA JPL demo 2025 | **$11M Series A** (Jun 2026), maritime | [[intel/raw/2026-06-23-spacenews-ubotica-11m-series-a]] |
| **The Entrant** (fictitious) | in-orbit processing for EO time-to-insight | scenario | — | [[scenario/entrant]] |

European onboard-compute **hardware** suppliers (not operators): Unibap (SE; iX10, ~0.1–0.5
TOPS/W; SEK 17.3M/quarter revenue, −SEK 13M operating result —
[[intel/raw/2025-11-05-investing-unibap-q3-2025-earnings]]), KP Labs (PL; Leopard 3 TOPS,
0.3 TOPS/W, Intuition-1 — [[intel/raw/2025-08-24-satnews-kp-labs-intuition-1-leopard-dpu]]),
EDGX (BE; Sterna ≥ 100 TOPS Q2 2026, Morus ≥ 250 TOPS 2027, ESA ARTES —
[[intel/raw/2024-10-08-esa-artes-edgx-ascend-dpu-family]]), D-Orbit (IT; ION hosted compute,
€150M Series C — [[intel/raw/2024-09-27-europeanspaceflight-d-orbit-series-c-150m]]), Ramon.Space
(rad-hard, [[intel/raw/2023-06-28-ramonspace-26m-series-b-space-computing]]). The compute
curve is moving to COTS GPUs 10–30× more efficient than the FPGA generation.

## C · Enabling layers

**Chips.** Nvidia Space-1 / Rubin Space Module (25× H100 inference, late 2028); partners
Starcloud, Cowboy, Axiom, Kepler, Planet, Sophia — **no European name**
([[intel/raw/2026-03-17-theregister-nvidia-vera-rubin-space-1]]).

**Optical relay (the time-to-insight enabler).** Kepler: 10 × 300 kg relay sats launched
2026-02-09, **33 satellites launched in total** (cumulative, not a planned constellation size —
[[intel/raw/2026-01-11-kepler-first-tranche-optical-relay-satellites]]), HydRON prime (E1 $39M, E3 €18.6M —
[[intel/raw/2026-04-17-via-satellite-esa-hydron-element-3-kepler]]). Tesat SCOT80 100 Gbps,
62 in orbit ([[intel/raw/2025-10-27-via-satellite-tesat-scot80-lockheed-62-in-orbit]]).
Mynaric: equity wiped, now Rocket Lab ($155.3M, Apr 2026); government = 70–80% of
optical-comms revenue ([[intel/raw/2026-04-14-via-satellite-rocket-lab-closes-mynaric]]).
NTT/Space Compass: ¥23.5B JAXA grant for GEO optical relay
([[intel/raw/2026-04-22-space-compass-jaxa-optical-relay-fund]]). **IRIS² has no compute
angle** and FOC is 2030 ([[intel/raw/2026-02-05-eu-space-observer-what-is-iris2]]).

**Buses.** Muon Space ($250M C @ $1.5B; Condor compute platform; 500 sats/yr by 2027 —
[[intel/raw/2026-08-20-viasatellite-muon-space-250m-series-c]]); Open Cosmos (€300M, Sep
2026; built Φsat-2 and CogniSAT-6 — [[intel/raw/2026-09-14-europeanspaceflight-open-cosmos-300m]]);
Reflex Aerospace; Planet (Owl bus for Suncatcher).

**Programmes (ESA / EU).**

| Programme | Money | Dates | Angle |
|---|---|---|---|
| ESA Space Cloud (Edge Aerospace study) | undisclosed | awarded May 2026 | orbital DC architecture + commercial roadmap |
| EOCognitiveLab (Φsat evolution + 3CS4EO) | not published | info day 2026-09-29 | 2-sat **open federated constellation**, onboard compute, open ISL — [[intel/raw/2026-09-29-esa-indico-eocognitivelab-info-day]] |
| InCubed (Φ-lab) | €0.3–4M/project, **80% SME co-funding**; €130M to date | rolling | funds AI-eXpress, Ubotica — [[intel/raw/2026-06-16-innovationnewsnetwork-incubed-7-26m-call]] |
| ARTES 4.0 "ASCEND" (EDGX) | undisclosed | 2026–28 | ≥ 100/250 TOPS DPUs |
| HydRON | E1 $39M, E3 €18.6M | 2024–26 awards | Tbps multi-orbit optical |
| Horizon Europe ASCEND (Thales) | undisclosed | 1 GW by 2050 | GW sovereign cloud |
| US: New Horizon Act / DIU pilot | $220M FY27 | 2026 bill | orbital DC pilot — [[intel/raw/2026-06-12-airandspaceforces-new-horizon-act-orbital-dc]] |
| National: BIFROST (DK/SE) | DALO + FMV | launched 2025-06-23 | onboard AI Arctic ISR — [[intel/raw/2025-06-23-spacenews-space-inventor-bifrost-arctic]] |

Naming clash: Horizon-Europe ASCEND (Thales, GW cloud) ≠ ESA ARTES ASCEND (EDGX DPUs).

## Funding benchmarks (opened sources)

| Stage | Examples |
|---|---|
| Seed | Satlyt $8M · Sophia $10M + $3.5M · Lonestar $6.6M |
| Series A | Ubotica $11M · Starcloud $170M (@ $1.1B) |
| Series B/C | Cowboy $275M (@ $2B) · Starcloud $250M ext (@ $2.3B) · Muon $250M (@ $1.5B) · D-Orbit €150M · Open Cosmos €300M |
| Sector | > $3B invested by Apr 2026, > 35 companies (ABI); Morgan Stanley counts 43 in the supply chain |

A European kW-class EO node would raise against Ubotica/Satlyt-sized rounds ($8–11M), not
Starcloud's.

## Where the gap is

1. **Europe is present as hardware supplier and as a 2050 programme, absent as a kW-class
   operator.** Nvidia's partner slide has no European name; the only flying commercial
   ODC is US/Canadian (Axiom/Kepler); ESA is opening the slot (Space Cloud, EOCognitiveLab,
   InCubed) and small players (Edge Aerospace, Planetek) are a year ahead.
2. **Direct competitors for the Entrant's stated product are Satlyt (software layer, flying) and
   Ubotica (EO models, funded).** Differentiation has to be EO-specific models, a European
   sovereign anchor customer, dedicated compute with a measured duty cycle, or relay
   integration (HydRON/Kepler) for pass-gap coverage.
3. **Two ESA-adjacent European actors hold opposite theses** — Edge Aerospace (downlink
   relief; only SpaceX can do training) vs Thales ASCEND (1 GW general cloud). The market
   has not picked; the evidence base ([[intel/wiki/orbital-compute-launch-economics]]) favours
   the first.

## Open items
- [ ] ODC Orbital Data Center GmbH (Neubiberg, HRB 293209) — registry entry only; product?
- [ ] Kepler ODC compute hardware ("40 Jetson Orin") — third-party snippets only
- [ ] EUMETSAT position on onboard processing — nothing found
- [ ] Aviation Week "$250M rounds" — second company is Muon Space (bus maker), a category stretch
- [ ] 2026-10-05: Cowboy's reported 20,000-sat "Stampede" FCC filing is not among the four
  data-centre systems the FCC lists as accepted for review — filed elsewhere, pending, or
  misreported? ([[intel/raw/2026-10-01-wilmerhale-orbital-data-centers-legal-reality]])
- [ ] 2026-10-05: corrected Kepler "33 planned" → 33 launched in total; a Kepler release of
  2026-10-05 still gives 33 (no new tranche since Feb) — not captured, every URL for it names
  an individual
