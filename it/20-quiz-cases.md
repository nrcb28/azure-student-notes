# 32 scenari per esercitarsi

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

<a id="quiz-q09"></a>

## DP-900 · Carichi di lavoro transazionali

Un servizio universitario di iscrizione deve riservare l’ultimo posto disponibile in laboratorio e creare l’iscrizione dello studente come un’unica operazione coerente. Quale descrizione del carico di lavoro corrisponde meglio al requisito?

- **A.** Un carico analitico che aggrega le iscrizioni per semestre.
- **B.** Un carico batch che riconcilia ogni notte aggiornamenti indipendenti dei posti.
- **C.** Un carico transazionale che esegue il commit delle modifiche correlate insieme.
- **D.** Un carico di streaming che pubblica eventi separati per posto e iscrizione senza coordinarne i commit.

<details>
<summary>Perché:</summary>

**C. Un carico transazionale che esegue il commit delle modifiche correlate insieme.**

Il requisito riguarda un’operazione piccola e mirata, le cui modifiche correlate devono riuscire o fallire insieme. Questo è un comportamento transazionale: un’altra richiesta non deve poter riservare lo stesso ultimo posto mentre i dati di iscrizione e capienza non concordano. La reportistica storica è un’attività analitica con modalità di accesso diverse. Eventi e riconciliazione successiva possono contribuire a un’architettura più ampia, ma aggiornamenti indipendenti, da soli, non soddisfano il requisito di coerenza indicato.

- **A.** L’aggregazione per semestre risponde a domande storiche; non coordina la prenotazione del posto e le modifiche all’iscrizione necessarie per questa richiesta in tempo reale.
- **B.** La riconciliazione notturna lascia un intervallo in cui il numero di posti e l’iscrizione possono non concordare, contro il requisito di coerenza immediata.
- **D.** La pubblicazione di eventi può informare altri sistemi, ma eventi con commit separati non rendono di per sé atomiche le due modifiche di origine.

[Fonte:](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing) · [Da ripassare:](../certifications/it/DP-900.md)

</details>

<a id="quiz-q10"></a>

## DP-900 · Ordine di ETL ed ELT

Un gruppo di ricerca estrae i record dei download di ieri, elimina gli identificatori non validi in un servizio di elaborazione e carica i record ripuliti nel warehouse di reportistica. Quale descrizione corrisponde a questo ordine?

- **A.** ETL, perché la trasformazione avviene prima del caricamento nella destinazione di reportistica.
- **B.** ELT, perché qualsiasi flusso che termina in un warehouse esegue la trasformazione al suo interno.
- **C.** Streaming, perché i record dei download provengono in origine da eventi applicativi.
- **D.** Solo orchestrazione, perché coordinare i passaggi elimina la necessità della trasformazione.

<details>
<summary>Perché:</summary>

**A. ETL, perché la trasformazione avviene prima del caricamento nella destinazione di reportistica.**

ETL significa estrarre, trasformare e poi caricare nella destinazione prevista. Qui gli identificatori non validi vengono gestiti prima che il warehouse di reportistica riceva i record ripuliti. Con ELT i dati verrebbero prima caricati, per poi usare le capacità di elaborazione della destinazione per trasformarli. La raccolta delimitata dei record di ieri è un input batch. Un orchestratore può coordinare queste attività, ma orchestrazione e trasformazione descrivono responsabilità diverse nella stessa pipeline.

- **B.** ELT richiede il caricamento prima della trasformazione nella destinazione; scegliere un warehouse come destinazione non determina di per sé quell’ordine.
- **C.** L’origine in eventi non rende streaming l’elaborazione successiva: questo processo gestisce una raccolta giornaliera delimitata, non record in arrivo continuo.
- **D.** L’orchestrazione coordina dipendenze e ripristino, mentre eliminare gli identificatori non validi modifica i dati e rimane una responsabilità distinta di trasformazione.

[Fonte:](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl) · [Da ripassare:](../certifications/it/DP-900.md)

</details>

<a id="quiz-q11"></a>

## SC-900 · Categorie dei fattori MFA

Uno studente confronta diverse soluzioni di accesso. Quale esempio combina un fattore di conoscenza con un fattore di possesso, supponendo che il dispositivo di autenticazione sia registrato e che l’approvazione sia obbligatoria?

- **A.** Una password seguita da una risposta memorizzata a una domanda di sicurezza.
- **B.** Una password universitaria seguita da una diversa password di servizio memorizzata.
- **C.** Una password seguita da un PIN memorizzato digitato nello stesso sito, senza un autenticatore associato al dispositivo.
- **D.** Una password seguita dall’approvazione tramite il dispositivo di autenticazione registrato dello studente.

<details>
<summary>Perché:</summary>

**D. Una password seguita dall’approvazione tramite il dispositivo di autenticazione registrato dello studente.**

La password rappresenta qualcosa che lo studente conosce, mentre il controllo di un dispositivo di autenticazione registrato fornisce un fattore di possesso. Richiederli entrambi combina quindi categorie di fattori diverse. Due segreti memorizzati rimangono fattori di conoscenza anche se le stringhe sono diverse. Questa classificazione non rende tutti i metodi MFA ugualmente resistenti al phishing: la politica di accesso dell’università deve considerare anche scelta del metodo, registrazione, recupero e applicazione effettiva dei controlli.

- **A.** Sia la password sia la risposta memorizzata sono fattori di conoscenza; un’ulteriore verifica di conoscenza non introduce il fattore di possesso richiesto.
- **B.** Password diverse possono separare le credenziali, ma sono entrambe segreti memorizzati e appartengono quindi alla stessa categoria di fattori.
- **C.** La domanda esclude un autenticatore associato al dispositivo: un PIN inserito come ulteriore segreto nel sito dimostra conoscenza, non possesso del dispositivo.

[Fonte:](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks) · [Da ripassare:](../certifications/it/SC-900.md)

</details>

<a id="quiz-q12"></a>

## SC-900 · Gestione dei dati con Purview

Un’università deve rilevare identificativi degli studenti nelle attività di condivisione di documenti supportate e avvisare o limitare la condivisione esterna quando viene soddisfatta una regola configurata. Quale funzionalità di Purview risponde più direttamente a questo requisito?

- **A.** Audit, usato solo per registrare l’avvenuta attività di condivisione.
- **B.** Prevenzione della perdita dei dati (DLP) con criteri dall’ambito adeguato e verificati.
- **C.** Conservazione, configurata per mantenere i documenti per sette anni.
- **D.** Un’etichetta di riservatezza chiamata Riservato, senza configurazione di protezione o DLP.

<details>
<summary>Perché:</summary>

**B. Prevenzione della perdita dei dati (DLP) con criteri dall’ambito adeguato e verificati.**

DLP valuta le informazioni sensibili e le attività corrispondenti rispetto ai criteri configurati e può avvisare o limitare le azioni supportate. Il progetto deve comunque specificare posizioni, condizioni di rilevamento, destinatari, eccezioni e risposta prevista. Audit fornisce evidenze delle attività, la conservazione gestisce il ciclo di vita dei contenuti e un’etichetta comunica la classificazione o applica la protezione configurata. Il solo nome di un’etichetta non stabilisce la limitazione alla condivisione esterna descritta nello scenario.

- **A.** Audit supporta le indagini registrando le attività; registrare una condivisione non fornisce di per sé l’avviso o la limitazione richiesti dai criteri.
- **C.** Conservare un documento per un periodo definito ne governa il ciclo di vita, ma non determina se questa attività di condivisione esterna debba essere consentita.
- **D.** Il solo nome di un’etichetta non configura alcuna limitazione alla condivisione; il comportamento previsto deve essere implementato dalla protezione o da criteri DLP adatti.

[Fonte:](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) · [Da ripassare:](../certifications/it/SC-900.md)

</details>

<a id="quiz-q13"></a>

## AZ-700 · Routing con il prefisso più lungo

Una VM di laboratorio ha due route effettive attive: una route definita dall’utente 0.0.0.0/0 verso un’appliance di rete e una route di sistema 10.20.0.0/16 tramite peering VNet. Non esiste una route più specifica. Quale hop successivo viene scelto per 10.20.7.5?

- **A.** Il peering VNet, perché il prefisso /16 corrispondente è più specifico.
- **B.** L’appliance di rete, perché le route definite dall’utente hanno sempre precedenza su qualsiasi route di sistema.
- **C.** Entrambi gli hop, perché Azure duplica i pacchetti su tutte le route corrispondenti.
- **D.** Nessun hop, perché prefissi corrispondenti sovrapposti rendono non valida la tabella di routing.

<details>
<summary>Perché:</summary>

**A. Il peering VNet, perché il prefisso /16 corrispondente è più specifico.**

Azure seleziona prima la route corrispondente con il prefisso più lungo. La destinazione appartiene a 10.20.0.0/16, che è più specifico di 0.0.0.0/0, quindi il pacchetto usa la route di peering attiva. La preferenza per l’origine della route conta quando le route applicabili hanno la stessa lunghezza di prefisso; non rende una route predefinita definita dall’utente sempre dominante. La scelta di un hop successivo non dimostra comunque che il firewall consenta il traffico o che l’applicazione sia accessibile.

- **B.** Qui la preferenza per l’origine della route non prevale sulla selezione del prefisso più lungo: la route predefinita definita dall’utente è meno specifica della route di peering attiva.
- **C.** Il normale routing in base alla destinazione seleziona la route corrispondente preferita; non copia il pacchetto verso ogni hop il cui prefisso corrisponde.
- **D.** I prefissi sovrapposti sono normali nelle tabelle di routing; una route predefinita può coesistere con route più specifiche senza invalidare la tabella.

[Fonte:](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview) · [Da ripassare:](../certifications/it/AZ-700.md)

</details>

<a id="quiz-q14"></a>

## AZ-700 · Crittografia di ExpressRoute

Un’università usa ExpressRoute e richiede la crittografia dal dispositivo VPN del campus a un gateway VPN di Azure. ExpressRoute deve rimanere il trasporto sottostante. Quale soluzione soddisfa più direttamente questo perimetro?

- **A.** Abilitare MACsec sui collegamenti ExpressRoute Direct supportati e considerare quella protezione fisica come l’intero perimetro dal campus al gateway.
- **B.** Usare il peering privato ExpressRoute senza altri meccanismi di crittografia, perché il routing privato cifra tutti i payload.
- **C.** Usare un tunnel IPsec supportato su ExpressRoute, verificando routing, supporto del gateway e velocità effettiva richiesta.
- **D.** Abilitare TLS solo tra l’applicazione Azure e il database, lasciando non cifrato il percorso dal campus al gateway.

<details>
<summary>Perché:</summary>

**C. Usare un tunnel IPsec supportato su ExpressRoute, verificando routing, supporto del gateway e velocità effettiva richiesta.**

ExpressRoute fornisce connettività privata, ma non cifra automaticamente i payload. Un overlay IPsec supportato può proteggere la connessione richiesta dal dispositivo VPN del campus al gateway VPN di Azure, usando ExpressRoute come trasporto sottostante. MACsec protegge i collegamenti fisici ExpressRoute Direct supportati, quindi un perimetro diverso. La proposta deve inoltre verificare routing, configurazioni di gateway supportate, capacità e comportamento in caso di guasto, senza presumere che la sola crittografia completi il progetto.

- **A.** MACsec protegge i collegamenti fisici Direct supportati; quel segmento non copre da solo l’intero perimetro richiesto, dal dispositivo del campus al gateway Azure.
- **B.** Il peering privato modifica connettività e routing, ma non cifra automaticamente il payload lungo la connessione richiesta dal campus al gateway.
- **D.** TLS tra applicazione e database protegge un altro segmento; lascia scoperto il perimetro esplicitamente richiesto tra dispositivo VPN del campus e gateway Azure.

[Fonte:](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-about-encryption) · [Da ripassare:](../certifications/it/AZ-700.md)

</details>

<a id="quiz-q15"></a>

## DP-300 · Ripristino temporizzato di SQL

Alle 14:20 un’università scopre un aggiornamento distruttivo di Azure SQL Database, confermato alle 13:00. La modifica ha raggiunto la replica. La conservazione dei backup automatici include le 12:59 e l’obiettivo è recuperare quello stato precedente con la minima perdita evitabile di dati. Quale piano è più adatto?

- **A.** Promuovere la replica attuale sincronizzata e presumere che l’aggiornamento confermato scompaia.
- **B.** Ripristinare alle 12:59 in un nuovo database, convalidarlo e pianificare la riconnessione controllata dell’applicazione e l’eventuale riconciliazione dei dati successivi.
- **C.** Ripristinare un backup conservato di due giorni prima, anche se il punto delle 12:59 richiesto è disponibile.
- **D.** Eseguire un ripristino temporizzato e presumere che Azure sovrascriva il database di produzione e reindirizzi automaticamente tutti i client.

<details>
<summary>Perché:</summary>

**B. Ripristinare alle 12:59 in un nuovo database, convalidarlo e pianificare la riconnessione controllata dell’applicazione e l’eventuale riconciliazione dei dati successivi.**

Il ripristino temporizzato permette di recuperare uno stato conservato precedente alla transazione distruttiva. In Azure SQL Database il ripristino crea un database, quindi convalida e riconnessione controllata dell’applicazione fanno parte del piano. Anche le attività legittime successive richiedono una decisione esplicita su come gestirle. La replica sincronizzata contiene già l’aggiornamento errato: promuoverla non migliora la correttezza storica e non recupera il momento richiesto.

- **A.** La replica ha già ricevuto la modifica distruttiva confermata, quindi promuovere quella copia attuale non recupera lo stato corretto precedente del database.
- **C.** Il backup più vecchio elimina inutilmente più dati storici, dato che la conservazione indicata supporta il punto richiesto prima dell’aggiornamento e la minima perdita evitabile.
- **D.** Il ripristino temporizzato di SQL Database crea un database; il team deve convalidarlo e gestire le connessioni applicative senza presumere una sostituzione automatica.

[Fonte:](https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups) · [Da ripassare:](../certifications/it/DP-300.md)

</details>

<a id="quiz-q16"></a>

## DP-300 · Perimetri della crittografia SQL

Un’applicazione di ricerca deve rendere alcuni valori dei partecipanti illeggibili agli amministratori del database che interrogano le tabelle. Solo il client attendibile può decifrarli e gli amministratori non devono disporre delle chiavi del client. Quale soluzione corrisponde meglio a questo perimetro?

- **A.** Abilitare TDE e lasciare agli amministratori il normale accesso alle query del database.
- **B.** Richiedere TLS tra client e database, senza cifrare i valori selezionati nel client.
- **C.** Applicare il mascheramento dinamico dei dati lasciando agli amministratori ampi privilegi di query.
- **D.** Usare Always Encrypted configurato correttamente con un client compatibile e chiavi gestite separatamente.

<details>
<summary>Perché:</summary>

**D. Usare Always Encrypted configurato correttamente con un client compatibile e chiavi gestite separatamente.**

Always Encrypted è progettato per un perimetro in cui client compatibili cifrano e decifrano i valori sensibili, mentre le chiavi possono rimanere fuori dall’accesso del motore di database. L’università deve verificare il supporto del driver, le operazioni consentite e l’amministrazione separata delle chiavi. TDE protegge i file del database a riposo, TLS protegge la connessione e il mascheramento cambia la presentazione delle query. Questi controlli, da soli, non soddisfano il requisito di escludere gli amministratori indicato nello scenario.

- **A.** TDE protegge i file del database a riposo; gli amministratori con normali diritti di query possono comunque ottenere valori in chiaro tramite il motore del database.
- **B.** TLS protegge i dati in transito sulla connessione, ma non impedisce di per sé a un amministratore autorizzato di interrogare i valori memorizzati.
- **C.** Il mascheramento modifica la presentazione dei risultati per gli utenti interessati; non crea un perimetro crittografico contro amministratori che mantengono ampi privilegi sul database.

[Fonte:](https://learn.microsoft.com/en-us/azure/azure-sql/database/security-overview) · [Da ripassare:](../certifications/it/DP-300.md)

</details>

<a id="quiz-q17"></a>

## AI-901 · Identità del client Foundry

Il client Foundry di uno studente usa l’endpoint e il nome della distribuzione documentati, ma non è configurata alcuna credenziale per il carico di lavoro chiamante. Che cosa deve aggiungere il progetto per identificare un chiamante autorizzato?

- **A.** Sostituire il nome della distribuzione con il nome del modello nel catalogo e lasciare assenti le credenziali.
- **B.** Configurare una credenziale supportata per il carico di lavoro e concedere a quell’identità l’accesso minimo necessario.
- **C.** Passare da REST a un SDK lasciando il chiamante non autenticato.
- **D.** Copiare nel client l’URL del portale di un amministratore che ha effettuato l’accesso, come prova dell’autorizzazione del carico di lavoro.

<details>
<summary>Perché:</summary>

**B. Configurare una credenziale supportata per il carico di lavoro e concedere a quell’identità l’accesso minimo necessario.**

Un endpoint identifica la destinazione della richiesta e una distribuzione identifica il modello configurato; nessuno dei due stabilisce chi sta chiamando. Il client necessita di un meccanismo di autenticazione supportato e l’identità risultante deve avere le autorizzazioni minime adeguate. Devono inoltre essere compatibili l’SDK scelto e la generazione dell’API. I segreti devono rimanere fuori dai notebook e dal codice sorgente, e l’accesso al portale di un amministratore umano non si trasferisce automaticamente all’applicazione.

- **A.** Il nome di un modello nel catalogo e quello di una distribuzione hanno funzioni diverse; cambiare quella stringa non autentica il carico di lavoro e non concede accesso.
- **C.** Un SDK incapsula i contratti di richiesta supportati, ma cambiare libreria client non elimina i requisiti di autenticazione e autorizzazione del servizio.
- **D.** Un URL del portale identifica una posizione; la sessione autenticata del browser dell’amministratore non stabilisce identità o autorizzazioni del carico di lavoro distinto.

[Fonte:](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) · [Da ripassare:](../certifications/it/AI-901.md)

</details>

<a id="quiz-q18"></a>

## AI-901 · Grounding e sostegno alle affermazioni

Un assistente per gli appunti indica una data di consegna e cita il PDF corretto della lezione, ma il passaggio recuperato definisce soltanto un algoritmo. L’app deve fornire date solo da passaggi consentiti che le supportino. Qual è la risposta migliore?

- **A.** Recuperare un passaggio che supporti la data oppure dichiarare che le evidenze disponibili sono insufficienti.
- **B.** Accettare la data perché citare il documento corretto dimostra ogni affermazione nella risposta.
- **C.** Impostare la temperatura di generazione a zero e accettare la stessa data senza verificare un altro passaggio.
- **D.** Accettare la data se il modello dichiara un’elevata sicurezza, anche se il passaggio non la supporta.

<details>
<summary>Perché:</summary>

**A. Recuperare un passaggio che supporti la data oppure dichiarare che le evidenze disponibili sono insufficienti.**

Il grounding richiede evidenze a sostegno della specifica affermazione, non soltanto una citazione di un documento correlato. La definizione dell’algoritmo fornita non stabilisce una data di consegna. Il recupero deve cercare un passaggio autorizzato che contenga la data pertinente e le relative condizioni; altrimenti l’assistente deve astenersi dal rispondere. Generazione deterministica e sicurezza dichiarata dal modello non possono creare le evidenze mancanti. La valutazione deve confrontare ogni affermazione rilevante con il testo effettivamente citato.

- **B.** Una citazione del documento corretto può comunque puntare a un passaggio non pertinente; la sola identità del documento non dimostra la data indicata.
- **C.** Una temperatura più bassa modifica la variabilità della generazione, ma non può trasformare la definizione di un algoritmo in evidenza per una data di consegna assente.
- **D.** La sicurezza del modello può essere infondata; la regola esplicita dell’applicazione richiede comunque un passaggio consentito che supporti quella specifica data.

[Fonte:](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators) · [Da ripassare:](../certifications/it/AI-901.md)

</details>

<a id="quiz-q19"></a>

## SC-200 · Evidenze temporali del SOC

Record sintetici dello stesso account verificato mostrano un’attività email alle 10:02 UTC, acquisita alle 10:20, e un accesso alle 10:08 UTC, acquisito alle 10:09. Gli orologi di entrambi gli eventi sono attendibili. Quale conclusione è supportata soltanto da questi record?

- **A.** L’accesso è avvenuto prima perché il relativo record è arrivato per primo nell’area di lavoro.
- **B.** L’email ha causato l’accesso e dimostra la compromissione dell’account.
- **C.** L’ora dell’evento email deve essere scartata perché l’acquisizione è avvenuta in ritardo.
- **D.** L’attività email ha preceduto l’accesso, mentre causalità e compromissione richiedono ulteriori evidenze.

<details>
<summary>Perché:</summary>

**D. L’attività email ha preceduto l’accesso, mentre causalità e compromissione richiedono ulteriori evidenze.**

I timestamp attendibili degli eventi collocano l’attività email prima dell’accesso. I timestamp di acquisizione descrivono l’arrivo dei record, e ritardi diversi nella raccolta possono invertirne l’ordine di arrivo. La corrispondenza di un account verificato aiuta a correlare i record, ma non dimostra che l’email abbia causato l’accesso o che uno dei due eventi fosse dannoso. L’analista deve conservare entrambi i campi temporali, indagare sulle attività circostanti e dichiarare i limiti delle evidenze.

- **A.** L’ordine di acquisizione descrive l’arrivo dei dati raccolti, non l’ordine delle attività; i timestamp attendibili collocano l’email prima dell’accesso in questi dati.
- **B.** Un account comune e la sequenza temporale giustificano un’indagine, ma da soli non stabiliscono un nesso causale, un’attività dannosa o una compromissione confermata.
- **C.** Un’acquisizione tardiva può verificarsi senza invalidare un timestamp di evento attendibile; occorre conservare entrambi i campi e indagare sul ritardo senza scartare le evidenze.

[Fonte:](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender) · [Da ripassare:](../certifications/it/SC-200.md)

</details>

<a id="quiz-q20"></a>

## SC-200 · Idempotenza delle azioni di risposta

Un playbook di Sentinel crea un ticket universitario per un incidente, ma la risposta di successo va persa. Un nuovo tentativo potrebbe creare un altro ticket per la stessa azione approvata. Quale controllo del flusso gestisce meglio questo errore?

- **A.** Usare un timeout più lungo e presumere che una risposta assente significhi sempre che non esiste un ticket.
- **B.** Generare un nuovo identificatore di azione a ogni tentativo, così che ogni richiesta appaia indipendente.
- **C.** Salvare in modo persistente una chiave incidente/azione e lo stato del ticket, quindi riconciliare o riusare il risultato esistente quando l’azione viene ritentata.
- **D.** Deduplicare solo i record di avviso in ingresso, consentendo al passaggio di creazione del ticket di ripetersi senza controlli sullo stato.

<details>
<summary>Perché:</summary>

**C. Salvare in modo persistente una chiave incidente/azione e lo stato del ticket, quindi riconciliare o riusare il risultato esistente quando l’azione viene ritentata.**

L’idempotenza significa che ripetere la stessa azione logica ne preserva il risultato previsto senza creare un altro effetto collaterale. Una chiave incidente/azione persistente, lo stato registrato e il riferimento al ticket esterno permettono ai nuovi tentativi di trovare o riconciliare il lavoro esistente. Una risposta assente indica un esito sconosciuto finché non viene verificato. Il flusso necessita anche di tentativi limitati, un responsabile e autorizzazioni adeguate alla creazione di ticket; la sola deduplicazione degli avvisi non controlla l’esecuzione delle azioni.

- **A.** Un timeout più lungo può ridurre alcuni errori, ma una risposta persa lascia comunque incerto se il ticket esterno sia già stato creato.
- **B.** Un nuovo identificatore fa apparire il tentativo come un nuovo lavoro, impedendo al flusso di riconoscere l’azione logica già tentata.
- **D.** La deduplicazione degli avvisi controlla i record in ingresso; un passaggio successivo ritentato può comunque duplicare i ticket se l’esecuzione dell’azione non ha controlli di stato propri.

[Fonte:](https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer) · [Da ripassare:](../certifications/it/SC-200.md)

</details>

<a id="quiz-q21"></a>

## SC-300 · Accesso condizionale in modalità solo report

Un’università sperimenta un criterio di accesso condizionale in modalità solo report. La valutazione indica che un accesso non soddisferebbe il requisito di concessione proposto, eppure l’accesso riesce. Nessun altro criterio richiede quel controllo. Qual è la spiegazione migliore?

- **A.** Le autorizzazioni dell’applicazione prevalgono sempre su un rifiuto imposto dall’accesso condizionale.
- **B.** Il controllo proposto è già stato applicato perché la modalità solo report lo valuta.
- **C.** La modalità solo report registra la valutazione del criterio senza applicarne il requisito di concessione.
- **D.** La modalità solo report consente il primo accesso non conforme e blocca automaticamente quello successivo.

<details>
<summary>Perché:</summary>

**C. La modalità solo report registra la valutazione del criterio senza applicarne il requisito di concessione.**

La modalità solo report valuta il criterio e registra l’esito previsto senza applicarne i controlli. Un accesso riuscito può quindi coesistere con evidenze che il requisito di concessione proposto non sarebbe soddisfatto se fosse applicato. Prima di una distribuzione approvata, il team deve esaminare i casi che si prevede di consentire o negare, le identità coinvolte, le esclusioni e il recupero dell’accesso amministrativo. Le autorizzazioni dell’applicazione costituiscono un perimetro distinto e non annullano un rifiuto imposto da un criterio di accesso condizionale.

- **A.** L’abilitazione all’applicazione non prevale automaticamente su un rifiuto applicabile imposto dall’accesso condizionale; è la modalità del criterio indicata nello scenario a spiegare l’accesso riuscito.
- **B.** Valutazione e applicazione sono distinte: la modalità solo report registra ciò che accadrebbe, quindi il risultato non dimostra che il requisito di concessione sia stato applicato.
- **D.** La modalità solo report non introduce un primo tentativo consentito seguito dall’applicazione automatica; per applicare i controlli occorre modificare la configurazione del criterio pertinente.

[Fonte:](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only) · [Da ripassare:](../certifications/it/SC-300.md)

</details>

<a id="quiz-q22"></a>

## SC-300 · Attestazioni della federazione dei carichi di lavoro

Un processo di compilazione universitario usa la federazione delle identità del carico di lavoro. Lo scambio di token non riesce e il valore subject del token esterno differisce per maiuscole e minuscole dal subject federato configurato. Issuer e audience corrispondono. Quale modifica risolve questa incongruenza?

- **A.** Assegnare al carico di lavoro il ruolo Owner della sottoscrizione lasciando invariato il subject federato.
- **B.** Allineare esattamente il subject configurato all’attestazione in ingresso prevista, quindi verificare separatamente le autorizzazioni minime dell’identità sulle risorse.
- **C.** Aggiungere mapping SCIM per il provisioning degli utenti relativi al nome del repository invece di correggere la credenziale federata.
- **D.** Aumentare la durata del token esterno lasciando invariato il subject non corrispondente.

<details>
<summary>Perché:</summary>

**B. Allineare esattamente il subject configurato all’attestazione in ingresso prevista, quindi verificare separatamente le autorizzazioni minime dell’identità sulle risorse.**

Le credenziali federate confrontano issuer, subject e audience attendibili con l’asserzione in ingresso: questi valori devono corrispondere, comprese maiuscole e minuscole. Correggere la corrispondenza del subject previsto risolve l’errore di scambio dei token indicato senza introdurre un segreto client archiviato. Uno scambio riuscito autentica il carico di lavoro, ma non concede accesso arbitrario alle risorse. L’identità risultante necessita comunque di autorizzazioni assegnate separatamente, con un ambito adeguato alle operazioni effettive della compilazione.

- **A.** Le autorizzazioni sulle risorse stabiliscono che cosa può fare un’identità autenticata; un ruolo ampio non corregge un’attestazione non corrispondente che impedisce lo scambio di token.
- **C.** SCIM riguarda il provisioning degli account e degli attributi; non sostituisce le verifiche di issuer, subject e audience federati in questo scambio di token del carico di lavoro.
- **D.** Modificare la durata interviene sul periodo di validità del token, ma non fa corrispondere il subject, che distingue maiuscole e minuscole, alla credenziale federata configurata.

[Fonte:](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) · [Da ripassare:](../certifications/it/SC-300.md)

</details>

<a id="quiz-q23"></a>

## AZ-140 · Autorizzazioni dei profili AVD

Uno studente può avviare una sessione Azure Virtual Desktop in pool assegnata, ma FSLogix riceve un errore di accesso negato sulla cartella SMB del suo profilo. L’accesso a livello di condivisione è presente, mentre le autorizzazioni NTFS della cartella negano l’accesso allo studente. Quale intervento risponde meglio alle evidenze?

- **A.** Correggere le autorizzazioni NTFS della cartella mantenendo un adeguato isolamento tra utenti, quindi verificare il collegamento del profilo con l’identità dello studente.
- **B.** Assegnare allo studente un ruolo Contributor più ampio sul piano di controllo di Azure senza modificare le autorizzazioni della cartella.
- **C.** Riassegnare il gruppo di applicazioni desktop e presumere che l’assegnazione conceda anche l’accesso NTFS al profilo.
- **D.** Ricreare l’immagine dell’host di sessione mantenendo lo stesso percorso del profilo e le autorizzazioni NTFS che negano l’accesso.

<details>
<summary>Perché:</summary>

**A. Correggere le autorizzazioni NTFS della cartella mantenendo un adeguato isolamento tra utenti, quindi verificare il collegamento del profilo con l’identità dello studente.**

L’accesso al profilo SMB dipende sia dall’accesso a livello di condivisione sia dalle autorizzazioni del file system. Le evidenze indicano un rifiuto NTFS: correggere l’accesso previsto alla cartella, mantenendo l’isolamento degli altri studenti, risolve quindi l’errore immediato. Occorre provare con l’identità interessata ed esaminare le evidenze del collegamento del profilo FSLogix. L’abilitazione al desktop e l’amministrazione delle risorse Azure costituiscono perimetri diversi; avviare correttamente la sessione non dimostra di avere il permesso di leggere e scrivere il profilo persistente.

- **B.** Un ruolo di gestione sul piano di controllo non corregge di per sé il rifiuto NTFS individuato sulla cartella SMB usata per il profilo dello studente.
- **C.** L’assegnazione al gruppo di applicazioni rende il desktop disponibile all’utente, ma non concede di per sé l’accesso al file system necessario per l’archivio dei profili.
- **D.** Sostituire l’host mantenendo lo stesso accesso negato alla cartella lascia il problema di autorizzazioni dell’archiviazione anche nel percorso della nuova sessione.

[Fonte:](https://learn.microsoft.com/en-us/fslogix/how-to-configure-storage-permissions) · [Da ripassare:](../certifications/it/AZ-140.md)

</details>

<a id="quiz-q24"></a>

## AZ-140 · Margine di capacità AVD in caso di guasto

Un laboratorio AVD simulato richiede 60 sessioni studente simultanee. I test indicano un massimo di 10 sessioni per host integro. Tutti gli host devono essere pronti prima della lezione e la capacità deve sostenere ancora 60 sessioni dopo il guasto di un qualsiasi host. Qual è il numero minimo di host pronti?

- **A.** Sei host.
- **B.** Cinque host.
- **C.** Otto host.
- **D.** Sette host.

<details>
<summary>Perché:</summary>

**D. Sette host.**

Per la domanda normale misurata servono sei host integri: 60 diviso 10 sessioni per host. Un ulteriore host già pronto fornisce il margine richiesto per un singolo guasto, lasciando sei host dopo il guasto. Sette è quindi il minimo con queste ipotesi esplicite. Il piano di ridimensionamento reale deve considerare anche tempi di avvio, stato di svuotamento delle sessioni, capacità non integra, carico dell’archiviazione durante gli accessi e autorizzazioni; avviare successivamente un host arrestato non soddisfa il requisito di disponibilità prima della lezione.

- **A.** Sei host soddisfano la domanda solo finché rimangono tutti integri; perderne uno lascia capacità per 50 sessioni con il limite misurato per host.
- **B.** Cinque host forniscono soltanto 50 sessioni già prima di un guasto, quindi non possono sostenere i 60 studenti simultanei indicati con queste ipotesi.
- **C.** Otto host soddisferebbero il requisito, ma sette lasciano già sei host integri dopo un guasto, quindi otto supera il minimo.

[Fonte:](https://learn.microsoft.com/en-us/azure/virtual-desktop/autoscale-create-assign-scaling-plan) · [Da ripassare:](../certifications/it/AZ-140.md)

</details>

<a id="quiz-q25"></a>

## AI-103 · Revoca dell’accesso nel recupero dei dati

Uno studente perde l’autorizzazione a un notebook di ricerca, ma un assistente ne conserva ancora passaggi nella cache. I criteri richiedono un accesso attuale prima che qualsiasi passaggio raggiunga il modello. L’applicazione non riesce a verificare che le autorizzazioni siano aggiornate. Quale comportamento rispetta i criteri?

- **A.** Inviare il passaggio nella cache eliminandone la citazione, così da non nominare il notebook.
- **B.** Continuare a fornire il passaggio nella cache fino al successivo aggiornamento pianificato dell’indice.
- **C.** Inviare il passaggio con un prompt che chieda al modello di non rivelare materiale a cui lo studente non può accedere.
- **D.** Trattenere il passaggio finché non è possibile verificare l’accesso e applicare controlli di autorizzazione aggiornati ai risultati del recupero e della cache.

<details>
<summary>Perché:</summary>

**D. Trattenere il passaggio finché non è possibile verificare l’accesso e applicare controlli di autorizzazione aggiornati ai risultati del recupero e della cache.**

I criteri collocano l’autorizzazione prima dell’accesso del modello, anche per i contenuti nella cache. Se non è possibile stabilire che le autorizzazioni siano aggiornate, trattenere il passaggio preserva questo perimetro. L’applicazione deve verificare il progetto di recupero e cache scelto rispetto a revoche, modifiche ai gruppi e indici obsoleti. Un prompt o l’assenza della citazione non possono annullare la divulgazione al modello di un passaggio non autorizzato. Le funzionalità native per le autorizzazioni e i filtri personalizzati richiedono verifiche distinte delle capacità e dell’effettiva applicazione dei controlli.

- **A.** Eliminare una citazione cambia la presentazione, ma il contenuto non autorizzato del notebook raggiungerebbe comunque il modello e resterebbe disponibile per generare la risposta.
- **B.** Un aggiornamento pianificato lascia un intervallo di accesso che viola il requisito di autorizzazioni attuali, soprattutto se i passaggi nella cache sopravvivono alle modifiche dell’indice.
- **C.** Un prompt delega alla generazione una decisione di accesso dopo la divulgazione; non può far rispettare il perimetro richiesto prima che il passaggio raggiunga il modello.

[Fonte:](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) · [Da ripassare:](../certifications/it/AI-103.md)

</details>

<a id="quiz-q26"></a>

## AI-103 · Esiti sconosciuti degli strumenti

Uno strumento approvato di un agente richiede la creazione di una condivisione di appunti di ricerca. Il backend accetta una chiave operazione stabile, ma la risposta scade e la condivisione potrebbe già esistere. È disponibile una verifica dello stato. Che cosa deve fare l’applicazione?

- **A.** Registrare un esito sconosciuto, verificare e riconciliare lo stato usando la chiave operazione e riutilizzarla se serve un nuovo tentativo supportato.
- **B.** Riprovare immediatamente con una nuova chiave operazione, così che il backend tratti la richiesta come un’azione nuova.
- **C.** Segnare l’operazione come sicuramente fallita ed eliminare la chiave perché non è arrivata una risposta.
- **D.** Chiedere al modello di dedurre il successo dalla precedente richiesta allo strumento e dichiarare il completamento senza controllare il backend.

<details>
<summary>Perché:</summary>

**A. Registrare un esito sconosciuto, verificare e riconciliare lo stato usando la chiave operazione e riutilizzarla se serve un nuovo tentativo supportato.**

Un timeout dopo l’invio non stabilisce se l’effetto si sia verificato. Conservare uno stato esplicito di esito sconosciuto e una chiave operazione stabile permette all’applicazione di interrogare il backend e riconciliare il risultato prima di un’altra scrittura. Se è supportato un nuovo tentativo, la stessa chiave logica mantiene il perimetro di idempotenza previsto. Approvazione e convalida degli argomenti rimangono necessarie; la chiamata proposta dal modello non dimostra che il backend abbia completato la condivisione autorizzata.

- **B.** Una chiave nuova rende il tentativo un’operazione distinta, che può creare un’altra condivisione se la prima richiesta è già stata confermata correttamente.
- **C.** L’assenza di risposta indica un esito incerto, non un fallimento sicuro; eliminare la chiave rimuove anche il riferimento disponibile per la riconciliazione.
- **D.** La richiesta generata allo strumento descrive il lavoro previsto; solo le evidenze del backend possono confermare se la condivisione richiesta sia stata effettivamente creata.

[Fonte:](https://learn.microsoft.com/en-us/azure/architecture/patterns/asynchronous-request-reply) · [Da ripassare:](../certifications/it/AI-103.md)

</details>

<a id="quiz-q27"></a>

## DP-700 · Ordine delle eliminazioni incrementali

Un caricamento delle iscrizioni in Fabric elabora la modifica di origine con sequenza 98, che elimina l’iscrizione E. In seguito arriva in ritardo un aggiornamento di E con sequenza 94. Le sequenze di origine definiscono l’ordine di riferimento delle modifiche ed è possibile una successiva reiscrizione legittima. Quale regola di unione preserva lo stato corretto?

- **A.** Applicare l’aggiornamento 94 perché è arrivato più recentemente alla pipeline.
- **B.** Ignorare per sempre tutte le modifiche future di E dopo aver osservato qualsiasi eliminazione.
- **C.** Conservare le informazioni sull’eliminazione e sulla versione per la sequenza 98 e rifiutare l’aggiornamento 94 perché precedente, consentendo una modifica valida più recente.
- **D.** Eliminare il checkpoint e riprodurre le modifiche rigorosamente nell’ordine di arrivo senza confronti di versione.

<details>
<summary>Perché:</summary>

**C. Conservare le informazioni sull’eliminazione e sulla versione per la sequenza 98 e rifiutare l’aggiornamento 94 perché precedente, consentendo una modifica valida più recente.**

La sequenza di origine determina l’ordine delle operazioni aziendali, quindi l’aggiornamento 94 non deve ricreare un’iscrizione eliminata alla sequenza 98. Conservare l’eliminazione e la sua versione permette a un’unione idempotente di rifiutare modifiche obsolete, accettando comunque una versione successiva valida. Qui l’ordine di arrivo non determina la sequenza corretta delle modifiche. Sono necessari insieme chiavi stabili, confronti di versione deterministici e avanzamento registrato in modo persistente; rielaborare l’input senza queste regole non risolve il problema di ordinamento.

- **A.** L’ordine di arrivo può differire dall’ordine delle modifiche di origine; applicare l’aggiornamento più vecchio ricreerebbe erroneamente un’iscrizione eliminata dalla modifica più recente.
- **B.** Un divieto permanente rifiuterebbe anche una successiva reiscrizione valida; l’unione deve confrontare le versioni, senza vietare tutte le modifiche future per quella chiave.
- **D.** Riprodurre lo stesso ordine di arrivo senza controlli di versione può ricreare di nuovo l’iscrizione; eliminare il checkpoint, da solo, non garantisce il rispetto dell’ordine delle modifiche di origine.

[Fonte:](https://learn.microsoft.com/en-us/fabric/data-engineering/delta-lake-change-data-feed) · [Da ripassare:](../certifications/it/DP-700.md)

</details>

<a id="quiz-q28"></a>

## DP-700 · Percorsi di accesso in Fabric

Un report universitario applica correttamente restrizioni a livello di riga e ha un’etichetta di riservatezza. Lo stesso analista può leggere direttamente i file con dati dei singoli studenti tramite un percorso OneLake autorizzato. I criteri consentono soltanto i totali per modulo. Che cosa deve modificare e verificare l’ingegnere?

- **A.** Rinominare l’etichetta Altamente riservato e presumere che il nome imponga le restrizioni di riga del report anche nella lettura diretta dei file.
- **B.** Limitare il percorso di accesso sottostante alle autorizzazioni minime necessarie e provare i totali consentiti e i dettagli negati con l’identità dell’analista.
- **C.** Nascondere la tabella dettagliata nel report lasciando invariate le autorizzazioni dell’analista sui file.
- **D.** Assegnare un ruolo più ampio nell’area di lavoro, così che le restrizioni di riga esistenti nel report governino automaticamente ogni percorso di accesso.

<details>
<summary>Perché:</summary>

**B. Limitare il percorso di accesso sottostante alle autorizzazioni minime necessarie e provare i totali consentiti e i dettagli negati con l’identità dell’analista.**

Una restrizione applicata da un report o da un motore di query non governa automaticamente un percorso separato di accesso diretto ai file. L’ingegnere deve allineare ai criteri le autorizzazioni di area di lavoro, elemento, motore e file e provare ogni percorso di accesso previsto usando l’identità dell’analista. Un’etichetta di riservatezza fornisce contesto di governance o protezione configurata, ma il solo nome non implementa ovunque un’autorizzazione equivalente. Autorizzazioni più ampie possono esporre ulteriori percorsi invece di colmare questa lacuna.

- **A.** Cambiare il nome di una classificazione non configura il perimetro separato di accesso ai file e non applica automaticamente in OneLake le restrizioni di riga del motore del report.
- **C.** Nascondere contenuti nel report cambia soltanto quella presentazione; l’analista conserva il percorso diretto indicato verso i file con dati dei singoli studenti.
- **D.** Un ruolo più ampio nell’area di lavoro estende l’accesso e non trasforma le restrizioni di riga del report in una regola universale per ogni motore e percorso di file.

[Fonte:](https://learn.microsoft.com/en-us/fabric/security/permission-model) · [Da ripassare:](../certifications/it/DP-700.md)

</details>

<a id="quiz-q29"></a>

## SC-100 · Responsabilità per il rischio residuo

Un architetto documenta che una piattaforma universitaria per gli appunti proposta conserva un rischio rilevante di interruzione anche dopo i controlli attuabili. Il team di sicurezza consiglia di procedere, ma la governance richiede l’accettazione del rischio da parte aziendale. Chi deve autorizzare l’accettazione del rischio residuo?

- **A.** L’analista SOC che può chiudere il ticket di sicurezza correlato.
- **B.** Il responsabile aziendale del rischio dotato dell’autorità decisionale richiesta, registrando l’esposizione e le condizioni di riesame.
- **C.** Il fornitore del prodotto, perché il suo punteggio di conformità sostituisce la decisione aziendale dell’università.
- **D.** L’amministratore cloud, soltanto perché può distribuire le risorse.

<details>
<summary>Perché:</summary>

**B. Il responsabile aziendale del rischio dotato dell’autorità decisionale richiesta, registrando l’esposizione e le condizioni di riesame.**

Il rischio residuo rimane un’esposizione aziendale anche dopo la scelta dei controlli tecnici. Il responsabile del rischio autorizzato e chiamato a risponderne deve decidere se l’esposizione sia accettabile, usando le evidenze dell’architetto su impatto, ipotesi di probabilità, alternative e lacune rimanenti. La decisione deve includere ambito, condizioni di riesame e responsabilità. Raccomandazioni di sicurezza, diritti di distribuzione delle risorse e valutazioni dei fornitori contribuiscono alla decisione, ma non conferiscono automaticamente l’autorità richiesta dall’università per accettare il rischio.

- **A.** Chiudere un ticket operativo è un’autorizzazione nel flusso di lavoro; non conferisce il potere di accettare per l’università un’esposizione aziendale rilevante.
- **C.** Una valutazione del fornitore può orientare la scelta dei controlli, ma non sostituisce una decisione assunta dal responsabile dell’università sul proprio rischio operativo residuo.
- **D.** La capacità di distribuire risorse è un’autorità tecnica; lo scenario richiede separatamente un responsabile aziendale autorizzato ad accettare il rischio residuo di interruzione.

[Fonte:](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/govern/assess-cloud-risks) · [Da ripassare:](../certifications/it/SC-100.md)

</details>

<a id="quiz-q30"></a>

## SC-100 · Verifica degli obiettivi di ripristino

Un’esercitazione di ripristino stabilisce un RTO di due ore e un RPO di 15 minuti. Un’interruzione inizia alle 11:00 UTC. Le letture autorizzate dei documenti riprendono alle 12:30, con dati recuperati soltanto fino alle 10:40. Si assumano questi come confini di misurazione concordati. Quale valutazione è corretta?

- **A.** Entrambi gli obiettivi sono rispettati perché il servizio è ripreso entro due ore.
- **B.** L’RPO è rispettato, ma l’RTO non lo è.
- **C.** Entrambi gli obiettivi sono mancati perché qualsiasi perdita di dati viola l’RTO.
- **D.** L’RTO è rispettato, ma l’RPO no, perché il punto di ripristino precede di 20 minuti l’interruzione.

<details>
<summary>Perché:</summary>

**D. L’RTO è rispettato, ma l’RPO no, perché il punto di ripristino precede di 20 minuti l’interruzione.**

L’RTO misura l’interruzione accettabile: le letture autorizzate riprendono dopo 90 minuti, entro l’obiettivo di due ore. L’RPO misura la perdita accettabile dei dati più recenti: recuperare fino alle 10:40 per un’interruzione delle 11:00 lascia un divario di 20 minuti, superiore all’obiettivo di 15 minuti. Sono verifiche indipendenti e rispettarne una non significa rispettare l’altra. L’esercitazione deve registrare entrambe le misurazioni e le dipendenze che hanno consentito di riprendere l’operazione aziendale definita.

- **A.** Ripristinare il servizio entro il tempo previsto soddisfa soltanto l’RTO; il distinto divario di 20 minuti del punto di ripristino supera comunque l’RPO indicato.
- **B.** L’interruzione dura 90 minuti, entro due ore, mentre il divario dei dati di 20 minuti supera 15 minuti; questa opzione inverte i risultati.
- **C.** L’RTO riguarda la durata dell’interruzione, non la presenza di qualsiasi perdita di dati; il ripristino misurato di 90 minuti rispetta l’obiettivo anche se l’RPO non è soddisfatto.

[Fonte:](https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recover-hadr-overview) · [Da ripassare:](../certifications/it/SC-100.md)

</details>

<a id="quiz-q31"></a>

## AZ-120 · Fencing SAP e singolo nodo di scrittura

Durante una simulazione di incidente di un cluster SAP HANA, si perde la comunicazione con il nodo primario e il secondario non riesce a isolarlo tramite fencing. Il team non può confermare che il primario abbia smesso di accettare scritture. Quale risposta preserva meglio l’integrità dei dati prima del subentro?

- **A.** Disabilitare il fencing e promuovere il secondario, così che il dashboard del cluster mostri subito le risorse in esecuzione.
- **B.** Promuovere il secondario perché l’ultimo stato di replica riuscita dimostra che il vecchio primario non può ancora scrivere.
- **C.** Seguire la procedura di incidente supportata per ripristinare o verificare il fencing e confermare l’isolamento del vecchio nodo di scrittura prima di consentire scritture dopo il subentro.
- **D.** Spostare l’indirizzo virtuale del servizio sul secondario lasciando invariata la capacità di scrittura del primario il cui stato è incerto.

<details>
<summary>Perché:</summary>

**C. Seguire la procedura di incidente supportata per ripristinare o verificare il fencing e confermare l’isolamento del vecchio nodo di scrittura prima di consentire scritture dopo il subentro.**

La perdita di comunicazione non dimostra che il primario si sia arrestato. Il fencing isola un nodo che non può proseguire in sicurezza, proteggendo il requisito di un solo nodo di scrittura e riducendo il rischio di split brain. Il team deve esaminare la configurazione supportata di fencing e quorum, conservare le evidenze sullo stato e stabilire che il vecchio nodo di scrittura sia isolato prima di consentire scritture sul nodo subentrante. Lo stato della replica e lo spostamento di un indirizzo non forniscono tale isolamento, mentre disabilitare il fencing elimina un meccanismo di sicurezza essenziale.

- **A.** Disabilitare il fencing elimina il meccanismo necessario a isolare un nodo di scrittura incerto, quindi la disponibilità apparente può comportare primari in conflitto.
- **B.** Un risultato precedente della replica descrive lo spostamento dei dati in quel momento; non dimostra che il primario irraggiungibile abbia ora smesso di accettare scritture.
- **D.** Spostare un indirizzo virtuale modifica un percorso dei client, ma non impedisce di per sé al vecchio primario di scrivere tramite altre sessioni o percorsi.

[Fonte:](https://learn.microsoft.com/en-us/azure/sap/workloads/sap-hana-high-availability) · [Da ripassare:](../certifications/it/AZ-120.md)

</details>

<a id="quiz-q32"></a>

## AZ-120 · Scritture SAP dopo il passaggio

Una migrazione SAP universitaria apre il sistema di destinazione agli acquisti e gli utenti creano nuovi ordini. L’origine invariata rimane isolata. Un successivo problema di convalida porta a considerare il rollback. Quale piano protegge meglio le nuove transazioni aziendali?

- **A.** Bloccare le scritture, stabilire lo stato dei dati da usare come riferimento, preservare le transazioni della destinazione e concordare un piano supportato di riconciliazione o migrazione inversa prima di riaprire un nodo di scrittura.
- **B.** Riportare il DNS all’origine invariata e presumere che i nuovi ordini della destinazione siano presenti anche lì.
- **C.** Sovrascrivere la destinazione dalla vecchia origine, poi riaprire gli acquisti senza identificare le transazioni create dopo il passaggio.
- **D.** Riaprire sia origine sia destinazione alle scritture mentre gli utenti aziendali decidono in seguito quali ordini mantenere.

<details>
<summary>Perché:</summary>

**A. Bloccare le scritture, stabilire lo stato dei dati da usare come riferimento, preservare le transazioni della destinazione e concordare un piano supportato di riconciliazione o migrazione inversa prima di riaprire un nodo di scrittura.**

Quando la destinazione accetta nuove scritture, il rollback diventa anche una decisione sulla gestione dei dati, oltre che una modifica dell’infrastruttura. Tornare a un’origine invariata può abbandonare i nuovi ordini, mentre riaprire entrambi i sistemi può creare storie di transazioni divergenti. Il runbook deve bloccare le scritture, preservare le evidenze e i nuovi dati aziendali, scegliere lo stato dei dati di riferimento e usare una riconciliazione o un trasferimento inverso supportati con i responsabili aziendali. La convalida e il controllo di un solo sistema autorizzato a scrivere precedono la riapertura degli acquisti.

- **B.** Il DNS reindirizza i client, ma non copia gli ordini successivi al passaggio nell’origine invariata; il solo ritorno può abbandonare quelle nuove transazioni.
- **C.** Sovrascrivere dalla vecchia origine può distruggere ordini legittimi della destinazione; il piano deve prima identificare e preservare le modifiche aziendali effettuate dopo il passaggio.
- **D.** Consentire scritture in entrambi gli ambienti crea storie di transazioni divergenti, rende più difficile la riconciliazione e interrompe il controllo richiesto di un unico sistema di scrittura di riferimento.

[Fonte:](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/migrate/execute-migration) · [Da ripassare:](../certifications/it/AZ-120.md)

</details>
