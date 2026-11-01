# DP-300 · 10 Fälle mit begründeten Antworten

[Leitfaden](DP-300.md) · [Arbeitsbuch](DP-300-workbook.md) · [Inhalt](README.md)

Eigene Übungen, keine offiziellen Prüfungsaufgaben. Benenne vor dem Aufklappen Einschränkung, Entscheidung und benötigte Nachweise. Die Fälle behaupten weder Azure-Ausführung noch vollständige Prüfungsabdeckung.

## 1. Eine Anwendung braucht eine unterstützte Betriebssystemerweiterung. Genügt T-SQL-Kompatibilität für die Wahl von SQL Database?

<details>
<summary>Begründung</summary>

Nein. Die Betriebssystemanforderung verändert die Hostinggrenze. Prüfe, ob die Erweiterung notwendig ist und eine unterstützte Alternative im verwalteten Dienst existiert. Bleibt direkter Betriebssystemzugriff erforderlich, bewerte SQL Server auf einer VM einschließlich Patching, Backup, Überwachung und Verfügbarkeitszuständigkeiten. Eine Kompatibilitätsbewertung muss neben T-SQL auch Abhängigkeiten außerhalb der Datenbankobjekte erfassen. Bestätige den tatsächlichen Anwendungsbedarf vor der Plattformwahl. Vertraute SQL-Syntax belegt keine Deploymentkompatibilität.

</details>

## 2. Die Datenmigration ist erfolgreich abgeschlossen. Können Schreibzugriffe sofort wieder geöffnet werden?

<details>
<summary>Begründung</summary>

Die Übertragung ist nur ein Kontrollpunkt. Prüfe endgültigen Datenzustand, wichtige fachliche Summen, Rechte, Anwendungspfade und geplante Aufgaben. Kläre den Zeitpunkt des Schreibstopps an der Quelle und die Übernahme verbleibender Änderungen. Erkläre das Ziel zur maßgeblichen Instanz, bevor Verkehr freigegeben wird. Ein Rücknahmeplan muss danach entstandene Zielschreibvorgänge behandeln; eine Rückverbindung zur Quelle könnte sie verwerfen. Nutze eine ausdrückliche Freigabe-/Abbruchliste und dokumentiere Beobachtungen statt Annahmen.

</details>

## 3. Die App löst die private SQL-Adresse auf und verbindet sich, SELECT wird aber verweigert. Muss das Netzwerk weiter geöffnet werden?

<details>
<summary>Begründung</summary>

Erfolgreiche Verbindung mit verweigerter Anweisung deutet auf Datenbankautorisierung statt allgemeinen Netzwerkausfall. Bestätige authentifizierten Prinzipal, Datenbank, Objekt und Operation. Prüfe die geltenden Datenbankrechte und gewähre im gewählten Zugriffsmodell die kleinste erforderliche Fähigkeit. Azure Contributor liefert nicht automatisch Tabellenzugriff. Öffentlicher Zugriff würde die Angriffsfläche verändern, ohne das fehlende Recht zu geben. Wiederhole zur Bestätigung dieselbe Anwendungsoperation mit derselben Identität.

</details>

## 4. Datenbankadministratoren dürfen bestimmte Klartextwerte nicht sehen. Reicht TDE allein?

<details>
<summary>Begründung</summary>

TDE schützt Datenbankdateien im Ruhezustand, verhindert aber allein keine Klartextrückgabe durch eine berechtigte Abfrage. Prüfe etwa Always Encrypted mit unterstützten Clients und Schlüsseln außerhalb der Zugriffsgrenze der Datenbankadministration. Betrachte erforderliche Abfrageoperationen, Anwendungskompatibilität, Schlüsselwiederherstellung und Betriebszuständigkeit. Dynamische Maskierung ist keine gleichwertige Vertraulichkeitsgrenze. Validiere das Bedrohungsmodell in einem genehmigten Test mit synthetischen Daten, statt alle Funktionen mit „Verschlüsselung“ im Namen gleichzusetzen.

</details>

## 5. Nach einem Release wird eine Abfrage langsamer, obwohl die Gesamt-CPU normal ist. Welche Nachweise helfen zuerst?

<details>
<summary>Begründung</summary>

Identifiziere die Abfrage und vergleiche ihre Pläne sowie Laufzeiteigenschaften in passenden Zeiträumen mit vorhandener Query-Store-Historie. Prüfe Anwendungsparameter, Lesezugriffe, Wartezeiten, Blockierungen und jüngste Schema- oder Statistikänderungen. Normale Gesamt-CPU beweist keine gesunde einzelne Transaktion. Formuliere eine konkrete Hypothese vor einer Größenänderung. Beim Test eines früheren Plans definiere Erfolgskriterien und Rücknahme und überwache repräsentativen Verkehr. Eine einzige schnelle Ausführung belegt keine dauerhafte Verbesserung.

</details>

## 6. Ein neuer Index beschleunigt Lesen, Importe werden aber erheblich langsamer. Ist er zwingend ein Erfolg?

<details>
<summary>Begründung</summary>

Nein. Bei Datenänderungen muss auch der Index gepflegt werden. Sein Nutzen muss deshalb am gesamten Workload gemessen werden. Vergleiche repräsentative Lese- und Schreiblatenz, Durchsatz, Speicher und Ausführungspläne vor und nach der Änderung. Prüfe Überschneidungen vorhandener Indizes und eine mögliche schmalere oder anders sortierte Definition. Definiere Akzeptanzgrenzen für Importe und Suchzugriffe. Behalte eine Änderung nicht allein, weil die Vorführabfrage schneller wurde.

</details>

## 7. Eine lange Transaktion blockiert kurze Abfragen. Soll jede blockierte Sitzung beendet werden?

<details>
<summary>Begründung</summary>

Finde zuerst Blockierungskette und die Transaktion mit den relevanten Sperren. Eine blockierte Sitzung ist oft Symptom, nicht Ursache. Ermittle Arbeit, Transaktionsalter, Eigentümer und Folgen einer Rücknahme. Das Beenden kann lange Rollbackzeiten verursachen und Anwendungskorrektheit beeinflussen. Prüfe in einer kontrollierten Untersuchung nach Verständnis der Konsistenzanforderungen kürzere Transaktionen oder eine passende Isolationsstrategie. Dokumentiere Nachweise und Incidententscheidung, statt ein pauschales Beendigungsskript auszuführen.

</details>

## 8. Ein SQL-Agent-Job soll nach Azure SQL Database umziehen. Kann nur sein Zeitplan kopiert werden?

<details>
<summary>Begründung</summary>

SQL Agent ist in Azure SQL Database nicht verfügbar. Klassifiziere die Aufgabe: Unterstützte T-SQL-Arbeit über mehrere Datenbanken könnte zu Elastic Jobs passen, ein Ablauf mit externen Diensten zu einer Orchestrierung. Prüfe Abhängigkeiten, Identität, Zielermittlung, Wiederholungen und Benachrichtigungen statt nur einen Zeitwert zu kopieren. Nach ungewisser Antwort darf eine Wiederholung keine fachlichen Duplikate erzeugen. Teste den Ersatz mit isolierten synthetischen Daten und vergleiche Ausführungsaufzeichnung sowie fachlichen Ergebniszustand.

</details>

## 9. Ein versehentliches DELETE erreicht die sekundäre Datenbank. Hat die Replikation versagt?

<details>
<summary>Begründung</summary>

Die Replikation kann genau wie konfiguriert arbeiten und eine gültig bestätigte Änderung übertragen. Verfügbarkeit und historische Wiederherstellung lösen andere Probleme. Ermittle Vorfallszeit und aufbewahrte Wiederherstellungspunkte; plane eine isolierte Wiederherstellung vor der unerwünschten Änderung. Prüfe fehlende und spätere legitime Datensätze, bevor der Dienst wiederhergestellt wird. Ein pauschaler Ersatz durch einen alten Zustand ist nicht automatisch akzeptabel. Berücksichtige gültige Schreibvorgänge seit dem Vorfall.

</details>

## 10. Die Datenbank ist umgeschaltet, die App funktioniert weiterhin nicht. Ist das RTO-Ziel erreicht?

<details>
<summary>Begründung</summary>

Nicht, wenn das Ziel den für Nutzer sichtbaren Dienst betrifft. Prüfe unterstützten Anwendungsendpunkt, Client-DNS, Wiederverbindung, Identitäten, Abhängigkeiten und geplante Operationen auf dem aktuellen Primärsystem. Führe eine Funktionsprüfung mit synthetischen Datensätzen durch und miss die Wiederherstellungszeit ab dem definierten Startvorfall. Erfasse Datenverlust getrennt zum RPO. Bestimme vor Failback maßgebliche Kopie und Synchronisationsplan. Ein gesunder Datenbankstatus beweist weder die funktionsfähige App noch erreichte Wiederherstellungsziele.

</details>

## Selbstbewertung und Quellen

Benenne je Fall die Anforderung, begründe eine Entscheidung und nenne einen Prüfschritt. Eine unabhängige Wiederholungsmethode, keine offizielle Prüfungsnote oder Bestehensprognose.

[Offizieller Leitfaden](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300) · [Technische Referenzen und Erklärungen](DP-300.md)
