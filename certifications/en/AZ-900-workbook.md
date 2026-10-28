# AZ-900 · Shared advanced workbook

[←](README.md) · [Common study core](../../en/16-common-core.md) · [Advanced labs](../../en/17-advanced-labs.md)

This block has the same objectives, scenarios, and deliverables in all eight languages. Equivalence is checked by learning units and evidence, not word count. Earlier guides remain complementary explanations.

<a id="az-900-unit-1"></a>

## 1. Allocate responsibilities

Compare a VM, a managed platform, and existing subscribed software for the same API need. List operating system, dependencies, data, access, and recovery. None is responsibility-free. Required control and the team's operating capacity decide.

**Case:** a library requires a system driver. Explain which option stops fitting and why. **Evidence:** a responsibility matrix and an alternative rejected because of a specific requirement.

<a id="az-900-unit-2"></a>

## 2. Availability and boundaries

Distinguish process, instance, zone, and region failure. Several instances can share critical dependencies. Explain sessions and documents when requests move between instances. A component SLA is not the whole application's availability.

**Case:** four APIs rely on one database without defined recovery. **Evidence:** a complete request path, the weak dependency, and a proposed validation.

<a id="az-900-unit-3"></a>

## 3. Data and connectivity choices

Separate objects, relational metadata, and shared files. Define reading, writing, authorisation, and recovery for each. Public does not imply anonymous; private DNS does not grant permission. A successful connection alone grants no data access.

**Case:** a teacher opens a document link while another user receives 403. **Evidence:** separate network, identity, and authorisation hypotheses and the observation that would confirm each.

<a id="az-900-unit-4"></a>

## 4. Govern and estimate

Use RBAC for identity actions, Policy for resource conditions, and tags for classification. Budgets track and alert rather than universally stopping costs. Estimate capacity, operations, transfer, logs, and backups with explicit assumptions.

**Case:** deploy only in approved regions and attribute spending by faculty. **Evidence:** a governance rule, minimal role, and cost-unit table without invented rates.

<a id="az-900-unit-5"></a>

## 5. Explain and verify

Distinguish deployment, functionality, and recovery. Creating resources does not prove student downloads work. Creating a backup does not prove timely restoration. Use business signals alongside CPU.

**Final submission:** application diagram, five justified decisions, tolerated failure, remaining responsibilities, and cleanup plan. Repeat with a changed requirement. If the answer never changes, check whether you are actually reasoning.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) · [AZ-900](AZ-900.md)
