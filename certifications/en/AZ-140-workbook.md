# AZ-140 · Common advanced workbook

[Guide](AZ-140.md) · [10 cases](AZ-140-cases.md) · [Contents](README.md)

Five matching units across languages. Work offline using the university notes app and virtual computer lab. Record predictions as predictions; these units deploy nothing, change no tenant, and do not establish production readiness.

<a id="az-140-unit-1"></a>

## 1. Map resources, users, and responsibility

Draw a pooled lab for 48 students and a personal desktop for one researcher. Identify host pools, session hosts, application groups, workspace registration, and user assignments. Separate Microsoft's broker and gateway responsibilities from customer images, VMs, networking, identity integration, and storage. Explain why supported multi-session operation is different from personal assignment.

**Scenario:** a student sees Azure VMs but has an empty desktop feed. **Evidence:** a resource relationship diagram, effective application-group entitlement, intended client account, and licensing assumptions. **Deliverable:** the first three checks, one unsuitable role escalation you reject, and an owner for each customer-managed dependency. Link the design to [compute foundations](../../en/03-compute.md).

<a id="az-140-unit-2"></a>

## 2. Trace identity and transport separately

Compare Entra join, AD DS join, and Entra Domain Services join against a legacy app and the selected profile-storage authentication. Draw feed authentication, entitlement, session sign-in, and file access as separate stages. Add outbound HTTPS reverse connect and an option-specific UDP Shortpath path. Explain the managed listener's private reachability and how ICE/STUN or TURN changes the transport requirements.

**Scenario:** campus users connect smoothly; home users receive another sign-in prompt and slower sessions. **Evidence:** client version, join type, SSO and Conditional Access assumptions, negotiated transport, DNS path, and latency observations needed. **Deliverable:** two independent hypotheses and their confirming tests, without public TCP 3389 exposure. Review [network foundations](../../en/05-networking.md).

<a id="az-140-unit-3"></a>

## 3. Protect profiles and publish a usable app

Design persistent FSLogix containers outside replaceable pooled hosts. Document storage identity/Kerberos compatibility, share and NTFS permissions, capacity, sign-in burst assumptions, single-connection behaviour, and backup/restore objectives. Distinguish profile preferences from authoritative notes data. Compare installing the editor in the image with a supported App Attach package and explain RemoteApp publication separately.

**Scenario:** a student reaches the desktop but receives a temporary profile and cannot launch the editor. **Evidence:** container attachment error, active-session ownership, expected permissions, host image version, package access, and assignments. **Deliverable:** an ordered fault tree with separate profile and application branches, a safe recovery proposal, and criteria for preserving existing user work.

<a id="az-140-unit-4"></a>

## 4. Release images and calculate classroom capacity

Write a versioned golden-image release plan covering supported OS, agents, security policy, applications, validation users, drain behaviour, and rollback. With a measured limit of 12 sessions per host, calculate capacity for 48 students during one-host failure. Distinguish a scaling plan's selected method from Start VM on Connect; include boot time, health, maximum sessions, and storage constraints.

**Scenario:** a patch arrives before class while one host is already unavailable. **Evidence:** a five-host capacity table, image versions, validation checklist, active sessions, and maintenance exclusions. **Deliverable:** a staged rollout that preserves sufficient usable capacity, with rollback triggers and an explicit policy for users still connected at ramp-down.

<a id="az-140-unit-5"></a>

## 5. Run a login-failure and recovery tabletop

Follow a synthetic connection using UTC timestamps, a pseudonymous user, resource, host, and correlation ID. Specify diagnostic settings, host performance collection, FSLogix logs, and the user-experience observations required. Explain why an attempt that never reaches AVD may leave no connection record. Add identity, DNS, app packages, profiles, and notes-API dependencies to an alternate-region recovery plan.

**Scenario:** the 09:00 class cannot restore profiles after a storage outage. **Evidence:** predicted checkpoints, a normal-session comparison, profile recovery objectives, available capacity, and continuing VM, disk, storage, network, monitoring, and licensing cost owners. **Deliverable:** an incident timeline, first-failure hypothesis, recovery and return-to-primary criteria, and a clear boundary between tabletop predictions and observed tests.

Use the six technical references in the [guide](AZ-140.md) to challenge assumptions. These exercises are original study material and do not cover every official objective or guarantee an exam result.
