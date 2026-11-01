# SC-100 · Security architecture workbook

[Guide](SC-100.md) · [Ten cases](SC-100-cases.md) · [Contents](README.md) · [Español](../es/SC-100-workbook.md)

Five original offline units for the fictional university notes service. Use invented assets, identities, incidents, and evidence. Produce architecture proposals and tabletop outcomes; do not change tenants, run attacks, deploy resources, or connect live telemetry. No cloud execution or control effectiveness is claimed.

<a id="sc-100-unit-1"></a>

## 1. Establish criticality and control coverage

**Scenario:** the university adds unpublished assessment answers to an app previously holding public notes. Identify critical operations, data owners, likely threats, and business impacts. Distinguish MCRA capability mapping, MCSB control requirements, CAF platform responsibilities, and Well-Architected workload review. Make assumptions explicit instead of inventing a complete inventory.

**Evidence:** a hypothetical asset diagram, three prioritised risks, current control boundaries, and missing information. Include one requirement that cannot be assessed through an Azure Policy result alone.

**Deliverable:** a coverage table containing requirement, control, scope, owner, evidence, gap, and acceptance criterion. Add a short ADR comparing two options and naming the owner authorised to accept residual risk.

<a id="sc-100-unit-2"></a>

## 2. Bound identity, network, and privilege

**Scenario:** campus users, visiting lecturers, administrators, a deployment pipeline, and an AI agent access different parts of the notes service. Draw identity, application, network, and administrative boundaries across campus and clouds. Specify minimum permissions, privileged activation, recovery access, and credential or federation ownership. Check feature and licensing assumptions for proposed agent controls.

**Evidence:** six expected allow or denial decisions, private DNS dependencies, public-access assumptions, and an explanation of how authorisation survives a reachable network path.

**Deliverable:** a trust-boundary diagram and access matrix with owner, scope, lifecycle, logging, and failure behaviour. Include a denied agent tool action and a recovery administrator path. Keep all identities and requests fictional.

<a id="sc-100-unit-3"></a>

## 3. Connect detection to authorised response

**Scenario:** suspicious campus identity activity coincides with unusual document downloads. Define the SOC capabilities needed across identity, endpoint, application, cloud, and SaaS. Map two priority threat paths to relevant MITRE ATT&CK techniques, expected telemetry, correlation, triage, and containment. Explain the responsibilities of Sentinel and Defender XDR without assuming complete visibility.

**Evidence:** a synthetic timeline showing event sources, ingestion delay, retention assumptions, a missing signal, and competing explanations. Identify who can disable an identity or interrupt an examination server.

**Deliverable:** a detection-coverage matrix and response-authority table with escalation, approval, rollback, and evidence preservation. Mark every detection and response as proposed, with acceptance evidence required before operational use.

<a id="sc-100-unit-4"></a>

## 4. Protect data and the software and AI lifecycle

**Scenario:** a new AI assistant retrieves course documents and a build pipeline deploys its API. Classify the information and map label, encryption, DLP, retention, and application-access boundaries. State where controls lack support. Threat-model dependencies, build identities, artefact promotion, document prompt injection, and tool access.

**Evidence:** one synthetic benign retrieval, one document carrying an untrusted instruction, and a fictional unapproved build. Record expected retrieval and tool denials rather than generating exploit instructions or running tests.

**Deliverable:** a data-control matrix and lifecycle review showing owner, scope, provenance, permissions, approval, and acceptance evidence. Explain why detection, encryption, and benchmark mappings each leave separate risks requiring assessment.

<a id="sc-100-unit-5"></a>

## 5. Rehearse recovery and sequence the programme

**Scenario:** ransomware affects the primary document store and a privileged account. Use exercise requirements of two-hour application RTO and fifteen-minute RPO. Trace identity, control-plane access, DNS, keys, configuration, metadata, files, and deployment dependencies. Compare protected recovery points with replication; consider corruption and compromised backup administration.

**Evidence:** a tabletop restore order, hypothetical recovery timestamps, consistency checks, and a dependency that prevents the application from serving authorised reads even after files return. Label measurements as assumed.

**Deliverable:** a recovery acceptance plan and a three-phase roadmap constrained by one semester's funding. Include owners, estimated effort, prerequisites, rollback criteria, expiring exceptions, and business approval of remaining risk. No actual restoration or recovery objective is validated.

[Official SC-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100) · [ADR template](ADR-template.md)
