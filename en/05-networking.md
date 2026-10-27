# Networking and connectivity

A network that allows traffic is not necessarily configured well. We need to understand the connection's route, name resolution, and the rules allowing it.

## Basic components

- **VNet:** a private virtual network.
- **Subnet:** part of a VNet's address space.
- **NSG:** stateful filtering rules for subnets or interfaces.
- **Route table:** controls the next hop for particular destinations.
- **Peering:** connects virtual networks; it is not automatically transitive.
- **DNS:** translates names into addresses.

If A peers with B and B peers with C, A does not necessarily have connectivity to C. Avoid overlapping address spaces when networks will connect.

## Connecting environments

VPN Gateway supports encrypted connections across the Internet. ExpressRoute provides private connectivity through a provider, but does not inherently provide end-to-end encryption.

A **Private Endpoint** provides an interface with a private address for a supported service. DNS and public access settings need checking. A **service endpoint** is different: it does not provide an equivalent private IP for the service.

## Distributing traffic

| Service | Main criterion |
|---|---|
| Load Balancer | TCP/UDP, layer 4 |
| Application Gateway | HTTP/HTTPS, layer 7, WAF options |
| Front Door | Global entry point for web applications |
| Traffic Manager | DNS-based destination selection |

Traffic Manager does not proxy application traffic. DNS caching affects how quickly clients change destinations.

## Class troubleshooting

If the API cannot reach the database:

1. Check the name and DNS resolution.
2. Check routing and port connectivity.
3. Check NSGs, firewalls, and public or private access.
4. Check authentication and permissions.
5. Read errors and metrics before changing rules.

**Common mistake:** opening every port to make it work and forgetting to close them.

## Worked example: private on the diagram, public in use

A private endpoint exists, but the laptop still resolves the service name to a public address. Traffic may continue publicly if allowed, or fail if public access is disabled before private resolution works.

First inspect the address returned to the client and its route. Then check service access settings. Avoid hard-coding an IP without considering names and certificates.

## NSG versus application

An allowed port does not prove a process is listening. Guest firewalls and application settings can also block connections.

With subnet and interface NSGs, inspect effective rules. Lower priority numbers are evaluated first, and filtering is stateful.

**Exercise:** draw both directions between an on-premises VM, VPN, VNet, and private service. Separate DNS, routing, filtering, and authentication checks.

---

[Contents](README.md) · [Other language](../es/05-networking.md) · [Previous](04-storage.md) · [Next](06-identity.md)

## Microsoft Learn expansion · dns

Clients must resolve the service name to the private endpoint address. Creating a private interface does not configure every resolver. Recommended zones depend on the service; indiscriminately replacing an entire public zone can break resolution.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) · [Microsoft Learn expansion](15-microsoft-learn.md#learn-dns)
