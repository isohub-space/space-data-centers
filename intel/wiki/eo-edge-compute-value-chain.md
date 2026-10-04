---
type: concept
tags: [sdc, intel/wiki, space/eo-edge, space/optical-isl, market/europe, market/defence]
updated: 2026-10-04
sources: Europe + literature lanes, 2026-10-04 — see [[intel/raw/_index]]
---
# EO edge compute — the time-to-insight value chain

The Entrant's hypothesis ([[scenario/entrant]]): the end-to-end Earth-observation chain with
processing *inside* it — collection → optical links → in-orbit compute → insight delivery —
measured by **time-to-insight**. This note is what the evidence says about that chain: where
the bottleneck is, who pays, what works, and the bar an in-orbit service has to beat.

## 1 · The bottleneck is real, and it is per satellite

| Satellite | Downlink | Per pass | Source |
|---|---|---|---|
| Planet Dove | 160 Mbps | ~12 GB | [[intel/raw/2025-05-01-arxiv-fool-downlink-bottleneck-satellite-computing]] |
| WorldView-3 | 1,200 Mbps | 90 GB | same |
| Sentinel-3 | 560 Mbps | 40 GB | same |
| KP Labs Intuition-1 (192-band HSI) | **3–50 Mbps X-band** | — | [[intel/raw/2025-08-24-satnews-kp-labs-intuition-1-leopard-dpu]] |

Passes last 120–600 s. Uplink for model updates is tens–hundreds of kbps: a 1 GB container
takes ~10.7 h of contact ≈ two weeks → weights must be delta-shipped
([[intel/raw/2026-03-14-arxiv-kth-fpga-onboard-inference]]). The "70,000 satellites data
trap" framing ([[intel/raw/2026-02-12-satnews-70000-satellites-data-trap]]) is the industry
version of the same number.

## 2 · The latency bar is ~13 minutes — without any compute in orbit

- **Vantor** (ex-Maxar): WorldView Legion 30 cm image on the customer portal **13 minutes**
  after tasking (Jan 2026), raw downlink + ground processing
  ([[intel/raw/2026-04-07-spacenews-eo-operators-images-within-minutes]]).
- **ICEYE Tactical Access**: "minutes" with a customer ground station and a *ground-side*
  edge processor, hours via cloud ([[intel/raw/2025-10-30-prnewswire-iceye-tactical-access]]).
- Ubotica, Satellogic, Little Place Labs, Planet all claim "minutes" — **every claim assumes
  a link is in view. No source publishes a measured orbit-average latency for in-orbit
  processing.**

So in-orbit processing earns its mass only by (a) delivering **well under ~10 min
orbit-average**, (b) covering the **pass gaps** where no station is in view (via optical
ISL to a relay — Constella's "communicator satellite" pattern cuts mean time-to-ground
4,129 s → 1,541 s, energy 3,184 → 43 Wh, [[intel/raw/2026-06-08-arxiv-constella]]), or (c)
serving operators without Vantor-class ground networks.

## 3 · Who pays for latency

| Buyer | Evidence |
|---|---|
| **Defence / ISR** first | Government = 70–80% of optical-comms revenue (Mynaric); CSET frames onboard compute as survivability/autonomy ([[intel/raw/2025-06-01-cset-ai-on-the-edge-of-space]]); Denmark's DALO + Sweden's FMV bought onboard-AI Arctic event reporting (BIFROST, [[intel/raw/2025-06-23-spacenews-space-inventor-bifrost-arctic]]); Satlyt's customers are NASA + SDA; US New Horizon Act $220M pilot |
| **Maritime** | Ubotica's $11M Series A is for maritime intelligence; BIFROST is Arctic maritime |
| **Civil protection** | IRIDE HEO's case is burnt-area mapping ([[intel/raw/2026-04-08-arxiv-iride-heo-onboard-processing-added-value]]); Constella's is wildfire |
| **Insurance / commodities / energy** | Little Place Labs 2026 targets ([[intel/raw/2025-12-31-littleplace-q4-2025-newsletter-orbitfy]]); Eni is an AI-eXpress tenant |

For a Nordic-rooted entrant, the defence buyers who already funded BIFROST are the closest
anchor. EUMETSAT's own position on onboard processing was **not found**.

## 4 · What onboard processing actually saves — a taxonomy

The quoted "downlink reduction" spans 21% to 10⁵× because sources measure different things:

| Mode | Reduction | Source | Caveat |
|---|---|---|---|
| **Send a decision** (cloud polygons, alerts) | 99.7–99.99% (Sentinel-2 SCL: 31.46 MB → 0.001–0.098 MB) | [[intel/raw/2026-03-19-arxiv-which-workloads-belong-in-orbit]] | the pixels never arrive |
| **Send meaning, then pixels** (onboard VLM text 485 B vs 50 MB image) | 200× preview, 10⁵× full | [[intel/raw/2026-08-07-arxiv-summarize-first-onboard-vlm]] | 60–74% VQA accuracy; 29–107 s per image, load-dominated |
| **Semantic packets** (toy CIFAR-10) | > 98% | [[intel/raw/2026-05-12-arxiv-communication-efficient-space-data-centers]] | not EO |
| **Drop cloudy frames** (Φ-Sat-1 pattern) | "reduced volume" — **no primary number in any of six papers citing it** | [[intel/raw/2026-09-11-arxiv-aquacubeai-phisat2]] | **deletes 5–29% of clear pixels** (false positives) on expert labels |
| **Deliver the pixels, smarter** (clear-weighted learned codec) | **39–48% fewer bytes** at equal clear-region quality; deadline-full delivery 38 → 83.5% | [[intel/raw/2026-08-02-arxiv-clear-weighted-bit-allocation]] | 19.9 ms / 103 mJ per 256² crop on Orin Nano |
| **Task-agnostic feature compression** (FOOL) | ~100× effective downlink at 15 W | [[intel/raw/2025-05-01-arxiv-fool-downlink-bottleneck-satellite-computing]] | downstream tasks must accept features |
| Satlyt, Gemma onboard (commercial, measured) | > 60% | [[intel/raw/2026-10-01-techcrunch-satlyt-8m-seed]] | the one commercial KPI published |

**Don't quote a "send a decision" ratio as an image-downlink saving.** The honest range when
customers still want pixels is 40–60%; the heritage "AI cloud filter" story destroys
sellable data.

## 5 · What binds on the hardware — thermal, then integrity, then radiation

- **Thermal first.** BUPT-1 (490 km, COTS): one accelerator hits its 30 °C structural limit
  in ~9 h, two in ~40 min; a 2B VLM reaches 55 °C shutdown in **48 s**; continuous compute
  overruns battery DoD ([[intel/raw/2026-08-21-arxiv-bupt-ai-infrastructure-in-space]]). Model
  choice is a thermal decision.
- **Silent corruption second.** Unmitigated COTS inference returned a wrong class for 39
  consecutive inferences with every watchdog green
  ([[intel/raw/2026-09-04-arxiv-tensil-proton-irradiation]]); mitigation is output checking
  and periodic weight reload. Detail in [[intel/wiki/orbital-compute-physical-constraints]].
- **Radiation third** at ~500 km (zero observable SEE in months on BUPT-1).
- **Compute envelope.** Φsat-2's Myriad 2: 8.5 ms per 20×20×8-band patch, 216 s per 4,096²
  scene — the institutional baseline a GPU-class node differentiates against. Rad-tolerant
  FPGA: 606 FPS at 5.75 W (9.5 mJ/inference) but ~2 orders below Jetson TOPS/W. Jetson
  Xavier NX flew on Chaohu-1 SAR (2022,
  [[intel/raw/2024-07-16-arxiv-rednet-application-aware-radiation]]). Next generation: EDGX
  Sterna ≥ 100 TOPS (Q2 2026), Morus ≥ 250 TOPS (2027), ESA-funded.
- **Image quality.** Infer on raw (skip onboard restoration) is fine; doubling GSD 100 → 200
  cm costs 4–8 AP50 points ([[intel/raw/2026-09-29-arxiv-cnes-raw-imagery-onboard-ai]]).

## 6 · Economics of the kW-class node

- The hardware-box business in Europe is **~€6M/yr and loss-making** (Unibap: SEK 17.3M
  per quarter, −SEK 13M operating result, ~100 units/yr capacity —
  [[intel/raw/2025-11-05-investing-unibap-q3-2025-earnings]]). Value sits in the **service
  layer**: orchestration, relay integration, model updates, multi-tenancy.
- The one price in the market is **$420k/kW·yr** (Atomic-6, 100 kW rack) — see
  [[intel/wiki/orbital-compute-launch-economics#4 · The one price that exists]].
- Launch at **$7,000/kg** rideshare: a 50 kg node = $350k; a 150 kg node ≈ $1M.
- Turyshev names "C1 space-native processing that reduces space-to-ground data" as *the*
  credible early regime; the inference traffic of a 2 MW cluster is only ~0.02 Tb/s (≈ 10
  bit/s per W) — outputs are tiny, inputs are not.

## 7 · Competitors in this exact segment

| | Flying? | Edge | Weakness vs the Entrant |
|---|---|---|---|
| **Satlyt** (US) | yes, 3 missions | software layer, hardware-agnostic, NASA/SDA customers, > 60% measured | US-only; no European sovereign anchor |
| **Ubotica** (IE) | yes | Φsat-1 heritage, > 30 EO models, $11M | maritime focus; Myriad-class compute |
| **Axiom + Kepler** | yes, operational | relay-integrated, SDA optical, Red Hat | general PED, not EO-specific |
| **Planetek AI-eXpress** (IT) | yes, 3 sats | multi-tenant, InCubed-funded, Eni/IBM tenants | FPGA-class compute |
| **Edge Aerospace** (LU) | demo | ESA Space Cloud study | architecture, not EO service |

## 8 · What this means for the Entrant

1. **Publish two measured numbers nobody else has:** orbit-average time-to-insight
   (tasking → alert, including pass gaps) and sustained compute at temperature (W
   continuous / duty cycle). The market's "minutes" claims are all link-conditional.
2. **Pitch bytes-not-downlinked honestly at 40–60%**, plus pass-gap coverage via relay (Kepler
   /HydRON/Tesat), not "99%" decision-only ratios.
3. **Anchor on a Nordic defence or civil-protection buyer** (BIFROST precedent, DALO/FMV);
   apply to InCubed (€0.3–4M, 80%) and EOCognitiveLab's open-constellation slots.
4. **Differentiate on integrity**: output-checked inference, weight reload, measured
   SDC rate — a credible engineering story against "we flew a Jetson".
5. **Don't build the box.** Buy EDGX/Unibap-class compute; own the service layer and the
   relay integration.

## Open questions
- [ ] EUMETSAT's position on onboard processing (nothing found)
- [ ] Φ-Sat-1 primary downlink-saving figure (Giuffrida 2022, TGRS — not opened)
- [ ] Measured orbit-average latency for *any* in-orbit processing service
- [ ] Kepler ODC node compute hardware (unverified)
