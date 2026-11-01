# DP-300 · Quaderno operativo comune

[Guida](DP-300.md) · [Dieci casi](DP-300-cases.md) · [Indice](README.md)

Cinque unità con obiettivi e prove corrispondenti nelle otto edizioni linguistiche. Se necessario, completa la progettazione senza Azure. Separa comportamento atteso da quanto sia stato realmente osservato. Non si dichiarano esecuzione in Azure o copertura completa dell'esame.

<a id="dp-300-unit-1"></a>

## 1. Motivare piattaforma e scelta di migrazione

Scrivi una tabella dei requisiti dell'app: funzionalità necessarie del database, accesso al sistema operativo, dipendenze di istanza, interruzione delle scritture accettabile, responsabilità di manutenzione e obiettivi di recupero. Confronta SQL Database, Managed Instance e SQL Server su VM rispetto ai requisiti, invece di assegnare punti ai nomi conosciuti.

**Caso:** un'attività pianificata esistente dipende da uno strumento del sistema operativo. **Prove:** stabilisci se la dipendenza resti necessaria, una destinazione o riprogettazione supportata e una verifica di compatibilità. **Consegna:** sequenza di migrazione con trasferimento iniziale, blocco delle scritture, validazione, passaggio, responsabile del ritorno e piano per le scritture successive. Una copia completata non è il collaudo di accettazione.

<a id="dp-300-unit-2"></a>

## 2. Separare accesso e confini di riservatezza

Disegna il percorso dall'identità applicativa a un'operazione consentita su una tabella. Segna risoluzione del nome, accesso di rete, autenticazione, entità nel database e permessi degli oggetti. Separa compiti dell'applicazione, distribuzione e amministrazione d'emergenza. Specifica quali dati possano apparire in query, log, esportazioni e backup.

**Caso:** la connessione privata funziona ma l'app non legge la sua tabella. **Prove:** identità effettiva, database, oggetto e operazione negata; non ampliare la rete pubblica al posto della diagnosi. **Consegna:** progetto dei permessi minimi e confronto tra cifratura del trasporto, TDE, Always Encrypted e mascheramento rispetto a uno specifico requisito di riservatezza. Includi recupero delle chiavi e responsabilità.

<a id="dp-300-unit-3"></a>

## 3. Diagnosticare una regressione misurata

Inventa due finestre comparabili di carico per una query sui permessi dei documenti, con durata, letture, CPU, concorrenza e identità del piano. Scrivi un'ipotesi che colleghi cambiamento e prove, quindi un'osservazione che la smentirebbe. Includi blocchi e durata delle transazioni insieme allo storico disponibile di Query Store: né una metrica normale della piattaforma né un operatore apparentemente costoso dimostrano da soli la causa.

**Caso:** un indice migliora le letture e rallenta le importazioni. **Prove:** risultati prima e dopo per entrambe le operazioni sotto un carico rappresentativo. **Consegna:** un esperimento reversibile, soglie di accettazione, passi di ritorno e limiti delle prove. Non proporre riduzioni dei file o terminazione di tutte le sessioni come manutenzione ordinaria.

<a id="dp-300-unit-4"></a>

## 4. Rendere l'automazione osservabile e ripetibile

Classifica un'attività notturna secondo lavoro e piattaforma di destinazione. Confronta SQL Agent per carichi SQL Server o Managed Instance supportati con Elastic Jobs per attività T-SQL di SQL Database. Specifica identità, destinazioni, calendario, timeout, limite dei tentativi e notifica di errore. Dipendenze esterne possono richiedere un orchestratore più ampio.

**Caso:** un'attività conferma il proprio risultato ma perde la risposta positiva. **Prove:** spiega come la ripetizione eviti duplicati aziendali e come l'operatore confermi il completamento. **Consegna:** tabella degli stati in attesa, in esecuzione, completato e incerto, più piano di prova con dati sintetici. Non confondere l'invocazione riuscita del pianificatore con un risultato aziendale verificato.

<a id="dp-300-unit-5"></a>

## 5. Recuperare dati e servizio completo

Definisci incidenti distinti di cancellazione accidentale e interruzione regionale. Scegli stati di recupero conservati e meccanismi di disponibilità per il problema risolto da ciascuno. Definisci RPO e RTO rispetto all'app degli appunti, quindi permessi, capacità di destinazione, endpoint, DNS, autenticazione e dipendenze necessari al ripristino. La replica può propagare una modifica indesiderata già confermata.

**Caso:** il nuovo primario è sano ma gli utenti non scaricano gli appunti. **Prove:** verifica funzionale e sequenza temporizzata che includa la riconnessione. **Consegna:** piano di validazione di un ripristino isolato, decisione sulla copia autorevole prima del ritorno e responsabilità di pulizia dei dati conservati. Indica i tempi proposti come ATTESI finché non osservati in un ambiente adatto: un'esercitazione teorica non misura il recupero in Azure.

[Obiettivi ufficiali](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300) · [Guida e fonti tecniche](DP-300.md)
