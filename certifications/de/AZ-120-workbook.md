# AZ-120 · Gemeinsames Arbeitsbuch für Fortgeschrittene

[Leitfaden](AZ-120.md) · [Zehn Fälle](AZ-120-cases.md) · [Inhalt](README.md)

Fünf übereinstimmende Einheiten in allen Sprachen. Arbeite offline an SAP-Einkaufs- und Finanzlandschaft der fiktiven Universität und der Forschungsportalintegration. Lizenz, Azure-Bereitstellung, SAP-Ausführung oder Produktionsreife werden weder geliefert noch behauptet. Trenne Annahmen und vorhergesagte Ergebnisse von beobachteten Belegen.

<a id="az-120-unit-1"></a>

## 1. Verantwortung und unterstützte Kapazität inventarisieren

Zeichne Produktions- und Nichtproduktions-SIDs, Anwendungsserver, ASCS/ERS oder SCS, HANA, gemeinsame Dateien, Identität, DNS und Schnittstellen. Benenne Verantwortliche für Infrastruktur, Betriebssystem, Basis, Datenbank, Sicherheit und fachliche Validierung. Erkläre verbleibende einzelne Ausfallpunkte trotz redundanter Anwendungsserver. Erstelle eine Dimensionierung für relevante SAPS, Speicher, Wachstum, Durchsatz, Latenz und Ausfallreserve; mache SKU-Wahl von Zertifizierungs- und Kompatibilitätsprüfungen abhängig.

**Szenario:** Eine günstigere VM hat dieselbe Kernzahl, aber keine dokumentierten HANA-Unterstützungsbelege. **Belege:** Abhängigkeitskarte, unterstützte VM-/Betriebssystem-/Datenbank-/Speicherkombination, regionale Kontingentannahmen und Verantwortung für Lizenzprüfung. **Abgabe:** Architekturentscheidung mit Abnahmekriterien und offenen Messungen. Wiederhole die [Compute-Grundlagen](../../de/03-compute.md).

<a id="az-120-unit-2"></a>

## 2. Platzierung, Netzwerk und HANA-Speicher entwerfen

Zeichne unterstützte Anwendungs-Datenbank-Pfade, Verwaltung, Replikation, Sicherung, Campusverbindung und DNS-Weiterleitung. Trenne private ExpressRoute-Verbindung von gewählten Verschlüsselungskontrollen. Vergleiche Zonenisolation mit PPG-Nähegrenzen unter ausdrücklichen Latenzannahmen. Plane `/hana/data`, `/hana/log` und `/hana/shared`, unterstützte Dateisysteme, Datenträger- und VM-E/A-Grenzen sowie konfigurationsabhängige Caching- oder Write-Accelerator-Entscheidungen.

**Szenario:** Ein Sicherungspunkt fällt mit langsamen Einkäufen zusammen; ein Vorschlag fügt ein Prüfgerät zwischen SAP-Anwendungs- und Datenbankebene ein. **Belege:** Verkehrswege, Platzierungsdiagramm, vorhergesagtes Latenzbudget, Volumenrollentabelle und benötigte E/A-Beobachtungen. **Abgabe:** unterstützte Alternative mit Kapazitäts- und Fehlerdomänenabwägung. Wiederhole die [Netzwerkgrundlagen](../../de/05-networking.md).

<a id="az-120-unit-3"></a>

## 3. Sicheres Failover von historischer Wiederherstellung trennen

Erkläre HANA System Replication, unterstützte Clustersteuerung, ASCS/SCS-Schutz, ERS, Quorum, Fencing, virtuelle Namen und Lastenausgleichsprüfungen. Zeichne den einzigen erlaubten Schreiber nach einer Netztrennung. Definiere fachliches RPO und RTO, workloadkonsistente Sicherungen, nutzbare Protokolle, Aufbewahrung und Wiederherstellungsabhängigkeiten. Zeige, warum Replikation Fehler kopieren kann und ein unkoordinierter Snapshot keine Anwendungskonsistenz beweist.

**Szenario:** Der Partner lässt sich nicht isolieren, und ein Finanzfehler ist bereits repliziert. **Belege:** vorhergesagte Clusterentscheidungen, Fencing-Abhängigkeiten, maßgebliche-Kopie-Regel, Sicherungs-/Protokollverfügbarkeit und Validierungskriterien. **Abgabe:** getrennte Hochverfügbarkeits- und Wiederherstellungsanweisungen, die deaktiviertes Fencing ausdrücklich als Reparatur ablehnen und fachlichen Abgleich nach historischer Wiederherstellung vorsehen.

<a id="az-120-unit-4"></a>

## 4. Eine Migrations- und Integrationsanweisung schreiben

Bewerte Quellunterstützung, Versionen, Schnittstellen, Änderungsrate, Übertragungsdauer, Ausfallzeit und Zielkompatibilität. Begründe einen unterstützten Migrationsweg. Definiere Probe, Schreibstopp, Endabgleich, Quellisolation, DNS-/Schnittstellenänderungen, technische Prüfungen, fachliche Abnahme und Schreibfreigabe. Ordne bei RISE Kundenintegration und SAP-Aufgaben anhand des Vertrags zu, statt Abonnementzugriff anzunehmen.

**Szenario:** Nach der Umschaltung entstehen Bestellungen; danach fällt das Forschungsportal aus. **Belege:** Zeitleiste der Schreibverantwortung, Warteschlangenstatus, Schnittstellenübergaben, Validierungspunkte und Entscheider. **Abgabe:** Rückführung vor neuen Schreibvorgängen und eine getrennte Entscheidung über späteren Abgleich oder Rückmigration einschließlich SAP-Eskalation, wenn die Fehlergrenze zu RISE gehört.

<a id="az-120-unit-5"></a>

## 5. Betrieb prüfen und regionale Wiederherstellung proben

Prüfe eine fiktive IaC-Änderung auf Image-Unterstützung, Platzierung, Speicher, Geheimnisreferenzen, Abhängigkeiten und destruktive Unterschiede. Staffel Updates mit clusterbewusster Reihenfolge und Rücksetzkriterien. Definiere Azure-Monitor-Erfassung, SAP-Überwachungsanbieter, Datenbank- und Clusterbelege, Alarmverantwortung und Aufbewahrung. Stelle den gesamten Dienst in einer anderen Region wieder her, einschließlich Identität, Netzwerk, zentraler Dienste, Apps, Daten, Integrationen und Rücksynchronisierung.

**Szenario:** Während des Einkaufs tritt ein regionaler Ausfall auf, während ein Größenänderungsvorschlag offen ist. **Belege:** Abhängigkeitsreihenfolge, vorhergesagtes RPO/RTO, Ausfallkapazität, Replikationszustand, fachliche Ablaufprüfungen und Verantwortliche für laufende Compute-/Speicher-/Netzwerk-/Überwachungskosten. **Abgabe:** Vorfallsplanspiel und Änderungsprüfprotokoll mit Trennung zwischen geplanten Prüfungen und ausgeführten Tests.

Hinterfrage Annahmen anhand der sechs technischen Quellen im [Leitfaden](AZ-120.md). Diese eigenen Übungen wählen nützliche Konzepte aus; sie decken nicht jedes offizielle Ziel ab und garantieren kein Prüfungsergebnis.
