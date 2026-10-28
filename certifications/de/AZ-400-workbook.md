# AZ-400 · Gemeinsames Vertiefungsheft

[←](README.md) · [Gemeinsamer Lernkern](../../de/16-common-core.md) · [Vertiefende Übungen](../../de/17-advanced-labs.md)

Ziele, Fälle und Abgaben entsprechen sich in allen acht Sprachen. Gleichwertigkeit wird anhand von Lerneinheiten und Nachweisen geprüft, nicht anhand der Wortzahl. Frühere Leitfäden bleiben ergänzende Erklärungen.

<a id="az-400-unit-1"></a>

## 1. Nachverfolgbarkeit und Git

Verbinde Bedarf, Issue, PR, Commit, Build, Artefakt und Deployment. Definiere konsistente Metrikgrenzen. Bewerte Menschen nicht nach Zeilen oder Commits. Wähle Zweige nach Frequenz und gepflegten Versionen.

**Fall:** gemeinsame Veröffentlichung zurücknehmen. **Nachweis:** Revert gegenüber Geschichtsänderung und Datenfolgen. Geheimnisse zuerst widerrufen oder rotieren.

<a id="az-400-unit-2"></a>

## 2. Tests und Artefakte

Einmal bauen, identifiziertes Ergebnis befördern. Version, Digest und Ursprung festhalten. Tests nach Risiko kombinieren; Coverage beweist keine guten Assertions.

**Fall:** gestern ohne Codeänderung erfolgreich. **Nachweis:** unfixierte Werkzeuge, Abhängigkeiten und Basisimages untersuchen. Instabile Tests nicht nur bis grün wiederholen. Cache und Artefakte trennen.

<a id="az-400-unit-3"></a>

## 3. Runner-Grenzen und Identität

Trenne vertrauenswürdigen Code, PR-Eingaben, Workflow-Rechte und Cloud-Bereich. Eigene Runner brauchen Isolation, Updates und Bereinigung. OIDC erfordert weiter genaue Vertrauensstellung und Autorisierung.

**Fall:** externer PR ändert internes Skript. **Nachweis:** Ausführung ohne Produktionszugriff, Identitätsgrenzen und Ressourcenkontrollen. Pipeline-Code ist nicht automatisch harmlos.

<a id="az-400-unit-4"></a>

## 4. Veröffentlichen und zurückkehren

Vergleiche Rolling, Blue-Green, Canary, Rings und Flags. Definiere Nutzergruppe, funktionale Signale, Beobachtung und Abbruch. Swaps isolieren nicht alle Abhängigkeiten. Plane kompatible Migrationen.

**Fall:** normale CPU, falsche Canary-Ergebnisse. **Nachweis:** fachliches Signal und Rollback-Kriterium. Erkläre, warum ein altes Image keine gelöschte Spalte erzeugt.

<a id="az-400-unit-5"></a>

## 5. Betriebskreis schließen

Kontext weitergeben, Versionen in Telemetrie aufnehmen, Log-Daten schützen. Alarmverantwortliche und Fenster benennen. Ressourcenfreigaben sind nicht nur veränderbare YAML-Bedingungen.

**Abgabe:** vollständiger Pipeline-Entwurf, sinnvoller Test, festes Artefakt und Beförderung. Lokalen Simulator mit geänderter Retry-Regel wiederholen. Postmortem mit Maßnahme, Eigentümer und Prüfung.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400) · [AZ-400](AZ-400.md)
