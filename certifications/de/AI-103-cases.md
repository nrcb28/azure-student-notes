# AI-103 · Zehn Entwicklungsfälle mit begründeten Antworten

[Leitfaden](AI-103.md) · [Arbeitsbuch](AI-103-workbook.md) · [Inhalt](README.md)

Eigene Szenarien zur universitären Notizen-App, keine Prüfungsfragen. Alle vorgeschlagenen Ausgaben und Zeiten sind hypothetisch. Erkläre vor dem Öffnen jeder Antwort die Umsetzungsentscheidung und benötigten Belege. Quellenprüfung: **1. November 2026**.

## 1. Ein Python-Beispiel lässt sich importieren, aber der Antwort fehlt die erwartete Eigenschaft. Sollte das Team die Bereitstellung ändern, bis es funktioniert?

<details>
<summary>Antwort</summary>

Prüfe zuerst installierte SDK-Version, API-Generation, Operation, Endpunkt und dokumentierte Antwortstruktur. Ein erfolgreicher Import sagt wenig über die Kompatibilität mit einem kopierten Beispiel aus. Fixiere zusammenpassende Abhängigkeiten und überführe eine bereinigte Beispielantwort in den eigenen Anwendungsvertrag. Unterscheide eine fehlende Eigenschaft von Authentifizierungsfehlern oder unbekannten Bereitstellungen. Ein anderes Modell repariert keinen Client, der das falsche Objekt liest. Dokumentiere die URL der Anleitung und Paketversionen; prüfe einen echten Aufruf erst in einem gesondert genehmigten Labor.

</details>

## 2. Ein größeres Modell verbessert Zusammenfassungen, verdoppelt aber die hypothetische Latenz in der Lernwoche. Welches Modell soll veröffentlicht werden?

<details>
<summary>Antwort</summary>

Verwende für beide Kandidaten dieselbe repräsentative Bewertungsmenge und Lastannahmen. Miss Belegbarkeit, Quellenkorrektheit, Antwortverzicht, strukturierte Ausgabe, Latenzverteilung, Durchsatz und Ressourcenverbrauch. Bestimme Pflichtanforderungen, bevor du Mittelwerte vergleichst. Ein kleineres Modell könnte gewöhnliche Fragen und eine begrenzte Eskalation schwierige Fragen bearbeiten; auch diese Weiterleitung muss bewertet werden. Berücksichtige Retrieval und Wiederholungen im Budget. Modellgröße oder eine gelungene Zusammenfassung bestimmen nicht allein die beste Bereitstellung; dokumentiere den begründeten Kompromiss zwischen Qualität, Kapazität, Latenz und Kosten ohne erfundene Preise.

</details>

## 3. Eine Person verliert den Zugriff auf ein geteiltes Notizbuch, aber zwischengespeicherte Abschnitte beantworten weiterhin ihre Frage. Genügt der Indexfilter?

<details>
<summary>Antwort</summary>

Der gesamte Retrieval-Pfad muss aktuelle Rechte durchsetzen, bevor Kontext das Modell erreicht. Prüfe die Übertragung von Rechten auf untergeordnete Abschnitte, Indexaktualisierungen, Gesprächsspeicher und Caches. Cache-Schlüssel benötigen passenden Identitäts- und Berechtigungskontext; Rechteentzug verlangt Invalidierung oder eine andere Aktualitätskontrolle. Eine korrekte Indexabfrage schützt keine Antwort aus einem älteren unbeschränkten Cache. Definiere zulässige Berechtigungsaktualität und verweigere Zugriff, wenn sie nicht eingehalten werden kann. Zeige die Verweigerung mit zwei synthetischen Identitäten und einer Ablaufspur vor und nach dem Entzug.

</details>

## 4. Eine Antwort nennt das richtige Vorlesungs-PDF, belegt eine Frist aber mit einem Absatz, der nur einen Algorithmus definiert. Reicht eine vorhandene Quellenangabe?

<details>
<summary>Antwort</summary>

Nein. Prüfe, ob der angegebene Abschnitt in dieser Version die Aussage tatsächlich stützt. Existenz, Relevanz und Aussagebeleg sind getrennte Prüfungen. Untersuche, ob Retrieval die Aufgabenseite ausgelassen, die Abschnittsbildung Kontext verloren oder die Generierung trotz ausreichender Belege ein Datum erfunden hat. Fehlt die Frist in den freigegebenen Abschnitten, soll die App auf eine Antwort verzichten. Bewahre das Fehlbeispiel als Regressionstest auf und bewerte Quellenkorrektheit getrennt von Lesbarkeit. Ein funktionierender Link hilft bei der Navigation, belegt aber keine quellengebundene Antwort.

</details>

## 5. Ein Agent überschreitet nach Anforderung eines Freigabewerkzeugs die Zeit; das Backend hat die Freigabe bereits erstellt. Sofort erneut versuchen?

<details>
<summary>Antwort</summary>

Behandle das Ergebnis bis zum Abgleich als unbekannt. Gib der genehmigten Anwendungsoperation einen stabilen Idempotenzschlüssel und speichere ihren Status unabhängig von der Modellantwort. Frage diesen Status ab oder stelle ihn wieder her, bevor du erneut übermittelst; Wiederholungen dürfen keine weitere Freigabe erzeugen. Binde Zustimmung an genaue Dokumente, Empfänger und Versionen und prüfe die Autorisierung bei Ausführung erneut. Unterscheide Werkzeugfrist und Gesamtbudget des Agents. Bereinigte Korrelationskennungen sollen Anfrage, Zustimmung, Backend-Abschluss und verlorene Antwort verbinden, ohne Studierendeninhalte offenzulegen.

</details>

## 6. Ein Planungsagent delegiert an einen Retrieval-Agent mit Zugriff auf alle Kurse. Bewahrt der eingeschränkte Planungsprompt die Studierendenrechte?

<details>
<summary>Antwort</summary>

Die Übergabe muss vertrauenswürdigen Aufruferkontext enthalten; das Retrieval-Werkzeug muss dessen Rechte erzwingen. Ein Planungsprompt begrenzt einen privilegierten nachgelagerten Dienst nicht zuverlässig. Definiere je Agent Rolle, Werkzeugumfang, erlaubte Übergabefelder, Speicherverantwortung und Abbruchbudget. Gib nur freigegebene Belege an den Planungsagent zurück und verhindere die Wiederverwendung fremder Gesprächserinnerungen. Teste eine verweigerte Kursanfrage und eine manipulierte Übergabe. Delegation darf Verantwortlichkeiten aufteilen, aber niemals unbemerkt den Zugriff der nutzenden Person erweitern.

</details>

## 7. Die App soll eine Grafik beschreiben und ein neues Lernposter erstellen. Können beide Anfragen denselben visuellen Vertrag verwenden?

<details>
<summary>Antwort</summary>

Definiere getrennte Verträge für das Verstehen vorhandener Belege und das Erstellen neuer Medien, auch wenn eine Plattform beides unterstützt. Die Grafikerklärung braucht sichtbare Beschriftungen, Einheiten und Beziehungen als Belege sowie Antwortverzicht bei unlesbaren Bereichen. Das Poster braucht Generierungssteuerung, passende Quellenrechte, Sicherheitsprüfungen und Kontrolle erzeugter Texte und Diagramme. Videoformen brauchen zusätzlich Segment- oder Bearbeitungssemantik. Teste den Nutzen von Alternativtext und erfinde keine unsichtbaren Details. Eine überzeugende generierte Abbildung bestätigt keine Aussage über die ursprüngliche Vorlesungsgrafik.

</details>

## 8. Spracherkennung macht aus „mutex“ das Wort „music“, und die Übersetzung erzeugt flüssigen Unsinn. Nur den Übersetzungsprompt ändern?

<details>
<summary>Antwort</summary>

Prüfe die Stufen anhand ihrer getrennten Verträge. Ein früher Erkennungsfehler kann flüssigen, aber falschen übersetzten Text und eine falsche Antwort erzeugen. Erstelle Beispiele mit Fachwortschatz, Störgeräuschen, Verneinungen und Unterbrechungen; erhalte eine Textkorrekturmöglichkeit und prüfe unterstützte Fachanpassungen des Diensts. Hat ein direkt multimodaler Entwurf kein sichtbares Transkript, bewerte dieselbe Bedeutungserhaltung von Anfang bis Ende. Dokumentiere sprachspezifische Fehler, statt sie in Mittelwerten zu verbergen. Eine Promptänderung ist erst nach Verortung des Fehlers und Messung ihrer Wirkung begründet.

</details>

## 9. Content Understanding liefert eine Entwurfsfrist mit hoher Konfidenz in `final_due_date`. Darf der Kalendervorschlag weiterlaufen?

<details>
<summary>Antwort</summary>

Der Wert verletzt trotz hoher Konfidenz die beabsichtigte Feldbedeutung. Beschreibe das Feld für die endgültige Abgabe klar, prüfe seinen Dokumentbeleg und vergleiche beschriftete Entwurfs- und Endfristbeispiele. Validiere Format, fehlende Werte und Beziehungen zu anderen Meilensteinen. Leite ungelöste Mehrdeutigkeit zur Prüfung weiter; Konfidenz ist eine Schätzung, keine Geschäftsregelentscheidung. Prüfe, ob API und Konfiguration die erforderlichen Belege liefern. Eine spätere Kalender- oder Teilungsaktion braucht eigene Autorisierung und Zustimmung, unabhängig von Extraktionsqualität oder gültigem JSON.

</details>

## 10. Ein Release ändert Prompt, Embedding-Modell und Werkzeugantwortschema; Quellenfehler nehmen zu. Genügt es, den Prompt zurückzusetzen?

<details>
<summary>Antwort</summary>

Ermittle anhand des Release-Manifests alle geänderten Komponenten und ihre Kompatibilität. Eine neue Embedding-Darstellung kann Neuindexierung verlangen; ein alter Client kann ein neues Werkzeugergebnis falsch lesen. Vergleiche Ablaufspuren und Regressionsfälle zur Fehlerlokalisierung und stelle einen kompatiblen bekannten Stand wieder her oder führe die dokumentierte Migration aus. Definiere vor dem Rollout Rücksetzbedingungen für Quellenbindung, Zugriff, Werkzeugfehler und Latenz. Bewahre Versionskennungen in bereinigter Telemetrie auf. Ein einzelner sichtbarer Prompt behebt Änderungen an Retrieval-Darstellungen oder Antwortverträgen nicht zuverlässig.

</details>

Quellen: [aktuelle Ziele](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103), [SDKs und Endpunkte](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview), [Bewertung](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation), [Dokumentzugriff](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview), [Function Calling](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling), [Analyzer-Entwurf](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/best-practices), [Konfidenz und Quellenbindung](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/document/analyzer-improvement).
