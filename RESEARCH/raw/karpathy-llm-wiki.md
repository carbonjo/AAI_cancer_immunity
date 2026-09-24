# LLM Wiki

Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
Author: Andrej Karpathy

A pattern for building personal knowledge bases using LLMs.

The LLM incrementally builds and maintains a persistent wiki — structured, interlinked markdown that sits between you and the raw sources. Knowledge is compiled once and kept current, not re-derived on every query.

Three layers:

1. **Raw sources** — immutable. The LLM reads; it never modifies them.
2. **The wiki** — LLM-generated markdown. You read; the LLM writes.
3. **The schema** — AGENTS.md / CLAUDE.md. Conventions and workflows.

Three operations: **ingest**, **query**, **lint**.

Two special files: **index.md** (catalog) and **log.md** (append-only chronology).

This file is a source snapshot for the RESEARCH bundle. Do not edit it in place; drop a newer snapshot if the gist changes.
