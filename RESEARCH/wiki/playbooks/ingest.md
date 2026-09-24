---
type: Playbook
title: Ingest
description: Drop one source in raw/, compile it into wiki pages, update index and log, lint.
tags: [playbook]
status: draft
generated: { by: agent:cursor, at: 2026-09-24T21:40:00Z }
sources:
  - id: schema
    resource: AGENTS.md
    title: RESEARCH schema
---

Follow [`AGENTS.md`](../../AGENTS.md) § Ingest. One source unless asked to batch. Do not rewrite `raw/`. Do not set `verified`.
