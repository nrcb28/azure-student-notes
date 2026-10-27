# Costs and optimisation

I would not choose an architecture based only on a service's headline price. Storage, operations, networking, monitoring, and maintenance time also count.

## What contributes to the bill

- Allocated or consumed compute capacity, depending on the service.
- Storage space and operations.
- Applicable network transfer and processing.
- Databases, backups, and retention.
- Log ingestion and retention.
- Licences and additional plans.

Rates depend on region, currency, agreement, and time. These notes do not include fixed prices.

## Tools

The pricing calculator helps estimate scenarios. Cost Management analyses actual spending and trends. Budgets can alert at thresholds, but do not automatically stop all resources.

Billing data can be delayed. I would not rely on budgets alone to prevent unexpected spending.

## Decisions that help

1. Measure usage before increasing size.
2. Remove test resources that are no longer needed.
3. Choose retention and redundancy based on requirements.
4. Schedule shutdown or deallocation where appropriate.
5. Consider consumption commitments only for sufficiently predictable workloads.

Reservations and savings plans have different conditions: do not assume they cover every resource or usage pattern. Spot capacity can suit interruptible work, but may be reclaimed.

## The VM trap

Shutting down from the operating system can leave a VM allocated. Deallocation stops the corresponding compute charges, but disks and other resources can still cost money.

**Class project:** an oversized lab service may cost more from being forgotten than from the actual exercise.

**Review:** does zero traffic mean zero cost? It depends on the service and plan.

---

[Contents](README.md) · [Other language](../es/09-costs.md) · [Previous](08-observability.md) · [Next](10-architecture.md)
