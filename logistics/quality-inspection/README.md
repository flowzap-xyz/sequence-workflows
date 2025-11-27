# Quality Inspection

Incoming quality inspection workflow with AQL sampling, defect classification, hold/release decision, supplier notification, and quality metrics tracking.

**Domain:** logistics  
**Complexity:** 3/5  
**Tags:** [quality-inspection, incoming-inspection, aql-sampling, defect-tracking, supplier-quality, hold-release]

## Lanes
- **Receiving** - Stages items for inspection
- **Quality Inspector** - Samples and inspects items
- **Quality System** - Records results, notifies supplier

## Process Flow
1. Receive items requiring inspection
2. Determine sample size based on AQL level
3. Pull random samples for inspection
4. Inspect against quality specifications
5. Classify any defects found
6. Calculate defect rate
7. Make hold/release decision
8. Notify supplier of quality issues
9. Update supplier quality scorecard
