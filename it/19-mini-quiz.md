# Mini simulazione: scegli e capisci il perché

[←](README.md) · [CLI](../QUIZ.md) · [Leggere le domande su GitHub](20-quiz-cases.md)

Questa mini simulazione contiene otto scenari originali, due per ciascun percorso: AZ-900, AZ-104, AZ-305 e AZ-400. Serve a esercitarsi su decisioni concrete di Azure senza account né connessione. Gli scenari sono originali; le spiegazioni rimandano a Microsoft Learn e le fonti restano in inglese.

## Inizia

Python 3.9+ · es / en / it / de / fr / ru / ja / zh

```bash
python tools/quiz.py demo --lang it
python tools/quiz.py run --lang it --exam AZ-104 --count 2
```

## Pratica con correzione

Nella modalità practice ricevi la correzione dopo ogni risposta, con il motivo della soluzione, il problema della tua alternativa e un capitolo da ripassare. Domande e opzioni cambiano ordine. Rispondi con A–D, premi S o Invio per saltare e Q per terminare; puoi filtrare per esame.

```bash
python tools/quiz.py run --lang it --exam AZ-900 --exam AZ-104 --count 4 --seed 42
```

## Simulazione con timer facoltativo

La modalità exam mostra le spiegazioni solo alla fine della sessione. Il timer è facoltativo e viene controllato quando premi Invio: non interrompe da solo l’attesa del terminale e rifiuta una risposta inviata fuori tempo. Le domande senza risposta restano nel totale, anche se termini prima.

```bash
python tools/quiz.py run --lang it --mode exam --count 8 --minutes 12 --report .study-reports/first-quiz.json
```

## Ripassare gli errori

review ripropone le risposte errate e le domande senza risposta; --all include anche quelle corrette. Il rapporto conserva una copia di domande, opzioni e spiegazioni, così un aggiornamento della banca non cambia ciò che ripassi. Le domande mantengono la lingua della sessione salvata; puoi cambiare la lingua dell’interfaccia.

```bash
python tools/quiz.py review --lang it --report .study-reports/first-quiz.json
python tools/quiz.py review --lang it --report .study-reports/first-quiz.json --all
python tools/quiz.py review --lang it --report .study-reports/first-quiz.json --json
```

## Rapporti personali

Al termine viene salvato un rapporto JSON locale in .study-reports/, cartella esclusa da Git. Contiene le domande, le tue scelte, i tempi e lo stato della sessione. Non viene inviato ad alcun servizio e non vengono effettuate chiamate ad Azure. Puoi indicare un altro percorso; un file esistente non viene mai sostituito.

## Cosa misura il risultato

Otto scenari coprono solo una piccola parte del programma e non costituiscono un esame ufficiale o completo. Il risultato misura soltanto le risposte corrette di questa sessione e non prevede il superamento dell’esame. Usa spiegazioni e fonti per ripassare i temi difficili e consulta gli obiettivi ufficiali aggiornati prima di preparare una certificazione.

```bash
python tools/quiz.py doctor --lang it
```

[CLI](../QUIZ.md) · [Leggere le domande su GitHub](20-quiz-cases.md) · [Microsoft Learn](../QUIZ-SOURCES.md)
