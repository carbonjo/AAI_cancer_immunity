---
okf_version: "0.2"
---

# AAI cancer immunity — RESEARCH wiki

OKF v0.2 bundle. Read this file first at query time. All concept pages are `status: draft` and unverified unless `verified.by` starts with `human:`.

# People

* [David Graham](people/david-graham.md) - Student. First drafts of notes, tutorial content, quizzes, and analyses.
* [Dominic Sciarrino](people/dominic-sciarrino.md) - Student. First drafts of notes, tutorial content, quizzes, and analyses.
* [Dr. John Krolewski](people/john-krolewski.md) - Subject-matter expert. Owns cancer cell biology, cancer immunity, and immunogenomics sanity checks.
* [Dr. Joaquin Carbonara](people/joaquin-carbonara.md) - Technical advisor. Flask/Docker/OpenAI tutorial, research methods, GitHub.

# Concepts

* [Cancer cell biology](concepts/cancer-cell-biology.md) - Cancer is clonal evolution inside a niche; hallmarks are a map, not a bingo card.
* [Cancer immunity](concepts/cancer-immunity.md) - Adaptive anti-tumor immunity is recognition; the cancer-immunity cycle can break at more than one step.
* [Four-module argument](concepts/four-module-argument.md) - Information flow, scRNA-seq, cancer biology, and cancer immunity are one chain, not four courses.
* [Hot vs cold TIME](concepts/time-hot-cold.md) - Learning-goals asks students to say what hot/cold TIME does and does not mean. Not a finished taxonomy.
* [Information flow in the cell](concepts/information-flow.md) - DNA, RNA, protein, and signaling are different information layers; mRNA is a useful incomplete snapshot.
* [scRNA-seq teaching failure modes](concepts/scrna-failure-modes.md) - Learning-goals names three: dropout, doublets, and over-naming clusters.
* [Single-cell RNA sequencing](concepts/scrna-seq.md) - A cells-by-genes count matrix is a noisy photograph of transcriptional programs, one barcode at a time.

# Papers

* [Alberts et al. — Molecular Biology of the Cell](papers/alberts-molbiol-cell.md) - Textbook spine for transcription, gene regulation, and signaling. Not a citation dump.
* [Chen & Mellman 2013 — The cancer-immunity cycle](papers/chen-mellman-2013.md) - Seven-step cycle used as the tutorial’s immunity figure.
* [Crick 1970 — Central dogma of molecular biology](papers/crick-1970.md) - Nature paper stating the direction of residue-by-residue sequence transfer.
* [Hanahan & Weinberg 2011 — Hallmarks of cancer, next generation](papers/hanahan-weinberg-2011.md) - Map of cancer phenotypes used as the tutorial’s hallmark cards.
* [Hanahan 2022 — Hallmarks of cancer, new dimensions](papers/hanahan-2022.md) - Optional extension on the starter list. Tutorial core stays on Hanahan & Weinberg 2011.
* [Luecken & Theis 2019 — Current best practices in scRNA-seq analysis](papers/luecken-theis-2019.md) - Mol Syst Biol tutorial from QC through interpretation, including what not to overclaim.
* [Sharma & Allison 2015 — The future of immune checkpoint therapy](papers/sharma-allison-2015.md) - Science review on the starter list for the cancer-immunity module.
* [Wolfe et al. 2022 — GeoTyper](papers/wolfe-2022-geotyper.md) - arXiv preprint of an automated GEO→FASTQ→count-matrix→cluster→label pipeline for scRNA-seq.
* [Zheng et al. 2017 — Massively parallel digital transcriptional profiling](papers/zheng-2017.md) - Droplet / 10x-style conceptual workflow for single-cell RNA-seq.

# Claims

* [Biology stays needs-SME-review until Krolewski comments](claims/needs-sme-review.md) - Roster rule. Agents and students do not treat drafted biology as signed.
* [Do not silently fix the tutorial when a paper disagrees](claims/do-not-silently-fix-tutorial.md) - Write a needs-SME-review note and ask Dr. Krolewski. Methods questions go to Dr. Carbonara.
* [GeoTyper’s cell-type tools disagree on the same PBMC run](claims/geotyper-label-disagreement.md) - Same Seurat clusters; PanglaoDB, SingleR, scCATCH, and ACTINN report different compositions and leave cells unlabeled.
* [Hallmarks are a map, not a checklist](claims/hallmarks-are-a-map.md) - Hallmarks organize mechanism families. They do not prove every tumor uses every hallmark equally.
* [mRNA is an incomplete snapshot of cell state](claims/rna-is-incomplete-readout.md) - Standard mRNA counts omit PTMs, many protein levels, space, and fast signaling.
* [One canonical marker can map to many cell types](claims/geotyper-marker-ambiguity.md) - GeoTyper’s PanglaoDB step scores markers by max(sensitivity − specificity) because markers are not unique.
* [The cancer-immunity cycle can fail at more than one step](claims/cycle-can-break-at-any-step.md) - Antigen, presentation, priming, trafficking, infiltration, recognition, and killing are distinct failure points.
* [UMAP is visualization, not evidence](claims/umap-is-not-evidence.md) - UMAP displays a neighborhood graph. It is not space, time, or proof of lineage.

# Methods

* [GeoTyper pipeline](methods/geotyper.md) - sratoolkit → Cell Ranger or Alevin → Seurat QC/cluster/UMAP → PanglaoDB, SingleR, scCATCH, ACTINN.
* [Karpathy LLM-wiki](methods/llm-wiki.md) - Persistent compiled markdown wiki between the reader and raw sources. Not query-time RAG.
* [Open Knowledge Format v0.2](methods/okf-v0.2.md) - Vendor-neutral markdown + YAML. Required field is type. Provenance, trust, and lifecycle are optional families.

# Playbooks

* [Ingest](playbooks/ingest.md) - Drop one source in raw/, compile it into wiki pages, update index and log, lint.
* [Lint](playbooks/lint.md) - Health-check the OKF bundle for missing type, broken links, and orphans.
* [Query](playbooks/query.md) - Answer from wiki/index.md and linked pages. File good answers back into the wiki.
* [SME review](playbooks/sme-review.md) - Only Dr. John Krolewski (or a human he designates) may set verified.by human on biology.

# Decisions

* [Knowledge base lives in RESEARCH/](decisions/kb-lives-in-research.md) - This folder is the compiled OKF wiki for AAI cancer immunity. Dated 2026-09-24.
* [No PHI or keys in git](decisions/no-phi-in-git.md) - Public teaching content only. No PHI, identifiable patients, unpublished matrices, or OpenAI keys in the tree.
