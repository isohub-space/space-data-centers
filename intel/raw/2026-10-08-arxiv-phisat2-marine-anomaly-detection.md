---
type: intel
tags: [sdc, intel/raw, literature/arxiv, edge/eo, programme/esa-phisat, use-case/maritime]
source: arXiv (cs.AI, cs.CV; submitted via CCSD/HAL proxy)
url: https://arxiv.org/abs/2610.11735
author: arXiv preprint (affiliations not shown on the abstract page)
published: 2026-10-08
captured: 2026-10-12
primary: this preprint (abstract opened; PDF fetched but not machine-readable in this sweep)
---
# arXiv — Onboard Marine Anomaly Detection on Φsat-2: From Simulation-Based Development to In-Orbit Demonstration

## Reported (what the source says)
- A lightweight **marine anomaly detection pipeline built for ESA's Φsat-2**: sea segmentation →
  self-supervised feature encoding → anomaly detection as deviation from normal sea state → optional
  characterisation of some anomaly types *(primary, abstract)*.
- First trained on **simulated Φsat-2 imagery**. Early tests on **real in-orbit data showed a significant
  mismatch with the simulation**; the team retrained on **real Level-1 imagery** with an improved annotation
  strategy, which "substantially" improved performance *(primary, abstract; no number given)*.
- Conclusion: simulation is valuable for pre-flight risk reduction, but scientific validation needs
  representative in-orbit data and should be kept separate from functional validation *(primary, abstract)*.

## Primary (what the underlying paper / filing says — where it differs)
- No quantitative metric (precision/recall, runtime, downlink saving) appears in the abstract. The full-text
  PDF (8 pages) was fetched but its text could not be extracted in this sweep — **metrics not checked**.
- Affiliations not listed on the abstract page.

## Derived (our arithmetic — formula shown)
- None — no figures to work with.

## Relevance to the Entrant
- **Sim-to-real is the hidden cost of onboard EO models.** A pipeline trained on simulated Φsat-2 imagery
  failed to transfer and had to be retrained on real Level-1 data. Combined with the CNES finding that
  inference on raw imagery is fine ([[intel/raw/2026-09-29-arxiv-cnes-raw-imagery-onboard-ai]]), the moat
  is **access to real in-orbit imagery from the target sensor**, not the model architecture.
- Maritime anomaly detection is the same buyer as Ubotica's maritime platform and the BIFROST Arctic case —
  more evidence that maritime is the first paying EO-edge use case in Europe.
- Practical: budget a post-launch retraining cycle (and the uplink to ship new weights — see the uplink
  constraint in [[intel/wiki/eo-edge-compute-value-chain]] §1) into the first mission plan.

## Promote to
- [[intel/wiki/eo-edge-compute-value-chain]]
