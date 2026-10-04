---
type: intel
tags: [sdc, intel/raw, space/eo-edge, space/onboard-ai, research/ieee, market/germany]
source: IEEE (LEO SatS Initiative workshop summary; DLR eLib copy)
url: https://elib.dlr.de/196553/1/paper_i2cicc_LEO_sats_v5_camera_ready.pdf
author: Markus Gardill (BTU Cottbus), Witold Kinsner (U Manitoba), Jan Budroweit (DLR Bremen), Akram Al-Hourani (RMIT), Emily Dunkel & Jason Swope (NASA JPL), David Evans (ESA ESOC), Maximilian Staebler (DLR Ulm)
published: 2023-07-26
captured: 2026-10-04
primary: "this is the primary (camera-ready PDF, pp. 1–3 read)"
---
# Towards Space Edge Computing and Onboard AI for Real-Time Teleoperations (IEEE LEO SatS, 2023)

## Reported (what the source says)
- Joint DLR / JPL / ESOC / academia summary of the IEEE **LEO Satellites and Systems (SatS)** workshop: (i) ML for mega-constellations, (ii) **benchmarking deep-learning models on edge processors onboard the ISS**, (iii) flight software on the Snapdragon processor on ISS, (iv) **ESA OPS-SAT Space Lab** as the experimentation platform for edge computing and onboard AI, (v) **Gaia-X / Dataspaces** synergy with EO satellites.
- Latency framing: LEO round-trip **~25–88 ms** vs GEO **477–600 ms**; optical ISL propagation in free space is **50% faster than fibre**, so LEO+ISL can beat terrestrial fibre latency.
- Compute framing: current space processors like **RAD750** have "limited compute compared with modern edge processors"; benchmarked **Intel Movidius Myriad X** and **Qualcomm Snapdragon 855** on HPE **Spaceborne Computer-2** on the ISS — "to date, we have found **no difference in output** between ground and ISS runs, and **no errors from memory checkers**" (ISS shielding, non-polar orbit caveated).
- Mega-constellation challenges listed include **onboard processing energy efficiency** and ISL routing.

## Primary (where the underlying document differs or adds)
- this is the primary

## Derived (our arithmetic — formula shown)
- none

## Relevance to the Entrant
- Shows that **DLR (Bremen, Ulm) and ESOC (Darmstadt)** have been publishing on space edge computing since 2023, and that **OPS-SAT** is the ESA sandbox they use. The German/ESOC network is a credible origin story for a European orbital-compute entrant.
- The **Gaia-X/Dataspaces** angle is a European-specific hook: an orbital node as a sovereign data-space participant.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]]
