# AZ-802 · Evidence-based Windows Server workbook

[Guide](AZ-802.md) · [10 reasoned cases](AZ-802-cases.md) · [Contents](README.md)

Five matching units combine the seven AZ-802 study areas. Use the fictional isolated university lab `lab.example.test`. Produce a reviewable decision and evidence package, not a list of settings copied from a video. These are proposed Windows exercises; no AD, Hyper-V, Azure, restore or security-control execution is claimed. Without a compatible Windows lab, submit a labelled design and predicted observations instead of inventing results.

Keep a ledger for every unit: baseline, hypothesis, competing explanation, selected read-only check, proposed change, expected observation, actual observation if executed, and stopping/rollback condition. Record OS edition/version, installed modules, required rights and target identity. Redact secrets and personal data. The guide's prerequisite matrix applies to its command examples; no command grants authority to inspect an unrelated system.

<a id="az-802-unit-1"></a>

## 1. Trace an identity change from directory to access

**Scenario:** LAB-DC1 accepts a research-group membership change, but a remote-building client still fails access to `\\LAB-FS1\LabNotes`. The client selects LAB-DC2. A separate branch proposal uses an RODC because the room has limited physical protection.

**Investigation:** draw the forest/domain, two writable controllers, branch RODC, DNS resolvers, sites and IP subnet mappings. Mark the controller that accepted the change and the one used by the client. Identify the replication path, relevant SRV records, time hierarchy, user token and share/NTFS boundary. Choose an ordered sequence of checks that can distinguish stale directory state from an effective-access problem. Include an expected observation that would disprove your first hypothesis.

Use the guide's AD inventory, resolver/time and replication queries only from an appropriate Windows administration context. For Group Policy, explain scope, client processing and effective settings separately. For the RODC, define ordinary accounts eligible for disconnected access, accounts that must remain denied, delegated branch administration and a device-loss response. Verify effective password replication policy rather than assuming a group label proves it.

**Evidence:** a topology with identity boundaries; sanitized query contexts and timestamps; an object-change timeline; intended and observed controller selection; a permitted/denied file-access pair; and an RODC caching decision without passwords.

**Deliverable and gates:** write a one-page diagnosis with a narrow proposed repair. Preserve the original resolver/site/policy settings before any authorized lab change. Stop if the failing controller or namespace is outside the disposable lab. Do not broaden privileges, seize FSMO roles or reset all accounts to make the symptom disappear. Success means the required directory change converges and the intended user gains only the intended access, with the denied user still denied.

<a id="az-802-unit-2"></a>

## 2. Review remote administration and VM recovery boundaries

**Scenario:** an operator reaches a member server remotely but cannot access a second resource. A proposal enables reusable credential delegation and runs a JEA endpoint on a DC. Meanwhile, a VM's production consistency step fails but a Standard checkpoint is created. The lab has two 64-GiB hosts, a synthetic 12-GiB host reserve and twelve fixed 4-GiB guests assigned to each host.

**Investigation:** draw each authentication hop, protocol, effective identity and required operation. Compare a supported second-hop design with the risks of CredSSP and protocol-specific delegation limits. Review JEA's allowed commands/parameters, execution groups, auditing and placement; explain why the default virtual-account privilege on a DC is excessive for a narrow member-service task. For an Arc-managed machine, separately identify Azure extension authority and local permissions.

Use VM/switch/memory/checkpoint inventory to explain the guest network and recovery state. Compare checkpoints, Replica, clustering and protected backup by the failure each addresses. Explain Production versus ProductionOnly and why the actual checkpoint type matters. For the synthetic sizing, normal assigned memory is 48 + 12 = 60 GiB per host; moving all 24 guests to one host would require 96 + 12 = 108 GiB. State the assumptions and show why normal fit does not establish single-host-failure capacity.

**Evidence:** a permission-and-hop diagram; a restricted-endpoint review; switch/guest path; a memory worksheet; actual checkpoint metadata if available; and an independent restore-copy plan.

**Deliverable and gates:** propose a supported, narrowly scoped administration design and separate recovery mechanisms. Stop if delegation would expose a real privileged identity or a VM's supported consistency requirements are unknown. Record prechange endpoint settings and recovery access. Do not delete AVHDX files, claim Replica fixes logical corruption, or call a same-storage checkpoint an independent backup. A successful command and a safely recoverable service require different validation.

<a id="az-802-unit-3"></a>

## 3. Diagnose a client-to-file path across network and storage

**Scenario:** new classroom clients cannot obtain an address, while old leases continue. After an approved network correction, one research user can reach a share but receives a folder denial. The server is registered with Azure File Sync and some files are tiered. A diagram also includes a hybrid DNS conditional forwarder and an unconfigured second DHCP server.

**Investigation:** trace the client VLAN/relay, authorized DHCP scope, exclusions/reservations, options and free capacity. Define what an actual new-allocation test adds beyond an existing-client test. Distinguish a second server from a configured supported failover relationship. Trace the intended resolver, namespace, conditional-forwarding target, return path and application port; a correct DNS answer does not establish a usable SMB connection.

Next record the actual user, share authorization, NTFS inheritance and group-token context. Test an allowed identity and an identity that must remain denied. For Azure Files, separate supported identity setup, share-level authorization and directory/file permissions. Inventory the File Sync endpoints, local cache assumptions, independent retained backups and a supported recovery procedure. Explicitly reject restoring/cloning/reverting a registered server OS/VM as a generic File Sync recovery method.

**Evidence:** an address-allocation worksheet; resolver and route diagrams; share/ACL observations with secrets removed; allowed/denied test criteria; a cloud/server endpoint map; and a selected historical recovery point with its dependencies.

**Deliverable and gates:** explain the network failure and permission failure as separate findings. Capture the existing scope and ACL before any authorized change. Stop on an overlapping allocation range, an unintended permission expansion or an unprotected recovery dependency. Success requires the intended new client to obtain valid settings, the intended user to access the folder, the denied user to remain blocked and the recovery plan to identify a protected copy rather than merely another synchronized endpoint.

<a id="az-802-unit-4"></a>

## 4. Design role-specific hardening without losing recovery access

**Scenario:** the fleet includes Windows Server 2022 and 2025, member servers, a DC and a file server. A proposal deploys one OSConfig baseline everywhere, exposes SMB over QUIC without checking certificates, and shares a LAPS password in a report. Removing the baseline is described as a complete rollback.

**Investigation:** build a role/version matrix before selecting controls. OSConfig's reviewed security-baseline guidance targets Windows Server 2025; record module version, scenario, expected setting differences, reboot needs and conflicts with existing GPO/other management. Pilot the correct role. Explain why removing management cannot be assumed to reconstruct the earlier state. Keep a protected prior-state record and an alternate authorized administration path.

For LAPS, separate rotation, backup destination, permitted retrieval, auditing and recovery access. Document DSRM recovery conditions where relevant, without retrieving or publishing a password. For SMB over QUIC, check the exact server/client support: the reviewed guidance lists Windows Server 2022 Datacenter: Azure Edition or Windows Server 2025 editions, with Windows 11 clients. Review certificate trust/names/private-key use and the permitted UDP path, then preserve share/file authorization. Do not treat QUIC as a replacement for it.

**Evidence:** the role/version matrix; selected controls with support references; a setting diff and rollback gate; permitted/denied retrieval roles; a sanitized certificate checklist; and an isolated allowed/denied access test plan.

**Deliverable and gates:** write a staged change proposal with named recovery responsibilities. Stop if the baseline is unsupported, the only management route would be removed, a certificate requirement is unresolved or a real secret appears in evidence. Treat any existing credential disclosure through the organization's response process. A compliance result, installed feature and demonstrated enforcement are separate observations.

<a id="az-802-unit-5"></a>

## 5. Trace a missing event and rehearse directory recovery

**Scenario:** an Arc-managed server reports connected, AMA sends Heartbeat, but a required System event exists only locally. During a separate tabletop, an AD object is deleted and Recycle Bin was not enabled beforehand. A supported directory backup exists. The team has a two-hour restoration target and wants evidence stronger than “the VM boots.”

**Investigation:** trace one sanitized local event through the intended AMA extension/service, DCR, association, source selection, destination and query time range. Record machine identity, event time and arrival time separately. Define a test that distinguishes missing source events from missing collection configuration and from a query against the wrong table/workspace. Explain what Arc connection and Heartbeat each demonstrate and what they leave uncertain.

For directory recovery, identify affected objects/dependencies, available supported backup, recovery owner, protected DSRM credentials and the appropriate restoration scope. Distinguish Recycle Bin object recovery, authoritative/non-authoritative directory recovery, SYSVOL recovery and whole-forest recovery. Select a supported procedure for the actual failure; do not convert a single object mistake into an automatic controller rollback or FSMO seizure. Rehearse dependency order, replication implications, validation and safe return of recovered services.

**Evidence:** an event-source-to-destination trace; a timestamped hypothesis log; a recovery-point inventory; predicted recovery timings clearly marked as estimates; and acceptance checks covering the required object, authentication, replication, policy and affected application.

**Deliverable and gates:** produce separate monitoring and recovery runbooks. Preserve original DCR/association evidence before changes. Stop if recovery scope or the authoritative copy is unclear. Keep a timeline of business interruption and usable recovered data so RTO and RPO are not confused. Record an operation as completed only after an authorized lab executes it and supplies the stated observations. The repository itself claims no Windows/AD restoration or measured two-hour result.

Finish by answering the [ten cases](AZ-802-cases.md) without opening their explanations. For each weak answer, identify the missing evidence or confused boundary and return to that part of the [guide](AZ-802.md). This workbook provides selected practice, not exhaustive objective coverage or a prediction of passing.
