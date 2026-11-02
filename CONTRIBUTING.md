# Contribuir / Contributing

- Corrige errores con una explicación y, cuando sea posible, un enlace oficial.
- Explain corrections and link official documentation where possible.
- Actualiza los ocho idiomas cuando cambie el significado de un concepto.
- Update all eight languages when a concept changes.
- Mantén frases claras, ejemplos pequeños y límites explícitos.
- Keep sentences clear, examples small, and limitations explicit.
- No incluyas credenciales, datos personales ni preguntas filtradas de exámenes.
- Do not include credentials, personal data, or leaked exam questions.
- Distingue entre una práctica verificada localmente y un despliegue probado en Azure.
- Distinguish local checks from actual Azure deployments.

## Rutas y comprobaciones / Routes and checks

Ejecuta la comprobación completa desde cualquier carpeta, indicando la ruta al script si no estás en la raíz. Requiere Python 3.9+ y Bash:

Run the complete offline verification with Python 3.9+ and Bash. Use the script's path when running outside the repository root:

```bash
python tools/verify.py
```

El comando detecta discrepancias entre registros de rutas e idiomas y ejecuta los comprobadores y pruebas. Devuelve un código distinto de cero ante cualquier fallo, aunque las comprobaciones posteriores pasen. No usa red ni Azure, ni modifica progreso, mazos o hojas generadas. La compilación Bicep se comprueba por separado cuando se dispone de su CLI.

The command checks route/language registry agreement and runs the checkers and tests. Any failed check makes it fail overall, even if later checks pass. No network or Azure calls, progress updates, deck exports, or generated-sheet writes. Bicep compilation remains separate.


Cada ruta de certificación necesita guía, diez casos con respuesta desplegable y cuaderno de cinco unidades en los ocho idiomas. Conserva IDs de casos y anclajes al corregir traducciones para no invalidar el progreso de quienes estudian. Las fuentes oficiales y fechas consultadas se registran en [CERTIFICATION-SOURCES.md](CERTIFICATION-SOURCES.md).

Every certification route needs a guide, ten cases with expandable answers, and a five-unit workbook in all eight languages. Preserve case IDs and workbook anchors when correcting translations. Record official source versions and review dates in the source register. If registering another route, update the trainer allowlist, documentation requirements, study-core manifest, and their fixtures together; regenerate the Anki decks from the source cases.

```bash
python tools/study.py doctor --lang es
python tools/check_docs.py
python tools/check_study_core.py
python tools/render_quiz_docs.py --check
python -m unittest discover -s tools -p 'test_*.py' -v
```

El banco de opción múltiple tiene su propio alcance y no se amplía por registrar una ruta en el entrenador. / The multiple-choice bank has its own scope; registering a trainer route does not add quiz questions automatically.
