# AZ-700 · 10 casi con risposte ragionate

[Guida](AZ-700.md) · [Quaderno](AZ-700-workbook.md) · [Indice](README.md)

Scenari originali di studio, non quesiti ufficiali o riservati. Prima di aprire la risposta indica il requisito, scarta un'alternativa e identifica le prove. Non si dichiara alcuna esecuzione in Azure.

## 1. Il campus e una nuova VNet Azure usano entrambi 10.70.0.0/16. Un peering ordinario o una VPN rendono univoci gli indirizzi?

<details>
<summary>Ragionamento</summary>

Gli intervalli sovrapposti sono un problema di progettazione, non una regola di autorizzazione mancante. Inventaria le reti reali e scegli spazio non sovrapposto prima di creare peering o connettività ibrida standard. Alcuni scenari ammettono soluzioni di traduzione supportate, ma aggiungono vincoli e richiedono un progetto esplicito. Un pacchetto verso lo stesso intervallo privato non identifica da solo la località voluta. Le prove comprendono inventario degli intervalli, piano rivisto e route attese per ciascuna destinazione.

</details>

## 2. A è in peering con B e B con C, ma A non raggiunge C. Bisogna dare Owner alla VM sorgente?

<details>
<summary>Ragionamento</summary>

No. Il peering VNet non è automaticamente transitivo e un ruolo di amministrazione Azure non crea un percorso di rete mancante. Decidi se serva un collegamento diretto o un progetto di transito supportato. Esamina route, inoltro e sicurezza in entrambe le direzioni. Se interviene un gateway condiviso, controlla le sue impostazioni specifiche di transito anziché presumere che inoltri qualsiasi traffico degli spoke. Le prove utili sono percorso completo e prossimi hop effettivi, non un ruolo amministrativo più ampio.

</details>

## 3. Una nuova route predefinita punta al firewall, ma il traffico per un prefisso più specifico va altrove. Le route definite dall'utente sono tutte guaste?

<details>
<summary>Ragionamento</summary>

Non necessariamente. Esamina tutte le route applicabili e la destinazione effettiva. Non presumere che una route predefinita ampia prevalga su ogni prefisso più specifico. Confronta prefissi, origine delle route e prossimo hop effettivo secondo le regole di Azure. Conferma anche che la tabella prevista sia associata alla subnet sorgente. Le prove devono mostrare prefissi concorrenti e prossimo hop osservato. Cambiare regole di sicurezza non permette di stabilire quale route sia stata selezionata.

</details>

## 4. Le richieste attraversano un'appliance con stato, ma le risposte seguono un altro percorso. Perché una connessione consentita può fallire?

<details>
<summary>Ragionamento</summary>

Un dispositivo con stato può aver bisogno di vedere entrambe le direzioni della connessione. Con routing asimmetrico, il ritorno può saltare il dispositivo che ha registrato il flusso iniziale oppure raggiungerne uno senza stato corrispondente. Esamina route di andata e ritorno, inoltro dell'appliance e traduzioni di indirizzo. Non aggiungere permessi casuali in ingresso prima di verificare l'ipotesi. Una consegna utile è un diagramma di entrambi i percorsi con osservazioni degli endpoint o degli strumenti diagnostici supportati.

</details>

## 5. L'accesso pubblico allo storage è disabilitato. L'API dispone di un endpoint privato ma risolve ancora l'indirizzo pubblico. Da dove cominciare?

<details>
<summary>Ragionamento</summary>

Indaga il percorso DNS effettivo del client API: server configurati, zona privata, collegamento alla VNet ed eventuale inoltro ibrido. Mantieni il nome del servizio e fallo risolvere correttamente per il collegamento privato desiderato. Assegnare Storage Blob Data Reader non corregge una risposta DNS pubblica. Una volta risolti nome e instradamento, verifica separatamente l'autorizzazione sui dati. Registra nome, indirizzo risolto, resolver, sottorisorsa dell'endpoint e successiva operazione autenticata come prove distinte.

</details>

## 6. Il requisito impone di cifrare i dati tra campus e Azure. Acquistare ExpressRoute basta a dimostrarlo?

<details>
<summary>Ragionamento</summary>

No. La connettività privata di ExpressRoute è distinta dalla cifratura e il traffico non viene cifrato per impostazione predefinita. Specifica che cosa proteggere e dove inizi e finisca la protezione. MACsec è un'opzione supportata per collegamenti ExpressRoute Direct, non automaticamente per ogni circuito del fornitore. Un progetto IPsec adeguato può soddisfare un requisito tra estremità. Confronta compatibilità e prestazioni e documenta la gestione delle chiavi. Il solo disegno di un percorso privato non prova la cifratura.

</details>

## 7. Il gruppo vuole selezione regionale tramite DNS e si aspetta che tutte le richieste attraversino Traffic Manager. Cosa correggere?

<details>
<summary>Ragionamento</summary>

Traffic Manager seleziona endpoint tramite DNS; non agisce da proxy delle richieste. Il client si collega alla destinazione selezionata e le cache possono ritardare l'effetto di una modifica DNS. Se serve un proxy HTTP globale, valuta Azure Front Door rispetto ai requisiti. Se serve instradamento HTTP regionale, valuta Application Gateway. Mostra lo scambio DNS separatamente dalla connessione applicativa e spiega come le informazioni sullo stato degli endpoint influenzino la selezione.

</details>

## 8. È stato abilitato un endpoint di servizio su una subnet. Perché questo non prova che lo storage abbia ora un indirizzo di endpoint privato?

<details>
<summary>Ragionamento</summary>

Endpoint di servizio ed endpoint privati sono progetti diversi. Abilitare il primo non crea nella subnet un'interfaccia privata per l'account di archiviazione. Controlla configurazione effettiva dell'endpoint di servizio, regole di rete del servizio e metodo di autenticazione. Se il requisito richiede espressamente una destinazione privata, valuta un endpoint privato supportato con DNS e impostazioni di accesso. Registra destinazione risolta e configurazione delle risorse, senza trattare la parola comune «endpoint» come equivalenza tecnica.

</details>

## 9. Una regola di negazione blocca nuove connessioni, ma una sessione già aperta continua. L'NSG sta necessariamente ignorando le regole?

<details>
<summary>Ragionamento</summary>

No. Gli NSG sono con stato: una modifica non interrompe necessariamente subito un flusso esistente. Distingui una connessione realmente nuova da una sessione riutilizzata, poi controlla le regole effettive di subnet e interfaccia. Verifica sorgente, destinazione, porta, protocollo e priorità, senza affidarti al nome della regola. L'osservazione deve indicare se la prova abbia creato un nuovo flusso. Ruoli più ampi o l'eliminazione della VM non spiegherebbero questo comportamento.

</details>

## 10. Un diagramma mostra ExpressRoute e una VPN di riserva. Quali prove mancano prima di dichiarare resiliente la connettività applicativa?

<details>
<summary>Ragionamento</summary>

Identifica domini di guasto condivisi e verifica l'intero percorso di riserva. Controlla apparati del cliente, fornitori, sedi di peering, gateway, annunci delle route, ritorno, capacità del tunnel, dipendenze DNS e riconnessione applicativa. Una seconda linea nel disegno non dimostra che il traffico la scelga correttamente al guasto. Proponi una prova isolata e autorizzata con risultati attesi e osservati e criteri di recupero e ritorno normale. Gli appunti forniscono il progetto dell'esercizio, senza dichiarare di aver eseguito il passaggio alla riserva.

</details>

Fonti tecniche e riferimento d'esame verificato sono nella [guida](AZ-700.md). Prosegui con il [quaderno](AZ-700-workbook.md) per trasformare le risposte in diagrammi e prove.
