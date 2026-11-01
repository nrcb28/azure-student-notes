# AZ-120 · Quaderno avanzato comune

[Guida](AZ-120.md) · [10 casi](AZ-120-cases.md) · [Indice](README.md)

Cinque unità corrispondenti tra le lingue. Lavora offline sull'ambiente SAP di acquisti e finanza dell'università immaginaria e sulla sua integrazione con il portale della ricerca. Non vengono forniti o dichiarati licenza, distribuzione Azure, esecuzione SAP o preparazione alla produzione. Distingui ipotesi e risultati previsti dalle prove osservate.

<a id="az-120-unit-1"></a>

## 1. Inventariare responsabilità e capacità supportata

Disegna SID di produzione e non produzione, server applicativi, ASCS/ERS o SCS, HANA, file condivisi, identità, DNS e interfacce. Assegna responsabili di infrastruttura, sistema operativo, Basis, database, sicurezza e convalida operativa. Spiega perché server applicativi ridondanti lasciano altri punti singoli di guasto. Costruisci un foglio di dimensionamento per SAPS pertinenti, memoria, crescita, velocità di trasferimento, latenza e margine in caso di guasto; lascia la scelta dello SKU subordinata ai controlli di certificazione e compatibilità.

**Scenario:** una VM più economica ha lo stesso numero di core ma non presenta prove registrate del supporto HANA. **Prove:** mappa delle dipendenze, combinazione VM/sistema operativo/database/archiviazione supportata, ipotesi sulle quote regionali e responsabile della revisione delle licenze. **Consegna:** una decisione architetturale che spieghi criteri di accettazione e misure ancora irrisolte. Rivedi i [fondamenti di calcolo](../../it/03-compute.md).

<a id="az-120-unit-2"></a>

## 2. Progettare posizionamento, rete e archiviazione HANA

Disegna percorsi supportati tra applicazione e database, amministrazione, replica, backup, connettività del campus e inoltro DNS. Separa connettività privata ExpressRoute e controlli crittografici scelti. Confronta isolamento delle zone e vincoli di vicinanza dei PPG usando ipotesi esplicite di latenza. Pianifica `/hana/data`, `/hana/log` e `/hana/shared`, filesystem supportati, limiti I/O di dischi e VM e decisioni su cache o Write Accelerator specifiche della configurazione.

**Scenario:** un savepoint coincide con acquisti lenti e una proposta colloca un'appliance di ispezione tra livelli applicativi e database SAP. **Prove:** percorsi del traffico, diagramma di posizionamento, budget previsto di latenza, tabella dei ruoli dei volumi e osservazioni I/O richieste. **Consegna:** un'alternativa supportata con compromessi di capacità e domini di guasto. Rivedi i [fondamenti di rete](../../it/05-networking.md).

<a id="az-120-unit-3"></a>

## 3. Separare failover sicuro e recupero storico

Spiega HANA System Replication, controllo supportato del cluster, protezione ASCS/SCS, ERS, quorum, fencing, nomi virtuali e probe del bilanciatore di carico. Disegna l'unico nodo autorizzato a scrivere dopo una partizione di rete. Definisci RPO e RTO organizzativi, backup coerenti con il carico, log utilizzabili, conservazione e dipendenze di ripristino. Mostra perché la replica può copiare un errore e perché uno snapshot non coordinato non dimostra coerenza applicativa.

**Scenario:** non si riesce a isolare con fencing il nodo pari e un errore finanziario è già stato replicato. **Prove:** decisioni previste del cluster, dipendenze del fencing, regola della copia autorevole, disponibilità di backup/log e criteri di convalida del ripristino. **Consegna:** procedure HA e di ripristino separate, che rifiutino esplicitamente la disabilitazione del fencing come riparazione e includano riconciliazione operativa dopo il recupero storico.

<a id="az-120-unit-4"></a>

## 4. Scrivere una procedura di migrazione e integrazione

Valuta supporto della fonte, versioni, interfacce, tasso di modifica, durata del trasferimento, inattività e compatibilità della destinazione. Scegli un approccio di migrazione supportato con motivazioni. Definisci simulazione, blocco delle scritture, sincronizzazione finale, isolamento della fonte, cambiamenti DNS e delle interfacce, verifiche tecniche, accettazione operativa e riapertura delle scritture. Per RISE, assegna responsabilità di integrazione del cliente e gestione SAP usando il contratto invece di presumere accesso alla sottoscrizione.

**Scenario:** gli utenti creano ordini di acquisto dopo il passaggio, poi il portale della ricerca smette di funzionare. **Prove:** sequenza temporale della titolarità delle scritture, stato delle code, punti di passaggio delle interfacce, punti di convalida e responsabili delle decisioni. **Consegna:** ritorno prima di nuove scritture e una decisione distinta di riconciliazione o migrazione inversa dopo le scritture, compresa escalation SAP quando il confine guasto appartiene a RISE.

<a id="az-120-unit-5"></a>

## 5. Esaminare le operazioni e simulare il recupero regionale

Esamina una modifica IaC immaginaria rispetto a supporto delle immagini, posizionamento, archiviazione, riferimenti ai segreti, dipendenze e differenze distruttive. Distribuisci gli aggiornamenti per fasi con ordine consapevole del cluster e criteri di ripristino. Specifica raccolta di Azure Monitor, provider del monitoraggio SAP, prove di database e cluster, responsabili degli avvisi e conservazione. Recupera l'intero servizio in un'area alternativa, compresi identità, rete, servizi centrali, app, dati, integrazioni e sincronizzazione per il ritorno al primario.

**Scenario:** un'interruzione regionale avviene durante gli acquisti mentre è in sospeso una proposta di ridimensionamento. **Prove:** ordine delle dipendenze, RPO/RTO previsti, capacità in caso di guasto, stato della replica, controlli del flusso operativo e responsabili dei costi ricorrenti di calcolo/archiviazione/rete/monitoraggio. **Consegna:** una simulazione a tavolino dell'incidente e un registro di revisione della modifica che distingua controlli pianificati e test eseguiti.

Usa i sei riferimenti tecnici nella [guida](AZ-120.md) per mettere alla prova le ipotesi. Questi esercizi originali selezionano concetti utili; non coprono ogni obiettivo ufficiale e non garantiscono un risultato d'esame.
