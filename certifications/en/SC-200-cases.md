# SC-200 · 10 cases with reasoned answers

[Guide](SC-200.md) · [Workbook](SC-200-workbook.md) · [Contents](README.md)

Original study scenarios, not official exam questions. Use the fictional university notes app and synthetic records. State the requirement, reject a tempting alternative, and identify missing evidence. These are offline tabletop exercises; no tenant query, message, or response action is performed.

## 1. Microsoft 365 alerts appear in Defender XDR, but the campus firewall is absent. Does XDR already cover it?

<details>
<summary>Answer</summary>

No. Existing Microsoft 365 evidence does not establish firewall coverage. Inventory the firewall's supported export path and the required analysis, then assess an appropriate Sentinel connector and its prerequisites. Defender XDR correlation and Sentinel collection serve related purposes, but neither invents missing telemetry. I would request the expected table, schema, source identifiers, collection scope, and sample arrival times. The tabletop deliverable is a coverage map showing present and missing sources, with expected ingestion distinguished from any observations actually supplied.

</details>

## 2. A connector says Connected, yet a query returns no device rows. Should the analyst close the investigation?

<details>
<summary>Answer</summary>

No. Check device onboarding, licence and service requirements, the connector's selected event types, destination table, analyst permissions, UTC window, ingestion delay, and retention. A table may use different fields from the query's assumed schema. Connected is a configuration signal, not proof that every required event arrived. Closing the case would confuse missing visibility with benign behaviour. Record the absent evidence and ask the source owner for a bounded synthetic event sample and collection-health evidence before drawing a conclusion.

</details>

## 3. Three alerts share one campus IP address. Is that enough to merge them into one confirmed attack?

<details>
<summary>Answer</summary>

A shared IP is a lead, especially behind campus network address translation, but it does not identify one person or attacker. Compare stable account and device identifiers, message or file evidence, activity types, and UTC timing. Alerts are detections; an incident groups related evidence, and an entity is an involved object. I would propose correlation only with supporting relationships and document uncertainty. The required evidence is a timeline and entity map that also considers unrelated students sharing the same public address.

</details>

## 4. An endpoint alert involves the lecture-streaming server. May the student analyst isolate it immediately?

<details>
<summary>Answer</summary>

The alert alone does not grant containment authority. Preserve the evidence, assess current activity and likely scope, and consult the incident runbook and authorised decision maker. Isolation could interrupt teaching, so document the service impact, proposed boundary, alternatives, and recovery conditions. Waiting without escalation is also inadequate if evidence suggests an ongoing threat. In this tabletop, record the escalation and proposed action; do not execute it. Completion would require an approved action record and separate evidence confirming the intended outcome.

</details>

## 5. The guide's synthetic query contains three Denied rows. Why is its expected count two?

<details>
<summary>Answer</summary>

The dataset repeats the same `EventId` and account pair for `e1`. After the UTC time filter, `distinct EventId, Account` retains one copy of that pair plus `e2`, so aggregation expects two events for `student-a`. This conclusion depends on the stated stable-identifier assumption. Removing duplicates by account alone would collapse separate events and undercount. The Allowed event also sits at the excluded upper time boundary. This is a predicted result from reading synthetic rows, not evidence of a query run in a tenant.

</details>

## 6. Joining message and sign-in records by account doubles the result count. Did twice as many attacks occur?

<details>
<summary>Answer</summary>

Not necessarily. Several messages and several sign-ins for one account can produce multiple matching pairs. State the join kind, key uniqueness, and the relationship the analysis is trying to establish. Default `innerunique` also changes the left input by deduplicating join keys, which may discard distinctions the analyst needs. Inspect each input's cardinality and add an appropriate time relationship before interpreting the output. I would preserve source event IDs and compare expected pairings on a tiny synthetic dataset rather than equating joined rows with attacks.

</details>

## 7. A hunt finds no private-file access after a suspicious email. Can the report say the account was never compromised?

<details>
<summary>Answer</summary>

That claim is broader than the evidence. Report that the defined query found no matching available records for its population and UTC interval. Check whether application auditing was enabled, relevant devices were onboarded, records remain within retention, and the analyst can read them. Also review filters and the meaning of access events. An authorised device replacement is a competing explanation for unfamiliar-device activity. Preserve the hypothesis, query version, coverage gaps, and a follow-up question instead of treating absence of matches as proof of safety.

</details>

## 8. A bulk course import creates repeated alerts. Should all lecturer accounts be excluded from the rule?

<details>
<summary>Answer</summary>

A broad role exclusion could hide compromised lecturer activity. First identify the import's specific authorised account, workload, time pattern, and audit evidence. Compare labelled synthetic import events with concerning access to unpublished solutions. Propose a narrowly scoped exception or rule adjustment and assess both false positives and false negatives. Also review schedule overlap, lookback, grouping, and suppression before blaming the threshold. Keep the expected results and rule version in a tuning record; reduced alert volume alone does not demonstrate improved detection quality.

</details>

## 9. A playbook retry would open another ticket and restrict the same account again. What is missing?

<details>
<summary>Answer</summary>

The design needs idempotency and a clear action state model. Associate the workflow with stable incident and action identifiers, check whether the intended step already completed, and handle partial failures without blindly repeating it. Separately verify the operator's roles, Sentinel's permission to invoke the playbook, and the workflow identity's downstream scope. Disruptive restrictions need the runbook's approval and recovery path. In this offline review, simulate a duplicate trigger and a timeout on paper; do not deploy or run the playbook.

</details>

## 10. Copilot says a cloud workload alert proves student-a downloaded solutions. Is its summary sufficient evidence?

<details>
<summary>Answer</summary>

No. Trace the claim to application access records, the cloud resource ID, identity identifiers, and the UTC timeline. A workload alert or posture recommendation does not by itself prove a particular document download. Review Copilot's cited sources, available integrations, and any generated query's schema, filters, joins, and counts. Mark unsupported statements and retain the analyst's corrected conclusion. The case record should distinguish observed synthetic evidence, an inferred relationship, and missing records. A fluent summary cannot supply unavailable telemetry or authorise a response.

</details>

[Official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · [Technical sources and explanations](SC-200.md)
