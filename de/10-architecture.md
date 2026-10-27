# Architektur und Wiederherstellung

[Inhalt](README.md) · [Zertifizierungen](../certifications/de/README.md)

Architektur beginnt mit Nutzern, Daten, Anforderungen, Budget und Betriebskompetenz. Mehr Dienste bedeuten nicht automatisch bessere Qualität.

Unsere App nutzt Web/API, Metadatenbank, Blob-Dokumente, Warteschlange und Analyseprozess. Das ist ein konzeptioneller Ausgangspunkt, keine fertige Produktionskonfiguration.

RTO bezeichnet die angestrebte Wiederherstellungszeit. RPO beschreibt tolerierten jüngsten Datenverlust als Zeitspanne. Wiederhergestellte Daten helfen wenig, wenn API, DNS und Rechte noch auf das alte System zeigen.

Plane Zeitlimits, gestaffelte Wiederholungen, Idempotenz und Teilausfälle. Wiederherstellungstests müssen isoliert sein.

**ADR:** Kontext, Anforderungen, Alternativen, Entscheidung, Folgen, Validierung und Überprüfungsanlass dokumentieren.

**Übung:** Begründe einen Entwurf mit zwei Stunden RTO und fünfzehn Minuten RPO. Diese Werte sind zu prüfende Anforderungen, keine automatisch garantierten Produkteigenschaften.

---

[Zurück](09-costs.md) · [Weiter](11-messaging.md) · [English](../en/10-architecture.md)

## Microsoft-Learn-Vertiefung · landing

Landing Zones organisieren Identität, Konnektivität, Verwaltung und Governance. Plattform und Workloads können verschiedene Eigentümer haben; Beschleuniger ersetzen keine Anforderungen.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) · [Microsoft-Learn-Vertiefung](15-microsoft-learn.md#learn-landing)
