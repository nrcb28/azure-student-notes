# DP-900 · 10 casi con risposte ragionate

[Guida](DP-900.md) · [Quaderno](DP-900-workbook.md) · [Indice](README.md)

Scenari originali di esercizio, non domande reali d'esame. Prima definisci il requisito, poi scarta un'alternativa e descrivi le evidenze da raccogliere. Non si dichiara alcuna distribuzione cloud.

## 1. L'app conserva PDF e metadati ricercabili sulla proprietà. Devono finire entrambi in un'unica tabella SQL?

<details>
<summary>Ragionamento</summary>

No. Un progetto plausibile conserva i PDF come oggetti in Blob Storage e proprietà e relazioni con i corsi in un database. Conta spiegare il confine di accesso e coerenza: il caricamento può riuscire mentre fallisce l'aggiornamento dei metadati. Definisci un flusso recuperabile e come individuare i file orfani. Rappresentare tutto in un database è un'altra possibilità se giustificata dai requisiti, ma «ogni dato deve essere una riga SQL» non è un buon punto di partenza.

</details>

## 2. Un file JSON contiene attributi annidati facoltativi. È non strutturato perché mancano alcuni campi?

<details>
<summary>Ragionamento</summary>

JSON può rappresentare dati semistrutturati: chiavi e annidamento danno organizzazione anche quando i record differiscono. I campi mancanti non cancellano quella struttura. Separa rappresentazione, qualità e scelta dell'archivio. Chiediti se un campo assente sia valido, sconosciuto o un errore di acquisizione, e documenta la reazione del consumatore. Un database a documenti potrebbe adattarsi all'accesso previsto, ma la sola presenza di JSON non decide l'architettura.

</details>

## 3. Ogni iscrizione ripete titolo e docente del corso. Quale problema potrebbe prevenire la normalizzazione?

<details>
<summary>Ragionamento</summary>

Un cambio di titolo potrebbe aggiornare alcune iscrizioni e lasciare il valore vecchio nelle altre. Conservare un record Corsi con chiave stabile e referenziarlo da Iscrizioni riduce questa anomalia. Spiega i vincoli necessari e come i join ricostruiscono il risultato utile. Questo non vieta ogni duplicazione: una fotografia analitica può conservare intenzionalmente descrizioni storiche. Dichiara se il problema riguarda la verità transazionale attuale o un modello storico di analisi.

</details>

## 4. Una query di analisi rallenta le iscrizioni. Spostare il grafico in Power BI elimina automaticamente il carico sul database?

<details>
<summary>Ragionamento</summary>

No. Dipende da come il modello acquisisce e aggiorna i dati. Un rapporto può continuare a interrogare la sorgente operativa o creare aggiornamenti costosi. Chiarisci freschezza, interrogazioni e capacità della sorgente prima di scegliere. Una copia analitica curata può isolare parte del lavoro, ma introduce ritardo e responsabilità sulla pipeline. Misura il carico sulla sorgente e definisci «aggiornato» invece di assumere che uno strumento di visualizzazione diverso cambi l'accesso sottostante.

</details>

## 5. Un'app SQL Server esistente richiede componenti del sistema operativo. Azure SQL Database è sempre un sostituto diretto?

<details>
<summary>Ragionamento</summary>

No. Censisci quei componenti e le altre dipendenze prima di scegliere la destinazione. Azure SQL Database, Managed Instance e SQL Server su VM Azure hanno confini diversi di compatibilità e gestione. Una VM offre accesso al sistema operativo, lasciando più manutenzione al team. Managed Instance può soddisfare alcuni requisiti di istanza senza risolvere ogni dipendenza esterna. Prepara una lista di compatibilità e prove di migrazione: riconoscere il motore non dimostra che l'applicazione completa funzionerà senza modifiche.

</details>

## 6. Uno studente pensa che Azure Table Storage offra chiavi esterne perché si chiama Table. Come correggeresti il progetto?

<details>
<summary>Ragionamento</summary>

Table Storage è un archivio non relazionale di entità, non un servizio SQL relazionale gestito. Il nome non implica join relazionali o applicazione delle chiavi esterne. Individua letture, aggiornamenti, relazioni e coerenza realmente richiesti; confronta poi un modello di entità adatto con uno relazionale. L'evidenza utile è un esempio svolto: mostra come un'iscrizione recupera il corso e come impedire o rilevare riferimenti non validi. Il nome invita a verificare le capacità, non le sostituisce.

</details>

## 7. Il batch notturno rispetta la scadenza del rapporto mattutino. Conviene sostituirlo con streaming solo per sembrare moderni?

<details>
<summary>Ragionamento</summary>

Parti dal ritardo ammesso dal business. Se un batch notturno affidabile consegna in tempo il risultato necessario, lo streaming può aggiungere lavoro operativo senza cambiare le decisioni degli utenti. Se invece occorre reagire al sovraccarico in pochi minuti, valuta un percorso a minore latenza per quel requisito. In entrambi i casi gestisci duplicati, input incompleto e tentativi ripetuti. Confronta freschezza dall'inizio alla fine e recupero dagli errori, non solo la frequenza di un componente.

</details>

## 8. I dati grezzi vengono caricati in un warehouse e puliti lì. È ETL? Il warehouse rende superflua la validazione?

<details>
<summary>Ragionamento</summary>

L'ordine descrive ELT: prima caricare, poi trasformare con le capacità della destinazione. ETL trasforma prima del caricamento nella destinazione prevista. Nessuno dei due elimina contratti e controlli dei dati. Definisci dove vanno i record non validi, quali trasformazioni sono ripetibili e come riconciliare i totali accettati con la sorgente. Controlla l'accesso ai dati grezzi riservati anche se gli analisti vedono solo il modello pulito: un'interfaccia comoda non dimostra che i record sottostanti siano sicuri o corretti.

</details>

## 9. Un pannello conta eventi di download. I retry producono ID duplicati. COUNT(*) indica necessariamente i download completati?

<details>
<summary>Ragionamento</summary>

Solo se la definizione dei dati garantisce che ogni riga contata equivalga a un download completato. Le consegne duplicate possono gonfiare COUNT(*). Definisci evento di business, identificatore stabile, condizione di completamento e intervallo, poi deduplica o aggrega secondo quella definizione. Conserva il conteggio di duplicati e rifiutati per spiegare la differenza. Prova con pochi dati che includano un ID ripetuto e un download incompleto. Un grafico plausibile non prova che la misura risponda alla domanda voluta.

</details>

## 10. Sei record di corsi entrano in un modello a documenti. Questo dimostra che Cosmos DB sia l'unico archivio sensato?

<details>
<summary>Ragionamento</summary>

No. Molti servizi possono conservare sei record; l'esempio dimostra soltanto che sono rappresentabili. Confronta query previste, relazioni, aggiornamenti, coerenza, requisiti operativi e competenze del team. Un database relazionale può essere più semplice se prevalgono vincoli ed entità collegate; un modello a documenti può adattarsi ad altri accessi. Scrivi una ragione della scelta e una condizione che la cambierebbe. Preparare i fondamenti significa sviluppare questo ragionamento, senza associare un prodotto a ogni esempio in forma JSON.

</details>

Fonti: [obiettivi ufficiali](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900), [Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview), [Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction), [ETL/ELT](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl), [Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview).
