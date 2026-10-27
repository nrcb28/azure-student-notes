# AZ-400 · 10 cases with reasoned answers

[Guide](AZ-400.md) · [Contents](README.md)

Original study questions, not official or leaked exam items. Before revealing each answer, identify the requirement, reject an alternative, and explain how to verify your decision.

## 1. Production rebuilds the artifact after tests. What is the risk?

<details>
<summary>Reasoning</summary>

Dependencies, tools, or inputs may differ. Promoting the tested, versioned artifact reduces that gap.

</details>

## 2. A migration drops a column and deployment fails. Is image rollback enough?

<details>
<summary>Reasoning</summary>

No. Schema and data may have changed. Prepare compatibility, migration sequencing, and recovery.

</details>

## 3. A secret was in Git for minutes. What comes first?

<details>
<summary>Reasoning</summary>

Revoke or rotate it and assess exposure. Removing the commit does not invalidate copied credentials.

</details>

## 4. An external PR runs scripts on an internally connected runner. What matters?

<details>
<summary>Reasoning</summary>

Trust, isolation, permissions, persistence, and events. PR content can execute code; privileged access needs a secure design.

</details>

## 5. A canary has normal CPU but wrong results. What was missing?

<details>
<summary>Reasoning</summary>

Functional signals and promotion criteria. Infrastructure health does not prove business correctness.

</details>

## 6. A test passes on its fifth attempt. What next?

<details>
<summary>Reasoning</summary>

Investigate flakiness and retain evidence. Repeating until green does not make the system reliable.

</details>

## 7. id-token: write exists but Azure rejects login. What should be verified?

<details>
<summary>Reasoning</summary>

Issuer, subject, audience, federated trust, and configured identity; then authorisation. Workflow permission does not establish all trust.

</details>

## 8. Deployment frequency improves but recovery slows. Is that clearly better?

<details>
<summary>Reasoning</summary>

Not necessarily. Evaluate speed and stability together using consistent definitions rather than rewarding one metric.

</details>

## 9. An old cache breaks builds. What should be reviewed?

<details>
<summary>Reasoning</summary>

Keys, inputs, tool versions, and scope. A cache accelerates work; it should not replace correct sources or published artifacts.

</details>

## 10. A postmortem concludes be more careful. What is missing?

<details>
<summary>Reasoning</summary>

A concrete action, owner, deadline, and verification method. Conclusions should measurably change the system or process.

</details>

## Self-assessment

Per case: one point for the requirement, one for justified choice, and one for a verification method. Maximum 30. This independent review scale does not predict exam scores. Revisit weak sections and write a different example.
