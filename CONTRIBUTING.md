# Contributing to flowzap-workflows

Thank you for your interest in contributing to the FlowZap workflows corpus! This document provides guidelines for adding new workflows or improving existing ones.

## Workflow Structure

Each workflow must include three files in its own directory:

```
domain/workflow-name/
├── workflow.fz      # FlowZap Code file
├── README.md        # Human-readable documentation
└── metadata.json    # Structured metadata
```

## FlowZap Code Syntax Rules

### Lane Definition
```
LaneName { # Display Name
  // nodes and edges
}
```

### Node Types
- `circle` - Start/End nodes
- `rectangle` - Process/Action nodes
- `diamond` - Decision nodes (must have 2-3 outcomes)

### Node Syntax
```
nodeId: nodeType label:"Node Label"
```

### Edge Syntax
```
n1.handle(right) -> n2.handle(left)
n1.handle(bottom) -> OtherLane.n3.handle(top) [label="Edge Label"]
```

### Handle Positions
- `top`, `bottom`, `left`, `right`

## Quality Guidelines

### Do's
- ✅ Use realistic, domain-specific terminology
- ✅ Include 2-3 outcomes for diamond (decision) nodes
- ✅ Use unique node IDs within the workflow
- ✅ Include cross-lane edges for multi-lane workflows
- ✅ Add meaningful edge labels for decision branches
- ✅ Keep workflows between 7-25 nodes

### Don'ts
- ❌ Reuse node IDs across lanes
- ❌ Create diamond nodes with only 1 outcome
- ❌ Use generic labels like "Step 1", "Process"
- ❌ Omit lane prefixes on cross-lane edges
- ❌ Create overly complex workflows (>30 nodes)

## Metadata Schema

```json
{
  "workflow_id": "kebab-case-id",
  "domain": "domain-name",
  "complexity": 3,
  "num_nodes": 15,
  "num_lanes": 3,
  "tags": ["tag1", "tag2", "tag3", "tag4", "tag5", "tag6"],
  "description": "One-sentence description of the workflow."
}
```

### Complexity Scale
- **1** - Simple (5-7 nodes, 1 lane, no decisions)
- **2** - Basic (7-10 nodes, 1-2 lanes, 1 decision)
- **3** - Moderate (10-15 nodes, 2-3 lanes, 2-3 decisions)
- **4** - Complex (15-20 nodes, 3-4 lanes, multiple decisions)
- **5** - Advanced (20+ nodes, 4+ lanes, complex branching)

## README Template

```markdown
# Workflow Title

One-sentence description matching metadata.

**Domain:** domain-name  
**Complexity:** X/5  
**Tags:** [tag1, tag2, tag3, tag4, tag5, tag6]

## Lanes
- **Lane Name** - Role description
- **Lane Name** - Role description

## Process Flow
1. First step
2. Second step
...
9. Final step
```

## Submitting Contributions

1. Fork the repository
2. Create a new branch for your workflow
3. Add your workflow files following the structure above
4. Ensure all three files are present and valid
5. Submit a pull request with a clear description

## Validation Checklist

Before submitting, verify:

- [ ] `workflow.fz` parses without errors
- [ ] All node IDs are unique
- [ ] Diamond nodes have 2-3 labeled outcomes
- [ ] Cross-lane edges use `Lane.nodeId` syntax
- [ ] `metadata.json` is valid JSON
- [ ] `num_nodes` and `num_lanes` match the `.fz` file
- [ ] `README.md` follows the template
- [ ] Tags are relevant and kebab-case

## Questions?

- Visit [flowzap.xyz](https://flowzap.xyz) for syntax documentation
- Check [examples](https://flowzap.xyz/examples) for reference workflows
- Open an issue for questions or suggestions

---

Thank you for helping grow the FlowZap ecosystem!
