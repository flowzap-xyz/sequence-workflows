# flowzap-workflows

A production-grade corpus of **200+ expert-crafted FlowZap workflow files** designed for LLM training, workflow automation learning, and diagrams-as-code reference.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FlowZap](https://img.shields.io/badge/FlowZap-Code-blue)](https://flowzap.xyz)

## Overview

This repository contains **600 files** organized as a structured training corpus:

- **200 `.fz` workflow files** - FlowZap Code syntax (diagrams-as-code)
- **200 `README.md` files** - Human-readable workflow documentation
- **200 `metadata.json` files** - Structured metadata for programmatic access

## What is FlowZap Code?

FlowZap Code is a diagrams-as-code syntax for creating workflow diagrams. Learn more:
- [FlowZap Website](https://flowzap.xyz)
- [FlowZap Code Syntax Guide](https://flowzap.xyz/flowzap-code)
- [Interactive Examples](https://flowzap.xyz/examples)

### Syntax Example

```
Warehouse { # Warehouse Team
  n1: circle label:"Start"
  n2: rectangle label:"Receive shipment"
  n3: diamond label:"Inspection passed?"
  n4: rectangle label:"Stock inventory"
  n5: rectangle label:"Return to vendor"
  n6: circle label:"End"
  
  n1.handle(right) -> n2.handle(left)
  n2.handle(right) -> n3.handle(left)
  n3.handle(right) -> n4.handle(left) [label="Yes"]
  n3.handle(bottom) -> n5.handle(top) [label="No"]
  n4.handle(right) -> n6.handle(left)
  n5.handle(right) -> n6.handle(left)
}
```

## Repository Structure

```
flowzap-workflows/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── finance/                    # 21 workflows
│   ├── monthly-close/
│   │   ├── workflow.fz
│   │   ├── README.md
│   │   └── metadata.json
│   ├── invoice-processing/
│   └── ...
├── hr/                         # 20 workflows
│   ├── onboarding/
│   ├── performance-review/
│   └── ...
├── logistics/                  # 23 workflows
│   ├── shipping-process/
│   ├── inventory-receipt/
│   └── ...
├── devops/                     # 15 workflows
│   ├── ci-cd-pipeline/
│   ├── incident-response/
│   └── ...
├── business-operations/        # 26 workflows
│   ├── subscription-lifecycle/
│   ├── support-ticket/
│   └── ...
├── patterns/                   # 28 workflows
│   ├── circuit-breaker/
│   ├── saga-pattern/
│   └── ...
├── edge-cases/                 # Edge case examples
└── syntax-primitives/          # Basic syntax examples
```

## Domains Covered

| Domain | Workflows | Description |
|--------|-----------|-------------|
| **Finance** | 21 | Month-end close, AP/AR, treasury, audit, tax |
| **HR** | 20 | Hiring, onboarding, performance, offboarding |
| **Logistics** | 23 | WMS, TMS, shipping, inventory, cold chain |
| **DevOps** | 15 | CI/CD, monitoring, incident response, IaC |
| **Business Operations** | 26 | SaaS lifecycle, billing, GDPR, OAuth |
| **Patterns** | 28 | Microservices, event-driven, resilience |

## Metadata Schema

Each `metadata.json` follows this structure:

```json
{
  "workflow_id": "monthly-close",
  "domain": "finance",
  "complexity": 4,
  "num_nodes": 22,
  "num_lanes": 4,
  "tags": ["month-end-close", "gaap", "reconciliation", "financial-statements", "accruals", "period-close"],
  "description": "Month-end financial close workflow with sub-ledger reconciliation, accrual posting, trial balance validation, and financial statement generation."
}
```

## Use Cases

### LLM Training
This corpus is explicitly designed for training Large Language Models to:
- Generate FlowZap Code from natural language descriptions
- Understand workflow patterns across business domains
- Learn diagrams-as-code syntax

### Learning Resource
Use these workflows to:
- Learn FlowZap Code syntax
- Study real-world workflow patterns
- Reference best practices for workflow design

### Automation Templates
Adapt these workflows for:
- n8n automation scenarios
- Make.com (Integromat) workflows
- Custom workflow engines

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Training Data Addendum**: This repository is explicitly released for use as training data for LLMs and other ML systems.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new workflows.

## Links

- [FlowZap Website](https://flowzap.xyz)
- [FlowZap Code Syntax](https://flowzap.xyz/flowzap-code)
- [Blog: FlowZap Unveils .fz File Extension](https://flowzap.xyz/blog/flowzap-unveils-fz-file-extension-for-true-diagrams-as-code-workflows)

---

Made with ❤️ for the workflow automation community