# Archiviazione e dati

[Indice](README.md) · [Certificazioni](../certifications/it/README.md)

Blob Storage conserva oggetti come PDF; Azure Files offre condivisioni; Managed Disks supporta VM. Un database relazionale gestisce relazioni e transazioni. Il fatto che un'API scambi JSON non impone un database documentale.

LRS replica localmente, ZRS tra zone. GRS e GZRS aggiungono replica geografica asincrona: le scritture recenti possono non essere già nella regione secondaria.

Versioning, eliminazione temporanea e backup affrontano rischi diversi dalla ridondanza. Archive può richiedere reidratazione: non è adatto a documenti da aprire immediatamente.

**App di appunti:** PDF in Blob, metadati nel database. Recuperare il file senza la sua registrazione può lasciare dati incoerenti.

Le SAS sono credenziali: limitiamo permessi e durata. Separiamo accesso amministrativo e accesso ai dati.

**Esercizio:** spiega come recuperare un documento eliminato dieci giorni fa.

---

[Precedente](03-compute.md) · [Successivo](05-networking.md) · [English](../en/04-storage.md)

## Approfondimento Microsoft Learn · sas

Una user delegation SAS per Blob usa una chiave di delegazione ottenuta con Entra ID. Servono i diritti per ottenerla; conoscere l'URL non basta.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli) · [Approfondimento Microsoft Learn](15-microsoft-learn.md#learn-sas)
