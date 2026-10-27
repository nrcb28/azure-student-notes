# Azure sin tanto lío · Azure without the confusion

Apuntes de Azure para estudiantes de informática. Explicaciones cortas, decisiones razonadas y prácticas pequeñas para entender lo que estamos desplegando.

Azure study notes for computer science students. Short explanations, practical decisions, and small labs to understand what we deploy.

**[Leer en español](es/README.md) · [Read in English](en/README.md)**

**Certificaciones / Certifications: [Español](certifications/es/README.md) · [English](certifications/en/README.md)**

## Certificaciones con más detalle / Detailed certification guides

| Examen / Exam | Español | English |
|---|---|---|
| AZ-900 · Fundamentals | [Guía](certifications/es/AZ-900.md) | [Guide](certifications/en/AZ-900.md) |
| AZ-104 · Administrator | [Guía](certifications/es/AZ-104.md) | [Guide](certifications/en/AZ-104.md) |
| AZ-305 · Infrastructure Solutions | [Guía](certifications/es/AZ-305.md) | [Guide](certifications/en/AZ-305.md) |
| AZ-400 · DevOps Solutions | [Guía](certifications/es/AZ-400.md) | [Guide](certifications/en/AZ-400.md) |

Cada guía desarrolla conceptos, decisiones, diagnóstico, práctica y repaso. Hay 10 casos adicionales por examen y por idioma: 80 casos en total. Las referencias de objetivos y pesos se comprobaron el 27 de octubre de 2026; consulta las páginas oficiales antes de reservar un examen.

Each guide develops concepts, decisions, troubleshooting, practice, and review. There are ten additional cases per exam and language: eighty in total. Objective dates and weightings were checked on 27 October 2026; consult official pages before booking an exam.

## Qué hay aquí / What's inside

- 12 capítulos en cada idioma: fundamentos, recursos, cómputo, almacenamiento, redes, identidad, gobierno, observabilidad, costes, arquitectura, mensajería y DevOps.
- 12 chapters in each language: fundamentals, resources, compute, storage, networking, identity, governance, observability, costs, architecture, messaging, and DevOps.
- Un caso común: una aplicación universitaria para compartir apuntes.
- A running example: a university app for sharing course notes.
- Prácticas con Azure CLI y Bicep, preguntas con respuestas y un glosario bilingüe.
- Azure CLI and Bicep labs, questions with answers, and a bilingual glossary.

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

Consulta [ATTRIBUTION.md](ATTRIBUTION.md), [LICENSE.md](LICENSE.md) y [las fuentes](SOURCES.md).
