# Calcolo e contenitori

[Indice](README.md) · [Certificazioni](../certifications/it/README.md)

Sceglierei una VM per controllare il sistema operativo, App Service per una web app compatibile, Functions per codice attivato da eventi. Container Instances e Container Apps permettono di eseguire contenitori senza amministrare direttamente un cluster Kubernetes. AKS serve quando i requisiti giustificano Kubernetes e il suo lavoro operativo.

Un contenitore non è una VM completa. Serverless non significa assenza di limiti: avvio, durata, rete e costo dipendono dal piano.

**Diagnosi:** il contenitore parte ma non risponde. Controlliamo porta, processo, configurazione, log e health check, poi una richiesta completa.

Separiamo immagine e configurazione; non inseriamo segreti nei layer. Una versione identificabile è più facile da riprodurre di un tag latest modificabile.

**Esercizio:** giustifica perché una semplice API dovrebbe, oppure non dovrebbe, usare AKS.

---

[Precedente](02-resources.md) · [Successivo](04-storage.md) · [English](../en/03-compute.md)

## Approfondimento Microsoft Learn · slots

Uno slot ha hostname e applicazione propri. Copiare impostazioni non clona contenuto, rete privata e tutte le dipendenze. Lo swap comprende preparazione e riscaldamento.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) · [Approfondimento Microsoft Learn](15-microsoft-learn.md#learn-slots)
