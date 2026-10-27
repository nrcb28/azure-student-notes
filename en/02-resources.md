# Resources and availability

Azure Resource Manager is the management layer used to deploy and manage resources. The portal, Azure CLI, and templates use this layer.

## Organisation

- **Microsoft Entra tenant:** the identity directory associated with subscriptions.
- **Management group:** a scope for governing several subscriptions.
- **Subscription:** a boundary for administration, quotas, and billing.
- **Resource group:** resources sharing a related lifecycle.
- **Resource:** a network, database, VM, and so on.

A tenant is not a resource container in the same sense as a resource group. Permissions can inherit from management groups down to resources, depending on the assignment scope.

A resource belongs to one resource group at a time. Moving resources has restrictions: support varies by resource type.

## Regions and zones

A region is a geographical area containing data centres. An availability zone contains one or more data centres with independent power, cooling, and networking within a region.

- A resource group's location applies to its metadata; its resources can be elsewhere.
- Zone support depends on the service and region.
- Two instances are not necessarily distributed across zones.
- Paired regions do not imply automatic replication for every resource.

## SLAs and locks

An SLA defines a service's commitments and conditions. Application availability also depends on design and dependencies.

Management locks can prevent accidental changes or deletion. They do not replace RBAC or backups, and their effects do not cover every data operation.

**Class project:** separate development and production resource groups make cleanup easier. Separate subscriptions can provide stronger administrative isolation.

**Review:** must a VM use its resource group's region? No.

## Lifecycle example

The test website and its storage are created and removed together, so grouping them makes sense. A network shared by several projects may need separate ownership and a separate group: deleting it with one application would affect others.

Tags can identify owners and environments but require maintenance. Do not assume group tags automatically appear on every resource.

## Before moving a resource

Check resource-type support, dependencies, destination, and permissions. Identifiers may change, affecting automation. Changing regions is not equivalent to changing groups.

Destination locks and policies can also matter. Validation reduces surprises but does not establish universally impact-free moves.

**Exercise:** two faculties need separate spending without breaking shared networking. Propose boundaries for billing, administration, and lifecycle.

---

[Contents](README.md) · [Other language](../es/02-resources.md) · [Previous](01-fundamentals.md) · [Next](03-compute.md)
