# Offline study trainer / Entrenador local

Turn the original case banks into a review session, track self-ratings, and export cards without a cloud account. Requires Python 3.9+ and the standard library. No pip installation, Azure credentials, telemetry, or network calls.

Usa los casos originales para practicar, guardar autoevaluaciones y exportar tarjetas. Python 3.9+ y biblioteca estándar. Sin instalación de paquetes, credenciales Azure, telemetría ni llamadas de red.

## Start / Empezar

```bash
python tools/study.py demo --lang es --exam AZ-104
python tools/study.py study --lang es --exam AZ-104 --limit 5
```

Supported routes: AZ-900, AZ-104, AZ-305, AZ-400, DP-900, SC-900, AZ-700, DP-300, AI-901, SC-200, SC-300, AZ-140, AI-103, DP-700, SC-100, AZ-120, and AZ-802. There are 170 cases per language, ten per route.

Rutas disponibles: las diecisiete del índice de certificaciones, con 170 casos por idioma y diez por ruta.

Choose es, en, it, de, fr, ru, ja, or zh. Repeat --exam to combine certifications. Question and answer text come directly from the Markdown case files. Press Enter to reveal, then rate 0–3; q leaves. Ratings are saved after each completed card. This is manual self-assessment, not automated answer grading.

Selecciona idioma y combina exámenes repitiendo --exam. Las preguntas proceden de los Markdown. Intro revela la solución; valora 0–3 y usa q para salir. Cada valoración se guarda. No hay corrección automática.

## Commands / Comandos

| Command | Behaviour / Comportamiento |
|---|---|
| study | Due and new cases; --mode weak for rated difficulties or lapse history; --mode random for a shuffled session |
| stats | New, due, consolidated and lapses by exam; --json for structured output |
| plan | Suggested sessions with --days and --minutes; not a prediction of future due dates |
| export | Anki TSV with --output; existing files are never overwritten |
| demo | One example without saving progress |
| doctor | Validate 1360 source-case variants across eight languages |

Consolidated means two consecutive ratings of at least 2. It is not a pass prediction. Weak mode can include a case with a past lapse even after a later successful rating.

Consolidada significa dos valoraciones consecutivas de al menos 2. No predice aprobar. El modo weak conserva casos con olvidos anteriores aunque luego se hayan recordado.

For longer plans, each exam starts another pass through its pool only after every case has been suggested. These are suggested practice slots, not predictions of due reviews.

En los planes largos, cada examen empieza otra vuelta por su banco después de haber propuesto todos sus casos. Son huecos de práctica sugeridos, no predicciones de repasos pendientes.

## Review intervals / Intervalos de repaso

Ratings 0 and 1 reset the successful-review streak and return after ten minutes or one day respectively. Ratings 2 and 3 share that streak. With 2, the first success schedules one day, the second three, and later successes double the previous interval. With 3, the first success schedules four days; later successes multiply the previous interval by 2.5, round to whole days, and use at least four days. Both cap at 365 days. Changing between 2 and 3 does not reset the streak: 3 followed by 2 schedules four then three days.

Las valoraciones 0 y 1 reinician la racha de aciertos y vuelven a los diez minutos o al día siguiente, respectivamente. Las valoraciones 2 y 3 comparten esa racha. Con 2, el primer acierto programa un día, el segundo tres y los siguientes duplican el intervalo anterior. Con 3, el primero programa cuatro días; los siguientes multiplican el intervalo anterior por 2,5, redondean a días enteros y usan al menos cuatro días. Ambos tienen un máximo de 365 días. Cambiar entre 2 y 3 no reinicia la racha: 3 seguido de 2 programa cuatro y luego tres días.

## Storage and recovery / Guardado y recuperación

The default .study-progress.json is excluded from Git. --progress selects another location; if choosing a custom name, keep it outside version control. Language progress is separate. Ratings and dates are stored; written answers are not. Internal timestamps use UTC. Display uses Europe/Madrid by default; override with --timezone and an IANA timezone.

El progreso está separado por idioma. No se guardan respuestas escritas. Las fechas internas están en UTC; la visualización usa Europe/Madrid y se cambia con --timezone.

Writes are atomic and use a lock and fingerprint to prevent stale sessions overwriting newer progress. Corrupt or unsupported JSON is not replaced. Back up the file before manual repairs. A leftover .lock may remain after a forced process termination: confirm no trainer is running before removing that lock. Do not delete the progress file to resolve a lock.

Las escrituras son atómicas y detectan sesiones concurrentes. Un JSON corrupto no se sustituye. Si queda un archivo .lock tras un cierre forzado, comprueba que no siga ejecutándose el entrenador antes de quitar solo ese bloqueo.

## Exports and verification / Exportación y comprobación

```bash
python tools/study.py export --lang es --exam AZ-104 --output exports/es-az104.tsv
python -m unittest discover -s tools -p test_study.py -v
```

Export columns are question, explanation, and tags. Text is HTML-escaped, with line breaks preserved for import. Anki has its own review schedule and does not synchronise trainer progress. See [ready-made decks](flashcards/README.md).

Las columnas son pregunta, explicación y etiquetas. Anki mantiene su propio progreso; no se sincroniza con el entrenador.

The scheduler is a deliberately simple interval rule, not FSRS or a scientifically validated retention guarantee. The study material is independent of Microsoft and not official exam content.

IANA timezone display needs the operating system timezone database. If it is unavailable, use --timezone UTC; that mode uses the standard library without additional packages. Export, stats, plan and doctor do not require timezone data.

Si no están disponibles los datos horarios del sistema, usa --timezone UTC. No requiere paquetes adicionales.

## Preguntas con corrección / Questions with marking

El [mini simulacro](QUIZ.md) añade 34 escenarios originales de opción múltiple para las diecisiete rutas, dos por ruta, traducidos a ocho idiomas: 272 variantes. Incluye explicación por distractor, informe local y repaso de errores. Es una herramienta separada: este entrenador sigue usando autoevaluación para sus casos abiertos.

The [mini quiz](QUIZ.md) adds 34 original multiple-choice scenarios across all seventeen routes, two per route, translated into eight languages: 272 variants. It includes distractor reasoning, local reports, and mistake review. Its results are separate from this trainer's open-case self-ratings.
