# Messaggi ed eventi

[Indice](README.md) · [Certificazioni](../certifications/it/README.md)

Una coda disaccoppia invio e lavorazione. Storage Queues serve code semplici; Service Bus offre code e topic; Event Grid distribuisce eventi; Event Hubs acquisisce flussi su larga scala. Non sono sostituti automatici.

Un messaggio può tornare dopo che il lavoro è stato completato ma prima della conferma. Il consumer deve tollerare ripetizioni mediante identificatori stabili e aggiornamenti coerenti.

**Miniature:** il messaggio identifica il documento; il processo verifica il risultato, lo genera e conferma. Consideriamo anche consumatori concorrenti e operazioni atomiche.

Monitoriamo età e quantità della coda. Aggiungere consumer non aiuta se il collo di bottiglia è il database. Ordine e gestione dei messaggi falliti dipendono dal servizio.

**Esercizio:** pianifica il replay di messaggi falliti senza duplicare documenti né cancellare la cronologia degli errori.

---

[Precedente](10-architecture.md) · [Successivo](12-devops.md) · [English](../en/11-messaging.md)
