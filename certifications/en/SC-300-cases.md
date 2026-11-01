# SC-300 · 10 cases with reasoned answers

[Guide](SC-300.md) · [Workbook](SC-300-workbook.md) · [Contents](README.md)

Original questions about a fictional university notes app, not official exam questions. Explain the access boundary, reject an unsuitable shortcut, and identify evidence. All outcomes are hypothetical; no live tenant changes or cloud execution were performed.

## 1. A departmental User Administrator cannot read a private notes container. Should we broaden the directory role?

<details>
<summary>Answer</summary>

First identify whether the failed action concerns directory administration, Azure resource management, storage data, or application permissions. A directory role scoped through an administrative unit does not grant every resource entitlement belonging to that department. Broadening it would address the wrong boundary. For this design, map the signed-in identity, requested operation, resource scope, and applicable data role or application entitlement. The evidence should explain why the specific read is allowed or denied without turning a departmental administrator into a tenant-wide administrator.

</details>

## 2. We removed a student's direct app assignment, but access remains. Does removal fail?

<details>
<summary>Answer</summary>

One removal does not establish that every grant disappeared. Inspect group-based app assignments, group membership sources, app roles, application-owned sharing, and the identity and tenant actually used. Depending on the resource, inherited assignments and existing sessions may also matter. Do not delete the account as the first diagnostic step. Produce a grant-path diagram and distinguish assignment state from the application's observed decision. A useful explanation identifies the remaining path, its owner, and the evidence needed to confirm removal at that boundary.

</details>

## 3. A partner university reports MFA success. May all its lecturers now open unpublished solutions?

<details>
<summary>Answer</summary>

No. Trusting a supported MFA claim through inbound cross-tenant settings can help satisfy a scoped authentication requirement; it does not grant access to all university resources. Examine both organisations' applicable access settings, the lecturer's resource-tenant identity, the target application, and its entitlement. Invitation restrictions and guest lifecycle also matter. I would record one permitted course and one denied unpublished solution in the matrix. The evidence must distinguish accepted authentication assurance from the separate authorisation decision for a particular document.

</details>

## 4. New editors cannot register passkeys. Should the help desk collect their passwords in a spreadsheet?

<details>
<summary>Answer</summary>

No. Design an approved bootstrap and recovery process using supported methods, potentially a Temporary Access Pass for eligible users. Check authentication-method policy scope, device support, identity verification, permitted lifetime and use, and secure delivery. A TAP is sensitive and temporary; it should not appear in the workbook or become a shared permanent credential. The deliverable describes expected registration and expiry outcomes, plus recovery ownership. Successful passkey registration still needs a separate check that the intended authentication-strength policy applies during access.

</details>

## 5. A report-only Conditional Access policy records failures. Has it protected the app by blocking those requests?

<details>
<summary>Answer</summary>

Report-only evaluation does not enforce the proposed controls. Its findings support planning, but they are not evidence that this policy blocked a request. Check targeted identities and resources, conditions, exclusions, other applicable policies, and the event's policy details. Document the expected enforced outcome separately from the observed report-only result. Before any authorised rollout elsewhere, the design should include a pilot, recovery access, rollback owner, and licensing checks. Here we only create that plan and an allowed-and-denied access matrix.

</details>

## 6. An unusual sign-in appears, while a former lecturer still has a course entitlement. Is one risk policy sufficient?

<details>
<summary>Answer</summary>

These are different decisions. Sign-in risk concerns the authentication request; user risk concerns possible compromise of the identity. Investigate detections and context before concluding that an unusual sign-in is malicious. Whether the lecturer still needs course access belongs to entitlement ownership and the leaver or access-review process. A risk policy cannot decide that business need. Keep an investigation timeline and a separate entitlement decision, with owners and expected remediation evidence. Removing obsolete access does not itself resolve a potentially compromised identity.

</details>

## 7. Our nightly indexer has a delegated permission request. Can it read every student's notes without a user?

<details>
<summary>Answer</summary>

A delegated permission depends on a signed-in user context and the relevant API's permission model. A headless workload needs an appropriate application identity and supported application permissions, or resource permissions through a managed identity. Requesting permissions is also distinct from granting consent. Compare the application object, local service principal, API, consent grants, and resource scope. Do not substitute a lecturer's password. The offline design should explain the indexer's minimum corpus, why it needs access, who approves it, and how its access is reviewed.

</details>

## 8. A federated build identity receives a token, but deployment fails. Should we create a permanent client secret?

<details>
<summary>Answer</summary>

First separate external assertion validation, Entra token issuance, and resource authorisation. Check the configured issuer, subject, and audience against the expected claims, including case, without recording live tokens. Then examine the resulting principal's minimum role and deployment scope. Token issuance does not prove permission to modify the target resource. A permanent secret would introduce credential maintenance without explaining the failure. Deliver a hypothetical claim-and-permission table containing one intended build context and one rejected context, plus the evidence needed at each boundary.

</details>

## 9. SAML SSO works, but an expired guest account remains in the learning platform. Is SSO the deprovisioning mechanism?

<details>
<summary>Answer</summary>

SSO federation and account provisioning have different jobs. SAML can support authentication while a SCIM connector separately creates, updates, or deactivates application accounts. Review assignment scope, mappings, source changes, provisioning logs, and the destination application's supported removal behaviour. Do not infer account deletion merely from an access-package expiry or successful sign-in. The governance record should name the owner of each step and distinguish removal of an Entra entitlement from the downstream account state. A failed provisioning action needs follow-up and observable completion evidence.

</details>

## 10. A reviewed administrator is PIM eligible, and a dashboard has no failures. Is maintenance access proven?

<details>
<summary>Answer</summary>

An access review can justify retaining eligibility, but activation and an active assignment remain separate. Check the exact role, scope, activation requirements, approval, duration, and relevant licensing. An empty dashboard also depends on log coverage, ingestion, retention, filters, and permissions; it does not prove successful maintenance or absence of failures. Record an expected activation and a scoped allowed operation, together with an out-of-scope denial. Keep the review decision, activation evidence, and hypothetical log analysis as distinct deliverables rather than claiming an operation was executed.

</details>

[Official guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) · [Technical sources and explanations](SC-300.md)
