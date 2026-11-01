# SC-300 · 10 casi con risposte motivate

[Guida](SC-300.md) · [Quaderno di esercizi](SC-300-workbook.md) · [Indice](README.md)

Domande originali su un'app universitaria di appunti fittizia, non domande ufficiali d'esame. Spiega il confine di accesso, scarta una scorciatoia inadatta e identifica le prove. Tutti gli esiti sono ipotetici; non sono state effettuate modifiche a tenant reali né esecuzioni cloud.

## 1. Un User Administrator di dipartimento non può leggere un contenitore privato di appunti. Dobbiamo ampliare il ruolo di directory?

<details>
<summary>Risposta</summary>

Identifica prima se l'azione fallita riguarda amministrazione della directory, gestione delle risorse Azure, dati di archiviazione o permessi applicativi. Un ruolo di directory limitato tramite un'unità amministrativa non concede ogni diritto sulle risorse del dipartimento. Ampliarlo agirebbe sul confine sbagliato. Per questo progetto, mappa identità connessa, operazione richiesta, ambito della risorsa e ruolo dati o diritto applicativo pertinente. Le prove devono spiegare perché quella specifica lettura sia consentita o negata senza trasformare un amministratore di dipartimento in un amministratore dell'intero tenant.

</details>

## 2. Abbiamo rimosso l'assegnazione diretta dell'app a uno studente, ma l'accesso rimane. La rimozione non funziona?

<details>
<summary>Risposta</summary>

Una rimozione non dimostra che siano scomparse tutte le concessioni. Esamina assegnazioni dell'app basate su gruppi, fonti delle appartenenze, ruoli applicativi, condivisioni gestite dall'app e identità e tenant effettivamente usati. Secondo la risorsa, possono contare anche assegnazioni ereditate e sessioni esistenti. Non eliminare l'account come primo passo diagnostico. Produci un diagramma dei percorsi di concessione e distingui stato dell'assegnazione e decisione osservata dell'applicazione. Una spiegazione utile identifica percorso residuo, responsabile e prove necessarie per confermare la rimozione a quel confine.

</details>

## 3. Un'università partner segnala il successo di MFA. Ora tutti i suoi docenti possono aprire soluzioni non pubblicate?

<details>
<summary>Risposta</summary>

No. Considerare attendibile un'attestazione MFA supportata tramite impostazioni in ingresso tra tenant può aiutare a soddisfare un requisito di autenticazione con ambito definito; non concede accesso a tutte le risorse universitarie. Esamina impostazioni di accesso applicabili di entrambe le organizzazioni, identità del docente nel tenant della risorsa, applicazione di destinazione e relativo diritto di accesso. Contano anche restrizioni agli inviti e ciclo di vita dell'ospite. Registrerei nella matrice un corso consentito e una soluzione non pubblicata negata. Le prove devono distinguere la garanzia di autenticazione accettata dalla decisione separata di autorizzazione su uno specifico documento.

</details>

## 4. I nuovi redattori non riescono a registrare passkey. L'help desk deve raccogliere le password in un foglio di calcolo?

<details>
<summary>Risposta</summary>

No. Progetta un processo approvato di accesso iniziale e recupero con metodi supportati, eventualmente un Temporary Access Pass per utenti idonei. Verifica ambito del criterio dei metodi di autenticazione, supporto del dispositivo, verifica dell'identità, durata e utilizzo consentiti e consegna sicura. Un TAP è sensibile e temporaneo; non deve comparire nel quaderno o diventare una credenziale permanente condivisa. La consegna descrive risultati previsti di registrazione e scadenza, oltre al responsabile del recupero. Dopo una registrazione passkey riuscita, serve ancora verificare separatamente che durante l'accesso si applichi il criterio previsto di livello di autenticazione.

</details>

## 5. Un criterio Conditional Access report-only registra errori. Ha protetto l'app bloccando quelle richieste?

<details>
<summary>Risposta</summary>

La valutazione report-only non applica i controlli proposti. I suoi risultati supportano la pianificazione, senza provare che quel criterio abbia bloccato una richiesta. Controlla identità e risorse interessate, condizioni, esclusioni, altri criteri applicabili e dettagli dei criteri nell'evento. Documenta l'esito previsto con applicazione dei controlli separatamente dal risultato report-only osservato. Prima di qualsiasi introduzione autorizzata altrove, il progetto deve includere pilota, accesso di recupero, responsabile del rollback e verifica delle licenze. Qui creiamo soltanto quel piano e una matrice degli accessi consentiti e negati.

</details>

## 6. Compare un accesso insolito, mentre un ex docente mantiene il diritto su un corso. Basta un solo criterio di rischio?

<details>
<summary>Risposta</summary>

Sono decisioni diverse. Il rischio di accesso riguarda la richiesta di autenticazione; il rischio utente riguarda una possibile compromissione dell'identità. Indaga rilevamenti e contesto prima di concludere che un accesso insolito sia malevolo. Stabilire se il docente abbia ancora bisogno del corso spetta al responsabile del diritto e al processo di uscita o verifica degli accessi. Un criterio di rischio non può decidere quell'esigenza operativa. Mantieni una cronologia dell'indagine e una decisione separata sul diritto di accesso, con responsabili e prove previste della correzione. Rimuovere accessi obsoleti non risolve di per sé un'identità potenzialmente compromessa.

</details>

## 7. Il nostro indicizzatore notturno ha una richiesta di permesso delegato. Può leggere gli appunti di ogni studente senza un utente?

<details>
<summary>Risposta</summary>

Un permesso delegato dipende da un contesto utente connesso e dal modello di autorizzazione dell'API pertinente. Un carico di lavoro senza interazione utente richiede un'identità applicativa appropriata e permessi applicativi supportati, oppure permessi sulle risorse tramite un'identità gestita. Anche richiedere permessi è diverso dal concedere consenso. Confronta oggetto applicazione, entità servizio locale, API, consensi concessi e ambito delle risorse. Non sostituirli con la password di un docente. Il progetto offline deve spiegare il corpus minimo dell'indicizzatore, perché richiede accesso, chi lo approva e come viene rivisto.

</details>

## 8. Un'identità di compilazione federata riceve un token, ma la distribuzione fallisce. Dobbiamo creare un segreto client permanente?

<details>
<summary>Risposta</summary>

Distingui prima convalida dell'asserzione esterna, emissione del token Entra e autorizzazione sulla risorsa. Confronta emittente, soggetto e destinatari configurati con le attestazioni previste, comprese maiuscole e minuscole, senza registrare token reali. Esamina poi ruolo minimo dell'entità risultante e ambito della distribuzione. L'emissione del token non prova il permesso di modificare la risorsa di destinazione. Un segreto permanente introdurrebbe manutenzione delle credenziali senza spiegare l'errore. Consegna una tabella ipotetica di attestazioni e permessi con un contesto di compilazione previsto e uno rifiutato, più le prove necessarie a ciascun confine.

</details>

## 9. SSO SAML funziona, ma nella piattaforma didattica rimane un account ospite scaduto. SSO è il meccanismo di deprovisioning?

<details>
<summary>Risposta</summary>

Federazione SSO e provisioning degli account hanno compiti diversi. SAML può supportare l'autenticazione mentre un connettore SCIM crea, aggiorna o disattiva separatamente gli account applicativi. Esamina ambito delle assegnazioni, mappature, modifiche alla fonte, log di provisioning e comportamento di rimozione supportato dall'applicazione di destinazione. Non dedurre l'eliminazione dell'account dalla sola scadenza di un pacchetto di accesso o da un accesso riuscito. La registrazione di governance deve nominare il responsabile di ciascun passo e distinguere la rimozione di un diritto Entra dallo stato dell'account a valle. Un'azione di provisioning fallita richiede seguito e prove osservabili del completamento.

</details>

## 10. Un amministratore sottoposto a verifica è idoneo in PIM e una dashboard non mostra errori. L'accesso di manutenzione è dimostrato?

<details>
<summary>Risposta</summary>

Una verifica di accesso può giustificare il mantenimento dell'idoneità, ma attivazione e assegnazione attiva restano separate. Controlla ruolo esatto, ambito, requisiti di attivazione, approvazione, durata e licenze pertinenti. Una dashboard vuota dipende anche da copertura dei log, acquisizione, conservazione, filtri e permessi; non dimostra manutenzione riuscita o assenza di errori. Registra un'attivazione prevista e un'operazione consentita nell'ambito, insieme a un diniego fuori ambito. Tieni decisione di revisione, prove di attivazione e analisi ipotetica dei log come consegne distinte, senza affermare di aver eseguito un'operazione.

</details>

[Guida ufficiale](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) · [Fonti tecniche e spiegazioni](SC-300.md)
