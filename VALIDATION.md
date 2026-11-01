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

## Foundry, security operations, identity and desktop routes · 2026-11-01

- Added AI-901, SC-200, SC-300, and AZ-140 in all eight languages: **96 additional documents** with detailed guides, ten original cases per route, and five-unit workbooks.
- Current totals: **twelve routes, 120 cases and sixty certification units per language**. The trainer parses **960 unique locale/case IDs**; these are 120 original scenario identities in eight languages, not 960 unrelated scenarios.
- Full local suite: **70 tests passed**. Updated route fixtures and progress tests cover current additions, earlier additions, legacy progress, and strict rejection of unregistered codes. The test count remains the same because existing route regressions now cover the expanded allowlist.
- Regenerated eight Anki decks with **120 cards each**. Export tests confirm exact correspondence to the source case banks.
- New-document checks passed for numbered guide sections, ten complete case answers, five stable workbook anchors per route, Microsoft Learn source URL sets, and unchanged fenced code across all eight editions. Answer-toggle labels are localised.
- Documentation: **496 Markdown files, 3,380 local links, 171 Bash blocks** passed. Common-core and generated multiple-choice-sheet checks also passed. The multiple-choice bank retains its original four-route scope; newly added routes are integrated into the self-rating trainer and Anki.
- Independent read-throughs reviewed the new English/Spanish material and 66 selected question/answer pairs in the six other languages. No remaining concrete factual or meaning mismatch was found. These checks do not establish professional translation certification or exhaustive exam coverage.
- Official guide and credential sources were opened on 2026-11-01. AI-901 follows current Foundry implementation objectives; SC-300 preserves the observed summary/detail weighting discrepancy instead of inventing a corrected value.
- KQL examples use hypothetical or synthetic data and were not executed against Azure. No deployment, Foundry model or agent invocation, identity-tenant change, security response, AVD session, or operational recovery is claimed.

La ampliación añade otras cuatro rutas completas en los ocho idiomas. La verificación es local y documental; los ejercicios proponen evidencia de estudio sin atribuir resultados observados en Azure.

## Advanced AI development, Fabric engineering, architecture and SAP · 2026-11-01

- Added AI-103, DP-700, SC-100, and AZ-120 in all eight languages: **96 additional guide, case-bank, and workbook documents**.
- Current totals: **sixteen routes, 160 original scenarios and eighty certification units per language**. The trainer parses **1280 unique locale/case IDs**, representing those scenarios in eight languages.
- Full local suite: **70 tests passed**. Existing route fixtures and progress regressions now include all sixteen registered codes, the four new case banks, preserved earlier ratings, and strict unknown-code rejection. The test count is unchanged; the covered route matrix is larger.
- Eight regenerated Anki decks contain **160 cards each**; export tests match all published source cases exactly.
- New-document checks passed for numbered sections, ten complete case answers, five stable unit anchors per route, Microsoft Learn source URL sets, and unchanged fenced code across languages. Answer toggles are localised.
- Documentation: **592 Markdown files, 3,999 local links, 172 Bash blocks** passed. Foundation-unit, eighty-unit certification coverage, advanced-lab command, and generated multiple-choice-sheet checks passed too.
- Independent read-throughs covered all new English/Spanish material and selected critical passages in the six other languages. Review clarified DP-700's yesterday-only reporting contract in all eight editions and corrected Spanish/Japanese SAP source-of-truth wording. The corrected passages were checked again; no remaining material issue was identified. This does not establish professional translation certification or exhaustive exam coverage.
- All editions preserve DP-700's undated live skills-heading qualification and the requirement to know the watermark at arrival before deciding late-event acceptance. They also preserve SC-100's current one-of-three Associate prerequisite and AZ-120's recommended, rather than mandatory, Azure Administrator preparation.
- Source checks are dated 2026-11-01. Synthetic loading states, architecture decisions, AI outputs, SAP failover and recovery evidence remain exercises or predictions. No Foundry, Fabric, security-control, SAP/HANA or Azure deployment execution is claimed.

La ampliación lleva el total a dieciséis rutas y 160 escenarios por idioma. El mini simulacro de opción múltiple conserva su banco anterior; las nuevas rutas están integradas en el entrenador de autoevaluación y en Anki.
