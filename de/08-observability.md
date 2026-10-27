# Überwachung und Diagnose

[Inhalt](README.md) · [Zertifizierungen](../certifications/de/README.md)

Metriken, Protokolle und Traces beantworten unterschiedliche Fragen. Azure Monitor bietet Überwachung, Application Insights beobachtet Anwendungen, Log Analytics fragt verfügbare Protokolle mit KQL ab.

Niedrige CPU bedeutet keine schnelle App: Sie kann auf eine Datenbank warten. Mittelwerte verdecken langsame Einzelanfragen. Verteilung, Perzentile und Stichprobengröße gehören zusammen.

Ein hilfreicher Alarm braucht Signal, Schwelle, Zeitfenster und Aktion. Service Health betrifft genutzte Azure-Dienste; Resource Health eine bestimmte Ressource.

**Vorgehen:** Beginn und Auswirkungen eingrenzen, letzte Änderung prüfen, Anfrage und Abhängigkeiten verfolgen, Hypothese testen, korrigieren und Erholung bestätigen.

Keine Token oder vollständigen Dokumente protokollieren. Aufbewahrung und Detailgrad beeinflussen Kosten und Datenschutz. OpenTelemetry muss zur Laufzeit und Integration passen.

**Übung:** Messe Upload-Erfolg, Latenz und Verarbeitungsdauer statt ausschließlich CPU.

---

[Zurück](07-governance.md) · [Weiter](09-costs.md) · [English](../en/08-observability.md)

## Microsoft-Learn-Vertiefung · dcr

Data Collection Rules beschreiben Erfassung und Weiterleitung in unterstützten Szenarien. Transformationen können Daten vor dem Ziel filtern oder verändern. Sie ersetzen Diagnostic Settings nicht pauschal.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview) · [Microsoft-Learn-Vertiefung](15-microsoft-learn.md#learn-dcr)
