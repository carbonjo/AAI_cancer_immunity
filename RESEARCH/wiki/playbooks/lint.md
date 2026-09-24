---
type: Playbook
title: Lint
description: Health-check the OKF bundle for missing type, broken links, and orphans.
tags: [playbook]
status: draft
generated: { by: agent:cursor, at: 2026-09-24T21:40:00Z }
sources:
  - id: schema
    resource: AGENTS.md
    title: RESEARCH schema
---

```bash
cd RESEARCH
python3 scripts/lint.py
```

Also look by hand for contradictions and missing concept pages. Log the pass.
