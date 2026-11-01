# DP-300 · 10 casi con risposte ragionate

[Guida](DP-300.md) · [Quaderno](DP-300-workbook.md) · [Indice](README.md)

Esercizi originali, non quesiti ufficiali d'esame. Prima di aprire la risposta identifica il vincolo, proponi una decisione e descrivi le prove da raccogliere. I casi non dichiarano esecuzioni in Azure né copertura completa dell'esame.

## 1. Un'applicazione richiede un'estensione supportata a livello di sistema operativo. Basta il supporto T-SQL per scegliere SQL Database?

<details>
<summary>Ragionamento</summary>

No. Il requisito sul sistema operativo cambia il confine dell'hosting. Verifica se l'estensione sia essenziale e se esista un'alternativa supportata in un servizio gestito. Se resta necessario il controllo diretto del sistema operativo, valuta SQL Server su VM includendo responsabilità su aggiornamenti, backup, monitoraggio e disponibilità. La compatibilità deve considerare dipendenze esterne agli oggetti del database oltre al T-SQL. Verifica il requisito applicativo reale prima di scegliere: conoscere la sintassi SQL non dimostra compatibilità di implementazione.

</details>

## 2. La migrazione dei dati termina correttamente. È sicuro riaprire subito le scritture?

<details>
<summary>Ragionamento</summary>

Il trasferimento completato è solo una tappa. Valida stato finale previsto, totali aziendali importanti, autorizzazioni, percorsi applicativi e attività pianificate. Stabilisci quando si siano fermate le scritture sorgenti e se le modifiche residue siano state applicate. Dichiara autorevole la destinazione prima di riaprire il traffico. Il piano di ritorno deve gestire le scritture sulla destinazione dopo il passaggio: riconnettere la sorgente potrebbe perderle. Usa una lista esplicita di via libera o arresto e registra quali verifiche siano osservate invece che presunte.

</details>

## 3. L'app risolve l'indirizzo SQL privato e si connette, ma SELECT viene negato. Bisogna aprire ulteriormente la rete?

<details>
<summary>Ragionamento</summary>

La connessione riuscita e l'istruzione negata indicano un problema di autorizzazione nel database più che un guasto generale di rete. Conferma entità autenticata, database, oggetto e operazione. Controlla i permessi applicabili e concedi la capacità minima secondo il modello scelto. Un ruolo Azure Contributor non fornisce automaticamente accesso alla tabella. Aprire l'endpoint pubblico cambierebbe l'esposizione senza aggiungere il permesso mancante. Ripeti la stessa operazione applicativa con la stessa identità per verificare la diagnosi.

</details>

## 4. Un requisito vieta agli amministratori del database di vedere alcuni valori in chiaro. TDE da solo basta?

<details>
<summary>Ragionamento</summary>

TDE protegge i file a riposo, ma da solo non impedisce a una query autorizzata di restituire valori in chiaro. Esamina una soluzione come Always Encrypted con client supportati e chiavi fuori dal confine di accesso dell'amministratore. Verifica operazioni di query richieste, compatibilità applicativa, recupero delle chiavi e responsabilità operative. Il mascheramento dinamico non offre un confine di riservatezza equivalente. Valida il modello di minaccia con dati sintetici e prove consentite, senza considerare intercambiabili tutte le funzionalità che nominano la cifratura.

</details>

## 5. Una query rallenta dopo un rilascio mentre la CPU complessiva resta normale. Quali prove cercare per prime?

<details>
<summary>Ragionamento</summary>

Identifica la query e confronta piani e comportamento negli intervalli equivalenti tramite lo storico disponibile di Query Store. Controlla parametri applicativi, letture, attese, blocchi e modifiche recenti a schema o statistiche. Una CPU aggregata normale non dimostra la salute di una transazione specifica. Formula un'ipotesi prima di ridimensionare il servizio. Se provi un piano precedente, definisci criteri di successo e ritorno, poi osserva traffico rappresentativo: una singola esecuzione veloce è una prova debole di miglioramento duraturo.

</details>

## 6. Un nuovo indice accelera le letture ma rallenta molto le importazioni. È necessariamente un successo?

<details>
<summary>Ragionamento</summary>

No. L'indice viene mantenuto durante i cambiamenti dei dati, quindi il beneficio va valutato sull'intero carico. Confronta latenze di lettura e scrittura, capacità elaborativa, spazio e piani prima e dopo il cambiamento con carichi rappresentativi. Verifica sovrapposizioni con gli indici esistenti e se una definizione più limitata o con ordine diverso soddisfi il requisito. Registra soglie di accettazione anche per le importazioni, non solo per le ricerche. Non conservare una modifica soltanto perché la query dimostrativa è diventata più veloce.

</details>

## 7. Una transazione lunga blocca ricerche brevi. Bisogna terminare tutte le sessioni bloccate?

<details>
<summary>Ragionamento</summary>

Trova la catena di blocco e la transazione che mantiene i blocchi pertinenti prima di decidere cosa interrompere. Una sessione bloccata è spesso un sintomo, non la sorgente. Identifica lavoro, durata, responsabile e conseguenze dell'annullamento. Terminare una transazione può richiedere un annullamento lungo e compromettere la correttezza applicativa. In un'indagine controllata valuta transazioni più brevi o un isolamento adatto dopo aver capito i requisiti di coerenza. Registra prove e decisione sull'incidente, anziché usare uno script di terminazione indiscriminata.

</details>

## 8. Un processo SQL Agent deve passare ad Azure SQL Database. Basta copiarne il calendario?

<details>
<summary>Ragionamento</summary>

SQL Agent non è disponibile in Azure SQL Database. Classifica l'attività: lavoro T-SQL supportato su più database può adattarsi a Elastic Jobs; un flusso con servizi esterni può richiedere orchestrazione. Valuta dipendenze, identità, scoperta delle destinazioni, tentativi e notifiche, non soltanto l'espressione dell'orario. La ripetizione non dovrebbe duplicare risultati aziendali dopo una risposta incerta. Prova la sostituzione su dati sintetici isolati e confronta sia la registrazione dell'esecuzione sia lo stato aziendale risultante.

</details>

## 9. Un DELETE accidentale arriva al database secondario. La replica ha fallito?

<details>
<summary>Ragionamento</summary>

La replica potrebbe fare esattamente il proprio compito: trasportare una modifica valida e confermata verso un'altra copia. Disponibilità e recupero storico risolvono problemi diversi. Determina momento dell'incidente e punti conservati disponibili, poi pianifica il ripristino in un database isolato prima della modifica indesiderata. Verifica record mancanti e scritture valide successive prima di scegliere come recuperare il servizio. Non presumere che sostituire tutto con uno stato precedente sia accettabile: la decisione deve considerare anche le scritture legittime avvenute nel frattempo.

</details>

## 10. Il database ha completato il failover, ma l'app degli appunti continua a fallire. L'obiettivo RTO è raggiunto?

<details>
<summary>Ragionamento</summary>

Non se l'obiettivo riguarda il servizio usato dagli studenti. Verifica endpoint applicativo supportato, DNS del client, riconnessione, identità, dipendenze e attività pianificate sul primario corrente. Esegui una verifica funzionale con record sintetici e misura il recupero dall'evento iniziale definito. Registra separatamente la perdita di dati rispetto all'RPO. Prima del ritorno stabilisci copia autorevole e piano di sincronizzazione. Uno stato sano del database, da solo, non dimostra che l'app o i suoi obiettivi di recupero siano stati ripristinati.

</details>

## Autovalutazione e fonti

Per ogni caso identifica il requisito, giustifica una decisione e nomina una verifica. È un metodo indipendente di ripasso, non un punteggio ufficiale d'esame né una previsione di superamento.

[Guida ufficiale](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300) · [Riferimenti tecnici e spiegazioni](DP-300.md)
