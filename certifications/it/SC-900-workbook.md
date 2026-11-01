# SC-900 · Quaderno di decisioni e prove

[Guida](SC-900.md) · [Dieci casi](SC-900-cases.md) · [Indice](README.md)

Cinque unità originali per applicare gli stessi obiettivi in ogni lingua. Usa un'università immaginaria e dati sintetici. Sono esercizi di progettazione senza connessione: non si dichiarano distribuzioni di criteri, modifiche del tenant o esecuzioni completate in Azure.

<a id="sc-900-unit-1"></a>

## 1. Descrivere responsabilità e confini di fiducia

Disegna browser, fornitore di identità, applicazione e archivio dei documenti. A ogni confine indica che cosa venga verificato e chi gestisca il controllo pertinente. Separa i compiti del fornitore sulla piattaforma dalle decisioni dell'organizzazione su utenti, condivisione, configurazione e dati. Spiega perché la rete del campus non basti a dimostrare che una richiesta sia affidabile.

**Scenario:** un ospite deve leggere appunti pubblicati, mai soluzioni non pubblicate. **Prove:** diagramma e tabella con due operazioni consentite e due negate, relativi responsabili e osservazioni necessarie a verificarle. **Consegna:** una pagina che distingua risultati attesi e risultati realmente osservati. Per questo esercizio non effettuare prove su un tenant reale.

<a id="sc-900-unit-2"></a>

## 2. Progettare una decisione di accesso

Specifica tipo di identità, applicazione destinataria, azione richiesta e autorizzazione minima. Proponi un requisito di autenticazione e spiegane categorie dei fattori e proprietà di resistenza al phishing. Descrivi quali segnali di Conditional Access conterebbero e quali verifiche applicative resterebbero necessarie. Documenta ambito, esclusioni, recupero e dipendenze di licenza, invece di scrivere soltanto «attivare MFA per tutti».

**Scenario:** un docente ospite accede ai materiali da un dispositivo personale. **Prove:** decisioni attese per una richiesta consentita, un metodo di autenticazione insufficiente e una richiesta oltre i suoi diritti. **Consegna:** matrice di accesso motivata. Mantieni l'esercizio ipotetico; non modificare controlli del tenant e non scambiare osservazioni in modalità solo report per decisioni applicate.

<a id="sc-900-unit-3"></a>

## 3. Separare privilegio, autorizzazione e rischio

Scrivi tre domande: chi può attivare un ruolo privilegiato, chi deve mantenere un accesso al progetto e quale comportamento dell'identità merita un'indagine? Associale rispettivamente ai concetti di PIM, revisione degli accessi e rischio dell'identità. Definisci ambito e durata del ruolo senza supporre che un ruolo ampio e temporaneo sia automaticamente minimo.

**Scenario:** un ex membro resta in un gruppo mentre un amministratore deve eseguire manutenzione temporanea. **Prove:** percorsi delle concessioni, decisione del proprietario della risorsa, processo di attivazione proposto e registrazioni distinte di eventuali comportamenti sospetti. **Consegna:** una breve procedura che spieghi chi approvi ogni decisione e cosa ne confermerebbe il completamento. Il quaderno non richiede di creare assegnazioni privilegiate.

<a id="sc-900-unit-4"></a>

## 4. Pianificare rilevamento e risposta circoscritta

Scegli una catena d'attacco ipotetica che coinvolga posta, identità e un carico di lavoro. Elenca gli eventi necessari a sostenere o respingere l'ipotesi. Spiega dove sia utile la correlazione di Defender XDR e dove contino connettori, analisi e orchestrazione della risposta di Sentinel. Segna i dati mancanti: un risultato vuoto non dimostra che l'evento non sia mai avvenuto.

**Scenario:** attività di accesso sospetta dopo un messaggio di phishing. **Prove:** sequenza temporale, copertura delle fonti, analista responsabile e notifica proposta prima di azioni che interrompano il servizio. **Consegna:** tabella di rilevamento e risposta con falsi positivi e recupero. Questo esercizio non acquisisce telemetria, non attiva servizi a pagamento e non blocca automaticamente account.

<a id="sc-900-unit-5"></a>

## 5. Seguire il ciclo di vita dei dati sensibili

Segui un documento sintetico dalla creazione a uso interno, condivisione, indagine ed eliminazione finale. Distingui classificazione, protezione configurata, gestione DLP, conservazione, prove di audit ed eDiscovery. Registra le ipotesi su carichi e licenze per ogni capacità proposta. Un punteggio di conformità non sostituisce la valutazione degli obblighi reali dell'organizzazione.

**Scenario:** una soluzione fittizia deve restare privata fino alla pubblicazione e alcuni messaggi vanno preservati per un'indagine. **Prove:** decisioni di gestione attese, registrazioni delle attività necessarie, ipotesi di conservazione e responsabile nominato. **Consegna:** tabella del ciclo di vita che spieghi perché nessuna singola etichetta, registrazione o copia di backup soddisfi tutto. Considera gli obblighi legali come requisiti forniti da un responsabile autorizzato.

[Guida Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900)
