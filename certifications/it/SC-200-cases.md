# SC-200 · 10 casi con risposte motivate

[Guida](SC-200.md) · [Quaderno di esercizi](SC-200-workbook.md) · [Indice](README.md)

Scenari di studio originali, non domande ufficiali d'esame. Usa l'app universitaria di appunti fittizia e record sintetici. Dichiara il requisito, scarta un'alternativa allettante e identifica le prove mancanti. Sono simulazioni offline su carta; non si eseguono query su tenant, invii di messaggi o azioni di risposta.

## 1. In Defender XDR compaiono avvisi Microsoft 365, ma manca il firewall del campus. XDR lo copre già?

<details>
<summary>Risposta</summary>

No. Le prove Microsoft 365 presenti non dimostrano la copertura del firewall. Inventaria il percorso di esportazione supportato dal firewall e l'analisi richiesta, poi valuta un connettore Sentinel adeguato e i suoi prerequisiti. Correlazione in Defender XDR e raccolta in Sentinel hanno scopi collegati, ma nessuna delle due inventa la telemetria mancante. Chiederei tabella prevista, schema, identificatori sorgente, ambito di raccolta ed esempi di orari di arrivo. La consegna della simulazione è una mappa della copertura con fonti presenti e mancanti, distinguendo l'acquisizione prevista dalle osservazioni effettivamente fornite.

</details>

## 2. Un connettore indica Connected, ma una query non restituisce righe sui dispositivi. L'analista deve chiudere l'indagine?

<details>
<summary>Risposta</summary>

No. Controlla onboarding dei dispositivi, requisiti di licenza e servizio, tipi di evento selezionati nel connettore, tabella di destinazione, permessi dell'analista, intervallo UTC, ritardo di acquisizione e conservazione. Una tabella può usare campi diversi dallo schema assunto dalla query. Connected segnala una configurazione, senza provare che ogni evento richiesto sia arrivato. Chiudere il caso confonderebbe la visibilità mancante con un comportamento lecito. Annota le prove assenti e chiedi al responsabile della fonte un campione delimitato di eventi sintetici e prove del corretto funzionamento della raccolta prima di concludere.

</details>

## 3. Tre avvisi condividono un IP del campus. Basta per unirli in un unico attacco confermato?

<details>
<summary>Risposta</summary>

Un IP condiviso è una pista, soprattutto dietro la traduzione degli indirizzi di rete del campus, ma non identifica una sola persona o un solo attaccante. Confronta identificatori stabili di account e dispositivi, prove relative a messaggi o file, tipi di attività e orari UTC. Gli avvisi sono rilevamenti; un incidente raggruppa prove correlate e un'entità è un oggetto coinvolto. Proporrei la correlazione solo con relazioni a supporto, documentando l'incertezza. Servono una cronologia e una mappa delle entità che considerino anche studenti non collegati tra loro che condividono lo stesso indirizzo pubblico.

</details>

## 4. Un avviso su un endpoint riguarda il server che trasmette le lezioni. Lo studente analista può isolarlo subito?

<details>
<summary>Risposta</summary>

L'avviso da solo non concede l'autorità di contenimento. Conserva le prove, valuta attività in corso e probabile ambito e consulta il runbook dell'incidente e chi è autorizzato a decidere. L'isolamento potrebbe interrompere la didattica: documenta impatto sul servizio, confine proposto, alternative e condizioni di ripristino. Anche aspettare senza escalation è inadeguato se le prove suggeriscono una minaccia in corso. In questa simulazione, registra l'escalation e l'azione proposta senza eseguirla. Per completare il caso servirebbero una registrazione dell'azione approvata e prove separate che confermino il risultato desiderato.

</details>

## 5. La query sintetica della guida contiene tre righe Denied. Perché il conteggio previsto è due?

<details>
<summary>Risposta</summary>

Il dataset ripete la stessa coppia `EventId` e account per `e1`. Dopo il filtro temporale UTC, `distinct EventId, Account` conserva una copia di quella coppia più `e2`, quindi l'aggregazione prevede due eventi per `student-a`. La conclusione dipende dall'ipotesi dichiarata di un identificatore stabile. Eliminare duplicati solo per account unirebbe eventi distinti, sottostimando il conteggio. Anche l'evento Allowed si trova sul limite temporale superiore escluso. Si tratta di un risultato previsto leggendo righe sintetiche, non della prova di una query eseguita in un tenant.

</details>

## 6. Unire record di messaggi e accessi per account raddoppia il conteggio. Ci sono stati il doppio degli attacchi?

<details>
<summary>Risposta</summary>

Non necessariamente. Più messaggi e più accessi per uno stesso account possono produrre diverse coppie corrispondenti. Dichiara tipo di join, unicità delle chiavi e relazione che l'analisi cerca di stabilire. Anche il tipo predefinito `innerunique` modifica l'input sinistro deduplicando le chiavi di join, e può eliminare distinzioni necessarie all'analista. Esamina la cardinalità di ciascun input e aggiungi una relazione temporale appropriata prima di interpretare l'output. Conserverei gli ID degli eventi sorgente e confronterei gli abbinamenti previsti in un piccolo dataset sintetico, senza equiparare le righe unite agli attacchi.

</details>

## 7. Una ricerca non trova accessi a file privati dopo un'email sospetta. Il rapporto può dire che l'account non è mai stato compromesso?

<details>
<summary>Risposta</summary>

L'affermazione va oltre le prove. Riporta che la query definita non ha trovato record disponibili corrispondenti per la popolazione e l'intervallo UTC scelti. Controlla che l'audit applicativo fosse abilitato, i dispositivi rilevanti avessero completato l'onboarding, i record rientrino ancora nella conservazione e l'analista possa leggerli. Rivedi anche i filtri e il significato degli eventi di accesso. Una sostituzione autorizzata del dispositivo è una spiegazione alternativa per l'attività da un dispositivo non familiare. Conserva ipotesi, versione della query, lacune di copertura e una domanda successiva, senza trattare l'assenza di corrispondenze come prova di sicurezza.

</details>

## 8. Un'importazione in blocco di un corso genera avvisi ripetuti. Bisogna escludere tutti gli account dei docenti dalla regola?

<details>
<summary>Risposta</summary>

Un'esclusione ampia per ruolo potrebbe nascondere attività di docenti compromessi. Identifica prima account autorizzato specifico dell'importazione, carico di lavoro, andamento temporale e prove di audit. Confronta eventi sintetici di importazione etichettati con accessi preoccupanti a soluzioni non pubblicate. Proponi un'eccezione delimitata o una modifica della regola e valuta falsi positivi e falsi negativi. Esamina anche sovrapposizione della pianificazione, intervallo retrospettivo, raggruppamento e soppressione prima di attribuire il problema alla soglia. Conserva risultati previsti e versione della regola in una registrazione dell'ottimizzazione; il solo calo del volume di avvisi non dimostra un miglioramento della qualità del rilevamento.

</details>

## 9. Un nuovo tentativo del playbook aprirebbe un altro ticket e limiterebbe di nuovo lo stesso account. Che cosa manca?

<details>
<summary>Risposta</summary>

Il progetto richiede idempotenza e un modello chiaro dello stato delle azioni. Associa il flusso a identificatori stabili di incidente e azione, verifica se il passo previsto è già stato completato e gestisci errori parziali senza ripeterlo alla cieca. Verifica separatamente ruoli dell'operatore, permesso di Sentinel di richiamare il playbook e ambito delle operazioni successive dell'identità del flusso. Le restrizioni che interrompono servizi richiedono approvazione e percorso di ripristino previsti dal runbook. In questa revisione offline, simula su carta un'attivazione duplicata e un timeout; non distribuire né eseguire il playbook.

</details>

## 10. Copilot dice che un avviso su un carico cloud prova che student-a ha scaricato soluzioni. Il riepilogo basta come prova?

<details>
<summary>Risposta</summary>

No. Collega l'affermazione a record di accesso applicativo, ID della risorsa cloud, identificatori di identità e cronologia UTC. Un avviso sul carico di lavoro o una raccomandazione sulla postura non dimostra da solo uno specifico download di documenti. Esamina fonti citate da Copilot, integrazioni disponibili e schema, filtri, join e conteggi di ogni query generata. Segnala le affermazioni prive di supporto e conserva la conclusione corretta dall'analista. Il fascicolo deve distinguere prove sintetiche osservate, relazione dedotta e record mancanti. Un riepilogo scorrevole non può fornire telemetria indisponibile né autorizzare una risposta.

</details>

[Guida ufficiale allo studio](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · [Fonti tecniche e spiegazioni](SC-200.md)
