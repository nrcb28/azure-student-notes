# Certificaciones: diecisiete rutas para estudiar

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

[Apuntes generales](../../es/README.md) · [Registro de fuentes](../../CERTIFICATION-SOURCES.md)

Aquí hay diecisiete rutas de examen. Cada una tiene una guía para entender decisiones, diez casos originales con respuestas y un cuaderno de cinco unidades con evidencias que entregar. No hace falta empezar por todas: elige según lo que quieras aprender.

| Ruta | Enfoque | Guía | Casos | Cuaderno |
|---|---|---|---|---|
| AZ-900 | Fundamentos de Azure | [Leer](AZ-900.md) | [10 casos](AZ-900-cases.md) | [5 unidades](AZ-900-workbook.md) |
| AZ-104 | Administración de Azure | [Leer](AZ-104.md) | [10 casos](AZ-104-cases.md) | [5 unidades](AZ-104-workbook.md) |
| AZ-305 | Arquitectura de soluciones | [Leer](AZ-305.md) | [10 casos](AZ-305-cases.md) | [5 unidades](AZ-305-workbook.md) |
| AZ-400 | Entrega y DevOps | [Leer](AZ-400.md) | [10 casos](AZ-400-cases.md) | [5 unidades](AZ-400-workbook.md) |
| DP-900 | Fundamentos de datos | [Leer](DP-900.md) | [10 casos](DP-900-cases.md) | [5 unidades](DP-900-workbook.md) |
| SC-900 | Seguridad, identidad y cumplimiento | [Leer](SC-900.md) | [10 casos](SC-900-cases.md) | [5 unidades](SC-900-workbook.md) |
| AZ-700 | Redes de Azure | [Leer](AZ-700.md) | [10 casos](AZ-700-cases.md) | [5 unidades](AZ-700-workbook.md) |
| DP-300 | Administración de Azure SQL | [Leer](DP-300.md) | [10 casos](DP-300-cases.md) | [5 unidades](DP-300-workbook.md) |
| AI-901 | IA con Microsoft Foundry | [Leer](AI-901.md) | [10 casos](AI-901-cases.md) | [5 unidades](AI-901-workbook.md) |
| SC-200 | Operaciones de seguridad | [Leer](SC-200.md) | [10 casos](SC-200-cases.md) | [5 unidades](SC-200-workbook.md) |
| SC-300 | Identidad y acceso | [Leer](SC-300.md) | [10 casos](SC-300-cases.md) | [5 unidades](SC-300-workbook.md) |
| AZ-140 | Azure Virtual Desktop | [Leer](AZ-140.md) | [10 casos](AZ-140-cases.md) | [5 unidades](AZ-140-workbook.md) |
| AI-103 | Desarrollo de aplicaciones y agentes de IA | [Leer](AI-103.md) | [10 casos](AI-103-cases.md) | [5 unidades](AI-103-workbook.md) |
| DP-700 | Ingeniería de datos con Fabric | [Leer](DP-700.md) | [10 casos](DP-700-cases.md) | [5 unidades](DP-700-workbook.md) |
| SC-100 | Arquitectura de ciberseguridad | [Leer](SC-100.md) | [10 casos](SC-100-cases.md) | [5 unidades](SC-100-workbook.md) |
| AZ-120 | Cargas SAP en Azure | [Leer](AZ-120.md) | [10 casos](AZ-120-cases.md) | [5 unidades](AZ-120-workbook.md) |
| AZ-802 | Administración de Windows Server | [Leer](AZ-802.md) | [10 casos](AZ-802-cases.md) | [5 unidades](AZ-802-workbook.md) |

## Por dónde empezar

Si empiezas desde cero, usa AZ-900 como mapa general. DP-900 ayuda a distinguir datos y cargas antes de entrar en DP-300. SC-900 trabaja identidad, seguridad y cumplimiento también en Microsoft 365. AZ-104 aporta base operativa para profundizar en AZ-700; AZ-305 y AZ-400 añaden diseño y entrega. Son sugerencias de estudio, no prerrequisitos oficiales.

## Qué se ha ampliado

DP-900, SC-900, AZ-700 y DP-300 tienen el mismo desarrollo, casos y entregables en los ocho idiomas. Las ediciones anteriores de otras rutas conservan notas complementarias de distinta longitud. Hay 170 escenarios por idioma, 1360 variantes en total; no son preguntas reales de examen.

## Repasar con el entrenador

El entrenador permite escoger cualquiera de las diecisiete rutas y exportar sus casos a Anki. Es autoevaluación: compara tu explicación con la respuesta y valora el recuerdo. El mini simulacro de opción múltiple incluye 34 escenarios originales para las diecisiete rutas, dos por ruta, traducidos a ocho idiomas: 272 variantes.

```bash
python tools/study.py demo --lang es --exam AZ-802
python tools/study.py study --lang es --exam DP-700 --limit 5
python tools/study.py export --lang es --exam SC-100 --output exports/es-sc100.tsv
```

## Referencias y alcance

Las referencias de AZ-900, AZ-104, AZ-305 y AZ-400 se consultaron el 27 de octubre de 2026; las de DP-900, SC-900, AZ-700 y DP-300, el 30 de octubre. Las ocho rutas añadidas después se consultaron el 1 de noviembre de 2026. Estas son fechas de consulta, no fechas de entrada en vigor de los objetivos. Consulta objetivos, disponibilidad, idioma y requisitos en Microsoft Learn antes de reservar. Los códigos de examen y las certificaciones no son lo mismo; las rutas Expert pueden requerir otras certificaciones. No se garantiza aprobar ni se afirma haber ejecutado prácticas en Azure.

[Entrenador](../../es/18-study-trainer.md) · [Mini simulacro](../../es/19-mini-quiz.md) · [Anki](../../flashcards/es.tsv) · [Laboratorio de redes](network-lab.md) · [ADR](ADR-template.md)

## IA, operaciones, identidad y escritorios

AI-901, SC-200, SC-300 y AZ-140 amplían la colección con guías, diez casos y cinco unidades por ruta en los ocho idiomas. AI-901 incluye implementación con Microsoft Foundry; SC-200 trabaja investigación y respuesta; SC-300 profundiza en Entra; AZ-140 estudia escritorios y aplicaciones virtuales. Las referencias de estas cuatro rutas se consultaron el 1 de noviembre de 2026.

## IA aplicada, datos, arquitectura de seguridad y SAP

AI-103, DP-700, SC-100 y AZ-120 añaden guías, diez casos y cinco unidades por ruta en los ocho idiomas. AI-103 profundiza en desarrollo con Foundry; DP-700 trata ingeniería de datos en Fabric; SC-100 diseña capacidades de seguridad; AZ-120 planifica infraestructura y operación SAP. Referencias consultadas el 1 de noviembre de 2026. Los requisitos de una credencial y la fecha de actualización de una página se comprueban por separado.

## Windows Server local e híbrido

AZ-802 trabaja la administración de Windows Server en entornos locales e híbridos mediante siete áreas: AD DS, gestión híbrida, máquinas virtuales, redes, almacenamiento y archivos, seguridad, y supervisión y resolución de problemas. La [guía](AZ-802.md), los [diez casos](AZ-802-cases.md) y el [cuaderno de cinco unidades](AZ-802-workbook.md) conectan identidad, permisos, recuperación y evidencias de un laboratorio aislado. Las fuentes oficiales se consultaron el **2026-11-03**; la [guía del examen](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802) tiene el encabezado «Skills measured» sin fecha y metadatos de actualización del **2026-10-19**, que no indican cuándo entran en vigor los objetivos.
