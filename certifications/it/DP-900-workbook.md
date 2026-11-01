# DP-900 · Quaderno avanzato comune

[Guida](DP-900.md) · [Dieci casi](DP-900-cases.md) · [Indice](README.md)

Cinque unità corrispondenti nelle otto lingue. Usa dati sintetici e separa previsioni e osservazioni. Questi esercizi non distribuiscono risorse Azure e non dimostrano la copertura dell'intero esame.

<a id="dp-900-unit-1"></a>

## 1. Descrivi i dati prima di scegliere l'archivio

Censisci un PDF, una riga di iscrizione, un documento JSON con metadati facoltativi e un evento di download. Per ciascuno descrivi struttura, identificatore, produttore, consumatore, conservazione e campi sensibili. Scrivi poi l'operazione importante: recuperare un file, registrare un'iscrizione o aggregare eventi. Distingui una scelta di formato dal requisito del carico.

**Scenario:** qualcuno propone un solo database perché i quattro insiemi appartengono alla stessa app. **Evidenze:** matrice decisionale di quattro righe, un'alternativa scartata per riga e una condizione nuova che cambierebbe la scelta. Non inventare limiti dei servizi e non assumere che ogni documento JSON richieda Cosmos DB.

<a id="dp-900-unit-2"></a>

## 2. Rendi visibile l'integrità relazionale

Disegna Studenti, Corsi e Iscrizioni con identificatori stabili. Crea sei righe sintetiche e spiega chiavi primarie, riferimenti e una regola che impedisca doppie iscrizioni. Prevedi il risultato di un join. Poi modifica il titolo di un corso e confronta gli aggiornamenti con un progetto che lo copia in ogni iscrizione. L'obiettivo è mostrare un'anomalia concreta, non recitare uno slogan sulla normalizzazione.

**Scenario:** uno studente risulta iscritto a un corso inesistente. **Evidenze:** regola che dovrebbe respingerlo o rilevarlo, record non valido di esempio ed esito previsto. Se esegui SQL localmente, indica il motore: il comportamento di SQLite non è una prova di Azure SQL.

<a id="dp-900-unit-3"></a>

## 3. Scegli chi gestisce il database

Confronta Azure SQL Database, Managed Instance e SQL Server su VM per una nuova app e una migrazione. Elenca dipendenze di compatibilità, esigenze di rete e identità, manutenzione e aspettative di recupero. Aggiungi un motore open source quando richiesto dall'app esistente. Separa una raccomandazione giustificata dall'affermazione che un prodotto sia sempre il migliore.

**Scenario:** l'inventario della migrazione comprende un componente che richiede accesso al sistema operativo ospite. **Evidenze:** domande di compatibilità, tabella delle responsabilità operative e piano di prova con criteri di successo. Non occorre distribuire: indica quali ipotesi devono ancora essere verificate prima di accettare la destinazione.

<a id="dp-900-unit-4"></a>

## 4. Riconcilia una piccola pipeline

Prepara sei eventi sintetici di download: includi un identificatore duplicato e un record senza corso. Definisci input valido, evento unico e condizione di completamento. Disegna un percorso ETL e uno ELT, collocando validazione e archivio dei record rifiutati. Spiega quando il batch rispetta il ritardo richiesto e quando sarebbe giustificato lo streaming.

**Scenario:** il totale del pannello differisce dal numero di righe sorgente. **Evidenze:** conteggi sorgente, duplicati, rifiutati e accettati con una spiegazione riproducibile. Assegna proprietario e risposta a un'esecuzione fallita. Lo stato riuscito della pipeline non dimostra la correttezza dei totali di business.

<a id="dp-900-unit-5"></a>

## 5. Definisci una misura analitica affidabile

Scegli una granularità, per esempio un evento di download completato, e definisci un fatto con contesto di corso e data. Specifica fuso orario, gestione degli eventi tardivi e freschezza. Spiega quale parte conserva i dati, quale li trasforma, quale offre il modello semantico e quale mostra il rapporto. Confronta lake, warehouse e lakehouse secondo il lavoro richiesto, non secondo l'etichetta del prodotto.

**Consegna finale:** matrice degli archivi, schema relazionale, riconciliazione della pipeline e rapporto mensile simulato con definizione della misura. Spiega i ruoli pertinenti di Fabric, Synapse e Power BI. Individua una domanda ancora aperta per la guida ufficiale: un buon rapporto simulato non dimostra capacità operative cloud o preparazione all'esame.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900) · [Appunti sui dati](../../it/04-storage.md)
