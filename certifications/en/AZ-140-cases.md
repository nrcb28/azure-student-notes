# AZ-140 · 10 cases with reasoned answers

[Guide](AZ-140.md) · [Workbook](AZ-140-workbook.md) · [Contents](README.md)

Original university-lab scenarios, not official exam questions. Explain the requirement and the confirming evidence before revealing each answer. All results below are design reasoning; no cloud deployment is claimed.

## 1. Forty students need interchangeable desktops, while one researcher needs the same dedicated machine. Should everyone receive a personal pool?

<details>
<summary>Answer</summary>

Evaluate a pooled host pool with a supported multi-session OS for the students and personal assignment for the researcher. Dedicated machines for everyone may consume unnecessary capacity, while forcing the researcher into an interchangeable pool could violate the requirement. Personal assignment still requires the appropriate published-resource entitlement. Record workload measurements, licensing checks, host density assumptions, and the researcher's persistence requirement. A suitable evidence set includes the assignment model and capacity calculation, rather than only the number of VMs.

</details>

## 2. A student has Azure Contributor and can see the VMs in the portal, but their AVD feed is empty. What should you inspect?

<details>
<summary>Answer</summary>

Inspect the student's identity and application-group assignment, the group's association with the intended host pool, and its registration with the workspace. Management access to VM resources does not publish a desktop to that user. Also verify that the client subscribes to the correct workspace using the expected account. Record group membership, effective resource entitlement, and feed diagnostics with timestamps. Opening an inbound VM port or assigning subscription Owner would not explain or correct the missing publication relationship.

</details>

## 3. The project wants Entra-joined hosts but an older app requires domain services. Is Entra ID automatically an AD DS replacement?

<details>
<summary>Answer</summary>

No. Separate the application's exact authentication and directory requirements from AVD feed authentication. Microsoft Entra ID, AD DS, and Microsoft Entra Domain Services offer different capabilities, and choosing a host join does not remove an application's dependencies. Check supported identity combinations, profile-storage authentication, policy management, and SSO requirements before selecting a design. Evidence should include an application dependency inventory and a supported authentication flow. Conditional Access policy alone cannot supply a missing domain protocol or domain-controller reachability.

</details>

## 4. A firewall team proposes public TCP 3389 to repair every AVD connection. Does reverse connect require that change?

<details>
<summary>Answer</summary>

No. Base AVD reverse connect relies on outbound service connectivity from the client and session host over HTTPS/TCP. Inspect required destinations, DNS, TLS, proxy behaviour, agent health, and the failing connection stage. Shortpath is a separate UDP transport choice with option-specific prerequisites, not a reason to expose public RDP. For a managed listener design, document private reachability and the selected UDP listener port. The evidence should identify the actual blocked dependency and a narrowly scoped correction proposal.

</details>

## 5. Campus clients use UDP, but home clients fall back to TCP. Does that prove the session host has failed?

<details>
<summary>Answer</summary>

No. Compare the clients, networks, and selected Shortpath options. A campus VPN might provide direct private reachability, while a home NAT or firewall prevents a particular UDP path. Check supported client versions, UDP policy, STUN/TURN reachability, cloud availability, and the negotiated transport. Reverse-connect fallback can preserve the session while performance differs. Record timestamps, round-trip delay, packet loss, and both successful and failed path observations. Do not assume the managed UDP 3390 listener is required for every public-network Shortpath connection.

</details>

## 6. Students authenticate successfully but receive temporary profiles after an SMB identity change. Would rebuilding every VM fix the cause?

<details>
<summary>Answer</summary>

First inspect FSLogix attachment logs and the storage authentication path. Verify the expected container location, DNS resolution, share-level permissions, NTFS permissions, supported Kerberos configuration, and encryption compatibility. Feed authentication and profile-file access are separate stages. Rebuilding hosts without correcting a shared storage dependency could reproduce the same failure everywhere. Preserve affected containers and investigate existing sessions or locks before recovery actions. Evidence should show the exact attachment error and a permitted profile operation using the intended user identity.

</details>

## 7. The same student opens two independent sessions and the second cannot attach the profile container. Should an operator delete the lock immediately?

<details>
<summary>Answer</summary>

Do not treat the lock as disposable evidence. The standard FSLogix profile configuration supports a single connection to a container; concurrent configurations have additional requirements and application limitations. Identify active and disconnected sessions, the owning host, and the actual lock state before deciding whether a stale resource needs recovery. Coordinate a controlled sign-out and protect unsaved work. Record timestamps and attachment logs. A design requiring concurrent sessions needs explicit supported configuration and validation rather than unrestricted simultaneous writes to the same container.

</details>

## 8. The notes editor appears in a RemoteApp group but fails on half the hosts. Does publishing the icon install the application?

<details>
<summary>Answer</summary>

Publishing a RemoteApp controls access and presentation; it does not prove that every eligible session host can run the application. Compare image versions, installed dependencies, and the selected delivery method. For App Attach, inspect package compatibility, storage access, host-pool and user assignments, and registration evidence. Test the same user on a known-good host and an affected host without editing production assignments. The deliverable should explain the difference and propose a staged package or image correction with a working fallback.

</details>

## 9. Forty-eight students arrive together. Hosts support twelve sessions each, and one host must be allowed to fail. Are four hosts plus Start VM on Connect enough?

<details>
<summary>Answer</summary>

Four healthy hosts provide exactly 48 sessions under the measured assumption, leaving no one-host failure allowance. Five available hosts provide 48 sessions after losing one. Start VM on Connect does not guarantee that spare hosts are healthy and ready before a simultaneous class arrival. Model boot time, maximum sessions, load balancing, scaling schedules, drain exclusions, and profile-storage capacity. Evidence is a capacity table for normal and degraded operation, plus predicted startup timing. Validate the density assumption with representative workloads before using it operationally.

</details>

## 10. A replacement region has VMs, yet students cannot recover their working environment. What is missing from the recovery claim?

<details>
<summary>Answer</summary>

A VM inventory alone does not establish desktop recovery. Trace identity and DNS availability, resource publication, application delivery, network paths, profile-storage access and consistency, and the notes API. Specify profile and application-data recovery objectives separately. Use a connection correlation ID, diagnostics, host events, and FSLogix logs to locate the first failed stage. The tabletop should assign operators, capacity assumptions, return-to-primary steps, and a successful student workflow as acceptance evidence. Label these as planned checks until an authorised recovery exercise produces actual observations.

</details>

Technical references, objective dates, and scope limits are in the [guide](AZ-140.md). Turn the reasoning into diagrams and evidence with the [workbook](AZ-140-workbook.md).
