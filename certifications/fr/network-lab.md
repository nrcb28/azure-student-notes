# Travaux pratiques · VNet / NSG

[Sommaire](README.md) · [English](../en/network-lab.md)

Ces travaux utilisent Bash, Azure CLI et Bicep dans un abonnement de test. Ils n'ont pas été exécutés sur Azure pendant la rédaction. Ils peuvent créer des ressources et des coûts. Lis la suppression avant de commencer.

Il faut les droits sur groupes et ressources. Les opérations Blob nécessitent un rôle de données adapté, par exemple Storage Blob Data Contributor sur la bonne étendue. Contributor de gestion ne suffit pas toujours. Ne donne pas Owner sur tout l'abonnement pour contourner une erreur.

La [configuration réseau](../../labs/network.bicep) crée VNet, deux sous-réseaux et NSG, sans VM, gateway ni IP publique. Prédis les règles : web 10.30.1.5 vers data 10.30.2.5 sur TCP 443 est autorisé par priorité 100 ; TCP 22 est refusé par 110. Les autres sources du sous-réseau data sont également refusées pour le trafic restant.

La règle 110 précède l'autorisation VirtualNetwork par défaut. C'est un choix pédagogique, pas une règle universelle de production. Sans VM ni processus à l'écoute, aucune connexion réelle n'est démontrée.

## 1. Vérifier et déployer

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

## 2. Contrôler la configuration

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

## 3. Supprimer et confirmer

```bash
az resource list --resource-group "$NET_RG" --output table
az group delete --name "$NET_RG"
az group exists --name "$NET_RG"
```

Deux sous-réseaux doivent exister ; data référence le NSG. Vérifie priorités 100 et 110. Lister les règles personnalisées ne montre pas toutes les règles effectives.

Distingue prédiction, configuration observée et test de connexion. Ce dernier n'a pas été réalisé. La suppression concerne tout le groupe dédié et doit être confirmée par false.
