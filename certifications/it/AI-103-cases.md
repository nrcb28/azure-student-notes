# AI-103 · 10 casi di sviluppo con risposte ragionate

[Guida](AI-103.md) · [Quaderno di esercizi](AI-103-workbook.md) · [Indice](README.md)

Scenari originali di un'app universitaria di appunti, non domande d'esame. Tutti gli output e i tempi proposti sono ipotetici. Spiega la decisione di implementazione e le prove necessarie prima di aprire ogni risposta. Verifica dei riferimenti: **1 novembre 2026**.

## 1. Un esempio Python si importa correttamente, ma la sua risposta non contiene la proprietà prevista. Il gruppo deve cambiare la distribuzione finché funziona?

<details>
<summary>Risposta</summary>

Esamina prima versione SDK installata, generazione API, operazione, endpoint e struttura documentata della risposta. Il successo dell'importazione dimostra poco sulla compatibilità con un esempio copiato. Fissa un insieme coerente di dipendenze e mappa una fixture di risposta ripulita dai dati sensibili sul contratto dell'app. Distingui una proprietà mancante da un errore di autenticazione o da una distribuzione sconosciuta. Cambiare modello non può correggere un client che legge l'oggetto sbagliato. Registra URL della documentazione e versioni dei pacchetti, poi verifica una chiamata reale solo in un laboratorio autorizzato separatamente.

</details>

## 2. Un modello più grande migliora i riepiloghi ma raddoppia la latenza ipotetica nella settimana di ripasso. Quale modello va rilasciato?

<details>
<summary>Risposta</summary>

Usa lo stesso insieme rappresentativo di valutazione e le stesse ipotesi di carico per entrambi i candidati. Misura supporto delle affermazioni, accuratezza delle citazioni, astensione, output strutturato, distribuzione della latenza, velocità di elaborazione e uso delle risorse. Decidi quali requisiti sono obbligatori prima di confrontare le medie. Un modello più piccolo potrebbe gestire le domande ordinarie, con un'escalation limitata per quelle difficili, ma anche questo instradamento richiede valutazione. Includi tempo di recupero e nuovi tentativi nel budget. Né la dimensione del modello né un singolo riepilogo convincente determinano la distribuzione migliore; registra un compromesso motivato tra qualità, capacità, latenza e costo senza inventare prezzi.

</details>

## 3. Uno studente perde l'accesso a un notebook condiviso, ma i blocchi in cache rispondono ancora alla sua domanda. Il filtro dell'indice è sufficiente?

<details>
<summary>Risposta</summary>

L'intero percorso di recupero deve applicare l'accesso corrente prima che il contesto raggiunga il modello. Esamina propagazione dei permessi ai blocchi figli, aggiornamenti dell'indice, memoria della conversazione e cache. Le chiavi di cache richiedono un contesto adeguato di identità e permessi, e la revoca richiede invalidazione o un altro controllo di aggiornamento. Una query corretta sull'indice non può proteggere una risposta servita da una vecchia cache senza restrizioni. Scrivi una politica sull'aggiornamento accettabile dei permessi e nega l'accesso quando non è rispettabile. Dimostra il rifiuto con due identità sintetiche e una traccia prima e dopo la revoca.

</details>

## 4. Una risposta cita il PDF corretto della lezione ma attribuisce una scadenza a un paragrafo che definisce solo un algoritmo. La presenza della citazione supera la valutazione?

<details>
<summary>Risposta</summary>

No. Convalida che passaggio e versione citati sostengano davvero l'affermazione. Esistenza della fonte, pertinenza della fonte e supporto dell'affermazione sono controlli distinti. Esamina se il recupero ha omesso la pagina della consegna, se la suddivisione ha perso contesto o se la generazione ha inventato una data nonostante prove sufficienti. L'app deve astenersi quando i passaggi autorizzati non contengono la scadenza. Conserva l'esempio fallito nella valutazione di regressione e valuta la correttezza delle citazioni separatamente dalla leggibilità. Un collegamento alla fonte che si apre correttamente è utile per navigare, ma non dimostra che la risposta sia ancorata alle prove.

</details>

## 5. Un agente va in timeout dopo aver richiesto uno strumento di condivisione; il backend ha già creato la condivisione. Il client deve riprovare subito?

<details>
<summary>Risposta</summary>

Tratta l'esito come sconosciuto finché non viene riconciliato. Assegna all'operazione applicativa approvata una chiave di idempotenza stabile e registrane lo stato indipendentemente dalla risposta del modello. Interroga o recupera quello stato prima di inviare nuovamente; i tentativi non devono creare un'altra condivisione. Vincola l'approvazione a documenti, destinatari e versioni esatti, poi ricontrolla l'autorizzazione in esecuzione. Distingui la scadenza dello strumento dal budget complessivo dell'agente. Raccogli identificatori di correlazione ripuliti, così la traccia collega richiesta, approvazione, completamento del backend e risposta persa senza esporre contenuti degli studenti.

</details>

## 6. Un agente pianificatore delega a un agente di recupero che può leggere tutti i corsi. Il prompt ristretto del pianificatore preserva i permessi degli studenti?

<details>
<summary>Risposta</summary>

Il passaggio di consegne deve trasportare un contesto attendibile del chiamante e lo strumento di recupero deve applicarne i permessi. Il prompt del pianificatore non può limitare in modo affidabile un servizio privilegiato a valle. Definisci per ogni agente ruolo, ambito degli strumenti, campi ammessi nel passaggio, proprietà della memoria e budget di terminazione. Restituisci al pianificatore solo prove autorizzate e impedisci che la conversazione di uno studente riutilizzi la memoria di un altro. Prova una richiesta a un corso negato e un passaggio contenente injection. Delegare il lavoro può dividere le responsabilità, ma non deve mai ampliare silenziosamente l'accesso dell'utente finale.

</details>

## 7. L'app richiede la descrizione di un grafico e un nuovo poster di ripasso. Entrambe le richieste possono usare lo stesso contratto visivo?

<details>
<summary>Risposta</summary>

Definisci contratti separati per comprendere prove esistenti e creare nuovi media, anche se una piattaforma supporta entrambi. La risposta sul grafico richiede supporto da etichette, unità e relazioni visibili, con astensione per aree illeggibili. Il poster richiede controlli di generazione, diritti adeguati sulle fonti, verifiche di sicurezza e revisione di testo e diagrammi generati. Le varianti video richiedono anche una semantica per segmenti o modifica. Verifica l'utilità del testo alternativo ed evita di dedurre dettagli invisibili. Un'illustrazione generata convincente non può convalidare un'affermazione sul grafico originale della lezione.

</details>

## 8. Il riconoscimento vocale cambia “mutex” in “music” e la traduzione produce poi un testo scorrevole ma privo di senso. Va rivisto solo il prompt di traduzione?

<details>
<summary>Risposta</summary>

Esamina le fasi rispetto ai loro contratti distinti. Un errore di riconoscimento a monte può diventare testo tradotto scorrevole ma errato e una risposta sbagliata. Costruisci esempi con lessico tecnico, rumore, negazioni e interruzioni; conserva un percorso di correzione testuale e verifica le personalizzazioni di dominio supportate dal servizio scelto. Se un progetto direttamente multimodale non espone la trascrizione, valuta la stessa conservazione del significato da un'estremità all'altra. Registra errori specifici per lingua invece di nasconderli nelle medie. La modifica del prompt è giustificata solo dopo aver individuato la fase e misurato l'effetto.

</details>

## 9. Content Understanding restituisce con alta confidenza la scadenza della bozza in `final_due_date`. La proposta per il calendario può proseguire?

<details>
<summary>Risposta</summary>

Il valore viola il significato previsto del campo nonostante la confidenza. Definisci chiaramente il campo della consegna finale, esaminane il grounding nel documento e confrontalo con esempi etichettati di bozza e consegna finale. Convalida formato, valori mancanti e coerenza con le altre tappe. Invia le ambiguità irrisolte alla revisione; la confidenza è una stima, non una decisione sulle regole operative. Verifica che API e configurazione scelte espongano le prove necessarie. Un'azione a valle su calendario o condivisione richiede inoltre autorizzazione e approvazione proprie, indipendentemente dalla qualità dell'estrazione o dalla validità del JSON.

</details>

## 10. Un rilascio cambia prompt, modello di embedding e schema di risposta degli strumenti; aumentano gli errori di citazione. Basta ripristinare il prompt?

<details>
<summary>Risposta</summary>

Usa il manifesto di rilascio per identificare tutti i componenti cambiati e la loro compatibilità. Una nuova rappresentazione di embedding può richiedere la reindicizzazione, mentre un vecchio client può leggere male un nuovo risultato di strumento. Confronta tracce e casi di regressione per localizzare il guasto, poi ripristina un insieme compatibile noto per il buon funzionamento o esegui la migrazione documentata. Definisci condizioni di ripristino per grounding, accesso, errori degli strumenti e latenza prima della distribuzione graduale. Conserva identificatori di versione nella telemetria ripulita dai dati sensibili. Ripristinare un singolo prompt visibile non può correggere in modo affidabile cambiamenti nelle rappresentazioni del recupero o nei contratti di risposta applicativi.

</details>

Fonti: [obiettivi attuali](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103), [SDK ed endpoint](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview), [valutazione](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation), [accesso ai documenti](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview), [function calling](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling), [progettazione dell'analizzatore](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/best-practices), [confidenza e grounding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/document/analyzer-improvement).
