# AZ-104 · 10 cases with reasoned answers

[Guide](AZ-104.md) · [Contents](README.md)

Original study questions, not official or leaked exam items. Before revealing each answer, identify the requirement, reject an alternative, and explain how to verify your decision.

## 1. Reader is removed from a resource but read access remains. What next?

<details>
<summary>Reasoning</summary>

Inspect inherited assignments, groups, actual identity, and propagation. Granting another role does not remove existing access.

</details>

## 2. An administrator creates Storage but receives 403 listing blobs. What should be checked?

<details>
<summary>Reasoning</summary>

Authentication method, data role, scope, and service access controls. Management Contributor does not guarantee data access.

</details>

## 3. A VNet-integrated web app remains publicly accessible. Is that contradictory?

<details>
<summary>Reasoning</summary>

No. App Service VNet integration supports outbound access. Review inbound access, private endpoints, and restrictions separately.

</details>

## 4. All load balancer backends are unhealthy. What should be checked?

<details>
<summary>Reasoning</summary>

Probe port and expected response, listening process, rules, and configured destination. Existing backends are not necessarily healthy.

</details>

## 5. A peers with B and B with C, but A cannot reach C. Why?

<details>
<summary>Reasoning</summary>

Peering is not automatically transitive. Design supported connectivity or transit, routes, and security rather than random permission changes.

</details>

## 6. Bicep compiles but Azure denies deployment. What next?

<details>
<summary>Reasoning</summary>

Check policies, permissions, quotas, names, parameters, and availability. Local compilation does not verify every remote control.

</details>

## 7. A backup succeeds. Can we guarantee a thirty-minute RTO?

<details>
<summary>Reasoning</summary>

Not without measuring restoration and dependencies. Recover the service rather than merely proving that a copy exists.

</details>

## 8. DNS still returns a public IP after creating a private endpoint. What next?

<details>
<summary>Reasoning</summary>

Inspect private zones, links, forwarding, and client resolution. Endpoint creation does not automatically configure every consumer.

</details>

## 9. A stopped VM still costs money. What should be distinguished?

<details>
<summary>Reasoning</summary>

Stopped versus deallocated states and charges for disks and associated resources. Verify state and components before considering cleanup complete.

</details>

## 10. A policy fixes new resources but not old ones. Why might this happen?

<details>
<summary>Reasoning</summary>

Effects, scope, evaluation, and remediation of existing resources differ. Not every policy modifies or automatically remediates resources.

</details>

## Self-assessment

Per case: one point for the requirement, one for justified choice, and one for a verification method. Maximum 30. This independent review scale does not predict exam scores. Revisit weak sections and write a different example.
