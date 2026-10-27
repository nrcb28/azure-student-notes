# Identität und Sicherheit

[Inhalt](README.md) · [Zertifizierungen](../certifications/de/README.md)

Entra ID verwaltet Identitäten. Authentifizierung prüft, wer wir sind; Autorisierung legt erlaubte Aktionen fest. MFA stärkt die Anmeldung und vergibt keine Dokumentberechtigungen.

Azure RBAC kombiniert Identität, Rolle und Bereich. Reader liest, Contributor verwaltet ohne RBAC-Rollenzuweisungen zu vergeben, Owner kann zusätzlich Zugriff vergeben. Verzeichnisrollen sind von Ressourcenrollen zu unterscheiden.

Managed Identities vermeiden selbst gespeicherte Anwendungszugangsdaten, brauchen aber Berechtigungen. Key Vault verwaltet Geheimnisse, Schlüssel und Zertifikate.

**Fall:** Nach Entfernen von Reader bleibt Zugriff. Prüfe Gruppen, geerbte Zuweisungen, tatsächliche Identität und Weitergabezeit.

Unsere App muss den Zugriff auf jedes Dokument prüfen. Angemeldete Studierende dürfen nicht automatisch fremde Unterlagen ändern.

**Übung:** Definiere unterschiedliche Rechte für Studierende, API und Vorschaubild-Prozess.

---

[Zurück](05-networking.md) · [Weiter](07-governance.md) · [English](../en/06-identity.md)

## Microsoft-Learn-Vertiefung · sas

Eine Blob User Delegation SAS verwendet einen mit Entra ID beschafften Delegierungsschlüssel. Dessen Anforderung benötigt Rechte; eine bekannte URL genügt nicht.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli) · [Microsoft-Learn-Vertiefung](15-microsoft-learn.md#learn-sas)

## RBAC anhand von Nachweisen prüfen

Ressourcenverwaltung gewährt nicht automatisch Rollenzuweisung oder Datenzugriff. Passende Aktion und Bereich sind erforderlich; Bedingungen können Rollen und Empfänger beschränken.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting) · [RBAC anhand von Nachweisen prüfen](15-microsoft-learn.md#learn-rbac-diagnosis)

## Key Vault samt Abhängigkeiten wiederherstellen

Soft Delete ermöglicht Wiederherstellung innerhalb der Aufbewahrung. Der wiederhergestellte Vault stellt Integrationen wie RBAC-Zuweisungen und Event-Grid-Abonnements nicht automatisch wieder her.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview) · [Key Vault samt Abhängigkeiten wiederherstellen](15-microsoft-learn.md#learn-vault-recovery)
