# Allenatore di studio senza Azure

[←](README.md) · [Anki](../flashcards/it.tsv)

Esercitati sui 40 casi della tua lingua, dieci per certificazione. Richiede Python 3.9 o successivo e solo libreria standard. Nessun account cloud, pacchetto esterno o connessione durante l'uso.

```bash
python tools/study.py demo --lang it --exam AZ-104
python tools/study.py study --lang it --exam AZ-104 --limit 5
```

## 1. Mettiti alla prova

Leggi, pensa e premi Invio. Confronta la spiegazione e valuta: 0 dimenticata, 1 difficile, 2 bene, 3 facile. q esce; le valutazioni completate vengono salvate. È autovalutazione, non correzione automatica o voto d'esame.

## 2. Ripassa le difficoltà

La modalità normale sceglie schede scadute e nuove, prima le scadute. weak sceglie casi difficili o con dimenticanze; random mescola. Progresso separato per lingua. Le risposte scritte non vengono conservate.

## 3. Progresso e piano

stats mostra nuove, scadute, consolidate e dimenticanze per esame. Consolidata significa due valutazioni consecutive almeno 2, non preparazione garantita. plan suggerisce circa quattro minuti per caso senza prevedere le scadenze future.

## 4. Intervalli

0 torna dopo dieci minuti e azzera la sequenza; 1 domani e azzera. 2 usa un giorno, poi tre, poi raddoppia. 3 inizia con quattro giorni e moltiplica per 2,5, massimo 365. Regola semplice propria, non FSRS né garanzia di memoria.

## 5. Portalo in Anki

Scarica mazzi pronti o esporta una selezione. UTF-8, tre colonne: domanda, spiegazione, tag. Il progresso Anki è indipendente. Controlla anteprima e mappatura.

## 6. I tuoi dati

Il file predefinito .study-progress.json è escluso da Git. --progress sceglie un altro percorso. Scrittura atomica e protezione da sessioni concorrenti; JSON corrotto non sostituito. Conserva copie per trasferire la cronologia.

```bash
python tools/study.py study --lang it --mode weak --limit 5
python tools/study.py stats --lang it
python tools/study.py plan --lang it --days 7 --minutes 20
python tools/study.py export --lang it --exam AZ-104 --output exports/it-az104.tsv
python tools/study.py doctor --lang it
```

[CLI reference](../TRAINER.md) · [Anki decks](../flashcards/README.md)

## Mini simulazione: scegli e capisci il perché

[Mini simulazione: scegli e capisci il perché](19-mini-quiz.md) · [Leggere le domande su GitHub](20-quiz-cases.md)
