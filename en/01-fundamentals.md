# Cloud fundamentals

Cloud computing lets us request compute, storage, and other services through software interfaces. Servers, networks, and disks still exist underneath. What changes is who operates them and how we access them.

## Concepts to separate

- **Scalability:** the ability to increase or decrease resources.
- **Elasticity:** adapting resources to demand, usually through automation.
- **High availability:** reducing interruptions through redundancy and recovery mechanisms.
- **Disaster recovery:** restoring service after a serious incident.
- **Vertical scaling:** more capacity in one instance.
- **Horizontal scaling:** more instances.

An application that keeps state only in memory can break when requests reach different instances. Before scaling, inspect session handling, files, and connections.

## IaaS, PaaS, and SaaS

| Model | What we manage | Example |
|---|---|---|
| IaaS | Operating system, applications, data, and configuration | Virtual Machines |
| PaaS | Application, data, and available configuration | App Service |
| SaaS | Users, data, and product settings | Microsoft 365 |

Microsoft handles physical infrastructure. Customers retain responsibilities for data, identities, and configuration, including in SaaS.

## Public, private, and hybrid

Public cloud provides a vendor's services. Private cloud dedicates infrastructure to one organisation. A hybrid solution integrates on-premises or private infrastructure with public cloud.

**Class project:** PaaS can save us server setup when we only need an API. A VM makes more sense when the assignment is about configuring Linux.

**Common mistake:** assuming cloud means cheap. Flexibility helps, but usage still needs measuring.

**Review:** is adding more CPU horizontal scaling? No, it is vertical.

## Worked example: adding instances is not the entire fix

We have two API instances and a database with limited connections. Doubling the API could increase pressure on the database. Measure connections, query duration, CPU, and waiting time before scaling.

If the API keeps files on local disk, another instance may not find them. Horizontal scaling calls for suitable shared storage and a review of sessions and background work.

Compare behaviour before and after under representative load. Checking that four instances exist verifies deployed capacity, not user improvement.

### Cost versus control

A VM's hourly price may look lower than a managed alternative. Include patching, backups, monitoring, and recovery effort. Managed services can save work but have capacity minimums and relevant limits.

**Exercise:** change the requirement from a standard API to an application installing custom drivers. Explain why platform choice changes even with the same users.

---

[Contents](README.md) · [Other language](../es/01-fundamentals.md) · [Next](02-resources.md)
