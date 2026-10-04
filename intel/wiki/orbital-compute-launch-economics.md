---
type: concept
tags: [sdc, intel/wiki, space/orbital-compute, space/launch, economics/cost-model, market/sizing]
updated: 2026-10-04
sources: 113 raw captures, 2026-10-04 market search — see [[intel/raw/_index]]
---
# Orbital compute — launch economics and the cost gap

**Claim under test:** orbital data centres become cost-competitive with terrestrial ones
when launch reaches ~$200/kg. Every optimist case (Google, SpaceX, Starcloud) rests on that
number; every sceptic case shows how far away it is. The binding constraint is **launch
cadence and tonnage**, not physics — and today's demonstrated reality is two orders of
magnitude short.

Physical constraints (mass per kW, radiators, radiation, thermal) are in
[[intel/wiki/orbital-compute-physical-constraints]]; who is building what is in
[[intel/wiki/orbital-data-center-landscape]].

## 1 · Launch cost: Wright's law, not a calendar

Google fits SpaceX pricing to a learning curve in **cumulative launched mass** $M$:

$$
P(M) = P_0 \left(\frac{M}{M_0}\right)^{-b}, \qquad b = -\log_2(1-\lambda) = -\log_2 0.8 \approx 0.322
$$

with $\lambda \approx 20\%$ per **doubling of $M$**. Price falls only as fast as mass flown
accumulates. (TechCrunch's "20% a year" is a mis-paraphrase —
[[intel/raw/2026-10-01-techcrunch-google-suncatcher-1800-starship-launches]].)

**Derived — doublings to reach $200/kg**, $n = \log(P_0/200)/\log(1.25)$:

| Starting price $P_0$ ($/kg) | Doublings $n$ | Cumulative-mass multiplier $2^n$ |
|---:|---:|---:|
| 600 | 4.9 | ×30 |
| 1,500 | 9.0 | ×523 |
| 2,500 | 11.3 | ×2,555 |

Google's own primary ([[intel/raw/2025-11-22-arxiv-google-suncatcher-system-design]],
[[intel/raw/2025-11-04-google-research-suncatcher-system-design]]): < $200/kg by ~2035 at
~180 Starship flights/yr; with 70% fewer launches still ≈ $300/kg; Starship-4 bottom-up
cost ≲ $60/kg at 10× reuse. Press: 370,000 t ≈ **1,800 launches / 180 per yr at 200 t**.

## 2 · Cadence reality vs. the model

| | Assumed by the $200/kg case | Demonstrated (2026-10-04) | Gap |
|---|---|---|---|
| Starship flights/yr | 180 | 5 (2025), 3 YTD 2026 → ~4/yr | **36–45×** |
| Payload per flight | 200 t | ~44 t (F14, 2026-09-28, first orbital deployment) | **4.5×** |
| Tonnage/yr | ~37,000 t | ~115 t (2026 YTD) | **~320×** |
| Success rate | — | 5 of 8 flights nominal 2025–26 (62%) | — |

Sources: [[intel/raw/2026-09-28-wikipedia-starship-launch-list-cadence]],
[[intel/raw/2026-09-29-gizmodo-starship-orbital-hard-part]] (Raptor 3 failed on all three
Block-3 flights; Musk: "2–3 years from hourly flights"). SpaceX's FCC plan for 1M compute
satellites assumes **1 Mt/yr** → derived ≈ 5,000 Starship flights/yr
([[intel/raw/2026-02-02-via-satellite-spacex-xai-fcc-million-satellites]]). Alternatives:
New Glenn pad out > 1 yr after the May 2026 static-fire explosion; Neutron NET Q4 2026 at
~$3,850/kg ([[intel/raw/2026-10-04-wikipedia-new-glenn-neutron-status]]).

**Small-payload prices are rising, not falling:** Transporter SSO rideshare $5,000/kg (2019)
→ **$7,000/kg (2026)**, +40% in 7 years
([[intel/raw/2026-02-27-newspaceeconomy-rideshare-pricing-2026]]). A kW-class operator buys
at this price, not at Google's curve.

## 3 · Launched power price — and why the comparisons disagree

$$
C_{\text{kW·yr}} = \frac{\alpha \cdot P_{\text{launch}}}{L}
$$

($\alpha$ = specific mass kg/kW, $L$ = life, yr). Google: **$810/kW·yr at $200/kg** vs
terrestrial power opex $570–3,000/kW·yr; **$14,700/kW·yr at today's Falcon 9 price**
([[intel/raw/2026-02-11-techcrunch-economics-of-orbital-ai-brutal]]).

The optimist/sceptic split is a **boundary** choice, not arithmetic
([[intel/raw/2026-04-29-arxiv-turyshev-odc-economic-viability]]):

- Google compares *launch-only* cost against terrestrial *power opex*, sizing with a comms
  bus ($\alpha \approx 20$ kg/kW) that never radiated 28 kW of compute heat.
- Turyshev (JPL) compares *launch + build capital* against terrestrial *facility capital*
  (10–40 k$/kW): at $\alpha \approx 40$ kg/kW that leaves **$250–1,000/kg for launch and
  spacecraft together**, 3.4–13.5× below Falcon 9's $3,360/kg.
- *Derived reconciliation:* at $200/kg and 40 kg/kW, launch alone is $8,000/kW — Google's
  target closes only with a near-free bus or against the 40 k$/kW high benchmark.

### Cost-closure estimates, 2026

| Source | Space vs terrestrial | Parity when |
|---|---|---|
| BCG ([[intel/raw/2026-08-27-bcg-space-based-data-centers-cost-outlook]]) | 20-yr TCO $660–750M/MW vs $230–300M/MW = **2.5–3×** now; 1.6–1.8× in 5–10 yr | "unlikely this decade"; target $100/kg |
| ABI ([[intel/raw/2026-05-11-abi-research-data-centers-in-space-qa]], [[intel/raw/2026-06-11-ieee-spectrum-thermodynamics-orbital-data-centers]]) | up to **78×** TCO; ≥ 10× even at $44/kg | not before 2035 |
| McCalip calculator ([[intel/raw/2026-02-11-techcrunch-economics-of-orbital-ai-brutal]]) | 1 GW ≈ $42B ≈ **3×** ground | — |
| Turyshev O&M ([[intel/raw/2026-08-27-arxiv-turyshev-odc-operations-maintenance]]) | servicing logistics **5.3–9 t/(MW·yr)** ≈ 11%/yr of mass → derived +$1,320/kW·yr at $200/kg | — |
| Google's Beals ([[intel/raw/2026-10-01-npr-google-suncatcher-launch-sceptics]]) | — | "not cheaper in the next five years" |
| Morgan Stanley ([[intel/raw/2026-09-15-kucoin-morgan-stanley-spacex-orbital-compute]], low-tier relay) | $1,080/kg (2026) → $836/kg (2028) | "orbital primary capacity by 2032" |
| Musk ([[intel/raw/2026-06-10-lightreading-musk-spacex-orbital-ai-plan]]) | — | "2–3 years"; SpaceX S-1: "may not achieve commercial viability" ([[intel/raw/2026-04-22-tnw-spacex-ipo-orbital-dc-risk-disclosure]]) |
| Bezos ([[intel/raw/2025-10-03-toms-hardware-bezos-gigawatt-space-data-centers]]) | — | "10+ years, not more than 20" |

**Timeline-to-parity spread: 2–3 years (Musk) → never this decade (BCG) → 2035 (ABI, Google
paper) → 2040s (Bezos).** Only one party in that list has put the pessimistic version in a
securities filing.

## 4 · The one price that exists

Atomic-6's marketplace: **$3.5M/month for a 100 kW sovereign 42U rack** → derived
$35,000/kW·month = **$420,000/kW·yr ≈ 100–200× terrestrial colocation** ($150–300/kW·month)
([[intel/raw/2026-04-13-payload-atomic-6-odc-space-marketplace]]). The only operational
commercial product is kW-class: Axiom's two ODC nodes on Kepler satellites, launched
2026-01-11 ([[intel/raw/2025-04-07-axiomspace-odc-nodes-press-release]]).

## 5 · Starcloud's walk-back — the cheap-power case is gone

| | 2024 white paper | March 2026 pitch | Factor |
|---|---|---|---|
| Launch | $30/kg | $500/kg | 17× |
| Energy | $0.002/kWh ("22× cheaper") | $0.05/kWh (≈ EU wholesale) | 25× |

([[intel/raw/2024-09-01-starcloud-whitepaper-why-train-ai-in-space]],
[[intel/raw/2026-03-30-techcrunch-starcloud-170m-series-a]]). What remains of the thesis is
**siting and latency** — the argument a space-native workload makes, not a cheaper-cloud
argument. Starcloud and Cowboy both name **launch capacity 2028–29**, not money or chips,
as the binding constraint ([[intel/raw/2026-08-21-techcrunch-starcloud-250m-series-a-extension]],
[[intel/raw/2026-05-11-techcrunch-cowboy-space-275m-series-b]]).

## 6 · Market sizing — figures are not comparable

| Source | 2026 | Horizon | Note |
|---|---|---|---|
| MarketsandMarkets ([[intel/raw/2026-08-26-marketsandmarkets-space-based-data-center-28b-2040]]) | $0.11B | $28.2B (2040) | stated 18.3% CAGR; endpoints imply **48.6%** — internally inconsistent |
| Three other vendors (snippets) | $1.44–1.9B | $3.8–8.4B (2034–35) | 15× spread on 2026 alone |
| BCG | — | 10–15% of AI DC market = **$240–320B/yr** (2040) | different definition (share of AI DC) |
| ABI | > $3B invested to Apr 2026 | 18,600 units, **1.5 GW** by 2035 → ~80 kW/unit | the unit size is the Entrant's class |
| BIS (via aggregator, unopened) | — | $1.77B (2029) → $39B (2035) | — |

Use ABI's *unit* figure and BCG's *share* logic; don't quote a dollar TAM without its
definition.

## 7 · What this means for the Entrant

- **Don't pitch $/kW.** At rideshare prices the launched-power price is ~$14,700/kW·yr
  against $570–3,000 on the ground. A kW-class EO node is valued on **insight latency and
  bytes not downlinked** ([[intel/wiki/eo-edge-compute-value-chain]]), where the price
  anchor is $420k/kW·yr (Atomic-6), not colocation.
- **Plan at $7,000/kg, not $200/kg.** The $200/kg curve needs 200 t × 180/yr; demonstrated
  is 44 t × 4/yr. Any plan that only closes at Google's curve is a 2035 plan.
- **The GW fight is not the Entrant's.** Every analyst (BCG, ABI, ITIF, JLL, MS, Turyshev)
  converges on ≤100 kW EO/space-native processing for defence/sovereign buyers, 2026–29, as
  the only near-term case.

## Watch list
- [ ] *Joule* publication of the Google paper (cell.com returned 403) — confirm 370,000 t
- [ ] Starship flights per year and tonnage — the leading indicator for the whole sector
- [ ] Transporter price list 2027 (rising or flat?)
- [ ] McKinsey "case for data centers in space" (503 on fetch) — $500/kg threshold unverified
