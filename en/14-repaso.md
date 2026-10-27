# Review with answers

Try answering before expanding each solution. These are original study questions, not official exam questions.

## 1. What responsibility remains with SaaS?

<details>
<summary>Show answer</summary>

Managing identities, access, data, and available product settings appropriately.

</details>

## 2. Is adding instances vertical or horizontal scaling?

<details>
<summary>Show answer</summary>

Horizontal. Increasing one instance's capacity is vertical.

</details>

## 3. Can a resource group contain resources in different regions?

<details>
<summary>Show answer</summary>

Yes. Its location does not force all its resources into the same region.

</details>

## 4. Do two VMs guarantee tolerance of a zone failure?

<details>
<summary>Show answer</summary>

No. Placement, configuration, and application dependencies matter.

</details>

## 5. When would you choose App Service over a VM?

<details>
<summary>Show answer</summary>

When the runtime and requirements fit and we want less operating system administration.

</details>

## 6. Does a container require Kubernetes?

<details>
<summary>Show answer</summary>

No. Alternatives include Container Instances, Container Apps, and other container-capable platforms.

</details>

## 7. Where would you store PDFs and their metadata?

<details>
<summary>Show answer</summary>

PDFs in Blob Storage; queryable metadata in a suitable database.

</details>

## 8. Is ZRS equivalent to backup?

<details>
<summary>Show answer</summary>

No. Zone redundancy alone does not restore earlier deleted or damaged versions.

</details>

## 9. Is VNet peering transitive?

<details>
<summary>Show answer</summary>

Not automatically. A-B and B-C do not imply A-C connectivity.

</details>

## 10. Does a Private Endpoint disable public access?

<details>
<summary>Show answer</summary>

Not necessarily. Check the service's public access settings and DNS.

</details>

## 11. Can Contributor always read blobs?

<details>
<summary>Show answer</summary>

No. Management actions and data actions are authorised separately.

</details>

## 12. What does managed identity provide?

<details>
<summary>Show answer</summary>

Workload authentication to supported services without storing application credentials; it still needs permissions.

</details>

## 13. Policy or RBAC to require tags?

<details>
<summary>Show answer</summary>

Policy. RBAC controls who can perform actions.

</details>

## 14. Does assigning a policy fix all existing resources?

<details>
<summary>Show answer</summary>

No. It depends on the effect, permissions, and remediation tasks.

</details>

## 15. Does low CPU prove an API is healthy?

<details>
<summary>Show answer</summary>

No. It may be waiting on a database, network, or slow dependency.

</details>

## 16. Does a budget guarantee a spending cap?

<details>
<summary>Show answer</summary>

No. It supports tracking and alerts, not a universal automatic spending limit.

</details>

## 17. Does deallocating a VM remove all its costs?

<details>
<summary>Show answer</summary>

No. Disks and other resources may continue generating charges.

</details>

## 18. How do RTO and RPO differ?

<details>
<summary>Show answer</summary>

RTO: target recovery time. RPO: tolerable data loss measured in time.

</details>

## 19. Why make a consumer idempotent?

<details>
<summary>Show answer</summary>

Because messages may be delivered or processed repeatedly without their effects needing duplication.

</details>

## 20. Are Event Grid and Event Hubs interchangeable?

<details>
<summary>Show answer</summary>

No. Event Grid distributes events; Event Hubs ingests event streams with a different consumption model.

</details>

## 21. Does OIDC work by adding one workflow line?

<details>
<summary>Show answer</summary>

No. Federated trust and permissions must be configured in Azure and the workflow.

</details>

## 22. Does rolling back code reverse a data migration?

<details>
<summary>Show answer</summary>

Not necessarily. Data compatibility and recovery need deliberate design.

</details>

## 23. Does compiling Bicep prove deployment will succeed?

<details>
<summary>Show answer</summary>

No. It does not establish quotas, permissions, policies, or all regional availability.

</details>

## 24. What would you check before deleting a group?

<details>
<summary>Show answer</summary>

That it is the lab's dedicated group and which resources it contains. Deletion affects all its resources.

</details>
