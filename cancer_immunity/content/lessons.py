"""Four-module tutorial content. Edit text here, not in the templates."""

from __future__ import annotations

MODULES: list[dict] = [
    {
        "id": "info-flow",
        "order": 1,
        "title": "Information flow in the cell",
        "blurb": "DNA is not a script that runs itself. Cells compute with signals, chromatin, RNA, and protein.",
        "minutes": 30,
        "objectives": [
            "Trace DNA → RNA → protein without treating the central dogma as the whole story.",
            "Explain how signaling and transcription factors change what a cell is doing.",
            "Say why mRNA abundance is a useful but incomplete snapshot of cell state.",
        ],
        "widget": "central_dogma",
        "sections": [
            {
                "title": "Why start here",
                "paragraphs": [
                    "Cancer immunity research is full of gene names, clusters, and pathways. Those objects only make sense if you can say what kind of information they carry. A mutation is a change in the genome. An mRNA count is evidence that a gene was transcribed recently. A phosphorylated receptor is a signal that may never appear in an RNA table.",
                    "This module builds a shared picture of cellular information flow so the next three modules have somewhere to sit. Single-cell RNA sequencing measures one layer of that flow. Cancer hijacks several layers at once. Immunity is another information system — recognition, not transcription — that collides with the tumor.",
                ],
                "bullets": [
                    "Sequence information: the genome (relatively stable in a clone).",
                    "Program information: which genes are on, spliced, and translated now.",
                    "Signal information: ligands, receptors, kinases, second messengers, lasting minutes to hours.",
                    "Identity information: durable cell-type programs plus more plastic cell states.",
                ],
            },
            {
                "title": "The central dogma, used carefully",
                "paragraphs": [
                    "Francis Crick’s central dogma says information in a cell does not flow backwards from protein into nucleic acid. DNA is transcribed into RNA; messenger RNA is translated into protein. That claim is still the backbone of molecular biology. It is not a claim that RNA and protein cannot regulate DNA, or that every functional RNA is a message for a protein.",
                    "Transcription copies a gene into RNA and is controlled by transcription factors, enhancers, silencers, and chromatin state. Many primary transcripts are spliced. Only some RNAs are mRNAs. Translation on ribosomes builds polypeptides, which fold and are often modified (phosphorylation, glycosylation, cleavage). Those modifications can switch a protein’s activity without any change in its mRNA.",
                    "Use the interactive diagram to walk DNA, RNA, and protein, then the regulatory arrows that the slogan version leaves out.",
                ],
                "callout": {
                    "label": "Keep this distinction",
                    "text": "Regulation (transcription factors, signaling, epigenetics) is not a violation of the central dogma. It is control of the flow, not a reverse translation of protein sequence into DNA sequence.",
                },
            },
            {
                "title": "Signaling is information from outside the nucleus",
                "paragraphs": [
                    "A T cell does not decide to kill a target by consulting its genome from scratch. It integrates ligands: antigen peptide on MHC, costimulatory molecules, cytokines, adhesion, nutrients, and inhibitory checkpoints. Receptors convert those ligands into intracellular chemistry — phosphorylation cascades, calcium, small GTPases — that converge on transcription factors (NFAT, AP-1, NF-κB, and others) and also on fast non-transcriptional effects such as cytoskeleton and vesicle trafficking.",
                    "The same logic applies to a tumor cell and to a macrophage. Growth factors, hypoxia, interferon, and contact with stroma all rewrite the RNA program. That is why a cluster in a scRNA-seq plot is not a genotype. It is a state that mixed inputs produced.",
                ],
                "bullets": [
                    "Ligand → receptor → adapters/kinases → transcription factors is the slow, RNA-visible arm.",
                    "The same receptor may also change protein activity in seconds, which RNA-seq will miss.",
                    "Feedback is normal: the products of transcription include more receptors, inhibitors, and ligands.",
                ],
            },
            {
                "title": "What RNA can and cannot tell you",
                "paragraphs": [
                    "If you could list every mRNA in a cell, you would know a lot about which transcriptional programs were recently active. You would not automatically know protein abundance, protein modification, which splice isoforms matter, or what the cell will do in twenty minutes. Cells also use noncoding RNAs and chromatin marks that a standard 3′ gene-count matrix does not represent well.",
                    "Still, mRNA is one of the few layers we can measure at genome scale in thousands of single cells. That is the bargain of scRNA-seq: a high-dimensional, noisy projection of state, not a complete wiring diagram. Module 2 is about how that projection is made and how it fails.",
                ],
                "callout": {
                    "label": "Bridge",
                    "text": "When a later module says a cell is exhausted, epithelial, or myeloid, the evidence will usually be a pattern of transcripts. Ask: which information layer is actually measured, and what is being inferred?",
                },
            },
        ],
        "quiz": [
            {
                "id": "if1",
                "prompt": "The central dogma is best stated as which of the following?",
                "choices": [
                    "DNA is transcribed to RNA, RNA is translated to protein, and protein sequence is not reverse-translated into nucleic acid.",
                    "The only functional molecules in a cell are proteins.",
                    "RNA levels always equal protein levels.",
                    "Signaling cannot change transcription because that would reverse the dogma.",
                ],
                "answer_index": 0,
                "explanation": "Crick’s claim is about the direction of residue-by-residue sequence transfer. Regulation of transcription by proteins is not reverse translation.",
            },
            {
                "id": "if2",
                "prompt": "A phosphorylated receptor can change cell behavior without a matching change in that receptor’s mRNA. What does that illustrate?",
                "choices": [
                    "The experiment must be wrong, because only RNA carries information.",
                    "Post-translational state is an information layer that standard mRNA counts omit.",
                    "Phosphorylation rewrites the gene’s DNA sequence.",
                    "Translation does not exist in immune cells.",
                ],
                "answer_index": 1,
                "explanation": "PTMs and signaling are real information. scRNA-seq will not see them directly.",
            },
            {
                "id": "if3",
                "prompt": "Why is mRNA still a reasonable readout of cell state for tumor–immune studies?",
                "choices": [
                    "Because mRNA is identical to protein function.",
                    "Because every cell type has a unique genome.",
                    "Because transcriptional programs are genome-scale, measurable in single cells, and often correlate with identity and activation programs — with known gaps.",
                    "Because droplet machines measure phosphorylation directly.",
                ],
                "answer_index": 2,
                "explanation": "We use RNA because it is measurable at scale, not because it is complete.",
            },
            {
                "id": "if4",
                "prompt": "A transcription factor sits at the junction of which two information flows?",
                "choices": [
                    "Only replication and cytokinesis.",
                    "Extracellular signals (via pathways that regulate the TF) and the DNA/RNA program (via binding to genomic control regions).",
                    "MHC peptide loading and glycosylation in the Golgi only.",
                    "Mitochondrial DNA repair and splicing of rRNA only.",
                ],
                "answer_index": 1,
                "explanation": "TFs convert signaling into a changed transcriptional program.",
            },
            {
                "id": "if5",
                "prompt": "Which statement should you take to Dr. Krolewski rather than treat as settled tutorial fact?",
                "choices": [
                    "mRNA is an incomplete snapshot of cell state.",
                    "A specific unpublished claim about how a particular patient’s prostate tumor processes interferon.",
                    "Droplet scRNA-seq produces a cells-by-genes count matrix.",
                    "PD-1 is an immune checkpoint receptor discussed in later modules.",
                ],
                "answer_index": 1,
                "explanation": "Teaching scaffolding is public. Patient-level or lab-specific biology needs the SME.",
            },
        ],
    },
    {
        "id": "scrna",
        "order": 2,
        "title": "Single-cell RNA sequencing",
        "blurb": "A count matrix is a noisy photograph of transcriptional programs, one cell at a time.",
        "minutes": 35,
        "objectives": [
            "Contrast bulk RNA-seq with single-cell RNA-seq.",
            "Walk a droplet experiment from tissue to count matrix.",
            "Name QC, embedding, clustering, and the temptation to over-name cells.",
        ],
        "widget": "umi_heatmap",
        "sections": [
            {
                "title": "Bulk averages hide the mixture",
                "paragraphs": [
                    "A tumor biopsy is not one cell type. It is malignant clones plus T cells, B cells, myeloid cells, endothelium, fibroblasts, and debris. Bulk RNA-seq blends those transcripts into one profile. If CD8A rises, you cannot tell whether T cells arrived, each T cell made more CD8A, or the tumor shrunk and the immune fraction grew.",
                    "Single-cell RNA-seq tries to attach transcripts to individual cells (or barcodes that usually correspond to cells). That is why it became a default language for tumor immune microenvironments: you can ask which cell is saying what, not only what the mixture said.",
                ],
            },
            {
                "title": "From tissue to a cells-by-genes matrix",
                "paragraphs": [
                    "A common teaching workflow (10x-style droplets) is: dissociate the tissue into a suspension, encapsulate cells with barcoded beads and enzymes, reverse-transcribe poly(A) RNA, add cell barcodes and unique molecular identifiers (UMIs), sequence, and count. The product is a sparse matrix: rows are genes, columns are barcodes, values are UMI counts.",
                    "Each design choice leaks into biology. Dissociation kills some cells preferentially (neutrophils and some neurons are famous casualties). Ambient RNA from broken cells contaminates droplets. Two cells in one droplet become a doublet that looks like a franken-cell. 3′ counting reports a gene, not a full isoform. None of this makes the method useless. It makes naive cluster names dangerous.",
                ],
                "bullets": [
                    "Cell barcode: which droplet / bead.",
                    "UMI: which original RNA molecule, used to collapse PCR duplicates.",
                    "Count: how many UMIs for that gene in that barcode, after filtering.",
                ],
            },
            {
                "title": "The usual computational story",
                "paragraphs": [
                    "Analysis is a pipeline with judgment at every step, not a single button. Typical stations: filter barcodes with too few counts or too many mitochondrial reads; normalize so libraries of different depth can be compared; find variable genes; reduce dimension (PCA, then a neighbor graph); embed for the human eye (UMAP/t-SNE are maps, not evidence); cluster; find marker genes; assign provisional names.",
                    "The heatmap widget is a toy version of the only object that is real at this stage: a handful of genes across a handful of cells. Epithelial-like cells light up EPCAM. T-cell-like cells light up CD3D. A cycling cell may show MKI67. Real data are sparser, noisier, and less polite.",
                ],
                "callout": {
                    "label": "Abstention",
                    "text": "If markers conflict, keep the label as lineage plus high/low genes (for example myeloid, high IDO1) rather than forcing a textbook name. That habit is part of the science, not a failure to finish.",
                },
            },
            {
                "title": "What scRNA-seq does not measure",
                "paragraphs": [
                    "Standard scRNA-seq is not spatial: you lost where the cell sat in the tumor. It is not time: each cell is destroyed for its library. It is not proteomics: PD-1 protein and PDCD1 mRNA can disagree. It is not genotype unless you add a separate assay. Multiome, CITE-seq, TCR-seq, and spatial methods exist because these gaps are scientifically expensive, especially in immunity.",
                    "Module 3 needs this honesty. A “tumor cluster” in UMAP is a transcriptional neighborhood. Whether those cells are one clone, many clones, or contaminated droplets is a separate question.",
                ],
            },
        ],
        "quiz": [
            {
                "id": "sc1",
                "prompt": "Bulk RNA-seq of a tumor and scRNA-seq of the same tumor differ most importantly because:",
                "choices": [
                    "Bulk sequences DNA while scRNA-seq sequences protein.",
                    "Bulk averages transcripts across cells; scRNA-seq assigns transcripts to barcodes that usually correspond to cells.",
                    "scRNA-seq cannot detect immune genes.",
                    "Bulk RNA-seq has no technical artifacts.",
                ],
                "answer_index": 1,
                "explanation": "The point of single-cell is to unmix the biopsy, not to magically remove error.",
            },
            {
                "id": "sc2",
                "prompt": "A UMI is used primarily to:",
                "choices": [
                    "Name the patient’s HLA type.",
                    "Collapse PCR duplicates from the same original RNA molecule.",
                    "Embed cells in UMAP.",
                    "Fix doublets during dissociation.",
                ],
                "answer_index": 1,
                "explanation": "Barcodes mark droplets; UMIs mark molecules.",
            },
            {
                "id": "sc3",
                "prompt": "A doublet is dangerous because:",
                "choices": [
                    "It can look like one cell that co-expresses programs from two cells (for example T cell + epithelial).",
                    "It deletes the genome.",
                    "It makes UMAP illegal.",
                    "It only occurs in plants.",
                ],
                "answer_index": 0,
                "explanation": "Mixed programs are a classic doublet signature and a classic biology signature — you have to look.",
            },
            {
                "id": "sc4",
                "prompt": "UMAP should be treated as:",
                "choices": [
                    "A proof of lineage relationships.",
                    "A visualization of a neighborhood graph, useful for display, not as the evidence itself.",
                    "A count of UMIs.",
                    "A spatial map of the biopsy.",
                ],
                "answer_index": 1,
                "explanation": "Do not read UMAP distances as developmental time or physical space.",
            },
            {
                "id": "sc5",
                "prompt": "Cluster 7 expresses both high EPCAM and high CD3D in a tumor sample. A disciplined next step is:",
                "choices": [
                    "Name it immediately as a new cell type, the epithelial T cell.",
                    "Consider doublet, ambient RNA, or a rare biology, and keep an uncertain label until reviewed.",
                    "Delete all epithelial genes from the matrix.",
                    "Average it back into bulk RNA-seq.",
                ],
                "answer_index": 1,
                "explanation": "Abstention is a feature. Flag it for the SME if it matters to a claim.",
            },
        ],
    },
    {
        "id": "cancer-bio",
        "order": 3,
        "title": "Cancer cell biology",
        "blurb": "Cancer is clonal evolution inside a tissue, not a single broken gene.",
        "minutes": 30,
        "objectives": [
            "Use the hallmarks as a map, not a checklist to memorize without mechanism.",
            "Separate driver events from heterogeneous cell states.",
            "Place malignant cells in a microenvironment that includes immune cells.",
        ],
        "widget": "hallmarks",
        "sections": [
            {
                "title": "A clone, not a uniform tissue",
                "paragraphs": [
                    "Cancers are populations. A founding cell acquires heritable changes (mutations, copy-number alterations, epigenetic states) that let its descendants expand when they should not. Daughter clones accumulate further changes. The biopsy you sequence is a mixture of those clones plus the normal and immune cells that live with them.",
                    "That evolutionary picture is why bulk measurements mislead and why single-cell methods are attractive. It is also why “the tumor cell” in a review article is a cartoon. Real tumors are heterogeneous in genotype and in state (cycling, hypoxic, epithelial, mesenchymal-like, drug-tolerant).",
                ],
            },
            {
                "title": "Hallmarks are a map",
                "paragraphs": [
                    "Hanahan and Weinberg organized cancer cell biology into hallmarks: sustaining proliferation, evading growth suppressors, resisting cell death, enabling replicative immortality, inducing angiogenesis, activating invasion and metastasis, reprogramming metabolism, and avoiding immune destruction — with enabling characteristics such as genome instability and tumor-promoting inflammation.",
                    "Click the cards in the diagram. Each hallmark is a family of mechanisms, not one gene. MYC can push proliferation; TP53 loss can weaken DNA-damage responses and apoptosis; VEGF-family signaling can recruit vessels; MHC loss or checkpoint ligands can blunt immunity. The same hallmark can be implemented differently in lung adenocarcinoma and in prostate adenocarcinoma.",
                ],
                "callout": {
                    "label": "needs-SME-review territory",
                    "text": "Which hallmarks dominate in a given disease setting — for example a particular prostate tumor immune microenvironment — is not something this tutorial should freeze. That is Dr. Krolewski’s lane.",
                },
            },
            {
                "title": "Drivers, passengers, and state",
                "paragraphs": [
                    "A driver alteration causally helps the clone expand. A passenger is along for the ride. Distinguishing them is a research problem, not a font choice on a slide. Transcriptional state is different again: a malignant cell can look hypoxic or interferon-stimulated without a new driver in that pathway. scRNA-seq sees state more directly than genotype unless you add DNA or mitochondrial-mutation assays.",
                    "Oncogenes (gain-of-function promoters of cancer phenotypes) and tumor suppressors (loss-of-function guardians) are still useful words. Use them with a mechanism attached: which pathway, which hallmark, which cell.",
                ],
            },
            {
                "title": "The niche is part of the disease",
                "paragraphs": [
                    "Malignant cells live with fibroblasts, endothelium, extracellular matrix, metabolites, and immune cells. That tumor microenvironment (TME) can feed growth, block drugs, and train immunity toward tolerance. Inflammation can be tumor-promoting even though adaptive immunity can also eliminate nascent clones. Both statements can be true in one patient at different times or places.",
                    "Module 4 zooms in on the immune side. Keep the rest of the niche in mind so “cancer immunity” does not collapse into T cells versus a floating cancer cell in empty space.",
                ],
            },
        ],
        "quiz": [
            {
                "id": "cb1",
                "prompt": "The most accurate one-line definition of cancer among these options is:",
                "choices": [
                    "Any cell that expresses MKI67.",
                    "A tissue in which heritable changes allow clones to expand and persist beyond normal controls, in a microenvironment they also reshape.",
                    "Infection by a virus.",
                    "High RNA-seq library size.",
                ],
                "answer_index": 1,
                "explanation": "Evolution plus niche, not a single marker gene.",
            },
            {
                "id": "cb2",
                "prompt": "Hallmarks of cancer are most useful as:",
                "choices": [
                    "A map of phenotypes and mechanism families, to organize evidence.",
                    "A proof that every tumor uses every hallmark equally.",
                    "A substitute for looking at data.",
                    "A list of FDA-approved drugs.",
                ],
                "answer_index": 0,
                "explanation": "Maps help you ask questions; they are not the answers.",
            },
            {
                "id": "cb3",
                "prompt": "A transcriptional cluster of “hypoxic tumor cells” in scRNA-seq most directly reports:",
                "choices": [
                    "A new driver mutation that has been proven in that cluster.",
                    "A cell state program — hypoxia-associated transcripts — which may or may not map one-to-one onto a clone.",
                    "The exact oxygen percentage in the droplet.",
                    "That those cells are fibroblasts.",
                ],
                "answer_index": 1,
                "explanation": "State versus genotype is the Module 2/3 junction.",
            },
            {
                "id": "cb4",
                "prompt": "Avoiding immune destruction is a hallmark. That means:",
                "choices": [
                    "Immunology is a separate subject that never touches cancer cell biology.",
                    "Selection on clones includes surviving recognition and killing by the immune system, so the next module is part of the same disease.",
                    "All tumors are equally visible to T cells.",
                    "Checkpoints do not exist.",
                ],
                "answer_index": 1,
                "explanation": "Hanahan & Weinberg already put immunity inside cancer biology.",
            },
            {
                "id": "cb5",
                "prompt": "Who should adjudicate a claim like “this prostate tumor is immunologically cold because of mechanism X”?",
                "choices": [
                    "The AI tutor, which has private access to the lab.",
                    "Dr. John Krolewski, using data and literature — the tutorial only supplies vocabulary.",
                    "Whoever first named the scRNA-seq cluster.",
                    "A random number generator.",
                ],
                "answer_index": 1,
                "explanation": "The SME owns disease-specific mechanism claims.",
            },
        ],
    },
    {
        "id": "immunity",
        "order": 4,
        "title": "Cancer immunity",
        "blurb": "Immunity can eliminate, ignore, or be blocked by a tumor. The cycle can break at more than one step.",
        "minutes": 35,
        "objectives": [
            "Walk the cancer-immunity cycle as a failure analysis, not a slogan.",
            "Place antigen presentation and checkpoints (CTLA-4, PD-1/PD-L1) on that cycle.",
            "Use hot / cold / excluded TIME language cautiously, tying it back to scRNA-seq.",
        ],
        "widget": "immunity_cycle",
        "sections": [
            {
                "title": "Recognition, not vibes",
                "paragraphs": [
                    "Adaptive anti-tumor immunity is an information problem. T cells see short peptides presented on MHC molecules, not “cancer-ness” as an abstract property. Innate cells (NK cells, macrophages, dendritic cells) use a different receptor logic — missing self, stress ligands, pattern recognition, Fc receptors — that can still decide whether adaptive immunity ever starts.",
                    "If a clone loses MHC class I, truncates the antigen-processing machinery, or never generates a visible neoantigen, T cells may have nothing to see. If antigen is present but dendritic cells do not activate, priming fails. If T cells prime but cannot enter the tumor, or enter and hit PD-1/PD-L1 or other brakes, killing fails. Different tumors break different steps.",
                ],
            },
            {
                "title": "The cancer-immunity cycle",
                "paragraphs": [
                    "Chen and Mellman described a cycle: tumor antigens are released, captured and presented (often by dendritic cells), T cells prime and expand in lymphoid tissue, they traffic to the tumor, they recognize peptide–MHC, they kill, and more antigen is released. Click each step in the diagram and ask “how could this step fail in a real tumor?”",
                    "Immune checkpoints are physiological brakes. CTLA-4 acts mainly at priming/amplification. PD-1 on T cells, engaged by PD-L1/PD-L2 in tissue, acts more at the effector end. Blocking those receptors can unleash anti-tumor T cells — and can also unleash autoimmunity. That clinical pattern is why checkpoint blockade is both a treatment class and a scientific probe of the cycle.",
                ],
                "callout": {
                    "label": "Not clinical advice",
                    "text": "This tutorial does not recommend treatments. Checkpoint blockade is taught as mechanism and as a historically important fact pattern.",
                },
            },
            {
                "title": "TIME, used as a sketch",
                "paragraphs": [
                    "People shorthand tumors as immune-hot (infiltrated, often IFN-high), immune-cold (few T cells), or excluded (T cells stuck at a margin). Those cartoons are starting sketches. Myeloid programs, stroma, endothelium, antigenicity, and prior therapy can all produce the same UMAP of “few CD8 T cells” for different reasons.",
                    "Single-cell RNA-seq is popular in this field because it can show tumor, myeloid, and lymphoid programs in one matrix. Remember Module 2: you lost space and protein unless you added assays. A “PD-L1 high” cluster is a transcript neighborhood until protein and location are measured.",
                ],
            },
            {
                "title": "Closing the four-module loop",
                "paragraphs": [
                    "You now have one chain. Information flow tells you what RNA is. scRNA-seq tells you how we measure it per cell. Cancer biology tells you why the tissue is a mixture of evolving clones and niche cells. Cancer immunity tells you that some of those niche cells are running a recognition program that the clone can evade.",
                    "Research in this folder should keep that chain visible. A figure that only shows a UMAP has not yet made a biological claim. A claim about prostate TIME, checkpoints, or antigen presentation is a draft until Dr. Krolewski reviews it. A pipeline, Docker path, or statistical choice is a draft until it would survive Dr. Carbonara’s methods questions.",
                ],
                "bullets": [
                    "Tutor answers are study aids, not SME sign-off.",
                    "Put new papers in references/ with one sentence on why they matter.",
                    "When markers conflict, abstain in public and ask in a meeting.",
                ],
            },
        ],
        "quiz": [
            {
                "id": "ci1",
                "prompt": "A cytotoxic T cell recognizes tumor primarily via:",
                "choices": [
                    "The cell’s total mRNA abundance.",
                    "Short peptides presented on MHC molecules, plus context from other receptors.",
                    "UMAP position.",
                    "The patient’s age alone.",
                ],
                "answer_index": 1,
                "explanation": "Antigen presentation is the information channel.",
            },
            {
                "id": "ci2",
                "prompt": "In the cancer-immunity cycle, PD-1 blockade is aimed mainly at which kind of failure?",
                "choices": [
                    "Failure to transcribe any genes in the tumor.",
                    "An effector-stage brake on T cells already in (or trying to act in) tissue, via PD-1 ligands.",
                    "Helicase failure during DNA replication.",
                    "Droplet doublet removal.",
                ],
                "answer_index": 1,
                "explanation": "CTLA-4 is more priming-centric; PD-1 is more effector-centric — still a teaching simplification.",
            },
            {
                "id": "ci3",
                "prompt": "Calling a tumor “immune-cold” from scRNA-seq alone is risky because:",
                "choices": [
                    "scRNA-seq always over-counts T cells.",
                    "Few T-cell barcodes can reflect biology (no infiltration), sampling, dissociation, or a spatial pattern you cannot see without location.",
                    "Cold is a formal SI unit.",
                    "MHC genes cannot be detected by RNA-seq.",
                ],
                "answer_index": 1,
                "explanation": "Hot/cold is a sketch. Mechanism still needs work — and often the SME.",
            },
            {
                "id": "ci4",
                "prompt": "Loss of MHC class I on a clone would be expected to interfere most directly with:",
                "choices": [
                    "CD8 T-cell recognition of peptide antigen.",
                    "Glycolysis in fibroblasts only.",
                    "Droplet formation in the 10x chip.",
                    "Translation of all cytokines in the body.",
                ],
                "answer_index": 0,
                "explanation": "No peptide–MHC-I, no classical CD8 TCR ligand. NK biology may change in the opposite direction — a nuance for later.",
            },
            {
                "id": "ci5",
                "prompt": "The four modules together support which research habit?",
                "choices": [
                    "Treat every cluster name as a final cell type and every tutor sentence as a citation.",
                    "Measure a noisy RNA snapshot, interpret it as state not gospel, put it in a cancer-plus-immune niche, and send mechanism claims to the SME.",
                    "Ignore immunity because hallmarks already listed it.",
                    "Skip QC because UMAP looks pretty.",
                ],
                "answer_index": 1,
                "explanation": "That is the working culture of this folder.",
            },
        ],
    },
]


def get_module(module_id: str) -> dict | None:
    for module in MODULES:
        if module["id"] == module_id:
            return module
    return None


def public_module(module: dict) -> dict:
    """Quiz without answers, for the client before submit."""
    return {
        "id": module["id"],
        "order": module["order"],
        "title": module["title"],
        "blurb": module["blurb"],
        "minutes": module["minutes"],
        "objectives": module["objectives"],
        "widget": module["widget"],
        "sections": module["sections"],
        "quiz": [
            {
                "id": item["id"],
                "prompt": item["prompt"],
                "choices": item["choices"],
            }
            for item in module["quiz"]
        ],
        "quiz_length": len(module["quiz"]),
    }


def module_summaries() -> list[dict]:
    return [
        {
            "id": module["id"],
            "order": module["order"],
            "title": module["title"],
            "blurb": module["blurb"],
            "minutes": module["minutes"],
            "quiz_length": len(module["quiz"]),
        }
        for module in MODULES
    ]
