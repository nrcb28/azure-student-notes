# DP-700 · Quaderno offline di ingegneria dei dati

[Guida](DP-700.md) · [Dieci casi](DP-700-cases.md) · [Indice](README.md) · [Español](../es/DP-700-workbook.md)

Cinque unità usano dati universitari sintetici. Non richiedono account, capacità a pagamento o esecuzione Fabric. Mantieni le stesse consegne nelle edizioni linguistiche. Etichetta gli output ragionati **EXPECTED**, le osservazioni locali **OBSERVED** e i controlli della piattaforma non eseguiti **NOT EXECUTED**. Ambito delle fonti e limiti della verifica dei riferimenti sono nella [guida](DP-700.md).

<a id="dp-700-unit-1"></a>

## 1. Disegnare la mappa della piattaforma e delle responsabilità

Spiega le differenze tra tenant, capacità, workspace, elemento, posizione OneLake e motore di esecuzione. Disegna fonte universitaria delle iscrizioni, file grezzi dei download, tabelle curate, shortcut del catalogo della biblioteca e consumatore analitico. Decidi dove potrebbero essere adatti lakehouse e warehouse, con un motivo concreto per ogni scelta. Dichiara la granularità di ogni tabella.

**Scenario:** la biblioteca controlla la destinazione dello shortcut e ne cambia la politica di accesso. **Prove:** registra proprietà della destinazione, ipotesi di autenticazione interna o esterna, permessi richiesti, contratto di schema ed effetto dell'eliminazione della destinazione. **Consegna:** un diagramma delle dipendenze e una matrice di accesso. Includi un requisito separato di conservazione storica; lo shortcut da solo non soddisfa esigenze di backup o recupero.

<a id="dp-700-unit-2"></a>

## 2. Riconciliare un registro di modifiche incrementali

Usa questo registro sintetico completo; `version` è l'ordinamento autorevole della fonte e `key` identifica un'iscrizione. Parti da una destinazione vuota. Conserva una tombstone con versione per le eliminazioni. Riduci ogni chiave alla versione massima, comprimi i duplicati identici, poi esegui il merge solo delle versioni più recenti. Payload in conflitto alla stessa versione richiedono quarantena.

| key | version | operation | module |
|---|---:|---|---|
| E1 | 1 | upsert | CS101 |
| E2 | 1 | upsert | DB201 |
| E1 | 2 | upsert | AI301 |
| E1 | 2 | upsert | AI301 |
| E2 | 2 | delete | DB201 |
| E2 | 1 | upsert | DB201 |

**Scenario:** ripeti il registro dopo aver perso la risposta di successo. **Prove attese:** E1 resta attiva in AI301 alla versione 2; E2 è eliminata alla versione 2. Il conteggio attivo è 1 dopo entrambe le esecuzioni. **Consegna:** stato intermedio e regole di conferma del progresso; spiega perché la versione 1 tardiva di E2 non può ripristinarla.

<a id="dp-700-unit-3"></a>

## 3. Specificare regole di qualità e tempo degli eventi

Progetta un record di download con identificatore dell'evento, insegnamento, tempo dell'evento, tempo di arrivo e versione dello schema. Definisci regole per null, tipi, valori ammessi e duplicati. Spiega la differenza tra approvare un nuovo campo facoltativo e accettare record non validi. La quarantena deve conservare un identificatore utilizzabile per la correzione e un motivo, limitando l'accesso ai contenuti sensibili.

**Scenario:** un evento avviene alle 23:59 UTC e arriva alle 00:07 UTC del giorno successivo; il ritardo ammesso dichiarato è di dieci minuti. **Prove attese:** il suo giorno basato sul tempo dell'evento è quello precedente. Per stabilirne l'accettazione occorre anche conoscere il watermark del motore al momento dell'arrivo; un ritardo di otto minuti misurato dall'orologio non basta a dimostrare l'accettazione. **Consegna:** regole di accettazione e correzione, riconciliazione, confini delle finestre, scopo del checkpoint e comportamento oltre la tolleranza.

<a id="dp-700-unit-4"></a>

## 4. Progettare una distribuzione controllata

Descrivi una pipeline che copia un intervallo delimitato di iscrizioni, richiama convalida e trasformazione e pubblica solo risultati accettati. Scegli SQL, PySpark o KQL per ogni trasformazione pertinente e motiva il motore. Distingui versionamento Git delle definizioni supportate, distribuzione dei contenuti supportati e spostamento dei dati.

**Scenario:** il notebook di test punta ancora al lakehouse di produzione. **Prove:** esamina riferimenti agli elementi, associazione della connessione, identità di runtime, parametri, dipendenze dell'ambiente e pianificazioni prima dell'esecuzione. **Consegna:** una tabella di configurazione sviluppo/test/produzione, prove di lettori autorizzati e negati attraverso report e file e passi di ripristino. Spiega perché un'etichetta di riservatezza da sola non implementa il progetto completo dei permessi.

<a id="dp-700-unit-5"></a>

## 5. Diagnosticare un'esecuzione lenta immaginaria

Crea una base di confronto per durata dell'esecuzione, conteggi di input e output, rifiuti, aggiornamento e utilizzo della capacità. Aggiungi un incidente in cui lo stesso volume di input richiede il doppio del tempo. Includi tre spiegazioni concorrenti: un join Spark squilibrato, molti file piccoli e domanda concorrente sulla capacità. Indica quali prove confermerebbero o escluderebbero ogni spiegazione; esamina esclusione delle partizioni e comportamento delle query dove pertinente.

**Scenario:** un nuovo tentativo segue una scrittura parziale. **Prove:** usa le regole delle versioni dell'unità 2 per mostrare se lo stato operativo cambia. **Consegna:** un esperimento reversibile di ottimizzazione con soglie di accettazione e riconciliazione della correttezza. Segna tutti i tempi Fabric come NOT EXECUTED; il ragionamento sintetico non può dimostrare velocità di elaborazione reale, durata del recupero o distribuzione cloud riuscita.
