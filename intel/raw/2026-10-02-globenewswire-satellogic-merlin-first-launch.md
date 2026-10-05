---
type: intel
tags: [sdc, intel/raw, space/eo-edge, space/optical-isl, company/satellogic, market/competitors, market/defence]
source: GlobeNewswire (Satellogic Inc. press release)
url: https://www.globenewswire.com/news-release/2026/10/02/3373776/0/en/satellogic-announces-successful-launch-of-first-merlin-satellite.html
author: Satellogic Inc. (press release)
published: 2026-10-02
captured: 2026-10-05
primary: "Company release (primary for Satellogic's claims). The March 2026 Merlin introduction (globenewswire 2026-03-18) was seen only as a search result, not opened."
---
# Satellogic — first Merlin satellite launched: onboard AI alerts within 30 minutes, ISL cueing

## Reported (what the source says)
- **Merlin.01**, two **NewSat Mark VI** and one **NewSat Mark V** launched **2026-10-01** on a
  Falcon 9 from Vandenberg into SSO.
- Merlin: **10-band payload aligned with Sentinel**, **1 m-class** imagery, **170 km effective
  swath**, designed to **remap the Earth daily**.
- **Onboard AI processing designed to deliver alerts within 30 minutes**; **inter-satellite link**
  lets Merlin direct NewSat Mark VI satellites to take **50 cm follow-up** imagery **without
  routing through a ground station**.
- Status: LEOP; payload testing and commissioning from **mid-October 2026**; daily global remap /
  full operational capacity **H2 2027**.
- Market framing: governments that "need to see change across an entire theater, not just the
  sites they already monitor".
- No compute hardware, power, constellation size or price disclosed.

## Primary (what the underlying paper / filing says — where it differs)
- The release is the primary. "Within 30 minutes" is a **design target**, not a measured figure;
  the satellite has not finished commissioning.

## Derived (our arithmetic — formula shown)
- Against the measured ground-only benchmark (Vantor, 13 min tasking → portal,
  [[intel/raw/2026-04-07-spacenews-eo-operators-images-within-minutes]]): 30 / 13 ≈ **2.3× slower**
  — but a different product: Merlin *detects* change across a 170 km swath without being tasked,
  Vantor delivers a *tasked* image. The 30-minute figure is the first published **onboard-AI
  alert latency** from an EO operator, and it is a ceiling, not an orbit-average.

## Relevance to the Entrant
- **This is the Entrant's chain, built vertically by an EO operator**: collection → onboard AI →
  ISL cueing → high-res follow-up → alert. Satellogic sells its own data; it does not host third
  parties. The Entrant's room is operators who **cannot** build this themselves.
- The latency bar now has two public reference points: 13 min (tasked, ground-processed) and
  30 min (untasked, onboard-detected, design target). The Entrant needs a **measured**
  orbit-average to beat both.
- Defence/"theater" framing confirms the first buyer again.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]]
- [[intel/wiki/orbital-data-center-landscape]]
