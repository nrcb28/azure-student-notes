# Architettura e recupero

[Indice](README.md) · [Certificazioni](../certifications/it/README.md)

Un progetto parte da utenti, dati, requisiti, budget e capacità operativa. Più servizi non significa progetto migliore.

Per l'app: web/API, database di metadati, Blob per PDF, coda e processo di analisi. È un modello concettuale, non una configurazione pronta per produzione.

RTO è il tempo obiettivo di ripristino; RPO è la perdita recente tollerata espressa in tempo. Ripristinare dati non basta se API, DNS e permessi puntano ancora all'ambiente vecchio.

Progettiamo timeout, retry progressivi, idempotenza e gestione dei guasti parziali. Le prove di recupero devono essere isolate.

**ADR:** contesto, requisiti, alternative, decisione, conseguenze, verifica e condizione di revisione.

**Esercizio:** difendi una soluzione con RTO di due ore e RPO di quindici minuti. Sono requisiti da verificare, non prestazioni garantite da un nome di prodotto.

---

[Precedente](09-costs.md) · [Successivo](11-messaging.md) · [English](../en/10-architecture.md)

## Approfondimento Microsoft Learn · landing

Le landing zone organizzano identità, connettività, gestione e governo. Piattaforma e carichi possono avere responsabili distinti; un acceleratore non sostituisce i requisiti.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) · [Approfondimento Microsoft Learn](15-microsoft-learn.md#learn-landing)

## Recupero dei blob: distinguere i livelli

Soft delete conserva gli oggetti eliminati durante la retention configurata. Non protegge da sola la cancellazione del contenitore o dell'intero account. Separiamo questi rischi.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview) · [Recupero dei blob: distinguere i livelli](15-microsoft-learn.md#learn-blob-recovery)

## Retry con limiti e idempotenza

I retry aiutano guasti transitori, non credenziali errate o richieste invalide. Limitiamo tentativi e tempo totale e controlliamo quelli già effettuati dagli SDK.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) · [Retry con limiti e idempotenza](15-microsoft-learn.md#learn-retry)

## Recuperare Key Vault e le dipendenze

Soft delete consente recupero entro retention. Ripristinare il vault non ricrea automaticamente integrazioni come assegnazioni RBAC e sottoscrizioni Event Grid.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview) · [Recuperare Key Vault e le dipendenze](15-microsoft-learn.md#learn-vault-recovery)
