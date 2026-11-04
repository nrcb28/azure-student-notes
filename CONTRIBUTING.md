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

El banco de opción múltiple tiene 34 escenarios originales para las diecisiete rutas, dos por ruta, con ocho variantes por escenario: 272 variantes. Registrar una ruta en el entrenador no añade preguntas automáticamente. Al ampliar el banco, actualiza también su registro de rutas y sus pruebas, añade preguntas, opciones, explicaciones y motivos de cada distractor en los ocho idiomas y regenera las hojas con python tools/render_quiz_docs.py. Conserva los IDs existentes. Las preguntas nuevas enlazan a guías de certificación del mismo idioma; las referencias anteriores a capítulos y los informes guardados deben seguir siendo compatibles. Consulta [QUIZ.md](QUIZ.md) para mantener el banco.

The multiple-choice bank has 34 original scenarios across the seventeen routes, two per route, with eight variants per scenario: 272 variants. Registering a trainer route does not add quiz questions automatically. When expanding the bank, update its route registry and tests, add questions, options, explanations, and distractor reasoning in all eight languages, and regenerate sheets with python tools/render_quiz_docs.py. Preserve existing IDs. New questions link to certification guides in the same language; earlier chapter references and saved reports must remain compatible. See [QUIZ.md](QUIZ.md) for bank maintenance.

## Integración continua / Continuous integration

El [flujo de GitHub Actions](.github/workflows/verify.yml) está configurado para ejecutar python tools/verify.py en push, pull request y ejecución manual. Usa Ubuntu 24.04 con Python 3.9 y 3.12. Ejecuta comprobaciones y pruebas locales sin cuenta, credenciales ni llamadas a Azure; no despliega recursos. Una ejecución correcta no demuestra calidad de traducción ni cobertura completa de los exámenes.

The [GitHub Actions workflow](.github/workflows/verify.yml) is configured to run python tools/verify.py on pushes, pull requests, and manual dispatch. It uses Ubuntu 24.04 with Python 3.9 and 3.12. Checks and tests run locally without an Azure account, credentials, or calls; no resources are deployed. A successful run does not establish translation quality or full exam coverage.

Un trabajo adicional de Windows Server 2025 analiza la sintaxis de los bloques PowerShell de AZ-802 con [check_az802_powershell.ps1](tools/check_az802_powershell.ps1). Solo utiliza el parser: no ejecuta los comandos de los apuntes, instala roles ni consulta servidores. Si tienes PowerShell 7, puedes ejecutar `pwsh -NoProfile -File tools/check_az802_powershell.ps1` desde cualquier directorio.

A separate Windows 2025 job parses the AZ-802 PowerShell blocks. It does not execute the examples, install roles, or query servers. With PowerShell 7 available, run the same parser check using the command above; the Python verifier remains independent of PowerShell.
