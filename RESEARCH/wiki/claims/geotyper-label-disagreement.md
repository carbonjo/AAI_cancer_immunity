---
type: Claim
title: GeoTyper’s cell-type tools disagree on the same PBMC run
description: Same Seurat clusters; PanglaoDB, SingleR, scCATCH, and ACTINN report different compositions and leave cells unlabeled.
tags: [scrna]
status: draft
generated: { by: agent:cursor, at: 2026-09-24T21:50:00Z }
sources:
  - id: pdf
    resource: raw/papers/2205.01187v1.pdf
    title: Wolfe et al. 2022 GeoTyper
---

From GeoTyper Results (PBMC benchmark; Seurat-vignette labels treated as ground truth for *this paper*):

- Baseline Seurat: Naive CD4+ T 23.9%, CD14+ monocytes 18.8%, Memory CD4+ T 18.1%, B 13.0%, CD8+ T 12.6%.
- PanglaoDB: T memory 18.2%, naive B 16.6%, monocytes 15.5%, T 14.2%, neutrophils 13.6%.
- SingleR: T 42.8%, monocytes 31.0%, B 16.2%, NK 4.78%, platelets 1.0%.
- scCATCH: Naive CD4+/CD8+ T 18.2%, B 16.56%, eosinophils 15.5%, Unknown 14.2%, CD1C+ dendritic 13.6%.
- ACTINN: T 45.3%, monocytes 33.6%, B 17.7%, NK 3.45%.

They say all methods put T cells first; monocytes usually second except scCATCH; less-common types vary. Confusion matrices: individual-cell labels differ “considerably,” partly because reference sets differ. Discussion: eager-learning tools (they list Seurat, ACTINN, SingleR after Xie et al.) have higher unlabeling rates; scCATCH can also unlabeled when markers do not split types. ACTINN training labels came from PanglaoDB, not flow cytometry.

Related: [geotyper](../methods/geotyper.md), [umap-is-not-evidence](umap-is-not-evidence.md).
