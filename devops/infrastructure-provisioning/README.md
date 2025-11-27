# Infrastructure Provisioning

Infrastructure as Code provisioning workflow with Terraform plan, approval gates, state management, resource creation, and drift detection.

**Domain:** devops  
**Complexity:** 4/5  
**Tags:** [infrastructure-provisioning, terraform, iac, cloud-resources, gitops, state-management]

## Lanes
- **Developer** - Writes IaC, submits PR
- **CI/CD Pipeline** - Plans and applies changes
- **Cloud Provider** - Provisions resources

## Process Flow
1. Write infrastructure code (Terraform/Pulumi)
2. Submit pull request for review
3. CI runs terraform plan
4. Review plan output for changes
5. Approve PR and merge
6. CD runs terraform apply
7. Provision cloud resources
8. Update state file
9. Run drift detection periodically
