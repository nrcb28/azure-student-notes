# Travaux pratiques · Azure CLI / Bicep

[Sommaire](README.md) · [English](../en/13-laboratorios.md)

Ces travaux utilisent Bash, Azure CLI et Bicep dans un abonnement de test. Ils n'ont pas été exécutés sur Azure pendant la rédaction. Ils peuvent créer des ressources et des coûts. Lis la suppression avant de commencer.

Il faut les droits sur groupes et ressources. Les opérations Blob nécessitent un rôle de données adapté, par exemple Storage Blob Data Contributor sur la bonne étendue. Contributor de gestion ne suffit pas toujours. Ne donne pas Owner sur tout l'abonnement pour contourner une erreur.

## 1. Vérifier l'abonnement

Depuis la racine, connecte-toi et remplace l'identifiant fictif. Vérifie nom et ID avant de créer le groupe dédié. Conserve les variables dans la même session. Choisis une région autorisée si nécessaire.

```bash
az login
az account list --output table

# Replace this value before continuing.
AZURE_LAB_SUBSCRIPTION='REPLACE_WITH_TEST_SUBSCRIPTION_ID'
az account set --subscription "$AZURE_LAB_SUBSCRIPTION"
az account show --query '{name:name,id:id}' --output table

LAB_RG="rg-notes-lab-$(date -u +%Y%m%d%H%M%S)"
LAB_LOCATION='westeurope'
az group create --name "$LAB_RG" --location "$LAB_LOCATION" \
  --tags project=notes-app environment=lab

# Confirm this is a newly created, empty group.
az resource list --resource-group "$LAB_RG" --output table
```

## 2. Compiler, vérifier et déployer

Lis la [configuration Bicep](../labs/storage.bicep). Elle crée Standard_LRS, impose HTTPS et désactive blobs anonymes et clés partagées. L'accès réseau public reste activé ; l'authentification est obligatoire. Elle ne configure ni réseau privé, ni sauvegarde, ni RBAC.

La compilation vérifie la syntaxe ; validate et what-if nécessitent Azure. Examine les modifications avant création. Unicité du nom, quotas et Policy peuvent encore bloquer. publicBlobs et sharedKey doivent être false.

```bash
# 22 lowercase alphanumeric characters; must be globally unique.
LAB_STORAGE="notes$(date -u +%y%m%d%H%M%S)$(printf '%05d' "$RANDOM")"

az bicep build --file labs/storage.bicep --stdout > /dev/null

az deployment group validate --resource-group "$LAB_RG" \
  --template-file labs/storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

az deployment group what-if --resource-group "$LAB_RG" \
  --template-file labs/storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

# Continue after reviewing the proposed changes.
az deployment group create --resource-group "$LAB_RG" \
  --template-file labs/storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

az storage account show --resource-group "$LAB_RG" --name "$LAB_STORAGE" \
  --query '{name:name,publicBlobs:allowBlobPublicAccess,sharedKey:allowSharedKeyAccess}' \
  --output table
```

## 3. Créer un conteneur privé avec son identité

Si le rôle de données manque, demande une attribution limitée à l'étendue nécessaire. La propagation peut prendre du temps. auth-mode login utilise l'identité CLI, sans récupérer la clé du compte. La liste doit contenir notes.

Un 403 peut concerner droits ou contrôles du service. Ne pas ouvrir le réseau sans diagnostic.

```bash
az storage container create --account-name "$LAB_STORAGE" \
  --name notes --auth-mode login --public-access off

az storage container list --account-name "$LAB_STORAGE" \
  --auth-mode login --query '[].name' --output table
```

## 4. Supprimer le groupe dédié

Vérifie la liste. La commande supprime le groupe et toutes ses ressources : utilise uniquement celui créé pour le laboratoire. Confirme sur demande et attends la fin.

```bash
az resource list --resource-group "$LAB_RG" --output table
az group delete --name "$LAB_RG"
```

## 5. Confirmer la suppression

Le résultat attendu est false. Sinon, examiner verrous, erreurs et permissions. Ne pas supposer que les ressources ont disparu.

```bash
az group exists --name "$LAB_RG"
```
