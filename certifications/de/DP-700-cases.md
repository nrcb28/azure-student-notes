# DP-700 · Zehn Fälle mit begründeten Antworten

[Leitfaden](DP-700.md) · [Arbeitsbuch](DP-700-workbook.md) · [Inhalt](README.md) · [English](../en/DP-700-cases.md)

Eigene Übungen mit Universitätsdaten, keine offiziellen Prüfungsaufgaben. Nenne Entscheidung und Belege vor dem Öffnen der Antwort. Der [Leitfaden](DP-700.md) dokumentiert offiziellen Umfang und Quellenprüfung; diese Fälle beanspruchen weder vollständige Abdeckung noch Fabric-Ausführung.

## 1. Das Team kennt Synapse Spark. Darf es identische Fabric-Standardwerte und Bereitstellungsabläufe voraussetzen?

<details>
<summary>Antwort</summary>

Nein. Vertraute Spark-Konzepte helfen, doch Fabric ist eine SaaS-Plattform mit eigenen Grenzen für Arbeitsbereiche, Kapazität, Elemente, Laufzeit und Lebenszyklus. Inventarisiere Abhängigkeiten, Bibliotheken, Speicherpfade, Identitäten und unterstützte Konfigurationen vor der Notebook-Anpassung. Definiere eine kleine synthetische Einschreibungslast und vergleiche ihre erwartete Ausgabe mit einer späteren kontrollierten Fabric-Ausführung. Prüfe Bereitstellung und Verbindungen getrennt von Transformationssyntax. Ähnlicher Code ist ein nützlicher Ausgangspunkt, belegt aber keine Gleichheit von Rechten, Laufzeitstandards oder Betriebsverantwortung.

</details>

## 2. Ein relationales Berichtsteam und ein Dateiverarbeitungsteam schlagen denselben Speicher vor. Was entscheidet?

<details>
<summary>Antwort</summary>

Vergleiche die tatsächliche Last: Dateiformate, Transformationsmotoren, relationale Schreibanforderungen, SQL-Nutzung, Governance und Verantwortung. Ein Lakehouse ist ein vernünftiger Kandidat für Spark-Aufbereitung von Downloaddateien; ein Warehouse passt möglicherweise zu einem T-SQL-orientierten Analysemodell. Bei begründeten Anforderungen können beide zusammenarbeiten. Definiere Tabellengranularität und akzeptable Aktualität vor dem Leistungsvergleich. Behandle den SQL-Analyseendpunkt eines Lakehouse nicht als allgemeine Warehouse-Schreiboberfläche. Dokumentiere unterstützte Operationen und einen repräsentativen Validierungsplan, statt ausschließlich nach Teamvertrautheit zu wählen.

</details>

## 3. Eine Verknüpfung stellt den Bibliothekskatalog bereit. Liefert sie Sicherung und Zugriff für alle Analysten?

<details>
<summary>Antwort</summary>

Nein. Die Verknüpfung verweist auf Quelldaten; ein fehlendes Ziel oder geänderte Quellrechte können den Zugriff beeinflussen. Sie ist keine unabhängig aufbewahrte Wiederherstellungskopie. Prüfe interne oder externe Art, verwendete Identität beziehungsweise Verbindung und Rechte des tatsächlichen Lesewegs. Teste einen erlaubten und einen gesperrten Analysten mit synthetischen Daten. Vereinbare Schemaänderungen und Verfügbarkeit mit dem Katalogverantwortlichen. Für historische Wiederherstellung ist ein gesonderter Aufbewahrungs- und Wiederherstellungsentwurf erforderlich.

</details>

## 4. Ein Bericht darf nur die Einschreibungen von gestern enthalten. Die Kopieraktivität ist erfolgreich, aber der Bericht enthält heutige Einschreibungen. War der gesamte Ablauf erfolgreich?

<details>
<summary>Antwort</summary>

Die Aktivität endete technisch erfolgreich, die fachliche Abnahmebedingung wurde jedoch verletzt. Prüfe Fensterparameter, dynamische Ausdrücke, Quellfilter, Zeitzonen und Zielbindungen. Gleiche Quellfensterzahlen und ausgewählte Geschäftsschlüssel mit der veröffentlichten Ausgabe ab, bevor Folgeaktualisierungen erlaubt werden. Eine Pipeline soll Validierung und Veröffentlichung koordinieren; Notebook oder SQL können Datenregeln umsetzen. Erfasse Laufkennung und vorgesehenes Intervall zur Rückverfolgung. Korrigiere betroffene Ausgaben durch idempotente Wiederholung, statt einen grünen Status als Korrektheitsbeweis anzusehen.

</details>

## 5. Ein Batch wurde bestätigt, verlor aber die Erfolgsantwort. Wie vermeidet eine Wiederholung doppelte Einschreibungen?

<details>
<summary>Antwort</summary>

Verwende einen stabilen Einschreibungsschlüssel und eine deterministische Quellversion, dedupliziere den Eingangs-Batch und führe ihn zum vorgesehenen Zielzustand zusammen. Speichere Fortschritt erst nach Ausgabevalidierung und erfolgreicher Bestätigung. Die Wiederholung desselben begrenzten Quellintervalls soll bereits angewendete gleichwertige Versionen erkennen und fachliche Summen unverändert lassen. Erfasse Batch-Kennung und Abgleichzahlen für die Diagnose. Einfaches Anhängen ohne Eindeutigkeitsregel würde Zeilen duplizieren. Berücksichtige ältere verspätete Änderungen und Löschungen: Wiederholung muss die Versionsreihenfolge bewahren, nicht nur identische Inhalte erkennen.

</details>

## 6. Eine Änderungsdatumsabfrage übersieht Abmeldungen und verspätete Korrekturen. Wie ändert sich der Ladeentwurf?

<details>
<summary>Antwort</summary>

Kläre, ob Abmeldungen Zeilen physisch löschen oder einen Status ändern. Eine Abfrage verbleibender Zeilen erkennt physische Löschungen nicht. Prüfe unterstützte CDC mit Löschdatensätzen, einen Vertrag für logische Löschung oder regelmäßigen Abgleich. Nutze für verspätete Korrekturen zuverlässige Quellordnung und Überlappung mit deterministischer Deduplizierung oder eine andere unterstützte Änderungserfassung. Bewahre genügend Versionsinformationen, um veraltete Änderungen nach einer Löschung abzulehnen. Teste gleiche Zeitstempel, verspätete Datensätze und Wiederholung. Dokumentiere die Quellaufbewahrung, damit eine längere Unterbrechung keine unbemerkte, unwiederbringliche Lücke erzeugt.

</details>

## 7. Ein Download erfolgt um 23:59 und trifft um 00:07 ein. Welcher Tageswert soll sich ändern?

<details>
<summary>Antwort</summary>

Die erklärte fachliche Zeitregel entscheidet. Zählen Berichte nach Ereigniszeit, gehört der Datensatz zum früheren Tagesfenster. Definiere Zeitzone, Fenstergrenze, erlaubte Verspätung und Korrigierbarkeit veröffentlichter Ergebnisse. Gruppierung nach Verarbeitungszeit würde ihn dem Ankunftstag zuordnen und eine andere Frage beantworten. Ein Streaming-Wasserzeichen steuert verspätete Behandlung und gespeicherten Zustand; ein Prüfpunkt unterstützt die Wiederherstellung des Fortschritts. Beides ersetzt keine ausdrückliche Korrekturregel und beweist nicht, dass das Ziel bei Wiederholung keine doppelten Ausgaben erzeugt.

</details>

## 8. Eine optionale Spalte kommt mit fehlerhaften Datumswerten und unbekannten Modulschlüsseln. Soll Schemaentwicklung alle Zeilen akzeptieren?

<details>
<summary>Antwort</summary>

Bewerte die optionale Spalte als Kompatibilitätsänderung getrennt von der Datensatzgültigkeit. Ein genehmigtes Zusatzfeld macht fehlerhafte Daten oder fehlende Referenzen nicht gültig. Wende ausdrückliche Typ- und Schlüsselregeln an, bewahre ungültige Eingaben kontrolliert mit Ursachencodes auf und gleiche akzeptierte und abgelehnte Datensätze ab. Ein unbekanntes Modul kann spätere Referenzauflösung statt endgültiger Ablehnung erfordern. Erhalte Quellkennungen für sichere Reparatur und Wiederholung. Prüfe nachgelagerte Verträge vor Veröffentlichung des neuen Schemas und vermeide Studierendendetails in frei zugänglichen Diagnoseprotokollen.

</details>

## 9. Ein Bericht erzwingt Zeilensicherheit und hat eine Vertraulichkeitsbezeichnung. Ist direkter Dateizugriff automatisch sicher?

<details>
<summary>Antwort</summary>

Nein. Ermittle die durchsetzende Grenze der Zeilenregel und untersuche Alternativen wie SQL-Abfragen und direkten OneLake-Zugriff. Arbeitsbereichsrollen, Elementrechte, motorspezifische Regeln und Dateirechte müssen zur benötigten Leserfähigkeit passen. Eine Vertraulichkeitsbezeichnung vermittelt Governance-Kontext und unterstütztes Schutzverhalten; ihre Existenz beweist allein nicht jede Autorisierungsanforderung. Teste erlaubte Modulaggregate und verweigerte Studierendendetails mit repräsentativen Identitäten. Prüfe außerdem Exportrechte und geerbte breite Zugriffe, die eine sorgfältig eingeschränkte Berichtsoberfläche unterlaufen können.

</details>

## 10. Ein bereitgestelltes Notebook ist langsamer und liest im Test Produktion. Zuerst Kapazität erhöhen?

<details>
<summary>Antwort</summary>

Korrigiere zuerst die Umgebungsbindung und verhindere unbeabsichtigte Veröffentlichung. Prüfe Verbindungsreferenzen, Parameter, Ausführungsidentität sowie Bereitstellungsunterstützung für Element und Abhängigkeiten. Git-Verlauf oder erfolgreiche Übernahme beweisen keine korrekten Werte. Vergleiche dann dieselbe Last mit einer Basislinie: Kapazitätskonkurrenz, Spark-Schieflage, Shuffle, Dateigrößen, Partitionsausschluss und Quellverhalten. Teste eine belegte Änderung mit Korrektheitsprüfungen. Erhöhe Kapazität, wenn gemessener Druck dafür spricht, statt Konfigurationsfehler oder ineffiziente Datenanordnung durch Skalierung zu verdecken.

</details>
