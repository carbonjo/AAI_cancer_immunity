# AAI Cancer Immunity

Research workspace for students **David Graham** and **Dominic Sciarrino**, SME **Dr. John Krolewski**, and technical advisor **Dr. Joaquin Carbonara**.

The public interactive tutorial lives in **[cancer_immunity/](cancer_immunity/)** as its own GitHub repository: https://github.com/carbonjo/cancer_immunity

## Folder map

| Path | What it is |
| --- | --- |
| [cancer_immunity/](cancer_immunity/) | Flask + Docker + OpenAI tutorial (GitHub repo) |
| [docs/](docs/) | Team, learning goals, meeting notes |
| [notes/](notes/) | Student research drafts |
| [references/](references/) | Starter reading |
| [.cursor/skills/aai-cancer-immunity/](.cursor/skills/aai-cancer-immunity/) | Cursor skill for this workspace |

## Run the tutorial

```bash
cd cancer_immunity
cp .env.example .env
# set OPENAI_API_KEY
docker compose up --build
```

Open [http://127.0.0.1:5050](http://127.0.0.1:5050). Details are in `cancer_immunity/README.md`.
