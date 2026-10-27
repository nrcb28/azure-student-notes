# Ressourcen und Verfügbarkeit

[Inhalt](README.md) · [[object Object]](../certifications/de/README.md)

Ein Abonnement bildet Grenzen für Verwaltung, Kontingente und Abrechnung. Verwaltungsgruppen bündeln Governance mehrerer Abonnements. Ressourcengruppen ordnen Ressourcen mit zusammengehörigem Lebenszyklus. Der Entra-Mandant ist das Identitätsverzeichnis, kein gewöhnlicher Ressourcencontainer.

Die Region einer Ressourcengruppe betrifft ihre Metadaten. Ihre Ressourcen dürfen anderswo liegen. Verfügbarkeitszonen bieten physische Trennung innerhalb einer Region; Unterstützung hängt vom Dienst ab.

**Beispiel:** Entwicklung und Produktion werden getrennt. Ein gemeinsam genutztes Netzwerk darf nicht zusammen mit einer einzelnen Anwendung gelöscht werden.

Vor einem Ressourcenwechsel prüfen wir Unterstützung, Abhängigkeiten, Berechtigungen und Kennungen. Ein Wechsel der Ressourcengruppe ist keine universelle Regionsmigration.

**Übung:** Erkläre den tatsächlich tolerierten Ausfall statt nur die Zahl der Instanzen.

---

[Zurück](01-fundamentals.md) · [Weiter](03-compute.md) · [English](../en/02-resources.md)
