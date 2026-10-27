# Governance und Compliance

[Inhalt](README.md) · [Zertifizierungen](../certifications/de/README.md)

RBAC bestimmt, wer handeln darf; Policy bestimmt Bedingungen für Ressourcen. Ein berechtigter VM-Administrator kann durch eine Regionsrichtlinie eingeschränkt werden.

Audit meldet Abweichungen, Deny blockiert unzulässige Anfragen. Modify und DeployIfNotExists brauchen passende Konfiguration und Rechte. Bestehende Ressourcen können eine Korrekturaufgabe benötigen.

Tags wie project, environment und owner klassifizieren. Sie sind keine Sicherheitsgrenze und werden nicht immer automatisch vererbt. Verwaltungssperren ersetzen weder Backups noch Datenberechtigungen.

Defender for Cloud und Sentinel erfüllen unterschiedliche Aufgaben. Die Zertifizierung des Anbieters macht unsere Anwendung nicht automatisch regelkonform.

**Übung:** Führe eine Regel zuerst als Audit ein. Prüfe Auswirkungen und Zuständigkeiten, bevor du blockierst. Jede Ausnahme braucht Begründung und Überprüfung.

---

[Zurück](06-identity.md) · [Weiter](08-observability.md) · [English](../en/07-governance.md)

## Microsoft-Learn-Vertiefung · policy

Korrekturaufgaben wenden modify oder deployIfNotExists auf vorhandene Ressourcen an. Sie verwenden Identität und Rechte der Zuweisung. Eine Definitionsänderung aktualisiert nicht automatisch jede Berechtigung.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources) · [Microsoft-Learn-Vertiefung](15-microsoft-learn.md#learn-policy)
