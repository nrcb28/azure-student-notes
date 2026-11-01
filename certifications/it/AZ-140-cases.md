# AZ-140 · 10 casi con risposte motivate

[Guida](AZ-140.md) · [Quaderno di esercizi](AZ-140-workbook.md) · [Indice](README.md)

Scenari originali di laboratorio universitario, non domande ufficiali d'esame. Spiega il requisito e le prove che lo confermano prima di aprire ogni risposta. Tutti i risultati seguenti sono ragionamenti di progettazione; non si dichiara alcuna distribuzione cloud.

## 1. Quaranta studenti richiedono desktop intercambiabili, mentre un ricercatore richiede sempre la stessa macchina dedicata. Tutti devono ricevere un pool personale?

<details>
<summary>Risposta</summary>

Valuta un pool di host condiviso con sistema operativo multisessione supportato per gli studenti e un'assegnazione personale per il ricercatore. Macchine dedicate a tutti potrebbero consumare capacità inutile, mentre forzare il ricercatore in un pool intercambiabile potrebbe violare il requisito. L'assegnazione personale richiede comunque il diritto appropriato sulla risorsa pubblicata. Documenta misure del carico, verifiche delle licenze, ipotesi sulla densità degli host e requisito di persistenza del ricercatore. Un insieme di prove adeguato include modello di assegnazione e calcolo della capacità, oltre al solo numero di VM.

</details>

## 2. Uno studente ha Azure Contributor e vede le VM nel portale, ma il suo feed AVD è vuoto. Che cosa devi esaminare?

<details>
<summary>Risposta</summary>

Esamina identità dello studente e assegnazione al gruppo di applicazioni, associazione del gruppo con il pool di host previsto e sua registrazione nell'area di lavoro. L'accesso di gestione alle risorse VM non pubblica un desktop per quell'utente. Verifica anche che il client sottoscriva l'area di lavoro corretta usando l'account previsto. Annota appartenenza ai gruppi, diritto effettivo sulla risorsa e diagnostica del feed con timestamp. Aprire una porta in ingresso della VM o assegnare Owner della sottoscrizione non spiegherebbe né correggerebbe la relazione di pubblicazione mancante.

</details>

## 3. Il progetto vuole host aggiunti a Entra, ma una vecchia app richiede servizi di dominio. Entra ID sostituisce automaticamente AD DS?

<details>
<summary>Risposta</summary>

No. Separa i requisiti esatti di autenticazione e directory dell'applicazione dall'autenticazione del feed AVD. Microsoft Entra ID, AD DS e Microsoft Entra Domain Services offrono capacità diverse, e scegliere un tipo di join per l'host non elimina le dipendenze dell'applicazione. Verifica combinazioni di identità supportate, autenticazione per l'archiviazione dei profili, gestione dei criteri e requisiti SSO prima di scegliere un progetto. Le prove devono includere un inventario delle dipendenze applicative e un flusso di autenticazione supportato. Un criterio Conditional Access da solo non può fornire un protocollo di dominio mancante o la raggiungibilità del controller di dominio.

</details>

## 4. Il team firewall propone TCP 3389 pubblico per riparare ogni connessione AVD. La connessione inversa richiede questa modifica?

<details>
<summary>Risposta</summary>

No. La connessione inversa AVD di base dipende dalla connettività in uscita ai servizi da client e host di sessione tramite HTTPS/TCP. Esamina destinazioni richieste, DNS, TLS, comportamento del proxy, stato dell'agente e fase in cui la connessione fallisce. Shortpath è una scelta di trasporto UDP separata con prerequisiti specifici per opzione, non un motivo per esporre RDP pubblico. Per un progetto con listener per reti gestite, documenta raggiungibilità privata e porta UDP del listener scelta. Le prove devono identificare la dipendenza effettivamente bloccata e una proposta di correzione circoscritta.

</details>

## 5. I client del campus usano UDP, ma quelli domestici ripiegano su TCP. Dimostra che l'host di sessione non funziona?

<details>
<summary>Risposta</summary>

No. Confronta client, reti e opzioni Shortpath selezionate. Una VPN del campus potrebbe fornire raggiungibilità privata diretta, mentre un NAT o firewall domestico impedisce uno specifico percorso UDP. Verifica versioni client supportate, criteri UDP, raggiungibilità STUN/TURN, disponibilità nel cloud e trasporto negoziato. Il ripiego sulla connessione inversa può mantenere la sessione con prestazioni diverse. Documenta timestamp, tempo di andata e ritorno, perdita di pacchetti e osservazioni su percorsi riusciti e falliti. Non assumere che il listener gestito UDP 3390 sia necessario per ogni connessione Shortpath su rete pubblica.

</details>

## 6. Gli studenti si autenticano ma ricevono profili temporanei dopo una modifica dell'identità SMB. Ricreare tutte le VM risolverebbe la causa?

<details>
<summary>Risposta</summary>

Esamina prima i log di collegamento FSLogix e il percorso di autenticazione dell'archiviazione. Verifica posizione prevista del contenitore, risoluzione DNS, permessi a livello di condivisione, permessi NTFS, configurazione Kerberos supportata e compatibilità della crittografia. Autenticazione del feed e accesso ai file del profilo sono fasi separate. Ricreare gli host senza correggere una dipendenza di archiviazione condivisa potrebbe riprodurre lo stesso errore ovunque. Conserva i contenitori interessati e indaga sessioni o blocchi esistenti prima delle azioni di recupero. Le prove devono mostrare l'errore esatto di collegamento e un'operazione consentita sul profilo usando l'identità utente prevista.

</details>

## 7. Lo stesso studente apre due sessioni indipendenti e la seconda non riesce a collegare il contenitore del profilo. Un operatore deve eliminare subito il blocco?

<details>
<summary>Risposta</summary>

Non trattare il blocco come una prova eliminabile senza conseguenze. La configurazione standard dei profili FSLogix supporta una sola connessione a un contenitore; le configurazioni concorrenti hanno requisiti aggiuntivi e limiti applicativi. Identifica sessioni attive e disconnesse, host proprietario e stato effettivo del blocco prima di decidere se una risorsa obsoleta richieda recupero. Coordina una disconnessione controllata e proteggi il lavoro non salvato. Annota timestamp e log di collegamento. Un progetto che richiede sessioni concorrenti necessita di configurazione esplicita supportata e convalida, anziché scritture simultanee senza restrizioni nello stesso contenitore.

</details>

## 8. L'editor di appunti compare in un gruppo RemoteApp ma non funziona su metà degli host. Pubblicare l'icona installa l'applicazione?

<details>
<summary>Risposta</summary>

Pubblicare una RemoteApp controlla accesso e presentazione; non dimostra che ogni host di sessione idoneo possa eseguire l'applicazione. Confronta versioni dell'immagine, dipendenze installate e metodo di distribuzione scelto. Per App Attach, esamina compatibilità del pacchetto, accesso all'archiviazione, assegnazioni a pool di host e utenti e prove di registrazione. Prova lo stesso utente su un host noto funzionante e su uno interessato senza modificare assegnazioni di produzione. La consegna deve spiegare la differenza e proporre una correzione graduale del pacchetto o dell'immagine con un ripiego funzionante.

</details>

## 9. Arrivano insieme quarantotto studenti. Ogni host supporta dodici sessioni e deve essere tollerato il guasto di un host. Bastano quattro host più Start VM on Connect?

<details>
<summary>Risposta</summary>

Quattro host integri forniscono esattamente 48 sessioni nell'ipotesi misurata, senza margine per il guasto di un host. Cinque host disponibili offrono 48 sessioni dopo averne perso uno. Start VM on Connect non garantisce che gli host di riserva siano integri e pronti prima dell'arrivo simultaneo di una classe. Modella tempo di avvio, massimo di sessioni, bilanciamento del carico, pianificazioni di scalabilità, esclusioni drain e capacità dell'archiviazione dei profili. Le prove sono una tabella di capacità per funzionamento normale e degradato e i tempi di avvio previsti. Convalida l'ipotesi sulla densità con carichi rappresentativi prima di usarla operativamente.

</details>

## 10. Un'area geografica sostitutiva ha VM, ma gli studenti non riescono a recuperare il proprio ambiente di lavoro. Che cosa manca alla dichiarazione di recupero?

<details>
<summary>Risposta</summary>

Un inventario di VM da solo non dimostra il recupero dei desktop. Segui disponibilità di identità e DNS, pubblicazione delle risorse, distribuzione applicativa, percorsi di rete, accesso e coerenza dell'archiviazione dei profili e API degli appunti. Specifica separatamente obiettivi di recupero dei profili e dei dati applicativi. Usa un ID di correlazione della connessione, diagnostica, eventi host e log FSLogix per trovare la prima fase fallita. La simulazione deve assegnare operatori, ipotesi sulla capacità, passi di ritorno all'area primaria e un flusso studente riuscito come prova di accettazione. Etichetta questi elementi come controlli pianificati finché un'esercitazione di recupero autorizzata non produce osservazioni effettive.

</details>

Riferimenti tecnici, date degli obiettivi e limiti di ambito sono nella [guida](AZ-140.md). Trasforma il ragionamento in diagrammi e prove con il [quaderno di esercizi](AZ-140-workbook.md).
