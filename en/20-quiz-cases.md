# 32 scenarios to practise

[←](19-mini-quiz.md) · [CLI](../QUIZ.md)

Small independent practice bank. This is not a full official exam or a pass prediction. Unanswered questions remain in the total.

<a id="quiz-q01"></a>

## AZ-900 · Control of the operating system

A lab application must install its own Linux kernel driver. Which hosting option best meets that requirement?

- **A.** Run the application in Microsoft 365.
- **B.** Use an Azure virtual machine with a compatible Linux image.
- **C.** Deploy it to an App Service managed runtime.
- **D.** Put the driver inside a standard Azure Function.

<details>
<summary>Why:</summary>

**B. Use an Azure virtual machine with a compatible Linux image.**

The decisive requirement is control of the guest operating system. A compatible Azure VM lets the team manage that environment and its drivers. This also leaves operating system maintenance with the team. A convenient managed application platform is unsuitable if it does not expose the required kernel control.

- **A.** Microsoft 365 is ready-to-use software, not a host for arbitrary kernel drivers.
- **C.** An App Service managed runtime does not provide the required guest-kernel administration.
- **D.** A standard Function does not grant the required kernel-driver control.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) · [Review chapter:](03-compute.md)

</details>

<a id="quiz-q02"></a>

## AZ-900 · Scaling and session state

A notes API adds instances behind a load balancer. Any instance may be replaced, but users must keep their sessions. Sessions currently exist only in each instance's memory. What should change?

- **A.** Increase CPU on every instance.
- **B.** Keep sessions in memory and enable sticky routing only.
- **C.** Move session state to an appropriate shared external store.
- **D.** Give every instance a public IP address.

<details>
<summary>Why:</summary>

**C. Move session state to an appropriate shared external store.**

Horizontal scaling distributes requests across instances, so important session state cannot depend solely on one instance's memory. An appropriate external store lets replacement instances retrieve it. Sticky routing alone cannot preserve memory after that instance disappears. The application must also handle access and failures of the external state service.

- **A.** More CPU does not preserve memory after instance replacement.
- **B.** Sticky routing still loses the session when its selected instance disappears.
- **D.** Public addresses do not provide shared or durable session state.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/scale-out) · [Review chapter:](01-fundamentals.md)

</details>

<a id="quiz-q03"></a>

## AZ-104 · Storage data permissions

A user has Contributor on a storage account. A Blob request using that user's Entra identity reaches the service but is denied for missing data permission. The user only needs to read blobs in one container. What is the least-privilege response?

- **A.** Assign Storage Blob Data Reader at that container's scope.
- **B.** Assign Owner on the entire subscription.
- **C.** Open every inbound network port.
- **D.** Distribute the storage account key to the user.

<details>
<summary>Why:</summary>

**A. Assign Storage Blob Data Reader at that container's scope.**

Management permissions and blob data permissions are separate. Storage Blob Data Reader grants the required read capability, and container scope limits the grant to the stated need. The scenario already identifies a data-permission problem, so broad administrative rights or unrelated network changes would not be a proportionate diagnosis.

- **B.** Subscription Owner exceeds the stated container-read requirement.
- **C.** Opening ports does not supply the missing data authorisation.
- **D.** An account key grants much broader access than the stated need.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access) · [Review chapter:](06-identity.md)

</details>

<a id="quiz-q04"></a>

## AZ-104 · Inherited RBAC permissions

A user has Reader directly on a VM and also through a group assigned Reader at subscription scope. You remove only the direct VM assignment. The user can still read the VM. What explains this?

- **A.** Azure automatically gives every user Reader on all VMs.
- **B.** A resource-group tag restores the deleted assignment.
- **C.** Removing a role always requires deleting the VM.
- **D.** The group assignment still grants inherited access.

<details>
<summary>Why:</summary>

**D. The group assignment still grants inherited access.**

Removing one assignment does not remove permissions obtained from another assignment. The group has Reader at the subscription, so its members can inherit that access to the VM. Inspect direct assignments, group membership, and parent scopes before treating the remaining access as a service error or granting more permissions.

- **A.** There is no universal Reader grant to every user.
- **B.** Tags classify resources and do not recreate role assignments.
- **C.** Role removal does not require deleting the protected resource.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview) · [Review chapter:](06-identity.md)

</details>

<a id="quiz-q05"></a>

## AZ-305 · Recovery point objectives

A design keeps successful recoverable database points only once every 24 hours. The business now requires no more than one hour of recent data loss after a disaster. Which change directly addresses the gap?

- **A.** Increase the API server's CPU.
- **B.** Design recoverable data protection points no more than one hour apart, and validate recovery.
- **C.** Add a cost-alert budget.
- **D.** Rename the resource group to production.

<details>
<summary>Why:</summary>

**B. Design recoverable data protection points no more than one hour apart, and validate recovery.**

RPO concerns the amount of recent data that may be lost, expressed in time. Daily recovery points alone cannot support a one-hour target. The protection design must produce sufficiently frequent recoverable states and be validated. Faster application compute or cost labels do not change the age of the available recovery data.

- **A.** API CPU does not increase the frequency of protected recovery data.
- **C.** A budget alerts on spending, not data loss.
- **D.** A resource-group name does not change recovery-point frequency.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery) · [Review chapter:](10-architecture.md)

</details>

<a id="quiz-q06"></a>

## AZ-305 · Private endpoint DNS

Public access to a storage service has been disabled and a private endpoint exists. The client still resolves the service hostname to its public IP. Its private network path is otherwise available. What should you investigate first?

- **A.** Give the client subscription Owner.
- **B.** Hard-code the public IP permanently.
- **C.** Private DNS zones, links, and forwarding used by that client.
- **D.** Increase the application's retry count indefinitely.

<details>
<summary>Why:</summary>

**C. Private DNS zones, links, and forwarding used by that client.**

The client is resolving the wrong destination for the intended private connection. Check the service's recommended private DNS configuration and how this client reaches it, including links and forwarding. Keep using the service hostname. Correcting DNS does not itself grant data permissions, but unrelated privileges and endless retries do not fix this mismatch.

- **A.** Owner does not change the client's name resolution.
- **B.** The public address is the wrong destination after public access is disabled.
- **D.** Repeating a request does not correct deterministic DNS configuration.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) · [Review chapter:](05-networking.md)

</details>

<a id="quiz-q07"></a>

## AZ-400 · Promoting tested artifacts

A pipeline tests one container image, then rebuilds from source for production using changeable dependencies. How can the team ensure production receives the image that passed testing?

- **A.** Retest only the source comments.
- **B.** Use the latest tag without recording which image it points to.
- **C.** Skip testing because the source commit is unchanged.
- **D.** Promote the same tested image, identified by an immutable digest.

<details>
<summary>Why:</summary>

**D. Promote the same tested image, identified by an immutable digest.**

The same source commit can produce different outputs when tools, dependencies, or base images change. Promoting the already tested image avoids that rebuild difference. An immutable digest identifies the actual artifact rather than a tag that can move. Environment configuration still needs its own validation and controlled handling.

- **A.** Source comments do not identify the built artifact.
- **B.** A mutable tag can refer to a different image later.
- **C.** An unchanged commit does not establish an identical rebuilt output.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-concepts) · [Review chapter:](12-devops.md)

</details>

<a id="quiz-q08"></a>

## AZ-400 · Canary correctness signals

A canary release has normal CPU and memory, but its document downloads return incorrect files. What should the deployment decision rely on?

- **A.** Functional correctness signals and a defined stop or rollback criterion.
- **B.** CPU alone, because healthy infrastructure proves correct results.
- **C.** A larger VM before checking the returned files.
- **D.** Deleting old logs so the dashboard looks cleaner.

<details>
<summary>Why:</summary>

**A. Functional correctness signals and a defined stop or rollback criterion.**

A release can run comfortably while producing incorrect business results. Promotion needs signals that reflect the user operation, not just infrastructure utilisation. A defined stop or rollback rule makes that evidence actionable. Also check data compatibility: reverting application code does not automatically undo harmful data changes made by the release.

- **B.** CPU and memory do not prove that users receive the correct documents.
- **C.** More compute does not inherently fix incorrect application output.
- **D.** Removing evidence makes investigation harder and does not correct results.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments) · [Review chapter:](12-devops.md)

</details>

<a id="quiz-q09"></a>

## DP-900 · Transactional workloads

A university registration service must reserve one remaining lab seat and create the student's enrolment as one consistent operation. Which workload description best matches this requirement?

- **A.** An analytical workload that aggregates enrolments by semester.
- **B.** A batch workload that reconciles independent seat updates each night.
- **C.** A transactional workload that commits the related changes together.
- **D.** A streaming workload that publishes separate seat and enrolment events without coordinating their commits.

<details>
<summary>Why:</summary>

**C. A transactional workload that commits the related changes together.**

The requirement concerns a small, focused operation whose related changes must succeed or fail together. That is transactional behaviour: another request must not reserve the same final seat while the enrolment and capacity records disagree. Historical reporting is analytical work with different access patterns. Events and later reconciliation can support a wider architecture, but independent updates alone do not satisfy the stated consistency requirement.

- **A.** Semester aggregation answers historical questions; it does not coordinate the seat reservation and enrolment changes required for this live request.
- **B.** Nightly reconciliation leaves an interval in which a seat count and enrolment can disagree, contrary to the immediate consistency requirement.
- **D.** Publishing events can inform other systems, but separately committed events do not by themselves make the two source changes atomic.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing) · [Review chapter:](../certifications/en/DP-900.md)

</details>

<a id="quiz-q10"></a>

## DP-900 · ETL and ELT order

A research team extracts yesterday's download records, removes invalid identifiers in a processing service, and then loads the cleaned records into its reporting warehouse. Which description matches that order?

- **A.** ETL, because transformation occurs before loading the reporting target.
- **B.** ELT, because any workflow ending in a warehouse transforms inside that warehouse.
- **C.** Streaming, because download records originally came from application events.
- **D.** Orchestration alone, because coordinating steps removes the need for transformation.

<details>
<summary>Why:</summary>

**A. ETL, because transformation occurs before loading the reporting target.**

ETL means extract, transform, then load the intended target. Here, invalid identifiers are handled before the reporting warehouse receives the cleaned records. ELT would first load the data and then use the target's processing capabilities for transformation. The bounded collection of yesterday's records is batch input. An orchestrator may coordinate these activities, but orchestration and transformation describe different responsibilities in the same pipeline.

- **B.** ELT depends on loading before target-side transformation; merely choosing a warehouse as the destination does not determine that order.
- **C.** Event origins do not make later processing streaming; this job processes a bounded daily collection rather than continuously arriving records.
- **D.** Orchestration coordinates dependencies and recovery, while removing invalid identifiers changes the data and remains a separate transformation responsibility.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl) · [Review chapter:](../certifications/en/DP-900.md)

</details>

<a id="quiz-q11"></a>

## SC-900 · MFA factor categories

A student compares sign-in designs. Which example combines a knowledge factor with a possession factor, assuming the authenticator device is enrolled and the approval is required?

- **A.** A password followed by a memorised answer to a security question.
- **B.** A university password followed by a different memorised service password.
- **C.** A password followed by a memorised PIN typed into the same website, without a device-bound authenticator.
- **D.** A password followed by approval through the student's enrolled authenticator device.

<details>
<summary>Why:</summary>

**D. A password followed by approval through the student's enrolled authenticator device.**

A password represents something the student knows, while control of an enrolled authenticator device supplies a possession factor. Requiring both therefore combines different factor categories. Two memorised secrets remain knowledge factors even if their strings differ. This classification does not make every MFA method equally resistant to phishing: method selection, registration, recovery, and actual enforcement still need consideration for the university's access policy.

- **A.** Both the password and memorised answer are knowledge factors; an additional knowledge check does not introduce the required possession factor.
- **B.** Using different passwords may separate credentials, but both are still memorised secrets and therefore belong to the same factor category.
- **C.** The question excludes a device-bound authenticator: a PIN entered as another website secret supplies knowledge rather than proof of device possession.

[Microsoft Learn:](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks) · [Review chapter:](../certifications/en/SC-900.md)

</details>

<a id="quiz-q12"></a>

## SC-900 · Purview data handling

A university must detect student identifiers in supported document-sharing activities and warn or restrict external sharing when a configured rule matches. Which Purview capability most directly addresses that requirement?

- **A.** Audit, used only to record that sharing activity occurred.
- **B.** Data Loss Prevention with an appropriately scoped and tested policy.
- **C.** Retention, configured to keep the documents for seven years.
- **D.** A sensitivity label named Confidential, with no protection or DLP configuration.

<details>
<summary>Why:</summary>

**B. Data Loss Prevention with an appropriately scoped and tested policy.**

DLP evaluates sensitive information and matching activities against configured policies, and can warn or restrict supported actions. The design must still specify locations, detection conditions, recipients, exceptions, and the intended response. Audit supplies activity evidence, retention manages content lifecycle, and a label communicates classification or applies configured protection. A label's name alone does not establish the external-sharing restriction described in this scenario.

- **A.** Audit supports investigation by recording activity; recording a share does not itself supply the requested policy warning or restriction.
- **C.** Keeping a document for a defined period governs its lifecycle, but does not determine whether this external sharing activity should proceed.
- **D.** A label name alone supplies no configured sharing restriction; protection or a suitable DLP policy must implement the intended behaviour.

[Microsoft Learn:](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) · [Review chapter:](../certifications/en/SC-900.md)

</details>

<a id="quiz-q13"></a>

## AZ-700 · Longest prefix routing

A lab VM has two active effective routes: a user-defined 0.0.0.0/0 route to a network appliance and a system 10.20.0.0/16 route through VNet peering. No more-specific route exists. Which next hop is selected for 10.20.7.5?

- **A.** VNet peering, because the matching /16 prefix is more specific.
- **B.** The network appliance, because user-defined routes always outrank every system route.
- **C.** Both next hops, because Azure duplicates packets across all matching routes.
- **D.** No next hop, because overlapping matching prefixes invalidate the route table.

<details>
<summary>Why:</summary>

**A. VNet peering, because the matching /16 prefix is more specific.**

Azure first selects the matching route with the longest prefix. The destination belongs to 10.20.0.0/16, which is more specific than 0.0.0.0/0, so this packet uses the active peering route. Route-source preference matters when applicable routes have the same prefix length; it does not make a default user-defined route universally dominant. Selecting a next hop still does not establish firewall permission or application access.

- **B.** Route-source preference does not override longest-prefix selection here; the default user-defined route is less specific than the active peering route.
- **C.** Ordinary destination routing selects the preferred matching route; it does not copy a packet to every next hop whose prefix matches.
- **D.** Overlapping prefixes are normal in routing tables; a default route can coexist with more-specific routes without making the table invalid.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview) · [Review chapter:](../certifications/en/AZ-700.md)

</details>

<a id="quiz-q14"></a>

## AZ-700 · ExpressRoute encryption

A university uses ExpressRoute and requires encryption from its campus VPN device to an Azure VPN gateway. The ExpressRoute path must remain the underlay. Which design most directly meets that stated boundary?

- **A.** Enable MACsec on supported ExpressRoute Direct links and treat that physical-link protection as the entire campus-to-gateway boundary.
- **B.** Use ExpressRoute private peering without another encryption mechanism because private routing encrypts all payloads.
- **C.** Use a supported IPsec tunnel over ExpressRoute, validating routing, gateway support, and required throughput.
- **D.** Enable TLS only between the Azure application and its database while leaving the campus-to-gateway path unencrypted.

<details>
<summary>Why:</summary>

**C. Use a supported IPsec tunnel over ExpressRoute, validating routing, gateway support, and required throughput.**

ExpressRoute provides private connectivity, but does not automatically encrypt payloads. A supported IPsec overlay can protect the stated connection from the campus VPN device to the Azure VPN gateway while using ExpressRoute underneath. MACsec protects supported ExpressRoute Direct physical links, which is a different boundary. The proposal must also validate routing, supported gateway arrangements, capacity, and failure behaviour rather than assuming encryption alone completes the design.

- **A.** MACsec protects supported Direct physical links; that segment does not by itself cover the full campus-device-to-Azure-gateway boundary requested here.
- **B.** Private peering changes connectivity and routing, but it does not automatically encrypt the payload across the required campus-to-gateway connection.
- **D.** Application-to-database TLS protects a different segment; it leaves the explicitly required campus VPN device to Azure gateway boundary unaddressed.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-about-encryption) · [Review chapter:](../certifications/en/AZ-700.md)

</details>

<a id="quiz-q15"></a>

## DP-300 · SQL point-in-time restore

At 14:20, a university discovers a destructive Azure SQL Database update committed at 13:00. The change reached its replica. Automatic backup retention includes 12:59, and the goal is that pre-update state with minimal avoidable data loss. Which recovery plan best fits?

- **A.** Promote the current synchronized replica and assume the committed update disappears.
- **B.** Restore to 12:59 as a new database, validate it, and plan the application's controlled reconnection and any later-data reconciliation.
- **C.** Restore a two-day-old retained backup even though the required 12:59 recovery point is available.
- **D.** Perform a point-in-time restore and assume Azure overwrites the production database and redirects every client automatically.

<details>
<summary>Why:</summary>

**B. Restore to 12:59 as a new database, validate it, and plan the application's controlled reconnection and any later-data reconciliation.**

Point-in-time restore can recover a retained state before the destructive transaction. For Azure SQL Database, restoration creates a database, so validation and controlled application reconnection are part of the recovery plan. Any legitimate later activity also needs an explicit handling decision. The synchronized replica already contains the bad update; promoting it improves neither historical correctness nor recovery to the requested time.

- **A.** The replica already received the committed destructive change, so promoting that current copy does not recover the earlier correct database state.
- **C.** The older backup unnecessarily discards more history when the stated retention supports the required pre-update point and minimal avoidable loss.
- **D.** SQL Database point-in-time restoration creates a database; the team must validate it and manage application connections rather than assuming automatic replacement.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups) · [Review chapter:](../certifications/en/DP-300.md)

</details>

<a id="quiz-q16"></a>

## DP-300 · SQL encryption boundaries

A research application must keep selected participant values unreadable to database administrators querying the tables. Only its trusted client may decrypt them, and administrators must not have the client keys. Which approach best matches that boundary?

- **A.** Enable TDE and give administrators their usual database query access.
- **B.** Require TLS between the client and database, without encrypting selected values at the client boundary.
- **C.** Apply dynamic data masking while retaining administrators' broad query privileges.
- **D.** Use appropriately configured Always Encrypted with a compatible client and separately controlled keys.

<details>
<summary>Why:</summary>

**D. Use appropriately configured Always Encrypted with a compatible client and separately controlled keys.**

Always Encrypted is designed for a boundary in which compatible clients handle sensitive-value encryption and decryption while keys can remain outside the database engine's access. The university must validate driver support, permitted operations, and separate key administration. TDE protects database files at rest, TLS protects the connection, and masking changes query presentation. Those controls alone do not satisfy the specified administrator-exclusion requirement.

- **A.** TDE protects database files at rest; administrators with normal query rights can still obtain plaintext values through the database engine.
- **B.** TLS protects data travelling over the connection, but does not by itself prevent an authorised database administrator from querying stored values.
- **C.** Masking alters result presentation for relevant users; it does not establish a cryptographic boundary against administrators retaining broad database privileges.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/azure-sql/database/security-overview) · [Review chapter:](../certifications/en/DP-300.md)

</details>

<a id="quiz-q17"></a>

## AI-901 · Foundry client identity

A student's Foundry client uses the documented endpoint and deployment name, but no credential is configured for the calling workload. What must the design add to establish an authorised caller?

- **A.** Replace the deployment name with the catalogue model name and leave credentials absent.
- **B.** Configure a supported credential for the workload and grant that identity the minimum required access.
- **C.** Switch from REST to an SDK while leaving the caller unauthenticated.
- **D.** Copy a successful administrator's portal URL into the client as proof of the workload's permission.

<details>
<summary>Why:</summary>

**B. Configure a supported credential for the workload and grant that identity the minimum required access.**

An endpoint identifies where a request goes and a deployment identifies the configured model; neither establishes who is calling. The client needs a supported authentication mechanism, and its resulting identity needs the appropriate minimum permissions. The selected SDK and API generation must also match. Secrets should remain outside notebooks and source code, and a human administrator's portal access does not automatically transfer to the application.

- **A.** A catalogue model name and a deployment name serve different purposes; changing that string does not authenticate the workload or grant access.
- **C.** An SDK wraps supported request contracts, but changing client libraries does not remove the service's authentication and authorisation requirements.
- **D.** A portal URL identifies a location; the administrator's authenticated browser session does not establish the separate workload's identity or permissions.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) · [Review chapter:](../certifications/en/AI-901.md)

</details>

<a id="quiz-q18"></a>

## AI-901 · Grounding and claim support

A notes assistant gives a submission date and cites the right lecture PDF, but the retrieved passage only defines an algorithm. The app must answer dates only from permitted supporting passages. What is the best response?

- **A.** Retrieve a passage that supports the date, or state that the available evidence is insufficient.
- **B.** Accept the date because citing the correct document proves every claim in the answer.
- **C.** Set generation temperature to zero and accept the same date without checking another passage.
- **D.** Accept the date if the model reports high confidence, even though the passage does not support it.

<details>
<summary>Why:</summary>

**A. Retrieve a passage that supports the date, or state that the available evidence is insufficient.**

Grounding requires evidence that supports the particular claim, not merely a citation to a related document. The supplied algorithm definition does not establish a submission date. Retrieval should seek an authorised passage containing the relevant date and its qualifications; otherwise the assistant should abstain. Deterministic generation and self-reported confidence cannot create missing evidence. Evaluation should compare each consequential claim with the actual cited text.

- **B.** A citation to the correct document may still point to an irrelevant passage; document identity alone does not substantiate the stated date.
- **C.** A lower temperature changes generation variability, but cannot turn an algorithm definition into supporting evidence for a missing submission date.
- **D.** Model confidence can be misplaced; the application's explicit evidence rule still requires a permitted passage supporting the particular date claim.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators) · [Review chapter:](../certifications/en/AI-901.md)

</details>

<a id="quiz-q19"></a>

## SC-200 · SOC timeline evidence

Synthetic records for the same verified account show email activity at 10:02 UTC, ingested at 10:20, and a sign-in at 10:08 UTC, ingested at 10:09. Both event clocks are trusted. Which conclusion is supported by these records alone?

- **A.** The sign-in occurred first because its record reached the workspace first.
- **B.** The email caused the sign-in and proves account compromise.
- **C.** The email event time must be discarded because its ingestion was delayed.
- **D.** The email activity preceded the sign-in, while causation and compromise still require more evidence.

<details>
<summary>Why:</summary>

**D. The email activity preceded the sign-in, while causation and compromise still require more evidence.**

Trusted event timestamps place the email activity before the sign-in. Ingestion timestamps describe when records arrived, and different collection delays can reverse their arrival order. Matching a verified account helps correlate the records, but does not establish that the email caused the sign-in or that either event was malicious. The analyst should preserve both time fields, investigate the surrounding activity, and state the limits of the evidence.

- **A.** Ingestion order describes collection arrival rather than activity order; the trusted event timestamps place the email before the sign-in in this dataset.
- **B.** A shared account and temporal sequence support investigation, but do not alone establish a causal link, malicious activity, or confirmed compromise.
- **C.** Delayed ingestion can occur without invalidating a trusted event timestamp; preserve both fields and investigate the delay rather than discarding evidence.

[Microsoft Learn:](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender) · [Review chapter:](../certifications/en/SC-200.md)

</details>

<a id="quiz-q20"></a>

## SC-200 · Response action idempotency

A Sentinel playbook creates a university incident ticket, but the success response is lost. A retry could create another ticket for the same approved action. Which workflow control best addresses this failure?

- **A.** Use a longer timeout and assume a missing response always means no ticket exists.
- **B.** Generate a fresh action identifier for each retry so every request looks independent.
- **C.** Persist an incident/action key and ticket state, then reconcile or reuse the existing result when that action is retried.
- **D.** Deduplicate incoming alert records only, while allowing the ticket-creation step to repeat without state checks.

<details>
<summary>Why:</summary>

**C. Persist an incident/action key and ticket state, then reconcile or reuse the existing result when that action is retried.**

Idempotency means repeating the same logical action preserves its intended result instead of creating another side effect. A durable incident/action key, recorded state, and external ticket reference allow retries to find or reconcile the existing work. A missing response is an unknown outcome until checked. The workflow also needs bounded retries, an accountable owner, and permissions appropriate to ticket creation; alert deduplication alone does not control action execution.

- **A.** A longer timeout may reduce some failures, but a lost response still leaves uncertainty about whether the external ticket was already created.
- **B.** A new identifier makes the retry appear to be new work, preventing the workflow from recognising the already attempted logical action.
- **D.** Alert deduplication controls input records; a retried downstream step can still duplicate tickets unless action execution has its own state checks.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer) · [Review chapter:](../certifications/en/SC-200.md)

</details>

<a id="quiz-q21"></a>

## SC-300 · Conditional Access report-only

A university pilots a Conditional Access policy in report-only mode. Its evaluation shows that a sign-in would not satisfy the proposed grant requirement, yet the sign-in succeeds. No other policy requires that control. What best explains this result?

- **A.** Application permissions always override an enforced Conditional Access denial.
- **B.** The proposed control has already been enforced because report-only evaluates it.
- **C.** Report-only records the policy's evaluation without enforcing its grant requirement.
- **D.** Report-only allows the first failing sign-in and automatically blocks the next one.

<details>
<summary>Why:</summary>

**C. Report-only records the policy's evaluation without enforcing its grant requirement.**

Report-only mode evaluates the policy and records the predicted outcome without applying its controls. A successful sign-in can therefore coexist with evidence that the proposed grant requirement would fail if enforced. The team should inspect expected allowed and denied cases, affected identities, exclusions, and administrator recovery before an approved rollout. Application permissions remain a separate authorisation boundary and do not explain away an enforced Conditional Access failure.

- **A.** Application entitlement does not automatically override an applicable enforced Conditional Access denial; the stated policy mode explains this successful sign-in.
- **B.** Evaluation and enforcement are distinct: report-only records what would happen, so its result does not prove that the grant requirement was applied.
- **D.** Report-only does not introduce a first-attempt allowance followed by automatic enforcement; enforcement requires changing the applicable policy configuration.

[Microsoft Learn:](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only) · [Review chapter:](../certifications/en/SC-300.md)

</details>

<a id="quiz-q22"></a>

## SC-300 · Workload federation claims

A university build job uses workload identity federation. Its token exchange fails, and the external token's subject differs in letter case from the configured federated subject. The issuer and audience match. Which change addresses this identified mismatch?

- **A.** Grant subscription Owner to the workload while leaving the federated subject unchanged.
- **B.** Align the configured subject with the intended incoming claim exactly, then separately verify the identity's minimum resource permissions.
- **C.** Add SCIM user-provisioning mappings for the repository name instead of correcting the federated credential.
- **D.** Increase the external token's lifetime while leaving the mismatched subject unchanged.

<details>
<summary>Why:</summary>

**B. Align the configured subject with the intended incoming claim exactly, then separately verify the identity's minimum resource permissions.**

Federated credentials compare the trusted issuer, subject, and audience with the incoming assertion; these values must match, including case. Correcting the intended subject relationship addresses the stated token-exchange mismatch without introducing a stored client secret. Successful exchange then authenticates the workload, but does not grant arbitrary resource access. The resulting identity still requires separately assigned, appropriately scoped permissions for the build's actual operations.

- **A.** Resource permissions govern what an authenticated identity may do; a broad role does not repair a mismatched claim that prevents token exchange.
- **C.** SCIM concerns account provisioning and attributes; it does not replace the federated issuer, subject, and audience checks in this workload token exchange.
- **D.** Changing lifetime addresses token validity duration, but does not make the case-sensitive subject claim match the configured federated credential.

[Microsoft Learn:](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) · [Review chapter:](../certifications/en/SC-300.md)

</details>

<a id="quiz-q23"></a>

## AZ-140 · AVD profile permissions

A student can launch an assigned pooled Azure Virtual Desktop session, but FSLogix receives access denied on the student's SMB profile folder. Share-level access is present, while the folder's NTFS permissions deny the student. Which fix best addresses the evidence?

- **A.** Correct the folder's NTFS permissions with appropriate user isolation, then validate profile attachment as that student.
- **B.** Grant the student a broader Azure control-plane Contributor role without changing the folder permissions.
- **C.** Reassign the desktop application group and assume that assignment also grants NTFS profile access.
- **D.** Reimage the session host while preserving the same profile path and denying NTFS permissions.

<details>
<summary>Why:</summary>

**A. Correct the folder's NTFS permissions with appropriate user isolation, then validate profile attachment as that student.**

SMB profile access depends on both share-level access and filesystem permissions. The stated evidence identifies NTFS denial, so correcting the intended folder access while preserving other students' isolation addresses the immediate failure. Test using the affected identity and inspect FSLogix attachment evidence. Desktop entitlement and Azure resource administration are different boundaries; successful session launch does not establish permission to read and write the persistent profile.

- **B.** A control-plane management role does not itself correct the identified NTFS denial on the SMB folder used for the student's profile.
- **C.** Application-group assignment makes the desktop available to the user, but does not by itself grant the required filesystem access to profile storage.
- **D.** Replacing the host while retaining the same denied folder access leaves the identified storage permission failure in the new session path.

[Microsoft Learn:](https://learn.microsoft.com/en-us/fslogix/how-to-configure-storage-permissions) · [Review chapter:](../certifications/en/AZ-140.md)

</details>

<a id="quiz-q24"></a>

## AZ-140 · AVD failure headroom

A synthetic AVD lab needs 60 simultaneous student sessions. Testing supports at most 10 sessions per healthy host. All hosts must be ready before class, and capacity must still support 60 sessions after any one host fails. What is the minimum number of ready hosts?

- **A.** Six hosts.
- **B.** Five hosts.
- **C.** Eight hosts.
- **D.** Seven hosts.

<details>
<summary>Why:</summary>

**D. Seven hosts.**

Six healthy hosts are required for the measured normal demand: 60 divided by 10 sessions per host. One additional ready host provides the stated single-host failure headroom, leaving six hosts after a failure. Seven is therefore the minimum under these explicit assumptions. The real scaling plan must also consider boot time, drain state, unhealthy capacity, storage sign-in load, and permissions; starting a stopped host later does not satisfy the ready-before-class requirement.

- **A.** Six hosts meet demand only while all remain healthy; losing one leaves capacity for 50 sessions under the measured per-host limit.
- **B.** Five hosts provide only 50 sessions even before a failure, so they cannot support the stated 60 simultaneous students under these assumptions.
- **C.** Eight hosts would meet the requirement, but seven already preserve six healthy hosts after one failure, making eight larger than the minimum.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/virtual-desktop/autoscale-create-assign-scaling-plan) · [Review chapter:](../certifications/en/AZ-140.md)

</details>

<a id="quiz-q25"></a>

## AI-103 · Retrieval access revocation

A student loses permission to a research notebook, but an assistant still has cached passages from it. Policy requires current access before any passage reaches the model. The application cannot establish current permission freshness. Which behaviour meets the policy?

- **A.** Send the cached passage but remove its citation so the notebook is not named.
- **B.** Continue serving the cached passage until the next scheduled index refresh.
- **C.** Send the passage with a prompt telling the model not to reveal material the student cannot access.
- **D.** Withhold the passage until access can be verified, and apply current authorisation checks to retrieval and cache results.

<details>
<summary>Why:</summary>

**D. Withhold the passage until access can be verified, and apply current authorisation checks to retrieval and cache results.**

The policy places authorisation before model access, including cached content. When permission freshness cannot be established, withholding the passage preserves that boundary. The application must validate the chosen retrieval and cache design against revocations, group changes, and stale indexes. A prompt or missing citation cannot undo disclosure of an unauthorised passage to the model. Native permission features and custom filters require separate capability and enforcement checks.

- **A.** Removing a citation changes presentation, but the unauthorised notebook content would still reach the model and remain available for answer generation.
- **B.** A scheduled refresh leaves an access gap that violates the stated current-permission policy, especially when cached passages survive index changes.
- **C.** A prompt delegates an access decision to generation after disclosure; it cannot enforce the required boundary before the passage reaches the model.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) · [Review chapter:](../certifications/en/AI-103.md)

</details>

<a id="quiz-q26"></a>

## AI-103 · Unknown tool outcomes

An approved agent tool requests creation of one research-note share. The backend accepts a stable operation key, but the response times out and the share may already exist. A status lookup is available. What should the application do next?

- **A.** Record an unknown outcome, reconcile status using the operation key, and reuse that key if a supported retry is needed.
- **B.** Immediately retry with a new operation key so the backend treats the request as a fresh action.
- **C.** Mark the operation definitely failed and discard its key because no response arrived.
- **D.** Ask the model to infer success from its earlier tool request and report completion without checking the backend.

<details>
<summary>Why:</summary>

**A. Record an unknown outcome, reconcile status using the operation key, and reuse that key if a supported retry is needed.**

A timeout after submission does not establish whether the side effect occurred. Keeping an explicit unknown state and stable operation key allows the application to query the backend and reconcile the result before another write. If retry is supported, the same logical key preserves the intended idempotency boundary. Approval and argument validation still apply; the model's proposed call is not evidence that the backend completed the authorised share.

- **B.** A fresh key makes the retry a distinct operation, which can create another share if the first request already committed successfully.
- **C.** No response means the outcome is uncertain, not definitely failed; discarding the key also removes the available handle for reconciliation.
- **D.** The generated tool request describes intended work; only backend evidence can confirm whether the requested share was actually created.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/architecture/patterns/asynchronous-request-reply) · [Review chapter:](../certifications/en/AI-103.md)

</details>

<a id="quiz-q27"></a>

## DP-700 · Incremental delete ordering

A Fabric enrolment load processes source change sequence 98, which deletes enrolment E. A delayed update for E with sequence 94 arrives afterward. Source sequences define authoritative order, and a later legitimate re-enrolment is possible. Which merge rule preserves the correct state?

- **A.** Apply update 94 because it arrived most recently at the pipeline.
- **B.** Ignore every future change for E permanently once any deletion is observed.
- **C.** Retain deletion/version information for sequence 98 and reject update 94 as older, while allowing a valid newer change.
- **D.** Discard the checkpoint and replay changes strictly in arrival order without version comparisons.

<details>
<summary>Why:</summary>

**C. Retain deletion/version information for sequence 98 and reject update 94 as older, while allowing a valid newer change.**

The source sequence determines business ordering, so update 94 must not resurrect an enrolment deleted at sequence 98. Retaining the deletion and its version allows an idempotent merge to reject stale changes while still accepting a valid later version. Arrival time is not authoritative here. Stable keys, deterministic version comparisons, and durable progress are needed together; rerunning input without those rules does not repair the ordering problem.

- **A.** Arrival order can differ from source change order; applying the older update would incorrectly resurrect an enrolment deleted by the newer change.
- **B.** A permanent ban would also reject a valid later re-enrolment; the merge must compare versions rather than prohibit all future changes for that key.
- **D.** Replaying the same arrival order without version checks can reproduce the resurrection; checkpoint removal alone does not establish authoritative business ordering.

[Microsoft Learn:](https://learn.microsoft.com/en-us/fabric/data-engineering/delta-lake-change-data-feed) · [Review chapter:](../certifications/en/DP-700.md)

</details>

<a id="quiz-q28"></a>

## DP-700 · Fabric access paths

A university report correctly applies row-level restrictions and has a sensitivity label. The same analyst can read underlying student-level files directly through an authorised OneLake path. Policy permits only module totals. What should the engineer change and validate?

- **A.** Rename the label Highly Confidential and assume its name enforces the report's row restrictions on direct file reads.
- **B.** Restrict the underlying access path to the minimum required permissions and test permitted totals and denied detail as the analyst.
- **C.** Hide the detailed table in the report while leaving the analyst's direct file permissions unchanged.
- **D.** Grant a broader workspace role so the report's existing row restrictions govern every access route automatically.

<details>
<summary>Why:</summary>

**B. Restrict the underlying access path to the minimum required permissions and test permitted totals and denied detail as the analyst.**

A restriction enforced by a report or query engine does not automatically govern a separate direct-file route. The engineer must align workspace, item, engine, and file permissions with the policy and test each intended access path using the analyst's identity. A sensitivity label supplies governance context or configured protection, but its name alone does not implement equivalent authorisation everywhere. Broader permissions can expose additional routes instead of closing this gap.

- **A.** Changing a classification name does not configure the separate file-access boundary or make report-engine row restrictions automatically apply through OneLake.
- **C.** Hiding report content changes that presentation only; the analyst retains the stated direct route to the underlying student-level files.
- **D.** A broader workspace role expands access and does not turn the report's row restrictions into a universal rule for every engine and file path.

[Microsoft Learn:](https://learn.microsoft.com/en-us/fabric/security/permission-model) · [Review chapter:](../certifications/en/DP-700.md)

</details>

<a id="quiz-q29"></a>

## SC-100 · Residual risk ownership

An architect documents that a proposed university notes platform still has a material outage risk after feasible controls. The security team recommends proceeding, but governance requires business risk acceptance. Who should authorise accepting that residual risk?

- **A.** The SOC analyst who can close the related security ticket.
- **B.** The accountable business risk owner with the required decision authority, recording the exposure and review conditions.
- **C.** The product vendor, because its compliance score replaces the university's business decision.
- **D.** The cloud administrator, solely because that administrator can deploy the resources.

<details>
<summary>Why:</summary>

**B. The accountable business risk owner with the required decision authority, recording the exposure and review conditions.**

Residual risk remains a business exposure even after technical controls are selected. The authorised, accountable risk owner should decide whether that exposure is acceptable, using the architect's evidence about impact, likelihood assumptions, alternatives, and remaining gaps. The decision should include scope, review conditions, and ownership. Security recommendations, resource deployment rights, and vendor assessments inform the decision but do not automatically confer the university's required risk-acceptance authority.

- **A.** Closing an operational ticket is a workflow permission; it does not establish authority to accept material business exposure for the university.
- **C.** A vendor assessment can inform control selection, but cannot substitute for the university's accountable decision about its own remaining operational risk.
- **D.** The ability to deploy resources is technical authority; the scenario separately requires an authorised business owner to accept the residual outage risk.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/govern/assess-cloud-risks) · [Review chapter:](../certifications/en/SC-100.md)

</details>

<a id="quiz-q30"></a>

## SC-100 · Recovery objective validation

A recovery exercise sets a two-hour RTO and a 15-minute RPO. An outage begins at 11:00 UTC. Authorised document reads resume at 12:30, with data recovered only through 10:40. Assume these are the agreed measurement boundaries. Which assessment is correct?

- **A.** Both objectives are met because service resumed within two hours.
- **B.** The RPO is met, but the RTO is missed.
- **C.** Both objectives are missed because any data loss breaches the RTO.
- **D.** The RTO is met, but the RPO is missed because the recovery point is 20 minutes before the outage.

<details>
<summary>Why:</summary>

**D. The RTO is met, but the RPO is missed because the recovery point is 20 minutes before the outage.**

RTO measures acceptable interruption: authorised reads resume after 90 minutes, within the two-hour target. RPO measures acceptable recent data loss: recovery through 10:40 for an 11:00 outage leaves a 20-minute gap, exceeding the 15-minute target. These are independent checks, and satisfying one does not satisfy the other. The exercise should record both measurements and the dependencies that allowed the defined business operation to resume.

- **A.** Restoring the service within its time target satisfies the RTO only; the separate 20-minute recovery-point gap still exceeds the stated RPO.
- **B.** The elapsed interruption is 90 minutes, within two hours, while the 20-minute data gap exceeds 15 minutes; this option reverses the results.
- **C.** RTO concerns interruption duration rather than whether any data is lost; the measured 90-minute recovery meets that target despite the RPO miss.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recover-hadr-overview) · [Review chapter:](../certifications/en/SC-100.md)

</details>

<a id="quiz-q31"></a>

## AZ-120 · SAP fencing and single writers

During a SAP HANA cluster tabletop, communication with the primary is lost and the secondary cannot fence it. The team cannot confirm that the primary has stopped accepting writes. Which response best preserves data integrity before takeover?

- **A.** Disable fencing and promote the secondary so the cluster dashboard immediately shows resources running.
- **B.** Promote the secondary because the last successful replication status proves the old primary cannot still write.
- **C.** Follow the supported incident procedure to restore or verify fencing and confirm isolation of the old writer before permitting takeover writes.
- **D.** Move the virtual service address to the secondary while leaving the uncertain primary's write capability unchanged.

<details>
<summary>Why:</summary>

**C. Follow the supported incident procedure to restore or verify fencing and confirm isolation of the old writer before permitting takeover writes.**

Lost communication does not prove that the primary has stopped. Fencing isolates a node that cannot safely continue, protecting the single-writer requirement and reducing split-brain risk. The team must investigate the supported fencing and quorum arrangement, preserve state evidence, and establish that the old writer is isolated before allowing takeover writes. Replication health and moving an address do not supply that isolation, while disabling fencing removes a critical safety mechanism.

- **A.** Disabling fencing removes the mechanism needed to isolate an uncertain writer, so apparent availability can come at the cost of conflicting primaries.
- **B.** A previous replication result describes data movement at that time; it does not prove the unreachable primary has stopped accepting writes now.
- **D.** Moving a virtual address changes a client path, but does not itself prevent the old primary from writing through other sessions or paths.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/sap/workloads/sap-hana-high-availability) · [Review chapter:](../certifications/en/AZ-120.md)

</details>

<a id="quiz-q32"></a>

## AZ-120 · SAP writes after cutover

A university SAP migration opens the target for purchasing, and users create new purchase orders. The unchanged source remains isolated. A later validation issue triggers consideration of rollback. Which plan best protects the new business transactions?

- **A.** Freeze writes, establish the authoritative data state, preserve the target transactions, and agree a supported reconciliation or reverse-migration plan before reopening a writer.
- **B.** Point DNS back to the unchanged source and assume the target's new purchase orders are present there.
- **C.** Overwrite the target from the old source, then reopen purchasing without identifying transactions created after cutover.
- **D.** Reopen both source and target for writes while business users decide which purchase orders to keep later.

<details>
<summary>Why:</summary>

**A. Freeze writes, establish the authoritative data state, preserve the target transactions, and agree a supported reconciliation or reverse-migration plan before reopening a writer.**

Once the target accepts new writes, rollback becomes a data-handling decision as well as an infrastructure change. Returning to an unchanged source can abandon new orders, while reopening both sides can fork transactions. The runbook should freeze writes, preserve evidence and new business data, select an authoritative state, and use supported reconciliation or reverse movement with the responsible business owners. Validation and single-writer control precede reopening purchasing.

- **B.** DNS redirects clients but does not copy post-cutover orders into the unchanged source; switching back alone can abandon those new transactions.
- **C.** Overwriting from the stale source can destroy legitimate target orders; the plan must first identify and preserve business changes made after cutover.
- **D.** Allowing both landscapes to accept writes creates divergent transaction histories, making reconciliation harder and breaking the required control of an authoritative writer.

[Microsoft Learn:](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/migrate/execute-migration) · [Review chapter:](../certifications/en/AZ-120.md)

</details>
