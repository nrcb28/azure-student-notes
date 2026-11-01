# SC-200 · Quaderno di decisioni e prove

[Guida](SC-200.md) · [Dieci casi](SC-200-cases.md) · [Indice](README.md)

Cinque unità originali per un'app universitaria di appunti fittizia. Lavora offline con record e identificatori inventati. Etichetta i risultati previsti separatamente dalle osservazioni fornite nell'esercizio. Non si richiedono né si dichiarano accessi a tenant, distribuzioni cloud, query reali, invii di messaggi o contenimenti.

<a id="sc-200-unit-1"></a>

## 1. Mappare i confini di raccolta e accesso

Disegna Microsoft 365, un'applicazione Azure, un server locale e un firewall del campus. Assegna dove appropriato l'indagine a Defender XDR oppure la raccolta e l'analisi a Sentinel. Per ogni fonte, specifica onboarding, prerequisiti del connettore, tabella e colonna temporale previste, identificatori stabili, ritardo, conservazione e un responsabile. Separa permessi di lettura, gestione incidenti, creazione di regole e automazione.

**Scenario:** il connettore del firewall risulta collegato, ma manca l'evento richiesto. **Prove:** una tabella di copertura delle quattro fonti, una domanda sul corretto funzionamento della raccolta e un evento sintetico con schema previsto. **Consegna:** un diagramma e un elenco delle lacune che spieghino le conclusioni consentite all'analista. Includi regole per dati personali ed esportazioni; non raccogliere informazioni reali sugli studenti.

<a id="sc-200-unit-2"></a>

## 2. Costruire una cronologia dell'incidente sostenuta da prove

Inventa sei record relativi a email, identità, endpoint, applicazione e carico di lavoro cloud. Assegna a ciascuno orario UTC dell'evento, orario di acquisizione, ID sorgente, identificatori delle entità e osservazione. Raggruppa avvisi correlati in un incidente proposto senza assumere che un IP condiviso del campus provi la relazione. Separa ambito noto, ambito sospetto e telemetria indisponibile.

**Scenario:** un messaggio sospetto precede un apparente accesso a un documento privato. **Prove:** cronologia, mappa delle entità, una spiegazione alternativa e un record mancante richiesto. **Consegna:** una nota di triage con responsabile, motivazione della priorità, contenimento proposto, requisito di autorizzazione, impatto sul servizio e condizione di ripristino. Segna ogni azione proposta come non eseguita; una conferma prevista non è una risposta osservata.

<a id="sc-200-unit-3"></a>

## 3. Spiegare i risultati delle query prima di fidarsi dei conteggi

Leggi il dataset KQL sintetico fisso della guida. Segui le righe attraverso intervallo UTC semiaperto, filtro Denied, deduplicazione e aggregazione. Spiega perché il risultato previsto è due eventi per `student-a`. Aggiungi una seconda tabella inventata con due righe per quell'account e disegna gli abbinamenti prodotti da un inner join esplicito. Confrontali con la deduplicazione del lato sinistro eseguita dal tipo predefinito `innerunique`.

**Scenario:** un rapporto scambia righe unite per attacchi distinti. **Prove:** conteggi intermedi delle righe, chiavi di join, ipotesi sugli identificatori e un esempio sul limite temporale. **Consegna:** un'interpretazione corretta con output previsto e limiti. Non si dichiara alcuna esecuzione di query; eventuali calcoli locali restano distinti dalle osservazioni in un tenant.

<a id="sc-200-unit-4"></a>

## 4. Trasformare un'ipotesi di ricerca in una revisione del rilevamento

Scrivi un'ipotesi che colleghi la ricezione di messaggi sospetti ad accessi insoliti a file privati. Definisci popolazione, intervallo UTC, fonti necessarie e spiegazione alternativa. Crea quattro esempi sintetici leciti e quattro preoccupanti, tutti etichettati. Proponi un rilevamento e un'eccezione circoscritta, poi identifica quali esempi genererebbero un avviso, sfuggirebbero o richiederebbero più contesto. Spiega come ASIM potrebbe normalizzare fonti compatibili e dove vanno convalidate le mappature dei parser.

**Scenario:** un'importazione autorizzata somiglia a un uso improprio. **Prove:** una tabella decisionale con versione, lacune nelle fonti, analisi di falsi positivi e falsi negativi e una verifica della mappatura del parser. **Consegna:** una raccomandazione di ottimizzazione. Una ricerca vuota e meno avvisi non dimostrano assenza di compromissione o copertura completa.

<a id="sc-200-unit-5"></a>

## 5. Rivedere un flusso di risposta assistita

Schematizza una regola di automazione che richiami un playbook per arricchire le informazioni e richieda approvazione prima di un contenimento che interrompa servizi. Identifica separatamente operatore, permesso di invocazione di Sentinel, identità del flusso e ambito delle operazioni successive. Simula un'attivazione duplicata e un timeout; documenta identificatori e controlli dello stato che impediscono ticket duplicati o restrizioni ripetute inutilmente. Includi un responsabile e condizioni di ripristino.

**Scenario:** un riepilogo IA collega un avviso cloud al download di uno studente senza un log applicativo. **Prove:** una tabella che associ affermazioni a fonti, una conclusione corretta, il confine dell'approvazione e il comportamento previsto dei nuovi tentativi. **Consegna:** un runbook di simulazione revisionato. Verifica i suggerimenti di Copilot rispetto ai record forniti e alla semantica delle query. Non viene inviata alcuna notifica, richiesta di approvazione o risposta reale.

[Guida ufficiale allo studio](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · [Fondamenti di osservabilità](../../it/08-observability.md)
