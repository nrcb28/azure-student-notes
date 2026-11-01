# SC-200 · 10 casos con respuestas razonadas

[Guía](SC-200.md) · [Cuaderno](SC-200-workbook.md) · [Índice](README.md)

Escenarios de estudio originales, no preguntas oficiales. Usa la aplicación universitaria ficticia de apuntes y registros sintéticos. Identifica el requisito, descarta una alternativa tentadora y señala la evidencia ausente. Son ejercicios de mesa sin conexión; no se ejecutan consultas en un tenant, mensajes ni acciones de respuesta.

## 1. Las alertas de Microsoft 365 aparecen en Defender XDR, pero falta el firewall del campus. ¿XDR ya lo cubre?

<details>
<summary>Respuesta</summary>

No. La evidencia de Microsoft 365 no demuestra cobertura del firewall. Identifica su vía de exportación compatible y el análisis necesario; después evalúa un conector de Sentinel adecuado y sus requisitos. La correlación de Defender XDR y la recopilación de Sentinel cumplen funciones relacionadas, pero ninguna inventa telemetría ausente. Pediría la tabla prevista, esquema, identificadores de origen, alcance y horas de llegada de ejemplo. El resultado del ejercicio es un mapa de fuentes presentes y ausentes que distingue la ingesta esperada de las observaciones aportadas.

</details>

## 2. Un conector indica Conectado, pero una consulta no devuelve filas del dispositivo. ¿Debe cerrarse la investigación?

<details>
<summary>Respuesta</summary>

No. Comprueba la incorporación del dispositivo, licencias, requisitos del servicio, eventos seleccionados, tabla de destino, permisos, intervalo UTC, retraso de ingesta y retención. La tabla podría tener campos distintos de los supuestos por la consulta. Conectado indica configuración; no demuestra la llegada de cada evento necesario. Cerrar el caso confundiría falta de visibilidad con comportamiento benigno. Registra qué evidencia falta y solicita al responsable de la fuente una muestra sintética acotada y evidencia del estado de recopilación antes de concluir.

</details>

## 3. Tres alertas comparten una IP del campus. ¿Basta para unirlas en un ataque confirmado?

<details>
<summary>Respuesta</summary>

Compartir una IP es una pista, especialmente si el campus usa traducción de direcciones de red, pero no identifica a una sola persona o atacante. Compara identificadores estables de cuentas y dispositivos, evidencia de mensajes o archivos, tipos de actividad y horas UTC. Las alertas son detecciones; un incidente agrupa evidencia relacionada y una entidad es un objeto implicado. Propondría correlacionarlas solo con relaciones que lo respalden y documentaría la incertidumbre. Hace falta una cronología y un mapa de entidades que contemplen estudiantes sin relación compartiendo dirección pública.

</details>

## 4. Una alerta de endpoint afecta al servidor de retransmisión de clases. ¿Puede aislarlo inmediatamente el estudiante analista?

<details>
<summary>Respuesta</summary>

La alerta por sí sola no concede autoridad de contención. Conserva la evidencia, evalúa actividad actual y alcance probable, y consulta el procedimiento del incidente y a quien puede decidir. El aislamiento podría interrumpir clases: documenta impacto, límite propuesto, alternativas y recuperación. Esperar sin escalar tampoco basta si hay indicios de una amenaza en curso. En este ejercicio, registra la escalación y acción propuesta sin ejecutarla. Para considerarla completada harían falta una autorización registrada y evidencia separada que confirme el resultado previsto.

</details>

## 5. La consulta sintética de la guía contiene tres filas Denied. ¿Por qué el recuento esperado es dos?

<details>
<summary>Respuesta</summary>

Los datos repiten el mismo par de `EventId` y cuenta para `e1`. Tras el filtro UTC, `distinct EventId, Account` conserva una copia del par y `e2`; la agregación espera dos eventos de `student-a`. Depende del supuesto explícito de identificador estable. Eliminar duplicados solo por cuenta reduciría eventos distintos a uno y produciría un recuento insuficiente. El evento Allowed también coincide con el límite superior excluido. Es una predicción al leer filas sintéticas, no evidencia de ejecutar la consulta en un tenant.

</details>

## 6. Al unir mensajes e inicios de sesión por cuenta se duplica el recuento. ¿Hubo el doble de ataques?

<details>
<summary>Respuesta</summary>

No necesariamente. Varios mensajes y varios inicios de sesión de una cuenta pueden producir múltiples parejas coincidentes. Declara el tipo de unión, unicidad de claves y relación que intentas demostrar. El tipo predeterminado `innerunique` también modifica la entrada izquierda al eliminar claves duplicadas y podría perder distinciones necesarias. Examina la cardinalidad de ambas entradas y añade una relación temporal adecuada antes de interpretar el resultado. Conservaría los identificadores originales y compararía las parejas esperadas en datos sintéticos pequeños, sin equiparar filas unidas con ataques.

</details>

## 7. Una búsqueda no encuentra accesos privados después de un correo sospechoso. ¿Puede afirmarse que nunca se comprometió la cuenta?

<details>
<summary>Respuesta</summary>

La afirmación supera la evidencia. Informa de que la consulta no encontró registros disponibles coincidentes para la población e intervalo UTC definidos. Comprueba si había auditoría de aplicación, dispositivos incorporados, registros dentro de retención y permisos para leerlos. Revisa también filtros y significado de los eventos de acceso. Un cambio autorizado de dispositivo es una explicación alternativa de actividad desde uno desconocido. Conserva hipótesis, versión, lagunas y siguiente pregunta, en vez de tratar la ausencia de coincidencias como prueba de seguridad.

</details>

## 8. Una importación masiva de cursos genera alertas repetidas. ¿Conviene excluir a todo el profesorado?

<details>
<summary>Respuesta</summary>

Una exclusión amplia podría ocultar actividad de cuentas docentes comprometidas. Identifica primero la cuenta autorizada concreta, carga, patrón horario y evidencia de auditoría de la importación. Compara eventos sintéticos etiquetados de importación con accesos preocupantes a soluciones sin publicar. Propón una excepción acotada o ajuste y evalúa falsos positivos y negativos. Revisa también solapamiento de programación, período retrospectivo, agrupación y supresión antes de culpar al umbral. Conserva resultados esperados y versión; reducir el volumen de alertas no demuestra por sí solo una mejor detección.

</details>

## 9. Un reintento del playbook abriría otro ticket y restringiría de nuevo la misma cuenta. ¿Qué falta?

<details>
<summary>Respuesta</summary>

Faltan idempotencia y un modelo claro de estados. Asocia el flujo con identificadores estables de incidente y acción, comprueba si el paso previsto ya terminó y gestiona fallos parciales sin repetirlo a ciegas. Verifica por separado los roles del operador, el permiso de Sentinel para invocar el playbook y el alcance de la identidad del flujo. Las restricciones con impacto necesitan aprobación y recuperación según el procedimiento. En esta revisión sin conexión, simula sobre papel un disparador duplicado y un tiempo de espera agotado; no despliegues ni ejecutes nada.

</details>

## 10. Copilot dice que una alerta de nube demuestra que student-a descargó soluciones. ¿Basta su resumen como evidencia?

<details>
<summary>Respuesta</summary>

No. Contrasta la afirmación con registros de acceso de aplicación, identificador del recurso, identidades y cronología UTC. Una alerta de carga o recomendación de postura no demuestra por sí sola una descarga concreta. Revisa fuentes citadas, integraciones disponibles y esquema, filtros, uniones y recuentos de cualquier consulta generada. Señala afirmaciones sin respaldo y conserva la conclusión corregida del analista. El expediente debe distinguir evidencia sintética observada, relación inferida y registros ausentes. Un resumen fluido no aporta telemetría inexistente ni autoriza respuestas.

</details>

[Guía oficial de estudio](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · [Fuentes técnicas y explicaciones](SC-200.md)
