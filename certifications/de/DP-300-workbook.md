# DP-300 · Gemeinsames betriebliches Arbeitsbuch

[Leitfaden](DP-300.md) · [Zehn Fälle](DP-300-cases.md) · [Inhalt](README.md)

Fünf Einheiten mit entsprechenden Zielen und Nachweisen in acht Sprachen. Bearbeite die Entwurfsübungen bei Bedarf ohne Azure. Trenne erwartetes Verhalten von tatsächlichen Beobachtungen. Keine Azure-Ausführung oder vollständige Prüfungsabdeckung wird behauptet.

<a id="dp-300-unit-1"></a>

## 1. Plattform- und Migrationswahl begründen

Erstelle eine Anforderungstabelle für die App: nötige Datenbankfunktionen, Betriebssystemzugriff, Instanzabhängigkeiten, zulässige Schreibunterbrechung, Wartungszuständigkeit und Wiederherstellungsziele. Vergleiche SQL Database, Managed Instance und SQL Server auf einer VM anhand dieser Anforderungen statt vertrauter Namen.

**Fall:** Eine bestehende geplante Aufgabe benötigt ein Betriebssystemwerkzeug. **Nachweis:** weiterhin notwendige Abhängigkeit, unterstütztes Ziel oder Neuentwurf und Kompatibilitätsprüfung. **Abgabe:** Migrationsfolge mit Anfangsübertragung, Schreibstopp, Validierung, Umschaltung, Rücknahmezuständigkeit und Plan für Schreibvorgänge nach Umschaltung. Eine fertige Kopie ist kein Abnahmetest.

<a id="dp-300-unit-2"></a>

## 2. Zugriff und Vertraulichkeitsgrenzen trennen

Zeichne den Pfad von einer Anwendungsidentität zu einer erlaubten Tabellenoperation. Markiere Namensauflösung, Netzwerkzugriff, Authentifizierung, Datenbankprinzipal und Objektrechte. Trenne Zuständigkeiten für Anwendung, Deployment und Notfalladministration. Bestimme, welche Daten in Abfragen, Protokollen, Exporten und Backups erscheinen dürfen.

**Fall:** Die private Verbindung funktioniert, aber die App darf ihre Tabelle nicht lesen. **Nachweis:** tatsächliche Identität, Datenbank, Objekt und verweigerte Aktion. Erweitere nicht ersatzweise das öffentliche Netzwerk. **Abgabe:** minimale Berechtigungsplanung und Vergleich von Transportverschlüsselung, TDE, Always Encrypted und Maskierung für eine konkrete Vertraulichkeitsanforderung. Ergänze Schlüsselwiederherstellung und Zuständigkeit.

<a id="dp-300-unit-3"></a>

## 3. Eine gemessene Verschlechterung untersuchen

Erfinde zwei vergleichbare Lastfenster für eine Dokumentberechtigungsabfrage mit Dauer, Lesezugriffen, CPU, Parallelität und Plankennung. Verknüpfe eine Änderung durch eine Hypothese mit Nachweisen und nenne eine widerlegende Beobachtung. Betrachte Blockierung und Transaktionsdauer zusammen mit der verfügbaren Query-Store-Historie. Weder normale Plattformmetriken noch ein teuer wirkender Planoperator allein erklären die Ursache.

**Fall:** Ein neuer Index verbessert Lesen und bremst Importe. **Nachweis:** Vorher-/Nachher-Ergebnisse beider Operationen unter repräsentativer Last. **Abgabe:** ein umkehrbares Optimierungsexperiment, Akzeptanzgrenzen, Rücknahmeschritte und Aussagegrenzen. Kein pauschales Verkleinern oder Beenden aller Sitzungen als Routinewartung vorschlagen.

<a id="dp-300-unit-4"></a>

## 4. Automatisierung beobachtbar und wiederholbar machen

Ordne eine nächtliche Aufgabe nach Arbeit und Zielplattform ein. Vergleiche SQL Agent für unterstützte SQL-Server- oder Managed-Instance-Workloads mit Elastic Jobs für T-SQL-Aufgaben in SQL Database. Definiere Identität, Zielmenge, Zeitplan, Zeitlimit, Wiederholungsbudget und Fehlermeldung. Externe Abhängigkeiten können eine umfassendere Orchestrierung verlangen.

**Fall:** Eine Aufgabe bestätigt ihre Ausgabe, verliert aber die Erfolgsantwort. **Nachweis:** Erkläre duplikatfreie Wiederholung und die Abschlussprüfung durch den Betrieb. **Abgabe:** Zustandstabelle für ausstehend, laufend, abgeschlossen und ungewiss sowie ein Testplan mit synthetischen Daten. Eine erfolgreiche Scheduleransteuerung ist kein geprüftes fachliches Ergebnis.

<a id="dp-300-unit-5"></a>

## 5. Daten und vollständigen Dienst wiederherstellen

Definiere getrennte Vorfälle für versehentliche Löschung und regionalen Ausfall. Wähle aufbewahrte Zustände und Verfügbarkeitsmechanismen nach ihrem jeweiligen Problem. Formuliere RPO und RTO für die App. Erfasse erforderliche Berechtigungen, Zielkapazität, Endpunkt, DNS, Authentifizierung und Abhängigkeiten. Replikation kann eine unerwünschte bestätigte Änderung übertragen.

**Fall:** Das neue Primärsystem ist gesund, doch Nutzer können keine Mitschriften herunterladen. **Nachweis:** Funktionsprüfung und Zeitfolge einschließlich Wiederverbindung. **Abgabe:** isolierter Wiederherstellungsprüfplan, Entscheidung über die maßgebliche Kopie vor Failback und Zuständigkeit für aufbewahrte Daten. Markiere vorgeschlagene Zeiten als ERWARTET, bis sie in einer geeigneten Umgebung beobachtet wurden. Eine Papierübung misst keine Azure-Wiederherstellung.

[Offizielle Ziele](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300) · [Leitfaden und technische Quellen](DP-300.md)
