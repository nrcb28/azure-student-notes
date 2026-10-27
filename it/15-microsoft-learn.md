# Approfondimenti pratici da Microsoft Learn

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

Riferimenti controllati il 27 ottobre 2026. Spiegazioni rielaborate e casi originali. Le verifiche proposte non sono state eseguite in Azure.

<a id="learn-sas"></a>

## 1. SAS basata su Entra ID

Una user delegation SAS per Blob usa una chiave di delegazione ottenuta con Entra ID. Servono i diritti per ottenerla; conoscere l'URL non basta.

**Caso:** download temporaneo di un PDF. Limitiamo risorsa, lettura e durata, evitando URL sensibili nei log. Separiamo scadenza, autorizzazione e rete nella diagnosi. Pianifichiamo risposta alla fuga del token e revoca secondo il tipo, senza presumere che ogni SAS funzioni allo stesso modo.

[Microsoft Learn · Storage: user delegation SAS](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

<a id="learn-dns"></a>

## 2. Seguire il DNS privato

Il client deve risolvere il nome del servizio verso l'IP del private endpoint. Creare l'interfaccia non configura ogni resolver; le zone dipendono dal servizio.

**Caso:** funziona dalla VM ma non dall'università. Confrontiamo risposte DNS, collegamenti delle zone, inoltro e percorsi. Non sostituiamo indiscriminatamente una zona pubblica né fissiamo un IP nel codice. La risoluzione corretta non concede diritti sui dati.

[Microsoft Learn · Private endpoint DNS](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

<a id="learn-policy"></a>

## 3. Valutazione e remediation

La remediation applica modify o deployIfNotExists alle risorse esistenti utilizzando identità e permessi dell'assegnazione. Una modifica della definizione non aggiorna automaticamente ogni autorizzazione.

**Caso:** risorse vecchie restano non conformi. Controlliamo effetto, ambito, identità e ruoli; proviamo su un gruppo pilota e registriamo i risultati. Deny non trasforma automaticamente qualsiasi configurazione precedente.

[Microsoft Learn · Policy remediation](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

<a id="learn-dcr"></a>

## 4. DCR e raccolta dei dati

Le data collection rules descrivono raccolta e instradamento negli scenari compatibili; possono trasformare o filtrare dati prima della destinazione. Non sostituiscono universalmente diagnostic settings.

**Caso:** mancano eventi di VM. Verifichiamo agente, associazione, origine, flusso, destinazione e schema. Raccogliere tutto aumenta costo e rischio di esposizione; filtrare troppo elimina prove utili.

[Microsoft Learn · Azure Monitor data collection rules](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview)

<a id="learn-whatif"></a>

## 5. Limiti di what-if

What-if prevede cambiamenti senza applicarli. Permessi, dipendenze ed espressioni possono limitare l'analisi. Un risultato incompleto non significa assenza di cambiamenti.

**Caso:** Ignore o modulo non valutato. Leggiamo diagnostica e isoliamo il modulo invece di interpretarlo come NoChange. Distinguiamo compilazione, validazione, previsione e controllo successivo. La revisione deve considerare ciò che non è stato analizzato.

[Microsoft Learn · Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

<a id="learn-slots"></a>

## 6. Slot come applicazioni attive

Uno slot ha hostname e applicazione propri. Copiare impostazioni non clona contenuto, rete privata e tutte le dipendenze. Lo swap comprende preparazione e riscaldamento.

**Caso:** staging invia email reali. Controlliamo connessioni, identità, impostazioni specifiche e processi iniziali. Zero traffico utenti non ferma attività autonome. Tornare allo slot precedente non annulla migrazioni distruttive.

[Microsoft Learn · App Service deployment slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)

<a id="learn-landing"></a>

## 7. Landing zone e responsabilità

Le landing zone organizzano identità, connettività, gestione e governo. Piattaforma e carichi possono avere responsabili distinti; un acceleratore non sostituisce i requisiti.

**Caso:** cinque facoltà condividono rete ma gestiscono app diverse. Definiamo proprietari, confini, permessi, policy e costi. Non copiamo una piattaforma aziendale completa per un piccolo laboratorio senza motivazione.

[Microsoft Learn · Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)

<a id="learn-checks"></a>

## 8. Checks e pubblicazione

In Azure Pipelines i responsabili delle risorse amministrano approvals e checks fuori dal YAML. Prima della fase devono essere soddisfatti i controlli delle risorse utilizzate.

**Caso:** produzione richiede revisione indipendente e finestra oraria. Definiamo risorsa, revisori, timeout e rifiuto. Verifichiamo scadenze e cambiamenti. Un pipeline verde non autorizza ogni service connection.

[Microsoft Learn · Azure Pipelines approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops)

---

[Source register](../LEARN-SOURCES.md) · [Attribution](../ATTRIBUTION.md)

<a id="learn-blob-recovery"></a>

## 9. Recupero dei blob: distinguere i livelli

Soft delete conserva gli oggetti eliminati durante la retention configurata. Non protegge da sola la cancellazione del contenitore o dell'intero account. Separiamo questi rischi.

**Caso:** viene eliminato il contenitore degli appunti. La protezione dei singoli blob non dimostra che il contenitore sia recuperabile. Verifichiamo in anticipo protezione dei contenitori e copie adeguate.

**Procedura:** identificare oggetto, momento, retention già attiva e identità di recupero. Verificare contenuto e permessi, poi riconciliare i metadati. Attivare la funzione dopo l'incidente non significa aver conservato lo stato precedente.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview)

<a id="learn-retry"></a>

## 10. Retry con limiti e idempotenza

I retry aiutano guasti transitori, non credenziali errate o richieste invalide. Limitiamo tentativi e tempo totale e controlliamo quelli già effettuati dagli SDK.

**Caso:** il documento viene registrato ma si perde la risposta. Ripetere può duplicarlo. Servono identificatore stabile e verifica coerente.

**Procedura:** classificare il guasto, rispettare indicazioni di attesa applicabili, fissare scadenza totale e registrare esaurimento dei tentativi senza segreti. Calcolare le richieste reali se più livelli ripetono. Una tempesta di retry può peggiorare la saturazione.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)

<a id="learn-rbac-diagnosis"></a>

## 11. Diagnosticare RBAC con prove

Amministrare risorse non concede automaticamente assegnazione di ruoli o accesso ai dati. Servono azione e ambito adeguati; condizioni possono limitare ruoli e destinatari.

**Caso:** pulsante di assegnazione disabilitato. Verificare account, tenant, ambito e permesso prima di chiedere Owner.

**Procedura:** annotare azione, identità effettiva e risorsa. Esaminare gruppi, assegnazioni dirette ed ereditate, condizioni e piano dati o gestione. Considerare propagazione e aggiornamento credenziali. Riprovare l'operazione minima fallita e conservare la spiegazione del risultato.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting)

<a id="learn-vault-recovery"></a>

## 12. Recuperare Key Vault e le dipendenze

Soft delete consente recupero entro retention. Ripristinare il vault non ricrea automaticamente integrazioni come assegnazioni RBAC e sottoscrizioni Event Grid.

**Caso:** il vault riappare ma l'API non legge il segreto. Controllare identità, permessi e configurazione dei consumatori.

**Procedura:** inventariare oggetti e dipendenze, preparare protezione prima dell'incidente, distinguere recupero e purge. Non usare purge come pulizia improvvisata: dove consentita elimina la possibilità di recuperare l'oggetto. Verificare protezioni e restrizioni. Concludere con una richiesta completa del consumatore autorizzato.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview)
