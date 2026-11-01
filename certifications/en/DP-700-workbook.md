# DP-700 · Offline data-engineering workbook

[Guide](DP-700.md) · [Ten cases](DP-700-cases.md) · [Contents](README.md) · [Español](../es/DP-700-workbook.md)

Five units use synthetic university data. They require no account, paid capacity, or Fabric execution. Keep the same deliverables across language editions. Label reasoned outputs **EXPECTED**, local observations **OBSERVED**, and unperformed platform checks **NOT EXECUTED**. Source scope and reference-check limitations are in the [guide](DP-700.md).

<a id="dp-700-unit-1"></a>

## 1. Draw the platform and ownership map

Explain how tenant, capacity, workspace, item, OneLake location, and execution engine differ. Draw the university enrolment source, raw download files, curated tables, library catalogue shortcut, and analytical consumer. Decide where a lakehouse and a warehouse could fit, with one concrete reason for each choice. State each table's grain.

**Scenario:** the library controls the shortcut target and changes its access policy. **Evidence:** record target ownership, internal or external authentication assumptions, required permissions, schema contract, and the effect of target deletion. **Deliverable:** a dependency diagram and access matrix. Include a separate historical-retention requirement; the shortcut does not itself satisfy backup or recovery needs.

<a id="dp-700-unit-2"></a>

## 2. Reconcile an incremental change log

Use this complete synthetic log; `version` is authoritative source ordering and `key` identifies an enrolment. Start with an empty target. Keep a versioned tombstone for deletes. Reduce each key to its greatest version, collapse identical duplicates, then merge only newer versions. Conflicting payloads at the same version require quarantine.

| key | version | operation | module |
|---|---:|---|---|
| E1 | 1 | upsert | CS101 |
| E2 | 1 | upsert | DB201 |
| E1 | 2 | upsert | AI301 |
| E1 | 2 | upsert | AI301 |
| E2 | 2 | delete | DB201 |
| E2 | 1 | upsert | DB201 |

**Scenario:** replay the log after losing the success response. **Expected evidence:** E1 remains active in AI301 at version 2; E2 is deleted at version 2. Active count is 1 after both runs. **Deliverable:** intermediate state and progress-commit rules; explain why the late E2 version 1 cannot resurrect it.

<a id="dp-700-unit-3"></a>

## 3. Specify quality and event-time rules

Design a download record with event identifier, module, event time, arrival time, and schema version. Define null, type, allowed-value, and duplicate rules. Explain the difference between approving an optional new field and accepting invalid records. Quarantine must retain a repairable identifier and reason while restricting access to sensitive content.

**Scenario:** an event occurs at 23:59 UTC and arrives at 00:07 UTC the next day; the stated lateness allowance is ten minutes. **Expected evidence:** its event-time day is the earlier day. Acceptance also requires knowing the engine's watermark at arrival; an eight-minute wall-clock delay alone does not prove acceptance. **Deliverable:** acceptance and correction rules, reconciliation, window boundaries, checkpoint purpose, and behaviour beyond the allowance.

<a id="dp-700-unit-4"></a>

## 4. Design a controlled deployment

Describe a pipeline that copies a bounded enrolment interval, invokes validation and transformation, and publishes only accepted results. Choose SQL, PySpark, or KQL for each relevant transformation and justify the engine. Distinguish Git versioning of supported definitions from deployment of supported content and from data movement.

**Scenario:** the test notebook still points to the production lakehouse. **Evidence:** inspect item references, connection binding, runtime identity, parameters, environment dependencies, and schedules before execution. **Deliverable:** a development/test/production configuration table, allowed and denied reader tests across report and file routes, and rollback steps. Explain why a sensitivity label alone does not implement the complete permission design.

<a id="dp-700-unit-5"></a>

## 5. Diagnose a fictional slow run

Create a baseline for run duration, input and output counts, rejects, freshness, and capacity utilisation. Add an incident where the same input volume takes twice as long. Include three competing explanations: a skewed Spark join, many small files, and concurrent capacity demand. State which evidence would support or reject each explanation; inspect partition pruning and query behaviour where relevant.

**Scenario:** a retry follows a partial write. **Evidence:** use unit 2's version rules to show whether business state changes. **Deliverable:** one reversible tuning experiment with acceptance thresholds and correctness reconciliation. Mark all Fabric timings NOT EXECUTED; synthetic reasoning cannot establish actual throughput, recovery duration, or successful cloud deployment.
