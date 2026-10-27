# Speicher und Daten

[Inhalt](README.md) · [Zertifizierungen](../certifications/de/README.md)

Blob Storage speichert Objekte wie PDFs, Azure Files bietet Dateifreigaben, Managed Disks unterstützen VMs. Relationale Datenbanken verwalten Beziehungen und Transaktionen. JSON als Austauschformat erzwingt keine Dokumentdatenbank.

LRS repliziert lokal, ZRS über Zonen. GRS und GZRS ergänzen asynchrone geografische Replikation. Neue Schreibvorgänge sind möglicherweise noch nicht in der sekundären Region.

Versionierung, vorläufiges Löschen und Backups lösen andere Probleme als Redundanz. Archivierte Objekte können Rehydrierung benötigen und eignen sich nicht für sofortigen Zugriff.

**Lernunterlagen-App:** PDFs liegen in Blob Storage, Metadaten in der Datenbank. Nur die Datei wiederherzustellen kann inkonsistente Daten hinterlassen.

SAS-Token sind Zugangsdaten. Begrenze Berechtigungen und Gültigkeit. Unterscheide Verwaltungsrechte und Datenzugriff.

**Übung:** Erkläre die Wiederherstellung einer vor zehn Tagen gelöschten Datei.

---

[Zurück](03-compute.md) · [Weiter](05-networking.md) · [English](../en/04-storage.md)

## Microsoft-Learn-Vertiefung · sas

Eine Blob User Delegation SAS verwendet einen mit Entra ID beschafften Delegierungsschlüssel. Dessen Anforderung benötigt Rechte; eine bekannte URL genügt nicht.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli) · [Microsoft-Learn-Vertiefung](15-microsoft-learn.md#learn-sas)

## Blob-Wiederherstellung nach Schutzebene

Soft Delete bewahrt gelöschte Objekte während der Aufbewahrung. Es schützt allein weder die Löschung des Containers noch des gesamten Kontos. Diese Risiken getrennt behandeln.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview) · [Blob-Wiederherstellung nach Schutzebene](15-microsoft-learn.md#learn-blob-recovery)
