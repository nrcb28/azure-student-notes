# Certificaciones: ocho rutas para estudiar

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

[Apuntes generales](../../es/README.md) · [Registro de fuentes](../../CERTIFICATION-SOURCES.md)

Aquí hay ocho rutas de examen. Cada una tiene una guía para entender decisiones, diez casos originales con respuestas y un cuaderno de cinco unidades con evidencias que entregar. No hace falta empezar por todas: elige según lo que quieras aprender.

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

## Por dónde empezar

Si empiezas desde cero, usa AZ-900 como mapa general. DP-900 ayuda a distinguir datos y cargas antes de entrar en DP-300. SC-900 trabaja identidad, seguridad y cumplimiento también en Microsoft 365. AZ-104 aporta base operativa para profundizar en AZ-700; AZ-305 y AZ-400 añaden diseño y entrega. Son sugerencias de estudio, no prerrequisitos oficiales.

## Qué se ha ampliado

DP-900, SC-900, AZ-700 y DP-300 tienen el mismo desarrollo, casos y entregables en los ocho idiomas. Las ediciones anteriores de otras rutas conservan notas complementarias de distinta longitud. Hay 80 escenarios por idioma, 640 variantes en total; no son preguntas reales de examen.

## Repasar con el entrenador

El entrenador permite escoger cualquiera de las ocho rutas y exportar sus casos a Anki. Es autoevaluación: compara tu explicación con la respuesta y valora el recuerdo. El mini simulacro de opción múltiple mantiene sus ocho preguntas sobre las cuatro rutas originales.

```bash
python tools/study.py demo --lang es --exam DP-900
python tools/study.py study --lang es --exam AZ-700 --limit 5
python tools/study.py export --lang es --exam SC-900 --output exports/es-sc900.tsv
```

## Referencias y alcance

Las referencias iniciales se consultaron el 27 de octubre de 2026 y las cuatro rutas nuevas el 30 de octubre de 2026. Consulta objetivos, disponibilidad, idioma y requisitos en Microsoft Learn antes de reservar. Los códigos de examen y las certificaciones no son lo mismo; las rutas Expert pueden requerir otras certificaciones. No se garantiza aprobar ni se afirma haber ejecutado prácticas en Azure.

[Entrenador](../../es/18-study-trainer.md) · [Mini simulacro](../../es/19-mini-quiz.md) · [Anki](../../flashcards/es.tsv) · [Laboratorio de redes](network-lab.md) · [ADR](ADR-template.md)
