# Certifications : huit parcours d’étude

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

[Notes générales](../../fr/README.md) · [Registre des sources](../../CERTIFICATION-SOURCES.md)

Huit parcours d’examen, chacun avec un guide pour comprendre les décisions, dix cas originaux avec réponses argumentées et un cahier de cinq unités avec éléments à rendre. Choisis d’abord le domaine que tu souhaites comprendre.

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

## Par où commencer

AZ-900 donne une vue générale. DP-900 explique les données et les charges avant DP-300. SC-900 aborde sécurité, identité et conformité aussi dans Microsoft 365. AZ-104 apporte les bases opérationnelles pour AZ-700 ; AZ-305 et AZ-400 ajoutent conception et livraison. Ce sont des conseils d’étude, pas des prérequis officiels.

## Ce qui a été ajouté

DP-900, SC-900, AZ-700 et DP-300 proposent des explications, cas et livrables équivalents dans les huit langues. Les anciennes notes complémentaires des autres parcours gardent des longueurs différentes. Il y a 80 scénarios par langue, soit 640 variantes au total ; aucune question réelle d’examen.

## Réviser avec le trainer

Le trainer d’autoévaluation permet de sélectionner les huit parcours et d’exporter leurs cas vers Anki. Compare ton explication à la réponse et évalue ton rappel. Le mini quiz à choix multiple conserve ses huit questions sur les quatre parcours initiaux.

```bash
python tools/study.py demo --lang fr --exam DP-900
python tools/study.py study --lang fr --exam AZ-700 --limit 5
python tools/study.py export --lang fr --exam SC-900 --output exports/fr-sc900.tsv
```

## Références et limites

Les références initiales ont été consultées le 27 octobre 2026 ; les quatre nouveaux parcours le 30 octobre 2026. Revérifie objectifs, disponibilité, langue et conditions sur Microsoft Learn avant de réserver. Code d’examen et certification sont différents ; les certifications Expert peuvent exiger d’autres titres. Aucune garantie de réussite ni exécution dans Azure revendiquée.

[Trainer](../../fr/18-study-trainer.md) · [Mini quiz](../../fr/19-mini-quiz.md) · [Anki](../../flashcards/fr.tsv) · [Laboratoire réseau](network-lab.md) · [ADR](ADR-template.md)
