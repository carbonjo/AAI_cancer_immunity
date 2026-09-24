---
type: Method
title: Open Knowledge Format v0.2
description: Vendor-neutral markdown + YAML. Required field is type. Provenance, trust, and lifecycle are optional families.
tags: [okf, methods]
status: draft
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
generated: { by: agent:cursor, at: 2026-09-24T21:40:00Z }
sources:
  - id: spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: OKF SPEC.md
---

This `wiki/` directory is the OKF **bundle**. Concept ID = file path minus `.md`. Reserved names: `index.md`, `log.md`.

Trust tiers (derived): no `verified` → unverified; `human:…` on `verified.by` → human-reviewed. See [sme-review](../playbooks/sme-review.md).
