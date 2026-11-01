# SC-100 · Arbeitsbuch zur Sicherheitsarchitektur

[Leitfaden](SC-100.md) · [Zehn Fälle](SC-100-cases.md) · [Inhalt](README.md) · [English](../en/SC-100-workbook.md)

Fünf eigene Offline-Einheiten für den fiktiven universitären Notizendienst. Nutze erfundene Anlagen, Identitäten, Vorfälle und Belege. Erstelle Architekturvorschläge und Planspielergebnisse; ändere keine Mandanten, führe keine Angriffe aus, stelle keine Ressourcen bereit und verbinde keine Live-Telemetrie. Cloud-Ausführung oder Kontrollwirksamkeit wird nicht behauptet.

<a id="sc-100-unit-1"></a>

## 1. Kritikalität und Kontrollabdeckung festlegen

**Szenario:** Die Universität ergänzt unveröffentlichte Prüfungsantworten in einer App, die bisher öffentliche Notizen enthielt. Ermittle kritische Abläufe, Datenverantwortung, wahrscheinliche Bedrohungen und fachliche Auswirkungen. Unterscheide MCRA-Fähigkeitszuordnung, MCSB-Kontrollanforderungen, CAF-Plattformverantwortung und Well-Architected-Workload-Prüfung. Benenne Annahmen, statt ein vollständiges Inventar zu erfinden.

**Belege:** hypothetisches Anlagendiagramm, drei priorisierte Risiken, aktuelle Kontrollgrenzen und fehlende Informationen. Ergänze eine Anforderung, die nicht allein anhand eines Azure-Policy-Ergebnisses bewertbar ist.

**Abgabe:** Abdeckungstabelle mit Anforderung, Kontrolle, Umfang, Verantwortung, Beleg, Lücke und Abnahmekriterium. Ergänze ein kurzes ADR mit zwei Optionen und der zur Restrisikoannahme befugten Person.

<a id="sc-100-unit-2"></a>

## 2. Identität, Netzwerk und Privilegien begrenzen

**Szenario:** Campusnutzende, Gastlehrende, Administratoren, eine Bereitstellungspipeline und ein KI-Agent greifen auf verschiedene Dienstteile zu. Zeichne Identitäts-, Anwendungs-, Netzwerk- und Verwaltungsgrenzen über Campus und Clouds. Definiere Mindestberechtigungen, privilegierte Aktivierung, Wiederherstellungszugriff und Verantwortung für Zugangsdaten oder Föderation. Prüfe Funktions- und Lizenzannahmen vorgeschlagener Agent-Kontrollen.

**Belege:** sechs erwartete Erlaubnis- oder Verweigerungsentscheidungen, private DNS-Abhängigkeiten, Annahmen zum öffentlichen Zugriff und eine Erklärung der Autorisierung trotz erreichbarem Netzwerkpfad.

**Abgabe:** Vertrauensgrenzendiagramm und Zugriffsmatrix mit Verantwortung, Umfang, Lebenszyklus, Protokollierung und Fehlerverhalten. Nimm eine verweigerte Agent-Werkzeugaktion und einen Wiederherstellungsadministratorweg auf. Alle Identitäten und Anfragen bleiben fiktiv.

<a id="sc-100-unit-3"></a>

## 3. Erkennung mit autorisierter Reaktion verbinden

**Szenario:** Verdächtige Campus-Identitätsaktivität fällt mit ungewöhnlichen Dokumentdownloads zusammen. Definiere benötigte SOC-Fähigkeiten für Identität, Endpunkt, Anwendung, Cloud und SaaS. Ordne zwei priorisierte Bedrohungswege relevanten MITRE-ATT&CK-Techniken, erwarteter Telemetrie, Korrelation, Ersteinschätzung und Eindämmung zu. Erkläre Aufgaben von Sentinel und Defender XDR ohne vollständige Sicht vorauszusetzen.

**Belege:** synthetische Zeitleiste mit Ereignisquellen, Aufnahmeverzögerung, Aufbewahrungsannahmen, fehlendem Signal und konkurrierenden Erklärungen. Bestimme, wer eine Identität sperren oder einen Prüfungsserver unterbrechen darf.

**Abgabe:** Erkennungsabdeckungsmatrix und Reaktionsbefugnistabelle mit Eskalation, Freigabe, Rücknahme und Beweissicherung. Kennzeichne jede Erkennung und Reaktion als Vorschlag mit vor Betrieb benötigten Abnahmebelegen.

<a id="sc-100-unit-4"></a>

## 4. Daten sowie Software- und KI-Lebenszyklus schützen

**Szenario:** Ein neuer KI-Assistent ruft Kursdokumente ab, und eine Build-Pipeline stellt seine API bereit. Klassifiziere Informationen und ordne Grenzen für Bezeichnung, Verschlüsselung, DLP, Aufbewahrung und Anwendungszugriff zu. Benenne fehlende Unterstützung. Modelliere Bedrohungen für Abhängigkeiten, Build-Identitäten, Artefaktübernahme, Dokument-Prompt-Injection und Werkzeugzugriff.

**Belege:** ein synthetisches gutartiges Retrieval, ein Dokument mit nicht vertrauenswürdiger Anweisung und ein fiktiver nicht freigegebener Build. Dokumentiere erwartete Retrieval- und Werkzeugverweigerungen, ohne Angriffsanweisungen zu erzeugen oder Tests auszuführen.

**Abgabe:** Datenkontrollmatrix und Lebenszyklusprüfung mit Verantwortung, Umfang, Herkunft, Rechten, Freigabe und Abnahmebelegen. Erkläre, warum Erkennung, Verschlüsselung und Benchmark-Zuordnung jeweils getrennte zu bewertende Risiken offenlassen.

<a id="sc-100-unit-5"></a>

## 5. Wiederherstellung proben und Programm ordnen

**Szenario:** Ransomware betrifft primären Dokumentenspeicher und ein privilegiertes Konto. Nutze Übungsanforderungen von zwei Stunden Anwendungs-RTO und fünfzehn Minuten RPO. Verfolge Identität, Steuerungszugang, DNS, Schlüssel, Konfiguration, Metadaten, Dateien und Bereitstellungsabhängigkeiten. Vergleiche geschützte Wiederherstellungspunkte mit Replikation; berücksichtige Beschädigung und kompromittierte Sicherungsverwaltung.

**Belege:** Wiederherstellungsreihenfolge im Planspiel, hypothetische Wiederherstellungszeitpunkte, Konsistenzprüfungen und eine Abhängigkeit, die trotz wiederhergestellter Dateien autorisierte Lesezugriffe verhindert. Kennzeichne Messwerte als Annahmen.

**Abgabe:** Wiederherstellungsabnahmeplan und dreiphasige Roadmap mit Finanzierung für ein Semester. Ergänze Verantwortung, geschätzten Aufwand, Voraussetzungen, Rücksetzkriterien, befristete Ausnahmen und fachliche Genehmigung des Restrisikos. Tatsächliche Wiederherstellung oder Zielerreichung wird nicht validiert.

[Offizieller SC-100-Studienleitfaden](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100) · [ADR-Vorlage](ADR-template.md)
