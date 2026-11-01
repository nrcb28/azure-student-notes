# AI-901 · Quaderno avanzato comune

[Guida](AI-901.md) · [Dieci casi](AI-901-cases.md) · [Indice](README.md)

Cinque unità corrispondenti tra le lingue di studio. Lavora offline con appunti universitari, prompt, trascrizioni e risposte candidate inventati. Etichetta ogni output candidato come **sintetico** e ogni risultato atteso come **previsione**. Non caricare materiale reale degli studenti. Questo quaderno non distribuisce nulla e non dimostra una copertura completa dell'esame. Verifica dei riferimenti: **1 novembre 2026**; [obiettivi in vigore dal 15 aprile 2026](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901).

<a id="ai-901-unit-1"></a>

## 1. Definire cinque contratti IA

Scrivi un contratto per ciascuna attività: rispondere a una domanda sul corso, estrarre la scadenza di una consegna, analizzare un testo di feedback, accettare una domanda parlata e descrivere un diagramma. Specifica modalità di input, dati consentiti, struttura dell'output, errori inaccettabili e una soluzione alternativa. Confronta risposte generative, analisi del testo, voce, visione e Content Understanding in base a ciò che producono. Includi una richiesta di generazione di immagini per distinguere creazione e interpretazione.

**Scenario:** un compagno propone un solo modello di immagini per ogni funzione. **Prove:** una matrice decisionale di cinque righe con una scelta motivata della capacità e un'alternativa scartata per ogni riga. Aggiungi domande di selezione del modello su modalità, opzioni di distribuzione, lingua e parametri supportati. Lascia i dettagli sconosciuti del servizio contrassegnati per la verifica nella documentazione attuale, senza inventare limiti.

<a id="ai-901-unit-2"></a>

## 2. Scrivere prompt ancorati alle fonti e regole di accesso

Inventa tre brevi passaggi: un appunto di lezione consentito, un quaderno privato e una pagina consentita contenente un'istruzione a esportare documenti. Assegna identificatori stabili alle fonti e due studenti con elenchi di accesso diversi. Scrivi prompt di sistema e utente che richiedano una risposta sostenuta dalle fonti, preservino i confini delle fonti e permettano l'astensione. Il recupero deve filtrare in base all'accesso del chiamante prima di costruire il contesto; il prompt non può fornire quel confine di sicurezza.

**Scenario:** una domanda non ha risposta nei passaggi consentiti. **Prove:** un'astensione prevista, un rifiuto di accesso vietato e una risposta sintetica resistente all'injection. Annota quali affermazioni sostiene ogni fonte. Spiega perché una citazione o un rilevatore di attacchi, da soli, non possono dimostrare verità, privacy o autorizzazione.

<a id="ai-901-unit-3"></a>

## 3. Seguire un client leggero senza chiamate cloud

Disegna una richiesta da un client Python all'endpoint Foundry previsto e alla distribuzione configurata, seguita da una risposta o un errore. Distingui identità, autorizzazione, destinazione e selezione della distribuzione. Abbozza pseudocodice che legga una configurazione protetta, ottenga una credenziale appropriata, invii input consentito, controlli errori e output e mostri un risultato sicuro. Etichetta lo schema come **pseudocodice**, non come codice SDK eseguibile. Spiega dove potrebbero comparire dizionari, iterazione, eccezioni e chiamate asincrone.

**Scenario:** l'autenticazione riesce ma la risorsa selezionata nega l'operazione. **Prove:** una lista di controlli diagnostici depurata dai dati sensibili e il comportamento previsto del client per accesso negato, timeout, output vuoto e configurazione non valida. Confronta come REST, SDK e CLI esprimono lo stesso compito. Identifica l'attuale [guida rapida all'SDK](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) che seguiresti nella successiva pratica cloud.

<a id="ai-901-unit-4"></a>

## 4. Convalidare l'estrazione multimodale

Inventa un foglio di consegna con una scadenza finale, un secondo foglio senza data, un diagramma con un'unità illeggibile e una domanda parlata rumorosa. Definisci uno schema delle scadenze con tipi dei campi, regola per i valori mancanti e riferimenti alle fonti. Produci output sintetici volutamente errati: una data indovinata, un'unità sbagliata e un termine tecnico frainteso. Individua l'errore in estrazione, interpretazione visiva, riconoscimento o ragionamento successivo. Descrivi un percorso di riconoscimento vocale e un'alternativa multimodale diretta supportata.

**Scenario:** un output è JSON valido ma contraddice il foglio. **Prove:** risultati separati di convalida dello schema e della fonte, regole di revisione per le ambiguità e un'alternativa testuale per l'accessibilità. Includi come [Content Understanding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) potrebbe elaborare input di documenti, immagini, audio e video. Non trattare la confidenza come sostituto delle prove.

<a id="ai-901-unit-5"></a>

## 5. Valutare un singolo agente con strumenti limitati

Progetta un agente di ricerca negli appunti con istruzioni, scelta del modello, recupero limitato all'ambito del chiamante e nessuno strumento di modifica. Definisci richiesta e risultato del suo strumento di ricerca e come un client identifichi l'agente e mantenga il contesto della conversazione. Crea una matrice degli errori con almeno sei righe: risposta sostenuta da prove, prove mancanti, documento negato, injection, scadenza in conflitto e timeout dello strumento. Aggiungi gli esiti previsti prima di scrivere due risposte sintetiche candidate per ogni riga.

**Prove finali:** consegna contratti, prompt, elenchi di accesso, schema del client, verifiche dell'estrazione e matrice valutata. Valuta separatamente supporto fattuale, citazioni, astensione e rifiuto, privacy, validità dello schema e permessi degli strumenti. Spiega una revisione del prompt e il suo compromesso. Elenca la pratica diretta ancora necessaria: distribuzione del modello e interazione nel portale, un client di chat SDK effettivo, un singolo agente provato nel portale e il suo client. La valutazione offline prepara a quel lavoro.
