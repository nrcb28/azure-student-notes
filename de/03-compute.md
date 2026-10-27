# Compute und Container

[Inhalt](README.md) · [[object Object]](../certifications/de/README.md)

Eine VM passt bei Kontrolle über das Betriebssystem, App Service bei kompatiblen Webanwendungen, Functions bei ereignisgesteuertem Code. Container Instances und Container Apps führen Container ohne selbst verwalteten Kubernetes-Cluster aus. AKS lohnt sich, wenn Anforderungen Kubernetes und seinen Betriebsaufwand rechtfertigen.

Ein Container ist keine vollständige VM. Serverless hat weiterhin Grenzen für Start, Laufzeit, Netzwerk und Abrechnung.

**Diagnose:** Der Container startet, beantwortet aber keine Anfrage. Prüfe Port, Prozess, Einstellungen, Startprotokolle und Zustandsprüfungen. Danach teste eine vollständige Anfrage samt Abhängigkeiten.

Trenne Image und Konfiguration. Geheimnisse gehören nicht in Image-Schichten. Eine identifizierbare Version lässt sich besser nachvollziehen als ein veränderliches latest-Tag.

**Übung:** Begründe, warum eine einfache API AKS braucht oder mit einer anderen Plattform auskommt.

---

[Zurück](02-resources.md) · [Weiter](04-storage.md) · [English](../en/03-compute.md)
