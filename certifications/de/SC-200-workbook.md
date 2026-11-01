# SC-200 · Arbeitsbuch für Entscheidungen und Belege

[Leitfaden](SC-200.md) · [Zehn Fälle](SC-200-cases.md) · [Inhalt](README.md)

Fünf eigene Einheiten für eine fiktive universitäre Notizen-App. Arbeiten Sie offline mit erfundenen Datensätzen und Kennungen. Kennzeichnen Sie erwartete Ergebnisse getrennt von den in der Übung gelieferten Beobachtungen. Weder Mandantenzugriff, Cloud-Bereitstellung, Live-Abfrage, Nachrichtenversand noch Eindämmung ist erforderlich oder wird behauptet.

<a id="sc-200-unit-1"></a>

## 1. Erfassungs- und Zugriffsgrenzen abbilden

Zeichnen Sie Microsoft 365, eine Azure-Anwendung, einen lokalen Server und eine Campus-Firewall. Ordnen Sie nach Bedarf Defender-XDR-Untersuchung oder Sentinel-Erfassung und -Analyse zu. Legen Sie für jede Quelle Onboarding, Connector-Voraussetzungen, erwartete Tabelle und Zeitspalte, stabile Kennungen, Verzögerung, Aufbewahrung und einen Verantwortlichen fest. Trennen Sie Lese-, Vorfallverwaltungs-, Regelautoren- und Automatisierungsberechtigungen.

**Szenario:** Der Firewall-Connector erscheint verbunden, aber sein erforderliches Ereignis fehlt. **Belege:** eine Abdeckungstabelle mit vier Quellen, eine Frage zum Erfassungszustand und ein synthetisches Ereignis mit erwartetem Schema. **Ergebnis:** ein Diagramm und eine Lückenliste, die erklären, was der Analyst schließen kann. Fügen Sie Verarbeitungsregeln für personenbezogene Daten und Exporte hinzu; sammeln Sie keine echten Studierendeninformationen.

<a id="sc-200-unit-2"></a>

## 2. Eine begründbare Vorfallzeitleiste erstellen

Erfinden Sie sechs Datensätze über E-Mail, Identität, Endpunkt, Anwendung und Cloud-Workload hinweg. Geben Sie jedem Datensatz UTC-Ereigniszeit, Erfassungszeit, Quellen-ID, Entitätskennungen und Beobachtung. Gruppieren Sie zusammenhängende Warnungen zu einem vorgeschlagenen Vorfall, ohne anzunehmen, eine gemeinsame Campus-IP beweise die Beziehung. Trennen Sie bekannten Umfang, vermuteten Umfang und nicht verfügbare Telemetrie.

**Szenario:** Eine verdächtige Nachricht geht einem scheinbaren privaten Dokumentzugriff voraus. **Belege:** Zeitleiste, Entitätskarte, eine konkurrierende Erklärung und ein angeforderter fehlender Datensatz. **Ergebnis:** eine Triagenotiz mit Verantwortlichem, Prioritätsbegründung, vorgeschlagener Eindämmung, Autorisierungsanforderung, Serviceauswirkungen und Wiederherstellungsbedingung. Markieren Sie jede vorgeschlagene Aktion als nicht ausgeführt; erwartete Bestätigung ist keine beobachtete Reaktion.

<a id="sc-200-unit-3"></a>

## 3. Abfrageergebnisse erklären, bevor Zählwerten vertraut wird

Lesen Sie den festen synthetischen KQL-Datensatz des Leitfadens. Verfolgen Sie Zeilen durch das halboffene UTC-Fenster, den Denied-Filter, Deduplizierung und Aggregation. Erklären Sie, warum zwei Ereignisse für `student-a` erwartet werden. Fügen Sie eine zweite erfundene Tabelle mit zwei Zeilen für dieses Konto hinzu und zeichnen Sie die Paarungen eines ausdrücklichen Inner Joins. Vergleichen Sie dies mit der linksseitigen Deduplizierung durch das standardmäßige `innerunique`.

**Szenario:** Ein Bericht verwechselt verknüpfte Zeilen mit getrennten Angriffen. **Belege:** Zwischenzählwerte, Join-Schlüssel, Kennungsannahmen und ein Beispiel an der Zeitgrenze. **Ergebnis:** eine korrigierte Interpretation mit erwarteter Ausgabe und Grenzen. Es wird keine Abfrageausführung behauptet; optionale lokale Berechnungen bleiben von Mandantenbeobachtungen getrennt.

<a id="sc-200-unit-4"></a>

## 4. Eine Hunting-Hypothese in eine Abstimmungsprüfung überführen

Schreiben Sie eine Hypothese, die den Empfang verdächtiger Nachrichten mit ungewöhnlichem privaten Dateizugriff verknüpft. Definieren Sie Population, UTC-Fenster, erforderliche Quellen und eine alternative Erklärung. Erstellen Sie vier gekennzeichnete harmlose und vier bedenkliche synthetische Beispiele. Schlagen Sie eine Erkennung und eine enge Ausnahme vor und identifizieren Sie anschließend, welche Beispiele warnen, übersehen werden oder mehr Kontext benötigen. Erklären Sie, wie ASIM kompatible Quellen normalisieren könnte und wo Parserzuordnungen validiert werden müssen.

**Szenario:** Ein autorisierter Import ähnelt Missbrauch. **Belege:** eine versionierte Entscheidungstabelle, Quellenlücken, Analyse falsch positiver und falsch negativer Ergebnisse und eine Parser-Zuordnungsprüfung. **Ergebnis:** eine Abstimmungsempfehlung. Eine leere Suche und weniger Warnungen beweisen weder fehlende Kompromittierung noch vollständige Abdeckung.

<a id="sc-200-unit-5"></a>

## 5. Einen unterstützten Reaktionsworkflow prüfen

Skizzieren Sie eine Automatisierungsregel, die ein Playbook zur Anreicherung aufruft und vor störender Eindämmung eine Genehmigung anfordert. Identifizieren Sie Operator, Sentinel-Aufrufberechtigung, Workflow-Identität und nachgelagerten Umfang getrennt. Simulieren Sie einen doppelten Auslöser und eine Zeitüberschreitung; dokumentieren Sie Kennungen und Zustandsprüfungen, die doppelte Tickets oder unnötig wiederholte Einschränkungen verhindern. Fügen Sie einen Verantwortlichen und Wiederherstellungsbedingungen hinzu.

**Szenario:** Eine KI-Zusammenfassung verknüpft eine Cloud-Warnung mit dem Download eines Studierenden, ohne dass ein Anwendungsprotokoll vorliegt. **Belege:** eine Zuordnungstabelle von Behauptungen zu Quellen, korrigierte Schlussfolgerung, Genehmigungsgrenze und erwartetes Wiederholungsverhalten. **Ergebnis:** ein geprüftes Planspiel-Handbuch. Prüfen Sie Copilot-Vorschläge anhand bereitgestellter Datensätze und Abfragesemantik. Es wird weder eine Benachrichtigung noch eine Genehmigungsanfrage oder echte Reaktion gesendet.

[Offizieller Studienleitfaden](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · [Beobachtbarkeitsgrundlagen](../../de/08-observability.md)
