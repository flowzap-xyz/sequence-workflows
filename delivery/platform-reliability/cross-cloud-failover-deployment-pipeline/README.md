# Cross-Cloud Failover Deployment Pipeline

CI builds the container, pushes it to a cross-cloud registry, deploys to AWS, GCP and metal, health-checks every endpoint and updates mesh routing only when all are healthy.

**Template ID:** `cross-cloud-failover-deployment-pipeline`  
**Kind:** workflow  
**Source domain:** Platform Reliability  
**Primary use case:** delivery  
**Secondary use cases:** platform-reliability  
**Complexity:** 2/5  
**Nodes:** 11  
**Lanes:** 5  
**Tags:** [multi-cloud, deployment, failover, ci-cd, health-check]  
**Source path:** ``  
**Repo path:** `delivery/platform-reliability/cross-cloud-failover-deployment-pipeline`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
