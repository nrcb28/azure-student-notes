# AZ-802 · 10 cases with reasoned answers

[Guide](AZ-802.md) · [Five-unit workbook](AZ-802-workbook.md) · [Contents](README.md)

These are original university-lab scenarios, not official exam questions. State a hypothesis, an alternative explanation, and the evidence needed before opening an answer. Commands mentioned here are proposed checks for an authorized Windows lab; no execution or production recovery is claimed. The complete scenario is included in each question so the trainer and Anki export retain its context.

## 1. After a classroom network change, a domain client resolves public websites but cannot find its domain controller. Its resolver is a public DNS service; the configured AD DNS server is reachable and its SRV records are known to be healthy. The client's time is correct. Should the first repair reset every student's password?

<details>
<summary>Answer</summary>

No. The supplied evidence points first to the client's name-resolution path. Public DNS success does not establish discovery of private AD service records. Record the client resolver, the relevant SRV query and its result, then compare that path with the approved lab DNS configuration. A suitable correction restores the intended AD-aware resolver path and validates discovery, controller reachability, and an affected logon before widening the change.

The healthy-server and correct-time assumptions narrow this particular investigation; they do not mean every real logon failure is a DNS problem. If discovery succeeds but authentication still fails, continue with the exact error, account state, protocol and secure-channel evidence. Preserve a before/after record with timestamps and the actual controller selected. Resetting all passwords would change unrelated state without addressing the identified resolver mismatch, and could obscure useful evidence. Rollback means restoring the recorded client configuration if the approved change breaks other required resolution, rather than leaving a public and private resolver arrangement whose behaviour has not been understood.

</details>

## 2. A research-group membership change is visible on LAB-DC1 but not on the remote-building controller. Clients there use that second controller, replication reports DNS-related failures, and a new share remains inaccessible. Is adding the user to another privileged group a suitable fix?

<details>
<summary>Answer</summary>

No. The observed directory versions and replication failure provide a concrete explanation to investigate before broadening privileges. Record the change time, the controller that accepted it, the controller selected by the client, and replication errors. Check the replication partners' DNS records, configured resolvers, connectivity and authentication prerequisites. Verify that the remote subnet maps to the intended site, but do not assume changing a site schedule repairs a DNS failure.

After a supported repair, confirm that the particular membership change has reached the relevant controller. Then obtain a new appropriate user logon/session token and test the intended share as that user; directory convergence and refreshed authorization context are separate checks. Also inspect share and filesystem permissions if access still fails. Keep the group narrow and record both a permitted and a denied test. Adding an unrelated privileged group could mask the symptom while leaving replication broken and widening the student's access. The deliverable is a change-convergence and access timeline, with predicted observations labelled until a lab test actually provides them.

</details>

## 3. An isolated branch classroom will use an RODC. A proposal allows privileged university administrators' passwords to be cached there so they can sign in during WAN outages. The room has weaker physical protection than the main data centre. What should the design review require?

<details>
<summary>Answer</summary>

Reject the assumption that an RODC makes any cached credential safe. Review its password replication policy, effective allowed and denied memberships, delegated administration and physical-loss procedure. Privileged accounts belong outside that branch credential cache. Where an account is both allowed and denied under the effective policy, the deny takes precedence. Identify the limited ordinary accounts that genuinely need disconnected access and check the resulting effective policy rather than relying on a group name alone.

The plan should distinguish cached-user authentication from operations that need a writable controller, including new or changed directory state. Define which services remain usable during the WAN interruption and how operators will obtain an approved administrative path without weakening the domain boundary. Evidence includes the branch threat assumptions, selected accounts, effective caching decisions, controller connectivity and a device-loss response. Do not publish passwords or cache contents as evidence. A recovery plan must consider affected cached credentials and the compromised server, not merely replace its hardware and assume that all directory secrets remained protected.

</details>

## 4. A server connected to Azure Arc is still failing a remoting job from server B to file server C. Someone proposes broad credential delegation and a default JEA virtual account on a domain controller. The task only needs a narrow service operation. Does Arc connection justify this design?

<details>
<summary>Answer</summary>

No. Arc connection creates an Azure management relationship; it does not join the server to AD, create a forest trust or automatically delegate the interactive operator's credentials to C. Draw the first and second hops, the protocol on each, the effective identity and the exact operation required. Diagnose the authorization and authentication boundary that fails. A successful first session cannot prove that the second resource will accept the intended identity.

Review supported second-hop options and their limitations before selecting one. CredSSP introduces credential exposure; constrained-delegation methods do not generically solve a WinRM-to-WinRM second hop. For JEA, inspect the session execution identity, allowed users, commands, parameters and audit trail together. A default virtual account on a DC can have Domain Admin privileges, which is disproportionate to a narrow service task. Prefer an appropriate management location and explicitly restricted execution rights. Evidence is a permission-and-hop diagram plus allowed and denied operations, not a successful command obtained with reusable administrator credentials. Extension permissions on an Arc-managed controller also need their own review.

</details>

## 5. A lab VM uses Production checkpoints, but guest consistency processing fails and the host creates a Standard checkpoint. A student calls that an independent application-consistent backup. The checkpoint and VM disks share the same storage. What needs correcting?

<details>
<summary>Answer</summary>

Correct both the consistency claim and the protection boundary. Production mode can allow fallback to a Standard checkpoint, so the requested setting is weaker evidence than the actual checkpoint type and guest-processing result. If the exercise requires a production checkpoint and rejects fallback, evaluate ProductionOnly and fix the guest integration/VSS or relevant filesystem-freeze prerequisites. A refusal to create the required checkpoint is useful failure evidence; silently accepting another type is not equivalent.

Even a successful production checkpoint does not establish an independent retained backup. Its disk chain can be lost with the VM storage, and application recovery still needs a supported consistency and restoration method. Keep a protected backup with suitable retention and a restore validation plan where the requirement demands it. Inspect checkpoint metadata and storage headroom through supported tools; do not delete AVHDX files manually. Explain separately whether the goal is reversing a disposable lab change, surviving host/storage loss, or recovering an earlier valid application state. Each goal needs different evidence and may need a different mechanism.

</details>

## 6. Existing classroom PCs keep working, but new clients fail to obtain addresses. The authorized DHCP server is reachable through a functioning relay; its affected scope has no free leases. A second server has been installed but no failover relationship exists. What should the investigation conclude?

<details>
<summary>Answer</summary>

The supplied evidence identifies scope exhaustion as the immediate problem for new allocations. Existing clients can continue under their lease state, so their success does not prove that the server can allocate another address. Inspect scope ranges, exclusions, reservations, active leases and the actual client subnet before proposing an approved capacity correction. Check for stale or unexpected allocation patterns, but do not delete leases indiscriminately or expand into an overlapping address range.

A second installed server does not automatically coordinate leases. If availability is required, design a supported DHCP failover relationship for the intended scopes, with its mode, partner state, lease behaviour and recovery responsibilities understood. Do not activate competing unmanaged copies of the same range. Evidence includes the scope inventory, available-address count, relay path and a test involving a genuinely new client as well as an existing one. Capacity and failover solve different failure conditions: a healthy partnership is not permission to ignore an undersized pool. Record the prechange scope and stop if the proposed range conflicts with routing or another allocation authority.

</details>

## 7. A student has the intended SMB share permission, but NTFS denies access to a project folder. Azure File Sync is healthy and its server endpoint has tiered files. Would granting Azure Contributor and calling the synchronized copy a backup resolve both concerns?

<details>
<summary>Answer</summary>

No. Follow the actual Windows file path and identity. The identified NTFS denial remains relevant even when share-level access is present. Correct the intended folder authorization with appropriate group membership and isolation, then test the affected student and a student who must remain denied. An Azure resource-management role does not automatically repair the filesystem ACL or establish SMB data access. Inspect effective access rather than inferring it from one configured entry.

Treat the recovery question separately. Healthy synchronization can propagate a deletion, and tiered server files may not contain a complete independent local copy. Identify the cloud endpoint, usable retained backups, restore dependencies and the supported recovery workflow. Reverting or cloning a registered File Sync server from an OS image or VM checkpoint is not a generic supported recovery method. Evidence should include the share/NTFS decision, the endpoint and tiering state, and a historical recovery-point plan. Access restored today and data recoverable after a later mistake are two different outcomes; neither should be claimed without its corresponding test or explicitly labelled design evidence.

</details>

## 8. A mixed fleet contains Windows Server 2022 and 2025. A hardening proposal applies an OSConfig Windows Server 2025 baseline everywhere, then promises that removing management restores every old setting. It also stores a retrieved LAPS password in a shared report. What must change?

<details>
<summary>Answer</summary>

Separate supportability, change recovery and secret handling. The reviewed OSConfig baseline guidance targets Windows Server 2025, so the same configuration should not be presented as supported on the 2022 machines. Record OS/module versions, role-specific settings and a pilot group. Identify existing GPO or other management that could conflict, inspect effective settings, and plan required restart and access validation. Baseline removal does not guarantee reconstruction of every value that existed before management; retain a reviewed prior-state and recovery procedure.

LAPS supports controlled password rotation, backup and authorized retrieval. Copying a retrieved password into a broadly readable report defeats that access boundary. Remove it through the appropriate incident/change process, treat exposure according to policy and rotate where required; publish only sanitized policy and authorization evidence. Recovery credentials need protected access that remains usable during the anticipated failure. Evidence should show supported deployment, permitted and denied retrieval roles, audited access and a recovery plan, rather than a plaintext credential or a compliance screenshot assumed to prove every protection.

</details>

## 9. An Arc server shows connected and its workspace has recent agent Heartbeat rows, but the required Windows System events are absent. Those events exist locally. Does the empty query prove that Windows generated no faults?

<details>
<summary>Answer</summary>

No. The scenario already states that relevant events exist locally. Arc connectivity and agent Heartbeat are different observations from successful delivery of the selected event source. Confirm the intended machine, time window, workspace and destination table, then inspect the AMA extension/service state, the associated DCR, its event selection and destination, and the configuration actually received by the agent. A DCR created without the relevant association cannot collect from that machine by intention alone.

Use a sanitized local event identifier and timestamp to trace one event through the proposed pipeline. Distinguish absence at the source, collection failure, transport/configuration problems and a query directed at the wrong destination. Keep the event's time separate from collection arrival time, and allow for documented ingestion delay without treating every delay as acceptable. Evidence includes the local record, machine identity, association and query context, followed by an expected arrival test. Avoid reinstalling all agents first: that changes state and may erase useful troubleshooting context without addressing the missing selection or association.

</details>

## 10. A student deletes an important AD object and discovers that Recycle Bin was not enabled before deletion. They propose rolling a production domain controller back to an ordinary VM checkpoint and seizing every FSMO role. The organization has a supported directory backup and an assigned recovery owner. What is the safer decision process?

<details>
<summary>Answer</summary>

Escalate to the documented directory recovery procedure and preserve the deletion, replication and backup evidence. Enabling Recycle Bin after the event does not magically create the missing prior recoverable state. Determine the object and dependencies affected, the available supported backup and the restoration scope before selecting a recovery method. A single-object mistake does not by itself justify a whole-forest recovery or seizure of unrelated FSMO roles.

The recovery owner should choose the supported authoritative or non-authoritative steps appropriate to the actual failure, including a DSRM context where required, protected recovery credentials and SYSVOL considerations. A generic VM checkpoint rollback is not a substitute for that plan. Document the authoritative state, replication implications, validation and conditions under which a former role holder may return if seizure is genuinely necessary. Validate directory objects, authentication, replication and the affected service, rather than stopping at “the VM boots.” In this repository the deliverable is a tabletop with explicit decision gates; no directory restoration, role seizure or measured recovery has been executed.

</details>

Use the technical references and version qualifications in the [guide](AZ-802.md). Develop evidence and controlled change decisions in the [workbook](AZ-802-workbook.md).
