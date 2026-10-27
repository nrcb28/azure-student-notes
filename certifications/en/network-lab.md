# Networking lab: predict rules and inspect configuration

[Certifications](README.md) · [Español](../es/network-lab.md)

## Purpose and limits

The template creates a VNet, two subnets, and an NSG. It creates no VM, public IP, gateway, or hybrid connectivity. It teaches configuration interpretation rather than proving an application connection.

It has not been deployed from these notes. Azure CLI, Bicep, and permissions in a test subscription are required. Policies and availability can block operations. Review resources and possible costs.

## Before execution

Read [network.bicep](../../labs/network.bicep) and predict:

| Source | Destination | Port | Expected data-subnet NSG result |
|---|---|---|---|
| 10.30.1.5 | 10.30.2.5 | TCP 443 | Allow at priority 100 |
| 10.30.1.5 | 10.30.2.5 | TCP 22 | Deny at priority 110 |
| 10.30.2.6 | 10.30.2.5 | TCP 443 | Deny at priority 110 |

These are rule predictions for new traffic subject to that NSG without other changes. They do not prove routing, resolution, a listening process, or application authorisation.

Priority 110 denies remaining inbound VirtualNetwork-tag traffic before the default allow rule. This is a teaching choice, not a production rule to copy without dependency analysis.

## Deploy from the root

```bash
az login
AZURE_NET_SUBSCRIPTION='REPLACE_WITH_TEST_SUBSCRIPTION_ID'
az account set --subscription "$AZURE_NET_SUBSCRIPTION"
az account show --query '{name:name,id:id}' --output table

NET_RG="rg-notes-network-$(date -u +%Y%m%d%H%M%S)"
NET_LOCATION='westeurope'
az group create --name "$NET_RG" --location "$NET_LOCATION" \
  --tags project=notes-app environment=lab

az bicep build --file labs/network.bicep --stdout > /dev/null

az deployment group validate --resource-group "$NET_RG" \
  --template-file labs/network.bicep

az deployment group what-if --resource-group "$NET_RG" \
  --template-file labs/network.bicep

# After reviewing proposed operations:
az deployment group create --resource-group "$NET_RG" \
  --template-file labs/network.bicep
```

## Verification

```bash
az network vnet subnet list --resource-group "$NET_RG" \
  --vnet-name vnet-notes-lab \
  --query '[].{name:name,prefix:addressPrefix,nsg:networkSecurityGroup.id}' \
  --output table

az network nsg rule list --resource-group "$NET_RG" \
  --nsg-name nsg-notes-lab \
  --query '[].{name:name,priority:priority,access:access,port:destinationPortRange}' \
  --output table
```

Expect two subnets. The data subnet references the NSG, and custom rules show priorities 100 and 110. Listing custom rules is not equivalent to listing all defaults or an interface's effective rules.

**Not tested:** without VMs or listeners, there is no real HTTPS test between the example addresses. End-to-end testing requires workloads, routes, and additional checks.

## Variants without deployment

1. Change the allowed port in a local copy and predict results.
2. Add a destination interface NSG on paper. Explain why a subnet allow is insufficient if another filter denies.
3. Assume DNS resolves a public address. Explain what the NSG does not solve.
4. Explain effects on established connections when changing stateful filters.

## Cleanup

Use only the dedicated group just created:

```bash
az resource list --resource-group "$NET_RG" --output table
az group delete --name "$NET_RG"
az group exists --name "$NET_RG"
```

Confirm when prompted. After completion it should return false. Inspect errors or locks otherwise.

## Submission

A prediction table, observed configuration results, and a paragraph distinguishing an allowed port from a working application.
