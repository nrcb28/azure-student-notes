# DP-700 · Diez casos con respuestas razonadas

[Guía](DP-700.md) · [Cuaderno](DP-700-workbook.md) · [Índice](README.md) · [English](../en/DP-700-cases.md)

Ejercicios originales con datos universitarios, no preguntas oficiales del examen. Expón tu decisión y las evidencias antes de abrir cada respuesta. La [guía](DP-700.md) documenta el alcance oficial y la comprobación de fuentes; estos casos no afirman cobertura completa ni ejecución en Fabric.

## 1. El equipo conoce Synapse Spark. ¿Puede suponer los mismos valores predeterminados y despliegues en Fabric?

<details>
<summary>Respuesta</summary>

No. Conocer Spark ayuda, pero Fabric es una plataforma SaaS con sus propios límites de área de trabajo, capacidad, elementos, ejecución y ciclo de vida. Inventaría dependencias, bibliotecas, rutas, identidades y configuraciones admitidas antes de adaptar el cuaderno. Define una pequeña carga de matrículas sintéticas y compara la salida esperada con una futura ejecución controlada en Fabric. Verifica el despliegue y las conexiones por separado de la sintaxis de transformación. Un código parecido sirve como punto de partida, pero no demuestra equivalencia de permisos, valores predeterminados o responsabilidades operativas.

</details>

## 2. Un equipo de informes relacionales y otro de archivos proponen el mismo almacén. ¿Qué decide?

<details>
<summary>Respuesta</summary>

Compara la carga real: formatos de archivo, motores de transformación, requisitos de escritura relacional, consumo SQL, gobierno y responsables. Un lakehouse es un candidato razonable para preparar archivos de descargas con Spark; un warehouse puede encajar con un modelo analítico centrado en T-SQL. Pueden colaborar cuando lo justifiquen los requisitos. Define la granularidad de las tablas y la actualización aceptable antes de comparar rendimiento. No trates el punto de conexión SQL del lakehouse como una superficie general de escritura de warehouse. Documenta operaciones admitidas y una validación representativa, sin elegir solo por familiaridad.

</details>

## 3. Un acceso directo expone el catálogo de la biblioteca. ¿Aporta respaldo y acceso para todos los analistas?

<details>
<summary>Respuesta</summary>

No. El acceso directo referencia datos del origen; un destino ausente o un permiso modificado puede afectar al acceso. No es una copia independiente conservada para recuperarse. Comprueba si es interno o externo, qué identidad o conexión utiliza y qué permisos rigen la ruta real de lectura. Prueba con datos sintéticos un analista autorizado y otro denegado. Acuerda los cambios de esquema y la disponibilidad con el responsable del catálogo. Hace falta un diseño separado de conservación y recuperación si se exige recuperar estados históricos.

</details>

## 4. Un informe debe incluir solo las matrículas de ayer. La actividad de copia figura como correcta, pero aparecen matrículas de hoy. ¿Ha tenido éxito el flujo completo?

<details>
<summary>Respuesta</summary>

La actividad terminó técnicamente, pero falló la condición de aceptación del negocio. Revisa parámetros del intervalo, expresiones dinámicas, filtros de origen, zonas horarias y enlaces de destino. Concilia recuentos del intervalo de origen y claves de negocio seleccionadas con la salida publicada antes de permitir la actualización posterior. Una canalización debe coordinar validación y publicación; un cuaderno o SQL puede implementar las reglas. Registra la ejecución y el intervalo previsto para rastrear el error. Corrige la salida mediante repetición idempotente, sin suponer que el estado correcto demuestra exactitud.

</details>

## 5. Un lote se confirmó, pero perdió la respuesta de éxito. ¿Cómo evita duplicados un reintento?

<details>
<summary>Respuesta</summary>

Utiliza una clave de matrícula estable y una versión de origen determinista, deduplica el lote entrante y combina para alcanzar el estado de destino previsto. Guarda el progreso solo tras validar y confirmar la salida. Repetir el mismo intervalo acotado debe encontrar versiones equivalentes ya aplicadas y conservar los totales. Registra un identificador de lote y recuentos de conciliación para diagnosticar. Añadir todas las llegadas sin unicidad duplicaría filas. Considera también actualizaciones antiguas retrasadas y eliminaciones: la estrategia debe conservar el orden de versiones, además de reconocer contenidos idénticos.

</details>

## 6. Una consulta por fecha de modificación omite bajas y correcciones tardías. ¿Cómo cambia la carga?

<details>
<summary>Respuesta</summary>

Determina si las bajas eliminan físicamente filas o cambian un estado. Consultar las filas restantes no permite descubrir eliminaciones físicas. Evalúa CDC compatible con registros de eliminación, un contrato de borrado lógico o conciliaciones periódicas. Para correcciones tardías, usa un orden fiable del origen y un intervalo solapado con deduplicación determinista, u otro mecanismo admitido de seguimiento. Conserva versiones suficientes para rechazar cambios antiguos tras una eliminación. Prueba marcas de tiempo iguales, retrasos y repeticiones. Documenta la conservación del origen para que una interrupción prolongada no genere silenciosamente una pérdida irrecuperable.

</details>

## 7. Una descarga ocurre a las 23:59 y llega a las 00:07. ¿A qué día corresponde?

<details>
<summary>Respuesta</summary>

La respuesta depende de la regla temporal declarada. Si los informes cuentan por tiempo del evento, el registro pertenece a la ventana del día anterior. Define zona horaria, límites, demora tolerada y si se puede corregir un resultado publicado. Agrupar por tiempo de procesamiento lo asignaría al día de llegada y respondería otra pregunta. Una marca de agua de streaming controla eventos tardíos y estado retenido; un punto de control ayuda a recuperar el progreso. Ninguno sustituye una política de corrección ni demuestra que el destino no duplicará la salida al repetir.

</details>

## 8. Llega una columna opcional junto con fechas inválidas y claves de asignatura desconocidas. ¿Se acepta todo?

<details>
<summary>Respuesta</summary>

Evalúa la columna opcional como cambio de compatibilidad, por separado de la validez de los registros. Aprobar un campo añadido no vuelve aceptables fechas inválidas ni referencias inexistentes. Aplica reglas explícitas de tipos y claves, conserva las entradas inválidas en cuarentena controlada con motivos y concilia registros aceptados y rechazados. Una asignatura desconocida puede necesitar resolución diferida en vez de rechazo permanente. Conserva identificadores para reparar y repetir con seguridad. Comprueba contratos posteriores antes de publicar el esquema y evita incluir detalles estudiantiles en registros diagnósticos sin restricciones.

</details>

## 9. Un informe aplica seguridad de filas y una etiqueta de confidencialidad. ¿Protege automáticamente los archivos?

<details>
<summary>Respuesta</summary>

No. Identifica dónde se aplica la restricción de filas y examina otras rutas, como consultas SQL y acceso directo a OneLake. Roles del área de trabajo, permisos de elementos, reglas del motor y permisos de archivos deben ajustarse a la capacidad requerida del lector. Una etiqueta aporta contexto de gobierno y protecciones admitidas; su presencia no demuestra todos los requisitos de autorización. Prueba totales por asignatura permitidos y detalles estudiantiles denegados con identidades representativas. Revisa también exportaciones y accesos amplios heredados, que pueden debilitar la superficie restringida del informe.

</details>

## 10. Un cuaderno desplegado va más lento y desde pruebas lee producción. ¿Primero aumentamos capacidad?

<details>
<summary>Respuesta</summary>

Primero corrige el enlace del entorno e impide publicaciones indebidas. Revisa referencias de conexión, parámetros, identidad de ejecución y compatibilidad de despliegue del elemento y sus dependencias. El historial Git o una promoción correcta no prueban estos valores. Después compara la misma carga con una referencia: contención de capacidad, sesgo en Spark, redistribución, tamaños de archivo, poda de particiones y comportamiento del origen. Prueba un cambio basado en evidencias con comprobaciones de corrección. Aumenta capacidad cuando la presión medida lo justifique, sin ocultar errores de configuración o una distribución ineficiente.

</details>
