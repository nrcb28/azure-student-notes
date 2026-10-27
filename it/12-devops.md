# DevOps e infrastruttura come codice

[Indice](README.md) · [[object Object]](../certifications/it/README.md)

DevOps combina sviluppo e operazioni per consegnare cambiamenti affidabili. CI integra con build e controlli; continuous delivery mantiene pronto al rilascio; continuous deployment pubblica automaticamente secondo criteri.

Promuoviamo lo stesso artefatto testato. Versioni e digest aiutano a ricostruire cosa era in esecuzione.

Bicep descrive risorse Azure; Terraform mantiene stato da proteggere. Plan e what-if aiutano, ma non garantiscono qualsiasi operazione futura. OIDC evita un segreto duraturo, non la necessità di fiducia federata e permessi.

**Rollback:** tornare al codice precedente non ricrea una colonna eliminata. Preferiamo migrazioni compatibili e recupero provato.

Un runner privilegiato non deve eseguire indiscriminatamente codice non fidato.

**Esercizio:** collega issue, PR, test, artefatto e rilascio. Definisci segnali di promozione e rollback. Esegui localmente python tools/check_docs.py.

---

[Precedente](11-messaging.md) · [Successivo](13-laboratorios.md) · [English](../en/12-devops.md)
