# AZ-700 · Quaderno avanzato comune

[Guida](AZ-700.md) · [10 casi](AZ-700-cases.md) · [Indice](README.md) · [Laboratorio di rete](network-lab.md)

Cinque unità con obiettivi, scenari e consegne corrispondenti nelle otto lingue. Sono esercizi di progettazione e diagnosi. Le previsioni non sono osservazioni di Azure e non si dichiara alcuna nuova distribuzione.

<a id="az-700-unit-1"></a>

## 1. Costruire un piano di indirizzi e dipendenze

Progetta reti del campus, hub, web e dati per l'app degli appunti. Inventaria gli intervalli esistenti prima di scegliere nuovi CIDR e riserva spazio alla crescita e alle subnet specifiche dei servizi. Spiega perché una /24 ordinaria abbia in Azure meno indirizzi IPv4 assegnabili del suo totale grezzo. Non presumere che un servizio delegato possa stare in qualsiasi subnet vuota.

**Scenario:** un partner usa un intervallo sovrapposto all'hub proposto. **Prove:** tabella con proprietario, prefisso, scopo, vincoli e spazio di crescita. **Consegna:** progetto rivisto senza sovrapposizioni, conflitto eliminato e un vincolo ancora da controllare nella documentazione attuale del servizio.

<a id="az-700-unit-2"></a>

## 2. Seguire una richiesta e la sua risposta

Disegna una chiamata API da uno spoke web, attraverso un'appliance di ispezione, verso un'altra rete. Scrivi a ogni passaggio prefisso di destinazione, prossimo hop e impostazione di inoltro pertinente. Disegna separatamente la risposta: ispezione con stato e traduzione di indirizzi possono far fallire un percorso asimmetrico apparentemente plausibile. Il peering da solo non trasforma un hub in router di transito.

**Scenario:** dopo una modifica UDR la sorgente invia richieste ma non riceve risposta. **Prove:** route concorrenti e prossimo hop effettivo in ciascuna direzione. **Consegna:** un'ipotesi verificabile, un'osservazione di conferma e una condizione di ripristino per la modifica proposta.

<a id="az-700-unit-3"></a>

## 3. Diagnosticare l'accesso privato per livelli

Descrivi come un client del campus risolva il nome dello storage attraverso il progetto DNS e di inoltro scelto. Identifica sottorisorsa del servizio, indirizzo privato, stato dell'approvazione e restrizioni di rete previste per l'endpoint. Separa risoluzione, raggiungibilità, TLS e permessi sui dati: dimostrarne uno non dimostra gli altri.

**Scenario:** accesso pubblico disabilitato, ma il chiamante risolve ancora un indirizzo pubblico. **Prove:** nome, percorso del resolver, indirizzo restituito e destinazione privata attesa. **Consegna:** proposta di correzione DNS e successive verifiche di routing e accesso autenticato ai dati. Spiega perché una sostituzione permanente con l'IP pubblico sia inadatta.

<a id="az-700-unit-4"></a>

## 4. Scegliere distribuzione e controlli di protezione

Confronta un servizio TCP, un'app web regionale e una globale. Scegli i candidati per protocollo, ambito, esigenze di instradamento e comportamento ai guasti, non in base a un'etichetta di prodotto memorizzata. Includi sonde e gestione dei certificati. Distingui selezione DNS e proxy delle richieste, ispezione WAF, filtri di rete e protezione della disponibilità da DDoS.

**Scenario:** il backend supera la sonda ma scarica documenti sbagliati. **Prove:** cosa controlli la sonda e cosa validi un'operazione reale. **Consegna:** breve decisione architetturale con un'alternativa scartata e un segnale funzionale che fermerebbe la promozione di una versione difettosa.

<a id="az-700-unit-5"></a>

## 5. Progettare e verificare il recupero ibrido

Pianifica collegamento principale e di riserva del campus. Elenca guasti correlati, cambi di routing, requisiti di cifratura, capacità e dipendenze applicative. La riservatezza del percorso ExpressRoute non dimostra cifratura predefinita. Specifica confine da proteggere e progetto di cifratura compatibile; non supporre che tutti i tipi di circuito offrano le stesse opzioni.

**Scenario:** il collegamento principale cade mentre molti studenti scaricano appunti. **Prove:** percorsi di andata e ritorno attesi, ipotesi sulla capacità di riserva e criteri misurabili di recupero dell'applicazione. **Consegna:** piano di prova isolata, passaggi di ritorno al funzionamento normale e colonne atteso/osservato. Se manca un ambiente autorizzato, consegna il progetto e indica esplicitamente che le osservazioni non sono state eseguite.

[Guida ufficiale](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700) · [Spiegazioni tecniche](AZ-700.md)
