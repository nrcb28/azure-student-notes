# Allenatore di studio senza Azure

[←](README.md) · [Anki](../flashcards/it.tsv)

Esercitati sui 170 casi della tua lingua, dieci per certificazione. Richiede Python 3.9 o successivo e solo libreria standard. Nessun account cloud, pacchetto esterno o connessione durante l'uso.

```bash
python tools/study.py demo --lang it --exam AZ-802
python tools/study.py study --lang it --exam AZ-104 --limit 5
```

Il fuso di visualizzazione predefinito, Europe/Madrid, richiede i dati IANA del sistema operativo. Se non sono disponibili, aggiungi --timezone UTC al comando demo o study; non servono pacchetti aggiuntivi.

## 1. Mettiti alla prova

Leggi, pensa e premi Invio. Confronta la spiegazione e valuta: 0 dimenticata, 1 difficile, 2 bene, 3 facile. q esce; le valutazioni completate vengono salvate. È autovalutazione, non correzione automatica o voto d'esame.

## 2. Ripassa le difficoltà

La modalità normale sceglie schede scadute e nuove, prima le scadute. weak sceglie casi difficili o con dimenticanze; random mescola. Progresso separato per lingua. Le risposte scritte non vengono conservate.

## 3. Progresso e piano

stats mostra nuove, scadute, consolidate e dimenticanze per esame. Consolidata significa due valutazioni consecutive almeno 2, non preparazione garantita. plan suggerisce circa quattro minuti per caso senza prevedere le scadenze future.

## 4. Intervalli

0 torna dopo dieci minuti e azzera la sequenza; 1 torna il giorno dopo e la azzera. Le valutazioni 2 e 3 condividono una sequenza di ripassi consecutivi riusciti. Con 2, il primo successo programma un giorno, il secondo tre e i successivi raddoppiano l’intervallo precedente. Con 3, il primo successo programma quattro giorni; i successivi moltiplicano l’intervallo precedente per 2,5, arrotondano a giorni interi e usano almeno quattro giorni. Entrambi hanno un massimo di 365 giorni. Cambiare valutazione non azzera la sequenza: 3 seguito da 2 programma quattro e poi tre giorni. Regola semplice propria, non FSRS né garanzia di memoria.

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
