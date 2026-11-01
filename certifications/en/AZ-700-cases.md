# AZ-700 · 10 cases with reasoned answers

[Guide](AZ-700.md) · [Workbook](AZ-700-workbook.md) · [Contents](README.md)

Original scenarios for learning, not official or leaked exam items. State the requirement, rule out an alternative, and identify evidence before revealing the answer. No Azure execution is claimed.

## 1. The campus and a new Azure VNet both use 10.70.0.0/16. Can ordinary peering or a VPN make their addresses unambiguous?

<details>
<summary>Reasoning</summary>

Overlapping ranges are a design problem, not a missing allow rule. Inventory the actual networks and choose nonoverlapping space before building standard peering or hybrid connectivity. Depending on the scenario, supported translation designs exist, but they add constraints and should be designed explicitly. A packet addressed to the same private range cannot communicate the intended location by its address alone. Evidence would include a range inventory, a revised address plan, and expected routes for each destination.

</details>

## 2. A peers with B, and B peers with C. A still cannot reach C. Should you grant the source VM Owner?

<details>
<summary>Reasoning</summary>

No. VNet peering is not automatically transitive, and an Azure management role does not supply a missing network path. Decide whether direct connectivity or a supported transit design is required. Inspect routes, forwarding and security in both directions. If a shared gateway is involved, check its specific transit settings rather than assuming it forwards all spoke traffic. The useful evidence is a complete packet path and effective next hops, not a broader management role.

</details>

## 3. A new default route points to a firewall, but traffic to a more-specific prefix goes elsewhere. Is every user-defined route broken?

<details>
<summary>Reasoning</summary>

Not necessarily. Inspect all applicable routes and the actual destination. A broad default route must not be assumed to override every more-specific route. Compare prefixes, route origin, and the effective next hop according to Azure's route-selection rules. Also confirm that the intended route table is associated with the source subnet. Evidence should show the competing prefixes and observed next hop. Changing security rules cannot establish which route was selected.

</details>

## 4. Requests traverse a stateful appliance, but responses use a different path. Why can a permitted connection still fail?

<details>
<summary>Reasoning</summary>

A stateful device can require seeing both sides of a connection. With asymmetric routing, the returning traffic may miss the device that recorded the original flow or reach a device with no matching state. Inspect forward and return routes, appliance forwarding, and any address translation. Do not add random inbound allowances before testing this hypothesis. A useful delivery is a diagram containing both paths and observations from the relevant endpoints or supported diagnostic tools.

</details>

## 5. Public storage access is disabled. The API has a private endpoint available but still resolves the public address. What comes first?

<details>
<summary>Reasoning</summary>

Investigate the API client's actual DNS path: server settings, private zone, VNet link, and any hybrid forwarding. Keep using the service hostname and make it resolve appropriately for the intended private connection. Assigning Storage Blob Data Reader cannot correct a public DNS answer. After resolution and routing work, verify data authorisation separately. Record the hostname, resolved address, resolver used, endpoint subresource, and a subsequent authenticated operation as different pieces of evidence.

</details>

## 6. A requirement says that campus-to-Azure data must be encrypted. Does buying ExpressRoute alone establish that property?

<details>
<summary>Reasoning</summary>

No. ExpressRoute's private connectivity is distinct from encryption, and its traffic is not encrypted by default. Specify what needs protection and where it begins and ends. MACsec is a supported option for ExpressRoute Direct links; it is not automatically available on every provider circuit. An appropriate IPsec design can address an end-to-end requirement. Compare compatibility and performance, and document key operations. A private path diagram alone is insufficient encryption evidence.

</details>

## 7. A team needs DNS-based regional selection and expects every request to pass through Traffic Manager. What should be corrected?

<details>
<summary>Reasoning</summary>

Traffic Manager supplies DNS-based endpoint selection; it does not act as the request proxy. The client connects to the selected destination, and caching can delay how quickly a DNS change affects that client. If the design needs global HTTP proxy delivery, evaluate Azure Front Door against the requirements. For a regional HTTP routing requirement, evaluate Application Gateway. Show the DNS exchange separately from the application connection and explain how health information affects selection.

</details>

## 8. A service endpoint was enabled on a subnet. Why does that not prove the storage account now has a private endpoint address there?

<details>
<summary>Reasoning</summary>

A service endpoint and a private endpoint are different designs. Enabling a service endpoint does not create a private network interface for the storage account in that subnet. Check the actual service endpoint configuration, service network rules, and authentication method. If the requirement specifically calls for a private destination address, evaluate a supported private endpoint plus its DNS and access settings. Record the resolved destination and relevant resource configuration instead of treating the shared word “endpoint” as equivalence.

</details>

## 9. A new deny rule blocks fresh connections, but one established session continues. Is the NSG necessarily ignoring its rules?

<details>
<summary>Reasoning</summary>

No. NSGs are stateful, so a changed rule need not interrupt an existing flow immediately. Distinguish a genuinely new connection from a reused session, then inspect the effective rules at both subnet and interface. Check source, destination, port, protocol, and priority rather than relying on a rule name. The observation should include whether the test created a new flow. Broader role assignments or deleting the VM would not explain this behaviour.

</details>

## 10. A diagram shows ExpressRoute and a backup VPN. What evidence is still missing before claiming resilient application connectivity?

<details>
<summary>Reasoning</summary>

Identify shared failure domains and validate the complete backup path. Check customer devices, providers, peering locations, gateways, route advertisements, return routes, tunnel capacity, DNS dependencies, and application reconnection. A second line on a drawing does not prove that traffic selects it correctly during a failure. Propose an isolated, authorised test with expected and observed results plus recovery and return-to-normal criteria. These notes provide the design exercise; they do not claim that such a failover was executed.

</details>

Technical sources and the checked exam reference are linked in the [guide](AZ-700.md). Continue with the [workbook](AZ-700-workbook.md) to turn answers into diagrams and evidence.
