---
type: Decision
title: Three-layer layout for the shared GitHub repo
description: Group ops, tutorials, and RESEARCH stay separate. Dated 2026-09-25.
tags: [decision, layout]
status: draft
generated: { by: agent:cursor, at: 2026-09-25T11:28:00Z }
sources:
  - id: team
    resource: raw/team.md
    title: Team roster
---

The GitHub repo shared by David Graham, Dominic Sciarrino, Dr. John Krolewski, and Dr. Joaquin Carbonara is the parent folder **AAI_cancer_immunity**.

Three layers:

1. **Group** — `docs/`, `notes/`, `references/`. Meetings, roster, student drafts, starter reading.
2. **Tutorials** — `tutorials/`. Teaching apps. First sibling is `tutorials/cancer_immunity/`. Later tutorials are more siblings, not new top-level folders.
3. **Research** — `RESEARCH/`. Karpathy LLM-wiki compiled as OKF v0.2. This is where research memory is ingested, queried, and linted.

Do not put minutes in `RESEARCH/wiki/`. Do not put claims in `docs/meetings/`. Do not treat tutorial copy as SME-verified biology. Related: [kb-lives-in-research](kb-lives-in-research.md), [do-not-silently-fix-tutorial](../claims/do-not-silently-fix-tutorial.md).
