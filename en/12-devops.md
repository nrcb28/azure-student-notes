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

## Worked example: rollback does not recover service

New code removes a column, then fails. Returning to the previous image does not recreate lost data or expected schema.

A compatible strategy adds first, migrates later, and removes structures after dependencies disappear. Test coexistence between versions and retain recovery options.

## Chain of trust

Pipeline code is sensitive too. Review who changes it, its permissions, and PR-controlled inputs. Persistent self-hosted runners can retain files or credentials between runs.

Promoting an identified artifact reduces test-to-production differences. Mutable tags and unpinned tools hinder reproduction.

**Exercise:** define delivery with a meaningful test, versioned artifact, test environment, production authorisation, and rollback condition. Link results to the source commit.

Run python tools/check_docs.py from the repository root to verify documentation locally.

---

[Contents](README.md) · [Other language](../es/12-devops.md) · [Previous](11-messaging.md) · [Next](13-laboratorios.md)

## Microsoft Learn expansion · whatif

What-if predicts changes without applying them. It has permission requirements and analytical limits; dependencies or expressions can prevent evaluation of part of a deployment. Incomplete output does not establish that no changes exist.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if) · [Microsoft Learn expansion](15-microsoft-learn.md#learn-whatif)

## Microsoft Learn expansion · slots

A deployment slot has its own hostname and runs an application. Copying settings does not clone content, private networking, or every dependency. Swaps include preparation and warm-up steps.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) · [Microsoft Learn expansion](15-microsoft-learn.md#learn-slots)

## Microsoft Learn expansion · checks

Azure Pipelines resource owners administer approvals and checks outside pipeline YAML. A stage must satisfy checks on its resources before starting. Author-controlled conditions are not equivalent separation of responsibility.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops) · [Microsoft Learn expansion](15-microsoft-learn.md#learn-checks)
