---
type: Method
title: Karpathy LLM-wiki
description: Persistent compiled markdown wiki between the reader and raw sources. Not query-time RAG.
tags: [okf, methods]
status: draft
generated: { by: agent:cursor, at: 2026-09-24T21:50:00Z }
sources:
  - id: gist
    resource: raw/karpathy-llm-wiki.md
    title: Karpathy LLM Wiki gist snapshot
---

From `raw/karpathy-llm-wiki.md` (Karpathy gist snapshot). Knowledge is compiled once and kept current, not re-derived on every query.

Three layers: **raw/** (immutable; the LLM reads, never edits), **wiki/** (LLM-generated markdown; you read, the LLM writes), **schema** (`AGENTS.md`). Three operations: [ingest](../playbooks/ingest.md), [query](../playbooks/query.md), [lint](../playbooks/lint.md). Two reserved files: `index.md` (catalog) and `log.md` (newest first).

Shipped here as [OKF v0.2](okf-v0.2.md). Decision that this bundle lives in `RESEARCH/`: [kb-lives-in-research](../decisions/kb-lives-in-research.md).
