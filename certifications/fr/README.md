# Certifications : seize parcours d’étude

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

[Notes générales](../../fr/README.md) · [Registre des sources](../../CERTIFICATION-SOURCES.md)

Seize parcours d’examen, chacun avec un guide pour comprendre les décisions, dix cas originaux avec réponses argumentées et un cahier de cinq unités avec éléments à rendre. Choisis d’abord le domaine que tu souhaites comprendre.

| Parcours | Thème | Guide | Cas | Cahier |
|---|---|---|---|---|
| AZ-900 | Fondamentaux Azure | [Lire](AZ-900.md) | [10 cas](AZ-900-cases.md) | [5 unités](AZ-900-workbook.md) |
| AZ-104 | Administration Azure | [Lire](AZ-104.md) | [10 cas](AZ-104-cases.md) | [5 unités](AZ-104-workbook.md) |
| AZ-305 | Architecture de solutions | [Lire](AZ-305.md) | [10 cas](AZ-305-cases.md) | [5 unités](AZ-305-workbook.md) |
| AZ-400 | Livraison et DevOps | [Lire](AZ-400.md) | [10 cas](AZ-400-cases.md) | [5 unités](AZ-400-workbook.md) |
| DP-900 | Fondamentaux des données | [Lire](DP-900.md) | [10 cas](DP-900-cases.md) | [5 unités](DP-900-workbook.md) |
| SC-900 | Sécurité, identité et conformité | [Lire](SC-900.md) | [10 cas](SC-900-cases.md) | [5 unités](SC-900-workbook.md) |
| AZ-700 | Réseaux Azure | [Lire](AZ-700.md) | [10 cas](AZ-700-cases.md) | [5 unités](AZ-700-workbook.md) |
| DP-300 | Administration Azure SQL | [Lire](DP-300.md) | [10 cas](DP-300-cases.md) | [5 unités](DP-300-workbook.md) |
| AI-901 | IA avec Microsoft Foundry | [Lire](AI-901.md) | [10 cas](AI-901-cases.md) | [5 unités](AI-901-workbook.md) |
| SC-200 | Opérations de sécurité | [Lire](SC-200.md) | [10 cas](SC-200-cases.md) | [5 unités](SC-200-workbook.md) |
| SC-300 | Identité et accès | [Lire](SC-300.md) | [10 cas](SC-300-cases.md) | [5 unités](SC-300-workbook.md) |
| AZ-140 | Azure Virtual Desktop | [Lire](AZ-140.md) | [10 cas](AZ-140-cases.md) | [5 unités](AZ-140-workbook.md) |
| AI-103 | Développement d’apps et d’agents IA | [Lire](AI-103.md) | [10 cas](AI-103-cases.md) | [5 unités](AI-103-workbook.md) |
| DP-700 | Ingénierie des données avec Fabric | [Lire](DP-700.md) | [10 cas](DP-700-cases.md) | [5 unités](DP-700-workbook.md) |
| SC-100 | Architecture de cybersécurité | [Lire](SC-100.md) | [10 cas](SC-100-cases.md) | [5 unités](SC-100-workbook.md) |
| AZ-120 | Charges SAP sur Azure | [Lire](AZ-120.md) | [10 cas](AZ-120-cases.md) | [5 unités](AZ-120-workbook.md) |

## Par où commencer

AZ-900 donne une vue générale. DP-900 explique les données et les charges avant DP-300. SC-900 aborde sécurité, identité et conformité aussi dans Microsoft 365. AZ-104 apporte les bases opérationnelles pour AZ-700 ; AZ-305 et AZ-400 ajoutent conception et livraison. Ce sont des conseils d’étude, pas des prérequis officiels.

## Ce qui a été ajouté

DP-900, SC-900, AZ-700 et DP-300 proposent des explications, cas et livrables équivalents dans les huit langues. Les anciennes notes complémentaires des autres parcours gardent des longueurs différentes. Il y a 160 scénarios par langue, soit 1280 variantes au total ; aucune question réelle d’examen.

## Réviser avec le trainer

Le trainer d’autoévaluation permet de sélectionner les seize parcours et d’exporter leurs cas vers Anki. Compare ton explication à la réponse et évalue ton rappel. Le mini quiz à choix multiple propose 32 scénarios originaux pour les seize parcours, deux par parcours, traduits en huit langues : 256 variantes.

```bash
python tools/study.py demo --lang fr --exam AI-103
python tools/study.py study --lang fr --exam DP-700 --limit 5
python tools/study.py export --lang fr --exam SC-100 --output exports/fr-sc100.tsv
```

## Références et limites

Les références de AZ-900, AZ-104, AZ-305 et AZ-400 ont été consultées le 27 octobre 2026 ; celles de DP-900, SC-900, AZ-700 et DP-300 le 30 octobre. Les huit parcours ajoutés ensuite ont été vérifiés le 1er novembre 2026. Ces dates de consultation sont distinctes des dates d’entrée en vigueur des objectifs. Revérifie objectifs, disponibilité, langue et conditions sur Microsoft Learn avant de réserver. Code d’examen et certification sont différents ; les certifications Expert peuvent exiger d’autres titres. Aucune garantie de réussite ni exécution dans Azure revendiquée.

[Trainer](../../fr/18-study-trainer.md) · [Mini quiz](../../fr/19-mini-quiz.md) · [Anki](../../flashcards/fr.tsv) · [Laboratoire réseau](network-lab.md) · [ADR](ADR-template.md)

## IA, opérations, identité et bureaux

AI-901, SC-200, SC-300 et AZ-140 ajoutent des guides, dix cas et cinq unités par parcours dans les huit langues. AI-901 comprend la mise en œuvre avec Microsoft Foundry ; SC-200 développe investigation et réponse ; SC-300 approfondit Entra ; AZ-140 porte sur les bureaux et applications virtuels. Sources consultées le 1er novembre 2026 pour ces quatre parcours.

## IA appliquée, données, architecture de sécurité et SAP

AI-103, DP-700, SC-100 et AZ-120 ajoutent des guides, dix cas et cinq unités par parcours dans les huit langues. Développement Foundry, ingénierie Fabric, capacités de sécurité et infrastructure SAP sont approfondis. Sources consultées le 1er novembre 2026 ; conditions des titres et dates de mise à jour des pages restent distinctes.
