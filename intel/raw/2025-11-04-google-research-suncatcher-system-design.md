---
type: intel
tags: [sdc, intel/raw, market/incumbents, space/launch, space/orbital-compute]
source: Google Research blog
url: https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/
author: Travis Beals, Blaise Agüera y Arcas, Maria Biggs, Jessica V. Bloom, Thomas Fischbacher, Konstantin Gromov, Urs Köster, Rishiraj Pravahan, James Manyika (Google)
published: 2025-11-04
captured: 2026-10-04
primary: "arXiv:2511.19468 'Towards a future space-based, highly scalable AI infrastructure system design' (preprint); peer-reviewed version in Joule (Oct 2026, page not accessible)"
---
# Google Research — "Exploring a space-based, scalable AI infrastructure system design" (Project Suncatcher announcement)

## Reported (what the source says)
- Solar panels in the chosen dawn-dusk sun-synchronous orbit are "up to **8x** more productive" than on Earth (near-continuous sunlight).
- Modelled cluster: **81 satellites**, **1 km** cluster radius, **650 km** altitude, satellites **~100–200 m** apart.
- Inter-satellite optical link bench demo: **800 Gbps each way, 1.6 Tbps total**.
- Launch cost: "historical and projected launch pricing data" implies **< $200/kg by the mid-2030s**. Quote: *"At that price point, the cost of launching and operating a space-based data center could become roughly comparable to the reported energy costs of an equivalent terrestrial data center."*
- Radiation: Trillium (v6e) TPUs tested in a 67 MeV proton beam; HBM showed irregularities only above **2 krad(Si)** vs an expected shielded 5-year mission dose of **750 rad(Si)**; *"No hard failures were attributable to TID up to the maximum tested dose of 15 krad(Si)."*
- Next step: **two prototype satellites with Planet, launch by early 2027**.
- Quote on energy: the Sun emits "more power than 100 trillion times humanity's total electricity production."

## Primary (where the underlying document differs or adds)
- Preprint adds (per existing TechCrunch note): $200/kg assumes ~180 Starship launches/yr; with 70% fewer launches still ≈ $300/kg; launched-power price at $200/kg ≈ $810/kW/yr vs terrestrial data-centre energy spend $570–3,000/kW/yr. Explicitly *not* an economic-feasibility study.
- Joule version not read (403).

## Derived (our arithmetic — formula shown)
- Price gap today: SpaceX 2026 rideshare list $7,000/kg (see pricing note) ÷ $200/kg = **35×** reduction required.
- HBM margin: 2,000 rad ÷ 750 rad = **2.7×** margin on the component that fails first — thin for a 5-year life if shielding is lighter than the 10 mm-Al-equivalent assumed.

## Relevance to the Entrant
- Google's radiation result is the single most reusable datum for the Entrant: a COTS 2024-generation AI accelerator survives 5 years in LEO at the component level. It de-risks the "can we fly a modern inference chip?" question for EO edge processing.
- The 8× solar productivity number is for dawn-dusk SSO — the same orbit most EO constellations fly. The Entrant's power budget argument can cite it.

## Promote to
- [[intel/wiki/orbital-compute-launch-economics]]
- [[intel/wiki/orbital-data-center-landscape]]
