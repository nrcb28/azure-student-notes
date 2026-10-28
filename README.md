# Azure sin tanto lío · Azure without the confusion

[Español](es/README.md) · [English](en/README.md) · [Italiano](it/README.md) · [Deutsch](de/README.md) · [Français](fr/README.md) · [Русский](ru/README.md) · [日本語](ja/README.md) · [简体中文](zh/README.md)

Apuntes de Azure para estudiantes de informática. Explicaciones cortas, decisiones razonadas y prácticas pequeñas para entender lo que estamos desplegando.

Azure study notes for computer science students. Short explanations, practical decisions, and small labs to understand what we deploy.

**[Leer en español](es/README.md) · [Read in English](en/README.md)**

**Certificaciones / Certifications: [Español](certifications/es/README.md) · [English](certifications/en/README.md)**

## Ruta común ampliada / Expanded common route

- [Doce unidades básicas en ocho idiomas / Twelve foundation units](STUDY-PARITY.md).
- [20 unidades avanzadas por idioma / 20 advanced units per language](certifications/es/README.md).
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
| Español | [Español](es/README.md) | [AZ-900 · AZ-104 · AZ-305 · AZ-400](certifications/es/README.md) |
| English | [English](en/README.md) | [AZ-900 · AZ-104 · AZ-305 · AZ-400](certifications/en/README.md) |
| Italiano | [Italiano](it/README.md) | [AZ-900 · AZ-104 · AZ-305 · AZ-400](certifications/it/README.md) |
| Deutsch | [Deutsch](de/README.md) | [AZ-900 · AZ-104 · AZ-305 · AZ-400](certifications/de/README.md) |
| Français | [Français](fr/README.md) | [AZ-900 · AZ-104 · AZ-305 · AZ-400](certifications/fr/README.md) |
| Русский | [Русский](ru/README.md) | [AZ-900 · AZ-104 · AZ-305 · AZ-400](certifications/ru/README.md) |
| 日本語 | [日本語](ja/README.md) | [AZ-900 · AZ-104 · AZ-305 · AZ-400](certifications/ja/README.md) |
| 简体中文 | [简体中文](zh/README.md) | [AZ-900 · AZ-104 · AZ-305 · AZ-400](certifications/zh/README.md) |

Las versiones italiana, alemana, francesa, rusa, japonesa y china son adaptaciones de estudio más compactas: incluyen los doce temas, prácticas, repaso y las cuatro certificaciones. Español e inglés mantienen los desarrollos más extensos. [Detalles de las ediciones](LOCALIZATION.md).

The Italian, German, French, Russian, Japanese, and Chinese editions are more compact study adaptations covering all twelve topics, labs, review, and the four certification routes. Spanish and English retain the longer explanations. [Edition details](LOCALIZATION.md).

[Glosario en ocho idiomas / Eight-language glossary](GLOSSARY-multilingual.md).

## Certificaciones con más detalle / Detailed certification guides

| Examen / Exam | Español | English |
|---|---|---|
| AZ-900 · Fundamentals | [Guía](certifications/es/AZ-900.md) | [Guide](certifications/en/AZ-900.md) |
| AZ-104 · Administrator | [Guía](certifications/es/AZ-104.md) | [Guide](certifications/en/AZ-104.md) |
| AZ-305 · Infrastructure Solutions | [Guía](certifications/es/AZ-305.md) | [Guide](certifications/en/AZ-305.md) |
| AZ-400 · DevOps Solutions | [Guía](certifications/es/AZ-400.md) | [Guide](certifications/en/AZ-400.md) |

Cada guía desarrolla conceptos, decisiones, diagnóstico, práctica y repaso. Hay 10 casos de certificación por examen y por idioma: 320 casos en los ocho idiomas. Las referencias de objetivos y pesos se comprobaron el 27 de octubre de 2026; consulta las páginas oficiales antes de reservar un examen.

Each guide develops concepts, decisions, troubleshooting, practice, and review. There are ten certification cases per exam and language: 320 cases across eight languages. Objective dates and weightings were checked on 27 October 2026; consult official pages before booking an exam.

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

Comprueba enlaces relativos a archivos, bloques de código, correspondencia de idiomas, archivos de certificaciones y sintaxis Bash. No consulta URLs remotas ni valida despliegues Azure o compilación Bicep.

Checks relative file links, code fences, language counterparts, certification files, and Bash syntax. It does not check remote URLs, Azure deployments, or Bicep compilation.

[Validación de esta revisión / Revision validation](VALIDATION.md) · [Equivalencia del núcleo / Core parity](STUDY-PARITY.md)

Consulta [ATTRIBUTION.md](ATTRIBUTION.md), [LICENSE.md](LICENSE.md) y [las fuentes](SOURCES.md).
