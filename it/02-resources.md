# Risorse e disponibilità

[Indice](README.md) · [[object Object]](../certifications/it/README.md)

Una sottoscrizione delimita amministrazione, quote e fatturazione. I gruppi di gestione applicano governo a più sottoscrizioni. Un gruppo di risorse raccoglie elementi con un ciclo di vita correlato. Il tenant Entra è la directory delle identità, non un normale contenitore di risorse.

La regione del gruppo riguarda i metadati: le risorse possono trovarsi altrove. Una zona di disponibilità offre separazione fisica all'interno di una regione. Non tutti i servizi supportano le stesse opzioni.

**Esempio:** teniamo sviluppo e produzione separati. Una rete condivisa non va eliminata insieme a una singola app.

Prima di spostare risorse controlliamo supporto, dipendenze, autorizzazioni e identificatori. Spostare tra gruppi non equivale a migrare regione.

**Verifica:** descrivi quale guasto tollera davvero il progetto, invece di limitarti a contare le istanze.

---

[Precedente](01-fundamentals.md) · [Successivo](03-compute.md) · [English](../en/02-resources.md)
