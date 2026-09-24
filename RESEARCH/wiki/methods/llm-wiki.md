---
type: Method
title: Karpathy LLM-wiki
description: Persistent compiled markdown wiki between the reader and raw sources. Not query-time RAG.
tags: [okf, methods]
status: draft
generated: { by: agent:cursor, at: 2026-09-24T21:40:00Z }
sources:
  - id: gist
    resource: raw/karpathy-llm-wiki.md
    title: Karpathy LLM Wiki gist snapshot
---

Three layers: `raw/`, `wiki/`, schema ([`AGENTS.md`](../../AGENTS.md)). Three operations: [ingest](../playbooks/ingest.md), [query](../playbooks/query.md), [lint](../playbooks/lint.md).

Shipped here as [OKF v0.2](okf-v0.2.md).
