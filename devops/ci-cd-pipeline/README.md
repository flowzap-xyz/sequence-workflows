# CI/CD Pipeline

Full CI/CD pipeline with code checkout, linting, unit tests, artifact building, staging deployment, smoke tests, production deployment, and automatic rollback on failure.

**Domain:** devops  
**Complexity:** 4/5  
**Tags:** [ci-cd, continuous-integration, continuous-deployment, github-actions, artifact-registry, staging, production, rollback]

## Lanes
- **Developer** - Pushes code, reviews pipeline status, merges to main
- **Continuous Integration** - Checkout, lint, test, build, push artifacts
- **Continuous Deployment** - Deploy to staging, run smoke tests, deploy to production

## Process Flow
1. Developer pushes code to repository, triggering the build
2. CI checks out source code and installs dependencies
3. Run linting checks (fail build if lint fails)
4. Run unit tests (fail build if tests fail)
5. Build artifacts and push to artifact registry
6. Pull artifacts and deploy to staging environment
7. Run staging tests to validate deployment
8. Deploy to production if staging passes
9. Run smoke tests and health checks
10. Update load balancer if healthy, rollback if not
