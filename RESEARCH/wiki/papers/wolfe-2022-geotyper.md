---
type: Paper
title: Wolfe et al. 2022 — GeoTyper
description: arXiv preprint of an automated GEO→FASTQ→count-matrix→cluster→label pipeline for scRNA-seq.
tags: [scrna, pipeline]
status: draft
resource: https://arxiv.org/abs/2205.01187
generated: { by: agent:cursor, at: 2026-09-24T21:50:00Z }
sources:
  - id: pdf
    resource: raw/papers/2205.01187v1.pdf
    title: 2205.01187v1.pdf
---

Compiled from `raw/papers/2205.01187v1.pdf` (arXiv:2205.01187v1, 2 May 2022). Authors: Cecily Wolfe, Yayi Feng, David Chen, Edwin Purcell (UVA School of Data Science); Anne Talkington, Sepideh Dolatshahi (UVA Biomedical Engineering); Heman Shakeri (UVA School of Data Science). Code named in the abstract: https://github.com/celineyayifeng/GeoTyper.

Motivation they write: TME composition (malignant, stromal, immune) and ligand–receptor communication; immune-system evasion cited as a Hanahan & Weinberg 2011 hallmark. Goal: a standardized workflow from NCBI GEO raw reads to visualization, statistics, and cell-type IDs for users in immunology or computational biology.

They tested on public FASTQs: 10x PBMC ([15] in the PDF), 10x NSCLC mixture from 7 donors ([16]), and lymphoma GEO [GSE175785](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE175785) (Cerapio / Gravelle et al.). Pair of FASTQs: barcodes/UMIs vs cDNA.

Method page: [geotyper](../methods/geotyper.md). Claims: [geotyper-marker-ambiguity](../claims/geotyper-marker-ambiguity.md), [geotyper-label-disagreement](../claims/geotyper-label-disagreement.md). They display clusters with UMAP — [umap-is-not-evidence](../claims/umap-is-not-evidence.md). Related teaching pages: [scrna-seq](../concepts/scrna-seq.md), [cancer-immunity](../concepts/cancer-immunity.md). They cite [Luecken & Theis 2019](luecken-theis-2019.md) as a best-practices tutorial, not as this pipeline.
