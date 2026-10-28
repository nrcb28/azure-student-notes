# AZ-400 · Quaderno avanzato comune

[←](README.md) · [Nucleo comune di studio](../../it/16-common-core.md) · [Laboratori avanzati](../../it/17-advanced-labs.md)

Obiettivi, scenari e consegne corrispondono nelle otto lingue. L'equivalenza si controlla per unità ed evidenze, non contando parole. Le guide precedenti restano spiegazioni complementari.

<a id="az-400-unit-1"></a>

## 1. Tracciabilità e Git

Collega bisogno, issue, PR, commit, build, artefatto e deploy. Definisci metriche coerenti, non valore personale tramite commit. Scegli rami secondo frequenza e versioni mantenute.

**Caso:** annullare una release condivisa. **Evidenza:** revert contro riscrittura e impatto sui dati. Se è uscito un segreto, revoca o rotazione prima della semplice cancellazione.

<a id="az-400-unit-2"></a>

## 2. Test e artefatti

Costruisci una volta, promuovi lo stesso risultato identificato. Registra versione, digest e origine. Combina test secondo rischio; coverage non dimostra asserzioni utili.

**Caso:** ieri funzionava senza modifiche. **Evidenza:** strumenti, dipendenze e immagini non fissati. Indaga test instabili invece di ripetere fino al verde. Distingui cache e artefatti.

<a id="az-400-unit-3"></a>

## 3. Identità del runner

Separa codice fidato, input PR, permessi workflow e ambito cloud. Runner propri richiedono isolamento, aggiornamento e pulizia. OIDC richiede ancora fiducia e autorizzazione precise.

**Caso:** PR esterno modifica script interno. **Evidenza:** esecuzione senza produzione, limiti di identità e controlli delle risorse. Il codice di pipeline non è innocuo per definizione.

<a id="az-400-unit-4"></a>

## 4. Distribuire e tornare indietro

Confronta rolling, blue-green, canary, rings e flag. Definisci pubblico, segnali funzionali, osservazione e arresto. Swap non isola ogni dipendenza. Preferisci migrazioni compatibili quando possibile.

**Caso:** CPU normale ma risultato errato. **Evidenza:** segnale applicativo e criterio rollback. Spiega perché l'immagine precedente non ricrea una colonna eliminata.

<a id="az-400-unit-5"></a>

## 5. Chiudere il ciclo

Propaga contesto, associa versione alla telemetria e proteggi dati registrati. Definisci responsabili e finestre degli alert. Le approvazioni delle risorse non sono solo condizioni YAML modificabili.

**Consegna:** pipeline completa, test significativo, artefatto fisso e promozione. Esegui il simulatore e ripeti con retry diverso. Postmortem con azione, responsabile e verifica.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400) · [AZ-400](AZ-400.md)
