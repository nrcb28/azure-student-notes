# Nachrichten und Ereignisse

[Inhalt](README.md) · [Zertifizierungen](../certifications/de/README.md)

Warteschlangen entkoppeln Senden und Verarbeiten. Storage Queues eignet sich für einfache Aufgaben, Service Bus bietet Queues und Topics, Event Grid verteilt Ereignisse, Event Hubs nimmt große Ereignisströme auf. Sie sind nicht beliebig austauschbar.

Eine Nachricht kann erneut erscheinen, obwohl ihre Arbeit fertig war, aber die Bestätigung fehlte. Verbraucher brauchen stabile Kennungen und konsistente, idempotente Verarbeitung.

**Vorschaubilder:** Nachricht identifiziert Dokument, Prozess prüft Ergebnis, erzeugt es und bestätigt. Beachte konkurrierende Verbraucher und atomare Schritte.

Überwache Alter und Anzahl wartender Nachrichten. Mehr Verbraucher helfen nicht, wenn die Datenbank begrenzt. Reihenfolge und Behandlung fehlerhafter Nachrichten hängen vom Dienst ab.

**Übung:** Plane die erneute Verarbeitung fehlgeschlagener Nachrichten ohne doppelte Dokumente oder verlorene Fehlerhistorie.

---

[Zurück](10-architecture.md) · [Weiter](12-devops.md) · [English](../en/11-messaging.md)
