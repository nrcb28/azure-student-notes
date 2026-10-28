# AZ-305 · Quaderno avanzato comune

[←](README.md) · [Nucleo comune di studio](../../it/16-common-core.md) · [Laboratori avanzati](../../it/17-advanced-labs.md)

Obiettivi, scenari e consegne corrispondono nelle otto lingue. L'equivalenza si controlla per unità ed evidenze, non contando parole. Le guide precedenti restano spiegazioni complementari.

<a id="az-305-unit-1"></a>

## 1. Tradurre bisogni in vincoli

Definisci utenti, crescita, residenza, privacy, prestazioni, RTO, RPO, budget e competenze. Separa fatti da ipotesi. Sempre disponibile richiede operazioni e finestra misurabili.

**Caso:** cinque facoltà condividono rete ma hanno dati privati. **Evidenza:** confini, proprietari e requisito che impone separazione. Non scegliere un'architettura per la sua grandezza.

<a id="az-305-unit-2"></a>

## 2. Progettare dati e stato

Confronta query, transazioni, compatibilità, consistenza e recupero. JSON non decide il motore. Scalare letture non aumenta necessariamente scritture. Distingui stato applicativo, sessioni e documenti.

**Caso:** cache veloce con permessi vecchi. **Evidenza:** invalidazione, scadenza, comportamento in guasto e dati che non devono fidarsi di copie obsolete.

<a id="az-305-unit-3"></a>

## 3. Recuperare il servizio completo

Assegna RTO/RPO a servizi e dati. Includi capacità, credenziali, permessi, DNS e configurazione. La replica può propagare danni logici. Confronta attivo-attivo e passivo con costi e complessità.

**Caso:** Key Vault ritorna senza integrazioni. **Evidenza:** ordine di recupero, prova del consumatore autorizzato, dipendenze non ripristinate automaticamente e prova isolata.

<a id="az-305-unit-4"></a>

## 4. Esecuzione e comunicazione

Confronta VM, PaaS, contenitori e batch per controllo, durata e operazione. Una coda aggiunge stati e duplicati. Progetta timeout, retry limitato e idempotenza prima di aumentare consumer.

**Caso:** risposta persa e messaggio ripetuto. **Evidenza:** ID stabile, limite tentativi e gestione parziale. Giustifica cluster oppure piattaforma semplice.

<a id="az-305-unit-5"></a>

## 5. Migrazione documentata

Inventaria dipendenze e uso, verifica compatibilità, pilota, trasferimento iniziale, modifiche successive, cutover e rollback. Definisci integrità e ritiro dell'origine. La VM senza file richiesti non completa la migrazione.

**Consegna:** due ADR, rete, recupero e rischi. Per ogni decisione: alternativa ragionevole, conseguenza, prova e revisione. Rivaluta con budget o residenza diversi.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305) · [AZ-305](AZ-305.md)
