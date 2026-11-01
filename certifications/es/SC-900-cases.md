# SC-900 · 10 casos con respuestas razonadas

[Guía](SC-900.md) · [Cuaderno](SC-900-workbook.md) · [Índice](README.md)

Escenarios de estudio propios, no preguntas oficiales. Identifica el requisito, descarta una alternativa y explica qué evidencia necesitarías. Todos los ejemplos son hipotéticos; no se hicieron cambios de tenant ni pruebas en Azure.

## 1. La aplicación pasa a un servicio administrado. ¿Puede el equipo dejar de revisar los permisos de documentos?

<details>
<summary>Razonamiento</summary>

No. El proveedor opera partes de la plataforma, mientras que nuestra organización sigue determinando el acceso adecuado a sus datos. Dibujaría el modelo de servicio separando operación de plataforma, identidad, compartición y configuración de aplicación. Una declaración de cumplimiento del proveedor no demuestra que nuestros documentos sin publicar sean privados. La evidencia útil incluiría el ámbito de compartición configurado y una comprobación de las operaciones permitidas y denegadas previstas, realizada únicamente en un entorno de pruebas autorizado.

</details>

## 2. Un estudiante inicia sesión, pero no puede abrir la carpeta privada de una asignatura. ¿Falla la autenticación?

<details>
<summary>Razonamiento</summary>

No necesariamente. La autenticación puede funcionar mientras la autorización deniega correctamente el acceso a un recurso concreto. Comprueba qué identidad inició sesión realmente, sus grupos, el permiso que requiere la carpeta y las políticas aplicables. Darle un rol administrativo eludiría el diagnóstico y excedería la necesidad. En el ejercicio de diseño, registra la decisión de acceso esperada y la evidencia que permitiría distinguir un error de autenticación de una denegación por permisos de aplicación o recurso.

</details>

## 3. Un equipo propone una contraseña seguida de otra contraseña como MFA. ¿Qué falta?

<details>
<summary>Razonamiento</summary>

Ambos secretos pertenecen a la categoría de conocimiento, por lo que utilizar dos no establece factores de autenticación diferentes. Elige un método y una política compatibles con los factores o la intensidad de autenticación requeridos. Considera también resistencia al phishing, registro, compatibilidad del dispositivo y recuperación. Una captura de la página de registro no demuestra aplicación efectiva. Describiría un inicio de sesión que exija el método configurado y otro en el que un método insuficiente no satisfaga el requisito.

</details>

## 4. Un documento descargado tiene el hash esperado. ¿Demuestra quién lo subió o mantiene su contenido secreto?

<details>
<summary>Razonamiento</summary>

No. Comparar un resumen adecuado ayuda a comprobar si el contenido coincide con la referencia esperada. No cifra el archivo ni establece que la referencia venga de un origen fiable. La confidencialidad necesita acceso adecuado y, cuando corresponda, cifrado; asegurar el origen necesita un mecanismo fiable para ese flujo, como una firma verificada. Explica primero de dónde procede el hash esperado. Si un atacante puede sustituir archivo y referencia, que coincidan aporta mucha menos garantía de la que supone el equipo.

</details>

## 5. Una política de acceso condicional exige MFA para finanzas. ¿Quedan cubiertas todas las aplicaciones de la universidad?

<details>
<summary>Razonamiento</summary>

La conclusión supera el ámbito de la política. Revisa identidades, aplicaciones, condiciones, exclusiones y controles de concesión incluidos. La regla de finanzas puede ser correcta mientras otras aplicaciones quedan fuera. Después de esa decisión siguen aplicándose los permisos de la aplicación. Prepararía una matriz de resultados esperados para distintos usuarios y aplicaciones, con recuperación del administrador y dependencias, antes de cualquier implantación autorizada. El análisis en modo de solo informe ayuda a revisar, pero sus observaciones no equivalen a un bloqueo aplicado.

</details>

## 6. Un administrador es elegible para un rol privilegiado, pero todavía no puede operar. ¿Está fallando PIM?

<details>
<summary>Razonamiento</summary>

La elegibilidad puede exigir una activación antes de utilizar los permisos privilegiados. Comprueba el rol y ámbito previstos, los requisitos de activación, duración, estado de aprobación y asignación realmente activa. No asignes permanentemente un rol más amplio solo para hacer desaparecer el error. PIM modifica cuándo están disponibles los privilegios; no vuelve mínimo un rol inadecuado. La evidencia útil es la activación aprobada y una operación acotada con la identidad prevista, no únicamente la existencia de una asignación elegible.

</details>

## 7. Una antigua integrante del proyecto conserva acceso. ¿Corresponde una revisión de acceso o una detección de ID Protection?

<details>
<summary>Razonamiento</summary>

La pregunta inmediata es si un permiso existente sigue justificado, lo que encaja con una revisión de acceso y el proceso de altas, cambios y bajas de la organización. ID Protection trata señales de riesgo de identidad y no decide todas las necesidades de negocio de una carpeta. Investiga aparte comportamientos sospechosos si existe evidencia. Identifica al dueño del recurso, el origen del permiso y si retirarlo afectaría a otros proyectos. Registra la decisión y la evidencia necesaria para confirmar la retirada del acceso obsoleto.

</details>

## 8. Un correo malicioso y una alerta podrían estar relacionados, pero el dispositivo no envía telemetría. ¿Qué falta primero?

<details>
<summary>Razonamiento</summary>

Relacionar señales requiere datos de las fuentes correspondientes. Comprueba producto compatible, licencia, incorporación, correspondencia de identidades y llegada de eventos a la plataforma de investigación. Defender XDR no puede reconstruir toda la evidencia ausente del dispositivo porque exista otra alerta. Sentinel puede añadir análisis entre fuentes conectadas, pero también necesita ingesta y reglas útiles. Documentaría qué eventos existen, qué falta y una hipótesis acotada que comprobar antes de afirmar que el panel representa todo el ataque.

</details>

## 9. Un documento lleva la etiqueta Confidencial, pero admite compartirlo fuera. ¿Demuestra un fallo del producto?

<details>
<summary>Razonamiento</summary>

El nombre de la etiqueta no establece su protección configurada ni la regla aplicada a esa vía de compartición. Comprueba ajustes de etiqueta, carga compatible, publicación y ámbito, además de condiciones y acciones de DLP. Una etiqueta solo clasificatoria puede ser válida sin bloquear el envío. Define los casos permitidos y bloqueados previstos antes de investigar. Usa contenido sintético en una prueba autorizada; no distribuyas datos confidenciales reales solo para demostrar si una política funciona.

</details>

## 10. Una investigación necesita actividad del mes pasado y mensajes preservados. ¿Auditoría equivale a retención o backup?

<details>
<summary>Razonamiento</summary>

Estas capacidades tienen propósitos diferentes. Auditoría aporta evidencia de actividad dentro de su disponibilidad y retención configuradas. La retención de contenido regula su conservación o eliminación, mientras que eDiscovery puede ayudar a localizar y preservar material relevante para una investigación. Un backup aborda necesidades de recuperación y no se obtiene automáticamente con esas herramientas. Determina fuentes, fechas, permisos, requisitos de retención y preservación, y responsable. No prometas evidencia nunca recopilada ni contenido que ya quedó fuera de la retención aplicable.

</details>

[Guía oficial](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) · [Fuentes técnicas y explicaciones](SC-900.md)
