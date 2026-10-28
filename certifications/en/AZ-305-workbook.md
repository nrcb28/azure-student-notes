# AZ-305 · Shared advanced workbook

[←](README.md) · [Common study core](../../en/16-common-core.md) · [Advanced labs](../../en/17-advanced-labs.md)

This block has the same objectives, scenarios, and deliverables in all eight languages. Equivalence is checked by learning units and evidence, not word count. Earlier guides remain complementary explanations.

<a id="az-305-unit-1"></a>

## 1. Translate needs into constraints

Define users, growth, residency, privacy, performance, RTO, RPO, budget, and operational skills. Separate verified requirements from assumptions. Always available needs defined operations and a measurement window.

**Case:** five faculties share networking but own private data. **Evidence:** administrative and data boundaries, owners, and a requirement requiring separation. Do not select enterprise architecture simply for its size.

<a id="az-305-unit-2"></a>

## 2. Design data and state

Compare queries, transactions, compatibility, consistency, and recovery. JSON does not determine an engine. Read scaling does not necessarily increase write capacity. Define application, session, and document state.

**Case:** a cache accelerates reads but serves outdated permissions. **Evidence:** invalidation, expiry, and cache-failure behaviour. Explain which information must not rely on a stale copy.

<a id="az-305-unit-3"></a>

## 3. Design complete recovery

Assign RTO and RPO per service and data set. Include capacity, credentials, permissions, DNS, and configuration. Replication can propagate logical damage. Compare active-active and active-passive against cost and complexity.

**Case:** Key Vault returns without required integrations. **Evidence:** recovery order and an authorised-consumer test. Document dependencies not restored automatically and an isolated rehearsal method.

<a id="az-305-unit-4"></a>

## 4. Choose execution and communication

Compare VMs, PaaS, containers, and batch against control, duration, and operations. Queues decouple work but add states and duplicates. Design timeouts, bounded retries, and idempotency before increasing consumers.

**Case:** lost save response and repeated message. **Evidence:** stable identifier, retry limit, and partial-processing handling. Explain when a cluster is necessary and when a simpler platform suffices.

<a id="az-305-unit-5"></a>

## 5. Document migration decisions

Inventory dependencies and utilisation, validate compatibility, run a pilot, and plan initial transfer, subsequent changes, cutover, and rollback. Define integrity evidence and source retirement. Moving a VM without required files is incomplete migration.

**Final submission:** two ADRs, networking and recovery design, and risk table. Each decision includes a reasonable alternative, consequence, test, and review condition. Reassess when budget or residency changes.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305) · [AZ-305](AZ-305.md)
