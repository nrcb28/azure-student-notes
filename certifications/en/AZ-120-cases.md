# AZ-120 · 10 cases with reasoned answers

[Guide](AZ-120.md) · [Workbook](AZ-120-workbook.md) · [Contents](README.md)

Original university-enterprise scenarios, not official exam questions. Explain the decision and evidence before opening each answer. All proposed checks are offline design work; no Azure or SAP execution is claimed.

## 1. The university adds two application servers but keeps one ASCS VM and one HANA VM. Has it removed the important single points of failure?

<details>
<summary>Answer</summary>

No. Application-server redundancy does not protect the central services or database. Inventory each SID and distinguish ASCS, ERS, application instances, HANA, shared files, and their dependencies. Propose supported HA designs for central services and the database, with explicit ownership and client reconnection paths. Evidence should include a dependency diagram and the predicted effect of losing each component. Confirm application capacity after a failure as well. Counting VMs cannot demonstrate that a purchasing transaction survives the loss of its coordination or data service.

</details>

## 2. A cheaper VM has the same core count as the proposed HANA VM. Is that enough evidence to substitute it?

<details>
<summary>Answer</summary>

No. Check SAP HANA certification for the precise VM type, workload, OS release, database version, and deployment model. Compare measured memory demand, growth, relevant SAPS requirements for application tiers, storage throughput, log latency, and network limits. Also verify regional capacity and quotas. Evidence is a supported-combination record and a sizing worksheet with failure headroom, rather than a CPU comparison. A lower infrastructure estimate is not a supportability decision, and these study notes cannot establish the university's SAP licensing rights or sufficient production capacity.

</details>

## 3. The campus network team says ExpressRoute makes every SAP connection encrypted. Should the architecture record accept that claim?

<details>
<summary>Answer</summary>

No. Private connectivity and encryption are separate properties. Draw the campus-to-Azure path, provider handoff, Azure routing, application endpoints, and any selected encryption boundary. Specify supported application encryption or another appropriate encryption arrangement where policy requires it, and verify the exact service capabilities. Also document DNS resolution, authentication dependencies, route resilience, and permitted flows. Evidence should identify which traffic is encrypted, where protection begins and ends, and how configuration would be checked. A private circuit alone does not prove end-to-end confidentiality for every protocol.

</details>

## 4. A student places both HA nodes in one PPG and claims this also protects them from a zone outage. What must change in the reasoning?

<details>
<summary>Answer</summary>

Separate colocation for latency from isolation for resilience. A PPG constrains physical proximity and does not provide cross-zone failure isolation. Choose supported availability placement for the recovery requirement, then evaluate actual inter-node latency and replication behaviour. If PPGs are justified, apply them within the appropriate placement constraints and document allocation limitations. Evidence should include the failure-domain diagram, measured or explicitly assumed latency, remaining capacity, and takeover sequence. Neither a PPG nor availability zones by themselves configure a safe SAP cluster or database failover.

</details>

## 5. HANA has plenty of free disk space, but purchasing slows during savepoints. Should the team only add disk capacity?

<details>
<summary>Answer</summary>

Investigate data and log throughput, latency, queueing, and the VM's aggregate I/O ceiling. Savepoint traffic can contend with log writes even when free capacity is high. Review the supported storage layout, filesystem, disk configuration, shared-volume demand, and workload timing before selecting a change. Caching or Write Accelerator must follow the exact volume and storage guidance, not a universal performance recipe. Evidence is a correlated workload and I/O timeline plus a proposed supported configuration. Label measurements as required evidence until an authorized test actually supplies them.

</details>

## 6. A cluster cannot fence its peer after a communication fault. Would disabling fencing restore a safe service?

<details>
<summary>Answer</summary>

No. Removing fencing can allow conflicting primaries and damage data integrity. Preserve evidence and follow the incident procedure while investigating quorum, node communication, fence-agent permissions and connectivity, or the selected supported SBD configuration. Confirm that the allegedly failed node cannot continue as an independent writer before takeover. Evidence should include cluster state, timestamps, fencing results, replication state, and an identified authoritative primary. The corrective design restores supported isolation and decision-making. Making cluster resources appear started is insufficient evidence that the SAP service is safe to accept writes.

</details>

## 7. A mistaken finance update has reached both HANA replicas. Why might yesterday's protected backup still matter?

<details>
<summary>Answer</summary>

Replication preserves availability but can copy logical mistakes. A protected backup and usable log chain can support recovery to an acceptable point before the error, subject to the chosen supported restore process. Establish the business-approved RPO, restoration dependencies, retention, and any legitimate later transactions requiring reconciliation. Confirm application consistency; a generic VM snapshot is not automatically sufficient. Evidence should include a recovery-point selection, backup and log availability, isolated restore plan, database checks, and business validation. Successful replication alone cannot recover historical correctness after both copies receive the same bad change.

</details>

## 8. Cutover passes basic checks, then users enter new purchase orders. Can rollback simply point DNS back at the unchanged source?

<details>
<summary>Answer</summary>

That would abandon or fork the new transactions. The runbook needs a separate decision once target writes begin: freeze writes again, identify the authoritative dataset, preserve new transactions, and evaluate supported reconciliation or reverse migration. Include business approval, interface queues, final synchronization, source isolation, and validation before reopening either side. Evidence is a timeline of write ownership and a documented data-handling decision, not just DNS instructions. Rehearsal should distinguish rollback before reopening writes from recovery afterward, with clear deadlines and operators responsible for each gate.

</details>

## 9. The research portal cannot reach SAP RISE. Should its operator edit NSGs inside SAP's subscription using the university's Azure role?

<details>
<summary>Answer</summary>

First respect the contractual responsibility matrix. SAP manages the RISE landscape in its own Azure environment; a university subscription role does not grant control over those resources. Trace the portal's DNS, routes, peering or connectivity, firewall rules, identity, and agreed SAP interface, assigning each check to the correct owner. Coordinate SAP-side changes and escalation through SAP. Evidence should include the failing transfer point and both parties' responsibilities. RISE does not eliminate customer responsibility for its own integration services, security configuration, or network path to an available interface.

</details>

## 10. The DR region has a current database copy and running VMs, but purchasing remains unavailable. What else must the tabletop validate?

<details>
<summary>Answer</summary>

Validate central services, application startup order, identity, DNS, virtual names, routes, secrets, shared files, integration endpoints, and enough supported capacity. Compare the usable recovery point and predicted restoration time with business RPO and RTO. Prevent the original primary from accepting independent writes. Define a successful purchasing workflow and interface exchange as acceptance checks, followed by a controlled return-to-primary plan. Evidence should include owners, dependency order, replication state, predicted timings, and validation criteria. Running infrastructure is only one part of restoring a complete university SAP service.

</details>

Objective dates and six primary technical references are in the [guide](AZ-120.md). Develop reviewable diagrams and runbooks in the [workbook](AZ-120-workbook.md).
