---
name: aai-cancer-immunity
description: >-
  Research workspace for AAI cancer immunity (Fall 2026): students David Graham
  and Dominic Sciarrino, SME Dr. John Krolewski, technical advisor Dr. Joaquin
  Carbonara. Use when working in AAI_cancer_immunity or when the user mentions
  information flow in the cell, scRNA-seq, cancer cell biology, cancer immunity,
  the Flask/Docker tutorial, or this team's notes, meetings, or GitHub repo.
---

# AAI cancer immunity

This folder is a **student research workspace** plus a **public interactive tutorial**.
The tutorial teaches four linked topics. Research notes capture what the team actually
decides. Do not mix the two: tutorial prose is teaching material; `notes/` is work product.

## People (do not invent titles)

| Person | Role | What they own |
| --- | --- | --- |
| **David Graham** | Student | First drafts of notes, tutorial edits, analyses |
| **Dominic Sciarrino** | Student | First drafts of notes, tutorial edits, analyses |
| **Dr. John Krolewski** | Subject-matter expert | Biological truth, cancer/immune framing, what not to overclaim |
| **Dr. Joaquin Carbonara** | Technical advisor | AI/software design, reproducibility, GitHub/Docker, methods |

If a task needs a biology judgment, stop and flag it for Dr. Krolewski rather than filling the gap. If it needs an architecture or tooling judgment, flag Dr. Carbonara.

Details: [people.md](people.md). Topic map: [topics.md](topics.md).

## Sources of truth (read, do not invent)

| Need | File |
| --- | --- |
| Public repo story, how to run the app | `cancer_immunity/README.md` |
| Agent constraints | `AGENTS.md` |
| Team and working agreements | `docs/team.md` |
| Why the four topics are sequenced this way | `docs/learning-goals.md` |
| Meeting notes | `docs/meetings/` (copy `template.md`) |
| Working notes | `notes/` |
| Compiled research wiki (OKF / LLM-wiki) | `RESEARCH/wiki/index.md` |
| Wiki schema (ingest / query / lint) | `RESEARCH/AGENTS.md` |
| Landmark readings | `references/starter-reading.md` |
| Lesson and quiz content | `cancer_immunity/content/lessons.py` |
| App routes and OpenAI tutor | `cancer_immunity/app.py` |

Do not dump these files into chat. Cite paths and change the files.

## Pedagogical arc (keep this order)

Students learn the four topics as **one argument**, not four disconnected units:

1. **Information flow in the cell** — why mRNA is a useful (incomplete) readout of cell state.
2. **Single-cell RNA sequencing** — how that readout is measured, and where it lies.
3. **Cancer cell biology** — what goes wrong in the malignant cell and its niche.
4. **Cancer immunity** — how the immune system sees, fails to see, or is blocked from seeing tumor.

When adding tutorial pages, quizzes, or tutor prompts, preserve this arc. New content should say which module it belongs to and what it prepares the next module to do.

## Research workflow

```
Task progress:
- [ ] Name the artifact (note, tutorial edit, figure, meeting recap)
- [ ] Students draft first
- [ ] Separate facts / claims / open questions
- [ ] Methods/code reviewed with Dr. Carbonara
- [ ] Biology reviewed with Dr. Krolewski
- [ ] Only then treat it as team-approved
```

**Writing rules**

- Label uncertain biology as `needs-SME-review`.
- Do not invent papers, GEO accessions, grants, or clinical recommendations.
- Prefer a short claim with a citation file in `references/` over a long uncited essay.
- AI-generated text is a draft. Named humans are responsible for every sentence that leaves the folder.
- No PHI, no identifiable patient data, no unpublished lab data in the GitHub tutorial.

## Tutorial engineering

The GitHub artifact is the nested repo **`cancer_immunity/`**: a **Flask** app in **Docker** that uses an **OpenAI** key for the tutor.

| Piece | Where |
| --- | --- |
| Lessons / quizzes | `cancer_immunity/content/lessons.py` |
| Tutor system prompt | `cancer_immunity/content/tutor.py` |
| Routes | `cancer_immunity/app.py` |
| Accessible UI | `cancer_immunity/templates/`, `cancer_immunity/static/` |
| Run locally | `cd cancer_immunity && docker compose up --build` |
| Secrets | `cancer_immunity/.env` from `.env.example` — never commit |

**When editing the app**

1. Change lesson text in `cancer_immunity/content/lessons.py`, not by hard-coding paragraphs in templates.
2. Keep quizzes gradable **without** an API key. The tutor is optional.
3. Follow WCAG 2.1 AA / Ally HTML: `lang="en"`, one `h1`, no heading skips, data tables with `<th scope="col">` and captions, underlined links, contrast on `#1a1a1a` / `#ffffff`, visible `:focus`.
4. Do not put the OpenAI key in client JavaScript, images, or README examples.
5. Default model is `gpt-4o-mini` via `OPENAI_MODEL`. Do not bake a second provider in unless asked.
6. After UI changes, run the app and click the affected module, quiz, and tutor path.

## Do not

- Treat tutorial copy as Dr. Krolewski-approved biology.
- Add a fifth teaching topic without updating `docs/learning-goals.md` and the home page.
- Commit `.env`, keys, `data/progress.json` with real student chats, or large raw count matrices.
- Give clinical advice in the tutor prompt or lesson text.
- Copy biology encyclopedias into this skill.
