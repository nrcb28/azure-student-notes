# SC-100 · Ten architecture cases

[Guide](SC-100.md) · [Workbook](SC-100-workbook.md) · [Contents](README.md) · [Español](../es/SC-100-cases.md)

Original hypothetical questions for the university notes app. Explain the business requirement, control boundary, accountable owner, and acceptance evidence before opening an answer. These are offline design exercises, not official exam questions or claims of executed controls.

## 1. A dean wants the highest security score before protecting unpublished answers. How should priorities be set?

<details>
<summary>Answer</summary>

Start with the impact of disclosing answers and the paths that could expose them. Identify the data owner, current access, privileged identities, sharing routes, and available evidence. A score can highlight posture gaps but cannot assign the university's business priorities. Propose controls that reduce the critical exposure, then define acceptance through scoped access tests and reviewable configuration evidence. Record costs, residual risks, and the dean's authorised risk decision. Improving an unrelated low-impact recommendation first would require a defensible reason, not simply an easier score increase.

</details>

## 2. The API uses a private endpoint. Can the architecture declare Zero Trust complete?

<details>
<summary>Answer</summary>

Private connectivity limits a network path; it does not establish identity, application authorisation, or comprehensive isolation. Check whether public access remains enabled, how campus and recovery environments resolve DNS, and which callers can reach the endpoint. Then define user authentication, workload permissions, device requirements where applicable, and course-level access decisions. Include administration and egress paths. Acceptance should include expected allowed and denied requests and the evidence needed to distinguish network failure from permission denial. The architecture should record remaining boundaries rather than label one feature a complete strategy.

</details>

## 3. The indexer and AI agent share an administrator account. What must change in the design?

<details>
<summary>Answer</summary>

Give each workload a distinguishable identity, owner, lifecycle, and permission boundary. The indexer needs access to permitted published documents; the agent needs only the retrieval and tools required for its task. Evaluate managed identities, federation, and supported agent identity controls against those requirements. Remove dependence on a human administrator and define how access would expire or be revoked. Successful authentication must not imply broad data access or deployment rights. Acceptance evidence should show allowed operations, denied cross-course access, attributable activity, and recovery if either identity becomes unavailable.

</details>

## 4. Sentinel receives cloud alerts but no campus directory events. Is the SOC architecture adequate?

<details>
<summary>Answer</summary>

Adequacy depends on the priority threats and documented coverage. If a compromised campus directory can affect the notes service, missing directory telemetry is a material detection gap. Map that threat to expected signals, ingestion dependencies, retention, detection, triage, and containment authority. Explain how Defender XDR and Sentinel contribute without assuming either sees every asset automatically. Propose an onboarding phase or compensating monitoring with an owner and deadline. Acceptance requires usable representative events and a response walkthrough, not merely a connector's enabled status or a populated dashboard.

</details>

## 5. A sensitivity label and encrypted disks are proposed as the entire student-data strategy. What is missing?

<details>
<summary>Answer</summary>

Clarify the data locations, classification, recipients, and obligations. Check what the label actually configures and which clients and repositories honour its protections. Disk encryption protects a storage boundary but does not prevent an authorised service from reading or exporting plaintext. Consider scoped access, sharing restrictions, DLP coverage, auditing, retention, deletion, and key administration. Assign evidence and owners to each requirement, including unsupported routes. Privacy and legal stakeholders must assess obligations; neither a label nor a compliance score proves the institution meets every legal requirement.

</details>

## 6. A lecturer's uploaded document instructs the AI assistant to email all course files. Which boundary matters?

<details>
<summary>Answer</summary>

The document is untrusted retrieved content and cannot grant authority to the model or its tools. Keep retrieval constrained to the user's allowed material, restrict the agent identity, and enforce tool authorisation outside model-generated instructions. A sending tool needs a deliberate recipient and data-access policy, plus approval for consequential disclosure where required by the design. Evaluate prompt-attack detection as an additional control with supported integration and language assumptions. Use synthetic documents in the tabletop. Acceptance should demonstrate that an instruction inside a document cannot expand retrieval or tool permissions.

</details>

## 7. Nightly backups restore individual files, but the service requires a fifteen-minute RPO. Can the design pass review?

<details>
<summary>Answer</summary>

Not from that evidence. Nightly recovery points alone do not satisfy a fifteen-minute maximum data-loss requirement. Identify every data source and the recovery mechanism proposed for each, including consistency between documents and metadata. Also assess ransomware-resistant backup administration, retention, and key recovery. The two-hour application RTO needs identity, DNS, configuration, and control-plane access, not just file retrieval. The owner must either fund and validate a design meeting the objectives or approve revised requirements with explicit impact. Record expected measurements; this offline exercise proves no restore performance.

</details>

## 8. The cloud platform team applies policy to Azure. How should a departmental SaaS exception be handled?

<details>
<summary>Answer</summary>

First establish whether that policy's scope can govern the SaaS service; do not infer coverage from an Azure compliance result. Map the departmental service to the university's control requirements and assess its native controls, identity integration, data handling, audit evidence, and contract responsibilities. Use the landing-zone responsibility model to clarify platform and workload ownership without pretending every service fits the same enforcement mechanism. If a gap remains, record compensating controls, an accountable risk owner, review date, and expiry. The architecture decision should show how the exception affects the wider service.

</details>

## 9. A signed build artefact comes from a runner with broad production permissions. Is the supply chain protected?

<details>
<summary>Answer</summary>

Signing supports artefact integrity and provenance under defined trust assumptions, but it cannot make a compromised authorised build trustworthy by itself. Review source approval, dependency controls, runner isolation, signing-key access, artefact promotion, and deployment permissions. Separate test and production trust, and constrain federation claims and resource scope where applicable. Define who investigates a suspicious release and how a known-good version is restored. Acceptance evidence should connect an approved source revision to the promoted artefact and authorised deployment, while showing that an unapproved pipeline cannot modify production or signing policy.

</details>

## 10. Funding covers only one semester. How can an architect justify a phased security programme?

<details>
<summary>Answer</summary>

Rank work by business-critical exposure, dependencies, practical delivery capacity, and expected risk reduction. Protecting recovery and privileged administration may enable later migration and response improvements, but justify that sequence against the university's threats. Compare feasible options, licensing, operational burden, and disruption to teaching. For every phase, assign an owner, scoped acceptance criteria, evidence, rollback conditions, and a dated review of residual risk. Document an alternative and why it was rejected in an ADR. A funded purchase is a milestone; validated control effectiveness and authorised risk acceptance determine readiness.

</details>

[Official SC-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100)
