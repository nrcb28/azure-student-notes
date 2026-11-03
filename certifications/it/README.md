# Certificazioni: sedici percorsi di studio

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

[Appunti generali](../../it/README.md) · [Registro delle fonti](../../CERTIFICATION-SOURCES.md)

Sedici percorsi d’esame, ciascuno con una guida per capire le decisioni, dieci casi originali con risposte ragionate e un quaderno di cinque unità con prove da consegnare. Scegli prima l’area che vuoi approfondire.

| Percorso | Tema | Guida | Casi | Quaderno |
|---|---|---|---|---|
| AZ-900 | Fondamenti di Azure | [Leggi](AZ-900.md) | [10 casi](AZ-900-cases.md) | [5 unità](AZ-900-workbook.md) |
| AZ-104 | Amministrazione di Azure | [Leggi](AZ-104.md) | [10 casi](AZ-104-cases.md) | [5 unità](AZ-104-workbook.md) |
| AZ-305 | Architettura delle soluzioni | [Leggi](AZ-305.md) | [10 casi](AZ-305-cases.md) | [5 unità](AZ-305-workbook.md) |
| AZ-400 | Rilascio e DevOps | [Leggi](AZ-400.md) | [10 casi](AZ-400-cases.md) | [5 unità](AZ-400-workbook.md) |
| DP-900 | Fondamenti dei dati | [Leggi](DP-900.md) | [10 casi](DP-900-cases.md) | [5 unità](DP-900-workbook.md) |
| SC-900 | Sicurezza, identità e conformità | [Leggi](SC-900.md) | [10 casi](SC-900-cases.md) | [5 unità](SC-900-workbook.md) |
| AZ-700 | Reti Azure | [Leggi](AZ-700.md) | [10 casi](AZ-700-cases.md) | [5 unità](AZ-700-workbook.md) |
| DP-300 | Amministrazione di Azure SQL | [Leggi](DP-300.md) | [10 casi](DP-300-cases.md) | [5 unità](DP-300-workbook.md) |
| AI-901 | IA con Microsoft Foundry | [Leggi](AI-901.md) | [10 casi](AI-901-cases.md) | [5 unità](AI-901-workbook.md) |
| SC-200 | Operazioni di sicurezza | [Leggi](SC-200.md) | [10 casi](SC-200-cases.md) | [5 unità](SC-200-workbook.md) |
| SC-300 | Identità e accesso | [Leggi](SC-300.md) | [10 casi](SC-300-cases.md) | [5 unità](SC-300-workbook.md) |
| AZ-140 | Azure Virtual Desktop | [Leggi](AZ-140.md) | [10 casi](AZ-140-cases.md) | [5 unità](AZ-140-workbook.md) |
| AI-103 | Sviluppo di app e agenti IA | [Leggi](AI-103.md) | [10 casi](AI-103-cases.md) | [5 unità](AI-103-workbook.md) |
| DP-700 | Ingegneria dei dati con Fabric | [Leggi](DP-700.md) | [10 casi](DP-700-cases.md) | [5 unità](DP-700-workbook.md) |
| SC-100 | Architettura della cybersicurezza | [Leggi](SC-100.md) | [10 casi](SC-100-cases.md) | [5 unità](SC-100-workbook.md) |
| AZ-120 | Carichi SAP in Azure | [Leggi](AZ-120.md) | [10 casi](AZ-120-cases.md) | [5 unità](AZ-120-workbook.md) |

## Da dove iniziare

AZ-900 offre una mappa generale. DP-900 chiarisce dati e carichi prima di DP-300. SC-900 tratta sicurezza, identità e conformità anche in Microsoft 365. AZ-104 prepara le basi operative per AZ-700; AZ-305 e AZ-400 aggiungono progettazione e rilascio. Sono consigli di studio, non prerequisiti ufficiali.

## Cosa è stato ampliato

DP-900, SC-900, AZ-700 e DP-300 hanno spiegazioni, casi e consegne equivalenti nelle otto lingue. Le note supplementari precedenti degli altri percorsi mantengono lunghezze diverse. Ci sono 160 scenari per lingua, 1280 varianti in totale; non sono domande reali d’esame.

## Ripasso con il trainer

Il trainer di autovalutazione consente di scegliere tutti i sedici percorsi e di esportare i casi in Anki. Confronta la tua spiegazione con la risposta e valuta il ricordo. Il mini quiz a scelta multipla comprende 32 scenari originali per tutti i sedici percorsi, due per percorso, tradotti in otto lingue: 256 varianti.

```bash
python tools/study.py demo --lang it --exam AI-103
python tools/study.py study --lang it --exam DP-700 --limit 5
python tools/study.py export --lang it --exam SC-100 --output exports/it-sc100.tsv
```

## Fonti e limiti

Le fonti di AZ-900, AZ-104, AZ-305 e AZ-400 sono state consultate il 27 ottobre 2026; quelle di DP-900, SC-900, AZ-700 e DP-300 il 30 ottobre. Gli otto percorsi aggiunti dopo sono stati verificati il 1º novembre 2026. Sono date di consultazione, distinte dalle date di validità degli obiettivi. Controlla obiettivi, disponibilità, lingua e requisiti su Microsoft Learn prima di prenotare. Esame e certificazione sono concetti diversi; i percorsi Expert possono richiedere altre credenziali. Nessuna garanzia di superamento né esecuzione in Azure dichiarata.

[Trainer](../../it/18-study-trainer.md) · [Mini quiz](../../it/19-mini-quiz.md) · [Anki](../../flashcards/it.tsv) · [Laboratorio di rete](network-lab.md) · [ADR](ADR-template.md)

## IA, operazioni, identità e desktop

AI-901, SC-200, SC-300 e AZ-140 aggiungono guide, dieci casi e cinque unità per percorso nelle otto lingue. AI-901 comprende l’implementazione con Microsoft Foundry; SC-200 tratta indagine e risposta; SC-300 approfondisce Entra; AZ-140 riguarda desktop e app virtuali. Le fonti di questi quattro percorsi sono state consultate il 1º novembre 2026.

## IA applicata, dati, architettura di sicurezza e SAP

AI-103, DP-700, SC-100 e AZ-120 aggiungono guide, dieci casi e cinque unità per percorso nelle otto lingue. Si approfondiscono sviluppo con Foundry, ingegneria con Fabric, capacità di sicurezza e infrastruttura SAP. Fonti consultate il 1º novembre 2026; requisiti delle credenziali e date di aggiornamento delle pagine sono distinti.
