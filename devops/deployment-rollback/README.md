# Deployment Rollback

Deployment rollback workflow with issue detection, rollback decision, previous version restoration, health verification, and post-mortem documentation.

**Domain:** devops  
**Complexity:** 3/5  
**Tags:** [deployment-rollback, version-revert, incident-response, kubernetes, helm-rollback, service-recovery]

## Lanes
- **Monitoring** - Detects issues, triggers alerts
- **On-Call Engineer** - Decides and executes rollback
- **CI/CD System** - Performs rollback deployment

## Process Flow
1. Detect deployment issue (errors, latency)
2. Assess severity and impact
3. Decide to rollback vs hotfix
4. Identify last known good version
5. Execute rollback (helm rollback, kubectl)
6. Verify health checks pass
7. Confirm error rates normalized
8. Notify stakeholders
9. Schedule post-mortem
