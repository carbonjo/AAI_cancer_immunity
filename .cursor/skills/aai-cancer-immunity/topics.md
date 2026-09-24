# Four topics

Teach and research these as a chain.

## 1. Information flow in the cell

DNA sequence is not the only information. Cells also run **signaling**, **transcriptional programs**, **splicing**, **translation**, and **protein modification**. Messenger RNA is a high-throughput projection of that program — useful, not complete.

Bridge to module 2: scRNA-seq measures that projection one cell at a time.

## 2. Single-cell RNA sequencing

A count matrix (cells × genes) is the starting object. Typical teaching pipeline: dissociation → barcodes/UMIs → QC → normalization → embedding → clusters → marker genes → **provisional** cell labels.

Honesty rules the students must practice: dropout, doublets, dissociation bias, batch effects, and **abstention** when a cluster should stay “lineage + markers” rather than a forced name.

Bridge to module 3: malignant and non-malignant cells share a tissue; bulk RNA averages them away.

## 3. Cancer cell biology

Cancer is clonal evolution plus a corrupted microenvironment. Use the hallmarks as a **map**, not a bingo card. Drivers vs passengers, heterogeneity, and the tumor niche (stroma, endothelium, immune cells) all matter.

Bridge to module 4: many hallmarks only make sense once immune recognition and evasion are in the picture.

## 4. Cancer immunity

The cancer-immunity cycle (antigen release → presentation → T-cell priming → trafficking → recognition → killing → more antigen) can break at any step. Checkpoints (CTLA-4, PD-1/PD-L1) are physiological brakes that tumors exploit. TIME language (hot / cold / excluded) is a starting sketch, not a finished taxonomy.

Close the loop: scRNA-seq is one way to see immune and tumor states together — with the limits from modules 1–2 still in force.

## Landmark teaching citations (not a literature review)

Full annotated list: `references/starter-reading.md`.

- Central dogma and its later refinements
- 10x-style droplet scRNA-seq conceptual workflow
- Hanahan & Weinberg hallmarks
- Chen & Mellman cancer-immunity cycle
- Immune checkpoint blockade as a clinical/scientific fact pattern (Allison / Honjo line of work)
