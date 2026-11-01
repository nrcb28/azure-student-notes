# DP-900 · Gemeinsames vertiefendes Arbeitsbuch

[Leitfaden](DP-900.md) · [Zehn Fälle](DP-900-cases.md) · [Inhalt](README.md)

Fünf entsprechende Einheiten in acht Sprachen. Verwende synthetische Daten und dokumentiere Vorhersagen getrennt von Beobachtungen. Die Übungen stellen nichts in Azure bereit und belegen keine vollständige Prüfungsabdeckung.

<a id="dp-900-unit-1"></a>

## 1. Daten vor der Speicherwahl beschreiben

Erfasse eine PDF-Datei, eine Einschreibungszeile, ein JSON-Dokument mit optionalen Metadaten und ein Downloadereignis. Beschreibe Struktur, Kennung, Erzeuger, Verbraucher, Aufbewahrung und sensible Felder. Schreibe dann die wichtige Operation auf: eine Datei abrufen, eine Einschreibung erfassen oder Ereignisse zusammenfassen. Trenne eine Formatwahl von einer Workloadanforderung.

**Szenario:** Alle vier Datenmengen sollen wegen derselben App in eine einzige Datenbank. **Nachweis:** eine Entscheidungsmatrix mit vier Zeilen, je einer verworfenen Alternative und einer neuen Anforderung, die die Wahl ändern könnte. Erfinde keine Dienstgrenzen und unterstelle nicht, dass jedes JSON-Dokument Cosmos DB benötigt.

<a id="dp-900-unit-2"></a>

## 2. Relationale Integrität sichtbar machen

Zeichne Students, Courses und Enrolments mit stabilen Kennungen. Erzeuge sechs synthetische Zeilen und erläutere Primärschlüssel, Verweise und eine Regel gegen doppelte Einschreibungen. Sage ein Join-Ergebnis voraus. Ändere anschließend einen Kurstitel und vergleiche die erforderlichen Änderungen mit einem Entwurf, der den Titel in jede Einschreibung kopiert. Ziel ist eine konkrete Änderungsanomalie statt eines auswendig gelernten Normalisierungssatzes.

**Szenario:** Eine Einschreibung verweist auf einen nicht existierenden Kurs. **Nachweis:** die ablehnende oder erkennende Regel, ein ungültiger Beispieldatensatz und das erwartete Ergebnis. Nenne bei einer lokalen SQL-Ausführung die Engine; SQLite-Verhalten prüft nicht Azure SQL.

<a id="dp-900-unit-3"></a>

## 3. Entscheiden, wer die Datenbank betreibt

Vergleiche Azure SQL Database, Managed Instance und SQL Server auf einer VM für eine neue App und eine Migration. Erfasse Kompatibilitätsabhängigkeiten, Netzwerk und Identität, Wartungszuständigkeiten und Wiederherstellungserwartungen. Ergänze eine Open-Source-Engine, wenn die bestehende Anwendung sie benötigt. Unterscheide eine begründete Empfehlung von der Behauptung, ein Produkt sei immer überlegen.

**Szenario:** Das Migrationsinventar enthält eine Komponente mit erforderlichem Gastbetriebssystemzugriff. **Nachweis:** Kompatibilitätsfragen, eine Betriebszuständigkeitstabelle und ein Machbarkeitsplan mit Erfolgskriterien. Ein Deployment ist nicht nötig. Benenne die Annahmen, die vor der endgültigen Zielannahme geprüft werden müssen.

<a id="dp-900-unit-4"></a>

## 4. Eine kleine Datenpipeline abstimmen

Erzeuge sechs synthetische Downloadereignisse mit einer doppelten Kennung und einem Datensatz ohne Kurs. Definiere gültige Eingaben, ein eindeutiges Ereignis und die Abschlussbedingung. Zeichne einen ETL- und einen ELT-Pfad und markiere jeweils Validierung sowie Ablage abgewiesener Datensätze. Erkläre, wann Stapelverarbeitung die Zeitvorgabe erfüllt und wann Streaming begründet wäre.

**Szenario:** Die Dashboard-Summe unterscheidet sich von der Quellzeilenzahl. **Nachweis:** Zahlen für Quelle, Duplikate, abgelehnte und angenommene Ereignisse mit reproduzierbarer Erklärung. Benenne Zuständigkeit und Reaktion bei einem fehlerhaften Lauf. Ein erfolgreicher Pipelinestatus beweist keine fachlich korrekten Summen.

<a id="dp-900-unit-5"></a>

## 5. Eine verlässliche analytische Kennzahl definieren

Wähle eine Berichtskörnung, etwa ein abgeschlossenes Downloadereignis, und definiere einen Fakt mit Kurs- und Datumskontext. Lege Zeitzone, Behandlung später Ereignisse und Aktualität fest. Erkläre, welche Komponente Daten speichert, transformiert, ein semantisches Modell bereitstellt und den Bericht anzeigt. Vergleiche Lake, Warehouse und Lakehouse nach der erforderlichen Arbeit statt nach Produktnamen.

**Abschlussnachweise:** Speichermatrix, relationale Skizze, Pipelineabstimmung und ein monatlicher Musterbericht mit Kennzahldefinition. Erläutere die Rollen von Fabric, Synapse und Power BI. Benenne eine offene Frage für den offiziellen Leitfaden. Ein guter Musterbericht belegt weder Cloudbetrieb noch Prüfungsreife.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900) · [Datennotizen](../../de/04-storage.md)
