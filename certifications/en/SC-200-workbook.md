# SC-200 · Decisions and evidence workbook

[Guide](SC-200.md) · [Ten cases](SC-200-cases.md) · [Contents](README.md)

Five original units for a fictional university notes app. Work offline with invented records and identifiers. Label expected outcomes separately from observations supplied in the exercise. No tenant access, cloud deployment, live query, message delivery, or containment is required or claimed.

<a id="sc-200-unit-1"></a>

## 1. Map collection and access boundaries

Draw Microsoft 365, an Azure application, an on-premises server, and a campus firewall. Assign Defender XDR investigation or Sentinel collection and analysis where appropriate. For each source, specify onboarding, connector prerequisites, expected table and time column, stable identifiers, delay, retention, and a responsible owner. Separate read, incident-management, rule-authoring, and automation permissions.

**Scenario:** the firewall connector appears connected, but its required event is missing. **Evidence:** a four-source coverage table, a collection-health question, and one synthetic event with expected schema. **Deliverable:** a diagram and gap list explaining what the analyst can conclude. Include handling rules for personal data and exports; do not collect real student information.

<a id="sc-200-unit-2"></a>

## 2. Build a defensible incident timeline

Invent six records spanning an email, identity, endpoint, application, and cloud workload. Give every record a UTC event time, ingestion time, source ID, entity identifiers, and observation. Group related alerts into a proposed incident without assuming that a shared campus IP proves the relationship. Separate known scope, suspected scope, and unavailable telemetry.

**Scenario:** a suspicious message precedes an apparent private-document access. **Evidence:** the timeline, entity map, a competing explanation, and one requested missing record. **Deliverable:** a triage note with owner, priority rationale, proposed containment, authorisation requirement, service impact, and recovery condition. Mark every proposed action as unexecuted; expected confirmation is not an observed response.

<a id="sc-200-unit-3"></a>

## 3. Explain query results before trusting counts

Read the guide's fixed synthetic KQL dataset. Trace rows through the half-open UTC window, the Denied filter, deduplication, and aggregation. Explain why the expected answer is two events for `student-a`. Add a second invented table with two rows for that account and draw the pairings produced by an explicit inner join. Contrast this with left-side deduplication by default `innerunique`.

**Scenario:** a report mistakes joined rows for distinct attacks. **Evidence:** intermediate row counts, join keys, identifier assumptions, and one boundary-time example. **Deliverable:** a corrected interpretation with expected output and limitations. No query execution is claimed; optional local calculations remain distinct from tenant observations.

<a id="sc-200-unit-4"></a>

## 4. Turn a hunting hypothesis into a tuning review

Write a hypothesis linking suspicious-message receipt to unusual private-file access. Define population, UTC window, required sources, and an alternative explanation. Create four labelled benign and four concerning synthetic examples. Propose a detection and a narrow exception, then identify which examples would alert, be missed, or require more context. Explain how ASIM could normalise compatible sources and where parser mappings need validation.

**Scenario:** an authorised import resembles misuse. **Evidence:** a versioned decision table, source gaps, false-positive and false-negative analysis, and a parser mapping check. **Deliverable:** a tuning recommendation. An empty hunt and fewer alerts do not prove compromise absent or coverage complete.

<a id="sc-200-unit-5"></a>

## 5. Review an assisted response workflow

Sketch an automation rule that invokes a playbook for enrichment and requests approval before disruptive containment. Identify the operator, Sentinel invocation permission, workflow identity, and downstream scope separately. Simulate a duplicate trigger and a timeout; document identifiers and state checks that prevent duplicate tickets or unnecessary repeated restrictions. Include an owner and recovery conditions.

**Scenario:** an AI summary links a cloud alert to a student's download without an application log. **Evidence:** a claim-to-source table, corrected conclusion, approval boundary, and expected retry behaviour. **Deliverable:** a reviewed tabletop runbook. Verify Copilot suggestions against supplied records and query semantics. No notification, approval request, or real response is sent.

[Official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · [Observability foundations](../../en/08-observability.md)
