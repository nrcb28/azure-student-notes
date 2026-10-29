# Common learning route / Ruta común de estudio

The new learning route uses the same twelve foundation units, twenty advanced certification units, scenarios, requested evidence, and three new lab procedures in all eight languages. This is parity of the new learning core, not a claim that every older explanatory paragraph has been translated verbatim or that equal word counts indicate quality.

La nueva ruta comparte doce unidades básicas, veinte unidades avanzadas, escenarios, evidencias y tres procedimientos de laboratorio en los ocho idiomas. La igualdad corresponde a este núcleo nuevo. No se afirma que cada párrafo histórico esté traducido literalmente ni que contar palabras demuestre calidad.

| Language | Core | Advanced labs | Certification workbooks |
|---|---|---|---|
| es | [12 units](es/16-common-core.md) | [3 labs](es/17-advanced-labs.md) | [Index](certifications/es/README.md) |
| en | [12 units](en/16-common-core.md) | [3 labs](en/17-advanced-labs.md) | [Index](certifications/en/README.md) |
| it | [12 units](it/16-common-core.md) | [3 labs](it/17-advanced-labs.md) | [Index](certifications/it/README.md) |
| de | [12 units](de/16-common-core.md) | [3 labs](de/17-advanced-labs.md) | [Index](certifications/de/README.md) |
| fr | [12 units](fr/16-common-core.md) | [3 labs](fr/17-advanced-labs.md) | [Index](certifications/fr/README.md) |
| ru | [12 units](ru/16-common-core.md) | [3 labs](ru/17-advanced-labs.md) | [Index](certifications/ru/README.md) |
| ja | [12 units](ja/16-common-core.md) | [3 labs](ja/17-advanced-labs.md) | [Index](certifications/ja/README.md) |
| zh | [12 units](zh/16-common-core.md) | [3 labs](zh/17-advanced-labs.md) | [Index](certifications/zh/README.md) |

## How to study / Cómo estudiar

1. Complete the core unit and its requested evidence / Completa cada unidad y evidencia.
2. Work through five advanced units for your exam / Desarrolla las cinco unidades del examen.
3. Run the local simulator before optional Azure labs / Empieza por el simulador local.
4. Compare expected and observed outcomes / Compara esperado y observado.
5. Review a decision after changing a requirement / Cambia un requisito y revisa la decisión.

Earlier notes remain linked as supplementary reading, with different historical lengths. The common route is intended to reduce that imbalance without removing existing material. Complete linguistic equivalence of the older editions remains a separate editorial task; structural checks cannot establish it.

Las notas previas se conservan como lectura complementaria y tienen extensiones históricas distintas. La ruta común reduce ese desequilibrio sin eliminar contenido. La equivalencia lingüística completa de las ediciones anteriores sigue siendo una tarea editorial distinta; los controles estructurales no la demuestran.

## Verification / Verificación

- python tools/check_docs.py: file links, structure, source-topic integration, Bash blocks.
- python tools/check_study_core.py: matching unit IDs, nonempty sections, identical lab commands, standalone script syntax.
- python -m unittest discover -s tools -p 'test_*lab*.py' -v: seven behavioural tests.
- Bicep compilation, when reported, is local validation only. Azure deployments, permissions, pricing, and recovery timing require a test subscription.

The new local simulator and unit tests run without Azure credentials. Azure procedures have not been executed here. A source link and a green local check are not a certification guarantee.

## Multiple-choice practice / Práctica de opción múltiple

The [mini quiz](QUIZ.md) adds eight original scenarios, each translated into all eight languages: 64 variants, not 64 distinct questions. Each has four options, matching correct-answer indices and references, general reasoning, and a reason for each wrong choice. The interface, user guide, and generated question sheet are also available in every language. Automated checks establish structure; meaning was reviewed separately.

El [mini simulacro](QUIZ.md) añade ocho escenarios con variantes en los ocho idiomas, además de interfaz, guía y hoja de preguntas. Los índices de respuesta y las referencias coinciden; cada alternativa incorrecta tiene explicación. La comprobación automática cubre la estructura y se complementó con lectura del significado.
