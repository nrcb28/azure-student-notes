# SC-200 · 10 Fälle mit begründeten Antworten

[Leitfaden](SC-200.md) · [Arbeitsbuch](SC-200-workbook.md) · [Inhalt](README.md)

Eigene Lernszenarien, keine offiziellen Prüfungsfragen. Verwenden Sie die fiktive universitäre Notizen-App und synthetische Datensätze. Nennen Sie die Anforderung, verwerfen Sie eine verlockende Alternative und benennen Sie fehlende Belege. Dies sind Offline-Planspiele; es werden weder Mandantenabfragen noch Nachrichten oder Reaktionsaktionen ausgeführt.

## 1. Microsoft-365-Warnungen erscheinen in Defender XDR, aber die Campus-Firewall fehlt. Deckt XDR sie bereits ab?

<details>
<summary>Antwort</summary>

Nein. Vorhandene Microsoft-365-Belege stellen keine Firewall-Abdeckung fest. Inventarisieren Sie den unterstützten Exportpfad der Firewall und die benötigte Analyse und bewerten Sie anschließend einen passenden Sentinel-Connector mit seinen Voraussetzungen. Defender-XDR-Korrelation und Sentinel-Erfassung dienen verwandten Zwecken, aber keines erfindet fehlende Telemetrie. Ich würde die erwartete Tabelle, das Schema, Quellenkennungen, Erfassungsumfang und beispielhafte Ankunftszeiten anfordern. Das Planspiel-Ergebnis ist eine Abdeckungskarte mit vorhandenen und fehlenden Quellen, die erwartete Erfassung von tatsächlich bereitgestellten Beobachtungen unterscheidet.

</details>

## 2. Ein Connector meldet Connected, doch eine Abfrage liefert keine Gerätezeilen. Sollte der Analyst die Untersuchung schließen?

<details>
<summary>Antwort</summary>

Nein. Prüfen Sie Geräte-Onboarding, Lizenz- und Dienstanforderungen, ausgewählte Ereignistypen des Connectors, Zieltabelle, Analystenberechtigungen, UTC-Fenster, Erfassungsverzögerung und Aufbewahrung. Eine Tabelle kann andere Felder als das von der Abfrage angenommene Schema verwenden. Connected ist ein Konfigurationssignal und kein Beweis, dass jedes erforderliche Ereignis ankam. Ein Schließen des Falls würde fehlende Sichtbarkeit mit harmlosem Verhalten verwechseln. Dokumentieren Sie fehlende Belege und bitten Sie den Quellenverantwortlichen um eine begrenzte synthetische Ereignisstichprobe sowie Belege zum Erfassungszustand, bevor Sie eine Schlussfolgerung ziehen.

</details>

## 3. Drei Warnungen teilen eine Campus-IP-Adresse. Reicht das, um sie zu einem bestätigten Angriff zusammenzuführen?

<details>
<summary>Antwort</summary>

Eine gemeinsame IP ist ein Ansatzpunkt, besonders hinter der Netzwerkadressübersetzung des Campus, identifiziert aber keine einzelne Person oder einen Angreifer. Vergleichen Sie stabile Konto- und Gerätekennungen, Nachrichten- oder Dateibelege, Aktivitätstypen und UTC-Zeiten. Warnungen sind Erkennungen; ein Vorfall gruppiert zusammengehörige Belege, und eine Entität ist ein beteiligtes Objekt. Ich würde eine Korrelation nur mit stützenden Beziehungen vorschlagen und Unsicherheit dokumentieren. Benötigt werden eine Zeitleiste und eine Entitätskarte, die auch nicht zusammenhängende Studierende mit derselben öffentlichen Adresse berücksichtigen.

</details>

## 4. Eine Endpunktwarnung betrifft den Server für Vorlesungsübertragungen. Darf der studentische Analyst ihn sofort isolieren?

<details>
<summary>Antwort</summary>

Die Warnung allein verleiht keine Eindämmungsbefugnis. Bewahren Sie Belege auf, bewerten Sie aktuelle Aktivität und wahrscheinlichen Umfang und konsultieren Sie das Vorfallhandbuch sowie den autorisierten Entscheider. Isolation könnte die Lehre unterbrechen; dokumentieren Sie daher Serviceauswirkungen, vorgeschlagene Grenze, Alternativen und Wiederherstellungsbedingungen. Warten ohne Eskalation ist ebenfalls unzureichend, wenn Belege eine laufende Bedrohung nahelegen. Dokumentieren Sie in diesem Planspiel die Eskalation und die vorgeschlagene Aktion; führen Sie sie nicht aus. Der Abschluss würde einen genehmigten Aktionsnachweis und getrennte Belege zur Bestätigung des beabsichtigten Ergebnisses erfordern.

</details>

## 5. Die synthetische Abfrage des Leitfadens enthält drei Denied-Zeilen. Warum ist der erwartete Zählwert zwei?

<details>
<summary>Antwort</summary>

Der Datensatz wiederholt dasselbe Paar aus `EventId` und Konto für `e1`. Nach dem UTC-Zeitfilter behält `distinct EventId, Account` eine Kopie dieses Paars plus `e2`, sodass die Aggregation zwei Ereignisse für `student-a` erwartet. Diese Schlussfolgerung hängt von der genannten Annahme stabiler Kennungen ab. Eine Deduplizierung nur nach Konto würde separate Ereignisse zusammenfassen und zu wenig zählen. Das Allowed-Ereignis liegt außerdem an der ausgeschlossenen oberen Zeitgrenze. Dies ist ein durch Lesen synthetischer Zeilen vorhergesagtes Ergebnis, kein Beleg für eine im Mandanten ausgeführte Abfrage.

</details>

## 6. Eine Verknüpfung von Nachrichten und Anmeldedaten nach Konto verdoppelt die Ergebniszahl. Fanden doppelt so viele Angriffe statt?

<details>
<summary>Antwort</summary>

Nicht unbedingt. Mehrere Nachrichten und mehrere Anmeldungen für ein Konto können mehrere passende Paare erzeugen. Nennen Sie Join-Art, Schlüsseleindeutigkeit und die Beziehung, die die Analyse feststellen soll. Das standardmäßige `innerunique` verändert zudem die linke Eingabe durch Deduplizierung der Join-Schlüssel und kann Unterscheidungen entfernen, die der Analyst benötigt. Prüfen Sie die Kardinalität jeder Eingabe und ergänzen Sie eine passende Zeitbeziehung, bevor Sie die Ausgabe interpretieren. Ich würde Quellenereignis-IDs bewahren und erwartete Paarungen an einem winzigen synthetischen Datensatz vergleichen, statt verknüpfte Zeilen mit Angriffen gleichzusetzen.

</details>

## 7. Eine Suche findet nach einer verdächtigen E-Mail keinen privaten Dateizugriff. Darf der Bericht sagen, dass das Konto nie kompromittiert wurde?

<details>
<summary>Antwort</summary>

Diese Behauptung geht über die Belege hinaus. Berichten Sie, dass die definierte Abfrage für ihre Population und ihr UTC-Intervall keine passenden verfügbaren Datensätze fand. Prüfen Sie, ob Anwendungsauditing aktiviert war, relevante Geräte eingebunden waren, Datensätze noch aufbewahrt werden und der Analyst sie lesen kann. Prüfen Sie auch Filter und die Bedeutung von Zugriffsereignissen. Ein genehmigter Gerätewechsel ist eine konkurrierende Erklärung für Aktivität von einem unbekannten Gerät. Bewahren Sie Hypothese, Abfrageversion, Abdeckungslücken und eine Folgefrage auf, statt fehlende Treffer als Sicherheitsbeweis zu behandeln.

</details>

## 8. Ein Massenimport von Kursen erzeugt wiederholte Warnungen. Sollten alle Lehrendenkonten von der Regel ausgeschlossen werden?

<details>
<summary>Antwort</summary>

Ein breiter Rollenausschluss könnte Aktivität kompromittierter Lehrendenkonten verbergen. Identifizieren Sie zuerst das konkrete autorisierte Importkonto, den Workload, das Zeitmuster und Auditbelege. Vergleichen Sie gekennzeichnete synthetische Importereignisse mit bedenklichen Zugriffen auf unveröffentlichte Lösungen. Schlagen Sie eine eng begrenzte Ausnahme oder Regelanpassung vor und bewerten Sie sowohl falsch positive als auch falsch negative Ergebnisse. Prüfen Sie außerdem Zeitplanüberlappung, Rückblickzeitraum, Gruppierung und Unterdrückung, bevor Sie den Schwellenwert verantwortlich machen. Bewahren Sie erwartete Ergebnisse und Regelversion im Abstimmungsprotokoll auf; weniger Warnungen allein beweisen keine bessere Erkennungsqualität.

</details>

## 9. Ein Playbook-Wiederholungsversuch würde ein weiteres Ticket öffnen und dasselbe Konto erneut beschränken. Was fehlt?

<details>
<summary>Antwort</summary>

Der Entwurf benötigt Idempotenz und ein klares Aktionszustandsmodell. Verknüpfen Sie den Workflow mit stabilen Vorfall- und Aktionskennungen, prüfen Sie, ob der vorgesehene Schritt bereits abgeschlossen ist, und behandeln Sie Teilausfälle, ohne ihn blind zu wiederholen. Prüfen Sie getrennt Operatorrollen, Sentinels Berechtigung zum Playbook-Aufruf und den nachgelagerten Umfang der Workflow-Identität. Störende Einschränkungen benötigen die Genehmigung und den Wiederherstellungspfad des Handbuchs. Simulieren Sie in dieser Offline-Prüfung einen doppelten Auslöser und eine Zeitüberschreitung auf Papier; stellen Sie das Playbook weder bereit noch führen Sie es aus.

</details>

## 10. Copilot sagt, eine Cloud-Workload-Warnung beweise, dass student-a Lösungen heruntergeladen hat. Reicht seine Zusammenfassung als Beleg?

<details>
<summary>Antwort</summary>

Nein. Verfolgen Sie die Behauptung zu Anwendungszugriffsdatensätzen, Cloud-Ressourcen-ID, Identitätskennungen und UTC-Zeitleiste zurück. Eine Workload-Warnung oder Haltungsempfehlung beweist für sich genommen keinen bestimmten Dokumentdownload. Prüfen Sie Copilots zitierte Quellen, verfügbare Integrationen sowie Schema, Filter, Joins und Zählwerte jeder generierten Abfrage. Markieren Sie unbelegte Aussagen und bewahren Sie die korrigierte Schlussfolgerung des Analysten auf. Das Fallprotokoll sollte beobachtete synthetische Belege, eine abgeleitete Beziehung und fehlende Datensätze unterscheiden. Eine flüssige Zusammenfassung kann weder fehlende Telemetrie liefern noch eine Reaktion autorisieren.

</details>

[Offizieller Studienleitfaden](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · [Technische Quellen und Erklärungen](SC-200.md)
