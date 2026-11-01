# DP-900 · 10 casos con respuestas razonadas

[Guía](DP-900.md) · [Cuaderno](DP-900-workbook.md) · [Índice](README.md)

Escenarios originales de práctica, no preguntas reales de examen. Primero identifica el requisito; después descarta una alternativa y describe la evidencia que recogerías. No se afirma haber realizado un despliegue en Azure.

## 1. La app guarda PDF y metadatos consultables de propiedad. ¿Deben ir ambos a una tabla SQL?

<details>
<summary>Razonamiento</summary>

No. Un diseño posible mantiene los PDF como objetos en Blob Storage y las relaciones de propiedad y asignatura en una base de datos. Lo importante es explicar la frontera de acceso y coherencia: la subida puede completarse y fallar la actualización de metadatos. Define un flujo recuperable y cómo detectar archivos huérfanos. Guardarlo todo en una base también podría justificarse por los requisitos, pero «todo dato debe ser una fila SQL» no es un buen punto de partida.

</details>

## 2. Un JSON contiene atributos opcionales y anidados. ¿Es no estructurado porque faltan algunos campos?

<details>
<summary>Razonamiento</summary>

JSON puede representar datos semiestructurados: las claves y el anidamiento aportan organización aunque los registros difieran. La ausencia de campos no elimina esa estructura. Separa representación, calidad y elección del almacén. Pregunta si el campo ausente es válido, desconocido o un error de ingestión, y anota cómo debe reaccionar quien lo consume. Una base documental podría encajar con el acceso previsto, pero la presencia de JSON por sí sola no resuelve esa decisión de arquitectura.

</details>

## 3. Cada matrícula repite el título y docente de la asignatura. ¿Qué fallo puede evitar la normalización?

<details>
<summary>Razonamiento</summary>

Cambiar el título podría actualizar unas matrículas y dejar otras con el valor antiguo. Mantener un registro en Asignaturas con una clave estable y referenciarlo desde Matrículas reduce esa anomalía. Explica las restricciones necesarias y cómo una consulta con join reconstruye un resultado útil. No significa prohibir toda duplicación: una instantánea analítica puede conservar descripciones históricas intencionadamente. Aclara si estamos representando la verdad transaccional actual o un modelo para consultar el pasado.

</details>

## 4. Un informe ralentiza la matriculación. ¿Mover su gráfica a Power BI elimina automáticamente la carga de la base?

<details>
<summary>Razonamiento</summary>

No. Depende de cómo obtiene y actualiza los datos el modelo. El informe podría seguir consultando el origen operativo o lanzar actualizaciones costosas. Aclara frescura, patrón de consultas y capacidad del origen antes de elegir el diseño. Una copia analítica preparada puede aislar parte del trabajo, pero añade retraso de actualización y responsabilidades de canalización. Mide la carga del origen y define «actualizado»; cambiar la herramienta de visualización no demuestra que cambie el acceso subyacente.

</details>

## 5. Una aplicación existente de SQL Server necesita componentes del sistema operativo. ¿Azure SQL Database es siempre un reemplazo directo?

<details>
<summary>Razonamiento</summary>

No. Inventaría esos componentes y las demás dependencias antes de elegir destino. Azure SQL Database, Managed Instance y SQL Server en VM tienen fronteras distintas de administración y compatibilidad. Una VM puede permitir acceso al sistema operativo, pero deja más mantenimiento al equipo. Managed Instance puede resolver ciertos requisitos de instancia sin cubrir cada dependencia externa. Prepara una lista de compatibilidad y un plan de pruebas de migración: reconocer el motor no demuestra que toda la aplicación funcione sin cambios.

</details>

## 6. Un estudiante atribuye claves externas a Azure Table Storage porque se llama Table. ¿Cómo corregirías el diseño?

<details>
<summary>Razonamiento</summary>

Table Storage almacena entidades no relacionales; no es un servicio SQL relacional administrado. Su nombre no justifica asumir joins relacionales ni restricciones de clave externa. Identifica lecturas, actualizaciones, relaciones y necesidades de coherencia reales, y compara un modelo de entidades adecuado con otro relacional. Una evidencia útil es un ejemplo resuelto: muestra cómo una matrícula recupera su asignatura y cómo se previenen o detectan referencias inválidas. Los nombres ayudan a investigar, pero no sustituyen las capacidades.

</details>

## 7. Un lote nocturno entrega el informe a la mañana siguiente. ¿Conviene sustituirlo por streaming para modernizarlo?

<details>
<summary>Razonamiento</summary>

Empieza por el retraso que admite el negocio. Si un lote fiable entrega el resultado a tiempo, el streaming puede añadir trabajo operativo sin cambiar las decisiones de los usuarios. Si el personal debe reaccionar a una sobrecarga en minutos, evalúa una ruta de menor latencia para ese requisito. En ambos casos hay que tratar duplicados, entradas incompletas y reintentos. Compara frescura de extremo a extremo y recuperación ante fallos, no solo la frecuencia de un componente.

</details>

## 8. Se cargan datos brutos en un almacén y allí se limpian. ¿Es ETL y podemos omitir la validación?

<details>
<summary>Razonamiento</summary>

Ese orden corresponde a ELT: primero cargar y después transformar con las capacidades de procesamiento del destino. ETL transforma antes de cargar en el destino previsto. Ninguno elimina contratos de datos y comprobaciones. Define dónde van los registros inválidos, qué transformaciones pueden repetirse y cómo conciliar los totales aceptados con el origen. Controla también el acceso a datos brutos restringidos, aunque el analista solo vea un modelo limpio; una interfaz fácil no demuestra que los registros subyacentes sean correctos o seguros.

</details>

## 9. Un panel cuenta eventos de descarga, pero los reintentos repiten identificadores. ¿COUNT(*) equivale necesariamente a descargas completadas?

<details>
<summary>Razonamiento</summary>

Solo si la definición de los datos convierte cada fila contada en una descarga completada. Las entregas duplicadas pueden inflar COUNT(*). Define evento de negocio, identificador estable, condición de finalización e intervalo del informe; después elimina duplicados o agrega según esa definición. Conserva un recuento de duplicados o rechazados para explicar el ajuste. Prueba con pocos datos, incluido un identificador repetido y una descarga incompleta. Una gráfica plausible no demuestra que mida la pregunta prevista.

</details>

## 10. Seis registros de asignatura encajan en documentos. ¿Demuestra eso que Cosmos DB es el único almacén razonable?

<details>
<summary>Razonamiento</summary>

No. Muchos servicios pueden guardar seis registros; el ejemplo solo demuestra que pueden representarse. Compara consultas previstas, relaciones, actualizaciones, coherencia, necesidades operativas y conocimientos del equipo. Una base relacional podría resultar más sencilla cuando dominan restricciones y entidades relacionadas; un modelo documental podría encajar en otros patrones. Documenta un motivo de tu elección y una condición que la cambiaría. Preparar fundamentos debería desarrollar ese razonamiento, sin asignar un producto a cualquier ejemplo con aspecto de JSON.

</details>

Fuentes: [objetivos oficiales](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900), [Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview), [Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction), [ETL/ELT](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl), [Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview).
