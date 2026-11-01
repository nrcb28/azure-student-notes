# Certifications: sixteen study routes

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

[General notes](../../en/README.md) · [Source register](../../CERTIFICATION-SOURCES.md)

Sixteen exam routes, each with a guide that explains decisions, ten original cases with reasoned answers, and a five-unit evidence workbook. Pick the area you want to understand before trying to study everything.

| Route | Focus | Guide | Cases | Workbook |
|---|---|---|---|---|
| AZ-900 | Azure fundamentals | [Read](AZ-900.md) | [10 cases](AZ-900-cases.md) | [5 units](AZ-900-workbook.md) |
| AZ-104 | Azure administration | [Read](AZ-104.md) | [10 cases](AZ-104-cases.md) | [5 units](AZ-104-workbook.md) |
| AZ-305 | Solution architecture | [Read](AZ-305.md) | [10 cases](AZ-305-cases.md) | [5 units](AZ-305-workbook.md) |
| AZ-400 | Delivery and DevOps | [Read](AZ-400.md) | [10 cases](AZ-400-cases.md) | [5 units](AZ-400-workbook.md) |
| DP-900 | Data fundamentals | [Read](DP-900.md) | [10 cases](DP-900-cases.md) | [5 units](DP-900-workbook.md) |
| SC-900 | Security, identity, and compliance | [Read](SC-900.md) | [10 cases](SC-900-cases.md) | [5 units](SC-900-workbook.md) |
| AZ-700 | Azure networking | [Read](AZ-700.md) | [10 cases](AZ-700-cases.md) | [5 units](AZ-700-workbook.md) |
| DP-300 | Azure SQL administration | [Read](DP-300.md) | [10 cases](DP-300-cases.md) | [5 units](DP-300-workbook.md) |
| AI-901 | AI with Microsoft Foundry | [Read](AI-901.md) | [10 cases](AI-901-cases.md) | [5 units](AI-901-workbook.md) |
| SC-200 | Security operations | [Read](SC-200.md) | [10 cases](SC-200-cases.md) | [5 units](SC-200-workbook.md) |
| SC-300 | Identity and access | [Read](SC-300.md) | [10 cases](SC-300-cases.md) | [5 units](SC-300-workbook.md) |
| AZ-140 | Azure Virtual Desktop | [Read](AZ-140.md) | [10 cases](AZ-140-cases.md) | [5 units](AZ-140-workbook.md) |
| AI-103 | AI app and agent development | [Read](AI-103.md) | [10 cases](AI-103-cases.md) | [5 units](AI-103-workbook.md) |
| DP-700 | Fabric data engineering | [Read](DP-700.md) | [10 cases](DP-700-cases.md) | [5 units](DP-700-workbook.md) |
| SC-100 | Cybersecurity architecture | [Read](SC-100.md) | [10 cases](SC-100-cases.md) | [5 units](SC-100-workbook.md) |
| AZ-120 | SAP workloads on Azure | [Read](AZ-120.md) | [10 cases](AZ-120-cases.md) | [5 units](AZ-120-workbook.md) |

## Where to start

Use AZ-900 as a general map when starting. DP-900 introduces data and workloads before DP-300. SC-900 covers security, identity, and compliance across Azure and Microsoft 365. AZ-104 gives an operational base for AZ-700; AZ-305 and AZ-400 add design and delivery. These are learning suggestions, not formal prerequisites.

## What has expanded

DP-900, SC-900, AZ-700, and DP-300 have matching explanations, cases, and deliverables in all eight languages. Older supplementary notes in other routes retain different lengths. There are 160 scenarios per language, 1280 variants overall; these are not real exam questions.

## Practise with the trainer

Choose any of the sixteen routes in the self-rating trainer or export cases to Anki. Compare your explanation with the answer and rate recall. The multiple-choice mini quiz retains its eight questions on the original four routes.

```bash
python tools/study.py demo --lang en --exam AI-103
python tools/study.py study --lang en --exam DP-700 --limit 5
python tools/study.py export --lang en --exam SC-100 --output exports/en-sc100.tsv
```

## References and scope

Initial references were checked on 27 October 2026; the four new routes on 30 October 2026. Recheck objectives, availability, exam languages, and requirements on Microsoft Learn before booking. Exam codes and certifications are different; Expert routes can require other credentials. No pass guarantee or Azure execution is claimed.

[Trainer](../../en/18-study-trainer.md) · [Mini quiz](../../en/19-mini-quiz.md) · [Anki](../../flashcards/en.tsv) · [Networking lab](network-lab.md) · [ADR](ADR-template.md)

## AI, operations, identity, and desktops

AI-901, SC-200, SC-300, and AZ-140 add guides, ten cases, and five units per route in all eight languages. AI-901 includes Microsoft Foundry implementation; SC-200 develops investigation and response; SC-300 focuses on Entra; AZ-140 covers virtual desktops and apps. References for these four routes were checked on 1 November 2026.

## Applied AI, data engineering, security architecture, and SAP

AI-103, DP-700, SC-100, and AZ-120 add guides, ten cases, and five units per route in all eight languages. Study Foundry development, Fabric engineering, security capabilities, and SAP infrastructure operations. References checked on 1 November 2026. Credential requirements and page-update metadata are checked separately.
