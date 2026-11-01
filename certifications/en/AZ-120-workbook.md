# AZ-120 · Common advanced workbook

[Guide](AZ-120.md) · [10 cases](AZ-120-cases.md) · [Contents](README.md)

Five matching units across languages. Work offline on the fictional university's purchasing and finance SAP landscape and its research-portal integration. No licence, Azure deployment, SAP execution, or production readiness is supplied or claimed. Distinguish assumptions and predicted results from observed evidence.

<a id="az-120-unit-1"></a>

## 1. Inventory responsibilities and supported capacity

Draw production and nonproduction SIDs, application servers, ASCS/ERS or SCS, HANA, shared files, identity, DNS, and interfaces. Assign infrastructure, OS, Basis, database, security, and business-validation owners. Explain why redundant application servers leave other single points of failure. Build a sizing worksheet covering relevant SAPS, memory, growth, throughput, latency, and failure headroom; leave SKU selection conditional on certification and compatibility checks.

**Scenario:** a cheaper VM matches core count but has no recorded HANA support evidence. **Evidence:** a dependency map, supported VM/OS/database/storage combination, regional quota assumptions, and licensing-review owner. **Deliverable:** an architecture decision explaining acceptance criteria and unresolved measurements. Review [compute foundations](../../en/03-compute.md).

<a id="az-120-unit-2"></a>

## 2. Design placement, network, and HANA storage

Draw supported application-to-database paths, administration, replication, backup, campus connectivity, and DNS forwarding. Separate private ExpressRoute connectivity from selected encryption controls. Compare zone isolation with PPG colocation constraints using explicit latency assumptions. Plan `/hana/data`, `/hana/log`, and `/hana/shared`, supported filesystems, disk and VM I/O ceilings, and configuration-specific cache or Write Accelerator decisions.

**Scenario:** a savepoint coincides with slow purchases, and a proposal puts an inspection appliance between SAP application and database tiers. **Evidence:** traffic paths, placement diagram, predicted latency budget, volume-role table, and required I/O observations. **Deliverable:** a supported alternative with capacity and failure-domain tradeoffs. Review [network foundations](../../en/05-networking.md).

<a id="az-120-unit-3"></a>

## 3. Separate safe failover from historical recovery

Explain HANA System Replication, supported cluster control, ASCS/SCS protection, ERS, quorum, fencing, virtual names, and load-balancer probes. Draw the single permitted writer after a network partition. Define business RPO and RTO, workload-consistent backups, usable logs, retention, and restore dependencies. Show why replication can copy an error and why an uncoordinated snapshot does not establish application consistency.

**Scenario:** the peer cannot be fenced and a finance mistake has already replicated. **Evidence:** predicted cluster decisions, fencing dependencies, authoritative-copy rule, backup/log availability, and restore validation criteria. **Deliverable:** separate HA and restore runbooks, explicitly rejecting disabled fencing as a repair and including business reconciliation after historical recovery.

<a id="az-120-unit-4"></a>

## 4. Write a migration and integration runbook

Assess source support, versions, interfaces, change rate, transfer duration, downtime, and target compatibility. Choose a supported migration approach with reasons. Define rehearsal, write freeze, final synchronization, source isolation, DNS/interface changes, technical checks, business acceptance, and reopening writes. For RISE, assign customer integration and SAP-managed responsibilities using the contract rather than assumed subscription access.

**Scenario:** users create purchase orders after cutover, then the research portal fails. **Evidence:** write-ownership timeline, queue state, interface transfer points, validation gates, and decision owners. **Deliverable:** rollback before new writes and a distinct post-write reconciliation or reverse-migration decision, including SAP escalation where the failing boundary belongs to RISE.

<a id="az-120-unit-5"></a>

## 5. Review operations and rehearse regional recovery

Review a fictional IaC change for image support, placement, storage, secret references, dependencies, and destructive differences. Stage updates with cluster-aware ordering and rollback criteria. Specify Azure Monitor collection, SAP monitoring providers, database and cluster evidence, alert owners, and retention. Recover the full service in an alternate region, including identity, network, central services, apps, data, integrations, and return-to-primary synchronization.

**Scenario:** a regional interruption occurs during purchasing while a resize proposal is pending. **Evidence:** dependency order, predicted RPO/RTO, failure capacity, replication state, business workflow checks, and ongoing compute/storage/network/monitoring cost owners. **Deliverable:** an incident tabletop and change-review record distinguishing planned checks from executed tests.

Use the six technical references in the [guide](AZ-120.md) to challenge assumptions. These original exercises select useful concepts; they do not cover every official objective or guarantee an exam result.
