# AZ-104 · Quaderno avanzato comune

[←](README.md) · [Nucleo comune di studio](../../it/16-common-core.md) · [Laboratori avanzati](../../it/17-advanced-labs.md)

Obiettivi, scenari e consegne corrispondono nelle otto lingue. L'equivalenza si controlla per unità ed evidenze, non contando parole. Le guide precedenti restano spiegazioni complementari.

<a id="az-104-unit-1"></a>

## 1. Ricostruire accesso effettivo

Annota identità, tenant, sottoscrizione, risorsa, azione e ambito. Esamina gruppi, assegnazioni dirette ed ereditate, condizioni e propagazione. Separa gestione e dati. Assegnare ruoli richiede permessi propri.

**Caso:** si crea Storage ma non si elencano blob. **Evidenza:** permesso necessario e verifica minima con la stessa identità. Non usare Owner come test generale né cambiare rete senza ipotesi.

<a id="az-104-unit-2"></a>

## 2. Proteggere e recuperare

Scegli protezione per oggetto, contenitore e account. Registra ciò che era attivo prima dell'incidente. Con versioning può servire selezionare o promuovere una versione; non esiste una procedura unica per ogni configurazione.

**Caso:** recuperare un file identico. **Evidenza:** configurazione precedente, hash prima/dopo, diritti verificati e dati ancora trattenuti dopo pulizia.

<a id="az-104-unit-3"></a>

## 3. Leggere prima di modificare

Interpreta parametri, risorse, dipendenze, output e differenze. Separa compilazione, validazione, what-if e applicazione. Un export può richiedere revisione; quote, regioni e Policy possono bloccare sintassi valida.

**Caso:** modulo non analizzato da what-if. **Evidenza:** diagnosi e ambito escluso, da risolvere prima di applicare. Rivedi dischi, rete e impostazioni nei cambiamenti di VM.

<a id="az-104-unit-4"></a>

## 4. Diagnosticare tutto il percorso

Segui DNS, IP, route, NSG, firewall del sistema, listener e autorizzazione. I filtri sono con stato e possono combinarsi. Verifica frontend, backend, regola e probe. Separa ingresso privato App Service e integrazione uscente.

**Caso:** probe sano e richiesta fallita. **Evidenza:** porta e risposta di ogni prova, regole e ipotesi verificabile. La salute del probe non dimostra correttezza funzionale.

<a id="az-104-unit-5"></a>

## 5. Operare con evidenze

Definisci metrica, log, alert, azione e responsabile. Controlla origine, associazione e destinazione prima della query. Misura recupero completo con identità, DNS e dipendenze.

**Consegna:** pratiche Storage e ispezione ruoli, previsto contro osservato e runbook. Distingui prove locali e Azure; verifica eliminazione o retention residua.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104) · [AZ-104](AZ-104.md)
