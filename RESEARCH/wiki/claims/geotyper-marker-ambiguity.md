---
type: Claim
title: One canonical marker can map to many cell types
description: GeoTyper’s PanglaoDB step scores markers by max(sensitivity − specificity) because markers are not unique.
tags: [scrna]
status: draft
generated: { by: agent:cursor, at: 2026-09-24T21:50:00Z }
sources:
  - id: pdf
    resource: raw/papers/2205.01187v1.pdf
    title: Wolfe et al. 2022 GeoTyper
---

From GeoTyper §IV-D: they take Seurat’s top five markers per cluster and match PanglaoDB; “one canonical marker could be associated with multiple cell types,” so they use the maximum difference between sensitivity and specificity to pick a type for that marker.

They also write (literature review) that automatic ID is non-trivial because it needs system-specific knowledge and because canonical-marker expression is heterogeneous.

Related: [geotyper](../methods/geotyper.md), [scrna-failure-modes](../concepts/scrna-failure-modes.md) (over-naming clusters).
