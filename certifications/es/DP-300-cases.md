# DP-300 · 10 casos con respuestas razonadas

[Guía](DP-300.md) · [Cuaderno](DP-300-workbook.md) · [Índice](README.md)

Ejercicios propios, no preguntas oficiales. Antes de abrir una respuesta, identifica la condición, propone una decisión y describe qué evidencias buscarías. No se afirma ejecución en Azure ni cobertura completa del examen.

## 1. Una aplicación necesita una extensión compatible a nivel del sistema operativo. ¿Basta con que SQL Database admita T-SQL para elegirlo?

<details>
<summary>Razonamiento</summary>

No. El requisito del sistema operativo cambia el límite del alojamiento. Comprueba si la extensión es imprescindible y si existe una alternativa admitida en un servicio administrado. Si sigue haciendo falta control del sistema, evalúa SQL Server en una VM e incluye actualizaciones, copias, monitorización y disponibilidad. La evaluación debe cubrir dependencias externas a los objetos de la base, además de T-SQL. Verifica el requisito real: compartir sintaxis SQL no demuestra compatibilidad del despliegue.

</details>

## 2. La migración termina correctamente. ¿Se pueden reabrir las escrituras de inmediato?

<details>
<summary>Razonamiento</summary>

Terminar la transferencia es solo una comprobación. Valida el estado final previsto, totales de negocio importantes, permisos, recorridos de la app y tareas programadas. Determina cuándo se detuvieron las escrituras de origen y si se aplicaron los últimos cambios. Declara el destino como fuente válida antes de reabrir tráfico. El plan de vuelta debe contemplar escrituras creadas después del cambio: reconectar al origen podría descartarlas. Usa criterios explícitos y registra qué comprobaciones se observaron realmente.

</details>

## 3. La app resuelve la dirección SQL privada y conecta, pero SELECT se deniega. ¿Hay que abrir más la red?

<details>
<summary>Razonamiento</summary>

La conexión correcta y la sentencia denegada apuntan a autorización en la base, no a un fallo general de red. Confirma principal autenticado, base, objeto y operación. Revisa los permisos aplicables y concede la capacidad mínima necesaria mediante el modelo de acceso elegido. Ser Contributor en Azure no concede automáticamente acceso a tablas. Abrir el endpoint público cambiaría la exposición sin aportar el permiso ausente. Repite la misma operación de la aplicación con la misma identidad para comprobar la hipótesis.

</details>

## 4. Se exige que los administradores de la base no vean determinados valores en claro. ¿Basta TDE?

<details>
<summary>Razonamiento</summary>

TDE protege archivos en reposo, pero por sí solo no impide que una consulta autorizada devuelva valores en claro. Examina un diseño como Always Encrypted, con clientes compatibles y claves fuera del acceso de esos administradores. Comprueba operaciones necesarias, compatibilidad de la app, recuperación de claves y responsables. El enmascaramiento dinámico no ofrece un límite de confidencialidad equivalente. Valida el modelo de amenaza con datos sintéticos y una prueba autorizada, sin asumir que todas las funciones llamadas cifrado resuelven el mismo problema.

</details>

## 5. Una consulta empeora tras una versión, pero la CPU global parece normal. ¿Qué evidencia buscarías primero?

<details>
<summary>Razonamiento</summary>

Identifica la consulta y compara planes y ejecución en periodos equivalentes usando el historial disponible de Query Store. Revisa parámetros, lecturas, esperas, bloqueos y cambios recientes de esquema o estadísticas. Una CPU agregada normal no demuestra que una transacción concreta funcione bien. Formula una hipótesis antes de cambiar el tamaño del servicio. Si pruebas un plan anterior, define éxito y reversión y observa tráfico representativo: una sola ejecución rápida no demuestra una mejora duradera.

</details>

## 6. Un índice acelera lecturas y ralentiza mucho las importaciones. ¿El cambio ha sido necesariamente un éxito?

<details>
<summary>Razonamiento</summary>

No. El índice se mantiene al modificar datos, así que hay que valorar el conjunto de la carga. Compara latencia de lectura y escritura, rendimiento, almacenamiento y planes antes y después con trabajo representativo. Comprueba si se solapa con otros índices y si una definición más estrecha o con otro orden cumpliría el requisito. Fija un umbral aceptable para importaciones y búsquedas. No mantengas un cambio solo porque la consulta de demostración se haya vuelto más rápida.

</details>

## 7. Una transacción larga bloquea consultas cortas. ¿Conviene terminar todas las sesiones bloqueadas?

<details>
<summary>Razonamiento</summary>

Busca la cadena de bloqueo y la transacción que mantiene los bloqueos relevantes antes de decidir qué interrumpir. Una sesión bloqueada suele ser un síntoma. Identifica trabajo, antigüedad, responsable y consecuencias de deshacerlo. Terminar una transacción puede exigir tiempo de rollback y afectar a la corrección de la app. En una investigación controlada, considera transacciones más cortas o un aislamiento adecuado tras entender la coherencia necesaria. Registra la evidencia y la decisión del incidente, sin ejecutar una terminación indiscriminada.

</details>

## 8. Una tarea de SQL Agent debe pasar a Azure SQL Database. ¿Se copia sin más su calendario?

<details>
<summary>Razonamiento</summary>

SQL Agent no está disponible en Azure SQL Database. Clasifica el trabajo: una tarea T-SQL compatible sobre varias bases podría encajar en Elastic Jobs; un flujo con servicios externos puede necesitar orquestación. Evalúa dependencias, identidad, descubrimiento de destinos, reintentos y avisos, no solo la hora. Una repetición no debería duplicar resultados de negocio tras una respuesta incierta. Prueba el reemplazo con datos sintéticos aislados y compara tanto el registro de ejecución como el estado producido.

</details>

## 9. Un DELETE accidental llega a la base secundaria. ¿Ha fallado la replicación?

<details>
<summary>Razonamiento</summary>

La replicación puede estar cumpliendo su configuración: llevar un cambio válido y confirmado a otra copia. Disponibilidad y recuperación histórica resuelven problemas distintos. Determina la hora del incidente y los puntos conservados, y planifica restaurar en una base aislada anterior al cambio no deseado. Valida registros perdidos y escrituras legítimas posteriores antes de decidir cómo recuperar el servicio. No asumas que sustituir todo por un estado antiguo es aceptable; hay que contemplar el trabajo válido realizado desde entonces.

</details>

## 10. La base ya ha conmutado, pero la app sigue fallando. ¿Se ha cumplido el RTO?

<details>
<summary>Razonamiento</summary>

No si el objetivo se refiere a recuperar el servicio de los usuarios. Comprueba endpoint admitido, DNS del cliente, reconexión, identidades, dependencias y tareas en el primario actual. Ejecuta una comprobación funcional con datos sintéticos y mide la recuperación desde el evento inicial definido. Registra por separado la pérdida de datos respecto al RPO. Antes del retorno, establece copia válida y sincronización. Que la base figure sana no demuestra que la app ni sus objetivos de recuperación estén restablecidos.

</details>

## Autoevaluación y fuentes

En cada caso: identifica el requisito, justifica una decisión y propone una comprobación. Es un método propio de repaso, no una puntuación oficial ni una predicción de aprobar.

[Guía oficial](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300) · [Referencias técnicas y explicaciones](DP-300.md)
