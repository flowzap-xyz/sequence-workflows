# Contributing

This repository is synchronized from the FlowZap application template library.

## Structure

- `primary-use-case/source-domain/template-slug/`
- `workflow.fz` contains the FlowZap Code source
- `metadata.json` stores machine-readable metadata including primary and secondary Use Cases
- `templates.index.json`, `use-cases.index.json`, and `metadata.csv` are generated artifacts

## Sync Expectations

- Keep the sitemap-driven template set aligned with `https://flowzap.xyz/sitemap-templates.xml`.
- Preserve one canonical template copy per slug.
- Use `primary_use_case` for folder placement and `use_cases` for the full taxonomy membership.
- Preserve `source_domain` from the app index for traceability.
