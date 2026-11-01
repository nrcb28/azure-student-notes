# AZ-140 · Quaderno avanzato comune

[Guida](AZ-140.md) · [10 casi](AZ-140-cases.md) · [Indice](README.md)

Cinque unità corrispondenti tra le lingue. Lavora offline usando l'app universitaria di appunti e il laboratorio informatico virtuale. Registra le previsioni come previsioni; queste unità non distribuiscono nulla, non modificano tenant e non dimostrano che il sistema sia pronto per la produzione.

<a id="az-140-unit-1"></a>

## 1. Mappare risorse, utenti e responsabilità

Disegna un laboratorio in pool per 48 studenti e un desktop personale per un ricercatore. Identifica pool di host, host di sessione, gruppi di applicazioni, registrazione nell'area di lavoro e assegnazioni agli utenti. Separa le responsabilità Microsoft per broker e gateway da quelle del cliente per immagini, VM, rete, integrazione delle identità e archiviazione. Spiega perché il funzionamento multisessione supportato è diverso dall'assegnazione personale.

**Scenario:** uno studente vede le VM Azure ma il feed dei desktop è vuoto. **Prove:** un diagramma delle relazioni tra risorse, diritto effettivo sul gruppo di applicazioni, account client previsto e ipotesi sulle licenze. **Consegna:** i primi tre controlli, un ampliamento inadatto dei ruoli che scarti e un responsabile per ogni dipendenza gestita dal cliente. Collega il progetto ai [fondamenti di calcolo](../../it/03-compute.md).

<a id="az-140-unit-2"></a>

## 2. Tracciare separatamente identità e trasporto

Confronta join a Entra, join ad AD DS e join a Entra Domain Services rispetto a un'app legacy e all'autenticazione scelta per l'archiviazione dei profili. Disegna autenticazione del feed, diritto di accesso, accesso alla sessione e accesso ai file come fasi separate. Aggiungi la connessione inversa HTTPS in uscita e un percorso UDP Shortpath specifico per l'opzione scelta. Spiega la raggiungibilità privata del listener gestito e come ICE/STUN o TURN cambino i requisiti di trasporto.

**Scenario:** gli utenti del campus si connettono senza problemi; quelli a casa ricevono un'altra richiesta di accesso e sessioni più lente. **Prove:** versione del client, tipo di join, ipotesi su SSO e Conditional Access, trasporto negoziato, percorso DNS e osservazioni di latenza necessarie. **Consegna:** due ipotesi indipendenti e relative prove di conferma, senza esporre TCP 3389 pubblico. Ripassa i [fondamenti di rete](../../it/05-networking.md).

<a id="az-140-unit-3"></a>

## 3. Proteggere i profili e pubblicare un'app utilizzabile

Progetta contenitori FSLogix persistenti fuori dagli host in pool sostituibili. Documenta compatibilità di identità e Kerberos dell'archiviazione, permessi di condivisione e NTFS, capacità, ipotesi sui picchi di accesso, comportamento a connessione singola e obiettivi di backup e ripristino. Distingui preferenze del profilo e dati autorevoli degli appunti. Confronta l'installazione dell'editor nell'immagine con un pacchetto App Attach supportato e spiega separatamente la pubblicazione RemoteApp.

**Scenario:** uno studente raggiunge il desktop ma riceve un profilo temporaneo e non può avviare l'editor. **Prove:** errore di collegamento del contenitore, titolarità della sessione attiva, permessi previsti, versione dell'immagine host, accesso al pacchetto e assegnazioni. **Consegna:** un albero dei guasti ordinato con rami distinti per profilo e applicazione, una proposta sicura di recupero e criteri per conservare il lavoro utente esistente.

<a id="az-140-unit-4"></a>

## 4. Rilasciare immagini e calcolare la capacità dell'aula

Scrivi un piano di rilascio dell'immagine master con versioni che comprenda sistema operativo supportato, agenti, criteri di sicurezza, applicazioni, utenti di convalida, comportamento drain e rollback. Con un limite misurato di 12 sessioni per host, calcola la capacità per 48 studenti durante il guasto di un host. Distingui il metodo scelto dal piano di scalabilità da Start VM on Connect; includi tempo di avvio, stato, massimo di sessioni e vincoli di archiviazione.

**Scenario:** arriva una patch prima della lezione mentre un host è già indisponibile. **Prove:** una tabella di capacità di cinque host, versioni delle immagini, elenco dei controlli di convalida, sessioni attive ed esclusioni dalla manutenzione. **Consegna:** un rilascio graduale che mantenga capacità utilizzabile sufficiente, con trigger di rollback e un criterio esplicito per gli utenti ancora connessi durante la riduzione della capacità.

<a id="az-140-unit-5"></a>

## 5. Simulare un errore di accesso e il recupero

Segui una connessione sintetica usando timestamp UTC, utente pseudonimo, risorsa, host e ID di correlazione. Specifica impostazioni diagnostiche, raccolta delle prestazioni host, log FSLogix e osservazioni necessarie sull'esperienza utente. Spiega perché un tentativo che non raggiunge AVD può non lasciare un record di connessione. Aggiungi dipendenze di identità, DNS, pacchetti applicativi, profili e API degli appunti a un piano di recupero in un'area geografica alternativa.

**Scenario:** la lezione delle 09:00 non riesce a ripristinare i profili dopo un'interruzione dell'archiviazione. **Prove:** checkpoint previsti, confronto con una sessione normale, obiettivi di recupero dei profili, capacità disponibile e responsabili dei costi continuativi di VM, dischi, archiviazione, rete, monitoraggio e licenze. **Consegna:** una cronologia dell'incidente, un'ipotesi sulla prima fase fallita, criteri di recupero e ritorno all'area primaria e un confine chiaro tra previsioni della simulazione e prove osservate.

Usa i sei riferimenti tecnici nella [guida](AZ-140.md) per mettere alla prova le ipotesi. Questi esercizi sono materiale di studio originale e non coprono ogni obiettivo ufficiale né garantiscono un risultato all'esame.
