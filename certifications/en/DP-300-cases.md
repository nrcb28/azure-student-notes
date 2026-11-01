# DP-300 · 10 cases with reasoned answers

[Guide](DP-300.md) · [Workbook](DP-300-workbook.md) · [Contents](README.md)

Original exercises, not official exam items. Before opening an answer, identify the constraint, propose a decision, and describe the evidence you would collect. These cases do not claim Azure execution or complete exam coverage.

## 1. An application needs a supported OS-level extension. Can SQL Database be chosen just because it runs T-SQL?

<details>
<summary>Reasoning</summary>

No. The OS requirement changes the hosting boundary. Check whether the extension is essential and whether a supported managed-service alternative exists. If direct OS control remains necessary, evaluate SQL Server on a VM and include patching, backup, monitoring, and availability responsibilities. Compatibility assessment should cover dependencies outside database objects as well as T-SQL. Verify the actual application requirement before selecting a platform; familiarity with SQL syntax does not establish deployment compatibility.

</details>

## 2. Data migration finishes successfully. Is it safe to reopen writes immediately?

<details>
<summary>Reasoning</summary>

A completed transfer is only one checkpoint. Validate the intended final data state, important business totals, permissions, application paths, and scheduled tasks. Establish when source writes stopped and whether remaining changes were applied. Name the destination as authoritative before reopening traffic. A rollback plan must address destination writes created after cutover; reconnecting to the source could discard them. Use an explicit go/no-go checklist and record which checks were observed rather than assumed.

</details>

## 3. An app resolves the private SQL address and connects, but SELECT is denied. Should networking be opened further?

<details>
<summary>Reasoning</summary>

The successful connection and denied statement point to database authorisation rather than a general network outage. Confirm the authenticated principal, database, object, and operation. Check the applicable database permissions and grant the minimum required capability through the chosen access model. An Azure Contributor assignment does not automatically supply table-level access. Opening the public endpoint would change exposure without supplying the missing permission. Repeat the same application operation with the same identity to verify the diagnosis.

</details>

## 4. A requirement says database administrators must not see selected cleartext values. Is TDE alone enough?

<details>
<summary>Reasoning</summary>

TDE protects database files at rest; it does not by itself prevent an authorised query from returning cleartext. Examine a design such as Always Encrypted with supported clients and keys held outside the database administrator's access boundary. Check required query operations, application compatibility, key recovery, and operational ownership. Dynamic masking is not an equivalent confidentiality boundary. Validate the threat model with a permitted synthetic-data test rather than treating every feature containing the word encryption as interchangeable.

</details>

## 5. One query becomes slower after a release while overall CPU is normal. What evidence helps first?

<details>
<summary>Reasoning</summary>

Identify the query and compare its plans and runtime behaviour over matching periods using available Query Store history. Check application parameters, reads, waits, blocking, and recent schema or statistics changes. Normal aggregate CPU does not establish that a particular transaction is healthy. Form a specific hypothesis before changing service size. If testing a previous plan, define success criteria and a reversal path, then monitor representative traffic; a single fast execution is weak evidence of a durable improvement.

</details>

## 6. A new index speeds reads but imports become much slower. Was the index necessarily a success?

<details>
<summary>Reasoning</summary>

No. An index is maintained during data changes, so its benefit must be assessed against the whole workload. Compare representative read and write latency, throughput, storage, and execution plans before and after the change. Check whether the index overlaps existing ones and whether a narrower or differently ordered definition would serve the requirement. Record an acceptance threshold for imports as well as lookups. Avoid retaining a change solely because the demonstration query became faster.

</details>

## 7. A long transaction blocks short lookups. Should every blocked session be killed?

<details>
<summary>Reasoning</summary>

Find the blocking chain and the transaction holding the relevant locks before deciding what to interrupt. A blocked session is often a symptom rather than the source. Identify the work, transaction age, owner, and consequence of rollback. Killing a transaction may require substantial rollback time and can affect application correctness. In a controlled investigation, consider shorter transactions or a suitable isolation strategy after understanding consistency requirements. Record the evidence and incident decision rather than running an indiscriminate termination script.

</details>

## 8. A SQL Agent job must move to Azure SQL Database. Can its schedule simply be copied?

<details>
<summary>Reasoning</summary>

SQL Agent is not available in Azure SQL Database. Classify the task: supported T-SQL work across databases may fit Elastic Jobs, while a workflow involving external services may need orchestration. Assess dependencies, identity, target discovery, retries, and notifications instead of copying only a time expression. A repeated task should not duplicate business output after an uncertain response. Test the replacement on isolated synthetic data and compare both the execution record and the resulting business state.

</details>

## 9. An accidental DELETE reaches the secondary database. Has replication failed?

<details>
<summary>Reasoning</summary>

Replication may be doing exactly what it was configured to do: carrying a valid committed change to another copy. Availability and historical recovery solve different problems. Determine the incident time and available retained recovery points, then plan restoration to an isolated database before the unwanted change. Validate missing and later legitimate records before choosing how to restore service. Do not assume replacing everything with an old state is acceptable; the recovery decision must account for valid writes made since then.

</details>

## 10. The database has failed over, but the notes app still fails. Is the RTO target met?

<details>
<summary>Reasoning</summary>

Not if the target concerns restoration of the user-facing service. Verify the supported application endpoint, client DNS, reconnect behaviour, identities, dependencies, and scheduled operations on the current primary. Run a functional check with synthetic records and measure elapsed recovery against the defined starting event. Record any data loss against RPO separately. Before failback, establish the authoritative copy and synchronisation plan. A healthy database status alone cannot prove that the app or its recovery objectives have been restored.

</details>

## Self-assessment and sources

For each case: identify the requirement, justify a decision, and name a verification step. This is an independent review method, not an official exam score or pass prediction.

[Official guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300) · [Technical references and explanations](DP-300.md)
