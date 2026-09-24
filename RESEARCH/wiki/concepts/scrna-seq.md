---
type: Concept
title: Single-cell RNA sequencing
description: A cells-by-genes count matrix is a noisy photograph of transcriptional programs, one barcode at a time.
tags: [module-2, teaching]
status: draft
generated: { by: agent:cursor, at: 2026-09-24T21:50:00Z }
sources:
  - id: goals
    resource: raw/learning-goals.md
    title: Learning goals
  - id: starter
    resource: raw/starter-reading.md
    title: Starter reading
  - id: geotyper
    resource: raw/papers/2205.01187v1.pdf
    title: Wolfe et al. 2022 GeoTyper
---

Second module. Outcome 2: describe a droplet experiment through the count matrix and list three failure modes — [scrna-failure-modes](scrna-failure-modes.md). UMAP is a map, not evidence — [umap-is-not-evidence](../claims/umap-is-not-evidence.md).

Starter list: [Zheng 2017](../papers/zheng-2017.md) (droplet / 10x-style workflow); [Luecken & Theis 2019](../papers/luecken-theis-2019.md) (QC through interpretation). GeoTyper ([paper](../papers/wolfe-2022-geotyper.md), [method](../methods/geotyper.md)) is an end-to-end GEO→FASTQ→count matrix→cluster→label pipeline; it uses UMAP to *display* clusters.

Not a Scanpy/Seurat lab (learning-goals non-goal), even though GeoTyper itself uses Seurat.
