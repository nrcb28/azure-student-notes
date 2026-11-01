# SC-100 · Quaderno di architettura della sicurezza

[Guida](SC-100.md) · [Dieci casi](SC-100-cases.md) · [Indice](README.md) · [Español](../es/SC-100-workbook.md)

Cinque unità offline originali per il servizio universitario immaginario di appunti. Usa risorse, identità, incidenti e prove inventati. Produci proposte architetturali ed esiti di simulazioni a tavolino; non modificare tenant, eseguire attacchi, distribuire risorse o collegare telemetria reale. Non si dichiarano esecuzione cloud o efficacia dei controlli.

<a id="sc-100-unit-1"></a>

## 1. Stabilire criticità e copertura dei controlli

**Scenario:** l'università aggiunge soluzioni non pubblicate delle prove a un'app che prima conteneva appunti pubblici. Identifica operazioni critiche, responsabili dei dati, minacce probabili e impatti organizzativi. Distingui mappatura delle capacità MCRA, requisiti di controllo MCSB, responsabilità della piattaforma CAF e revisione dei carichi Well-Architected. Esplicita le ipotesi invece di inventare un inventario completo.

**Prove:** un diagramma ipotetico delle risorse, tre rischi prioritari, confini attuali dei controlli e informazioni mancanti. Includi un requisito che non può essere valutato con il solo risultato di Azure Policy.

**Consegna:** una tabella di copertura con requisito, controllo, ambito, responsabile, prova, lacuna e criterio di accettazione. Aggiungi un breve ADR che confronti due opzioni e nomini il responsabile autorizzato ad accettare il rischio residuo.

<a id="sc-100-unit-2"></a>

## 2. Delimitare identità, rete e privilegi

**Scenario:** utenti del campus, docenti ospiti, amministratori, una pipeline di distribuzione e un agente IA accedono a parti diverse del servizio di appunti. Disegna confini di identità, applicazione, rete e amministrazione tra campus e cloud. Specifica permessi minimi, attivazione dei privilegi, accesso di recupero e proprietà di credenziali o federazione. Verifica le ipotesi di funzionalità e licenze per i controlli proposti degli agenti.

**Prove:** sei decisioni attese di autorizzazione o rifiuto, dipendenze dal DNS privato, ipotesi sull'accesso pubblico e una spiegazione di come l'autorizzazione regga quando il percorso di rete è raggiungibile.

**Consegna:** un diagramma dei confini di fiducia e una matrice di accesso con responsabile, ambito, ciclo di vita, registrazione e comportamento in caso di errore. Includi un'azione di strumento negata all'agente e un percorso per l'amministratore di recupero. Mantieni immaginarie tutte le identità e le richieste.

<a id="sc-100-unit-3"></a>

## 3. Collegare rilevamento e risposta autorizzata

**Scenario:** attività sospette delle identità del campus coincidono con download insoliti di documenti. Definisci le capacità SOC necessarie tra identità, endpoint, applicazione, cloud e SaaS. Mappa due percorsi di minaccia prioritari su tecniche MITRE ATT&CK pertinenti, telemetria attesa, correlazione, triage e contenimento. Spiega le responsabilità di Sentinel e Defender XDR senza presumere visibilità completa.

**Prove:** una sequenza temporale sintetica che mostri fonti degli eventi, ritardo di acquisizione, ipotesi di conservazione, un segnale mancante e spiegazioni concorrenti. Identifica chi può disabilitare un'identità o interrompere un server d'esame.

**Consegna:** una matrice di copertura del rilevamento e una tabella dell'autorità di risposta con escalation, approvazione, ripristino e conservazione delle prove. Segna ogni rilevamento e risposta come proposti, con prove di accettazione richieste prima dell'uso operativo.

<a id="sc-100-unit-4"></a>

## 4. Proteggere dati e ciclo di vita di software e IA

**Scenario:** un nuovo assistente IA recupera documenti dei corsi e una pipeline di build ne distribuisce l'API. Classifica le informazioni e mappa i confini di etichette, crittografia, DLP, conservazione e accesso applicativo. Indica dove i controlli non sono supportati. Modella le minacce relative a dipendenze, identità di build, promozione degli artefatti, prompt injection nei documenti e accesso agli strumenti.

**Prove:** un recupero sintetico innocuo, un documento con un'istruzione non attendibile e una build immaginaria non approvata. Registra rifiuti attesi di recupero e strumenti invece di generare istruzioni di exploit o eseguire test.

**Consegna:** una matrice dei controlli dei dati e una revisione del ciclo di vita che mostri responsabile, ambito, provenienza, permessi, approvazione e prove di accettazione. Spiega perché rilevamento, crittografia e mappature dei benchmark lasciano ciascuno rischi separati da valutare.

<a id="sc-100-unit-5"></a>

## 5. Simulare il recupero e ordinare il programma

**Scenario:** un ransomware colpisce l'archivio documentale primario e un account privilegiato. Usa i requisiti dell'esercizio: RTO applicativo di due ore e RPO di quindici minuti. Traccia identità, accesso al piano di controllo, DNS, chiavi, configurazione, metadati, file e dipendenze di distribuzione. Confronta punti di recupero protetti e replica; considera corruzione e amministrazione dei backup compromessa.

**Prove:** un ordine di ripristino simulato a tavolino, timestamp ipotetici di recupero, controlli di coerenza e una dipendenza che impedisca all'applicazione di servire letture autorizzate anche dopo il ritorno dei file. Etichetta le misure come ipotesi.

**Consegna:** un piano di accettazione del recupero e una tabella di marcia in tre fasi limitata al finanziamento di un semestre. Includi responsabili, impegno stimato, prerequisiti, criteri di ripristino, eccezioni con scadenza e approvazione organizzativa del rischio residuo. Non si convalidano alcun ripristino reale o obiettivo di recupero.

[Guida ufficiale SC-100](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100) · [Modello ADR](ADR-template.md)
