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

---

[Contents](README.md) · [Other language](../es/05-networking.md) · [Previous](04-storage.md) · [Next](06-identity.md)
