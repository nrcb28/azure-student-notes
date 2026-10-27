# Übungen · VNet / NSG

[Inhalt](README.md) · [English](../en/network-lab.md)

Diese Übungen verwenden Bash, Azure CLI und Bicep in einem Testabonnement. Sie wurden bei der Erstellung nicht in Azure ausgeführt. Echte Ressourcen und Kosten können entstehen. Lies die Löschschritte vorher.

Du brauchst Rechte für Gruppe und Ressourcen. Blob-Operationen benötigen eine Datenrolle, etwa Storage Blob Data Contributor im erforderlichen Bereich. Verwaltungsrechte allein genügen nicht immer. Vergib nicht pauschal Owner für das ganze Abonnement.

Die [Netzwerkkonfiguration](../../labs/network.bicep) erstellt VNet, zwei Subnetze und NSG ohne VMs, Gateway oder öffentliche IP. Sage Regeln voraus: Web 10.30.1.5 nach Daten 10.30.2.5 auf TCP 443 erlaubt Priorität 100; TCP 22 verweigert Priorität 110. Auch andere Quellen aus dem Datensubnetz werden für übrigen Verkehr verweigert.

Regel 110 liegt vor der Standardfreigabe VirtualNetwork. Das ist ein Lehrbeispiel, keine allgemeine Produktionsrichtlinie. Reale Konnektivität wird ohne VMs und lauschende Prozesse nicht nachgewiesen.

## 1. Prüfen und bereitstellen

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

## 2. Konfiguration kontrollieren

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

## 3. Löschen und bestätigen

```bash
az resource list --resource-group "$NET_RG" --output table
az group delete --name "$NET_RG"
az group exists --name "$NET_RG"
```

Erwartet werden zwei Subnetze; data verweist auf das NSG. Prüfe Prioritäten 100 und 110. Benutzerdefinierte Regeln sind nicht mit allen effektiven Regeln gleichzusetzen.

Trenne Vorhersage, beobachtete Konfiguration und Verbindungstest. Letzterer wurde nicht durchgeführt. Das Löschen betrifft die gesamte Laborgruppe und sollte mit false bestätigt werden.
