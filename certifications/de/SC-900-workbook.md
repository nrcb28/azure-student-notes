# SC-900 · Arbeitsbuch für Entscheidungen und Nachweise

[Leitfaden](SC-900.md) · [Zehn Fälle](SC-900-cases.md) · [Inhalt](README.md)

Fünf eigene Einheiten mit denselben Lernzielen in jeder Sprache. Verwende eine erfundene Hochschule und synthetische Daten. Es sind Offline-Entwurfsübungen; keine Richtlinienbereitstellung, Mandantenänderung oder abgeschlossene Azure-Ausführung wird behauptet.

<a id="sc-900-unit-1"></a>

## 1. Verantwortung und Vertrauensgrenzen abbilden

Zeichne Browser, Identitätsanbieter, Anwendung und Dokumentenspeicher. Beschreibe an jeder Grenze, was geprüft wird und wer die Kontrolle betreibt. Trenne Plattformpflichten des Anbieters von Organisationsentscheidungen zu Personen, Freigaben, Konfiguration und Daten. Erkläre, warum ein Campusnetz keinen ausreichenden Vertrauensnachweis liefert.

**Szenario:** Ein Gast darf veröffentlichte Mitschriften, aber keine unveröffentlichten Lösungen lesen. **Nachweis:** Diagramm sowie Tabelle mit zwei erlaubten und zwei verweigerten Aktionen, ihren Verantwortlichen und den erforderlichen Beobachtungen. **Abgabe:** eine Seite, die Erwartungen von tatsächlich beobachteten Ergebnissen trennt. Teste für diese Übung nicht gegen einen echten Mandanten.

<a id="sc-900-unit-2"></a>

## 2. Eine Zugriffsentscheidung entwerfen

Definiere Identitätstyp, Zielanwendung, gewünschte Aktion und Mindestberechtigung. Schlage eine Authentifizierungsanforderung vor und erläutere Faktoren sowie Phishingresistenz. Beschreibe relevante Conditional-Access-Signale und weiterhin erforderliche Anwendungsprüfungen. Dokumentiere Umfang, Ausnahmen, Wiederherstellung und Lizenzabhängigkeiten, statt pauschal „MFA für alle“ aufzuschreiben.

**Szenario:** Eine Gastdozentin greift von einem privaten Gerät auf Kursmaterial zu. **Nachweis:** erwartete Entscheidungen für einen erlaubten Zugriff, ein unzureichendes Anmeldeverfahren und eine Aktion außerhalb ihrer Berechtigung. **Abgabe:** Zugriffsmatrix mit Begründungen. Bleibe hypothetisch, ändere keine Mandantenkontrollen und verwechsle Berichtsbeobachtungen nicht mit durchgesetzten Entscheidungen.

<a id="sc-900-unit-3"></a>

## 3. Privilegien, Berechtigungen und Risiken trennen

Formuliere drei Fragen: Wer darf eine privilegierte Rolle aktivieren, wer soll Projektzugriff behalten und welches Identitätsverhalten muss untersucht werden? Ordne ihnen PIM, Zugriffsüberprüfung und Identitätsrisiko zu. Definiere Rollenbereich und Dauer. Eine kurzlebige breite Rolle ist nicht automatisch minimal.

**Szenario:** Ein ehemaliges Projektmitglied bleibt in einer Gruppe, während ein Administrator vorübergehend Wartungszugriff braucht. **Nachweis:** Vergabepfade, Entscheidung des Ressourcenverantwortlichen, vorgeschlagene Aktivierung und getrennte Aufzeichnungen verdächtigen Verhaltens, falls vorhanden. **Abgabe:** kurzes Runbook mit Genehmigungszuständigkeit und Abschlussnachweisen je Entscheidung. Erstelle in dieser Einheit keine privilegierten Zuweisungen.

<a id="sc-900-unit-4"></a>

## 4. Erkennung und begrenzte Reaktion planen

Wähle eine hypothetische Angriffskette aus E-Mail, Identität und Workload. Liste Ereignisse auf, die die Hypothese stützen oder widerlegen. Erkläre den Nutzen der Defender-XDR-Korrelation und mögliche Sentinel-Konnektoren, Analysen und Reaktionsorchestrierung. Markiere fehlende Daten; ein leeres Ergebnis beweist nicht, dass ein Ereignis nie stattfand.

**Szenario:** Auf eine Phishingnachricht folgen verdächtige Anmeldungen. **Nachweis:** Zeitachse, Quellenabdeckung, zuständige Analyseperson und ein Benachrichtigungsvorschlag vor störenden Aktionen. **Abgabe:** Erkennungs- und Reaktionstabelle mit Fehlalarmüberlegungen und Wiederherstellungsschritten. Keine Telemetrie einlesen, kostenpflichtige Dienste aktivieren oder Konten automatisch sperren.

<a id="sc-900-unit-5"></a>

## 5. Den Lebenszyklus sensibler Daten verfolgen

Verfolge ein synthetisches Dokument von Erstellung über interne Nutzung und Freigabe bis Untersuchung und Löschung. Unterscheide Klassifizierung, konfigurierten Schutz, DLP, Aufbewahrung, Auditnachweise und eDiscovery. Notiere Workload- und Lizenzannahmen je Fähigkeit. Ein Compliancewert ersetzt keine Feststellung der tatsächlichen Organisationspflichten.

**Szenario:** Ein erfundenes Lösungsblatt bleibt bis zur Veröffentlichung privat; relevante Nachrichten werden für eine Untersuchung bewahrt. **Nachweis:** erwartete Verarbeitungsentscheidungen, erforderliche Aktivitäten, Aufbewahrungsannahmen und benannte Zuständigkeit. **Abgabe:** Lebenszyklustabelle, die erklärt, warum eine einzelne Bezeichnung, ein Protokoll oder ein Backup nicht alle Anforderungen erfüllt. Rechtliche Pflichten werden als Vorgaben einer autorisierten verantwortlichen Person behandelt.

[Microsoft-Learn-Leitfaden](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900)
