# DevOps e infrastruttura come codice

[Indice](README.md) · [Certificazioni](../certifications/it/README.md)

DevOps combina sviluppo e operazioni per consegnare cambiamenti affidabili. CI integra con build e controlli; continuous delivery mantiene pronto al rilascio; continuous deployment pubblica automaticamente secondo criteri.

Promuoviamo lo stesso artefatto testato. Versioni e digest aiutano a ricostruire cosa era in esecuzione.

Bicep descrive risorse Azure; Terraform mantiene stato da proteggere. Plan e what-if aiutano, ma non garantiscono qualsiasi operazione futura. OIDC evita un segreto duraturo, non la necessità di fiducia federata e permessi.

**Rollback:** tornare al codice precedente non ricrea una colonna eliminata. Preferiamo migrazioni compatibili e recupero provato.

Un runner privilegiato non deve eseguire indiscriminatamente codice non fidato.

**Esercizio:** collega issue, PR, test, artefatto e rilascio. Definisci segnali di promozione e rollback. Esegui localmente python tools/check_docs.py.

---

[Precedente](11-messaging.md) · [Successivo](13-laboratorios.md) · [English](../en/12-devops.md)

## Approfondimento Microsoft Learn · whatif

What-if prevede cambiamenti senza applicarli. Permessi, dipendenze ed espressioni possono limitare l'analisi. Un risultato incompleto non significa assenza di cambiamenti.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if) · [Approfondimento Microsoft Learn](15-microsoft-learn.md#learn-whatif)

## Approfondimento Microsoft Learn · slots

Uno slot ha hostname e applicazione propri. Copiare impostazioni non clona contenuto, rete privata e tutte le dipendenze. Lo swap comprende preparazione e riscaldamento.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) · [Approfondimento Microsoft Learn](15-microsoft-learn.md#learn-slots)

## Approfondimento Microsoft Learn · checks

In Azure Pipelines i responsabili delle risorse amministrano approvals e checks fuori dal YAML. Prima della fase devono essere soddisfatti i controlli delle risorse utilizzate.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops) · [Approfondimento Microsoft Learn](15-microsoft-learn.md#learn-checks)

## Retry con limiti e idempotenza

I retry aiutano guasti transitori, non credenziali errate o richieste invalide. Limitiamo tentativi e tempo totale e controlliamo quelli già effettuati dagli SDK.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) · [Retry con limiti e idempotenza](15-microsoft-learn.md#learn-retry)
