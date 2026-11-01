# SC-100 · Dieci casi di architettura

[Guida](SC-100.md) · [Quaderno di esercizi](SC-100-workbook.md) · [Indice](README.md) · [Español](../es/SC-100-cases.md)

Domande ipotetiche originali per l'app universitaria di appunti. Spiega requisito organizzativo, confine del controllo, responsabile e prove di accettazione prima di aprire una risposta. Sono esercizi di progettazione offline, non domande ufficiali d'esame o affermazioni di controlli eseguiti.

## 1. Un preside vuole il punteggio di sicurezza più alto prima di proteggere le soluzioni non pubblicate. Come si stabiliscono le priorità?

<details>
<summary>Risposta</summary>

Parti dall'impatto della divulgazione delle soluzioni e dai percorsi che potrebbero esporle. Identifica responsabile dei dati, accesso attuale, identità privilegiate, percorsi di condivisione e prove disponibili. Un punteggio può evidenziare lacune nella postura ma non assegnare le priorità organizzative dell'università. Proponi controlli che riducano l'esposizione critica, poi definisci l'accettazione tramite test di accesso con ambito definito e prove revisionabili della configurazione. Registra costi, rischi residui e decisione autorizzata del preside sul rischio. Migliorare prima una raccomandazione non pertinente e a basso impatto richiederebbe una motivazione difendibile, non solo un aumento più facile del punteggio.

</details>

## 2. L'API usa un endpoint privato. L'architettura può dichiarare completato Zero Trust?

<details>
<summary>Risposta</summary>

La connettività privata limita un percorso di rete; non stabilisce identità, autorizzazione applicativa o isolamento completo. Verifica se l'accesso pubblico resta abilitato, come campus e ambienti di recupero risolvono il DNS e quali chiamanti possono raggiungere l'endpoint. Definisci poi autenticazione degli utenti, permessi dei carichi di lavoro, requisiti dei dispositivi dove applicabili e decisioni di accesso per corso. Includi percorsi di amministrazione e uscita. L'accettazione deve includere richieste consentite e negate attese e le prove necessarie per distinguere un guasto di rete da un rifiuto per permessi. L'architettura deve registrare i confini rimanenti invece di chiamare una singola funzionalità una strategia completa.

</details>

## 3. Indicizzatore e agente IA condividono un account amministratore. Che cosa deve cambiare nel progetto?

<details>
<summary>Risposta</summary>

Assegna a ogni carico un'identità distinguibile, un responsabile, un ciclo di vita e un confine di permessi. L'indicizzatore richiede accesso ai documenti pubblicati consentiti; all'agente servono solo recupero e strumenti richiesti dal compito. Valuta identità gestite, federazione e controlli supportati per l'identità degli agenti rispetto a questi requisiti. Elimina la dipendenza da un amministratore umano e definisci come scade o si revoca l'accesso. L'autenticazione riuscita non deve implicare accesso ampio ai dati o diritti di distribuzione. Le prove di accettazione devono mostrare operazioni consentite, accesso tra corsi negato, attività attribuibile e recupero se una delle identità diventa indisponibile.

</details>

## 4. Sentinel riceve avvisi cloud ma nessun evento della directory del campus. L'architettura SOC è adeguata?

<details>
<summary>Risposta</summary>

L'adeguatezza dipende dalle minacce prioritarie e dalla copertura documentata. Se una directory del campus compromessa può influire sul servizio di appunti, la telemetria mancante della directory è una lacuna rilevante di rilevamento. Mappa quella minaccia su segnali attesi, dipendenze di acquisizione, conservazione, rilevamento, triage e autorità di contenimento. Spiega come contribuiscono Defender XDR e Sentinel senza presumere che uno dei due veda automaticamente ogni risorsa. Proponi una fase di integrazione o un monitoraggio compensativo con responsabile e scadenza. L'accettazione richiede eventi rappresentativi utilizzabili e una simulazione della risposta, non soltanto lo stato abilitato di un connettore o una dashboard popolata.

</details>

## 5. Un'etichetta di riservatezza e dischi crittografati vengono proposti come intera strategia per i dati degli studenti. Che cosa manca?

<details>
<summary>Risposta</summary>

Chiarisci posizioni dei dati, classificazione, destinatari e obblighi. Verifica che cosa configura davvero l'etichetta e quali client e repository ne rispettano le protezioni. La crittografia dei dischi protegge un confine di archiviazione ma non impedisce a un servizio autorizzato di leggere o esportare testo in chiaro. Considera accesso limitato, restrizioni di condivisione, copertura DLP, audit, conservazione, eliminazione e amministrazione delle chiavi. Assegna prove e responsabili a ogni requisito, compresi i percorsi non supportati. I referenti legali e della privacy devono valutare gli obblighi; né un'etichetta né un punteggio di conformità dimostrano che l'istituzione soddisfa ogni requisito legale.

</details>

## 6. Un documento caricato da un docente ordina all'assistente IA di inviare via email tutti i file del corso. Quale confine conta?

<details>
<summary>Risposta</summary>

Il documento è contenuto recuperato non attendibile e non può concedere autorità al modello o ai suoi strumenti. Mantieni il recupero limitato al materiale consentito all'utente, restringi l'identità dell'agente e applica l'autorizzazione degli strumenti al di fuori delle istruzioni generate dal modello. Uno strumento di invio richiede una politica esplicita per destinatari e accesso ai dati, più approvazione per divulgazioni con conseguenze dove prevista dal progetto. Valuta il rilevamento degli attacchi ai prompt come controllo aggiuntivo con ipotesi su integrazione e lingue supportate. Usa documenti sintetici nella simulazione a tavolino. L'accettazione deve dimostrare che un'istruzione dentro un documento non può ampliare recupero o permessi degli strumenti.

</details>

## 7. I backup notturni ripristinano singoli file, ma il servizio richiede un RPO di quindici minuti. Il progetto può superare la revisione?

<details>
<summary>Risposta</summary>

Non sulla base di queste prove. I soli punti di recupero notturni non soddisfano un requisito di perdita massima dei dati di quindici minuti. Identifica ogni fonte dati e il meccanismo di recupero proposto per ciascuna, compresa la coerenza tra documenti e metadati. Valuta anche amministrazione dei backup resistente al ransomware, conservazione e recupero delle chiavi. L'RTO applicativo di due ore richiede identità, DNS, configurazione e accesso al piano di controllo, non solo recupero dei file. Il responsabile deve finanziare e convalidare un progetto che soddisfi gli obiettivi oppure approvare requisiti rivisti con impatto esplicito. Registra le misure attese; questo esercizio offline non dimostra alcuna prestazione di ripristino.

</details>

## 8. Il gruppo della piattaforma cloud applica criteri ad Azure. Come va gestita un'eccezione SaaS dipartimentale?

<details>
<summary>Risposta</summary>

Stabilisci prima se l'ambito di quel criterio può governare il servizio SaaS; non dedurre copertura da un risultato di conformità Azure. Mappa il servizio dipartimentale sui requisiti di controllo dell'università e valuta controlli nativi, integrazione delle identità, trattamento dei dati, prove di audit e responsabilità contrattuali. Usa il modello di responsabilità delle landing zone per chiarire proprietà della piattaforma e dei carichi senza pretendere che ogni servizio rientri nello stesso meccanismo di applicazione. Se resta una lacuna, registra controlli compensativi, responsabile del rischio, data di revisione e scadenza. La decisione architetturale deve mostrare come l'eccezione influisce sul servizio complessivo.

</details>

## 9. Un artefatto di build firmato proviene da un runner con ampi permessi di produzione. La supply chain è protetta?

<details>
<summary>Risposta</summary>

La firma supporta integrità e provenienza dell'artefatto entro ipotesi di fiducia definite, ma da sola non può rendere attendibile una build autorizzata compromessa. Esamina approvazione del sorgente, controlli delle dipendenze, isolamento del runner, accesso alla chiave di firma, promozione degli artefatti e permessi di distribuzione. Separa fiducia di test e produzione e limita dichiarazioni della federazione e ambito delle risorse dove applicabile. Definisci chi indaga su un rilascio sospetto e come si ripristina una versione nota per il buon funzionamento. Le prove di accettazione devono collegare una revisione approvata del sorgente all'artefatto promosso e alla distribuzione autorizzata, mostrando che una pipeline non approvata non può modificare produzione o politica di firma.

</details>

## 10. Il finanziamento copre un solo semestre. Come può un architetto giustificare un programma di sicurezza per fasi?

<details>
<summary>Risposta</summary>

Ordina il lavoro per esposizione organizzativa critica, dipendenze, capacità concreta di realizzazione e riduzione del rischio attesa. Proteggere recupero e amministrazione privilegiata può abilitare successive migrazioni e miglioramenti della risposta, ma giustifica la sequenza rispetto alle minacce dell'università. Confronta opzioni realizzabili, licenze, oneri operativi e interruzioni della didattica. Per ogni fase assegna responsabile, criteri di accettazione con ambito definito, prove, condizioni di ripristino e revisione datata del rischio residuo. Documenta un'alternativa e il motivo del suo rifiuto in un ADR. Un acquisto finanziato è una tappa; efficacia convalidata dei controlli e accettazione autorizzata del rischio determinano la prontezza.

</details>

[Guida ufficiale SC-100](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100)
