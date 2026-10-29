# Otto scenari per esercitarsi

[←](19-mini-quiz.md) · [CLI](../QUIZ.md)

È un breve esercizio: non è un esame ufficiale o completo e il risultato non prevede il superamento dell’esame.

<a id="quiz-q01"></a>

## AZ-900 · Controllo del sistema operativo

Un’applicazione di laboratorio deve installare un proprio driver del kernel Linux. Quale soluzione di hosting soddisfa meglio questo requisito?

- **A.** Eseguire l’applicazione in Microsoft 365.
- **B.** Usare una macchina virtuale Azure con un’immagine Linux compatibile.
- **C.** Distribuirla in un runtime gestito di App Service.
- **D.** Inserire il driver in una Azure Function standard.

<details>
<summary>Perché:</summary>

**B. Usare una macchina virtuale Azure con un’immagine Linux compatibile.**

Il requisito decisivo è il controllo del sistema operativo guest. Una VM Azure compatibile permette al team di gestire quell’ambiente e i relativi driver, ma lascia al team anche la manutenzione del sistema. Una piattaforma applicativa gestita non è adatta se non offre il controllo del kernel richiesto.

- **A.** Microsoft 365 offre software pronto all’uso, non un ambiente per driver del kernel arbitrari.
- **C.** Un runtime gestito di App Service non consente l’amministrazione necessaria del kernel guest.
- **D.** Una Function standard non concede il controllo necessario per installare quel driver.

[Fonte:](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) · [Da ripassare:](03-compute.md)

</details>

<a id="quiz-q02"></a>

## AZ-900 · Scalabilità orizzontale e sessioni

Un’API di appunti aggiunge istanze dietro un bilanciatore di carico. Ogni istanza può essere sostituita, ma gli utenti devono conservare le sessioni. Ora le sessioni esistono solo nella memoria di ogni istanza. Che cosa va cambiato?

- **A.** Aumentare la CPU di tutte le istanze.
- **B.** Lasciare le sessioni in memoria e attivare soltanto l’affinità di sessione.
- **C.** Spostare lo stato delle sessioni in un archivio esterno condiviso adatto.
- **D.** Assegnare un indirizzo IP pubblico a ogni istanza.

<details>
<summary>Perché:</summary>

**C. Spostare lo stato delle sessioni in un archivio esterno condiviso adatto.**

La scalabilità orizzontale distribuisce le richieste tra istanze: lo stato importante di una sessione non può dipendere solo dalla memoria di una di esse. Un archivio esterno adatto permette alle istanze sostitutive di recuperarlo. La sola affinità non conserva la memoria quando l’istanza scompare. L’applicazione deve anche gestire l’accesso all’archivio e i suoi possibili guasti.

- **A.** Più CPU non conserva la memoria quando l’istanza viene sostituita.
- **B.** Anche con l’affinità, la sessione va persa se l’istanza scelta scompare.
- **D.** Un IP pubblico non fornisce uno stato di sessione condiviso o durevole.

[Fonte:](https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/scale-out) · [Da ripassare:](01-fundamentals.md)

</details>

<a id="quiz-q03"></a>

## AZ-104 · Accesso ai dati di archiviazione

Un utente ha Contributor su un account di archiviazione. Una richiesta Blob con la sua identità Entra raggiunge il servizio, ma viene rifiutata perché mancano i permessi sui dati. Deve soltanto leggere i blob di un contenitore. Quale soluzione rispetta il privilegio minimo?

- **A.** Assegnare Storage Blob Data Reader nell’ambito di quel contenitore.
- **B.** Assegnare Owner sull’intera sottoscrizione.
- **C.** Aprire tutte le porte di rete in ingresso.
- **D.** Consegnare all’utente la chiave dell’account di archiviazione.

<details>
<summary>Perché:</summary>

**A. Assegnare Storage Blob Data Reader nell’ambito di quel contenitore.**

I permessi di gestione e quelli sui dati Blob sono distinti. Storage Blob Data Reader consente la lettura richiesta, mentre l’ambito del contenitore limita la concessione alla necessità indicata. Il caso identifica già un problema di autorizzazione sui dati: concedere ampi diritti amministrativi o modificare la rete non sarebbe una risposta proporzionata.

- **B.** Owner sulla sottoscrizione supera il requisito di lettura di un solo contenitore.
- **C.** Aprire porte non fornisce l’autorizzazione mancante sui dati.
- **D.** Una chiave dell’account concede un accesso molto più ampio del necessario.

[Fonte:](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access) · [Da ripassare:](06-identity.md)

</details>

<a id="quiz-q04"></a>

## AZ-104 · Ereditarietà dei permessi RBAC

Un utente ha Reader direttamente su una VM e appartiene anche a un gruppo con Reader nell’ambito della sottoscrizione. Rimuovi solo l’assegnazione diretta sulla VM. L’utente può ancora leggerla. Perché?

- **A.** Azure assegna automaticamente Reader su tutte le VM a ogni utente.
- **B.** Un tag del gruppo di risorse ripristina l’assegnazione eliminata.
- **C.** Per rimuovere un ruolo bisogna sempre eliminare la VM.
- **D.** L’assegnazione del gruppo continua a concedere accesso ereditato.

<details>
<summary>Perché:</summary>

**D. L’assegnazione del gruppo continua a concedere accesso ereditato.**

Rimuovere un’assegnazione non elimina i permessi ottenuti tramite un’altra. Il gruppo ha Reader sulla sottoscrizione, quindi i suoi membri possono ereditare quell’accesso alla VM. Controlla assegnazioni dirette, appartenenza ai gruppi e ambiti superiori prima di considerare l’accesso residuo un errore del servizio o aggiungere altri permessi.

- **A.** Non esiste una concessione universale di Reader a ogni utente.
- **B.** I tag classificano le risorse e non ricreano le assegnazioni di ruolo.
- **C.** Rimuovere un ruolo non richiede l’eliminazione della risorsa protetta.

[Fonte:](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview) · [Da ripassare:](06-identity.md)

</details>

<a id="quiz-q05"></a>

## AZ-305 · Obiettivi di ripristino

Un progetto conserva punti validi di ripristino del database soltanto una volta ogni 24 ore. L’azienda ora accetta di perdere al massimo un’ora di dati recenti dopo un disastro. Quale modifica risolve direttamente questa lacuna?

- **A.** Aumentare la CPU del server API.
- **B.** Prevedere punti di protezione dei dati recuperabili distanti al massimo un’ora e verificare il ripristino.
- **C.** Aggiungere un budget con avvisi sui costi.
- **D.** Rinominare il gruppo di risorse in production.

<details>
<summary>Perché:</summary>

**B. Prevedere punti di protezione dei dati recuperabili distanti al massimo un’ora e verificare il ripristino.**

L’RPO esprime in tempo la quantità di dati recenti che si può perdere. I soli punti giornalieri non bastano per un obiettivo di un’ora. Il progetto deve produrre stati recuperabili con frequenza adeguata e verificarne il ripristino. Più potenza di calcolo o etichette dei costi non cambiano l’età dei dati disponibili per recuperare.

- **A.** La CPU dell’API non aumenta la frequenza di protezione dei dati.
- **C.** Un budget segnala la spesa, non la perdita di dati.
- **D.** Il nome del gruppo di risorse non cambia la frequenza dei punti di ripristino.

[Fonte:](https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery) · [Da ripassare:](10-architecture.md)

</details>

<a id="quiz-q06"></a>

## AZ-305 · DNS per le connessioni private

L’accesso pubblico a un servizio di archiviazione è disabilitato ed esiste un endpoint privato. Il client continua a risolvere il nome del servizio nel suo IP pubblico. Il percorso di rete privato è disponibile. Che cosa controlli per prima cosa?

- **A.** Assegnare al client Owner sulla sottoscrizione.
- **B.** Impostare in modo permanente l’IP pubblico nella configurazione.
- **C.** Le zone DNS private, i collegamenti e l’inoltro usati da quel client.
- **D.** Aumentare senza limiti i tentativi dell’applicazione.

<details>
<summary>Perché:</summary>

**C. Le zone DNS private, i collegamenti e l’inoltro usati da quel client.**

Il client risolve una destinazione sbagliata per la connessione privata prevista. Controlla la configurazione DNS privata consigliata per il servizio e come il client la raggiunge, inclusi collegamenti e inoltro. Continua a usare il nome del servizio. Correggere il DNS non concede da solo i permessi sui dati, ma privilegi aggiuntivi e tentativi infiniti non risolvono questa discrepanza.

- **A.** Owner non cambia la risoluzione dei nomi del client.
- **B.** L’indirizzo pubblico è la destinazione sbagliata quando l’accesso pubblico è disabilitato.
- **D.** Ripetere una richiesta non corregge una configurazione DNS errata.

[Fonte:](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) · [Da ripassare:](05-networking.md)

</details>

<a id="quiz-q07"></a>

## AZ-400 · Promozione dell’artefatto testato

Una pipeline testa un’immagine di container e poi ricompila dal sorgente per la produzione usando dipendenze che possono cambiare. Come assicurarsi che in produzione arrivi l’immagine che ha superato i test?

- **A.** Ripetere i test solo sui commenti del codice.
- **B.** Usare il tag latest senza registrare a quale immagine punta.
- **C.** Saltare i test perché il commit del sorgente non è cambiato.
- **D.** Promuovere la stessa immagine già testata, identificata da un digest immutabile.

<details>
<summary>Perché:</summary>

**D. Promuovere la stessa immagine già testata, identificata da un digest immutabile.**

Lo stesso commit può generare risultati diversi se cambiano strumenti, dipendenze o immagini di base. Promuovere l’immagine già testata evita questa differenza dovuta alla ricompilazione. Un digest immutabile identifica l’artefatto effettivo, mentre un tag può cambiare destinazione. La configurazione degli ambienti richiede comunque una propria validazione e una gestione controllata.

- **A.** I commenti del codice non identificano l’artefatto compilato.
- **B.** Un tag modificabile può in seguito puntare a un’altra immagine.
- **C.** Un commit invariato non dimostra che la nuova compilazione produca un risultato identico.

[Fonte:](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-concepts) · [Da ripassare:](12-devops.md)

</details>

<a id="quiz-q08"></a>

## AZ-400 · Segnali di un rilascio canary

Una versione canary mostra CPU e memoria normali, ma i download dei documenti restituiscono file sbagliati. Su che cosa dovrebbe basarsi la decisione di proseguire il rilascio?

- **A.** Su segnali di correttezza funzionale e un criterio definito per fermare o annullare il rilascio.
- **B.** Solo sulla CPU, perché un’infrastruttura sana dimostra che i risultati sono corretti.
- **C.** Su una VM più grande prima di controllare i file restituiti.
- **D.** Sull’eliminazione dei vecchi log per rendere più pulita la dashboard.

<details>
<summary>Perché:</summary>

**A. Su segnali di correttezza funzionale e un criterio definito per fermare o annullare il rilascio.**

Una versione può usare poche risorse e produrre comunque risultati sbagliati. Per promuoverla servono segnali legati all’operazione dell’utente, oltre alle metriche infrastrutturali. Un criterio definito di arresto o rollback permette di agire su queste evidenze. Verifica anche la compatibilità dei dati: ripristinare il codice precedente non annulla automaticamente le modifiche dannose ai dati introdotte dalla versione.

- **B.** CPU e memoria non dimostrano che gli utenti ricevano i documenti corretti.
- **C.** Più potenza di calcolo non corregge automaticamente un risultato applicativo errato.
- **D.** Eliminare le evidenze rende l’indagine più difficile e non corregge i risultati.

[Fonte:](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments) · [Da ripassare:](12-devops.md)

</details>
