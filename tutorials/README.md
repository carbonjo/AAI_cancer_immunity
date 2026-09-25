# Tutorials

Teaching software for this group. Each tutorial is a **sibling folder** under `tutorials/`.

The compiled science does **not** live here. Claims, papers, and SME-verified memory live in [`../RESEARCH/`](../RESEARCH/). Lesson text may *teach* a claim; it does not *establish* it.

| Folder | What it is | Public GitHub (optional) |
| --- | --- | --- |
| [cancer_immunity/](cancer_immunity/) | Flask + Docker + OpenAI tutor: information flow → scRNA-seq → cancer cell biology → cancer immunity | https://github.com/carbonjo/cancer_immunity |

## Add another tutorial later

1. Create `tutorials/<short-name>/` with its own README, app, and `.env.example`.
2. Link it from this table.
3. Do not put meeting notes or OKF pages inside a tutorial folder.

## Git note

The team clone is **AAI_cancer_immunity**. Commit tutorial edits from the repo root so David, Dominic, John, and Joaquin all see them.

`cancer_immunity/` may still contain a nested `.git` pointing at the public tutorial repo. Prefer the parent repo for shared work. Use the nested remote only when someone is deliberately publishing that product on its own.
