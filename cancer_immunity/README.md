# Cancer Immunity tutorial

Interactive tutorial for **information flow in the cell**, **single-cell RNA sequencing**, **cancer cell biology**, and **cancer immunity**.

Built to be posted on GitHub. Run it with **Flask**, **Docker**, and an **OpenAI** API key.

**Repository:** https://github.com/carbonjo/cancer_immunity

## People

| Name | Role |
| --- | --- |
| David Graham | Student |
| Dominic Sciarrino | Student |
| Dr. John Krolewski | Subject-matter expert |
| Dr. Joaquin Carbonara | Technical advisor |

Teaching material is not clinical advice. Biological claims are drafts until Dr. Krolewski reviews them. App, Docker, and methods questions go to Dr. Carbonara.

## What the tutorial is

Four modules, one argument:

1. A cell’s state is an information-processing program (DNA, RNA, protein, signaling).
2. scRNA-seq reads a noisy projection of that program, one barcode at a time.
3. Cancer is clonal evolution inside a niche, mapped by the hallmarks.
4. Immunity can clear, ignore, or be blocked by that niche; the cancer-immunity cycle names the failure points.

Each module has an interactive figure, a five-question checkpoint quiz, and an optional AI tutor. Quizzes grade **without** an API key. The tutor needs `OPENAI_API_KEY`.

## Run with Docker (recommended)

```bash
cp .env.example .env
# edit .env and set OPENAI_API_KEY=sk-...
docker compose up --build
```

Open [http://127.0.0.1:5050](http://127.0.0.1:5050).

If you skip the key, the site still runs. The tutor banner will say it is off; modules and quizzes work.

Stop with `docker compose down`.

## Run without Docker

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# set OPENAI_API_KEY in .env
flask --app app run --host 127.0.0.1 --port 5050
```

## Environment

Copy `.env.example` to `.env`. Never commit `.env`.

| Variable | Default | Meaning |
| --- | --- | --- |
| `OPENAI_API_KEY` | (empty) | Enables the in-lesson tutor |
| `OPENAI_MODEL` | `gpt-4o-mini` | Chat model |
| `SECRET_KEY` | `replace-me-in-production` | Flask secret |
| `PORT` | `5050` | Host port for Docker |

Get a key from [OpenAI API keys](https://platform.openai.com/api-keys). Keep it out of screenshots, issues, and git.

## Repository layout

| Path | What it is |
| --- | --- |
| `app.py` | Flask routes, quiz grading, OpenAI tutor |
| `content/lessons.py` | Module text and quizzes |
| `content/tutor.py` | Tutor system prompt |
| `templates/`, `static/` | Accessible HTML/CSS/JS |
| `Dockerfile`, `docker-compose.yml` | Container run |

## Tests

```bash
pip install -r requirements.txt pytest
pytest -q
```

A GitHub Actions workflow file is in `.github/workflows/tests.yml` locally. Pushing it requires a GitHub token with the `workflow` scope (`gh auth refresh -s workflow`).

## Research use of this folder

Students draft first. Mark uncertain biology `needs-SME-review`. Do not put PHI, unpublished patient data, or API keys in git.
