# Zertifizierungen: sechzehn Lernwege

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

[Allgemeine Notizen](../../de/README.md) · [Quellenverzeichnis](../../CERTIFICATION-SOURCES.md)

Sechzehn Prüfungswege mit jeweils einem Leitfaden für begründete Entscheidungen, zehn eigenen Fällen mit Lösungen und einem Arbeitsbuch mit fünf Einheiten und überprüfbaren Ergebnissen. Wähle zuerst das Gebiet, das du verstehen möchtest.

| Prüfung | Schwerpunkt | Leitfaden | Fälle | Arbeitsbuch |
|---|---|---|---|---|
| AZ-900 | Azure-Grundlagen | [Lesen](AZ-900.md) | [10 Fälle](AZ-900-cases.md) | [5 Einheiten](AZ-900-workbook.md) |
| AZ-104 | Azure-Administration | [Lesen](AZ-104.md) | [10 Fälle](AZ-104-cases.md) | [5 Einheiten](AZ-104-workbook.md) |
| AZ-305 | Lösungsarchitektur | [Lesen](AZ-305.md) | [10 Fälle](AZ-305-cases.md) | [5 Einheiten](AZ-305-workbook.md) |
| AZ-400 | Bereitstellung und DevOps | [Lesen](AZ-400.md) | [10 Fälle](AZ-400-cases.md) | [5 Einheiten](AZ-400-workbook.md) |
| DP-900 | Datengrundlagen | [Lesen](DP-900.md) | [10 Fälle](DP-900-cases.md) | [5 Einheiten](DP-900-workbook.md) |
| SC-900 | Sicherheit, Identität und Compliance | [Lesen](SC-900.md) | [10 Fälle](SC-900-cases.md) | [5 Einheiten](SC-900-workbook.md) |
| AZ-700 | Azure-Netzwerke | [Lesen](AZ-700.md) | [10 Fälle](AZ-700-cases.md) | [5 Einheiten](AZ-700-workbook.md) |
| DP-300 | Azure-SQL-Administration | [Lesen](DP-300.md) | [10 Fälle](DP-300-cases.md) | [5 Einheiten](DP-300-workbook.md) |
| AI-901 | KI mit Microsoft Foundry | [Lesen](AI-901.md) | [10 Fälle](AI-901-cases.md) | [5 Einheiten](AI-901-workbook.md) |
| SC-200 | Sicherheitsbetrieb | [Lesen](SC-200.md) | [10 Fälle](SC-200-cases.md) | [5 Einheiten](SC-200-workbook.md) |
| SC-300 | Identität und Zugriff | [Lesen](SC-300.md) | [10 Fälle](SC-300-cases.md) | [5 Einheiten](SC-300-workbook.md) |
| AZ-140 | Azure Virtual Desktop | [Lesen](AZ-140.md) | [10 Fälle](AZ-140-cases.md) | [5 Einheiten](AZ-140-workbook.md) |
| AI-103 | Entwicklung von KI-Apps und Agenten | [Lesen](AI-103.md) | [10 Fälle](AI-103-cases.md) | [5 Einheiten](AI-103-workbook.md) |
| DP-700 | Data Engineering mit Fabric | [Lesen](DP-700.md) | [10 Fälle](DP-700-cases.md) | [5 Einheiten](DP-700-workbook.md) |
| SC-100 | Cybersicherheitsarchitektur | [Lesen](SC-100.md) | [10 Fälle](SC-100-cases.md) | [5 Einheiten](SC-100-workbook.md) |
| AZ-120 | SAP-Workloads in Azure | [Lesen](AZ-120.md) | [10 Fälle](AZ-120-cases.md) | [5 Einheiten](AZ-120-workbook.md) |

## Einstieg wählen

AZ-900 gibt einen allgemeinen Überblick. DP-900 erklärt Daten und Workloads vor DP-300. SC-900 behandelt Sicherheit, Identität und Compliance auch in Microsoft 365. AZ-104 liefert die Betriebsgrundlagen für AZ-700; AZ-305 und AZ-400 ergänzen Entwurf und Bereitstellung. Das sind Lernempfehlungen, keine offiziellen Voraussetzungen.

## Was neu hinzugekommen ist

DP-900, SC-900, AZ-700 und DP-300 enthalten in allen acht Sprachen entsprechende Erklärungen, Fälle und Abgaben. Ältere ergänzende Notizen anderer Wege bleiben unterschiedlich lang. Es gibt 160 Szenarien pro Sprache und 1280 Sprachvarianten insgesamt, keine echten Prüfungsfragen.

## Mit dem Trainer wiederholen

Der Trainer zur Selbsteinschätzung unterstützt alle sechzehn Wege und den Export nach Anki. Vergleiche deine Erklärung mit der Lösung und bewerte dein Erinnern. Das Multiple-Choice-Miniquiz behält seine acht Fragen zu den vier ursprünglichen Wegen.

```bash
python tools/study.py demo --lang de --exam AI-103
python tools/study.py study --lang de --exam DP-700 --limit 5
python tools/study.py export --lang de --exam SC-100 --output exports/de-sc100.tsv
```

## Quellen und Grenzen

Die ursprünglichen Quellen wurden am 27. Oktober 2026 geprüft, die vier neuen Wege am 30. Oktober 2026. Prüfe Ziele, Verfügbarkeit, Prüfungssprachen und Voraussetzungen vor der Buchung auf Microsoft Learn. Prüfungscode und Zertifizierung sind verschieden; Expert-Zertifizierungen können weitere Nachweise verlangen. Keine Bestehensgarantie oder behauptete Ausführung in Azure.

[Trainer](../../de/18-study-trainer.md) · [Miniquiz](../../de/19-mini-quiz.md) · [Anki](../../flashcards/de.tsv) · [Netzwerklabor](network-lab.md) · [ADR](ADR-template.md)

## KI, Sicherheitsbetrieb, Identität und Desktops

AI-901, SC-200, SC-300 und AZ-140 ergänzen Leitfäden, zehn Fälle und fünf Einheiten je Lernweg in allen acht Sprachen. AI-901 enthält die Umsetzung mit Microsoft Foundry, SC-200 Untersuchung und Reaktion, SC-300 vertieft Entra und AZ-140 behandelt virtuelle Desktops und Apps. Die Quellen dieser vier Wege wurden am 1. November 2026 geprüft.

## Angewandte KI, Data Engineering, Sicherheitsarchitektur und SAP

AI-103, DP-700, SC-100 und AZ-120 ergänzen Leitfäden, zehn Fälle und fünf Einheiten je Weg in allen acht Sprachen. Themen sind Foundry-Entwicklung, Fabric-Datenverarbeitung, Sicherheitsfähigkeiten und SAP-Infrastruktur. Quellenprüfung am 1. November 2026; Zertifikatsvoraussetzungen und Seitenaktualisierungen sind getrennte Angaben.
