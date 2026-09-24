---
type: Concept
title: scRNA-seq teaching failure modes
description: Learning-goals names three: dropout, doublets, and over-naming clusters.
tags: [module-2, teaching]
status: draft
generated: { by: agent:cursor, at: 2026-09-24T21:50:00Z }
sources:
  - id: goals
    resource: raw/learning-goals.md
    title: Learning goals
  - id: geotyper
    resource: raw/papers/2205.01187v1.pdf
    title: Wolfe et al. 2022 GeoTyper
---

From `raw/learning-goals.md` outcome 2: dropout, doublets, over-naming clusters.

GeoTyper’s Seurat QC (not a substitute for those three names) filters cells with unique feature counts over 4,500 or under 200, and mitochondrial reads at 25% or two standard deviations above the mean, whichever is stricter, to drop likely multiplets or fragments. Their cell-type tools also disagree and leave cells unlabeled — see [geotyper-label-disagreement](../claims/geotyper-label-disagreement.md) and [geotyper-marker-ambiguity](../claims/geotyper-marker-ambiguity.md).

Parent: [scrna-seq](scrna-seq.md).
