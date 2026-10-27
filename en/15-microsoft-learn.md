# Practical Microsoft Learn deep dive

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

Reviewed on 27 October 2026. These are rewritten explanations of official documentation with original university-app scenarios. Examples propose checks; they have not been deployed in Azure. Linked references explain requirements and future changes.

<a id="learn-sas"></a>

## 1. Identity-backed SAS

A Blob user delegation SAS is signed using a delegation key obtained through Entra ID. Issuing one requires permission to obtain that key; possessing a blob URL does not grant that permission. Design the signature and access constraints together.

**Case:** a student needs a PDF briefly. Restrict resource, read access, and lifetime. Keep the URL out of logs and screenshots. Investigate expiry, permissions, and networking separately. Before issuance, decide how exposure will be handled and which revocation mechanisms this SAS type supports.

[Microsoft Learn · Storage: user delegation SAS](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

<a id="learn-dns"></a>

## 2. Private DNS: follow the name

Clients must resolve the service name to the private endpoint address. Creating a private interface does not configure every resolver. Recommended zones depend on the service; indiscriminately replacing an entire public zone can break resolution.

**Case:** a VM works but the university network fails. Compare answers, zone links, forwarding, and routes from each origin. Retain the service hostname rather than hard-coding an IP. Correct private resolution still grants no data permissions.

[Microsoft Learn · Private endpoint DNS](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

<a id="learn-policy"></a>

## 3. Remediation differs from evaluation

Remediation tasks apply modify operations or deployIfNotExists deployments to existing resources. They use the assignment's managed identity and permissions. Changing a definition does not automatically update every associated permission.

**Case:** old resources remain noncompliant. Check effect, scope, identity, and roles before remediating a pilot group. Record outcomes by resource. Deny does not automatically transform arbitrary old resources into compliant ones.

[Microsoft Learn · Policy remediation](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

<a id="learn-dcr"></a>

## 4. DCRs: decide what arrives

Data collection rules describe collection and routing in supported scenarios. Transformations can filter or modify data before its destination. Signals do not all use the same pipeline; DCRs are not a universal replacement for diagnostic settings.

**Case:** VM events are missing. Check agent, rule association, source, flow, destination, and schema before writing an alert. Collecting everything can increase cost and expose data. Removing useful fields can also remove evidence needed for investigation.

[Microsoft Learn · Azure Monitor data collection rules](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview)

<a id="learn-whatif"></a>

## 5. What-if: inspect analytical limits

What-if predicts changes without applying them. It has permission requirements and analytical limits; dependencies or expressions can prevent evaluation of part of a deployment. Incomplete output does not establish that no changes exist.

**Case:** output shows Ignore or an unevaluated module. Read diagnostics and isolate the module rather than treating it as NoChange. Distinguish local compilation, remote validation, prediction, and post-deployment testing. Approval must consider what was not checked.

[Microsoft Learn · Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

<a id="learn-slots"></a>

## 6. Slots are live applications

A deployment slot has its own hostname and runs an application. Copying settings does not clone content, private networking, or every dependency. Swaps include preparation and warm-up steps.

**Case:** staging sends real emails. Inspect connections, slot-specific settings, identity, and startup jobs before swapping. Zero user traffic does not stop background processes. Swapping back does not automatically undo destructive database migrations.

[Microsoft Learn · App Service deployment slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)

<a id="learn-landing"></a>

## 7. Landing zones: platform and workload

Landing zones organise identity, connectivity, management, and governance foundations for workloads. Platform and application teams can have different responsibilities. Accelerators provide starting points, not replacements for organisational requirements.

**Case:** five faculties share networking but own separate apps. Define owners, permissions, subscription boundaries, policies, and costs. Do not deploy a complete enterprise architecture for a small lab merely because a template exists. Document what is shared and isolated.

[Microsoft Learn · Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)

<a id="learn-checks"></a>

## 8. Checks: ownership of releases

Azure Pipelines resource owners administer approvals and checks outside pipeline YAML. A stage must satisfy checks on its resources before starting. Author-controlled conditions are not equivalent separation of responsibility.

**Case:** production needs independent review and a time window. Define the protected resource, reviewers, timeout, and rejection handling. Test changed-code and expired-check scenarios. A green pipeline does not grant access to every service connection.

[Microsoft Learn · Azure Pipelines approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops)

---

[Source register](../LEARN-SOURCES.md) · [Attribution](../ATTRIBUTION.md)
