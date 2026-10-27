# DevOps und Infrastruktur als Code

[Inhalt](README.md) · [[object Object]](../certifications/de/README.md)

DevOps verbindet Entwicklung und Betrieb für zuverlässige Änderungen. CI integriert mit Build und Prüfungen. Continuous Delivery hält Änderungen veröffentlichungsbereit; Continuous Deployment veröffentlicht automatisch nach Kriterien.

Befördere dasselbe getestete Artefakt. Versionen und Digests machen nachvollziehbar, was lief.

Bicep beschreibt Azure-Ressourcen. Terraform verwaltet schützenswerten Zustand. Plan und What-if helfen, garantieren aber nicht jede spätere Operation. OIDC vermeidet langlebige Geheimnisse, nicht Vertrauenskonfiguration und Berechtigungen.

**Rollback:** Alter Code stellt keine gelöschte Datenbankspalte wieder her. Plane kompatible Migrationen und geprüfte Wiederherstellung.

Ein privilegierter Runner darf nicht wahllos nicht vertrauenswürdigen Code ausführen.

**Übung:** Verbinde Issue, PR, Test, Artefakt und Release. Definiere Beförderungs- und Rollback-Signale. Führe lokal python tools/check_docs.py aus.

---

[Zurück](11-messaging.md) · [Weiter](13-laboratorios.md) · [English](../en/12-devops.md)
