# DP-300 · Shared operational workbook

[Guide](DP-300.md) · [Ten cases](DP-300-cases.md) · [Contents](README.md)

Five units with matching objectives and evidence across the eight language editions. Complete the design exercises without Azure if needed. Describe expected behaviour separately from anything actually observed. No Azure execution or full exam coverage is claimed.

<a id="dp-300-unit-1"></a>

## 1. Defend the platform and migration choice

Write a requirements table for the notes app: necessary database features, OS access, instance dependencies, acceptable write interruption, maintenance ownership, and recovery targets. Compare SQL Database, Managed Instance, and SQL Server on a VM against those requirements rather than awarding points for familiar names.

**Case:** an existing scheduled task depends on an OS tool. **Evidence:** identify whether that dependency remains necessary, a supported target or redesign, and a compatibility check. **Deliverable:** a migration sequence with initial transfer, write freeze, validation, cutover, rollback ownership, and a plan for writes made after cutover. A completed copy is not the acceptance test.

<a id="dp-300-unit-2"></a>

## 2. Separate access and confidentiality boundaries

Draw the route from an application identity to a permitted operation on a table. Mark name resolution, network access, authentication, database principal, and object permissions. Separate application, deployment, and emergency administration responsibilities. State what data may appear in queries, logs, exports, and backups.

**Case:** a private connection works but the app cannot read its table. **Evidence:** the actual identity, database, object, and denied operation; do not broaden the public network as a substitute for diagnosis. **Deliverable:** a minimal permission design and a comparison of transport encryption, TDE, Always Encrypted, and masking against a specific confidentiality requirement. Include key recovery and ownership.

<a id="dp-300-unit-3"></a>

## 3. Diagnose a measured regression

Invent two comparable workload windows for a document-permission query, including duration, reads, CPU, concurrency, and plan identity. Write a hypothesis linking the change to evidence, then name an observation that would disprove it. Include blocking and transaction duration alongside available Query Store history; neither a normal platform metric nor one expensive-looking plan operator establishes the cause alone.

**Case:** a new index improves reads and slows imports. **Evidence:** before-and-after results for both operations under representative load. **Deliverable:** one reversible tuning experiment, acceptance thresholds, rollback steps, and the limits of the evidence. Do not propose shrinking or killing every session as routine maintenance.

<a id="dp-300-unit-4"></a>

## 4. Make automation observable and repeatable

Classify a nightly task by its work and target platform. Compare SQL Agent for supported SQL Server or Managed Instance workloads with Elastic Jobs for SQL Database T-SQL tasks. Specify identity, target set, schedule, timeout, retry budget, and failure notification. External dependencies may require a broader orchestrator.

**Case:** a task commits its output but loses the success response. **Evidence:** explain how rerunning avoids duplicate business results and how an operator confirms completion. **Deliverable:** a state table for pending, running, completed, and uncertain work, plus a synthetic-data test plan. A successful scheduler invocation must not be confused with a verified business outcome.

<a id="dp-300-unit-5"></a>

## 5. Recover data and the complete service

Define separate incidents for accidental deletion and a regional outage. Choose retained recovery states and availability mechanisms for the problem each solves. State RPO and RTO in terms of the notes app, then identify the permissions, destination capacity, endpoint, DNS, authentication, and dependencies needed to restore it. Replication can carry an unwanted committed change.

**Case:** the new primary is healthy but users cannot download notes. **Evidence:** a functional check and a timed sequence that includes reconnection. **Deliverable:** an isolated restore-validation plan, an authoritative-copy decision before failback, and retained-data cleanup ownership. Label proposed timings EXPECTED until observed in a suitable environment; a tabletop exercise does not measure Azure recovery.

[Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300) · [Guide and technical sources](DP-300.md)
