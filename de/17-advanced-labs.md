# Vertiefende Übungen

[←](README.md) · [Gemeinsamer Lernkern](16-common-core.md)

Drei gleichwertige Übungen in acht Sprachen. Die Simulation ist lokal; die anderen benötigen Testabonnement, Azure CLI und Rechte. Hier nicht in Azure ausgeführt. Ressourcen und Aufbewahrung können Kosten erzeugen. Im Repository-Stamm arbeiten und Löschschritte vorher lesen.

<a id="advanced-lab-1"></a>

## 1. Datei wiederherstellen und Bytes vergleichen

Erstelle nur eigene Gruppe und Konto. Die Vorlage deaktiviert Versionierung und hierarchischen Namespace für undelete ohne Versionsbeförderung. Sie setzt sieben Tage Soft Delete für Blobs und Container, deaktiviert gemeinsame Schlüssel und öffentliche Blobs, behält authentifizierten öffentlichen Netzwerkzugang.

Verwaltungs- und Datenrechte wie Storage Blob Data Contributor auf dem Konto sind erforderlich. Keine Rollenzuweisung erfolgt automatisch. Weitergabe abwarten, nicht pauschal Owner vergeben.

Das Skript erstellt neuen Container, lädt synthetischen Text, löscht nur diesen Blob, stellt wieder her und vergleicht. Erwartet RECOVERY_OK. Danach Containerlöschung; aufbewahrte Daten können bleiben. Fehlerphase ohne Geheimnisse dokumentieren, Produktion nicht verändern.

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

## 2. Zuweisungen nur lesen

Ressourcen-ID und Principal-Objekt-ID statt Client-ID verwenden. Das Skript liest Zuweisungen an diesen Principal einschließlich geerbter Bereiche. Keine vollständige Effektivrechteberechnung: Gruppen, Bedingungen, Denials, zeitweise Aktivierung und Daten-/Netzwerkregeln gesondert prüfen.

Rolle, Bereich, Bedingung und gewünschte Aktion abgeben. Leere Ausgabe beweist keine vollständige Zugriffslosigkeit. Keine Zuweisung für sichtbare Ergebnisse erstellen.

[Script](../labs/inspect-access.sh)

```bash
export LAB_SCOPE=$(az storage account show --name "$LAB_STORAGE" \
  --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" --query id -o tsv)
export LAB_PRINCIPAL_ID='REPLACE_WITH_PRINCIPAL_OBJECT_ID'
bash labs/inspect-access.sh
```

<a id="advanced-lab-3"></a>

## 3. Verlorene Antwort simulieren

Ohne Netzwerk, Geheimnisse oder Cloud. SQLite speichert, die erste Antwort geht verloren, der Client wiederholt. Bei drei Versuchen: naive speichert zwei Dokumente, idempotent eines, permanent schreibt und wiederholt nicht. Wartezeiten werden nur berechnet.

Ein Versuch kann einen Schreibvorgang ohne bestätigten Erfolg hinterlassen. Ausnahme bedeutet nicht, dass nichts geschah. Sieben lokale Tests prüfen Verhalten und Schutz, nicht Azure-Verfügbarkeit.

[Simulator](../labs/retry_lab.py)

```bash
python labs/retry_lab.py --attempts 3
python labs/retry_lab.py --attempts 1
python -m unittest discover -s tools -p 'test_*lab*.py' -v
```

<a id="advanced-lab-4"></a>

## 4. Bereinigung und Abgabe

Eigene Gruppe auflisten, Löschung bestätigen und false prüfen. Containerlöschung beendet nicht zwingend jede Aufbewahrung. Sperren und Fehler beachten; gemeinsame Ressourcen nicht purgen.

Erwartung, Beobachtung, Rechte, Vergleich, Rolleninterpretation und Simulatorausgabe abgeben. Lokal und Cloud getrennt ausweisen.



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
