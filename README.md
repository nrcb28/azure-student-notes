# Azure sin tanto lío · Azure without the confusion

[Español](es/README.md) · [English](en/README.md) · [Italiano](it/README.md) · [Deutsch](de/README.md) · [Français](fr/README.md) · [Русский](ru/README.md) · [日本語](ja/README.md) · [简体中文](zh/README.md)

Apuntes de Azure para estudiantes de informática. Explicaciones cortas, decisiones razonadas y prácticas pequeñas para entender lo que estamos desplegando.

Azure study notes for computer science students. Short explanations, practical decisions, and small labs to understand what we deploy.

**[Leer en español](es/README.md) · [Read in English](en/README.md)**

**Certificaciones / Certifications: [Español](certifications/es/README.md) · [English](certifications/en/README.md)**

## Practica de verdad / Practise actively

**[Entrenador en español](es/18-study-trainer.md) · [English trainer](en/18-study-trainer.md) · [Anki en ocho idiomas](flashcards/README.md)**

Un entrenador local convierte 120 casos por idioma —960 variantes entre los ocho idiomas— en sesiones de repaso. Guarda valoraciones, prioriza repasos pendientes, recupera dificultades, propone un plan y exporta a Anki. Funciona sin Azure, cuenta ni paquetes externos. Es autoevaluación, no corrección automática ni predicción de aprobar.

An offline trainer turns 120 cases per language, 960 language variants overall, into review sessions. It saves ratings, prioritises due reviews, revisits difficulties, suggests a plan, and exports to Anki. No Azure account or external packages. Self-assessment, not automatic grading or a pass prediction.

```bash
python tools/study.py demo --lang es --exam AZ-104
python tools/study.py study --lang es --exam AZ-104 --limit 5
python tools/study.py stats --lang es
```

[Manual completo / Full manual](TRAINER.md). El progreso personal no se sube a Git / Personal progress is excluded from Git.

## Mini simulacro con corrección / Mini quiz with marking

**[Practicar en español](es/19-mini-quiz.md) · [Read in English](en/19-mini-quiz.md) · [Preguntas en GitHub](es/20-quiz-cases.md)**

Ocho escenarios originales para las cuatro rutas iniciales, dos por ruta, en los ocho idiomas. Elige una respuesta y revisa su explicación, el motivo del error, una fuente de Microsoft Learn y el capítulo relacionado. Incluye modos practice y exam, tiempo opcional, informes JSON locales y repaso de errores. Es un banco pequeño para practicar decisiones.

Eight original scenarios for the four initial certification routes, two per route, translated into all eight languages. Practise with immediate explanations or defer marking until the end, save a local report, and revisit mistakes by topic. This small bank does not cover a complete exam or predict passing.

```bash
python tools/quiz.py demo --lang es
python tools/quiz.py run --lang es --mode exam --count 8 --minutes 12
```

[Manual / Manual](QUIZ.md) · [Fuentes de cada caso / Scenario sources](QUIZ-SOURCES.md). El temporizador se comprueba al recibir la entrada; pulsa Intro al vencer el plazo. / Time is checked after terminal input; press Enter when it expires.

## Ruta común ampliada / Expanded common route

- [Doce unidades básicas en ocho idiomas / Twelve foundation units](STUDY-PARITY.md).
- [60 unidades avanzadas por idioma / 60 advanced units per language](certifications/es/README.md).
- [Tres laboratorios nuevos / Three new labs](es/17-advanced-labs.md): recuperación de blobs, inspección de roles y simulación local de reintentos.

Cada unidad avanzada incluye explicación, escenario y evidencia solicitada. Las notas anteriores se conservan; el núcleo nuevo tiene los mismos objetivos y entregables en los ocho idiomas. No se afirma traducción literal completa de cada párrafo anterior.

Each advanced unit includes explanation, scenario, and requested evidence. Earlier notes remain available; the new core has matching objectives and deliverables in all eight languages. This does not claim complete verbatim translation of every earlier paragraph.

## Microsoft Learn: nueva ampliación / New expansion

Doce temas con explicaciones reescritas, fuentes directas y casos propios, disponibles en los ocho idiomas e integrados también en los capítulos y certificaciones.

Twelve topics with rewritten explanations, direct sources, and original cases, available in all eight languages and integrated into chapters and exam routes.

[Fuentes verificadas / Source register](LEARN-SOURCES.md) · [Español](es/15-microsoft-learn.md) · [日本語](ja/15-microsoft-learn.md) · [简体中文](zh/15-microsoft-learn.md)

Nuevos temas: recuperación de blobs, reintentos e idempotencia, diagnóstico RBAC y recuperación de Key Vault. Cada uno incluye un caso y pasos de revisión en los ocho idiomas.

New topics: blob recovery, retries and idempotency, RBAC diagnosis, and Key Vault recovery. Each includes a case and review steps in all eight languages.

## Idiomas / Languages

| Idioma / Language | Apuntes / Notes | Certificaciones / Certifications |
|---|---|---|
| Español | [Español](es/README.md) | [12 rutas / 12 routes](certifications/es/README.md) |
| English | [English](en/README.md) | [12 rutas / 12 routes](certifications/en/README.md) |
| Italiano | [Italiano](it/README.md) | [12 rutas / 12 routes](certifications/it/README.md) |
| Deutsch | [Deutsch](de/README.md) | [12 rutas / 12 routes](certifications/de/README.md) |
| Français | [Français](fr/README.md) | [12 rutas / 12 routes](certifications/fr/README.md) |
| Русский | [Русский](ru/README.md) | [12 rutas / 12 routes](certifications/ru/README.md) |
| 日本語 | [日本語](ja/README.md) | [12 rutas / 12 routes](certifications/ja/README.md) |
| 简体中文 | [简体中文](zh/README.md) | [12 rutas / 12 routes](certifications/zh/README.md) |

Las versiones italiana, alemana, francesa, rusa, japonesa y china son adaptaciones de estudio más compactas: incluyen los doce temas, prácticas, repaso y las cuatro rutas iniciales. Las guías añadidas de datos, seguridad, redes, SQL, IA y escritorios desarrollan los mismos temas, casos y entregables en los ocho idiomas. [Detalles de las ediciones](LOCALIZATION.md).

The Italian, German, French, Russian, Japanese, and Chinese editions are more compact study adaptations covering all twelve topics, labs, review, and the four initial certification routes. The added data, security, networking, SQL, AI, and desktop guides have matching topics, cases, and deliverables in all eight languages. [Edition details](LOCALIZATION.md).

[Glosario en ocho idiomas / Eight-language glossary](GLOSSARY-multilingual.md).

## Más rutas: IA, seguridad y escritorios / More routes

Añadidas **AI-901, SC-200, SC-300 y AZ-140** en los ocho idiomas. Cada una incluye guía, diez casos propios con respuestas razonadas y cinco unidades con entregables. AI-901 trabaja Microsoft Foundry; SC-200 desarrolla análisis de incidentes; SC-300 profundiza en Entra; AZ-140 cubre escritorios y aplicaciones virtuales.

Added **AI-901, SC-200, SC-300, and AZ-140** in all eight languages, each with a guide, ten original reasoned cases, and five workbook units. Practise Foundry AI concepts and implementation, security operations, Entra identity administration, and virtual desktops. Cases are included in the self-rating trainer and Anki.

```bash
python tools/study.py demo --lang es --exam AI-901
python tools/study.py study --lang es --exam SC-200 --limit 5
```

[Índice de las doce rutas / Twelve-route index](certifications/es/README.md) · [Versiones y fuentes / Sources and versions](CERTIFICATION-SOURCES.md)

## Nuevas rutas: datos, seguridad, redes y SQL / New routes

Añadidas **DP-900, SC-900, AZ-700 y DP-300**. Cada ruta incluye una guía desarrollada, diez casos con respuestas razonadas y cinco unidades prácticas. Se puede estudiar en español, inglés, italiano, alemán, francés, ruso, japonés y chino simplificado. El entrenador y los mazos Anki incorporan los nuevos casos.

Added **DP-900, SC-900, AZ-700, and DP-300**. Every route has a detailed guide, ten cases with reasoned answers, and five workbook units in all eight languages. New cases are available in the trainer and Anki decks.

```bash
python tools/study.py demo --lang es --exam DP-900
python tools/study.py study --lang es --exam AZ-700 --limit 5
```

[Elegir ruta / Choose a route](certifications/es/README.md) · [Referencias oficiales / Official references](CERTIFICATION-SOURCES.md)

## Certificaciones con más detalle / Detailed certification guides

| Examen / Exam | Español | English |
|---|---|---|
| AZ-900 · Fundamentals | [Guía](certifications/es/AZ-900.md) | [Guide](certifications/en/AZ-900.md) |
| AZ-104 · Administrator | [Guía](certifications/es/AZ-104.md) | [Guide](certifications/en/AZ-104.md) |
| AZ-305 · Infrastructure Solutions | [Guía](certifications/es/AZ-305.md) | [Guide](certifications/en/AZ-305.md) |
| AZ-400 · DevOps Solutions | [Guía](certifications/es/AZ-400.md) | [Guide](certifications/en/AZ-400.md) |
| DP-900 · Data Fundamentals | [Guía](certifications/es/DP-900.md) | [Guide](certifications/en/DP-900.md) |
| SC-900 · Security, Compliance, Identity | [Guía](certifications/es/SC-900.md) | [Guide](certifications/en/SC-900.md) |
| AZ-700 · Networking Solutions | [Guía](certifications/es/AZ-700.md) | [Guide](certifications/en/AZ-700.md) |
| DP-300 · Azure SQL Administration | [Guía](certifications/es/DP-300.md) | [Guide](certifications/en/DP-300.md) |
| AI-901 · Azure AI Fundamentals | [Guía](certifications/es/AI-901.md) | [Guide](certifications/en/AI-901.md) |
| SC-200 · Security Operations | [Guía](certifications/es/SC-200.md) | [Guide](certifications/en/SC-200.md) |
| SC-300 · Identity and Access | [Guía](certifications/es/SC-300.md) | [Guide](certifications/en/SC-300.md) |
| AZ-140 · Azure Virtual Desktop | [Guía](certifications/es/AZ-140.md) | [Guide](certifications/en/AZ-140.md) |

Cada guía desarrolla conceptos, decisiones, diagnóstico, práctica y repaso. Hay 10 casos de certificación por examen y por idioma: 960 variantes en los ocho idiomas, a partir de 120 escenarios originales. Las referencias se registran por versión: 27 y 30 de octubre, y 1 de noviembre de 2026; consulta las páginas oficiales antes de reservar un examen.

Each guide develops concepts, decisions, troubleshooting, practice, and review. There are ten certification cases per exam and language: 960 language variants from 120 original scenarios. References are versioned by review date: 27 and 30 October, and 1 November 2026; consult official pages before booking an exam.

## Qué hay aquí / What's inside

- 12 capítulos en cada idioma: fundamentos, recursos, cómputo, almacenamiento, redes, identidad, gobierno, observabilidad, costes, arquitectura, mensajería y DevOps.
- 12 chapters in each language: fundamentals, resources, compute, storage, networking, identity, governance, observability, costs, architecture, messaging, and DevOps.
- Un caso común: una aplicación universitaria para compartir apuntes.
- A running example: a university app for sharing course notes.
- Prácticas con Azure CLI y Bicep, preguntas con respuestas y un glosario multilingüe.
- Azure CLI and Bicep labs, questions with answers, and a multilingual glossary.

## Cómo usarlo / How to use it

Lee los temas en orden si estás empezando. Después intenta explicar las decisiones del caso práctico sin mirar los apuntes. Las prácticas crean recursos reales y pueden generar costes; revisa sus pasos de limpieza.

Read in order if you are getting started. Then try explaining the case study decisions without looking at the notes. Labs create real resources and may incur costs; follow their cleanup steps.

Son apuntes conceptuales, no un temario oficial ni una garantía de aprobar una certificación. Los servicios, planes y objetivos de examen cambian. No se afirma que las prácticas se hayan desplegado en una suscripción real.

These are conceptual notes, not an official syllabus or a certification guarantee. Services, plans, and exam objectives change. The labs are not claimed to have been deployed in a live subscription.

## Créditos / Credits

Adaptación resumida y reescrita de [Azure-in-bullet-points](https://github.com/undergroundwires/Azure-in-bullet-points), de **undergroundwires**, bajo [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Condensed, rewritten adaptation of **undergroundwires**' Azure-in-bullet-points, under CC BY 4.0.

Cambios: organización por temas, redacción en español e inglés, ejemplos propios, ejercicios y uso de Microsoft Entra ID en lugar de Azure AD. Los antiguos bloques AZ-303 y AZ-304 se tratan como contenido histórico, no como exámenes vigentes. No se reproduce todo el repositorio original ni se implica su respaldo.

Changes: topic-based organisation, Spanish and English writing, original examples, exercises, and Microsoft Entra ID terminology. Historical AZ-303 and AZ-304 sections are not presented as current exams. This is not a complete reproduction of the original repository and does not imply endorsement.

## Validación local / Local validation

Con Python 3 y Bash, ejecuta desde la raíz / With Python 3 and Bash, run from the root:

```bash
python tools/check_docs.py
```

Comprueba enlaces relativos a archivos y secciones Markdown, bloques de código, correspondencia de idiomas, archivos de certificaciones y sintaxis Bash. No consulta URLs remotas ni valida despliegues Azure o compilación Bicep.

Checks relative file links, code fences, language counterparts, certification files, and Bash syntax. It does not check remote URLs, Azure deployments, or Bicep compilation.

[Validación de esta revisión / Revision validation](VALIDATION.md) · [Equivalencia del núcleo / Core parity](STUDY-PARITY.md)

Consulta [ATTRIBUTION.md](ATTRIBUTION.md), [LICENSE.md](LICENSE.md) y [las fuentes](SOURCES.md).
