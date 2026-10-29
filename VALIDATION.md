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

## Offline study trainer

The trainer has 23 tests covering all 320 source cases, interval scheduling, selection, Unicode export and HTML escaping, existing-file protection, damaged progress, concurrent sessions and locks, interactive saving and quitting, read-only commands, UTC fallback, and matching ready-made decks. These are local behaviour checks, not assessments of a learner or Azure deployments.

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
