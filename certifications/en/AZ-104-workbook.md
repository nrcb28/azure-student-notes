# AZ-104 · Shared advanced workbook

[←](README.md) · [Common study core](../../en/16-common-core.md) · [Advanced labs](../../en/17-advanced-labs.md)

This block has the same objectives, scenarios, and deliverables in all eight languages. Equivalence is checked by learning units and evidence, not word count. Earlier guides remain complementary explanations.

<a id="az-104-unit-1"></a>

## 1. Trace effective access

Record identity, tenant, subscription, resource, action, and scope. Check groups, direct assignments, inheritance, conditions, and propagation. Distinguish management and data actions. Assigning roles requires its own permissions; Contributor is not automatically an access administrator.

**Case:** an account creates Storage but cannot list blobs. **Evidence:** explain the necessary permission and a minimal check using the same identity. Do not use Owner as a general test or change networking without a hypothesis.

<a id="az-104-unit-2"></a>

## 2. Protect and recover data

Choose protection at object, container, and account levels. Record what was enabled before the incident. With versioning, restoration may require selecting or promoting a version; one procedure does not fit every configuration.

**Case:** a lab file is deleted and must return unchanged. **Evidence:** prior configuration, hashes before and after, permission checks, and data still retained after cleanup.

<a id="az-104-unit-3"></a>

## 3. Read infrastructure before changing it

Interpret parameters, resources, dependencies, outputs, and proposed differences. Separate compilation, validation, what-if, and application. Exported infrastructure may need work before reuse. Quotas, regions, and policies can block valid syntax.

**Case:** what-if cannot analyse a module. **Evidence:** diagnostics, unevaluated scope, and a decision to resolve it before applying. Review disks, networking, and settings when resizing or moving VMs.

<a id="az-104-unit-4"></a>

## 4. Diagnose the complete path

Follow DNS, IP, route, NSG, guest firewall, listener, and application authorisation. Rules are stateful and several layers can filter. Validate load balancer frontend, backend, rule, and probe. Separate App Service private ingress from outbound integration.

**Case:** healthy probe, failed real request. **Evidence:** each check's port and response, applicable rules, and a testable hypothesis. Probe health does not establish functional correctness.

<a id="az-104-unit-5"></a>

## 5. Operate with evidence

Define metric, log, alert, action, and owner. Verify collection source, association, and destination before blaming the query. For backup and Site Recovery, measure application recovery including identity, DNS, and dependencies.

**Final submission:** run Storage and role-inspection labs, record expected versus observed, and propose a recovery runbook. Separate local checks from Azure tests and verify deletion or residual retention.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104) · [AZ-104](AZ-104.md)
