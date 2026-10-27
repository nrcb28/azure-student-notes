# Laboratori · Azure CLI / Bicep

[Indice](README.md) · [English](../en/13-laboratorios.md)

Queste pratiche usano Bash, Azure CLI e Bicep in una sottoscrizione di prova. Non sono state eseguite su Azure durante la preparazione degli appunti. Possono creare risorse reali e costi. Leggi la pulizia prima di iniziare.

Servono permessi per gruppo e risorse. Le operazioni sui blob richiedono un ruolo dati appropriato, per esempio Storage Blob Data Contributor sull'ambito necessario. Contributor di gestione non basta sempre. Non assegnare Owner all'intera sottoscrizione per aggirare un errore.

## 1. Controllare la sottoscrizione

Dalla radice del repository, accedi e sostituisci l'identificatore segnaposto. Verifica nome e ID della sottoscrizione prima di creare il gruppo dedicato. Conserva le variabili nella stessa sessione. Se la regione non è consentita, scegline una compatibile.

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

## 2. Compilare, verificare e distribuire

Leggi la [configurazione Bicep](../labs/storage.bicep). Crea Standard_LRS, richiede HTTPS, disabilita blob anonimi e chiavi condivise. L'endpoint pubblico di rete rimane abilitato; l'autenticazione resta obbligatoria. Non configura rete privata, backup o RBAC.

Compilazione controlla sintassi; validate e what-if richiedono Azure. Esamina le modifiche prima di creare. Nomi globali, quote e Policy possono ancora impedire il deploy. publicBlobs e sharedKey devono risultare false.

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

## 3. Contenitore privato con la propria identità

Se manca il ruolo dati, chiedi un'assegnazione sul solo ambito richiesto. La propagazione può richiedere tempo. auth-mode login usa la tua identità CLI senza recuperare la chiave dell'account. La lista deve contenere notes.

Un 403 può dipendere da diritti o controlli del servizio; non aprire la rete senza diagnosi.

```bash
az storage container create --account-name "$LAB_STORAGE" \
  --name notes --auth-mode login --public-access off

az storage container list --account-name "$LAB_STORAGE" \
  --auth-mode login --query '[].name' --output table
```

## 4. Pulizia del gruppo dedicato

Controlla l'elenco. Il comando elimina il gruppo e tutte le sue risorse: eseguilo soltanto sul gruppo creato per la pratica. Conferma quando richiesto e attendi il completamento.

```bash
az resource list --resource-group "$LAB_RG" --output table
az group delete --name "$LAB_RG"
```

## 5. Confermare l'eliminazione

Il risultato deve essere false. In caso contrario esamina blocchi, errori e permessi. Non supporre che le risorse siano sparite.

```bash
az group exists --name "$LAB_RG"
```
