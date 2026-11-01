# AI-103 · Quaderno avanzato per sviluppatori

[Guida](AI-103.md) · [Dieci casi](AI-103-cases.md) · [Indice](README.md)

Cinque unità corrispondenti usano appunti universitari inventati e fixture offline di richiesta e risposta. Etichetta gli output candidati come **sintetici** e il comportamento atteso come **previsione**. Non servono risorse cloud, credenziali, dati reali degli studenti o misure del servizio. Questi esercizi sviluppano capacità di implementazione selezionate senza dichiarare una copertura completa. Verificato il **1 novembre 2026** rispetto agli [obiettivi in vigore dal 16 aprile 2026](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103).

<a id="ai-103-unit-1"></a>

## 1. Fissare un contratto client e una decisione di distribuzione

**Scenario:** l'app di appunti deve restituire una risposta ancorata alle fonti da un backend Python durante il picco del ripasso. Definisci fixture di richiesta e risposta con contesto di identità, ID della richiesta, corso, esito, risposta, citazioni e categorie di errore. Includi JSON non valido, accesso negato, timeout e output parziale. Crea un manifesto di compatibilità per risorsa/progetto, tipo di endpoint, nome della distribuzione, generazione API, versioni dei pacchetti e approccio alle credenziali, usando l'attuale [guida SDK](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview).

**Prove:** confronta due modelli candidati ipotetici su qualità, funzionalità supportate, capacità, latenza e uso delle risorse; segnala ciò che resta ignoto per una verifica successiva. **Consegna:** uno schema di contratto tipizzato, quattro fixture di errore e una decisione di distribuzione motivata senza limiti o prezzi inventati.

<a id="ai-103-unit-2"></a>

## 2. Progettare il recupero fino alla revoca dell'accesso

**Scenario:** due studenti condividono un notebook finché l'accesso di uno viene revocato. Inventa sei passaggi, compresa una precisazione della consegna divisa dal confine proposto di un blocco. Definisci ID dei documenti e dei blocchi, versioni, posizioni nelle fonti, metadati ACL e una versione di indice/embedding. Confronta le previsioni di recupero per parole chiave, vettoriale e ibrido. Disegna autenticazione del chiamante, filtro dei permessi, recupero, consultazione della cache e contesto del modello nell'ordine effettivo.

**Prove:** una tabella di accesso prima e dopo che copra propagazione nell'indice, blocchi in cache e memoria della conversazione, più una citazione non supportata e una risposta con prove mancanti. **Consegna:** un progetto di recupero con politica di aggiornamento dei permessi, regola di invalidazione e quattro casi di regressione. Spiega come i [modelli di accesso di Search](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) influenzano la scelta implementativa.

<a id="ai-103-unit-3"></a>

## 3. Tracciare uno strumento approvato dall'esito incerto

**Scenario:** un agente di appunti propone di condividere un documento consentito con un gruppo di studio. Definisci schema dello strumento, ambito del chiamante, payload esatto dell'approvazione, chiave dell'operazione, archivio degli stati, budget di timeout e proprietà della conversazione. Abbozza **pseudocodice** per convalida → autorizzazione → approvazione → esecuzione → riconciliazione → resoconto; è un progetto applicativo, non codice SDK eseguibile. Aggiungi un passaggio tra pianificatore e recuperatore che preservi gli stessi permessi.

**Prove:** tracce per rifiuto, esecuzione riuscita, consegna duplicata, approvazione scaduta e risposta persa dopo il successo del backend. **Consegna:** una tabella delle transizioni di stato e una traccia con dati sensibili oscurati che mostri perché un nuovo tentativo non può duplicare la condivisione. Collega il progetto all'attuale [confine del function calling](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling).

<a id="ai-103-unit-4"></a>

## 4. Convalidare campi multimodali e significato

**Scenario:** un foglio di consegna contiene scadenze della bozza e della versione finale, un grafico ha un asse illeggibile e una domanda vocale contiene “mutex”. Definisci contratti distinti per testo, voce, comprensione visiva, generazione di media ed estrazione. Scrivi uno schema di campi Content Understanding con descrizioni precise, tipi, gestione dei null e riferimenti alle fonti. Costruisci output sintetici difettosi: scadenze scambiate, un'unità inventata e un termine tecnico riconosciuto male.

**Prove:** controlli separati di schema, fonte, significato e accessibilità, compresi un campo sbagliato ad alta confidenza e un'alternativa di correzione testuale. **Consegna:** cinque fixture annotate e una politica di revisione calibrata con esempi etichettati. Verifica [progettazione dell'analizzatore](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/best-practices) e [disponibilità del grounding nei documenti](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/document/analyzer-improvement), mantenendo espliciti i limiti di modalità e API.

<a id="ai-103-unit-5"></a>

## 5. Valutare e provare un ripristino

**Scenario:** un rilascio candidato cambia prompt, schemi degli strumenti e un modello di embedding. Valuta otto casi fissi: risposta supportata, fonte mancante, accesso revocato, injection, citazione sbagliata, scadenza ambigua, timeout dello strumento e azione duplicata. Tieni separate qualità del recupero, supporto delle affermazioni, sicurezza, rispetto dei permessi e previsioni di latenza. Descrivi una distribuzione graduale limitata e le metriche che farebbero scattare il recupero.

**Prove:** un foglio di confronto, un manifesto di rilascio compatibile, uno schema di telemetria ripulito dai dati sensibili e una sequenza di ripristino che riporti insieme client, indice, prompt e strumenti. **Consegna:** un pacchetto di rilascio revisionabile e un elenco delle misure che richiedono ancora un laboratorio cloud autorizzato. Usa la [guida alla valutazione](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation) per distinguere previsioni offline e prove osservate della distribuzione; non presentare punteggi sintetici come risultati Azure.
