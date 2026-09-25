# Team

**Last updated:** 17 September 2026
**Status:** working roster for this folder; confirm emails and weekly meeting time at the first check-in

## Roster

| Person | Role | Owns in this folder |
| --- | --- | --- |
| **David Graham** | Student | First drafts: notes, tutorial content, quizzes, analyses |
| **Dominic Sciarrino** | Student | First drafts: notes, tutorial content, quizzes, analyses |
| **Dr. John Krolewski** | Subject-matter expert | Cancer cell biology, cancer immunity, immunogenomics sanity checks |
| **Dr. Joaquin Carbonara** | Technical advisor | Flask/Docker/OpenAI tutorial, research methods, GitHub |

Do not add people to this table without a named conversation.

## How work moves

1. Students draft in `notes/` or in `tutorials/cancer_immunity/content/lessons.py`.
2. Technical questions (app, Docker, git, data handling) go to Dr. Carbonara.
3. Biological claims stay marked `needs-SME-review` until Dr. Krolewski comments.
4. Meeting decisions are copied into `docs/meetings/` using [template.md](meetings/template.md).

## Authorship default

- Tutorial/code the students wrote: students lead; advisors author when they shaped the work.
- Biological framing that originates with the SME is attributed as such in notes, even if a student typed it.
- AI output is a draft. Humans named above are responsible for anything that is shared or committed.

## Data and safety

- Tutorial uses public teaching content only.
- No PHI, no identifiable patient data, no unpublished lab matrices in the GitHub tree.
- OpenAI keys stay in `.env`, never in git, screenshots, or issue trackers.
