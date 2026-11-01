# SC-200 · Cuaderno de decisiones y evidencia

[Guía](SC-200.md) · [Diez casos](SC-200-cases.md) · [Índice](README.md)

Cinco unidades originales para una aplicación universitaria ficticia de apuntes. Trabaja sin conexión con registros e identificadores inventados. Separa los resultados esperados de las observaciones proporcionadas. No se requiere ni se afirma acceso a un tenant, despliegue, consulta real, envío de mensajes o contención.

<a id="sc-200-unit-1"></a>

## 1. Dibujar los límites de recopilación y acceso

Dibuja Microsoft 365, una aplicación de Azure, un servidor local y un firewall del campus. Asigna investigación de Defender XDR o recopilación y análisis de Sentinel según corresponda. Para cada fuente, especifica incorporación, requisitos del conector, tabla y columna temporal esperadas, identificadores estables, retraso, retención y responsable. Separa permisos de lectura, gestión de incidentes, autoría de reglas y automatización.

**Escenario:** el conector del firewall parece conectado, pero falta el evento necesario. **Evidencia:** tabla de cuatro fuentes, pregunta sobre el estado de recopilación y evento sintético con esquema esperado. **Entrega:** diagrama y lagunas que expliquen qué puede concluirse. Incluye normas de datos personales y exportación; no recopiles información real del alumnado.

<a id="sc-200-unit-2"></a>

## 2. Construir una cronología justificable del incidente

Inventa seis registros de correo, identidad, endpoint, aplicación y carga de nube. Asigna a cada uno hora UTC del evento, hora de ingesta, identificador de origen, identificadores de entidades y observación. Agrupa alertas relacionadas en un incidente propuesto sin asumir que compartir una IP del campus demuestra relación. Separa alcance conocido, sospechado y telemetría no disponible.

**Escenario:** un mensaje sospechoso precede a un aparente acceso privado. **Evidencia:** cronología, mapa de entidades, explicación alternativa y registro ausente solicitado. **Entrega:** nota inicial con responsable, motivo de prioridad, contención propuesta, autorización necesaria, impacto y condición de recuperación. Marca cada acción como no ejecutada; la confirmación esperada no es una respuesta observada.

<a id="sc-200-unit-3"></a>

## 3. Explicar los resultados antes de confiar en los recuentos

Lee los datos sintéticos fijos de KQL de la guía. Sigue las filas por el intervalo UTC semiabierto, filtro Denied, eliminación de duplicados y agregación. Explica por qué se esperan dos eventos de `student-a`. Añade otra tabla inventada con dos filas de esa cuenta y dibuja las parejas de una unión interna explícita. Contrástala con la eliminación de duplicados de la izquierda del tipo predeterminado `innerunique`.

**Escenario:** un informe confunde filas unidas con ataques distintos. **Evidencia:** recuentos intermedios, claves, supuestos sobre identificadores y ejemplo del límite temporal. **Entrega:** interpretación corregida con salida esperada y limitaciones. No se afirma ejecución; cualquier cálculo local opcional se distingue de observaciones de un tenant.

<a id="sc-200-unit-4"></a>

## 4. Convertir una hipótesis de búsqueda en una revisión de ajustes

Escribe una hipótesis que relacione recibir un mensaje sospechoso con acceder de forma inusual a archivos privados. Define población, intervalo UTC, fuentes necesarias y explicación alternativa. Crea cuatro ejemplos sintéticos benignos y cuatro preocupantes, etiquetados. Propón una detección y excepción acotada; identifica qué ejemplos alertarían, se omitirían o necesitarían contexto. Explica cómo ASIM podría normalizar fuentes compatibles y qué asignaciones requieren validación.

**Escenario:** una importación autorizada parece un uso indebido. **Evidencia:** tabla de decisiones versionada, lagunas, análisis de falsos positivos y negativos, y comprobación del analizador. **Entrega:** recomendación de ajuste. Una búsqueda vacía y menos alertas no demuestran ausencia de intrusión ni cobertura completa.

<a id="sc-200-unit-5"></a>

## 5. Revisar un flujo de respuesta asistida

Esboza una regla que invoque un playbook para ampliar información y solicite aprobación antes de una contención con impacto. Identifica por separado operador, permiso de invocación de Sentinel, identidad del flujo y alcance posterior. Simula un disparador duplicado y un tiempo de espera agotado; documenta identificadores y comprobaciones que eviten tickets duplicados o restricciones repetidas innecesarias. Incluye responsable y recuperación.

**Escenario:** un resumen de IA vincula una alerta de nube con una descarga sin registro de aplicación. **Evidencia:** tabla de afirmaciones y fuentes, conclusión corregida, límite de aprobación y comportamiento esperado del reintento. **Entrega:** procedimiento de mesa revisado. Verifica sugerencias de Copilot con los registros y semántica de consulta. No se envía ninguna notificación, solicitud ni respuesta real.

[Guía oficial de estudio](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · [Fundamentos de observabilidad](../../es/08-observability.md)
