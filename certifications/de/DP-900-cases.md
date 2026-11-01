# DP-900 · 10 Fälle mit begründeten Antworten

[Leitfaden](DP-900.md) · [Arbeitsbuch](DP-900-workbook.md) · [Inhalt](README.md)

Eigene Übungsszenarien, keine echten Prüfungsfragen. Nenne zuerst die Anforderung, verwirf dann eine Alternative und beschreibe die benötigten Nachweise. Eine Cloudbereitstellung wird nicht behauptet.

## 1. Die App speichert PDFs und durchsuchbare Eigentümermetadaten. Muss beides in dieselbe SQL-Tabelle?

<details>
<summary>Begründung</summary>

Nein. Ein möglicher Entwurf hält PDF-Objekte in Blob Storage und Eigentümer- sowie Kursbeziehungen in einer Datenbank. Entscheidend ist die Zugriffs- und Konsistenzgrenze: Ein Upload kann funktionieren, während die Metadatenänderung scheitert. Definiere einen wiederaufnehmbaren Ablauf und die Erkennung verwaister Dateien. Eine gemeinsame Datenbankdarstellung kann bei passenden Anforderungen ebenfalls sinnvoll sein. Die Annahme „Alles muss eine SQL-Zeile sein“ hilft bei der Auswahl jedoch nicht weiter.

</details>

## 2. Eine JSON-Datei hat optionale verschachtelte Attribute. Ist sie wegen fehlender Felder unstrukturiert?

<details>
<summary>Begründung</summary>

JSON kann semistrukturierte Daten darstellen: Schlüssel und Verschachtelung organisieren den Inhalt auch bei unterschiedlichen Datensätzen. Fehlende Felder heben diese Struktur nicht auf. Trenne Darstellung, Qualität und Speicherwahl. Kläre, ob ein fehlendes Feld zulässig, unbekannt oder ein Einlesefehler ist, und wie Verbraucher reagieren sollen. Eine Dokumentdatenbank kann zum Zugriffsmuster passen. Allein die Verwendung von JSON entscheidet diese Architekturfrage aber nicht.

</details>

## 3. Jede Einschreibung wiederholt Kurstitel und Lehrperson. Welchen Fehler könnte Normalisierung verhindern?

<details>
<summary>Begründung</summary>

Eine Titeländerung könnte einige Einschreibungen aktualisieren und andere beim alten Wert belassen. Ein Courses-Datensatz mit stabilem Schlüssel, auf den Enrolments verweist, reduziert diese Änderungsanomalie. Erkläre die notwendigen Bedingungen und wie Joins das Ergebnis zusammensetzen. Duplikation ist dadurch nicht überall verboten: Ein analytischer Snapshot kann historische Beschreibungen bewusst erhalten. Halte fest, ob es um den aktuellen transaktionalen Zustand oder um ein historisches Berichtsmodell geht.

</details>

## 4. Eine Berichtsabfrage bremst die Einschreibung. Verschwindet die Datenbanklast automatisch mit einem Power-BI-Diagramm?

<details>
<summary>Begründung</summary>

Nein. Der Effekt hängt von Datenzugriff und Aktualisierung des Modells ab. Der Bericht kann weiterhin die operative Quelle abfragen oder teure Aktualisierungen verursachen. Kläre Aktualität, Abfragemuster und Kapazität der Quelle. Eine aufbereitete analytische Kopie kann Arbeit verlagern, bringt aber Verzögerung und Pipelineverantwortung mit. Miss die Quelllast und definiere „aktuell“, statt einem anderen Visualisierungswerkzeug automatisch einen anderen Datenzugriff zuzuschreiben.

</details>

## 5. Eine bestehende SQL-Server-App braucht Betriebssystemkomponenten. Ist Azure SQL Database immer direkt austauschbar?

<details>
<summary>Begründung</summary>

Nein. Erfasse diese Komponenten und weitere Abhängigkeiten vor der Zielwahl. Azure SQL Database, Managed Instance und SQL Server auf Azure-VMs besitzen unterschiedliche Verwaltungs- und Kompatibilitätsgrenzen. Eine VM erlaubt Betriebssystemzugriff, erfordert aber mehr Wartung durch das Team. Managed Instance kann manche Instanzanforderungen erfüllen, ohne jede externe Abhängigkeit abzudecken. Erstelle eine Kompatibilitätsliste und einen Migrationstestplan. Eine vertraute Datenbankengine beweist nicht, dass die gesamte Anwendung unverändert läuft.

</details>

## 6. Jemand erwartet wegen des Namens Table Storage Fremdschlüssel. Wie würdest du den Entwurf korrigieren?

<details>
<summary>Begründung</summary>

Table Storage ist ein nichtrelationaler Entitätsspeicher, kein verwalteter relationaler SQL-Dienst. Leite aus dem Namen keine relationalen Joins oder Fremdschlüsselprüfungen ab. Erfasse tatsächliche Lesezugriffe, Änderungen, Beziehungen und Konsistenzanforderungen und vergleiche ein geeignetes Entitätsmodell mit einem relationalen Entwurf. Ein durchgespieltes Beispiel ist der nützliche Nachweis: Wie findet eine Einschreibung ihren Kurs, und wie werden ungültige Verweise verhindert oder erkannt? Produktnamen ersetzen keine Prüfung der Fähigkeiten.

</details>

## 7. Die nächtliche Verarbeitung liefert den Bericht rechtzeitig am Morgen. Sollte sie allein aus Modernitätsgründen durch Streaming ersetzt werden?

<details>
<summary>Begründung</summary>

Beginne mit der fachlich zulässigen Verzögerung. Liefert ein zuverlässiger Nachtlauf rechtzeitig das benötigte Ergebnis, kann Streaming zusätzlichen Betriebsaufwand ohne besseren Nutzen erzeugen. Müssen Mitarbeitende innerhalb weniger Minuten auf Überlast reagieren, untersuche dafür einen schnelleren Pfad. In beiden Varianten sind Duplikate, unvollständige Eingaben und Wiederholungen zu behandeln. Vergleiche die Aktualität und Fehlerbehebung über den gesamten Ablauf, nicht nur die Ausführungsfrequenz einer Komponente.

</details>

## 8. Rohdaten werden in ein Warehouse geladen und dort bereinigt. Ist das ETL und entfällt dadurch die Validierung?

<details>
<summary>Begründung</summary>

Die Reihenfolge beschreibt ELT: zuerst laden, dann mit den Möglichkeiten des Ziels transformieren. Bei ETL erfolgt die Transformation vor dem Laden in das vorgesehene Ziel. Beide brauchen Datenvereinbarungen und Prüfungen. Definiere den Ablageort ungültiger Datensätze, die Wiederholbarkeit der Transformationen und die Abstimmung akzeptierter Mengen mit der Quelle. Beschränke auch den Zugriff auf geschützte Rohdaten, wenn Analysten nur das bereinigte Modell sehen. Ein bequemer Abfragezugang beweist weder sichere noch richtige Ausgangsdaten.

</details>

## 9. Ein Dashboard zählt Downloadereignisse. Wiederholungen erzeugen doppelte Ereignis-IDs. Ist COUNT(*) zwingend die Zahl abgeschlossener Downloads?

<details>
<summary>Begründung</summary>

Nur wenn jede gezählte Zeile laut Datendefinition genau einen abgeschlossenen Download darstellt. Doppelte Zustellung kann COUNT(*) erhöhen. Definiere Geschäftsereignis, stabile Kennung, Abschlussbedingung und Berichtsintervall. Entferne oder aggregiere Duplikate entsprechend dieser Definition. Halte eine Zahl abgewiesener oder doppelter Datensätze fest, damit die Änderung nachvollziehbar bleibt. Prüfe mit einer kleinen Datenmenge aus einer wiederholten ID und einem unvollständigen Download. Ein plausibles Diagramm beweist nicht die passende Kennzahl.

</details>

## 10. Sechs Kursdatensätze passen in ein Dokumentmodell. Beweist das, dass nur Cosmos DB sinnvoll ist?

<details>
<summary>Begründung</summary>

Nein. Viele Dienste können sechs Datensätze speichern; das Beispiel zeigt nur die Darstellbarkeit. Vergleiche erwartete Abfragen, Beziehungen, Aktualisierungen, Konsistenz, Betriebsanforderungen und Teamkenntnisse. Eine relationale Datenbank kann bei vielen Bedingungen und verknüpften Entitäten einfacher sein, ein Dokumentmodell bei anderen Zugriffsmustern. Dokumentiere einen Grund für deine Wahl und eine Bedingung, unter der du sie ändern würdest. Grundlagenlernen sollte diese Begründung fördern, statt jedem JSON-Beispiel automatisch ein bestimmtes Produkt zuzuordnen.

</details>

Quellen: [offizielle Ziele](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900), [Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview), [Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction), [ETL/ELT](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl), [Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview).
