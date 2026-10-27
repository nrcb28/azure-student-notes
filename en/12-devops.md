# DevOps and infrastructure as code

DevOps combines development and operations practices to deliver changes reliably. Installing a pipeline tool does not establish that process by itself.

## Workflow

```text
Branch → Pull request → Checks → Test environment
       → Review → Production → Observation
```

- **Continuous integration:** integrating changes with builds and checks.
- **Continuous delivery:** keeping changes ready to deploy.
- **Continuous deployment:** automatically releasing changes that meet the conditions.
- **Artifact:** a versioned output such as a package or image.

Deploy the artifact that was tested rather than rebuilding something potentially different for production.

## Infrastructure as code

Bicep describes Azure resources declaratively. Terraform uses providers and maintains state connecting configuration to resources.

- Version changes and review differences.
- Parameterise environments, regions, and names.
- Keep secrets out of version-controlled files.
- Review the plan or what-if before applying.
- Detect manual changes that cause configuration drift.

Bicep does not maintain a state file equivalent to Terraform's. Both approaches require understanding the resources being described.

## Automation identity

OIDC supports identity federation between GitHub Actions and Azure without storing a long-lived application credential. It requires configuring an application or identity, a federated credential, Azure permissions, and workflow permissions.

Adding id-token: write to YAML is not enough: the matching trust must exist in Azure.

## Deployment and rollback

App Service slots can support testing and swaps when the plan allows them. Container Apps revisions support version management depending on configuration.

Rolling back code does not necessarily reverse a database migration. Design compatible changes and test recovery.

**Class project:** review the Bicep files, deploy to development, and validate a complete request.

**Review:** a green pipeline alone does not prove the application works for users.

---

[Contents](README.md) · [Other language](../es/12-devops.md) · [Previous](11-messaging.md) · [Next](13-laboratorios.md)
