# Miniquiz: entscheiden und aus Fehlern lernen

[←](README.md) · [CLI](../QUIZ.md) · [Fragen auf GitHub lesen](20-quiz-cases.md)

Acht eigene Szenarien helfen dir, Azure-Entscheidungen zu begründen: je zwei zu AZ-900, AZ-104, AZ-305 und AZ-400. Fragen, Antworten und Erläuterungen gibt es in allen acht Sprachen. Das Werkzeug läuft lokal mit Python und benötigt weder ein Azure-Konto noch zusätzliche Pakete.

## Start

Python 3.9+ · es / en / it / de / fr / ru / ja / zh

```bash
python tools/quiz.py demo --lang de
python tools/quiz.py run --lang de --exam AZ-104 --count 2
```

## Üben mit Erklärung

Im Übungsmodus erhältst du die Erklärung direkt nach jeder Antwort. Neben der richtigen Lösung siehst du, warum deine gewählte Alternative nicht zu den Bedingungen passt. A–D wählt eine Antwort, S oder eine leere Eingabe überspringt die Frage und Q beendet die Sitzung. Frage- und Antwortreihenfolge werden gemischt.

```bash
python tools/quiz.py run --lang de --exam AZ-900 --exam AZ-104 --count 4 --seed 42
```

## Prüfungsmodus mit optionalem Timer

Im Prüfungsmodus erscheinen die Erläuterungen erst nach dem Ende der Sitzung. Du kannst eine Zertifizierungsroute auswählen und optional ein Zeitlimit in Minuten setzen. Die Eingabe ist synchron: Der Timer wird erst nach der Eingabetaste geprüft und weist verspätete Antworten zurück. Er beendet eine offene Eingabe nicht selbstständig.

```bash
python tools/quiz.py run --lang de --mode exam --count 8 --minutes 12 --report .study-reports/first-quiz.json
```

## Fehler nacharbeiten

Der gespeicherte Bericht zeigt richtige, falsche und unbeantwortete Fragen sowie die Ergebnisse je Thema. Beim Nacharbeiten werden standardmäßig falsche und unbeantwortete Fragen mit Erklärung, Quelle und passendem Kapitel angezeigt. Unbeantwortete Fragen bleiben Teil der Gesamtzahl; eine kurze Sitzung verbessert das Ergebnis also nicht künstlich.

```bash
python tools/quiz.py review --lang de --report .study-reports/first-quiz.json
python tools/quiz.py review --lang de --report .study-reports/first-quiz.json --all
python tools/quiz.py review --lang de --report .study-reports/first-quiz.json --json
```

## Persönliche Berichte

Berichte bleiben lokal als JSON im von Git ausgeschlossenen Ordner .study-reports/. Sie enthalten eine Momentaufnahme der Fragen, Antwortreihenfolge, Auswahl und Erläuterungen, damit eine spätere Änderung der Fragenbank alte Sitzungen nicht verändert. Es werden keine Azure-Ressourcen erstellt und keine Antworten an einen Dienst geschickt. Prüfe selbst gewählte Speicherorte, bevor du sie teilst.

## Aussagekraft des Ergebnisses

Mit acht Szenarien ist dies ein Miniquiz zum Wiederholen, keine vollständige Simulation, kein offizieller Fragenkatalog und keine Bestehensprognose. Die Erklärungen verweisen auf englische Microsoft-Learn-Seiten und passende Kapitel dieser Ausgabe. Ein gutes Ergebnis belegt nur, dass du diese konkreten Übungsfragen beantwortet hast.

```bash
python tools/quiz.py doctor --lang de
```

[CLI](../QUIZ.md) · [Fragen auf GitHub lesen](20-quiz-cases.md) · [Microsoft Learn](../QUIZ-SOURCES.md)
