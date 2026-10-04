---
type: intel
tags: [sdc, intel/raw, market/incumbents, market/sceptics, space/orbital-compute]
source: The Next Web
url: https://thenextweb.com/news/spacex-orbital-data-centres-ipo-risk-disclosure
author: Alina Maria Stan
published: 2026-04-22
captured: 2026-10-04
primary: "SpaceX S-1 (confidential draft as reported; final IPO 2026-06-12). Context from Wikipedia 'Initial public offering of SpaceX' (living page, read 2026-10-04): https://en.wikipedia.org/wiki/Initial_public_offering_of_SpaceX"
---
# TNW — "SpaceX's IPO filing says its orbital data centres may never work"

## Reported (what the source says)
- S-1 risk language: orbital data-centre plans "involve significant technical complexity and unproven technologies, and may not achieve commercial viability"; infrastructure could malfunction in "the harsh and unpredictable environment of space."
- IPO target at the time: **$1.75T** valuation, **$75B** raise.
- FCC filing: up to **1M** satellites at **500–2,000 km**; ~**10,000** satellites in LEO today → **100-fold** increase.
- Deployment cost **≥ $1 trillion** (citing Ars Technica).
- Thermal: **~1,200 m² of radiator per MW**; GPU obsolescence requires in-orbit replacement missions.
- Contradiction: three months earlier at Davos, Musk said space would be the lowest-cost AI location in "two years, maybe three at the latest", "a no-brainer", and orbital capacity would surpass Earth's within five years.

## Primary (where the underlying document differs or adds)
- Wikipedia IPO page: IPO priced **2026-06-12** at **$1.77T**, raised **$86B** (ticker SPCX). 2025 revenue **$18.7B**, net loss **$4.94B**; xAI segment revenue $3.2B with a $3.2B loss. Prospectus cites compute contracts with Anthropic ($1.25B/month) and Google ($920M/month), each with 90-day termination clauses. Morgan Stanley forecast $330B revenue by 2030 and $3.4T by 2040. Stock peaked at $211 and fell ~50% by late July 2026.

## Derived (our arithmetic — formula shown)
- Radiator-per-MW spread: TNW 1,200 m²/MW vs Spectrum 2,000 vs Turyshev 2,500 → factor **~2×**, driven by assumed radiator temperature (T⁴).
- $1T ÷ 1M satellites = **$1M per satellite** all-in, vs ~$1,000/kg × ~1 t ≈ $1M build — i.e. the Ars estimate is essentially build cost with launch at Starship-target prices.

## Relevance to the Entrant
- The legally-binding version of SpaceX's view (the S-1) says "may not achieve commercial viability." the Entrant's pitch should quote the filing, not the keynote.
- The anchor compute customers (Anthropic, Google) are terrestrial xAI/Colossus capacity, not orbital — SpaceX's orbital compute revenue today is **zero**.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
