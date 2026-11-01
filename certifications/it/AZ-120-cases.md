# AZ-120 · 10 casi con risposte ragionate

[Guida](AZ-120.md) · [Quaderno di esercizi](AZ-120-workbook.md) · [Indice](README.md)

Scenari originali di un'università come organizzazione, non domande ufficiali d'esame. Spiega decisione e prove prima di aprire ogni risposta. Tutti i controlli proposti sono progettazione offline; non si dichiara alcuna esecuzione Azure o SAP.

## 1. L'università aggiunge due server applicativi ma mantiene una sola VM ASCS e una sola VM HANA. Ha eliminato i punti singoli di guasto importanti?

<details>
<summary>Risposta</summary>

No. La ridondanza dei server applicativi non protegge servizi centrali o database. Inventaria ogni SID e distingui ASCS, ERS, istanze applicative, HANA, file condivisi e loro dipendenze. Proponi progetti HA supportati per servizi centrali e database, con responsabilità esplicite e percorsi di riconnessione dei client. Le prove devono includere un diagramma delle dipendenze e l'effetto previsto della perdita di ogni componente. Conferma anche la capacità applicativa dopo un guasto. Contare le VM non può dimostrare che una transazione di acquisto sopravviva alla perdita del servizio di coordinamento o dei dati.

</details>

## 2. Una VM più economica ha lo stesso numero di core della VM HANA proposta. È una prova sufficiente per sostituirla?

<details>
<summary>Risposta</summary>

No. Controlla la certificazione SAP HANA per tipo esatto di VM, carico, versione del sistema operativo, versione del database e modello di distribuzione. Confronta domanda misurata di memoria, crescita, requisiti SAPS pertinenti per i livelli applicativi, velocità di trasferimento dell'archiviazione, latenza dei log e limiti di rete. Verifica anche capacità regionale e quote. Le prove consistono in un registro della combinazione supportata e un foglio di dimensionamento con margine in caso di guasto, non in un confronto delle CPU. Una stima infrastrutturale più bassa non decide la supportabilità, e questi appunti non possono stabilire diritti di licenza SAP dell'università o capacità sufficiente per la produzione.

</details>

## 3. Il gruppo di rete del campus dice che ExpressRoute rende crittografata ogni connessione SAP. Il registro architetturale deve accettare questa affermazione?

<details>
<summary>Risposta</summary>

No. Connettività privata e crittografia sono proprietà distinte. Disegna il percorso dal campus ad Azure, il punto di passaggio del provider, il routing Azure, gli endpoint applicativi e ogni confine crittografico scelto. Specifica crittografia applicativa supportata o un'altra configurazione crittografica adeguata dove la politica lo richiede, e verifica le capacità esatte del servizio. Documenta anche risoluzione DNS, dipendenze di autenticazione, resilienza delle route e flussi consentiti. Le prove devono identificare quale traffico è crittografato, dove inizia e finisce la protezione e come si verificherebbe la configurazione. Un circuito privato da solo non dimostra riservatezza da un'estremità all'altra per ogni protocollo.

</details>

## 4. Uno studente colloca entrambi i nodi HA in un PPG e sostiene che ciò li protegga anche dall'interruzione di una zona. Che cosa deve cambiare nel ragionamento?

<details>
<summary>Risposta</summary>

Separa vicinanza per la latenza e isolamento per la resilienza. Un PPG vincola la prossimità fisica e non fornisce isolamento dei guasti tra zone. Scegli un posizionamento di disponibilità supportato per il requisito di recupero, poi valuta latenza effettiva tra nodi e comportamento della replica. Se i PPG sono giustificati, applicali entro i vincoli di posizionamento adatti e documenta i limiti di allocazione. Le prove devono includere diagramma dei domini di guasto, latenza misurata o esplicitamente ipotizzata, capacità rimanente e sequenza di subentro. Né un PPG né le zone di disponibilità configurano da soli un cluster SAP sicuro o il failover del database.

</details>

## 5. HANA ha molto spazio libero, ma gli acquisti rallentano durante i savepoint. Il gruppo deve soltanto aggiungere capacità disco?

<details>
<summary>Risposta</summary>

Indaga velocità di trasferimento di dati e log, latenza, code e limite aggregato di I/O della VM. Il traffico dei savepoint può contendere risorse alle scritture dei log anche con molto spazio libero. Esamina organizzazione dell'archiviazione supportata, filesystem, configurazione dei dischi, domanda del volume condiviso e tempi del carico prima di scegliere una modifica. Cache e Write Accelerator devono seguire le indicazioni esatte per volume e archiviazione, non una ricetta universale di prestazioni. Le prove sono una sequenza temporale correlata di carico e I/O più una configurazione supportata proposta. Etichetta le misure come prove richieste finché un test autorizzato non le fornisce davvero.

</details>

## 6. Un cluster non riesce a isolare con fencing il nodo pari dopo un guasto di comunicazione. Disabilitare il fencing ripristinerebbe un servizio sicuro?

<details>
<summary>Risposta</summary>

No. Rimuovere il fencing può consentire primari in conflitto e danneggiare l'integrità dei dati. Preserva le prove e segui la procedura di incidente indagando quorum, comunicazione tra nodi, permessi e connettività del fence agent oppure configurazione SBD supportata scelta. Conferma che il nodo ritenuto guasto non possa continuare a scrivere indipendentemente prima del subentro. Le prove devono includere stato del cluster, timestamp, risultati del fencing, stato della replica e un primario autorevole identificato. Il progetto correttivo ripristina isolamento e decisioni supportati. Far apparire avviate le risorse del cluster non basta a dimostrare che il servizio SAP accetti scritture in sicurezza.

</details>

## 7. Un aggiornamento finanziario sbagliato ha raggiunto entrambe le repliche HANA. Perché il backup protetto di ieri potrebbe ancora contare?

<details>
<summary>Risposta</summary>

La replica preserva la disponibilità ma può copiare errori logici. Un backup protetto e una catena di log utilizzabile possono supportare il recupero a un punto accettabile prima dell'errore, secondo il processo di ripristino supportato scelto. Stabilisci RPO approvato dai responsabili organizzativi, dipendenze di ripristino, conservazione ed eventuali transazioni legittime successive da riconciliare. Conferma la coerenza applicativa; uno snapshot generico della VM non è automaticamente sufficiente. Le prove devono includere scelta del punto di recupero, disponibilità di backup e log, piano di ripristino isolato, controlli del database e convalida operativa. La sola replica riuscita non può recuperare la correttezza storica dopo che entrambe le copie ricevono la stessa modifica sbagliata.

</details>

## 8. Il passaggio supera i controlli di base, poi gli utenti inseriscono nuovi ordini di acquisto. Per tornare indietro basta ripuntare il DNS alla fonte invariata?

<details>
<summary>Risposta</summary>

Così si abbandonerebbero o biforcherebbero le nuove transazioni. La procedura richiede una decisione separata quando iniziano le scritture sulla destinazione: bloccare di nuovo le scritture, identificare l'insieme di dati autorevole, preservare le nuove transazioni e valutare riconciliazione o migrazione inversa supportate. Includi approvazione organizzativa, code delle interfacce, sincronizzazione finale, isolamento della fonte e convalida prima di riaprire uno dei lati. Le prove sono una sequenza temporale della titolarità delle scritture e una decisione documentata sul trattamento dei dati, non soltanto istruzioni DNS. La simulazione deve distinguere ritorno prima della riapertura delle scritture e recupero successivo, con scadenze chiare e operatori responsabili di ogni punto di controllo.

</details>

## 9. Il portale della ricerca non raggiunge SAP RISE. Il suo operatore deve modificare NSG nella sottoscrizione SAP usando il ruolo Azure dell'università?

<details>
<summary>Risposta</summary>

Rispetta prima la matrice contrattuale delle responsabilità. SAP gestisce l'ambiente RISE nel proprio ambiente Azure; un ruolo della sottoscrizione universitaria non concede controllo su quelle risorse. Traccia DNS, route, peering o connettività, regole firewall, identità e interfaccia SAP concordata del portale, assegnando ogni verifica al responsabile corretto. Coordina cambiamenti lato SAP ed escalation tramite SAP. Le prove devono includere punto di passaggio guasto e responsabilità delle due parti. RISE non elimina la responsabilità del cliente per i propri servizi di integrazione, la configurazione di sicurezza o il percorso di rete verso un'interfaccia disponibile.

</details>

## 10. L'area DR ha una copia aggiornata del database e VM in esecuzione, ma gli acquisti restano indisponibili. Che altro deve convalidare la simulazione a tavolino?

<details>
<summary>Risposta</summary>

Convalida servizi centrali, ordine di avvio applicativo, identità, DNS, nomi virtuali, route, segreti, file condivisi, endpoint di integrazione e capacità supportata sufficiente. Confronta punto di recupero utilizzabile e tempo di ripristino previsto con RPO e RTO organizzativi. Impedisci al primario originale di accettare scritture indipendenti. Definisci un flusso di acquisto riuscito e uno scambio di interfaccia come controlli di accettazione, seguiti da un piano controllato di ritorno al primario. Le prove devono includere responsabili, ordine delle dipendenze, stato della replica, tempi previsti e criteri di convalida. Infrastruttura in esecuzione è soltanto una parte del ripristino di un servizio SAP universitario completo.

</details>

Date degli obiettivi e sei riferimenti tecnici principali sono nella [guida](AZ-120.md). Sviluppa diagrammi e procedure operative revisionabili nel [quaderno di esercizi](AZ-120-workbook.md).
