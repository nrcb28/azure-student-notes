# Validation record / Registro de validación

Checks performed for the common-core and advanced-lab revision:

- Documentation links, language file coverage, source integrations, and Bash syntax: passed.
- Common-core checker: twelve foundation units and twenty certification units in every language, with corresponding lab commands: passed.
- Local behavioural tests: seven passed. They cover lost responses, duplicate prevention, unconfirmed writes, permanent failures, invalid retry budgets, and guards that reject unsuitable lab inputs before cloud commands.
- SQLite simulation: with three allowed attempts, naive processing creates two records and idempotent processing creates one. A permanent failure is not retried and writes nothing. With one allowed attempt, a write can exist without a confirmed successful response.
- Bicep CLI 0.48.1: the base storage, base network, and new protected-storage templates compile locally.

No Azure deployment, Blob restore against Azure, effective-permission check against a real tenant, or measured recovery timing was performed. Local compilation does not establish cloud quota, policy, permissions, regional capacity, pricing, or operational success.

No se ejecutaron despliegues ni restauraciones en Azure, ni consultas de permisos en un tenant real. La compilación local no demuestra cuotas, políticas, permisos, disponibilidad regional, precios o éxito operativo.

Structural parity checks do not certify language quality or establish complete translation of older supplementary notes. See [STUDY-PARITY.md](STUDY-PARITY.md).

## Original offline trainer revision · 2026-10-29

At that revision, the trainer had 23 tests covering 320 source-case variants, interval scheduling, selection, Unicode export and HTML escaping, existing-file protection, damaged progress, concurrent sessions and locks, interactive saving and quitting, read-only commands, UTC fallback, and matching ready-made decks. These are local behaviour checks, not assessments of a learner or Azure deployments.

## Mini quiz and document fragments · 2026-10-29

- Full local suite: **64 tests passed**: 23 trainer, 22 quiz, 12 Markdown-link/fragment, five retry-simulator, and two lab-guard tests.
- Quiz bank: eight distinct original scenarios, two per exam route, translated into 64 complete variants. Structural checks enforce eight languages, matching correct-answer indices and references, four distinct options, and a reason for every wrong choice. A separate reading review found no concrete meaning drift; this is not professional translation certification.
- Quiz behaviour: shuffled options are graded by content; route-balanced selection is reproducible; skips and early exits keep unanswered questions in the denominator. Tests cover deferred feedback, late-answer rejection, input validation, Ctrl+C/end-of-input, extreme durations, saved snapshots, Unicode, and protection of existing reports. Completed reports are saved before final correction output.
- Report review recomputes results from saved snapshots without loading the current bank. Corrupt reports are rejected and preserved. These editable files are personal study records, not proof of a supervised assessment.
- Documentation: **303 Markdown files, 2,264 local links, 160 Bash blocks** passed the checker. Local Markdown fragments now include explicit anchors, Unicode headings, duplicate-heading suffixes, encoded paths, and same-file links; fenced examples are excluded. The checker supports ordinary inline links and GitHub-style heading slugs, not every Markdown extension.
- Eight generated question sheets match quiz_bank.json. Common-core and certification-unit checks passed in all eight languages.
- Eight quiz sources on Microsoft Learn were opened and reviewed; see [QUIZ-SOURCES.md](QUIZ-SOURCES.md). Source review is separate from the offline checker, which never fetches remote pages.

Quiz timing is checked after synchronous terminal input; it does not interrupt a waiting prompt. Tests use a controlled clock rather than a real delayed human response. No new cloud deployment or Azure lab execution was performed in this revision.

Las 64 pruebas son comprobaciones locales del software y la documentación. El mini simulacro contiene ocho escenarios traducidos, no 64 preguntas distintas. No se ejecutaron nuevas prácticas en Azure.

## Four additional certification routes · 2026-11-01

- Added DP-900, SC-900, AZ-700, and DP-300 in all eight languages: **96 new documents**, comprising a guide, ten-case bank, and five-unit workbook per route and language.
- Full local suite: **70 tests passed**: 27 trainer, 14 documentation, 22 quiz, five retry-simulator, and two lab-guard tests. Added coverage checks new-route selection, registered and unregistered progress IDs, preservation of earlier ratings, and required material missing even across all translations.
- Trainer: **80 cases per language, 640 unique locale/case IDs overall**. Regenerated all eight Anki decks with 80 cards each; export tests confirm exact correspondence to the current case banks.
- New-document parity: corresponding numbered guide sections, ten complete case answers, twenty new workbook anchors per language, and identical Microsoft Learn source URLs. No English file is used as a translated-edition fallback.
- Common core: twelve foundation units and **forty certification units across eight routes** per language. The three existing advanced labs retain four checked procedural sections and matching commands.
- Documentation checks: **400 Markdown files, 2,801 local links, 170 Bash blocks** passed. Generated multiple-choice sheets still match their separate bank.
- Read-throughs of the English/Spanish new material and selected critical translated cases found no concrete factual or meaning mismatch. They checked identity privilege, route selection, ExpressRoute encryption, SQL encryption boundaries, accidental deletion, Table Storage, and ETL/ELT. Structural checks and spot reviews do not establish professional linguistic certification or full exam coverage.
- Reference review dates remain 2026-10-30 for the four new routes; translation completion and final local validation occurred on 2026-11-01. No newly executed Azure lab, deployment, tenant change, or operational recovery is claimed.

La ampliación incorpora cuatro rutas nuevas y cuarenta escenarios nuevos por idioma. El total de 640 representa ochenta escenarios en ocho idiomas, no 640 escenarios distintos. El mini simulacro mantiene sus ocho preguntas de las cuatro rutas originales; las nuevas rutas están en el entrenador de autoevaluación y en Anki.
