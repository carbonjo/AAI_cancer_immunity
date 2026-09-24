---
type: Method
title: GeoTyper pipeline
description: sratoolkit → Cell Ranger or Alevin → Seurat QC/cluster/UMAP → PanglaoDB, SingleR, scCATCH, ACTINN.
tags: [scrna, pipeline]
status: draft
generated: { by: agent:cursor, at: 2026-09-24T21:50:00Z }
sources:
  - id: pdf
    resource: raw/papers/2205.01187v1.pdf
    title: Wolfe et al. 2022 GeoTyper
---

Compiled from the Methodology and Results sections of [Wolfe et al. 2022](../papers/wolfe-2022-geotyper.md). Three boxes they name: Data Processing, Cell Type Identification, Visualization.

**Processing.** `sratoolkit` pulls FASTQs by SRR ID (barcode/UMI file + cDNA file). 10x Chromium → Cell Ranger Count (align to a reference transcriptome → feature-barcode matrix). Alternative: Alevin (10x and Drop-seq). They write Alevin is cheaper than Cell Ranger but “highly variable” for genes per cell across datasets.

**Seurat.** Filter cells with unique feature counts over 4,500 or under 200. Mitochondrial-read threshold: 25% or two standard deviations above the mean, whichever is stricter — intended to drop likely multiplets or fragments. Then `LogNormalize`, scale, PCA, KNN graph (Euclidean, Jaccard edge weights, modularity clusters). Clusters are *shown* with UMAP (t-SNE mentioned as similar). Seurat itself does not name cell types.

**Labels.** PanglaoDB: top five Seurat markers per cluster, scored by max(sensitivity − specificity) because one marker can map to many types ([geotyper-marker-ambiguity](../claims/geotyper-marker-ambiguity.md)). scCATCH: cluster annotation via CellMatch. ACTINN: 3 hidden layers (100 / 50 / 25); their implementation labels B cell, monocyte, NK, T cell, or unknown. SingleR: iterative Spearman correlation to bulk reference types, cell-by-cell rather than cluster-then-label.

**What they report.** HTML from an R Markdown. PBMC used as the immune-rich benchmark; Seurat-vignette labels treated as “ground truth” for comparison. All methods called T cells (or T subtypes) most common; monocytes usually second except scCATCH. Compositions still differ — [geotyper-label-disagreement](../claims/geotyper-label-disagreement.md).

**Limits they state.** No valid cross-model accuracy for ACTINN because training labels came from PanglaoDB, not flow cytometry. ACTINN training set is narrow. Current pipeline limited to users with Rivanna (UVA HPC). Suggested future: ensemble / hard voting.

This is **not** the student tutorial’s method. Learning goals say the tutorial is not a Seurat lab.
