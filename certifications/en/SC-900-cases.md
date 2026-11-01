# SC-900 · 10 cases with reasoned answers

[Guide](SC-900.md) · [Workbook](SC-900-workbook.md) · [Contents](README.md)

Original study scenarios, not official exam questions. Identify the requirement, reject an alternative, and state what evidence you would need. All examples are hypothetical; no tenant changes or cloud tests were performed.

## 1. The notes app moved to a managed service. Can the team stop reviewing document permissions?

<details>
<summary>Reasoning</summary>

No. The provider operates parts of the platform, while our organisation still determines appropriate access to its data. I would map the service model and separate platform operations from identity, sharing, and application configuration. A provider compliance statement does not prove that our unpublished documents are private. The useful evidence would include the configured sharing scope and a test of the intended allowed and denied operations, performed only in an authorised test environment.

</details>

## 2. A student signs in successfully but cannot open one course's private folder. Is authentication broken?

<details>
<summary>Reasoning</summary>

Not necessarily. Authentication can succeed while authorisation correctly refuses access to a particular resource. Check which identity actually signed in, its group membership, the folder's required permission, and any applicable policy. Giving the student an administrative role would bypass the diagnosis and exceed the need. In the design exercise, record the expected access decision and the evidence that would distinguish an authentication error from an application or resource-permission denial.

</details>

## 3. A team proposes a password followed by another password as MFA. What is missing?

<details>
<summary>Reasoning</summary>

Both secrets belong to the knowledge category, so using two does not establish different authentication factors. Choose a supported method and policy that meet the required factor or authentication-strength conditions. Also consider phishing resistance, registration, device compatibility, and recovery. A screenshot of a registration page does not prove enforcement. I would describe an expected sign-in that requires the configured method and a negative case where an insufficient method cannot satisfy the requirement.

</details>

## 4. A downloaded document has the expected hash. Does that prove who uploaded it or keep it secret?

<details>
<summary>Reasoning</summary>

No. Comparing a suitable digest helps check whether content matches the expected reference. It does not encrypt the file or establish the reference's trusted origin. Confidentiality requires appropriate access and, where needed, encryption; origin assurance needs a trusted mechanism appropriate to the workflow, such as a verified signature. First explain where the expected hash came from. If an attacker can replace both file and reference, a matching comparison provides much weaker assurance than the team assumes.

</details>

## 5. One Conditional Access policy requires MFA for the finance app. Are all university applications now covered?

<details>
<summary>Reasoning</summary>

The conclusion exceeds the policy scope. Review targeted identities, applications, conditions, exclusions, and grant controls. The finance rule may be correct while other applications remain outside it. Application permissions still apply after the access decision. I would prepare a matrix of expected outcomes for different users and applications, including administrator recovery and dependencies, before any authorised rollout. Report-only analysis can inform that review; its observations are not the same as an enforced block.

</details>

## 6. An administrator is eligible for a privileged role but cannot yet perform the operation. Is PIM failing?

<details>
<summary>Reasoning</summary>

Eligibility can require activation before privileged permissions become usable. Check the intended role and scope, its activation requirements, duration, approval state, and actual active assignment. Do not permanently assign a broader role merely to make the error disappear. PIM changes when privileges are available; it does not make an inappropriate role minimal. The useful evidence is the approved activation and a scoped operation using the expected identity, not just the presence of an eligible assignment.

</details>

## 7. A former project member still has access. Should the team choose an access review or treat this as an ID Protection finding?

<details>
<summary>Reasoning</summary>

The immediate question is whether an existing entitlement remains justified, which fits an access review and the organisation's joiner, mover, and leaver process. ID Protection concerns identity-risk signals and cannot decide every business need for a project folder. Investigate suspicious behaviour separately if there is evidence. Identify the resource owner, the grant path, and whether removal would affect other projects. Record the access decision and the evidence required to confirm that the obsolete entitlement has been removed.

</details>

## 8. A malicious email and an endpoint alert might be related, but the endpoint sends no security telemetry. What is the first gap?

<details>
<summary>Reasoning</summary>

Correlation requires relevant source data. Check the supported product, licence, onboarding state, identity mapping, and whether events reach the investigation platform. Defender XDR cannot reconstruct all missing endpoint evidence just because another alert exists. Sentinel can add analysis across connected sources, but it also needs ingestion and useful rules. I would document which events are present, what is absent, and a narrow hypothesis to test before claiming that a dashboard represents the entire attack.

</details>

## 9. A document has a Confidential label but can still be shared externally. Does the label prove a product fault?

<details>
<summary>Reasoning</summary>

The label's name does not establish its configured protection or the handling rule applied to that sharing route. Check the label settings, supported workload, publication and scope, and relevant DLP policy conditions and actions. A classification-only label can be valid without blocking sharing. Define the intended allowed and blocked cases before investigating. Use synthetic content in an authorised test; do not distribute real confidential data merely to demonstrate whether a policy works.

</details>

## 10. An investigation needs last month's activity and preserved messages. Is an audit log equivalent to retention or backup?

<details>
<summary>Reasoning</summary>

These capabilities serve different purposes. Audit provides activity evidence within configured availability and retention. Content retention governs keeping or deleting information, while eDiscovery can help locate and preserve relevant material for an investigation. A backup addresses recovery needs and is not automatically provided by those investigation tools. Determine the data sources, dates, permissions, retention and hold requirements, and responsible owner. Do not promise evidence that was never collected or content already outside the applicable retention period.

</details>

[Official guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) · [Technical sources and explanations](SC-900.md)
