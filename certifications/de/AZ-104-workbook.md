# AZ-104 · Gemeinsames Vertiefungsheft

[←](README.md) · [Gemeinsamer Lernkern](../../de/16-common-core.md) · [Vertiefende Übungen](../../de/17-advanced-labs.md)

Ziele, Fälle und Abgaben entsprechen sich in allen acht Sprachen. Gleichwertigkeit wird anhand von Lerneinheiten und Nachweisen geprüft, nicht anhand der Wortzahl. Frühere Leitfäden bleiben ergänzende Erklärungen.

<a id="az-104-unit-1"></a>

## 1. Effektiven Zugang verfolgen

Erfasse Identität, Mandant, Abonnement, Ressource, Aktion und Bereich. Prüfe Gruppen, direkte und geerbte Zuweisungen, Bedingungen und Weitergabezeit. Trenne Verwaltungs- und Datenaktionen. Rollenzuweisung braucht eigene Rechte.

**Fall:** Storage erstellen, Blobs nicht auflisten. **Nachweis:** benötigtes Recht und minimale Prüfung mit derselben Identität. Nicht pauschal Owner vergeben oder ohne Hypothese Netzwerkregeln ändern.

<a id="az-104-unit-2"></a>

## 2. Daten schützen und wiederherstellen

Wähle Schutz auf Objekt-, Container- und Kontoebene. Halte vorher aktivierte Funktionen fest. Versionierung kann Auswahl oder Beförderung einer Version erfordern; es gibt kein universelles Verfahren.

**Fall:** Übungsdatei unverändert zurückholen. **Nachweis:** vorherige Konfiguration, Hashes vorher/nachher, Rechteprüfung und nach Bereinigung weiterhin aufbewahrte Daten.

<a id="az-104-unit-3"></a>

## 3. Infrastruktur vor Änderungen lesen

Interpretiere Parameter, Ressourcen, Abhängigkeiten, Outputs und Unterschiede. Trenne Kompilierung, Validierung, What-if und Anwendung. Exporte brauchen eventuell Bearbeitung; Quoten, Regionen und Policies können gültige Syntax blockieren.

**Fall:** What-if analysiert ein Modul nicht. **Nachweis:** Diagnose, ausgeschlossener Bereich und Klärung vor Anwendung. Bei VM-Änderungen Datenträger, Netzwerk und Einstellungen prüfen.

<a id="az-104-unit-4"></a>

## 4. Den gesamten Weg diagnostizieren

Verfolge DNS, IP, Route, NSG, Gast-Firewall, Listener und Autorisierung. Mehrere zustandsbehaftete Filter können wirken. Prüfe Frontend, Backend, Regel und Probe. Trenne privaten App-Service-Eingang von ausgehender Integration.

**Fall:** Probe gesund, echte Anfrage scheitert. **Nachweis:** Ports, Antworten, geltende Regeln und testbare Hypothese. Probe-Gesundheit beweist keine fachliche Korrektheit.

<a id="az-104-unit-5"></a>

## 5. Mit Nachweisen betreiben

Definiere Metrik, Log, Alarm, Aktion und Eigentümer. Prüfe Quelle, Zuordnung und Ziel vor der Abfrage. Miss vollständige Wiederherstellung inklusive Identität, DNS und Abhängigkeiten.

**Abgabe:** Storage- und Rolleninspektionsübung, Erwartung gegenüber Beobachtung, Wiederherstellungsablauf. Lokale Prüfungen von Azure-Tests trennen; Löschung oder verbleibende Aufbewahrung nachweisen.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104) · [AZ-104](AZ-104.md)
