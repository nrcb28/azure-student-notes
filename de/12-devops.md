# DevOps und Infrastruktur als Code

[Inhalt](README.md) · [Zertifizierungen](../certifications/de/README.md)

DevOps verbindet Entwicklung und Betrieb für zuverlässige Änderungen. CI integriert mit Build und Prüfungen. Continuous Delivery hält Änderungen veröffentlichungsbereit; Continuous Deployment veröffentlicht automatisch nach Kriterien.

Befördere dasselbe getestete Artefakt. Versionen und Digests machen nachvollziehbar, was lief.

Bicep beschreibt Azure-Ressourcen. Terraform verwaltet schützenswerten Zustand. Plan und What-if helfen, garantieren aber nicht jede spätere Operation. OIDC vermeidet langlebige Geheimnisse, nicht Vertrauenskonfiguration und Berechtigungen.

**Rollback:** Alter Code stellt keine gelöschte Datenbankspalte wieder her. Plane kompatible Migrationen und geprüfte Wiederherstellung.

Ein privilegierter Runner darf nicht wahllos nicht vertrauenswürdigen Code ausführen.

**Übung:** Verbinde Issue, PR, Test, Artefakt und Release. Definiere Beförderungs- und Rollback-Signale. Führe lokal python tools/check_docs.py aus.

---

[Zurück](11-messaging.md) · [Weiter](13-laboratorios.md) · [English](../en/12-devops.md)

## Microsoft-Learn-Vertiefung · whatif

What-if sagt Änderungen voraus, ohne sie anzuwenden. Rechte, Abhängigkeiten und Ausdrücke können die Analyse begrenzen. Unvollständige Ergebnisse beweisen keine Änderungslosigkeit.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if) · [Microsoft-Learn-Vertiefung](15-microsoft-learn.md#learn-whatif)

## Microsoft-Learn-Vertiefung · slots

Ein Slot hat eigenen Hostnamen und laufende Anwendung. Kopierte Einstellungen klonen weder Inhalt noch private Netzwerke und sämtliche Abhängigkeiten. Swaps enthalten Vorbereitung und Aufwärmen.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) · [Microsoft-Learn-Vertiefung](15-microsoft-learn.md#learn-slots)

## Microsoft-Learn-Vertiefung · checks

Azure-Pipelines-Ressourcenverantwortliche verwalten Approvals und Checks außerhalb der YAML-Datei. Vor einer Stage müssen die Prüfungen ihrer Ressourcen erfüllt sein.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops) · [Microsoft-Learn-Vertiefung](15-microsoft-learn.md#learn-checks)

## Begrenzte, idempotente Wiederholungen

Retries helfen vorübergehenden Fehlern, nicht falschen Zugangsdaten oder ungültigen Anfragen. Versuche und Gesamtdauer begrenzen, vorhandene SDK-Wiederholungen berücksichtigen.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) · [Begrenzte, idempotente Wiederholungen](15-microsoft-learn.md#learn-retry)
