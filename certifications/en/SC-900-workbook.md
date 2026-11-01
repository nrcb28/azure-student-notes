# SC-900 · Decisions and evidence workbook

[Guide](SC-900.md) · [Ten cases](SC-900-cases.md) · [Contents](README.md)

Five original units to apply the same learning goals in every language. Use a fictional university and synthetic data. These are offline design exercises: no policy deployment, tenant modification, or completed Azure execution is claimed.

<a id="sc-900-unit-1"></a>

## 1. Map responsibility and trust boundaries

Draw the browser, identity provider, application, and document store. At each boundary, describe what is verified and who operates the relevant control. Separate provider platform duties from the organisation's decisions about users, sharing, configuration, and data. Explain why a campus network is not sufficient evidence that a request should be trusted.

**Scenario:** a guest must read published notes but never unpublished solutions. **Evidence:** a diagram and a table of two allowed and two denied operations, their owners, and the observations needed to verify them. **Deliverable:** one page that distinguishes expected outcomes from any results actually observed. Do not test against a real tenant for this exercise.

<a id="sc-900-unit-2"></a>

## 2. Design an access decision

Specify the identity type, target application, requested action, and minimum entitlement. Propose an authentication requirement and explain its factor categories and phishing-resistance properties. Describe which Conditional Access signals would matter and which application checks would still be necessary. Document scope, exclusions, recovery, and licensing dependencies rather than writing “enable MFA for everyone”.

**Scenario:** a visiting lecturer accesses course material from a personal device. **Evidence:** expected decisions for an allowed request, an insufficient authentication method, and a request outside the lecturer's entitlement. **Deliverable:** an access matrix with reasons. Keep it hypothetical; do not change tenant controls or assume report-only observations are enforced decisions.

<a id="sc-900-unit-3"></a>

## 3. Separate privilege, entitlement, and risk

Write three questions: who may activate a privileged role, who should retain a project entitlement, and what identity behaviour merits investigation? Match them respectively to the relevant PIM, access-review, and identity-risk concepts. Define a role scope and duration without assuming that a short-lived broad role is automatically minimal.

**Scenario:** a former project member remains in a group, while an administrator needs temporary maintenance access. **Evidence:** grant paths, a resource-owner decision, a proposed activation process, and distinct records for suspicious behaviour if present. **Deliverable:** a short runbook explaining who approves each decision and what would confirm its completion. Do not create privileged assignments as part of this workbook.

<a id="sc-900-unit-4"></a>

## 4. Plan detection and a bounded response

Choose one hypothetical attack chain involving email, identity, and a workload. List the events needed to support or reject the hypothesis. Explain where Defender XDR correlation helps and where Sentinel connectors, analysis, and response orchestration might be relevant. Mark data that is missing; an empty result does not prove an event never happened.

**Scenario:** suspicious sign-in activity follows a phishing message. **Evidence:** an event timeline, source coverage, an analyst owner, and a proposed notification before any disruptive action. **Deliverable:** a detection-and-response table with false-positive considerations and recovery steps. No telemetry ingestion, paid service activation, or automated account blocking is performed in this exercise.

<a id="sc-900-unit-5"></a>

## 5. Trace the sensitive-data lifecycle

Follow a synthetic document from creation through internal use, sharing, investigation, and eventual disposal. Distinguish classification, configured protection, DLP handling, retention, audit evidence, and eDiscovery. Record the workload and licence assumptions behind each proposed capability. A compliance score does not replace a determination of the organisation's actual obligations.

**Scenario:** a fictional solution sheet must remain private until publication, and relevant messages must be preserved for an investigation. **Evidence:** expected handling decisions, required activity records, retention assumptions, and a named owner. **Deliverable:** a lifecycle table explaining why no single label, log, or backup satisfies every requirement. Treat legal obligations as inputs supplied by an authorised owner.

[Microsoft Learn study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900)
