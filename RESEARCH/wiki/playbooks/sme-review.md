---
type: Playbook
title: SME review
description: Only Dr. John Krolewski (or a human he designates) may set verified.by human on biology.
tags: [playbook, trust]
status: draft
generated: { by: agent:cursor, at: 2026-09-24T21:40:00Z }
sources:
  - id: team
    resource: raw/team.md
    title: Team roster
---

1. Student or agent leaves the page `status: draft` with `sources`.
2. [Dr. Krolewski](../people/john-krolewski.md) reads the page and the raw source.
3. He (or the agent at his instruction) adds:

```yaml
verified: { by: human:krolewski, at: YYYY-MM-DDTHH:MM:SSZ }
status: stable
```

Methods/OKF pages may be verified by [Dr. Carbonara](../people/joaquin-carbonara.md) as `human:carbonara`. Agents never self-verify.
