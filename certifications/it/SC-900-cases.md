# SC-900 · 10 casi con risposte ragionate

[Guida](SC-900.md) · [Quaderno](SC-900-workbook.md) · [Indice](README.md)

Scenari originali di studio, non domande ufficiali d'esame. Identifica il requisito, scarta un'alternativa e indica le prove necessarie. Tutti gli esempi sono ipotetici: non sono state modificate impostazioni del tenant né eseguite prove nel cloud.

## 1. L'app degli appunti passa a un servizio gestito. Il gruppo può smettere di controllare i permessi dei documenti?

<details>
<summary>Ragionamento</summary>

No. Il fornitore gestisce alcune parti della piattaforma, mentre la nostra organizzazione continua a stabilire l'accesso appropriato ai propri dati. Io descriverei il modello di servizio separando attività della piattaforma da identità, condivisione e configurazione applicativa. Una dichiarazione di conformità del fornitore non dimostra che i documenti non pubblicati siano privati. Servono l'ambito di condivisione configurato e una verifica delle operazioni consentite e negate previste, svolta soltanto in un ambiente di prova autorizzato.

</details>

## 2. Uno studente accede correttamente ma non apre la cartella privata di un corso. L'autenticazione è guasta?

<details>
<summary>Ragionamento</summary>

Non necessariamente. L'autenticazione può riuscire mentre l'autorizzazione rifiuta correttamente una determinata risorsa. Controlla quale identità abbia effettuato l'accesso, i suoi gruppi, i permessi richiesti dalla cartella e i criteri applicabili. Assegnare un ruolo amministrativo salterebbe la diagnosi e supererebbe il bisogno. Nell'esercizio di progettazione annota la decisione di accesso attesa e le prove che distinguerebbero un errore di autenticazione da un rifiuto applicativo o relativo alle autorizzazioni della risorsa.

</details>

## 3. Un gruppo propone una password seguita da un'altra password come MFA. Cosa manca?

<details>
<summary>Ragionamento</summary>

Entrambi i segreti appartengono alla categoria della conoscenza: usarne due non introduce fattori diversi. Scegli un metodo e un criterio supportati che soddisfino i fattori o il livello di autenticazione richiesti. Considera anche resistenza al phishing, registrazione, compatibilità dei dispositivi e recupero. Una schermata della pagina di registrazione non dimostra che il criterio venga applicato. Descriverei un accesso atteso che richiede il metodo configurato e un caso negativo nel quale un metodo insufficiente non soddisfa il requisito.

</details>

## 4. Un documento scaricato ha l'hash atteso. Questo dimostra chi lo ha caricato o lo mantiene segreto?

<details>
<summary>Ragionamento</summary>

No. Confrontare un'impronta adeguata aiuta a verificare che il contenuto corrisponda al riferimento. Non cifra il file né stabilisce l'origine fidata del riferimento. La riservatezza richiede accessi appropriati e, quando necessario, cifratura; la verifica dell'origine richiede un meccanismo fidato adatto al flusso, come una firma verificata. Spiega prima da dove provenga l'hash atteso. Se un attaccante può sostituire sia il file sia il riferimento, il confronto riuscito dà garanzie molto più deboli di quanto il gruppo supponga.

</details>

## 5. Un criterio di Conditional Access richiede MFA per l'app finanziaria. Tutte le applicazioni universitarie sono ora coperte?

<details>
<summary>Ragionamento</summary>

La conclusione va oltre l'ambito del criterio. Rivedi identità destinatarie, applicazioni, condizioni, esclusioni e controlli di concessione. La regola finanziaria può essere corretta mentre altre applicazioni ne restano escluse. Dopo la decisione di accesso valgono ancora i permessi applicativi. Preparerei una matrice dei risultati attesi per utenti e applicazioni diversi, considerando recupero amministrativo e dipendenze, prima di qualsiasi introduzione autorizzata. L'analisi in modalità solo report può aiutare, ma le sue osservazioni non equivalgono a un blocco realmente applicato.

</details>

## 6. Un amministratore è idoneo a un ruolo privilegiato ma non può ancora eseguire l'operazione. PIM non funziona?

<details>
<summary>Ragionamento</summary>

L'idoneità può richiedere l'attivazione prima di rendere utilizzabili i privilegi. Controlla ruolo e ambito previsti, requisiti di attivazione, durata, stato dell'approvazione e assegnazione realmente attiva. Non assegnare permanentemente un ruolo più ampio per far sparire l'errore. PIM modifica quando i privilegi sono disponibili, non rende minimo un ruolo inappropriato. La prova utile è l'attivazione approvata e un'operazione circoscritta con l'identità prevista, non la sola presenza di un'assegnazione idonea.

</details>

## 7. Un ex membro del progetto conserva l'accesso. Serve una revisione degli accessi o un rilevamento di ID Protection?

<details>
<summary>Ragionamento</summary>

La domanda immediata è se un'autorizzazione esistente sia ancora giustificata: è il compito di una revisione degli accessi e del processo aziendale per ingressi, cambi di mansione e uscite. ID Protection riguarda segnali di rischio dell'identità e non decide ogni esigenza organizzativa relativa a una cartella. Indaga separatamente eventuali comportamenti sospetti sostenuti da prove. Identifica proprietario della risorsa, percorso della concessione ed effetti della rimozione su altri progetti. Registra la decisione e le prove necessarie a confermare la rimozione del vecchio accesso.

</details>

## 8. Un messaggio dannoso e un avviso del dispositivo potrebbero essere collegati, ma il dispositivo non invia telemetria. Qual è la prima lacuna?

<details>
<summary>Ragionamento</summary>

La correlazione richiede i dati delle fonti pertinenti. Verifica prodotto supportato, licenza, stato dell'integrazione, associazione dell'identità e arrivo degli eventi alla piattaforma d'indagine. Defender XDR non ricostruisce tutte le prove mancanti del dispositivo soltanto perché esiste un altro avviso. Sentinel può aggiungere analisi tra fonti collegate, ma richiede anch'esso acquisizione e regole utili. Documenterei quali eventi siano presenti, quali manchino e un'ipotesi circoscritta da verificare, prima di sostenere che un pannello rappresenti l'intero attacco.

</details>

## 9. Un documento etichettato Confidential può ancora essere condiviso all'esterno. L'etichetta dimostra un guasto del prodotto?

<details>
<summary>Ragionamento</summary>

Il nome dell'etichetta non dimostra quali protezioni siano configurate né quale regola valga per quel percorso di condivisione. Controlla impostazioni, carico supportato, pubblicazione e ambito dell'etichetta, insieme a condizioni e azioni dei criteri DLP pertinenti. Un'etichetta di sola classificazione può essere valida senza bloccare la condivisione. Definisci prima i casi che dovrebbero essere consentiti e bloccati. Utilizza contenuti sintetici in una prova autorizzata: non distribuire dati realmente riservati solo per dimostrare se un criterio funzioni.

</details>

## 10. Un'indagine richiede attività del mese scorso e messaggi preservati. Un registro di audit equivale a conservazione o backup?

<details>
<summary>Ragionamento</summary>

Queste capacità hanno finalità differenti. Audit fornisce prove delle attività entro disponibilità e conservazione configurate. La conservazione dei contenuti regola mantenimento o eliminazione delle informazioni; eDiscovery può aiutare a individuare e preservare materiale pertinente a un'indagine. Un backup risponde a esigenze di recupero e non viene automaticamente fornito dagli strumenti d'indagine. Determina fonti dei dati, date, autorizzazioni, requisiti di conservazione e blocco, e responsabile. Non promettere prove mai raccolte o contenuti già fuori dal periodo di conservazione applicabile.

</details>

[Guida ufficiale](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) · [Fonti tecniche e spiegazioni](SC-900.md)
