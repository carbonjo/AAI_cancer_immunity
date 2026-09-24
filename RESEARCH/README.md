# RESEARCH knowledge base

Karpathy **LLM-wiki** compiled as an **OKF v0.2** bundle.

| Layer | Path | Who writes it |
| --- | --- | --- |
| Raw sources | [`raw/`](raw/) | Humans. Immutable. The agent reads; it never rewrites. |
| Wiki (OKF bundle) | [`wiki/`](wiki/) | The agent. Interlinked markdown with YAML frontmatter. |
| Schema | [`AGENTS.md`](AGENTS.md) | Humans + agent, co-evolved. Ingest / query / lint rules. |

Pattern: [karpathy/llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)  
Standard: [OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)

This is **compiled research memory**, not RAG. Read [`wiki/index.md`](wiki/index.md) first. Biology stays `status: draft` until [Dr. John Krolewski](wiki/people/john-krolewski.md) marks `verified.by: human:…`.

## Daily use

**Ingest** one source at a time: drop it in `raw/`, then ask the agent to ingest.  
**Query** against `wiki/`, not against a pile of PDFs. File good answers back as pages.  
**Lint:** `python3 scripts/lint.py`

## People

David Graham and Dominic Sciarrino (students). Dr. John Krolewski (SME). Dr. Joaquin Carbonara (technical advisor / schema).
