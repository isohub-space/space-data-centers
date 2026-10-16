---
type: intel
tags: [sdc, intel/raw, market/competitors, market/china, space/orbital-compute, company/star-vision]
source: Mediasat (English edition) — relays ITHome and China in Space
url: https://mediasat.info/en/2026/10/01/china-plans-to-laser-link-1000-satellites-into-an-orbital-supercomputer/
author: Mediasat
published: 2026-10-01
captured: 2026-10-12
primary: not opened (ITHome report of the 2026-09-25 Hangzhou unveiling; China in Space)
---
# Mediasat — China plans to laser-link 1,000+ satellites into an orbital supercomputer (Space.IDC)

## Reported (what the source says)
- **Space.IDC Computing Constellation** (literal: "Space String Computing Constellation"), developed by
  **STAR.VISION** and **Dongfang Xinglian**, unveiled **2026-09-25** in Hangzhou *(reported)*.
- Size: **> 1,080 satellites** — **> 720** application tier + **> 360** computing tier in sun-synchronous orbit;
  laser-linked *(reported; link rates not stated)*.
- Timeline: **first satellite in orbit Q4 2027**; full deployment **2035** *(reported)*.
- Satellite classes *(reported)*:

  | Class | Compute (PFLOPS) | Power (kW) |
  |---|---:|---:|
  | G1 test | 40–60 | 11.5 (solar) |
  | G2 standard | 160–310 | 48 |
  | G3 flagship | 460–1,000 | 140 (solar) |

- Funding: **CNY 10 B (~$1.49 B) credit agreements** with ICBC and Agricultural Bank of China; **≥ CNY 1 B
  (~$149 M)** for phase one *(reported)*.
- Launch: G1 booked on Orienspace Gravity-1 and Galactic Energy Ceres-2 *(reported)*. No Space.IDC satellite
  flown yet; STAR.VISION tested technology on two satellites built for Uzbekistan and Indonesia.
- Context: the **Three-Body** constellation (ADA Space + Zhejiang Lab) has **about a dozen** computing
  satellites in orbit *(reported; first 12 launched 2025-05-14 per other coverage, snippet, not opened)*.

## Primary (what the underlying paper / filing says — where it differs)
- ITHome and China in Space not opened. **FLOPS precision is not stated** (FP4/FP8/FP16 differ by 2–4×),
  so the PFLOPS figures cannot be compared with Nvidia or Google numbers as given.

## Derived (our arithmetic — formula shown)
- Compute density, PFLOPS per kW = compute / power *(derived; precision unknown)*:
  G1 40/11.5 – 60/11.5 = **3.5–5.2**; G2 160/48 – 310/48 = **3.3–6.5**; G3 460/140 – 1,000/140 = **3.3–7.1**.
- Power per satellite class vs the vault's tiers: G1 (11.5 kW) is in the kW-class band of Starcloud-2 (8 kW);
  G3 (140 kW) is comparable to SpaceX AI1 (150 kW peak, [[intel/raw/2026-02-02-via-satellite-spacex-xai-fcc-million-satellites]]).
- Phase-one capital per computing-tier satellite if phase one = all 360: CNY 1 B / 360 ≈ CNY 2.8 M (~$0.41 M) —
  **not meaningful** without the phase-one satellite count; shown only to flag that the funding is credit, not
  equity, and its scope is undefined.

## Relevance to the Entrant
- **The vault had no Chinese tier-A/B entry.** China now has two orbital-compute programmes: one flying
  (Three-Body, ~12 sats) and one financed by state-bank credit (Space.IDC). Neither competes for European
  sovereign or defence customers — they **strengthen** the sovereignty argument for a European operator.
- Space.IDC's first flight (Q4 2027) is on the same clock as Starcloud-2 and SpaceX's first AI1 prototypes;
  the 2027–28 window will be crowded with **demonstrators**, not services.
- State-bank credit (not venture equity) is a different capital model from the US tier — a comparison point
  for European public financing (EIB, national promotional banks).

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
