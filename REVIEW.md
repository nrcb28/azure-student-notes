# Revisión y mejoras / Review and improvements · 2026-11-02

Se revisaron las herramientas locales, los índices en ocho idiomas y varios límites de validación. Las correcciones conservan las dieciséis rutas, los 160 casos por idioma y el formato del progreso existente.

This review covers local tools, eight-language navigation, and validation behaviour. It preserves sixteen routes, 160 cases per language, and the existing progress format.

| Hallazgo / Finding | Cambio comprobable / Verifiable change |
|---|---|
| El plan repetía 1–5 tras agotar diez casos / The plan repeatedly returned to 1–5 | Reinicia cada ciclo por examen tras cubrir sus casos / Each exam pool restarts after coverage; five-day regression alternates 1–5 and 6–10 |
| Plantillas de interfaz corruptas podían fallar durante una sesión / Damaged interface templates could fail during a session | Campos esperados y formato se validan antes de pedir respuestas / Canonical simple placeholders are checked before input |
| JSON con claves repetidas podía ocultar valoraciones / Duplicate progress keys could hide ratings | Se rechaza sin sustituir el archivo / Duplicate keys are rejected without replacement |
| Una ruta de informe con enlace simbólico roto pasaba la comprobación previa / A dangling report symlink passed preflight | Se rechaza antes de empezar, conservando enlace y destino / Reject before questions while preserving the link and target |
| UUID en mayúsculas omitía asignaciones en el filtro exacto / Uppercase UUID missed exact assignment matches | Normalización tras validar el UUID / Normalise the validated principal UUID before filtering |
| Recuperación rechazaba booleanos TSV válidos y no verificaba HNS / Recovery rejected valid TSV booleans and did not verify HNS | Acepta true/True y false/False; exige HNS deshabilitado y protección explícita / Accept both spellings and verify flat namespace and protection before data operations |
| Un fallo de verificación debía dejar evidencia recuperable / Failed recovery verification needs recoverable evidence | Se muestra el contenedor sintético y se conserva si falla la comparación / Print the synthetic container and preserve it when byte verification fails |
| Índices incompletos y fechas agrupadas de forma ambigua / Incomplete contents and ambiguous reference-date summaries | Capítulos 1–20 accesibles, navegación sin duplicados y fechas por revisión / Chapters 1–20 indexed, duplicate navigation removed, review dates distinguished |
| El comprobador trataba enlaces dentro de código como enlaces reales / Inline-code examples were treated as actual links | Ignora spans de código; informa URLs malformadas sin abortar todo el documento / Ignore code spans and report malformed targets without aborting the document |
| Varias comprobaciones separadas facilitaban omisiones / Separate commands made checks easy to omit | Un comando comprueba registros, documentos, contenido y pruebas / One command checks registries, documents, content and tests |

```bash
python tools/verify.py
```

La verificación completa requiere Python 3.9+ y Bash. Revisa enlaces y fragmentos locales, unidades, bancos de casos, interfaz del mini simulacro, hojas generadas y pruebas, incluida la correspondencia con Anki. No escribe datos personales ni regenera artefactos. Si falta Bash o falla cualquier paso, devuelve error.

Complete verification requires Python 3.9+ and Bash. It checks local links/fragments, units, case banks, quiz interface, generated sheets and tests, including Anki consistency. It does not update personal data or regenerate artifacts. Missing Bash or any failed check produces failure.

Las pruebas de laboratorio usan una CLI falsa local y datos sintéticos; no prueban una suscripción Azure. Las tres plantillas Bicep se compilaron localmente durante esta revisión. El registro de validación detalla el resultado final. Las comprobaciones de estructura no sustituyen una revisión lingüística profesional ni una prueba operativa en Azure.

Lab tests use a local fake CLI and synthetic data. All three Bicep templates compiled locally during this review. Structure and behaviour checks establish neither professional translation certification nor operational success in Azure.

El requisito de HNS deshabilitado pertenece a este laboratorio y su plantilla. Azure también admite recuperación de objetos con espacio jerárquico; sus condiciones deben consultarse en la [documentación de soft delete](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview). / The flat-namespace guard is this lab’s scope, rather than a claim that Azure lacks hierarchical-namespace recovery.

[Registro / Record](VALIDATION.md) · [Herramienta / Runner](tools/verify.py) · [Contribuir / Contributing](CONTRIBUTING.md)

## Ampliación del simulacro y verificación continua · 2026-11-03

El mini simulacro pasa de ocho a 32 escenarios originales: dos por cada una de las dieciséis rutas, con 256 variantes en ocho idiomas. Cada nueva pregunta incluye tres explicaciones de alternativas incorrectas, una fuente directa y una guía de certificación del mismo idioma. Los ocho casos anteriores y los informes guardados conservan su compatibilidad. La sesión rápida sigue usando hasta ocho preguntas; --count 32 permite recorrer todo el banco.

The quiz now covers all sixteen routes with two original scenarios each. New reference validation supports certification guides while preserving old chapter references and archived reports. Eleven additional regressions bring the suite to 109 passing tests. The source review replaced twelve broad or mismatched citations, and explicitly bounds application-owned policies and scenario reasoning.

La verificación está automatizada en [GitHub Actions](.github/workflows/verify.yml) para Python 3.9 y 3.12. El registro distingue los resultados locales de cada ejecución alojada. Dos preguntas por ruta orientan el repaso; no constituyen un temario completo ni predicen el aprobado.

## AZ-802: administración y diagnóstico de Windows Server · 2026-11-04

Se añadió una ruta completa en ocho idiomas: quince apartados de explicación, diez casos razonados y cinco investigaciones con evidencias. El material parte de un laboratorio universitario inventado y pregunta qué capa falla, qué observación distingue las hipótesis y cómo conservar el acceso o los datos. Incluye un plan de veinte sesiones, requisitos de los comandos y una comparación entre checkpoints, réplica, clúster y copias de seguridad.

The course follows AZ-802's seven-area guide rather than substituting older AZ-800/AZ-801 objectives or credential-page metadata. Reviews clarified JEA defaults on domain controllers, WinRM second-hop limits, supported File Sync recovery, Windows Server 2025 OSConfig restarts/removal, QUIC editions and certificates, and source-to-workspace monitoring. SnapshotType inventory is explicitly separated from proof of production consistency.

AZ-802 está integrado en el entrenador, Anki y el mini simulacro. El total pasa a diecisiete rutas, 170 casos abiertos por idioma y 34 preguntas de opción múltiple. Las 110 pruebas locales pasan; un trabajo independiente de Windows analiza la sintaxis de los 72 bloques PowerShell sin ejecutarlos. El registro de validación distingue esas comprobaciones de una práctica real en Windows o Azure.

[Guía de AZ-802](certifications/es/AZ-802.md) · [Casos](certifications/es/AZ-802-cases.md) · [Cuaderno](certifications/es/AZ-802-workbook.md)
