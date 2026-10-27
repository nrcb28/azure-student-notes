# Microsoft Learn praktisch vertieft

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

Quellenprüfung: 27. Oktober 2026. Neu formulierte Erklärungen und eigene Fälle. Die vorgeschlagenen Prüfungen wurden nicht in Azure ausgeführt.

<a id="learn-sas"></a>

## 1. SAS mit Entra ID

Eine Blob User Delegation SAS verwendet einen mit Entra ID beschafften Delegierungsschlüssel. Dessen Anforderung benötigt Rechte; eine bekannte URL genügt nicht.

**Fall:** kurzer PDF-Download. Ressource, Lesen und Gültigkeit begrenzen; sensible URLs nicht protokollieren. Ablauf, Autorisierung und Netzwerk getrennt prüfen. Für Offenlegung und Widerruf den konkreten SAS-Typ berücksichtigen.

[Microsoft Learn · Storage: user delegation SAS](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

<a id="learn-dns"></a>

## 2. Privates DNS nachvollziehen

Der Client muss den Dienstnamen zur privaten Endpoint-IP auflösen. Die Schnittstelle allein konfiguriert nicht jeden Resolver. Passende Zonen hängen vom Dienst ab.

**Fall:** VM funktioniert, Hochschulnetz nicht. DNS-Antworten, Zonenlinks, Weiterleitung und Routen vergleichen. Nicht pauschal öffentliche Zonen überschreiben oder IPs fest codieren. Korrekte Auflösung vergibt keine Datenrechte.

[Microsoft Learn · Private endpoint DNS](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

<a id="learn-policy"></a>

## 3. Bewertung und Korrektur trennen

Korrekturaufgaben wenden modify oder deployIfNotExists auf vorhandene Ressourcen an. Sie verwenden Identität und Rechte der Zuweisung. Eine Definitionsänderung aktualisiert nicht automatisch jede Berechtigung.

**Fall:** alte Ressourcen bleiben abweichend. Effekt, Bereich, Identität und Rollen prüfen, Pilotgruppe korrigieren, Ergebnisse dokumentieren. Deny verwandelt nicht beliebige alte Konfigurationen automatisch.

[Microsoft Learn · Policy remediation](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

<a id="learn-dcr"></a>

## 4. DCRs und Datenerfassung

Data Collection Rules beschreiben Erfassung und Weiterleitung in unterstützten Szenarien. Transformationen können Daten vor dem Ziel filtern oder verändern. Sie ersetzen Diagnostic Settings nicht pauschal.

**Fall:** VM-Ereignisse fehlen. Agent, Zuordnung, Quelle, Datenfluss, Ziel und Schema prüfen. Alles sammeln erhöht Kosten und Datenschutzrisiken; zu starkes Filtern entfernt nützliche Beweise.

[Microsoft Learn · Azure Monitor data collection rules](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview)

<a id="learn-whatif"></a>

## 5. What-if-Grenzen

What-if sagt Änderungen voraus, ohne sie anzuwenden. Rechte, Abhängigkeiten und Ausdrücke können die Analyse begrenzen. Unvollständige Ergebnisse beweisen keine Änderungslosigkeit.

**Fall:** Ignore oder nicht ausgewertetes Modul. Diagnosen lesen und Modul isolieren, nicht als NoChange behandeln. Kompilierung, Validierung, Vorschau und anschließenden Test unterscheiden. Reviews berücksichtigen ungeprüfte Teile.

[Microsoft Learn · Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

<a id="learn-slots"></a>

## 6. Slots sind aktive Anwendungen

Ein Slot hat eigenen Hostnamen und laufende Anwendung. Kopierte Einstellungen klonen weder Inhalt noch private Netzwerke und sämtliche Abhängigkeiten. Swaps enthalten Vorbereitung und Aufwärmen.

**Fall:** Staging versendet echte E-Mails. Verbindungen, Identität, Slot-Einstellungen und Startaufgaben prüfen. Null Benutzerverkehr verhindert keine Hintergrundarbeit. Zurücktauschen macht destruktive Migrationen nicht rückgängig.

[Microsoft Learn · App Service deployment slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)

<a id="learn-landing"></a>

## 7. Landing Zones und Zuständigkeit

Landing Zones organisieren Identität, Konnektivität, Verwaltung und Governance. Plattform und Workloads können verschiedene Eigentümer haben; Beschleuniger ersetzen keine Anforderungen.

**Fall:** fünf Fakultäten teilen Netzwerke und betreiben eigene Apps. Zuständigkeiten, Grenzen, Rechte, Policies und Kosten festlegen. Keine vollständige Unternehmensplattform ohne Grund in ein kleines Labor übernehmen.

[Microsoft Learn · Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)

<a id="learn-checks"></a>

## 8. Checks und Veröffentlichung

Azure-Pipelines-Ressourcenverantwortliche verwalten Approvals und Checks außerhalb der YAML-Datei. Vor einer Stage müssen die Prüfungen ihrer Ressourcen erfüllt sein.

**Fall:** Produktion verlangt unabhängige Prüfung und Zeitfenster. Ressource, Prüfer, Timeout und Ablehnung festlegen. Ablauf und Änderungen testen. Eine grüne Pipeline berechtigt nicht zu jeder Service Connection.

[Microsoft Learn · Azure Pipelines approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops)

---

[Source register](../LEARN-SOURCES.md) · [Attribution](../ATTRIBUTION.md)
