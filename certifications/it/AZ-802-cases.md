# AZ-802 · 10 casi con risposte ragionate

[Guida](AZ-802.md) · [Quaderno in cinque unità](AZ-802-workbook.md) · [Indice](README.md)

Questi sono scenari originali di laboratorio universitario, non domande ufficiali d’esame. Prima di aprire una risposta, indica un’ipotesi, una spiegazione alternativa e le prove necessarie. I comandi citati sono verifiche proposte per un laboratorio Windows autorizzato; non si dichiara alcuna esecuzione o recupero in produzione. Ogni domanda comprende lo scenario completo, così che esercitatore ed esportazione Anki ne conservino il contesto.

## 1. Dopo una modifica alla rete dell’aula, un client di dominio risolve i siti pubblici ma non trova il controller di dominio. Il suo resolver è un servizio DNS pubblico; il server DNS AD configurato è raggiungibile e i suoi record SRV sono noti come integri. L’ora del client è corretta. Il primo intervento deve reimpostare le password di tutti gli studenti?

<details>
<summary>Ragionamento</summary>

No. Le prove fornite indicano innanzitutto il percorso di risoluzione dei nomi del client. Il successo del DNS pubblico non dimostra l’individuazione dei record di servizio AD privati. Registra il resolver del client, la query SRV pertinente e il risultato, poi confronta quel percorso con la configurazione DNS approvata del laboratorio. Una correzione adeguata ripristina il percorso previsto verso un resolver che conosca AD e convalida individuazione, raggiungibilità del controller e un accesso interessato prima di ampliare la modifica.

Le ipotesi di server integro e ora corretta restringono questa indagine specifica; non significano che ogni errore reale di accesso sia un problema DNS. Se l’individuazione riesce ma l’autenticazione fallisce ancora, prosegui con errore esatto, stato dell’account, protocollo e prove del canale sicuro. Conserva un confronto prima/dopo con timestamp e controller effettivamente selezionato. Reimpostare tutte le password cambierebbe uno stato estraneo al problema senza correggere il resolver individuato e potrebbe nascondere prove utili. Il rollback consiste nel ripristinare la configurazione client registrata se la modifica approvata compromette altre risoluzioni necessarie, anziché lasciare una combinazione di resolver pubblici e privati dal comportamento non compreso.

</details>

## 2. Una modifica all’appartenenza di un gruppo di ricerca è visibile su LAB-DC1 ma non sul controller dell’edificio remoto. I client di quell’edificio usano il secondo controller, la replica segnala errori DNS e una nuova condivisione resta inaccessibile. Aggiungere l’utente a un altro gruppo privilegiato è una soluzione adeguata?

<details>
<summary>Ragionamento</summary>

No. Le versioni della directory osservate e l’errore di replica forniscono una spiegazione concreta da indagare prima di ampliare i privilegi. Registra ora della modifica, controller che l’ha accettata, controller selezionato dal client ed errori di replica. Controlla record DNS dei partner di replica, resolver configurati, connettività e prerequisiti di autenticazione. Verifica che la subnet remota corrisponda al sito previsto, ma non presumere che cambiare la pianificazione di un sito ripari un errore DNS.

Dopo un intervento supportato, conferma che la modifica specifica all’appartenenza abbia raggiunto il controller pertinente. Ottieni poi un nuovo token appropriato di accesso o sessione dell’utente e prova la condivisione prevista con quell’identità: convergenza della directory e contesto di autorizzazione aggiornato sono controlli distinti. Se l’accesso fallisce ancora, esamina anche autorizzazioni di condivisione e file system. Mantieni il gruppo ristretto e registra un test consentito e uno negato. Aggiungere un gruppo privilegiato estraneo potrebbe mascherare il sintomo lasciando guasta la replica e ampliando l’accesso dello studente. La consegna è una sequenza temporale della convergenza della modifica e dell’accesso, con le osservazioni previste indicate come tali finché un test reale nel laboratorio non le fornisce.

</details>

## 3. Un’aula di una sede isolata userà un RODC. Una proposta consente di memorizzarvi nella cache le password degli amministratori privilegiati dell’università, così che possano accedere durante le interruzioni WAN. La stanza ha una protezione fisica inferiore al data center principale. Che cosa deve richiedere la revisione del progetto?

<details>
<summary>Ragionamento</summary>

Rifiuta l’idea che un RODC renda sicura qualsiasi credenziale nella cache. Esamina il criterio di replica delle password, le appartenenze effettive consentite e negate, l’amministrazione delegata e la procedura per la perdita fisica del dispositivo. Gli account privilegiati devono restare fuori dalla cache della sede. Quando un account è sia consentito sia negato dal criterio effettivo, prevale il divieto. Identifica gli account ordinari limitati che necessitano davvero dell’accesso senza connessione e verifica il criterio effettivo risultante, anziché basarti soltanto sul nome di un gruppo.

Il piano deve distinguere l’autenticazione degli utenti con credenziali nella cache dalle operazioni che richiedono un controller scrivibile, compreso uno stato nuovo o modificato della directory. Definisci quali servizi restano utilizzabili durante l’interruzione WAN e come gli operatori ottengano un percorso amministrativo approvato senza indebolire il perimetro del dominio. Le prove comprendono ipotesi sulle minacce della sede, account scelti, decisioni effettive di memorizzazione nella cache, connettività dei controller e risposta alla perdita del dispositivo. Non pubblicare password o contenuti della cache come prove. Un piano di recupero deve considerare le credenziali nella cache coinvolte e il server compromesso, non soltanto sostituire l’hardware presumendo che tutti i segreti della directory siano rimasti protetti.

</details>

## 4. Un server collegato ad Azure Arc continua a fallire un’attività remota dal server B al file server C. Qualcuno propone un’ampia delega delle credenziali e un account virtuale JEA predefinito su un controller di dominio. L’attività richiede soltanto una specifica operazione su un servizio. Il collegamento Arc giustifica questo progetto?

<details>
<summary>Ragionamento</summary>

No. Il collegamento Arc crea una relazione di gestione Azure; non aggiunge il server ad AD, non crea un trust di foresta e non delega automaticamente a C le credenziali dell’operatore interattivo. Disegna primo e secondo hop, protocollo di ciascuno, identità effettiva e operazione esatta richiesta. Diagnostica il perimetro di autorizzazione o autenticazione che fallisce. Una prima sessione riuscita non dimostra che la seconda risorsa accetti l’identità prevista.

Esamina le opzioni supportate del secondo hop e i relativi limiti prima di sceglierne una. CredSSP introduce esposizione delle credenziali; i metodi di delega vincolata non risolvono genericamente un secondo hop da WinRM a WinRM. Per JEA esamina insieme identità di esecuzione della sessione, utenti consentiti, comandi, parametri e traccia di audit. Un account virtuale predefinito su un DC può avere privilegi Domain Admin, sproporzionati per una specifica operazione di servizio. Preferisci una sede di gestione adeguata e diritti di esecuzione esplicitamente limitati. La prova è un diagramma di permessi e hop con operazioni consentite e negate, non un comando riuscito grazie a credenziali amministrative riutilizzabili. Anche i permessi sulle estensioni di un controller gestito con Arc richiedono una revisione distinta.

</details>

## 5. Una VM di laboratorio usa checkpoint Production, ma l’elaborazione della coerenza guest fallisce e l’host crea un checkpoint Standard. Uno studente lo definisce un backup indipendente coerente a livello applicativo. Checkpoint e dischi VM condividono la stessa archiviazione. Che cosa va corretto?

<details>
<summary>Ragionamento</summary>

Correggi sia l’affermazione sulla coerenza sia il perimetro della protezione. La modalità Production può consentire il ripiego su un checkpoint Standard: l’impostazione richiesta è quindi una prova più debole del tipo di checkpoint effettivo e del risultato dell’elaborazione guest. Se l’esercizio richiede un checkpoint di produzione e rifiuta il ripiego, valuta ProductionOnly e correggi i prerequisiti di integrazione guest/VSS o di blocco del file system pertinente. Il rifiuto di creare il checkpoint richiesto è un’indicazione utile di errore; accettarne silenziosamente uno di altro tipo non è equivalente.

Anche un checkpoint di produzione riuscito non dimostra l’esistenza di un backup indipendente conservato. La sua catena di dischi può andare persa con l’archiviazione della VM e il recupero dell’applicazione richiede comunque un metodo supportato di coerenza e ripristino. Dove il requisito lo impone, conserva un backup protetto con durata adeguata e un piano di convalida del ripristino. Esamina metadati dei checkpoint e margine di archiviazione con strumenti supportati; non eliminare file AVHDX manualmente. Spiega separatamente se l’obiettivo sia annullare una modifica in un laboratorio eliminabile, sopravvivere alla perdita di host o archiviazione oppure recuperare uno stato applicativo precedente valido. Ogni obiettivo richiede prove diverse e può richiedere un meccanismo diverso.

</details>

## 6. I PC esistenti dell’aula continuano a funzionare, ma i nuovi client non ottengono indirizzi. Il server DHCP autorizzato è raggiungibile tramite un relay funzionante; nell’ambito interessato non ci sono lease liberi. È stato installato un secondo server, ma non esiste una relazione di failover. Quale conclusione deve trarre l’indagine?

<details>
<summary>Ragionamento</summary>

Le prove indicano l’esaurimento dell’ambito come problema immediato delle nuove assegnazioni. I client esistenti possono continuare secondo lo stato del proprio lease, quindi il loro funzionamento non dimostra che il server possa assegnare un altro indirizzo. Esamina intervalli, esclusioni, prenotazioni, lease attivi e subnet effettiva dei client prima di proporre una correzione approvata della capacità. Cerca schemi di assegnazione obsoleti o inattesi, ma non eliminare lease indiscriminatamente e non estendere l’ambito in un intervallo sovrapposto.

Un secondo server installato non coordina automaticamente i lease. Se serve disponibilità, progetta una relazione di failover DHCP supportata per gli ambiti previsti, comprendendone modalità, stato del partner, comportamento dei lease e responsabilità del recupero. Non attivare copie concorrenti non gestite dello stesso intervallo. Le prove comprendono inventario degli ambiti, numero di indirizzi disponibili, percorso del relay e un test con un client realmente nuovo oltre a uno esistente. Capacità e failover risolvono condizioni di guasto diverse: una relazione integra non autorizza a ignorare un pool sottodimensionato. Registra l’ambito precedente e fermati se l’intervallo proposto entra in conflitto con il routing o un’altra autorità di assegnazione.

</details>

## 7. Uno studente ha l’autorizzazione SMB prevista sulla condivisione, ma NTFS nega l’accesso a una cartella di progetto. Azure File Sync è integro e il suo endpoint server ha file suddivisi in livelli. Concedere Azure Contributor e definire la copia sincronizzata un backup risolverebbe entrambi i problemi?

<details>
<summary>Ragionamento</summary>

No. Segui il percorso effettivo del file Windows e l’identità usata. Il rifiuto NTFS individuato rimane rilevante anche con accesso a livello di condivisione presente. Correggi l’autorizzazione prevista della cartella con appartenenze ai gruppi e isolamento adeguati, poi prova lo studente interessato e uno che deve restare escluso. Un ruolo di gestione delle risorse Azure non ripara automaticamente l’ACL del file system e non conferisce accesso ai dati SMB. Esamina l’accesso effettivo anziché dedurlo da una sola voce configurata.

Tratta separatamente la questione del recupero. Una sincronizzazione integra può propagare un’eliminazione e i file del server suddivisi in livelli potrebbero non contenere una copia locale completa e indipendente. Identifica endpoint cloud, backup conservati utilizzabili, dipendenze del ripristino e flusso di recupero supportato. Riportare indietro o clonare un server File Sync registrato da un’immagine del sistema operativo o un checkpoint VM non è un metodo generico di recupero supportato. Le prove devono includere decisione su condivisione/NTFS, stato di endpoint e livelli e piano dei punti storici di ripristino. Accesso ripristinato oggi e dati recuperabili dopo un errore futuro sono due esiti diversi; nessuno va dichiarato senza il test corrispondente o prove progettuali esplicitamente indicate come tali.

</details>

## 8. Un insieme di server comprende Windows Server 2022 e 2025. Una proposta di rafforzamento applica ovunque una baseline OSConfig Windows Server 2025 e promette che rimuovere la gestione ripristini ogni vecchia impostazione. Inoltre conserva una password LAPS recuperata in una relazione condivisa. Che cosa deve cambiare?

<details>
<summary>Ragionamento</summary>

Separa supporto della configurazione, recupero dalle modifiche e gestione dei segreti. Le indicazioni OSConfig esaminate riguardano Windows Server 2025, quindi non presentare la stessa configurazione come supportata sui computer 2022. Registra versioni di sistema operativo e moduli, impostazioni specifiche dei ruoli e gruppo pilota. Individua GPO o altri sistemi di gestione esistenti che possano entrare in conflitto, esamina le impostazioni effettive e pianifica riavvio richiesto e convalida dell’accesso. Rimuovere la baseline non garantisce la ricostruzione di ogni valore precedente alla gestione; conserva uno stato precedente verificato e una procedura di recupero.

LAPS supporta rotazione controllata delle password, backup e recupero autorizzato. Copiare una password recuperata in una relazione leggibile da molti vanifica quel perimetro di accesso. Rimuovila mediante il processo appropriato per incidenti o modifiche, tratta l’esposizione secondo i criteri e ruotala dove richiesto; pubblica soltanto prove depurate di criteri e autorizzazione. Le credenziali di recupero richiedono accesso protetto che resti utilizzabile durante il guasto previsto. Le prove devono mostrare distribuzione supportata, ruoli di recupero consentiti e negati, accesso sottoposto ad audit e piano di ripristino, anziché una credenziale in chiaro o uno screenshot di conformità dato per prova di ogni protezione.

</details>

## 9. Un server Arc risulta connesso e l’area di lavoro contiene righe Heartbeat recenti dell’agente, ma gli eventi Windows System richiesti sono assenti. Quegli eventi esistono localmente. La query vuota dimostra che Windows non abbia generato errori?

<details>
<summary>Ragionamento</summary>

No. Lo scenario afferma già che gli eventi pertinenti esistono localmente. Connettività Arc e Heartbeat dell’agente sono osservazioni diverse dalla consegna riuscita dell’origine eventi scelta. Conferma computer, intervallo temporale, area di lavoro e tabella di destinazione previsti, poi esamina stato dell’estensione o servizio AMA, DCR associata, selezione degli eventi e destinazione e configurazione effettivamente ricevuta dall’agente. La sola creazione di una DCR, senza associarla al computer pertinente, non avvia la raccolta.

Usa un identificatore e un timestamp di evento locale depurati per seguire un evento lungo la pipeline proposta. Distingui assenza all’origine, errore di raccolta, problemi di trasporto o configurazione e query indirizzata alla destinazione sbagliata. Tieni separata l’ora dell’evento dall’ora di arrivo nella raccolta e considera il ritardo di acquisizione documentato senza giudicare accettabile qualsiasi ritardo. Le prove comprendono record locale, identità del computer, associazione e contesto della query, seguiti da un test di arrivo atteso. Evita di reinstallare subito tutti gli agenti: cambia lo stato e può cancellare contesto diagnostico utile senza correggere selezione o associazione mancanti.

</details>

## 10. Uno studente elimina un oggetto AD importante e scopre che il Cestino non era abilitato prima dell’eliminazione. Propone di riportare un controller di dominio di produzione a un normale checkpoint VM e acquisire forzatamente tutti i ruoli FSMO. L’organizzazione ha un backup della directory supportato e un responsabile del recupero assegnato. Qual è il processo decisionale più sicuro?

<details>
<summary>Ragionamento</summary>

Coinvolgi i responsabili seguendo la procedura documentata di recupero della directory e conserva le prove di eliminazione, replica e backup. Abilitare il Cestino dopo l’evento non crea magicamente lo stato recuperabile precedente mancante. Determina oggetto e dipendenze coinvolti, backup supportato disponibile e ambito del ripristino prima di scegliere il metodo. Un errore su un singolo oggetto non giustifica di per sé il recupero dell’intera foresta o l’acquisizione di ruoli FSMO estranei.

Il responsabile deve scegliere i passaggi supportati di ripristino autorevole o non autorevole adatti al guasto reale, compresi contesto DSRM dove necessario, credenziali di recupero protette e aspetti SYSVOL. Un rollback generico di checkpoint VM non sostituisce quel piano. Documenta stato di riferimento, implicazioni della replica, convalida e condizioni per il ritorno di un precedente titolare del ruolo, se l’acquisizione forzata è davvero necessaria. Convalida oggetti della directory, autenticazione, replica e servizio coinvolto anziché fermarti a «la VM si avvia». In questo repository la consegna è una simulazione con punti decisionali espliciti; non sono stati eseguiti ripristini della directory, acquisizioni di ruoli o recuperi misurati.

</details>

Usa i riferimenti tecnici e le precisazioni sulle versioni nella [guida](AZ-802.md). Sviluppa prove e decisioni di modifica controllata nel [quaderno](AZ-802-workbook.md).
