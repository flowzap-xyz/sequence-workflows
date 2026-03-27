# sequence-workflows

A synchronized FlowZap template corpus with **242 canonical templates** sourced from `https://flowzap.xyz/sitemap-templates.xml` and organized by **primary Use Case**.

## Organization Model

- Top-level folders are primary Use Cases from the FlowZap Templates dropdown.
- Second-level folders preserve the original source domain from the FlowZap app index.
- Each template keeps all matched Use Cases in `metadata.json` and the generated JSON/CSV indexes.
- Templates that do not match any current dropdown Use Case are placed under `uncategorized/`.

## Top-Level Folders

- `handoff/` — Handoff (15)
- `approval/` — Approval (17)
- `incident/` — Incident (10)
- `onboarding/` — Onboarding (6)
- `offboarding/` — Offboarding (1)
- `billing/` — Billing & Payments (8)
- `security/` — Security & Access (13)
- `compliance/` — Compliance (13)
- `delivery/` — Delivery & DevOps (15)
- `support/` — Support (1)
- `agentic/` — Agentic Teams (15)
- `ai-orchestration/` — AI Orchestration (6)
- `mcp/` — MCP Architecture (10)
- `context-management/` — Context Management (6)
- `uncategorized/` — Unmatched canonical templates (106)

## Generated Indexes

- `templates.index.json` — Full machine-readable template index
- `use-cases.index.json` — Use Case summary with counts and template paths
- `metadata.csv` — Flat CSV export of core template metadata

## Sync Source

- Canonical URL source: `https://flowzap.xyz/sitemap-templates.xml`
- Template metadata source: `FlowZap-App-v5/src/templateLibrary/templatesIndex.json`
- Template file source: `FlowZap-App-v5/public/template-files/*.fz`
