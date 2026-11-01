# AZ-700 · Common advanced workbook

[Guide](AZ-700.md) · [10 cases](AZ-700-cases.md) · [Contents](README.md) · [Network lab](network-lab.md)

Five units with matching objectives, scenarios, and deliverables across eight languages. These are design and diagnostic exercises. Predictions are not Azure observations, and no new deployment is claimed.

<a id="az-700-unit-1"></a>

## 1. Build an address and dependency plan

Design campus, hub, web, and data networks for the notes app. Inventory existing ranges before choosing new CIDRs, and reserve room for growth and service-specific subnets. Explain why an ordinary /24 has fewer assignable Azure IPv4 addresses than its raw address count. Do not assume a delegated service fits any empty subnet.

**Scenario:** a partner uses a range that overlaps the proposed hub. **Evidence:** a table of owner, prefix, purpose, constraints, and growth allowance. **Deliverable:** a revised nonoverlapping design, the conflict you removed, and one constraint that still needs checking in current service documentation.

<a id="az-700-unit-2"></a>

## 2. Trace a request and its reply

Draw an API call from a web spoke through an inspection appliance to a destination in another network. Write the destination prefix, next hop, and relevant forwarding setting at each step. Draw the response separately; stateful inspection and address translation can make a superficially plausible asymmetric route fail. Peering alone does not make a hub a transit router.

**Scenario:** the source sends requests but receives no response after a UDR change. **Evidence:** competing routes and the effective next hop in each direction. **Deliverable:** one testable hypothesis, a confirming observation, and a rollback condition for a proposed change.

<a id="az-700-unit-3"></a>

## 3. Diagnose private access in layers

Describe how a campus client resolves a storage hostname through the chosen DNS and forwarding design. Identify the private endpoint's service subresource, private address, approval state, and intended network restrictions. Keep name resolution, reachability, TLS, and data permissions separate: proving one does not prove the others.

**Scenario:** public access is disabled and the caller still resolves a public address. **Evidence:** the hostname, resolver path, returned address, and expected private destination. **Deliverable:** a DNS correction proposal and the subsequent checks for routing and authenticated data access. Explain why a permanent public-IP override is unsuitable.

<a id="az-700-unit-4"></a>

## 4. Choose delivery and protection controls

Compare a TCP service, a regional web app, and a global web app. Select delivery candidates by protocol, scope, routing requirements, and failure behaviour rather than by one remembered product label. Include probe behaviour and certificate handling. Distinguish DNS selection from request proxying, and WAF inspection from network filtering and DDoS availability protection.

**Scenario:** a backend passes its health probe while document downloads are wrong. **Evidence:** what the probe tests and what a real operation validates. **Deliverable:** a short decision record with one rejected alternative and a functional signal that would stop promotion of a faulty release.

<a id="az-700-unit-5"></a>

## 5. Design and verify hybrid recovery

Plan primary and backup campus connectivity. List correlated failures, routing changes, encryption requirements, capacity, and application dependencies. ExpressRoute privacy does not establish encryption by default. Specify the required protection boundary and a compatible encryption design; do not assume all circuit types support the same options.

**Scenario:** the primary connection fails while many students download notes. **Evidence:** expected forward and return paths, backup capacity assumptions, and measurable application recovery criteria. **Deliverable:** an isolated test plan, return-to-normal steps, and expected-versus-observed columns. If no authorised environment is available, submit the design and leave observation fields explicitly untested.

[Official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700) · [Technical explanations](AZ-700.md)
