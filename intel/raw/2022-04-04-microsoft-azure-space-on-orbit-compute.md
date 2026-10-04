---
type: intel
tags: [sdc, intel/raw, market/startups, company/microsoft, hyperscaler, edge/eo, software/orchestration, primary]
source: Microsoft Azure blog
url: https://azure.microsoft.com/en-us/blog/empowering-space-development-off-the-planet-with-azure/
author: Microsoft Azure Team
published: 2022-04-04
captured: 2026-10-04
primary: this is the primary
---
# Microsoft Azure — "Empowering space development off the planet with Azure" (Azure Space on-orbit compute)

Historical baseline: the hyperscaler "edge compute on satellites" pitch predates the ODC wave by
three years and was **EO-centric**.

## Reported (what the source says)
- Azure Space platform for **on-orbit compute "at the ultimate edge"**, spacecraft running AI
  workloads connected to Azure.
- Partners: **Ball Aerospace** (on-orbit testbed sats for US Government); **Loft Orbital** (satellite
  launching **2023** hosting third-party software apps); **Thales Alenia Space** (demonstrating on-orbit
  compute on the ISS); **HPE Spaceborne Computer-2** on ISS.
- Workloads: computer vision (astronaut equipment damage), **Earth observation and climate data
  processing**, **change detection**, reconfigurable containerized processing.
- Standards: SOSA, UCI, OMS; Azure services: Synapse, Data Lake Gen2, Batch, Container Registry;
  Blackshark.ai Orca geospatial.
- "Any developer can be a space developer with Azure."
- **No 2026 Azure Space orbital data-center announcement found** in this lane's searches; Microsoft's
  2026 presence is via the **$30B Azure capacity deal with Anthropic** (terrestrial) only.

## Primary (where the underlying document differs or adds)
- This is the primary.

## Derived (our arithmetic — formula shown)
- none

## Relevance to the Entrant
- Microsoft (with Thales Alenia, Loft, HPE) **already prototyped EO change-detection on orbit in
  2022–23** and did not productize it — a cautionary data point on demand, or evidence that the
  hyperscalers treat on-orbit EO processing as a feature, leaving the standalone service to startups.
- Container-portable (Azure/Red Hat Device Edge) is the expected integration surface; the Entrant's node
  should expose a cloud-native API, not a bespoke one.

## Promote to
- [[intel/wiki/orbital-data-center-landscape]]
