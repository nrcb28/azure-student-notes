# AZ-900 · 10 cases with reasoned answers

[Guide](AZ-900.md) · [Contents](README.md)

Original study questions, not official or leaked exam items. Before revealing each answer, identify the requirement, reject an alternative, and explain how to verify your decision.

## 1. An API needs processing only when a file arrives. What would you investigate first?

<details>
<summary>Reasoning</summary>

Event-triggered functions or execution, checking duration, startup, networking, and plan. A permanent VM is optional, and zero cost is not guaranteed.

</details>

## 2. A company needs to configure its own operating system. Which model fits?

<details>
<summary>Reasoning</summary>

IaaS generally provides that control. PaaS delegates more platform work and may not expose the required settings. Identify control level rather than brand.

</details>

## 3. Three instances are added and users lose sessions. What should be checked?

<details>
<summary>Reasoning</summary>

Local session state and traffic distribution. Horizontal scaling requires an application designed for multiple instances, not merely additional resources.

</details>

## 4. A Storage URL is public. Can anyone read its contents?

<details>
<summary>Reasoning</summary>

Not necessarily. Public networking and anonymous access differ; inspect authentication, authorisation, and service configuration.

</details>

## 5. How would you attribute spending to a project?

<details>
<summary>Reasoning</summary>

Use tags and cost analysis where resource and billing data support them. Cost classification is not permission assignment or an automatic consumption cap.

</details>

## 6. An authenticated user deletes someone else's documents. Must MFA have failed?

<details>
<summary>Reasoning</summary>

No. Object and operation authorisation failed. MFA does not decide which documents a user may modify.

</details>

## 7. Which service provides recommendations and which observes operations?

<details>
<summary>Reasoning</summary>

Advisor provides recommendations; Monitor offers operational observation capabilities. Recommendations do not replace actual health evidence.

</details>

## 8. An organisation has slow Internet and a large transfer. What should be compared?

<details>
<summary>Reasoning</summary>

Network transfers and device options such as Data Box where supported. Consider volume, deadline, security, and validation.

</details>

## 9. Can compliance controls exist while an app remains insecure?

<details>
<summary>Reasoning</summary>

Yes. Property checks do not prove whole-application security. Inspect permissions, logic, data, and processes as well as policies.

</details>

## 10. How would you demonstrate shared-responsibility understanding?

<details>
<summary>Reasoning</summary>

List provider and customer responsibilities for a specific workload and explain what changes across VM, PaaS, and SaaS.

</details>

## Self-assessment

Per case: one point for the requirement, one for justified choice, and one for a verification method. Maximum 30. This independent review scale does not predict exam scores. Revisit weak sections and write a different example.
