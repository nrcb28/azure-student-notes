# Identità e sicurezza

[Indice](README.md) · [Certificazioni](../certifications/it/README.md)

Entra ID gestisce identità. Autenticazione significa dimostrare chi siamo; autorizzazione decide cosa possiamo fare. MFA rafforza la prima, non concede accesso ai documenti.

Azure RBAC combina identità, ruolo e ambito. Reader consulta, Contributor amministra senza concedere assegnazioni RBAC, Owner può anche concedere accesso. I ruoli di directory sono distinti dai ruoli sulle risorse.

Una managed identity evita credenziali applicative conservate da noi, ma richiede comunque permessi. Key Vault gestisce segreti, chiavi e certificati.

**Caso:** rimuoviamo Reader da una risorsa e l'utente mantiene accesso. Controlliamo gruppi e assegnazioni ereditate prima di pensare a un errore.

La nostra app deve verificare il proprietario di ogni documento: essere autenticati non permette di modificare gli appunti altrui.

**Esercizio:** definisci permessi diversi per studente, API e processo di miniature.

---

[Precedente](05-networking.md) · [Successivo](07-governance.md) · [English](../en/06-identity.md)

## Approfondimento Microsoft Learn · sas

Una user delegation SAS per Blob usa una chiave di delegazione ottenuta con Entra ID. Servono i diritti per ottenerla; conoscere l'URL non basta.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli) · [Approfondimento Microsoft Learn](15-microsoft-learn.md#learn-sas)
