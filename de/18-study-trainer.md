# Lerntrainer ohne Azure

[←](README.md) · [Anki](../flashcards/de.tsv)

Übe 40 Fälle je Sprache, zehn pro Zertifizierung. Python 3.9 oder neuer und Standardbibliothek genügen. Kein Cloud-Konto, Zusatzpaket oder Netz während der Nutzung.

```bash
python tools/study.py demo --lang de --exam AZ-104
python tools/study.py study --lang de --exam AZ-104 --limit 5
```

## 1. Selbst prüfen

Frage lesen, nachdenken, Enter drücken. Erklärung vergleichen und bewerten: 0 vergessen, 1 schwer, 2 gut, 3 leicht. q beendet; fertige Bewertungen werden gespeichert. Selbstbewertung, keine automatische Korrektur oder Prüfungsnote.

## 2. Schwieriges wiederholen

Standardmäßig zuerst fällige, dann neue Karten. weak wählt schwierige Fälle oder solche mit früherem Vergessen; random mischt. Fortschritt ist sprachgetrennt. Ausgeschriebene Antworten werden nicht gespeichert.

## 3. Fortschritt und Plan

stats zeigt neue, fällige, gefestigte Karten und Vergessen je Prüfung. Gefestigt bedeutet zweimal hintereinander mindestens 2, nicht Prüfungsreife. plan schlägt etwa vier Minuten je Fall vor, keine sichere Fälligkeitsprognose.

## 4. Intervalle

0: zehn Minuten, Serie zurückgesetzt. 1: morgen, zurückgesetzt. 2: ein Tag, drei Tage, danach verdoppeln. 3: vier Tage, danach mal 2,5, höchstens 365 Tage. Einfache eigene Regel, nicht FSRS oder Gedächtnisgarantie.

## 5. Anki-Export

Fertige Stapel herunterladen oder Auswahl exportieren. UTF-8 und drei Spalten: Frage, Erklärung, Tags. Anki-Fortschritt bleibt unabhängig. Vorschau und Spaltenzuordnung prüfen.

## 6. Eigene Daten

Standarddatei .study-progress.json ist von Git ausgeschlossen. --progress wählt anderen Pfad. Atomare Schreibvorgänge schützen vor konkurrierender Überschreibung. Beschädigte JSON-Dateien werden nicht ersetzt. Sicherungskopien für Umzug behalten.

```bash
python tools/study.py study --lang de --mode weak --limit 5
python tools/study.py stats --lang de
python tools/study.py plan --lang de --days 7 --minutes 20
python tools/study.py export --lang de --exam AZ-104 --output exports/de-az104.tsv
python tools/study.py doctor --lang de
```

[CLI reference](../TRAINER.md) · [Anki decks](../flashcards/README.md)
