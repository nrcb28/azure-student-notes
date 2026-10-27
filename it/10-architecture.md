# Architettura e recupero

[Indice](README.md) · [[object Object]](../certifications/it/README.md)

Un progetto parte da utenti, dati, requisiti, budget e capacità operativa. Più servizi non significa progetto migliore.

Per l'app: web/API, database di metadati, Blob per PDF, coda e processo di analisi. È un modello concettuale, non una configurazione pronta per produzione.

RTO è il tempo obiettivo di ripristino; RPO è la perdita recente tollerata espressa in tempo. Ripristinare dati non basta se API, DNS e permessi puntano ancora all'ambiente vecchio.

Progettiamo timeout, retry progressivi, idempotenza e gestione dei guasti parziali. Le prove di recupero devono essere isolate.

**ADR:** contesto, requisiti, alternative, decisione, conseguenze, verifica e condizione di revisione.

**Esercizio:** difendi una soluzione con RTO di due ore e RPO di quindici minuti. Sono requisiti da verificare, non prestazioni garantite da un nome di prodotto.

---

[Precedente](09-costs.md) · [Successivo](11-messaging.md) · [English](../en/10-architecture.md)
