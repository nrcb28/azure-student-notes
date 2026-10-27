# Übungen · Azure CLI / Bicep

[Inhalt](README.md) · [English](../en/13-laboratorios.md)

Diese Übungen verwenden Bash, Azure CLI und Bicep in einem Testabonnement. Sie wurden bei der Erstellung nicht in Azure ausgeführt. Echte Ressourcen und Kosten können entstehen. Lies die Löschschritte vorher.

Du brauchst Rechte für Gruppe und Ressourcen. Blob-Operationen benötigen eine Datenrolle, etwa Storage Blob Data Contributor im erforderlichen Bereich. Verwaltungsrechte allein genügen nicht immer. Vergib nicht pauschal Owner für das ganze Abonnement.

## 1. Abonnement kontrollieren

Melde dich im Repository-Stamm an und ersetze die Platzhalterkennung. Prüfe Name und ID vor der Erstellung der Laborgruppe. Bewahre Variablen in derselben Shell auf. Wähle bei Bedarf eine erlaubte Region.

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

## 2. Kompilieren, prüfen und bereitstellen

Lies die [Bicep-Konfiguration](../labs/storage.bicep). Sie erstellt Standard_LRS, verlangt HTTPS und deaktiviert anonyme Blobs sowie gemeinsame Schlüssel. Der öffentliche Netzwerkendpunkt bleibt aktiviert; Authentifizierung ist erforderlich. Private Netzwerke, Backups und RBAC werden nicht eingerichtet.

Kompilierung prüft Syntax; validate und what-if benötigen Azure. Prüfe Änderungen vor dem Erstellen. Namenskonflikte, Kontingente und Policy können scheitern lassen. publicBlobs und sharedKey sollten false sein.

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

## 3. Privaten Container mit eigener Identität erstellen

Fehlt die Datenrolle, beantrage sie nur im nötigen Bereich. Weitergabe kann dauern. auth-mode login verwendet die CLI-Identität statt eines Kontoschlüssels. Die Liste sollte notes enthalten.

Ein 403 kann Rechte oder Dienstzugriff betreffen. Öffne nicht ohne Diagnose das Netzwerk.

```bash
az storage container create --account-name "$LAB_STORAGE" \
  --name notes --auth-mode login --public-access off

az storage container list --account-name "$LAB_STORAGE" \
  --auth-mode login --query '[].name' --output table
```

## 4. Eigene Laborgruppe löschen

Prüfe die Ressourcenliste. Der Befehl entfernt die Gruppe einschließlich aller Ressourcen. Nutze ausschließlich die neu erstellte Laborgruppe. Bestätige auf Nachfrage und warte auf Abschluss.

```bash
az resource list --resource-group "$LAB_RG" --output table
az group delete --name "$LAB_RG"
```

## 5. Löschung bestätigen

Erwartet wird false. Andernfalls prüfe Sperren, Fehler und Berechtigungen. Nicht bloß annehmen, dass alles gelöscht wurde.

```bash
az group exists --name "$LAB_RG"
```
