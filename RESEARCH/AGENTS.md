# RESEARCH — LLM-wiki schema (OKF v0.2)

This file is Karpathy’s **schema** layer. Follow it when ingesting, querying, or linting. Do not invent biology. Do not rewrite `raw/`.

## Layout

```
RESEARCH/
  raw/                 Immutable sources. Never edit after drop-in.
  wiki/                OKF bundle. Concept ID = path minus .md.
  AGENTS.md            This schema.
  scripts/lint.py      Health check.
```

Reserved wiki filenames: `index.md`, `log.md`. They are not concepts.

## OKF types (keep this list small)

| Type | Use |
| --- | --- |
| `Person` | Named humans on this project |
| `Concept` | Ideas (information flow, TIME, hallmarks) |
| `Paper` | A citable work |
| `Claim` | A single assertion the Critic can check |
| `Method` | How we work (llm-wiki, scRNA-seq pipeline) |
| `Playbook` | Ingest, query, lint, SME review |
| `Decision` | Dated go / no-go |

Unknown types must still render. Do not invent twenty types.

## Frontmatter

Required: `type`.  
Recommended: `title`, `description`, `tags`, `status`, `generated`, `sources`.  
Do **not** set `verified` unless a named human asked you to.

```yaml
---
type: Claim
title: Short name
description: One sentence.
tags: [scrna]
status: draft
generated: { by: agent:cursor, at: 2026-09-24T21:40:00Z }
sources:
  - id: src-id
    resource: raw/starter-reading.md
    title: Starter reading
---
```

`status`: `draft` | `stable` | `deprecated`.  
Trust tier is derived: no `verified` → unverified; `verified.by` starting `human:` → human-reviewed.

Actor strings: `agent:cursor`, `human:krolewski`, `human:carbonara`, `human:graham`, `human:sciarrino`.

## Ingest

1. Put the source in `raw/`. Never edit it after that.
2. Read `wiki/index.md`. Reuse concept IDs.
3. Extract a few concepts the source actually supports. Prefer updating existing pages.
4. Touch related Person / Concept / Claim pages and add markdown links.
5. Rebuild `wiki/index.md` (description from frontmatter; group by type).
6. Prepend `wiki/log.md` with ISO date, newest first. Also keep a Karpathy line agents can grep:

   `## [YYYY-MM-DD] ingest | Source title`

7. Run `python3 scripts/lint.py`. Fix broken links.
8. Leave biology `draft` and unverified.

One source per ingest unless the user asks to batch.

## Query

1. Read `wiki/index.md`, then the linked pages. Cite concept IDs.
2. If the wiki is thin, say so. Do not fill gaps from model memory and call them compiled.
3. File a useful answer back as a new wiki page (comparison, synthesis) and log it as `query`.

## Lint

Run `scripts/lint.py`. Also look for contradictions, stale `stable` claims, orphans, and concepts mentioned but missing a page. Suggest sources; do not fetch paywalled PDFs unless the user provides them.

## Do not

- Rewrite `raw/`.
- Mark pages `verified`.
- Put PHI, API keys, or unpublished patient matrices in this bundle.
- Quote `draft` claims as lab consensus or grant-ready science.
- Silently “fix” tutorial text when a paper disagrees — add a `Claim` flagged for SME review.
