# Archiviazione e dati

[Indice](README.md) · [[object Object]](../certifications/it/README.md)

Blob Storage conserva oggetti come PDF; Azure Files offre condivisioni; Managed Disks supporta VM. Un database relazionale gestisce relazioni e transazioni. Il fatto che un'API scambi JSON non impone un database documentale.

LRS replica localmente, ZRS tra zone. GRS e GZRS aggiungono replica geografica asincrona: le scritture recenti possono non essere già nella regione secondaria.

Versioning, eliminazione temporanea e backup affrontano rischi diversi dalla ridondanza. Archive può richiedere reidratazione: non è adatto a documenti da aprire immediatamente.

**App di appunti:** PDF in Blob, metadati nel database. Recuperare il file senza la sua registrazione può lasciare dati incoerenti.

Le SAS sono credenziali: limitiamo permessi e durata. Separiamo accesso amministrativo e accesso ai dati.

**Esercizio:** spiega come recuperare un documento eliminato dieci giorni fa.

---

[Precedente](03-compute.md) · [Successivo](05-networking.md) · [English](../en/04-storage.md)
