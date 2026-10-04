---
type: intel
tags: [sdc, intel/raw, research/paper, space/eo-edge, space/thermal, space/power, space/radiation, space/software]
source: arXiv
url: https://arxiv.org/abs/2608.21034
author: Qing Li, Qiyang Zhang, … Mengwei Xu, Shangguang Wang, Xuanzhe Liu (BUPT & Peking University)
published: 2026-08-21
captured: 2026-10-04
primary: self
---
# AI Infrastructure in Space: How Far Can We Go?

## Reported (what the paper claims)
Vision paper + three **first-party in-orbit case studies** on BUPT-1 (12U, SSO ~490 km) and BUPT-2.

**Case I — the node (BUPT-1, ~4 months of telemetry).** Payload: 2× Raspberry Pi 4B + 2× Huawei Atlas 200 DK.
- Thermal ceiling: shared aluminium surface limited to **30 °C**. One accelerator at full load reaches it in
  **~9 h**; two co-located accelerators hit 30 °C in **~40 min**, OS kills the first task at ~50 min, platform
  powers the second off at **~110 min**. "Co-location collapses the safe window from nine hours to under two."
- Energy: ~6 % of converted solar goes unused in sunlight. Depth-of-discharge normally ≈ 16 %/day; multi-day
  continuous compute drives it to **≈ 35 %**, past the **30 % design limit**; raising mean DoD 25→30 % costs
  "on the order of a quarter of battery lifetime".
- **Radiation: zero observed SEE errors** in months of unhardened COTS operation at ~490 km; "thermal and
  energy bind before radiation". Thermal throttling adds ~10 % inference latency on some models.

**Case II — the platform (SateLight on BUPT-2).** Uplink **tens–hundreds of kbps**, **4–6 ten-minute
contacts/day**. A full vision container ≈ **10.7 h of pure uplink at 200 kbps ≈ two weeks of wall-clock**;
a content-aware delta for a 10 % code change is tens of kB and ships in seconds. Transmission latency
−56.54 % average, −91.18 % max vs best baseline; ~2 s onboard reconstruction; rollback 0.48 ms prep /
~36 s recovery; 100 % correctness over 10 apps in 6 languages.

**Case III — the service (Rover runtime).** Sustained **Qwen3-VL-2B** inference heats the device from 45 °C
to the **55 °C shutdown threshold in 48 s**, while a video-level EO request needs minutes. Checkpointing of
ViT hidden states / KV frontier / batched decode gives **3.2× end-to-end speedup**, −85.6 % recovery
latency, 3.56× fewer SSD writes, 3.7–10.4 % normal-path energy overhead; "Rover completes most requests
while the baseline completes none".

**Survey content relevant here.** Φ-Sat-1 filtered cloudy hyperspectral images before downlink (cited, no
number); CloudScout, OPS-SAT, HYPSO-1 sea-land-cloud segmentation listed as EO-edge heritage. Evaluation
should be "per-orbit useful work, energy and thermal margins, contact usage, recovery behaviour".

## Primary (method / assumptions a sceptic would attack)
- Single 12U platform with a 30 °C *structural* limit — the thermal numbers describe a CubeSat radiator
  budget, not a purpose-built compute satellite. They are a floor on what happens without thermal design,
  not a ceiling on what is possible.
- Atlas 200 DK / RPi class compute (tens of W); nothing here is GPU-class.
- "Zero SEE" is anecdotal: no error-detection instrumentation is described, so silent corruption would be
  invisible (compare [[intel/raw/2026-09-04-arxiv-tensil-proton-irradiation]]).
- Case III speedups are from traces replayed on ground hardware plus one real deployment trace.

## Derived (our arithmetic — formula shown)
- Duty-cycle ceiling for co-located accelerators ≈ 110 min on / cooldown ⇒ a few compute windows per day
  on a shared radiator; i.e. **compute availability ≪ 100 %** even when power is fine.
- Uplink arithmetic check: 200 kbps × 10.7 h × 3600 = 7.7 Gbit ≈ **0.96 GB container**. At 5 contacts ×
  10 min = 50 min/day → 10.7 h / 0.83 h/day ≈ **13 days** ✓ ("two weeks").
- Model-weight refresh at kbps: a 2 B-param INT8 VLM (~2 GB) ≈ 22 h uplink ≈ a month of contacts. Weight
  updates in orbit need a feeder link, not TT&C.

## Relevance to the Entrant
- **The most grounded published evidence that the binding constraints for small-sat edge AI are thermal
  and battery DoD, not radiation.** the Entrant's design reviews should budget radiator area and DoD before
  rad-tolerance.
- Every in-orbit AI service needs delivery/update/rollback sized to kbps uplinks; SateLight is a reference
  design the Entrant could adopt or benchmark against.
- "Time-to-insight" claims must account for payload power-cycling: a 2 B VLM that trips thermal shutdown
  in 48 s cannot deliver minutes-scale reasoning without checkpoint/resume.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]] (thermal/DoD envelope of COTS edge compute; update-path economics)
- [[intel/wiki/orbital-compute-launch-economics]] (thermal binds before radiation at LEO)
