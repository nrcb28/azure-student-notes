# SC-300 · Quaderno di decisioni di accesso e governance

[Guida](SC-300.md) · [Dieci casi](SC-300-cases.md) · [Indice](README.md)

Cinque unità offline originali per un'app universitaria di appunti fittizia. Usa identità e documenti sintetici. Non modificare criteri del tenant, creare credenziali, attivare ruoli o collegare telemetria reale. Le consegne descrivono decisioni previste; non si dichiara alcuna esecuzione cloud.

<a id="sc-300-unit-1"></a>

## 1. Tracciare accesso effettivo e fonti delle identità

Mappa tenant, sottoscrizione, app e archivio documenti. Separa ruoli di directory, ambito delle unità amministrative, ruoli Azure per risorse e dati e diritti applicativi. Includi percorsi di concessione diretti e basati su gruppi e identifica chi controlla le appartenenze. Per un'identità ibrida, annota la fonte autorevole e le ipotesi scelte su sincronizzazione e autenticazione; evita di trattare la sincronizzazione come una concessione di accesso.

**Scenario:** uno studente perde un'assegnazione diretta ma riesce ancora a leggere una cartella del corso. **Prove:** un diagramma con due possibili percorsi di concessione e i record necessari per distinguerli. **Consegna:** una matrice decisionale di sei righe per studente, ospite, redattore, amministratore, indicizzatore ed ex membro, con ambito minimo e un diniego previsto per ciascuno.

<a id="sc-300-unit-2"></a>

## 2. Progettare autenticazione e Conditional Access

Specifica un metodo di autenticazione supportato, percorso di registrazione e responsabile del recupero. Spiega la resistenza al phishing e dove un Temporary Access Pass potrebbe avviare l'accesso di un utente idoneo senza conservare un codice reale. Descrivi destinatari dei criteri, condizioni, controlli di concessione e sessione, esclusioni, ipotesi sulle licenze e recupero di emergenza. Tieni le valutazioni report-only separate dagli esiti con controlli applicati.

**Scenario:** un docente ospite usa un dispositivo personale, mentre un redattore gestisce soluzioni non pubblicate. **Prove:** tre richieste previste con identità, metodi, dispositivi o risorse diversi; spiega l'attendibilità delle attestazioni tra tenant separatamente dal diritto applicativo. **Consegna:** una matrice di criteri proposta e una nota di introduzione con criteri per pilota, revisione, recupero e rollback. Non viene abilitato nulla in un tenant reale.

<a id="sc-300-unit-3"></a>

## 3. Scegliere e limitare le identità dei carichi di lavoro

Confronta una registrazione dell'app, la relativa entità servizio e un'identità gestita per l'indicizzatore. Spiega permessi delegati e applicativi, consenso e ambito delle risorse. Per una compilazione esterna fittizia, documenta emittente, soggetto e destinatari previsti per la federazione usando valori di attestazione inventati. Dichiara perché il successo dell'emissione del token non stabilisce il permesso di distribuire.

**Scenario:** l'indicizzatore legge solo appunti pubblicati, mentre la compilazione aggiorna solo la propria applicazione di test. **Prove:** un'operazione consentita e una rifiutata per ogni carico di lavoro, più un responsabile dei permessi e una data di revisione. **Consegna:** una tabella di scelta delle identità e uno schema della relazione di trust federata, senza password, segreti client, token reali o comandi di distribuzione. Annota le ipotesi non supportate come domande per il responsabile.

<a id="sc-300-unit-4"></a>

## 4. Costruire il ciclo di vita di diritti e privilegi

Separa idoneità PIM, attivazione e durata attiva dalle verifiche periodiche degli accessi. Proponi un pacchetto di accesso per docenti ospiti e automazione supportata del ciclo di vita per ingressi, trasferimenti e uscite. Distingui federazione SSO e provisioning SCIM e spiega come confermare la rimozione a valle. Elenca ipotesi sulle licenze delle singole funzionalità e responsabili dell'automazione non riuscita.

**Scenario:** termina il semestre di un docente mentre un amministratore richiede accesso temporaneo di manutenzione. **Prove:** una decisione di scadenza, una verifica del proprietario della risorsa, una proposta di attivazione con ambito delimitato e una registrazione del completamento del provisioning a valle. **Consegna:** una tabella di governance con trigger, approvatore, diritto, durata, revisione, rimozione prevista, prove e gestione delle eccezioni. Una verifica completata non dimostra l'attivazione di un ruolo.

<a id="sc-300-unit-5"></a>

## 5. Spiegare un errore con prove delimitate

Separa rischio utente, rischio di accesso, valutazione dei criteri, modifiche della directory ed errori di provisioning. Scegli i log pertinenti e descrivi ipotesi su instradamento diagnostico, conservazione, accesso e schema. Annota sulla query KQL ipotetica della guida ciò che l'aggregato può e non può stabilire. Aggiungi Private Access, Internet Access o il profilo di traffico Microsoft solo dove il percorso verso la risorsa ne renda pertinente lo scopo.

**Scenario:** un ospite non riesce ad aprire un corso, ma una dashboard non mostra errori corrispondenti. **Prove:** una cronologia ipotetica, lacune di copertura, campi di correlazione e due spiegazioni alternative. **Consegna:** una diagnosi di una pagina e un elenco di prove che colleghino identità, percorso di rete, criterio, diritto applicativo e provisioning. Etichetta ogni risultato come previsto; non si eseguono query o prove su tenant.

[Guida allo studio Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) · [Fondamenti di identità](../../it/06-identity.md)
