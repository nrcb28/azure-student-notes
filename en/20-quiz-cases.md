# Eight scenarios to practise

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
