# DP-700 · Dieci casi con risposte ragionate

[Guida](DP-700.md) · [Quaderno di esercizi](DP-700-workbook.md) · [Indice](README.md) · [Español](../es/DP-700-cases.md)

Esercizi originali su dati universitari, non quesiti ufficiali d'esame. Esponi decisione e prove prima di aprire ogni risposta. La [guida](DP-700.md) registra l'ambito ufficiale e la verifica delle fonti; questi casi non dichiarano copertura completa né esecuzione Fabric.

## 1. Il gruppo conosce Synapse Spark. Può presumere impostazioni predefinite e comportamenti di distribuzione identici in Fabric?

<details>
<summary>Risposta</summary>

No. I concetti familiari di Spark aiutano, ma Fabric è una piattaforma SaaS con confini propri di workspace, capacità, elementi, runtime e ciclo di vita. Fai l'inventario di dipendenze, librerie, percorsi di archiviazione, identità e configurazioni supportate prima di adattare il notebook. Definisci un piccolo carico sintetico di iscrizioni e confrontane l'output previsto con una successiva esecuzione Fabric controllata. Verifica il comportamento di distribuzione e connessione separatamente dalla sintassi delle trasformazioni. Codice simile è un punto di partenza utile, ma non dimostra equivalenza di permessi, impostazioni predefinite del runtime o responsabilità operative.

</details>

## 2. Un gruppo di reportistica relazionale e uno di elaborazione dei file propongono lo stesso archivio. Che cosa decide?

<details>
<summary>Risposta</summary>

Confronta il carico effettivo: formati dei file, motori di trasformazione, requisiti di scrittura relazionale, consumo SQL, governance e proprietà. Un lakehouse è un candidato ragionevole per preparare file di download tramite Spark; un warehouse può essere adatto a un modello analitico centrato su T-SQL. Possono collaborare quando i requisiti lo giustificano. Definisci granularità delle tabelle e aggiornamento accettabile prima di confrontare le prestazioni. Non trattare l'endpoint di analisi SQL del lakehouse come superficie generale di scrittura di un warehouse. Registra operazioni supportate e un piano di convalida rappresentativo invece di scegliere solo in base alla familiarità del gruppo.

</details>

## 3. Uno shortcut espone il catalogo della biblioteca. Fornisce un backup e accesso a ogni analista?

<details>
<summary>Risposta</summary>

No. Lo shortcut fa riferimento ai dati sorgente, quindi una destinazione mancante o un permesso della fonte modificato possono influire sull'accesso. Non è una copia di recupero conservata indipendentemente. Esamina se lo shortcut è interno o esterno, quale identità o connessione viene usata e quali permessi si applicano al percorso effettivo di lettura. Prova un analista autorizzato e uno a cui l'accesso è negato con dati sintetici. Concorda cambiamenti di schema e disponibilità con il responsabile del catalogo. Serve un progetto separato di conservazione e recupero se è richiesto il ripristino storico.

</details>

## 4. Un report deve contenere soltanto le iscrizioni di ieri. L’attività di copia risulta riuscita, ma il report contiene iscrizioni di oggi. L’intero flusso ha avuto successo?

<details>
<summary>Risposta</summary>

L'attività è terminata tecnicamente, ma la condizione di accettazione operativa è fallita. Esamina parametri della finestra di elaborazione, espressioni dinamiche, filtri sorgente, fusi orari e associazioni della destinazione. Riconcilia conteggi della finestra sorgente e chiavi operative selezionate con l'output pubblicato prima di consentire l'aggiornamento a valle. Una pipeline deve coordinare convalida e pubblicazione, mentre un notebook o una trasformazione SQL può implementare le regole sui dati. Registra identificatore dell'esecuzione e intervallo previsto per ricostruire l'errore. Correggi l'output interessato con una ripetizione idempotente invece di presumere che uno stato verde dimostri correttezza.

</details>

## 5. Un batch è stato confermato ma ha perso la risposta di successo. Come può un nuovo tentativo evitare iscrizioni duplicate?

<details>
<summary>Risposta</summary>

Usa una chiave stabile di iscrizione e una versione deterministica della fonte, deduplica il batch in ingresso ed esegui il merge nello stato di destinazione previsto. Rendi persistente il progresso solo dopo convalida dell'output e conferma riuscita. Un nuovo tentativo sullo stesso intervallo delimitato della fonte deve trovare versioni equivalenti già applicate e lasciare invariati i totali operativi. Registra identificatore del batch e conteggi di riconciliazione per la diagnosi operativa. Aggiungere ogni arrivo senza una regola di unicità duplicherebbe le righe. Considera anche aggiornamenti vecchi e ritardati ed eliminazioni: una strategia di ripetizione deve preservare l'ordine delle versioni, non soltanto riconoscere payload identici.

</details>

## 6. Una query sulla data di modifica perde ritiri e correzioni tardive. Che cosa cambia nel progetto di caricamento?

<details>
<summary>Risposta</summary>

Identifica se i ritiri rimuovono fisicamente righe o producono un cambiamento di stato. Una semplice query sulle righe rimaste non può scoprire eliminazioni fisiche. Valuta CDC supportato con record di eliminazione, un contratto di eliminazione logica o riconciliazione periodica. Per le correzioni tardive, usa ordinamento affidabile della fonte e una finestra di sovrapposizione con deduplicazione deterministica, oppure un altro meccanismo supportato di tracciamento delle modifiche. Conserva informazioni di versione sufficienti per rifiutare aggiornamenti obsoleti dopo un'eliminazione. Prova timestamp uguali, record ritardati e ripetizioni. Documenta la finestra di conservazione della fonte, così un'interruzione prolungata non crea silenziosamente una lacuna irrecuperabile.

</details>

## 7. Un download avviene alle 23:59 e arriva alle 00:07. Deve cambiare il conteggio di quale giorno?

<details>
<summary>Risposta</summary>

La risposta segue la regola temporale operativa dichiarata. Se i report contano i download per tempo dell'evento, il record appartiene alla finestra del giorno precedente. Definisci fuso orario, confine della finestra, ritardo tollerato e possibilità di correggere un risultato pubblicato. Raggruppare per tempo di elaborazione lo collocherebbe nel giorno di arrivo e risponderebbe a un'altra domanda. Un watermark di streaming controlla gestione dei ritardi e stato conservato; un checkpoint supporta il progresso del recupero. Nessuno dei due sostituisce una politica esplicita di correzione o dimostra che la destinazione non possa duplicare l'output dopo una ripetizione.

</details>

## 8. Arriva una colonna facoltativa insieme a date malformate e chiavi di insegnamento sconosciute. L'evoluzione dello schema deve accettare tutte le righe?

<details>
<summary>Risposta</summary>

Valuta la colonna facoltativa come modifica di compatibilità, separatamente dalla validità dei record. Un campo aggiuntivo approvato non rende accettabili date malformate o riferimenti mancanti. Applica regole esplicite di tipo e chiave, conserva l'input non valido in una quarantena controllata con codici del motivo e riconcilia record accettati e rifiutati. Un insegnamento sconosciuto può richiedere risoluzione ritardata del riferimento invece di rifiuto permanente. Preserva identificatori della fonte per correzione e ripetizione sicure. Controlla i contratti a valle prima di pubblicare il nuovo schema ed evita dettagli degli studenti in log diagnostici senza restrizioni.

</details>

## 9. Un report applica sicurezza sulle righe e ha un'etichetta di riservatezza. L'accesso diretto ai file è automaticamente sicuro?

<details>
<summary>Risposta</summary>

No. Identifica il confine che applica la restrizione sulle righe ed esamina percorsi alternativi come query SQL e accesso diretto a OneLake. Ruoli del workspace, permessi sugli elementi, regole specifiche del motore e permessi sui file devono corrispondere alle capacità richieste al lettore. Un'etichetta di riservatezza fornisce contesto di governance e comportamenti di protezione supportati; la sua sola presenza non dimostra l'applicazione di ogni requisito di autorizzazione. Prova aggregati consentiti per insegnamento e dettagli degli studenti negati usando identità rappresentative. Esamina anche permessi di esportazione e accesso ampio ereditato, che possono vanificare una superficie di report accuratamente limitata.

</details>

## 10. Un notebook distribuito è più lento e legge la produzione dall'ambiente di test. Si deve prima aumentare la capacità?

<details>
<summary>Risposta</summary>

Correggi prima l'associazione all'ambiente e impedisci pubblicazioni involontarie. Esamina riferimenti alle connessioni, parametri, identità di esecuzione e supporto della distribuzione per elemento e dipendenze. La cronologia Git o una promozione riuscita non dimostrano che questi valori siano corretti. Poi confronta lo stesso carico con una base: contesa sulla capacità, squilibrio delle fasi Spark, shuffle, dimensioni dei file, esclusione delle partizioni e comportamento della fonte. Prova una modifica sostenuta dalle prove con controlli di correttezza. Aumenta la capacità quando la pressione misurata sostiene la decisione, invece di usare le risorse per nascondere un errore di configurazione o un'organizzazione inefficiente dei dati.

</details>
