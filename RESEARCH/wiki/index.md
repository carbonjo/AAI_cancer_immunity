---
okf_version: "0.2"
---

# AAI cancer immunity — RESEARCH wiki

OKF v0.2 bundle. Read this file first at query time. All concept pages are `status: draft` and unverified unless `verified.by` starts with `human:`.

# People

* [David Graham](people/david-graham.md) - Student. First drafts of notes, tutorial edits, and analyses.
* [Dominic Sciarrino](people/dominic-sciarrino.md) - Student. First drafts of notes, tutorial edits, and analyses.
* [Dr. John Krolewski](people/john-krolewski.md) - Subject-matter expert. Cancer cell biology, cancer immunity, immunogenomics sanity checks.
* [Dr. Joaquin Carbonara](people/joaquin-carbonara.md) - Technical advisor. Schema owner for this OKF bundle; Flask/Docker/OpenAI tutorial; research methods.

# Concepts

* [Cancer cell biology](concepts/cancer-cell-biology.md) - Cancer is clonal evolution inside a niche; hallmarks are a map, not a bingo card.
* [Cancer immunity](concepts/cancer-immunity.md) - Adaptive anti-tumor immunity is recognition; the cancer-immunity cycle can break at more than one step.
* [Four-module argument](concepts/four-module-argument.md) - Information flow, scRNA-seq, cancer biology, and cancer immunity are one chain, not four courses.
* [Information flow in the cell](concepts/information-flow.md) - DNA, RNA, protein, and signaling are different information layers; mRNA is a useful incomplete snapshot.
* [Single-cell RNA sequencing](concepts/scrna-seq.md) - A cells-by-genes count matrix is a noisy photograph of transcriptional programs, one barcode at a time.

# Papers

* [Chen & Mellman 2013 — The cancer-immunity cycle](papers/chen-mellman-2013.md) - Seven-step cycle used as the tutorial’s immunity figure.
* [Crick 1970 — Central dogma of molecular biology](papers/crick-1970.md) - Nature paper stating the direction of residue-by-residue sequence transfer.
* [Hanahan & Weinberg 2011 — Hallmarks of cancer, next generation](papers/hanahan-weinberg-2011.md) - Map of cancer phenotypes used as the tutorial’s hallmark cards.
* [Wolfe et al. 2022 — GeoTyper](papers/wolfe-2022-geotyper.md) - Preprint on an automated pipeline from raw scRNA-seq to cell-type identification. PDF is in raw/.
* [Zheng et al. 2017 — Massively parallel digital transcriptional profiling](papers/zheng-2017.md) - Droplet / 10x-style conceptual workflow for single-cell RNA-seq.

# Claims

* [The cancer-immunity cycle can fail at more than one step](claims/cycle-can-break-at-any-step.md) - Antigen, presentation, priming, trafficking, infiltration, recognition, and killing are distinct failure points.
* [Hallmarks are a map, not a checklist](claims/hallmarks-are-a-map.md) - Hallmarks organize mechanism families. They do not prove every tumor uses every hallmark equally.
* [mRNA is an incomplete snapshot of cell state](claims/rna-is-incomplete-readout.md) - Standard mRNA counts omit PTMs, many protein levels, space, and fast signaling.
* [UMAP is visualization, not evidence](claims/umap-is-not-evidence.md) - UMAP displays a neighborhood graph. It is not space, time, or proof of lineage.

# Methods

* [Karpathy LLM-wiki](methods/llm-wiki.md) - Persistent compiled markdown wiki between the reader and raw sources. Not query-time RAG.
* [Open Knowledge Format v0.2](methods/okf-v0.2.md) - Vendor-neutral markdown + YAML. Required field is type. Provenance, trust, and lifecycle are optional families.

# Playbooks

* [Ingest](playbooks/ingest.md) - Drop one source in raw/, compile it into wiki pages, update index and log, lint.
* [Lint](playbooks/lint.md) - Health-check the OKF bundle for missing type, broken links, and orphans.
* [Query](playbooks/query.md) - Answer from wiki/index.md and linked pages. File good answers back into the wiki.
* [SME review](playbooks/sme-review.md) - Only Dr. John Krolewski (or a human he designates) may set verified.by human on biology.

# Decisions

* [Knowledge base lives in RESEARCH/](decisions/kb-lives-in-research.md) - This folder is the compiled OKF wiki for AAI cancer immunity. Dated 2026-09-24.
