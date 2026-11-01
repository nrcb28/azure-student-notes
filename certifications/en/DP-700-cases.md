# DP-700 · Ten cases with reasoned answers

[Guide](DP-700.md) · [Workbook](DP-700-workbook.md) · [Contents](README.md) · [Español](../es/DP-700-cases.md)

Original university-data exercises, not official exam items. State your decision and evidence before opening each answer. The [guide](DP-700.md) records the official scope and source check; these cases claim neither complete coverage nor Fabric execution.

## 1. The team knows Synapse Spark. Can it assume identical Fabric defaults and deployment behaviour?

<details>
<summary>Answer</summary>

No. Familiar Spark concepts help, but Fabric is a SaaS platform with its own workspace, capacity, item, runtime, and lifecycle boundaries. Inventory dependencies, libraries, storage paths, identities, and supported configurations before adapting the notebook. Define a small synthetic enrolment workload and compare its expected output with an eventual controlled Fabric run. Verify deployment and connection behaviour separately from transformation syntax. Similar code is useful starting evidence, but it does not establish that permissions, runtime defaults, or operational responsibilities are equivalent.

</details>

## 2. A relational reporting team and a file-processing team propose the same store. What decides?

<details>
<summary>Answer</summary>

Compare the actual workload: file formats, transformation engines, relational write requirements, SQL consumption, governance, and ownership. A lakehouse is a reasonable candidate for Spark-led preparation of download files; a warehouse may fit a T-SQL-centred analytical model. They can cooperate when requirements justify it. Define the table grain and acceptable freshness before comparing performance. Do not treat the lakehouse SQL analytics endpoint as a general warehouse write surface. Record supported operations and a representative validation plan rather than choosing solely from team familiarity.

</details>

## 3. A shortcut exposes the library catalogue. Does that provide a backup and access for every analyst?

<details>
<summary>Answer</summary>

No. The shortcut references source data, so a missing target or changed source permission can affect access. It is not an independently retained recovery copy. Inspect whether the shortcut is internal or external, which identity or connection is used, and which permissions apply to the actual read route. Test a permitted analyst and a denied analyst with synthetic data. Agree on schema changes and availability with the catalogue owner. A separate retention and recovery design is needed if historical recovery is required.

</details>

## 4. A report must contain only yesterday's enrolments. The copy activity is green, but the report contains today's enrolments. Was the workflow successful?

<details>
<summary>Answer</summary>

The activity completed technically, but the business acceptance condition failed. Inspect processing-window parameters, dynamic expressions, source filters, time zones, and destination bindings. Reconcile source-window counts and selected business keys against published output before allowing downstream refresh. A pipeline should coordinate validation and publication, while a notebook or SQL transformation can implement the data rules. Record the run identifier and intended interval so the mistake can be traced. Correct the affected output with an idempotent replay rather than assuming a green status proves correctness.

</details>

## 5. A batch committed but lost its success response. How can a retry avoid duplicate enrolments?

<details>
<summary>Answer</summary>

Use a stable enrolment key and deterministic source version, deduplicate the incoming batch, and merge into the intended target state. Persist progress only after output validation and successful commitment. A retry of the same bounded source interval should find equivalent versions already applied and leave business totals unchanged. Record a batch identifier and reconciliation counts for operational diagnosis. Appending every arrival without a uniqueness rule would duplicate rows. Also consider older delayed updates and deletes: a retry strategy must preserve version ordering, not merely recognise identical payloads.

</details>

## 6. A modified-date query misses withdrawals and late corrections. What changes in the loading design?

<details>
<summary>Answer</summary>

Identify whether withdrawals physically remove rows or produce a status change. A simple query over remaining rows cannot discover physical deletions. Evaluate supported CDC with delete records, a soft-delete contract, or periodic reconciliation. For late corrections, use reliable source ordering and an overlap window with deterministic deduplication, or another supported change-tracking mechanism. Keep enough version information to reject stale updates after a delete. Test equal timestamps, delayed records, and replay. Document the source retention window so an extended outage cannot silently create an unrecoverable gap.

</details>

## 7. A download occurs at 23:59 and arrives at 00:07. Which day's count should change?

<details>
<summary>Answer</summary>

The answer follows the declared business time rule. If reports count downloads by event time, the record belongs to the earlier day's window. Define the time zone, window boundary, tolerated lateness, and whether a published result can be corrected. Processing-time grouping would place it on the arrival day and answer a different question. A streaming watermark controls late handling and retained state; a checkpoint supports recovery progress. Neither substitutes for an explicit correction policy or proves the sink cannot duplicate output after replay.

</details>

## 8. An optional column arrives with malformed dates and unknown module keys. Should schema evolution accept all rows?

<details>
<summary>Answer</summary>

Assess the optional column as a compatibility change, separately from record validity. An approved additive field does not make malformed dates or missing references acceptable. Apply explicit type and key rules, retain invalid input in a controlled quarantine with reason codes, and reconcile accepted and rejected records. An unknown module may require delayed reference resolution rather than permanent rejection. Preserve source identifiers for safe repair and replay. Check downstream contracts before publishing the new schema, and avoid putting student details into unrestricted diagnostic logs.

</details>

## 9. A report enforces row security and has a sensitivity label. Is direct file access automatically safe?

<details>
<summary>Answer</summary>

No. Identify the boundary that enforces the row restriction and examine alternative paths such as SQL queries and direct OneLake access. Workspace roles, item permissions, engine-specific rules, and file permissions must fit the required reader capability. A sensitivity label supplies governance context and supported protection behaviour; its presence alone does not prove every authorisation requirement is enforced. Test allowed module aggregates and denied student detail using representative identities. Also review export permissions and inherited broad access, which can undermine a carefully restricted report surface.

</details>

## 10. A deployed notebook is slower and reads production from test. Should capacity be increased first?

<details>
<summary>Answer</summary>

First correct the environment binding and prevent unintended publication. Inspect connection references, parameters, execution identity, and deployment support for the item and its dependencies. Git history or a successful promotion does not prove these values are correct. Then compare the same workload against a baseline: capacity contention, Spark stage skew, shuffle, file sizes, partition pruning, and source behaviour. Test one evidence-based change with correctness checks. Increase capacity when measured pressure supports that decision, rather than using scaling to hide a configuration error or inefficient data layout.

</details>
