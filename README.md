# sequence-workflows

A synchronized FlowZap template corpus with **356 canonical templates**, mirrored from the FlowZap template library and organized by **primary Use Case**.

## Organization Model

- Top-level folders are primary Use Cases from the FlowZap Templates dropdown.
- Second-level folders preserve the original source domain from the FlowZap app index.
- Each template keeps all matched Use Cases in `metadata.json` and the generated JSON/CSV indexes.
- Templates that do not match any current dropdown Use Case are placed under `uncategorized/`.

## Top-Level Folders

- `handoff/` — Handoff (24)
- `approval/` — Approval (22)
- `incident/` — Incident (14)
- `onboarding/` — Onboarding (9)
- `offboarding/` — Offboarding (1)
- `billing/` — Billing & Payments (11)
- `security/` — Security & Access (27)
- `compliance/` — Compliance (13)
- `delivery/` — Delivery & DevOps (23)
- `support/` — Support (1)
- `agentic/` — Agentic Teams (28)
- `ai-orchestration/` — AI Orchestration (7)
- `mcp/` — MCP Architecture (11)
- `context-management/` — Context Management (7)
- `uncategorized/` — Unmatched canonical templates (158)

## Generated Indexes

- `templates.index.json` — Full machine-readable template index
- `use-cases.index.json` — Use Case summary with counts and template paths
- `metadata.csv` — Flat CSV export of core template metadata

## Sync Source

- Template library (source of truth): `src/templateLibrary/templatesIndex.json` in the FlowZap app
- Template file source: `public/template-files/*.fz` in the FlowZap app
- Public listing check: `https://flowzap.xyz/sitemap-templates.xml` — a template missing from the sitemap is still mirrored, this list only reports the gap
