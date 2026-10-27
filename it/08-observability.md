# Monitoraggio e diagnosi

[Indice](README.md) · [Certificazioni](../certifications/it/README.md)

Metriche, log e tracce raccontano aspetti diversi. Azure Monitor raccoglie capacità di osservazione; Application Insights segue applicazioni; Log Analytics interroga i log disponibili con KQL.

CPU bassa non significa applicazione veloce: potrebbe aspettare un database. Le medie possono nascondere richieste molto lente; guardiamo distribuzione, percentili e volume.

Un alert utile ha segnale, soglia, finestra e azione. Service Health riguarda problemi dei servizi usati; Resource Health riguarda una risorsa.

**Metodo:** delimitare impatto e inizio, controllare ultimo cambiamento, seguire una richiesta e dipendenze, verificare l'ipotesi, correggere e confermare recupero.

Non registriamo token o documenti completi. Retention e verbosità influenzano costo e privacy. OpenTelemetry va configurato secondo runtime e integrazione.

**Esercizio:** misura successo dei caricamenti, latenza e tempo di analisi, non soltanto CPU.

---

[Precedente](07-governance.md) · [Successivo](09-costs.md) · [English](../en/08-observability.md)

## Approfondimento Microsoft Learn · dcr

Le data collection rules descrivono raccolta e instradamento negli scenari compatibili; possono trasformare o filtrare dati prima della destinazione. Non sostituiscono universalmente diagnostic settings.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview) · [Approfondimento Microsoft Learn](15-microsoft-learn.md#learn-dcr)
