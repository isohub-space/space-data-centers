---
type: concept
tags: [sdc, intel/wiki, indicators, timeseries]
updated: 2026-10-05
---
# Indicators — dated observations

The handful of numbers that move the positioning question, kept as **dated observations**
so the dashboard can draw them over time. One row per observation; rows are **appended,
never edited** (a corrected value is a new row with a note). The weekly sweep adds a row
whenever a new source gives a new value for an indicator.

Columns: `Indicator` is a stable id (lowercase, hyphens); `Date` is `YYYY`, `YYYY-MM` or
`YYYY-MM-DD` (when the value applied, not when it was captured); `Value` is a plain number in
`Unit`; `Kind` is `reported`, `primary` or `derived`; `Source` links the capture.

Why these: launch price and cadence decide whether any orbital-compute plan closes
([[intel/wiki/orbital-compute-launch-economics]]); payload per flight is the other half of
the $/kg curve; valuations and cumulative funding show how much capital the GW-scale thesis
is absorbing ([[intel/wiki/orbital-data-center-landscape]]). Published EO insight latency
(added 2026-10-05) is the bar the Entrant's time-to-insight claim has to beat
([[intel/wiki/eo-edge-compute-value-chain]]); the Note says whether a value is measured or a
target.

## Observations

| Indicator | Unit | Date | Value | Kind | Note | Source |
|---|---|---|---|---|---|---|
| rideshare-price-sso | USD/kg | 2019 | 5000 | reported | approx.; 150 kg minimum at launch of programme | [[intel/raw/2026-02-27-newspaceeconomy-rideshare-pricing-2026]] |
| rideshare-price-sso | USD/kg | 2022-10 | 5500 | reported | $275k per 50 kg | [[intel/raw/2026-02-27-newspaceeconomy-rideshare-pricing-2026]] |
| rideshare-price-sso | USD/kg | 2024 | 6000 | reported | $300k per 50 kg (2024 to early 2025) | [[intel/raw/2026-02-27-newspaceeconomy-rideshare-pricing-2026]] |
| rideshare-price-sso | USD/kg | 2025 | 6500 | reported | $325k per 50 kg (mid/late 2025) | [[intel/raw/2026-02-27-newspaceeconomy-rideshare-pricing-2026]] |
| rideshare-price-sso | USD/kg | 2026 | 7000 | reported | $350k per 50 kg from Transporter-16 | [[intel/raw/2026-02-27-newspaceeconomy-rideshare-pricing-2026]] |
| starship-payload-per-flight | t | 2025-01-16 | 20 | reported | F7, simulators, ship lost | [[intel/raw/2026-09-28-wikipedia-starship-launch-list-cadence]] |
| starship-payload-per-flight | t | 2025-03-06 | 8 | reported | F8, simulators, ship lost | [[intel/raw/2026-09-28-wikipedia-starship-launch-list-cadence]] |
| starship-payload-per-flight | t | 2025-05-27 | 16 | reported | F9, simulators, booster and ship lost | [[intel/raw/2026-09-28-wikipedia-starship-launch-list-cadence]] |
| starship-payload-per-flight | t | 2025-08-26 | 16 | reported | F10, simulators | [[intel/raw/2026-09-28-wikipedia-starship-launch-list-cadence]] |
| starship-payload-per-flight | t | 2025-10-13 | 16 | reported | F11, simulators | [[intel/raw/2026-09-28-wikipedia-starship-launch-list-cadence]] |
| starship-payload-per-flight | t | 2026-05-22 | 37.5 | reported | F12, first Block 3 | [[intel/raw/2026-09-28-wikipedia-starship-launch-list-cadence]] |
| starship-payload-per-flight | t | 2026-07-24 | 34 | reported | F13, 20 Starlink V3 | [[intel/raw/2026-09-28-wikipedia-starship-launch-list-cadence]] |
| starship-payload-per-flight | t | 2026-09-28 | 44 | reported | F14, first orbital deployment | [[intel/raw/2026-09-28-wikipedia-starship-launch-list-cadence]] |
| starship-flights-per-year | flights | 2025 | 5 | derived | count of 2025 flights in the launch list | [[intel/raw/2026-09-28-wikipedia-starship-launch-list-cadence]] |
| starship-flights-per-year | flights | 2026 | 3 | derived | year to date as of 2026-09-28 | [[intel/raw/2026-09-28-wikipedia-starship-launch-list-cadence]] |
| odc-startup-valuation-max | USD bn | 2026-03-30 | 1.1 | reported | highest post-money among ODC startups (Starcloud Series A) | [[intel/raw/2026-03-30-techcrunch-starcloud-170m-series-a]] |
| odc-startup-valuation-max | USD bn | 2026-08-21 | 2.3 | reported | Starcloud Series A extension | [[intel/raw/2026-08-21-techcrunch-starcloud-250m-series-a-extension]] |
| odc-sector-funding-cumulative | USD bn | 2026-04 | 3 | reported | lower bound (">$3B"), ABI | [[intel/raw/2026-05-11-abi-research-data-centers-in-space-qa]] |
| eo-insight-latency-published | min | 2026-01 | 13 | reported | Vantor WorldView Legion, tasking → portal, ground-processed, measured once | [[intel/raw/2026-04-07-spacenews-eo-operators-images-within-minutes]] |
| eo-insight-latency-published | min | 2026-10-01 | 30 | reported | Satellogic Merlin onboard-AI alert, design target before commissioning (untasked detection) | [[intel/raw/2026-10-02-globenewswire-satellogic-merlin-first-launch]] |

## Watch list
- [ ] Starship flights and payload per flight — append a row per flight
- [ ] Rideshare price list for 2027
- [ ] Next priced round of any orbital-compute startup (valuation, cumulative funding)
- [ ] Measured EO insight latency (Satellogic Merlin after commissioning; any onboard service)
