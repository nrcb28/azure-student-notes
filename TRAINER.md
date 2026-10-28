# Offline study trainer / Entrenador local

Turn the original case banks into a review session, track self-ratings, and export cards without a cloud account. Requires Python 3.9+ and the standard library. No pip installation, Azure credentials, telemetry, or network calls.

Usa los casos originales para practicar, guardar autoevaluaciones y exportar tarjetas. Python 3.9+ y biblioteca estándar. Sin instalación de paquetes, credenciales Azure, telemetría ni llamadas de red.

## Start / Empezar

```bash
python tools/study.py demo --lang es --exam AZ-104
python tools/study.py study --lang es --exam AZ-104 --limit 5
```

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
| doctor | Validate 320 source cases across eight languages |

Consolidated means two consecutive ratings of at least 2. It is not a pass prediction. Weak mode can include a case with a past lapse even after a later successful rating.

Consolidada significa dos valoraciones consecutivas de al menos 2. No predice aprobar. El modo weak conserva casos con olvidos anteriores aunque luego se hayan recordado.

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
