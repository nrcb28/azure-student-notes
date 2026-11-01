# SC-300 · Access decisions and governance workbook

[Guide](SC-300.md) · [Ten cases](SC-300-cases.md) · [Contents](README.md)

Five original offline units for a fictional university notes app. Use synthetic identities and documents. Do not change tenant policies, create credentials, activate roles, or connect real telemetry. Deliverables describe expected decisions; no cloud execution is claimed.

<a id="sc-300-unit-1"></a>

## 1. Trace effective access and identity sources

Map the tenant, subscription, app, and document store. Separate directory roles, administrative-unit scope, Azure resource and data roles, and application entitlements. Include direct and group-based grant paths and identify who controls membership. For a hybrid identity, record the authoritative source and the chosen synchronisation and authentication assumptions; avoid treating synchronisation as an access grant.

**Scenario:** a student loses a direct assignment but can still read a course folder. **Evidence:** a diagram identifying two possible grant paths and the records needed to distinguish them. **Deliverable:** a six-row access-decision matrix covering student, guest, editor, administrator, indexer, and former member, with minimum scope and an expected denial for each.

<a id="sc-300-unit-2"></a>

## 2. Design authentication and Conditional Access

Specify a supported authentication method, registration route, and recovery owner. Explain phishing resistance and where a Temporary Access Pass could bootstrap an eligible user without storing a real passcode. Describe policy targets, conditions, grant and session controls, exclusions, licensing assumptions, and emergency recovery. Keep report-only evaluations separate from enforced outcomes.

**Scenario:** a visiting lecturer uses a personal device, while an editor handles unpublished solutions. **Evidence:** three expected requests with different identities, methods, devices, or resources; explain cross-tenant claim trust separately from app entitlement. **Deliverable:** a proposed policy matrix and rollout note containing pilot, review, recovery, and rollback criteria. Nothing is enabled in a real tenant.

<a id="sc-300-unit-3"></a>

## 3. Choose and constrain workload identities

Compare an app registration, its service principal, and a managed identity for the indexer. Explain delegated versus application permissions, consent, and resource scope. For a fictional external build, document the expected federation issuer, subject, and audience using invented claim values. State why successful token issuance does not establish permission to deploy.

**Scenario:** the indexer reads only published notes, while the build updates only its test application. **Evidence:** one allowed and one rejected operation per workload, plus a permission owner and review date. **Deliverable:** an identity-choice table and a federation trust sketch with no passwords, client secrets, real tokens, or deployment commands. Record unsupported assumptions as questions for the owner.

<a id="sc-300-unit-4"></a>

## 4. Build the entitlement and privilege lifecycle

Separate PIM eligibility, activation, and active duration from periodic access reviews. Propose an access package for visiting lecturers and supported lifecycle automation for joiners, movers, and leavers. Distinguish SSO federation from SCIM provisioning and explain how downstream removal would be confirmed. List feature-specific licence assumptions and owners of failed automation.

**Scenario:** a lecturer's semester ends while an administrator needs temporary maintenance access. **Evidence:** an expiry decision, a resource-owner review, a scoped activation proposal, and a downstream provisioning completion record. **Deliverable:** a governance table listing trigger, approver, entitlement, duration, review, expected removal, evidence, and exception handling. A completed review is not evidence of an activated role.

<a id="sc-300-unit-5"></a>

## 5. Explain a failure using bounded evidence

Separate user risk, sign-in risk, policy evaluation, directory changes, and provisioning failures. Choose the relevant logs and describe diagnostic routing, retention, access, and schema assumptions. Annotate the guide's hypothetical KQL query with what its aggregate can and cannot establish. Add Private Access, Internet Access, or the Microsoft traffic profile only where the resource path makes that purpose relevant.

**Scenario:** a guest cannot open a course, yet a dashboard shows no matching failures. **Evidence:** a hypothetical timeline, coverage gaps, correlation fields, and two competing explanations. **Deliverable:** a one-page diagnosis and evidence checklist connecting identity, network path, policy, application entitlement, and provisioning. Label every result as expected; no query or tenant test is executed.

[Microsoft Learn study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) · [Identity foundations](../../en/06-identity.md)
