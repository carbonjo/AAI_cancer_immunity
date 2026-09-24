---
type: Playbook
title: SME review
description: Only Dr. John Krolewski (or a human he designates) may set verified.by human on biology.
tags: [playbook, trust]
status: draft
generated: { by: agent:cursor, at: 2026-09-24T21:50:00Z }
sources:
  - id: team
    resource: raw/team.md
    title: Team roster
  - id: starter
    resource: raw/starter-reading.md
    title: Starter reading
---

1. Student or agent leaves the page `status: draft` with `sources`.
2. [Dr. Krolewski](../people/john-krolewski.md) reads the page and the raw source.
3. He (or the agent at his instruction) adds:

```yaml
verified: { by: human:krolewski, at: YYYY-MM-DDTHH:MM:SSZ }
status: stable
```

Methods/OKF pages may be verified by [Dr. Carbonara](../people/joaquin-carbonara.md) as `human:carbonara`. Agents never self-verify.

Roster claim: [needs-sme-review](../claims/needs-sme-review.md). If a paper figure disagrees with tutorial wording, [do-not-silently-fix-tutorial](../claims/do-not-silently-fix-tutorial.md).
