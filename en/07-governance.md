# Governance and compliance

Governance means setting rules and checking compliance. In a small project it prevents mistakes; in an organisation it lets many teams work without relying on manual configuration.

## RBAC versus Policy

- **RBAC:** who can perform an action.
- **Azure Policy:** which conditions resources must meet.

Someone may have permission to create a VM while a policy blocks deployment to an unapproved region.

Policy definitions express rules. An initiative groups related definitions. Assignments select the scope where rules apply.

## Effects

- **Audit:** reports noncompliance.
- **Deny:** blocks specified requests that violate a rule.
- **Modify:** can change supported properties.
- **DeployIfNotExists:** can deploy related resources when missing.

Modification and deployment effects require appropriate configuration and permissions. Existing resources may need a remediation task; assigning a policy does not immediately fix everything.

## Practical organisation

I would use predictable names and tags such as:

| Tag | Example |
|---|---|
| project | notes-app |
| environment | dev |
| owner | student-team |
| costCenter | training |

Tags are not automatically inherited in every situation. I would not store secrets or personal data in them.

## Security and compliance

Microsoft Defender for Cloud helps with security posture and workload protection, depending on configuration and plans. Microsoft Sentinel focuses on SIEM and SOAR capabilities. They are not interchangeable tools.

An Azure certification does not automatically make our application compliant. Data handling, permissions, processes, and applicable obligations still matter.

**Class project:** start with audit policies to understand their impact before enforcing broad denials.

**Review:** a rule restricting regions belongs in Policy, not in a tag.

## Worked example: moving from audit to compliance

A university finds resources outside approved regions. A policy with the Deny effect can block incompatible requests, but does not move existing resources.

First identify resources, owners, and justified exceptions. Plan changes and verify effects. Exemptions need reasons and review dates rather than permanent bypasses.

## Operational ownership

Every recommendation should end in a decision: fix, temporarily accept, or investigate. Findings without owners do not change risk.

A technical property check does not independently prove formal compliance across processes and data.

**Exercise:** design environment-tag and region policies. Explain scope, effect, existing resources, exceptions, and what happens when a required service exists only elsewhere.

---

[Contents](README.md) · [Other language](../es/07-governance.md) · [Previous](06-identity.md) · [Next](08-observability.md)

## Microsoft Learn expansion · policy

Remediation tasks apply modify operations or deployIfNotExists deployments to existing resources. They use the assignment's managed identity and permissions. Changing a definition does not automatically update every associated permission.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources) · [Microsoft Learn expansion](15-microsoft-learn.md#learn-policy)
