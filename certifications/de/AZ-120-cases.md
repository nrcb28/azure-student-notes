# AZ-120 · Zehn Fälle mit begründeten Antworten

[Leitfaden](AZ-120.md) · [Arbeitsbuch](AZ-120-workbook.md) · [Inhalt](README.md)

Eigene Unternehmensszenarien einer Universität, keine offiziellen Prüfungsfragen. Erkläre Entscheidung und Belege vor dem Öffnen der Antwort. Alle vorgeschlagenen Prüfungen sind Offline-Entwurfsarbeit; Azure- oder SAP-Ausführung wird nicht behauptet.

## 1. Die Universität ergänzt zwei Anwendungsserver, behält aber je eine ASCS- und HANA-VM. Sind wichtige einzelne Ausfallpunkte beseitigt?

<details>
<summary>Antwort</summary>

Nein. Redundante Anwendungsserver schützen weder zentrale Dienste noch Datenbank. Inventarisiere jede SID und unterscheide ASCS, ERS, Anwendungsinstanzen, HANA, gemeinsame Dateien und Abhängigkeiten. Schlage unterstützte Hochverfügbarkeit für zentrale Dienste und Datenbank mit ausdrücklicher Verantwortung und Client-Wiederverbindung vor. Belege sollen Abhängigkeitsdiagramm und vorhergesagte Folgen jedes Komponentenausfalls umfassen. Prüfe auch Anwendungskapazität nach einem Ausfall. Die Zahl der VMs zeigt nicht, dass eine Einkaufstransaktion den Verlust ihres Koordinations- oder Datendiensts übersteht.

</details>

## 2. Eine günstigere VM hat gleich viele Kerne wie die vorgeschlagene HANA-VM. Genügt das für einen Austausch?

<details>
<summary>Antwort</summary>

Nein. Prüfe SAP-HANA-Zertifizierung für genauen VM-Typ, Workload, Betriebssystemversion, Datenbankversion und Bereitstellungsmodell. Vergleiche gemessenen Speicherbedarf, Wachstum, relevante SAPS-Anforderungen der Anwendungsebene, Speicherdurchsatz, Protokolllatenz und Netzwerkgrenzen. Prüfe außerdem regionale Kapazität und Kontingente. Beleg sind dokumentierte unterstützte Kombination und Dimensionierung mit Ausfallreserve, kein CPU-Vergleich. Eine niedrigere Infrastrukturschätzung entscheidet nicht über Unterstützung; diese Lernnotizen können weder SAP-Nutzungsrechte der Universität noch ausreichende Produktionskapazität feststellen.

</details>

## 3. Das Campusteam behauptet, ExpressRoute verschlüssele jede SAP-Verbindung. Soll das ADR dies übernehmen?

<details>
<summary>Antwort</summary>

Nein. Private Verbindung und Verschlüsselung sind getrennte Eigenschaften. Zeichne Campus-Azure-Pfad, Anbieterübergabe, Azure-Routing, Anwendungsendpunkte und gewählte Verschlüsselungsgrenzen. Definiere bei Richtlinienbedarf unterstützte Anwendungsverschlüsselung oder eine andere geeignete Lösung und prüfe genaue Dienstfähigkeiten. Dokumentiere DNS-Auflösung, Authentifizierungsabhängigkeiten, Routenausfallsicherheit und erlaubte Flüsse. Die Belege sollen zeigen, welcher Verkehr verschlüsselt wird, wo Schutz beginnt und endet und wie die Konfiguration geprüft würde. Eine private Leitung allein beweist keine durchgehende Vertraulichkeit für jedes Protokoll.

</details>

## 4. Ein Student platziert beide HA-Knoten in einer PPG und behauptet Schutz vor Zonenausfall. Was muss die Begründung ändern?

<details>
<summary>Antwort</summary>

Trenne räumliche Nähe für Latenz von Isolation für Ausfallsicherheit. Eine PPG begrenzt physische Entfernung und liefert keine zonenübergreifende Fehlerisolation. Wähle unterstützte Verfügbarkeitsplatzierung für die Wiederherstellungsanforderung und bewerte dann tatsächliche Knotenlatenz und Replikation. Sind PPGs begründet, nutze sie innerhalb passender Platzierungsgrenzen und dokumentiere Zuweisungseinschränkungen. Belege sollen Fehlerdomänendiagramm, gemessene oder ausdrücklich angenommene Latenz, Restkapazität und Übernahmereihenfolge enthalten. Weder PPG noch Verfügbarkeitszonen konfigurieren allein einen sicheren SAP-Cluster oder ein Datenbankfailover.

</details>

## 5. HANA hat viel freien Speicherplatz, doch Einkäufe werden bei Sicherungspunkten langsam. Nur Kapazität ergänzen?

<details>
<summary>Antwort</summary>

Untersuche Daten- und Protokolldurchsatz, Latenz, Warteschlangen und die gesamte E/A-Grenze der VM. Sicherungspunktverkehr kann trotz viel freiem Platz mit Protokollschreibvorgängen konkurrieren. Prüfe unterstütztes Speicherlayout, Dateisystem, Datenträgerkonfiguration, Bedarf gemeinsamer Volumen und Lastzeitpunkte vor einer Änderung. Caching oder Write Accelerator müssen genauen Volumen- und Speicherhinweisen folgen, keiner pauschalen Leistungsregel. Beleg sind korrelierte Last- und E/A-Zeitleiste sowie vorgeschlagene unterstützte Konfiguration. Kennzeichne Messungen als benötigte Belege, bis ein genehmigter Test sie tatsächlich liefert.

</details>

## 6. Ein Cluster kann nach Kommunikationsfehler seinen Partner nicht per Fencing isolieren. Würde Abschalten von Fencing den Dienst sicher wiederherstellen?

<details>
<summary>Antwort</summary>

Nein. Entferntes Fencing kann konkurrierende Primärsysteme und Datenintegritätsschäden ermöglichen. Sichere Belege und folge dem Vorfallsverfahren bei Prüfung von Quorum, Knotenkommunikation, Fencing-Agent-Rechten und Verbindung oder unterstützter SBD-Konfiguration. Bestätige vor Übernahme, dass der vermeintlich ausgefallene Knoten nicht unabhängig schreiben kann. Belege sollen Clusterzustand, Zeitmarken, Fencing-Ergebnisse, Replikationszustand und ein maßgebliches Primärsystem enthalten. Die Korrektur stellt unterstützte Isolation und Entscheidungsfähigkeit wieder her. Gestartet erscheinende Clusterressourcen belegen keinen sicheren SAP-Schreibbetrieb.

</details>

## 7. Eine falsche Finanzänderung hat beide HANA-Replikate erreicht. Warum ist die geschützte Sicherung von gestern wichtig?

<details>
<summary>Antwort</summary>

Replikation erhält Verfügbarkeit, kann aber logische Fehler kopieren. Eine geschützte Sicherung und nutzbare Protokollkette können nach unterstütztem Verfahren einen akzeptablen Punkt vor dem Fehler wiederherstellen. Bestimme fachlich genehmigtes RPO, Abhängigkeiten, Aufbewahrung und später erfolgte legitime Transaktionen mit Abgleichbedarf. Prüfe Anwendungskonsistenz; ein allgemeiner VM-Snapshot genügt nicht automatisch. Belege sollen Auswahl des Wiederherstellungspunkts, Sicherungs- und Protokollverfügbarkeit, isolierten Wiederherstellungsplan, Datenbankprüfungen und fachliche Validierung enthalten. Erfolgreiche Replikation allein stellt nach derselben falschen Änderung auf beiden Kopien keine historische Korrektheit wieder her.

</details>

## 8. Nach grundlegender Umschaltprüfung erfassen Nutzende neue Bestellungen. Kann Rückführung einfach DNS auf die unveränderte Quelle setzen?

<details>
<summary>Antwort</summary>

Das würde neue Transaktionen aufgeben oder verzweigen. Nach Beginn von Zielschreibvorgängen braucht die Betriebsanweisung eine getrennte Entscheidung: erneuter Schreibstopp, maßgeblicher Datenbestand, Erhalt neuer Transaktionen und Prüfung unterstützten Abgleichs oder Rückmigration. Ergänze fachliche Zustimmung, Schnittstellenwarteschlangen, Endabgleich, Quellisolation und Validierung vor Wiederöffnung einer Seite. Beleg ist eine Zeitleiste der Schreibverantwortung mit dokumentierter Datenbehandlung, nicht nur DNS-Anweisungen. Die Probe soll Rückführung vor Schreibfreigabe von späterer Wiederherstellung mit klaren Fristen und Verantwortlichen je Kontrollpunkt unterscheiden.

</details>

## 9. Das Forschungsportal erreicht SAP RISE nicht. Soll der Betreiber mit der Azure-Rolle der Universität NSGs in SAPs Abonnement ändern?

<details>
<summary>Antwort</summary>

Beachte zuerst die vertragliche Verantwortungsmatrix. SAP verwaltet die RISE-Landschaft in einer eigenen Azure-Umgebung; eine Universitäts-Abonnementrolle gewährt dort keine Kontrolle. Verfolge Portal-DNS, Routen, Peering oder Verbindung, Firewallregeln, Identität und vereinbarte SAP-Schnittstelle und weise Prüfungen den richtigen Verantwortlichen zu. Koordiniere SAP-seitige Änderungen und Eskalation über SAP. Belege sollen den scheiternden Übergabepunkt und Aufgaben beider Seiten enthalten. RISE beseitigt keine Kundenverantwortung für eigene Integrationsdienste, Sicherheitskonfiguration oder Netzwerkweg zu einer verfügbaren Schnittstelle.

</details>

## 10. Die Wiederherstellungsregion hat aktuelle Datenbankkopie und laufende VMs, aber Einkauf bleibt unerreichbar. Was fehlt im Planspiel?

<details>
<summary>Antwort</summary>

Prüfe zentrale Dienste, Anwendungsstartreihenfolge, Identität, DNS, virtuelle Namen, Routen, Geheimnisse, gemeinsame Dateien, Integrationsendpunkte und genügend unterstützte Kapazität. Vergleiche nutzbaren Datenstand und vorhergesagte Wiederherstellungszeit mit fachlichem RPO und RTO. Verhindere unabhängiges Schreiben des ursprünglichen Primärsystems. Definiere erfolgreichen Einkauf und Schnittstellenaustausch als Abnahme, gefolgt von kontrollierter Rückkehr zur Primärregion. Belege sollen Verantwortung, Abhängigkeitsreihenfolge, Replikationszustand, vorhergesagte Zeiten und Validierungskriterien enthalten. Laufende Infrastruktur ist nur ein Teil der Wiederherstellung eines vollständigen universitären SAP-Diensts.

</details>

Zieldaten und sechs technische Primärquellen stehen im [Leitfaden](AZ-120.md). Entwickle prüfbare Diagramme und Betriebsanweisungen im [Arbeitsbuch](AZ-120-workbook.md).
