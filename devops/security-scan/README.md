# Security Scanning

Security scanning workflow with SAST, DAST, dependency vulnerability scanning, finding triage, and remediation tracking in CI/CD pipeline.

**Domain:** devops  
**Complexity:** 3/5  
**Tags:** [security-scanning, sast, dast, dependency-check, snyk, devsecops]

## Lanes
- **CI/CD Pipeline** - Triggers scans on code changes
- **Security Scanner** - Performs SAST/DAST/SCA
- **Security Team** - Triages and tracks findings

## Process Flow
1. Trigger scan on PR or commit
2. Run SAST (static analysis)
3. Run dependency vulnerability scan
4. Run DAST on deployed app (if applicable)
5. Aggregate findings
6. Filter false positives
7. Classify severity (critical, high, medium, low)
8. Block PR if critical findings
9. Track remediation in security dashboard
