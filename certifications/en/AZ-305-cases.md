# AZ-305 · 10 cases with reasoned answers

[Guide](AZ-305.md) · [Contents](README.md)

Original study questions, not official or leaked exam items. Before revealing each answer, identify the requirement, reject an alternative, and explain how to verify your decision.

## 1. A solution needs zero RPO and one-hour RTO. Are they contradictory?

<details>
<summary>Reasoning</summary>

Not inherently: data loss and recovery time differ. Validate a concrete solution against both objectives and defined failure scenarios.

</details>

## 2. An application uses JSON and complex transactions. What determines database choice?

<details>
<summary>Reasoning</summary>

Queries, relationships, transactions, and distribution. JSON transport does not mandate a document database.

</details>

## 3. A small inexperienced team requests AKS for one simple API. What should be discussed?

<details>
<summary>Reasoning</summary>

Kubernetes requirements, operations, alternatives, and total cost. Do not reject it automatically, but require a reason proportionate to complexity.

</details>

## 4. Regional replication works but data may not leave the country. What is missing?

<details>
<summary>Reasoning</summary>

Verify replicas, backups, logs, and dependency locations. Resilience does not override residency constraints.

</details>

## 5. The secondary environment lacks secrets and DNS. Is VM replication enough?

<details>
<summary>Reasoning</summary>

No. Recovery includes identity, configuration, networking, names, and dependencies. Measure the complete path.

</details>

## 6. Caching is proposed to speed reads. What new problem appears?

<details>
<summary>Reasoning</summary>

Consistency, expiry, and invalidation. Define stale-data tolerance and behaviour when the cache fails or empties.

</details>

## 7. A database migrates overnight while writes continue. What must be defined?

<details>
<summary>Reasoning</summary>

Initial transfer, supported change capture or synchronisation, cutover window, validation, and rollback. One copy is insufficient.

</details>

## 8. Historical reports slow enrolment. Which alternative should be investigated?

<details>
<summary>Reasoning</summary>

Separate analytics from transactions and inspect queries and integration. Do not scale everything without understanding the workload.

</details>

## 9. What is missing from a diagram showing only services?

<details>
<summary>Reasoning</summary>

Requirements, boundaries, identity, data, failures, operations, costs, and validation. Structure alone does not prove suitability.

</details>

## 10. Budget falls while reliability requirements remain. What is the response?

<details>
<summary>Reasoning</summary>

Compare alternatives with evidence, explain tradeoffs, and negotiate if no validated option exists. Do not promise unchanged objectives automatically.

</details>

## Self-assessment

Per case: one point for the requirement, one for justified choice, and one for a verification method. Maximum 30. This independent review scale does not predict exam scores. Revisit weak sections and write a different example.
