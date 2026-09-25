# AAI Cancer Immunity — agent notes

Read [`.cursor/skills/aai-cancer-immunity/SKILL.md`](.cursor/skills/aai-cancer-immunity/SKILL.md) before editing this folder.

## People

| Person | Role |
| --- | --- |
| David Graham | Student |
| Dominic Sciarrino | Student |
| Dr. John Krolewski | Subject-matter expert (cancer biology, immunity, immunogenomics) |
| Dr. Joaquin Carbonara | Technical advisor (AI, software, data-science methods) |

## Three layers (do not mix)

| Layer | Path | Role |
| --- | --- | --- |
| Group | `docs/`, `notes/`, `references/` | Meetings, roster, drafts, starter reading |
| Tutorials | `tutorials/` | Teaching apps. Current: `tutorials/cancer_immunity/` |
| Research | `RESEARCH/` | LLM-wiki / OKF compiled memory. Ingest, query, lint. |

## Hard rules

- Biology claims are drafts until Dr. Krolewski reviews them. Do not present tutorial or note text as lab-approved science.
- Do not invent affiliations, datasets, grants, or citations.
- Never commit `.env`, API keys, or patient-level data.
- Tutorial HTML must stay WCAG 2.1 AA: `lang` on `<html>`, one `h1`, heading order, underlined links, contrast, captions on data tables.
- Do not rewrite `RESEARCH/raw/`. Compile into `RESEARCH/wiki/`.
- Meeting minutes stay in `docs/meetings/`. They become wiki pages only after ingest.
- PDFs belong in `RESEARCH/raw/`, not at the repo root.
