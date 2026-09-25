# AAI Cancer Immunity

Shared workspace for **David Graham**, **Dominic Sciarrino**, **Dr. John Krolewski**, and **Dr. Joaquin Carbonara**.

**This GitHub repo (the four of you):** https://github.com/carbonjo/AAI_cancer_immunity

This folder has **three layers**. Do not mix them.

| Layer | Path | What happens here |
| --- | --- | --- |
| **Group** | [`docs/`](docs/), [`notes/`](notes/), [`references/`](references/) | Meetings, roster, student drafts, starter reading. Human conversation. |
| **Tutorials** | [`tutorials/`](tutorials/) | Teaching apps. First one is the Flask + Docker cancer-immunity tutorial. More tutorials go here as siblings. |
| **Research** | [`RESEARCH/`](RESEARCH/) | Karpathy LLM-wiki compiled as OKF v0.2. **This is where research memory lives.** Ingest sources, query the wiki, lint claims. |

```
AAI_cancer_immunity/          ← clone this repo
  docs/                       group operations
  notes/                      student drafts (before ingest)
  references/                 human reading list
  tutorials/
    cancer_immunity/          interactive tutorial
  RESEARCH/                   OKF wiki (raw/ + wiki/)
```

## Who writes where

- **Meetings and decisions for the group** → `docs/meetings/` (copy the template).
- **A student idea that is not yet wiki** → `notes/YYYY-MM-DD-short-slug.md`.
- **A paper or PDF the wiki should know** → drop it in `RESEARCH/raw/`, then ingest. Do not leave extra PDFs at the repo root.
- **Tutorial code or lesson text** → `tutorials/cancer_immunity/`.
- **A claim, concept, or paper page** → `RESEARCH/wiki/` (the agent compiles this; humans curate).

Biology stays a draft until Dr. Krolewski reviews it. Methods, Docker, and git go to Dr. Carbonara.

## Run the cancer-immunity tutorial

```bash
cd tutorials/cancer_immunity
cp .env.example .env
# set OPENAI_API_KEY
docker compose up --build
```

Open [http://127.0.0.1:5050](http://127.0.0.1:5050). Details: [`tutorials/cancer_immunity/README.md`](tutorials/cancer_immunity/README.md).

That tutorial also has a public product repo: https://github.com/carbonjo/cancer_immunity. **Team work is this repo.** Commit from the `AAI_cancer_immunity` root so the other three people see it.

## Research (OKF)

Read [`RESEARCH/README.md`](RESEARCH/README.md) and [`RESEARCH/wiki/index.md`](RESEARCH/wiki/index.md). Lint with `python3 RESEARCH/scripts/lint.py`.
