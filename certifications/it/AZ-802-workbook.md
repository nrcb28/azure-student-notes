# AZ-802 · Quaderno Windows Server basato sulle prove

[Guida](AZ-802.md) · [10 casi ragionati](AZ-802-cases.md) · [Indice](README.md)

Cinque unità corrispondenti combinano le sette aree di studio AZ-802. Usa il laboratorio universitario fittizio e isolato `lab.example.test`. Produci una decisione e un insieme di prove verificabili, non un elenco di impostazioni copiate da un video. Sono esercizi Windows proposti; non si dichiara l’esecuzione di operazioni AD, Hyper-V, Azure, ripristini o controlli di sicurezza. Senza un laboratorio Windows compatibile, consegna un progetto e osservazioni previste indicati come tali, anziché inventare risultati.

Tieni un registro per ogni unità: baseline, ipotesi, spiegazione alternativa, verifica in sola lettura scelta, modifica proposta, osservazione attesa, osservazione effettiva se eseguita e condizione di arresto o rollback. Registra edizione e versione del sistema operativo, moduli installati, diritti necessari e identità di destinazione. Oscura segreti e dati personali. La matrice dei prerequisiti della guida vale per i relativi esempi di comando; nessun comando conferisce l’autorità di esaminare un sistema estraneo all’attività.

<a id="az-802-unit-1"></a>

## 1. Seguire una modifica dell’identità dalla directory all’accesso

**Scenario:** LAB-DC1 accetta una modifica all’appartenenza di un gruppo di ricerca, ma un client dell’edificio remoto continua a non accedere a `\\LAB-FS1\LabNotes`. Il client seleziona LAB-DC2. Una proposta distinta per una sede usa un RODC perché la stanza ha una protezione fisica limitata.

**Indagine:** disegna foresta e dominio, due controller scrivibili, RODC della sede, resolver DNS, siti e mapping delle subnet IP. Segna il controller che ha accettato la modifica e quello usato dal client. Identifica percorso di replica, record SRV pertinenti, gerarchia dell’ora, token utente e perimetro di condivisione/NTFS. Scegli una sequenza ordinata di controlli che distingua uno stato obsoleto della directory da un problema di accesso effettivo. Includi un’osservazione attesa che smentirebbe la tua prima ipotesi.

Usa le query della guida per inventario AD, resolver, ora e replica soltanto da un contesto di amministrazione Windows adeguato. Per Criteri di gruppo spiega separatamente ambito, elaborazione del client e impostazioni effettive. Per l’RODC definisci account ordinari ammessi all’accesso senza connessione, account che devono restare esclusi, amministrazione delegata della sede e risposta alla perdita del dispositivo. Verifica il criterio effettivo di replica delle password anziché presumere che il nome di un gruppo lo dimostri.

**Prove:** topologia con perimetri delle identità; contesti delle query e timestamp depurati; sequenza temporale di modifica di un oggetto; selezione prevista e osservata dei controller; una coppia di test di accesso ai file consentito e negato; una decisione sulla cache RODC senza password.

**Consegna e condizioni decisionali:** scrivi una diagnosi di una pagina con una correzione proposta circoscritta. Conserva le impostazioni originali di resolver, siti e criteri prima di qualsiasi modifica autorizzata nel laboratorio. Fermati se il controller o lo spazio dei nomi interessato è fuori dal laboratorio eliminabile. Non ampliare i privilegi, acquisire ruoli FSMO o reimpostare tutti gli account per far sparire il sintomo. Il successo richiede la convergenza della modifica necessaria e che l’utente previsto ottenga soltanto l’accesso previsto, mentre l’utente escluso rimane escluso.

<a id="az-802-unit-2"></a>

## 2. Esaminare i perimetri dell’amministrazione remota e del recupero VM

**Scenario:** un operatore raggiunge da remoto un server membro ma non accede a una seconda risorsa. Una proposta abilita la delega di credenziali riutilizzabili ed esegue un endpoint JEA su un DC. Intanto il passaggio di coerenza di produzione di una VM fallisce, ma viene creato un checkpoint Standard. Il laboratorio ha due host da 64 GiB, una riserva simulata di 12 GiB per host e dodici guest da 4 GiB fissi assegnati a ogni host.

**Indagine:** disegna ogni hop di autenticazione, protocollo, identità effettiva e operazione richiesta. Confronta un progetto supportato del secondo hop con rischi di CredSSP e limiti della delega specifici dei protocolli. Esamina comandi e parametri JEA consentiti, gruppi di esecuzione, audit e collocazione; spiega perché i privilegi predefiniti dell’account virtuale su un DC siano eccessivi per una specifica attività di servizio su un server membro. Per un computer gestito con Arc identifica separatamente autorità sulle estensioni Azure e autorizzazioni locali.

Usa l’inventario di VM, switch, memoria e checkpoint per spiegare rete guest e stato di recupero. Confronta checkpoint, Replica, clustering e backup protetti in base al guasto che ciascuno affronta. Spiega Production rispetto a ProductionOnly e perché conti il tipo effettivo del checkpoint. Per il dimensionamento simulato, la memoria normalmente assegnata è 48 + 12 = 60 GiB per host; trasferire tutti i 24 guest su un host richiederebbe 96 + 12 = 108 GiB. Dichiara le ipotesi e mostra perché rientrare nella capacità normale non dimostri la capacità in caso di guasto di un host.

**Prove:** diagramma di autorizzazioni e hop; revisione dell’endpoint limitato; percorso switch/guest; foglio di calcolo della memoria; metadati effettivi dei checkpoint se disponibili; piano di una copia di ripristino indipendente.

**Consegna e condizioni decisionali:** proponi un progetto amministrativo supportato e dall’ambito ristretto, con meccanismi di recupero separati. Fermati se la delega esporrebbe un’identità privilegiata reale o se i requisiti supportati di coerenza di una VM sono sconosciuti. Registra le impostazioni precedenti dell’endpoint e l’accesso di recupero. Non eliminare file AVHDX, non affermare che Replica corregga corruzioni logiche e non chiamare backup indipendente un checkpoint sulla stessa archiviazione. Un comando riuscito e un servizio recuperabile in sicurezza richiedono convalide diverse.

<a id="az-802-unit-3"></a>

## 3. Diagnosticare il percorso dal client ai file attraverso rete e archiviazione

**Scenario:** i nuovi client dell’aula non ottengono un indirizzo mentre i vecchi lease continuano. Dopo una correzione di rete approvata, un utente della ricerca raggiunge una condivisione ma riceve un rifiuto sulla cartella. Il server è registrato con Azure File Sync e alcuni file sono suddivisi in livelli. Un diagramma include anche un server d’inoltro DNS condizionale ibrido e un secondo server DHCP non configurato.

**Indagine:** segui VLAN e relay del client, ambito DHCP autorizzato, esclusioni e prenotazioni, opzioni e capacità libera. Definisci che cosa aggiunga una vera prova di nuova assegnazione rispetto a un test con un client esistente. Distingui un secondo server da una relazione di failover supportata configurata. Segui resolver previsto, spazio dei nomi, destinazione dell’inoltro condizionale, percorso di ritorno e porta applicativa; una risposta DNS corretta non dimostra una connessione SMB utilizzabile.

Registra poi utente effettivo, autorizzazione della condivisione, ereditarietà NTFS e contesto del token di gruppo. Prova un’identità consentita e una che deve restare esclusa. Per Azure Files separa configurazione supportata delle identità, autorizzazione a livello di condivisione e permessi di directory e file. Inventaria endpoint File Sync, ipotesi sulla cache locale, backup conservati indipendenti e procedura di recupero supportata. Rifiuta esplicitamente il ripristino, la clonazione o il rollback del sistema operativo o della VM di un server registrato come metodo generico di recupero File Sync.

**Prove:** foglio delle assegnazioni di indirizzi; diagrammi di resolver e route; osservazioni su condivisione e ACL senza segreti; criteri dei test consentiti e negati; mappa degli endpoint cloud e server; punto storico di recupero scelto con le sue dipendenze.

**Consegna e condizioni decisionali:** spiega guasto di rete e guasto di autorizzazione come risultati distinti. Acquisisci ambito e ACL esistenti prima di qualsiasi modifica autorizzata. Fermati davanti a intervalli di assegnazione sovrapposti, estensione involontaria dei permessi o dipendenze di recupero non protette. Il successo richiede che il nuovo client previsto ottenga impostazioni valide, che l’utente previsto acceda alla cartella, che quello escluso resti bloccato e che il piano di recupero identifichi una copia protetta anziché soltanto un altro endpoint sincronizzato.

<a id="az-802-unit-4"></a>

## 4. Progettare la sicurezza in base al ruolo senza perdere l’accesso di recupero

**Scenario:** l’insieme dei server comprende Windows Server 2022 e 2025, server membri, un DC e un file server. Una proposta distribuisce la stessa baseline OSConfig ovunque, espone SMB over QUIC senza verificare i certificati e condivide una password LAPS in una relazione. Rimuovere la baseline viene descritto come un rollback completo.

**Indagine:** costruisci una matrice di ruoli e versioni prima di scegliere i controlli. Le indicazioni esaminate per le baseline di sicurezza OSConfig riguardano Windows Server 2025; registra versione del modulo, scenario, differenze attese delle impostazioni, necessità di riavvio e conflitti con GPO o altri sistemi di gestione esistenti. Sperimenta sul ruolo corretto. Spiega perché non si possa presumere che rimuovere la gestione ricostruisca lo stato precedente. Conserva uno stato precedente protetto e un percorso amministrativo autorizzato alternativo.

Per LAPS separa rotazione, destinazione del backup, recupero consentito, audit e accesso di emergenza. Documenta le condizioni del recupero DSRM dove pertinenti, senza recuperare o pubblicare password. Per SMB over QUIC controlla l’esatto supporto di server e client: le indicazioni esaminate elencano Windows Server 2022 Datacenter: Azure Edition o edizioni Windows Server 2025, con client Windows 11. Esamina attendibilità e nomi del certificato, uso della chiave privata e percorso UDP consentito, poi preserva l’autorizzazione di condivisione e file. Non trattare QUIC come un sostituto dell’autorizzazione.

**Prove:** matrice di ruoli e versioni; controlli scelti con riferimenti al supporto; differenze delle impostazioni e condizione di rollback; ruoli di recupero consentiti e negati; elenco di verifica dei certificati depurato; piano isolato di test di accesso consentito e negato.

**Consegna e condizioni decisionali:** scrivi una proposta di modifica graduale con responsabili del recupero identificati. Fermati se la baseline non è supportata, se verrebbe eliminato l’unico percorso di gestione, se un requisito del certificato rimane irrisolto o se appare un segreto reale nelle prove. Tratta eventuali divulgazioni di credenziali esistenti attraverso il processo di risposta dell’organizzazione. Un risultato di conformità, una funzione installata e l’applicazione dimostrata del controllo sono osservazioni distinte.

<a id="az-802-unit-5"></a>

## 5. Seguire un evento mancante e simulare il recupero della directory

**Scenario:** un server gestito con Arc risulta connesso, AMA invia Heartbeat, ma un evento System necessario esiste soltanto localmente. In una simulazione distinta viene eliminato un oggetto AD e il Cestino non era stato abilitato prima. Esiste un backup della directory supportato. Il team ha un obiettivo di ripristino di due ore e desidera prove più forti di «la VM si avvia».

**Indagine:** segui un evento locale depurato attraverso estensione o servizio AMA previsti, DCR, associazione, selezione dell’origine, destinazione e intervallo temporale della query. Registra separatamente identità del computer, ora dell’evento e ora di arrivo. Definisci un test che distingua eventi mancanti all’origine, configurazione di raccolta mancante e query sulla tabella o area di lavoro sbagliata. Spiega che cosa dimostrino rispettivamente connessione Arc e Heartbeat e che cosa lascino incerto.

Per il recupero della directory identifica oggetti e dipendenze coinvolti, backup supportato disponibile, responsabile del recupero, credenziali DSRM protette e ambito di ripristino appropriato. Distingui recupero di oggetti dal Cestino, ripristino autorevole o non autorevole della directory, recupero SYSVOL e recupero dell’intera foresta. Scegli una procedura supportata per il guasto effettivo; non trasformare un errore su un singolo oggetto in un rollback automatico del controller o in un’acquisizione FSMO. Simula ordine delle dipendenze, implicazioni della replica, convalida e ritorno sicuro dei servizi recuperati.

**Prove:** tracciamento dall’origine dell’evento alla destinazione; registro delle ipotesi con timestamp; inventario dei punti di recupero; tempi di ripristino previsti chiaramente indicati come stime; controlli di accettazione su oggetto richiesto, autenticazione, replica, criteri e applicazione coinvolta.

**Consegna e condizioni decisionali:** produci runbook distinti per monitoraggio e recupero. Conserva le prove originali di DCR e associazioni prima delle modifiche. Fermati se l’ambito del recupero o la copia di riferimento non sono chiari. Mantieni una sequenza temporale dell’interruzione aziendale e dei dati recuperati utilizzabili per non confondere RTO e RPO. Registra un’operazione come completata soltanto dopo che un laboratorio autorizzato l’ha eseguita e ha fornito le osservazioni indicate. Il repository non dichiara alcun ripristino Windows o AD né un risultato di due ore misurato.

Termina rispondendo ai [dieci casi](AZ-802-cases.md) senza aprirne le spiegazioni. Per ogni risposta debole identifica la prova mancante o il perimetro confuso e torna a quella parte della [guida](AZ-802.md). Questo quaderno offre esercizi selezionati, non una copertura esaustiva degli obiettivi o una previsione del superamento.
