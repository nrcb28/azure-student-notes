# Mini simulacro local / Offline mini quiz

34 escenarios originales, dos por cada una de las diecisiete rutas, traducidos a ocho idiomas: 272 variantes. Corrección por opción elegida, explicación del error y lecturas para repasar. Python 3.9+ y biblioteca estándar; funciona sin cuenta de Azure ni conexión.

34 original scenarios, two per route across all seventeen routes, with questions, explanations, and interface in eight languages: 272 variants. This is a small practice bank, independent of Microsoft and separate from the 1360 open-response language variants used by the [self-rating trainer](TRAINER.md).

[Español](es/19-mini-quiz.md) · [English](en/19-mini-quiz.md) · [Italiano](it/19-mini-quiz.md) · [Deutsch](de/19-mini-quiz.md) · [Français](fr/19-mini-quiz.md) · [Русский](ru/19-mini-quiz.md) · [日本語](ja/19-mini-quiz.md) · [简体中文](zh/19-mini-quiz.md)

Puedes practicar leyendo las [preguntas desplegables en GitHub](es/20-quiz-cases.md) o ejecutar el programa desde la raíz del repositorio. / Read the [questions on GitHub](en/20-quiz-cases.md) or run the program from the repository root.

Rutas disponibles / Available routes: AZ-900, AZ-104, AZ-305, AZ-400, DP-900, SC-900, AZ-700, DP-300, AI-901, SC-200, SC-300, AZ-140, AI-103, DP-700, SC-100, AZ-120.

## Empezar / Start

```bash
python tools/quiz.py demo --lang es
python tools/quiz.py run --lang es --exam AZ-104 --count 2
python tools/quiz.py run --lang en --mode exam --count 8 --minutes 12
python tools/quiz.py run --lang en --mode exam --count 34
```

A–D responde; S o Intro salta; Q termina. El orden de preguntas y opciones cambia. La selección reparte preguntas entre las rutas elegidas, sin repetir escenarios. Repite --exam para combinar rutas y usa --seed 42 para reproducir una selección y su orden. Cada ruta contiene dos escenarios: --count 4 con una sola ruta se rechaza; sin --count se usan hasta ocho escenarios disponibles. Usa --count 34 sin filtrar rutas para recorrer todo el banco.

A–D answers; S or Enter skips; Q finishes. Selection balances the chosen routes and never repeats a scenario within a session. A fixed seed reproduces both question and option order. With two questions in one route, an explicit count of four is rejected. Omitting --count selects up to eight available scenarios. Use --count 34 without an exam filter to practise the complete bank.

| Modo / Mode | Comportamiento / Behaviour |
|---|---|
| practice | Explicación tras cada respuesta / Explanation after each answer |
| exam | Explicaciones al terminar / Explanations after the session |
| review | Repasar errores y preguntas sin responder / Revisit incorrect and unanswered questions |
| demo | Ejemplo sin guardar / Read-only example |
| doctor | Comprobar las 272 variantes y sus referencias / Validate all 272 variants and their references |

El resultado muestra aciertos sobre todas las preguntas seleccionadas, errores y preguntas sin responder. Salir antes no reduce el denominador. No hay nota de aprobado ni predicción sobre una certificación: dos preguntas por ruta cubren una parte pequeña del temario.

Results show correct answers out of all selected questions, incorrect answers, and unanswered questions. Finishing early does not shrink the denominator. No pass threshold or readiness prediction is assigned; two questions per route cover only a small part of each syllabus.

## Lecturas relacionadas / Related reading

Los 26 escenarios añadidos enlazan a guías de certificación del mismo idioma en `certifications/<idioma>/<examen>.md`, por ejemplo [AI-103 en español](certifications/es/AI-103.md). Los ocho escenarios iniciales conservan sus enlaces a capítulos. Los informes anteriores a la ampliación siguen siendo compatibles: review usa las preguntas y referencias guardadas en cada informe.

The 26 added scenarios link to certification guides in the same language at `certifications/<language>/<exam>.md`, such as [AI-103 in English](certifications/en/AI-103.md). The original eight scenarios keep their chapter links. Reports saved before the expansion remain compatible: review uses the question and reference snapshots stored in each report.

## Temporizador / Timer

--minutes es opcional. El reloj usa tiempo transcurrido monotónico e incluye el tiempo dedicado a leer las correcciones del modo practice. La entrada del terminal es síncrona: **pulsa Intro al vencer el plazo**. El programa comprueba el tiempo al recibir la entrada y rechaza respuestas tardías; no interrumpe una espera de teclado por sí solo.

The optional limit uses monotonic elapsed time, including practice feedback. **Press Enter when time expires.** Time is checked after input; late answers are rejected. It does not interrupt a blocked terminal prompt.

## Informe y repaso / Report and review

```bash
python tools/quiz.py run --lang es --mode exam --report .study-reports/my-first-quiz.json
python tools/quiz.py review --lang es --report .study-reports/my-first-quiz.json
python tools/quiz.py review --lang es --report .study-reports/my-first-quiz.json --all
python tools/quiz.py review --lang es --report .study-reports/my-first-quiz.json --json
```

La ruta se imprime al terminar. Por defecto cada sesión obtiene un archivo nuevo en .study-reports/, excluido de Git. Una ruta personalizada con --report es responsabilidad de quien la elige: mantenla fuera del control de versiones. Un archivo existente se rechaza antes de empezar y nunca se sustituye.

The report path is printed at the end. Default filenames are unique and live in .study-reports/, excluded from Git. Keep custom report locations outside version control. Existing reports are rejected before questions begin and are never overwritten.

El JSON contiene fechas UTC, duración, estado de la sesión y copias de las preguntas, opciones, elecciones, explicaciones y fuentes. review calcula de nuevo los totales desde esas copias y funciona aunque cambie el banco. --lang cambia las etiquetas de la interfaz; las preguntas guardadas conservan su idioma. Por defecto muestra errores y preguntas sin responder; --all incluye las acertadas. El resumen por tema orienta la siguiente lectura.

JSON stores UTC timestamps, duration, session status, and snapshots of questions, option order, choices, explanations, and sources. Review recomputes totals from those snapshots, so later bank edits do not change the saved session. --lang changes interface labels, while saved questions keep their original language. Reports are editable personal files, not signed assessment evidence.

No se guardan respuestas escritas, credenciales ni telemetría, ni se hacen llamadas de red. Q, fin de entrada y Ctrl+C durante las preguntas conservan las elecciones completadas. **El informe se guarda al terminar la sesión**, antes de la corrección final; un cierre forzado del proceso o un fallo de almacenamiento puede impedirlo. El progreso de este modo y el del entrenador de autoevaluación son independientes.

No written answers, credentials, telemetry, or network calls. Q, end-of-input, and Ctrl+C during questioning retain completed choices. **Saving occurs at session end**, before final correction output. Forced termination or a storage failure can prevent saving; this is separate from the self-rating trainer's progress.

## Mantener el banco / Maintain the bank

El archivo [quiz_bank.json](tools/quiz_bank.json) es la fuente de las preguntas. Cada escenario requiere ocho variantes con cuatro opciones, índice de respuesta correcto, explicación general, motivo para cada distractor, fuente HTTPS de Microsoft Learn y lectura local del mismo idioma (capítulo o guía de certificación). Las variantes conservan los mismos índices y referencias; la revisión de significado requiere lectura humana.

The bank is the question source. Every scenario needs eight variants, four options, one answer index, general reasoning, a reason for each distractor, a Microsoft Learn URL, and a local reading reference in the same language (a chapter or certification guide). Matching structure cannot establish translation quality. Sources support the reasoning; they are not exam dumps or full-syllabus coverage.

```bash
python tools/quiz.py doctor --lang es
python tools/render_quiz_docs.py
python tools/render_quiz_docs.py --check
python -m unittest discover -s tools -p 'test_*.py' -v
python tools/check_docs.py
python tools/check_study_core.py
```

render_quiz_docs.py regenera las ocho hojas Markdown a partir del banco. --check detecta hojas desactualizadas sin modificarlas. doctor verifica estructura, idiomas, índices coincidentes y lecturas locales; no consulta las URLs ni prueba Azure.

The renderer regenerates the eight Markdown question sheets; --check detects stale copies without writing. Doctor checks structure, locale coverage, matching answer indices, and local reading references. It does not fetch remote URLs or test Azure. See the [source map](QUIZ-SOURCES.md) and [validation record](VALIDATION.md).
