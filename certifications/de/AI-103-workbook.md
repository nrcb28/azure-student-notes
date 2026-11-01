# AI-103 · Arbeitsbuch für fortgeschrittene Entwicklung

[Leitfaden](AI-103.md) · [Zehn Fälle](AI-103-cases.md) · [Inhalt](README.md)

Fünf übereinstimmende Einheiten nutzen erfundene universitäre Notizen und Offline-Beispiele für Anfragen und Antworten. Kennzeichne Kandidatenausgaben als **synthetisch** und erwartetes Verhalten als **Vorhersage**. Cloud-Ressourcen, Zugangsdaten, echte Studierendenakten und Dienstmessungen sind nicht nötig. Die Übungen vertiefen ausgewählte Umsetzungsfähigkeiten ohne vollständige Abdeckung zu behaupten. Geprüft am **1. November 2026** gegen die [ab 16. April 2026 gültigen Ziele](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103).

<a id="ai-103-unit-1"></a>

## 1. Clientvertrag und Bereitstellungsentscheidung festhalten

**Szenario:** Die Notizen-App soll bei hoher Lernlast aus einem Python-Backend eine belegte Antwort liefern. Definiere Anfrage- und Antwortbeispiele mit Identitätskontext, Anfragekennung, Kurs, Ergebnis, Antwort, Quellen und Fehlerkategorien. Nimm ungültiges JSON, verweigerten Zugriff, Zeitüberschreitung und unvollständige Ausgabe auf. Erstelle anhand aktueller [SDK-Dokumentation](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview) ein Kompatibilitätsmanifest für Ressource/Projekt, Endpunkttyp, Bereitstellungsname, API-Generation, Paketversionen und Anmeldeverfahren.

**Belege:** Vergleiche zwei hypothetische Modelle nach Qualität, Funktionen, Kapazität, Latenz und Ressourcenverbrauch; markiere offene Punkte zur späteren Prüfung. **Abgabe:** typisierte Vertragsskizze, vier Fehlerbeispiele und eine begründete Bereitstellungsentscheidung ohne erfundene Grenzen oder Preise.

<a id="ai-103-unit-2"></a>

## 2. Retrieval bei Rechteentzug entwerfen

**Szenario:** Zwei Studierende teilen ein Notizbuch, bis einer Person die Rechte entzogen werden. Erfinde sechs Abschnitte, darunter eine Aufgabenbedingung über eine vorgeschlagene Abschnittsgrenze hinweg. Definiere Dokument- und Abschnittskennungen, Versionen, Quellenpositionen, ACL-Metadaten und eine Index-/Embedding-Version. Vergleiche Vorhersagen für Schlüsselwort-, Vektor- und hybride Suche. Zeichne Aufruferauthentifizierung, Rechtefilterung, Retrieval, Cache-Abfrage und Modellkontext in tatsächlicher Reihenfolge.

**Belege:** Zugriffstabelle vor und nach Entzug für Indexweitergabe, Cache und Gesprächsspeicher sowie eine unbelegte Quellenangabe und eine Antwort wegen fehlender Belege. **Abgabe:** Retrieval-Entwurf mit Aktualitätsrichtlinie, Invalidierungsregel und vier Regressionsfällen. Erkläre den Einfluss der [Search-Zugriffsmuster](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) auf die Umsetzung.

<a id="ai-103-unit-3"></a>

## 3. Ein genehmigtes Werkzeug mit unklarem Ergebnis verfolgen

**Szenario:** Ein Notizen-Agent schlägt vor, ein erlaubtes Dokument mit einer Lerngruppe zu teilen. Definiere Werkzeugschema, Aufruferumfang, genaue Freigabedaten, Operationsschlüssel, Statusspeicher, Zeitbudget und Gesprächsverantwortung. Skizziere **Pseudocode** für validieren → autorisieren → freigeben → ausführen → abgleichen → berichten; dies ist ein Anwendungsentwurf, kein ausführbarer SDK-Code. Ergänze eine Übergabe zwischen Planungs- und Retrieval-Agent mit unveränderten Berechtigungen.

**Belege:** Ablaufspuren für Ablehnung, Erfolg, doppelte Zustellung, abgelaufene Zustimmung und eine nach Backend-Erfolg verlorene Antwort. **Abgabe:** Zustandsübergangstabelle und bereinigte Ablaufspur, die zeigt, warum eine Wiederholung keine doppelte Freigabe erzeugt. Verbinde den Entwurf mit der aktuellen [Function-Calling-Grenze](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling).

<a id="ai-103-unit-4"></a>

## 4. Multimodale Felder und Bedeutung prüfen

**Szenario:** Ein Aufgabenblatt enthält Entwurfs- und Endfrist, eine Grafik hat eine unlesbare Achse, und eine gesprochene Frage enthält „mutex“. Definiere getrennte Verträge für Text, Sprache, Bildverständnis, Mediengenerierung und Extraktion. Schreibe ein Content-Understanding-Feldschema mit genauen Beschreibungen, Typen, Nullbehandlung und Quellenverweisen. Erstelle fehlerhafte synthetische Ausgaben: vertauschte Fristen, eine erfundene Einheit und ein falsch verstandener Fachbegriff.

**Belege:** getrennte Schema-, Quellen-, Bedeutungs- und Barrierefreiheitsprüfungen einschließlich eines selbstsicher falschen Felds und einer Textkorrekturmöglichkeit. **Abgabe:** fünf kommentierte Beispiele und eine anhand beschrifteter Daten kalibrierte Prüfrichtlinie. Prüfe [Analyzer-Entwurf](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/best-practices) und [Verfügbarkeit von Dokumentbelegen](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/document/analyzer-improvement); benenne Grenzen der Modalität und API ausdrücklich.

<a id="ai-103-unit-5"></a>

## 5. Bewerten und ein Zurücksetzen proben

**Szenario:** Ein Release-Kandidat ändert Prompts, Werkzeugschemas und ein Embedding-Modell. Bewerte acht feste Fälle: belegte Antwort, fehlende Quelle, entzogener Zugriff, Injection, falsche Quellenangabe, mehrdeutige Frist, Werkzeugzeitüberschreitung und doppelte Aktion. Trenne Retrieval-Qualität, Aussagebelege, Sicherheit, Berechtigungstreue und Latenzvorhersagen. Beschreibe einen begrenzten Rollout und Kennzahlen für die Wiederherstellung.

**Belege:** Vergleichsblatt, kompatibles Release-Manifest, bereinigtes Telemetrieschema und eine Rücksetzfolge, die Client, Index, Prompt und Werkzeuge gemeinsam wiederherstellt. **Abgabe:** prüfbares Release-Paket mit Liste der noch im genehmigten Cloud-Labor benötigten Messungen. Nutze die [Bewertungsdokumentation](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation), um Offline-Vorhersagen von beobachteten Bereitstellungsbelegen zu trennen; berichte synthetische Werte nicht als Azure-Ergebnisse.
