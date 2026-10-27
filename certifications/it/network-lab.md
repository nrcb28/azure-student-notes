# Laboratori · VNet / NSG

[Indice](README.md) · [English](../en/network-lab.md)

Queste pratiche usano Bash, Azure CLI e Bicep in una sottoscrizione di prova. Non sono state eseguite su Azure durante la preparazione degli appunti. Possono creare risorse reali e costi. Leggi la pulizia prima di iniziare.

Servono permessi per gruppo e risorse. Le operazioni sui blob richiedono un ruolo dati appropriato, per esempio Storage Blob Data Contributor sull'ambito necessario. Contributor di gestione non basta sempre. Non assegnare Owner all'intera sottoscrizione per aggirare un errore.

La [configurazione di rete](../../labs/network.bicep) crea VNet, due subnet e NSG, senza VM, gateway o IP pubblico. Prima prevedi il comportamento: web 10.30.1.5 verso dati 10.30.2.5 su TCP 443 è consentito dalla priorità 100; TCP 22 è negato dalla 110. Anche un'altra origine della subnet dati viene negata per il traffico restante.

La regola 110 precede il permesso predefinito VirtualNetwork. È una scelta didattica, non una regola universale di produzione. Non dimostra connettività reale: mancano VM e processi in ascolto.

## 1. Controllare e distribuire

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

## 2. Verificare la configurazione

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

## 3. Eliminare e verificare

```bash
az resource list --resource-group "$NET_RG" --output table
az group delete --name "$NET_RG"
az group exists --name "$NET_RG"
```

Devono esistere due subnet e la subnet data deve referenziare il NSG. Controlla priorità 100 e 110. Elencare regole personalizzate non equivale a vedere tutte le regole effettive.

Distingui risultato previsto, configurazione osservata e test di connessione: quest'ultimo non è stato eseguito. La pulizia elimina tutto il gruppo dedicato e deve terminare con false.
