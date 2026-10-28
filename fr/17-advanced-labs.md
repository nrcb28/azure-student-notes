# Travaux pratiques avancés

[←](README.md) · [Socle commun d'étude](16-common-core.md)

Trois pratiques équivalentes dans huit langues. Simulation locale ; les autres exigent abonnement de test, Azure CLI et droits. Non exécutées ici dans Azure. Ressources et rétention peuvent coûter. Partir de la racine et lire d'abord le nettoyage.

<a id="advanced-lab-1"></a>

## 1. Restaurer et comparer les octets

Créer uniquement groupe et compte dédiés. Le modèle désactive versioning et namespace hiérarchique pour utiliser undelete sans promotion. Il active sept jours de soft delete blobs/conteneurs, désactive clés partagées et blobs publics, mais garde le réseau public authentifié.

Droits de gestion et rôle de données adapté, par exemple Storage Blob Data Contributor sur ce compte, sont nécessaires. Aucun rôle attribué par le modèle. Attendre propagation sans accorder Owner partout.

Le script crée un conteneur neuf, écrit du texte synthétique, supprime seulement ce blob, restaure et compare. Attendu RECOVERY_OK. Il supprime ensuite son conteneur ; la rétention peut subsister. Noter phase et erreur sans secrets, sans modifier production.

[Bicep](../labs/protected-storage.bicep) · [Script](../labs/blob-recovery.sh)

```bash
az login
export LAB_SUBSCRIPTION='REPLACE_WITH_TEST_SUBSCRIPTION_ID'
az account show --subscription "$LAB_SUBSCRIPTION" --query '{name:name,id:id}' -o table
export LAB_RG="rg-notes-recovery-$(date -u +%Y%m%d%H%M%S)"
export LAB_STORAGE="notes$(date -u +%y%m%d%H%M%S)$RANDOM"
az group create --name "$LAB_RG" --location westeurope \
  --subscription "$LAB_SUBSCRIPTION" --tags environment=lab project=notes-recovery

az deployment group what-if --resource-group "$LAB_RG" \
  --subscription "$LAB_SUBSCRIPTION" --template-file labs/protected-storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

# Review proposed changes before running create.
az deployment group create --resource-group "$LAB_RG" \
  --subscription "$LAB_SUBSCRIPTION" --template-file labs/protected-storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

# Run after the required data permissions have been provided.
bash labs/blob-recovery.sh
```

<a id="advanced-lab-2"></a>

## 2. Inspecter sans attribuer

Utiliser ID de ressource et object ID du principal, pas client ID. Le script lit les attributions du principal, avec étendues héritées. Ce n'est pas tout l'accès effectif : groupes, conditions, refus, activation temporaire et contrôles données/réseau restent à analyser.

Fournir rôle, étendue, condition et action souhaitée. Une sortie vide ne prouve pas l'absence totale d'accès. Ne pas créer d'attribution pour remplir le résultat.

[Script](../labs/inspect-access.sh)

```bash
export LAB_SCOPE=$(az storage account show --name "$LAB_STORAGE" \
  --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" --query id -o tsv)
export LAB_PRINCIPAL_ID='REPLACE_WITH_PRINCIPAL_OBJECT_ID'
bash labs/inspect-access.sh
```

<a id="advanced-lab-3"></a>

## 3. Simuler une réponse perdue

Sans réseau, identifiants ni cloud. SQLite écrit puis la première réponse disparaît ; le client répète. Trois tentatives : naive conserve deux documents, idempotent un, permanent n'écrit ni ne répète. Les délais sont calculés sans attente réelle.

Une tentative peut laisser une écriture sans succès confirmé. Une exception ne signifie pas absence d'opération. Sept tests locaux vérifient comportement et garde-fous, pas disponibilité Azure.

[Simulator](../labs/retry_lab.py)

```bash
python labs/retry_lab.py --attempts 3
python labs/retry_lab.py --attempts 1
python -m unittest discover -s tools -p 'test_*lab*.py' -v
```

<a id="advanced-lab-4"></a>

## 4. Nettoyage et livrable

Lister le groupe dédié, confirmer sa suppression et vérifier false. Supprimer le conteneur ne termine pas toute rétention. Examiner erreurs et verrous, sans purger de ressources partagées.

Fournir attendu, observé, droits, comparaison, interprétation des rôles et simulation. Distinguer local et cloud.



```bash
case "$LAB_RG" in
  rg-notes-recovery-*) ;;
  *) echo "Not a dedicated recovery lab group"; exit 2 ;;
esac
az resource list --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" -o table
az group delete --name "$LAB_RG" --subscription "$LAB_SUBSCRIPTION"
az group exists --name "$LAB_RG" --subscription "$LAB_SUBSCRIPTION"
```

[Microsoft Learn: Blob soft delete](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-enable) · [Restore](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-manage) · [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-cli)
