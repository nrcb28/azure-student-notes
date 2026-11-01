# AI-901 · Gemeinsames Arbeitsbuch für Fortgeschrittene

[Leitfaden](AI-901.md) · [Zehn Fälle](AI-901-cases.md) · [Inhalt](README.md)

Fünf übereinstimmende Einheiten in den Lernsprachen. Arbeiten Sie offline mit erfundenen Universitätsnotizen, Prompts, Transkripten und Antwortentwürfen. Kennzeichnen Sie jede mögliche Ausgabe als **synthetisch** und jedes erwartete Ergebnis als **Vorhersage**. Laden Sie kein echtes Material von Studierenden hoch. Dieses Arbeitsbuch stellt nichts bereit und belegt keine vollständige Prüfungsabdeckung. Referenzprüfung: **1. November 2026**; [Lernziele gültig ab 15. April 2026](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901).

<a id="ai-901-unit-1"></a>

## 1. Fünf KI-Verträge definieren

Schreiben Sie je einen Vertrag für das Beantworten einer Kursfrage, das Extrahieren einer Aufgabenfrist, die Analyse von Feedbacktext, das Annehmen einer gesprochenen Frage und das Beschreiben eines Diagramms. Legen Sie Eingabemodalität, erlaubte Daten, Ausgabeform, inakzeptable Fehler und eine Rückfalllösung fest. Vergleichen Sie generative Antworten, Textanalyse, Sprache, Bildverarbeitung und Content Understanding anhand ihrer Erzeugnisse. Fügen Sie eine Anfrage zur Bildgenerierung hinzu, damit Erstellung von Interpretation unterschieden wird.

**Szenario:** Ein Teammitglied schlägt ein Bildmodell für jede Funktion vor. **Belege:** eine Entscheidungsmatrix mit fünf Zeilen, jeweils mit begründeter Fähigkeitsauswahl und einer verworfenen Alternative. Ergänzen Sie Fragen zur Modellauswahl bezüglich Modalitäten, Bereitstellungsoptionen, Sprache und unterstützten Parametern. Kennzeichnen Sie unbekannte Dienstdetails zur Prüfung in der aktuellen Dokumentation, statt Grenzen zu erfinden.

<a id="ai-901-unit-2"></a>

## 2. Quellengebundene Prompts und Zugriffsregeln schreiben

Erfinden Sie drei kurze Passagen: eine erlaubte Vorlesungsnotiz, ein privates Notizbuch und eine erlaubte Seite mit einer Anweisung zum Dokumentexport. Vergeben Sie stabile Quellenkennungen und definieren Sie zwei Studierende mit unterschiedlichen Zugriffslisten. Schreiben Sie System- und Nutzer-Prompts, die eine quellenbelegte Antwort verlangen, Quellgrenzen bewahren und Antwortverzicht erlauben. Der Abruf muss nach dem Zugriff der aufrufenden Person filtern, bevor der Kontext aufgebaut wird; der Prompt kann diese Sicherheitsgrenze nicht herstellen.

**Szenario:** Eine Frage hat in den erlaubten Passagen keine Antwort. **Belege:** ein erwarteter Antwortverzicht, eine Ablehnung verbotenen Zugriffs und eine synthetische, Injection-resistente Antwort. Vermerken Sie, welche Aussagen jede Quelle stützt. Erklären Sie, warum ein Zitat oder ein Angriffsdetektor allein weder Wahrheit noch Datenschutz oder Berechtigung belegen kann.

<a id="ai-901-unit-3"></a>

## 3. Einen schlanken Client ohne Cloud-Aufrufe nachverfolgen

Zeichnen Sie eine Anfrage eines Python-Clients an den vorgesehenen Foundry-Endpunkt und die konfigurierte Bereitstellung, gefolgt von einer Antwort oder einem Fehler. Unterscheiden Sie Identität, Autorisierung, Ziel und Bereitstellungsauswahl. Skizzieren Sie Pseudocode, der geschützte Konfiguration liest, geeignete Anmeldeinformationen beschafft, erlaubte Eingaben sendet, Fehler und Ausgabe prüft und ein sicheres Ergebnis darstellt. Kennzeichnen Sie die Skizze als **Pseudocode**, nicht als ausführbaren SDK-Code. Erklären Sie, wo Dictionaries, Iteration, Ausnahmen und asynchrone Aufrufe vorkommen könnten.

**Szenario:** Die Authentifizierung gelingt, aber die ausgewählte Ressource verweigert die Operation. **Belege:** eine bereinigte Diagnosecheckliste und erwartetes Clientverhalten für verweigerten Zugriff, Zeitüberschreitung, leere Ausgabe und ungültige Konfiguration. Vergleichen Sie, wie REST, SDK und CLI dieselbe Aufgabe ausdrücken. Benennen Sie den aktuellen [SDK-Schnellstart](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code), dem Sie bei späteren Cloud-Übungen folgen würden.

<a id="ai-901-unit-4"></a>

## 4. Multimodale Extraktion validieren

Erfinden Sie ein Aufgabenblatt mit endgültiger Frist, ein zweites Blatt ohne Datum, ein Diagramm mit unleserlicher Einheit und eine verrauschte gesprochene Frage. Definieren Sie ein Fristenschema mit Feldtypen, Regeln für fehlende Werte und Quellenverweisen. Erzeugen Sie absichtlich fehlerhafte synthetische Ausgaben: ein geratenes Datum, eine falsche Einheit und einen falsch verstandenen Fachbegriff. Verorten Sie den Fehler in Extraktion, visueller Interpretation, Erkennung oder nachgelagertem Schlussfolgern. Beschreiben Sie eine Sprache-zu-Text-Pipeline und eine unterstützte direkte multimodale Alternative.

**Szenario:** Eine Ausgabe ist gültiges JSON, widerspricht aber dem Blatt. **Belege:** getrennte Ergebnisse der Schema- und Quellenvalidierung, Prüfregeln für Mehrdeutigkeit und eine barrierearme Textalternative. Beschreiben Sie, wie [Content Understanding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) Dokument-, Bild-, Audio- und Videoeingaben verarbeiten könnte. Behandeln Sie Konfidenz nicht als Ersatz für Belege.

<a id="ai-901-unit-5"></a>

## 5. Einen einzelnen Agenten mit begrenzten Werkzeugen bewerten

Entwerfen Sie einen Notizensuchagenten mit Anweisungen, einer Modellauswahl, auf den Aufrufer begrenztem Abruf und ohne Änderungswerkzeuge. Definieren Sie Anfrage und Ergebnis seines Suchwerkzeugs sowie die Art, wie ein Client den Agenten identifiziert und den Gesprächskontext erhält. Erstellen Sie eine Fehlermatrix mit mindestens sechs Zeilen: belegte Antwort, fehlende Belege, verweigertes Dokument, Injection, widersprüchliche Frist und Werkzeug-Zeitüberschreitung. Ergänzen Sie erwartete Ergebnisse, bevor Sie für jede Zeile zwei konkurrierende synthetische Antworten schreiben.

**Abschließende Belege:** Reichen Sie Verträge, Prompts, Zugriffslisten, Clientskizze, Extraktionsprüfungen und bewertete Matrix ein. Bewerten Sie sachliche Belegbarkeit, Zitate, Antwortverzicht/Ablehnung, Datenschutz, Schemagültigkeit und Werkzeugberechtigungen getrennt. Erklären Sie eine Prompt-Überarbeitung und ihren Zielkonflikt. Listen Sie verbleibende praktische Arbeiten auf: Modellbereitstellung und Portalinteraktion, einen tatsächlichen SDK-Chatclient, einen im Portal getesteten einzelnen Agenten und dessen Client. Die Offline-Bewertung bereitet diese Arbeit vor.
