# DP-900 · Cuaderno avanzado común

[Guía](DP-900.md) · [Diez casos](DP-900-cases.md) · [Índice](README.md)

Cinco unidades equivalentes en los ocho idiomas. Utiliza datos sintéticos y separa predicciones y observaciones. Estos ejercicios no despliegan Azure ni demuestran cobertura completa del examen.

<a id="dp-900-unit-1"></a>

## 1. Describir los datos antes de elegir almacén

Inventaría un PDF, una fila de matrícula, un JSON con metadatos opcionales y un evento de descarga. Para cada uno, describe estructura, identificador, productor, consumidor, retención y campos sensibles. Después escribe la operación importante: recuperar un archivo, registrar una matrícula o agregar eventos. Separa la elección del formato del requisito de la carga.

**Caso:** alguien propone una sola base porque los cuatro conjuntos pertenecen a la misma app. **Evidencia:** matriz de cuatro filas, una alternativa descartada por fila y una condición nueva que podría cambiar la elección. No inventes límites de servicio ni supongas que cualquier JSON necesita Cosmos DB.

<a id="dp-900-unit-2"></a>

## 2. Hacer visible la integridad relacional

Dibuja Estudiantes, Asignaturas y Matrículas con identificadores estables. Crea seis filas sintéticas y explica claves primarias, referencias y una regla que impida matrículas duplicadas. Predice el resultado de un join. Después cambia el título de una asignatura y compara los cambios necesarios con un diseño que copiaba el título en cada matrícula. Queremos mostrar una anomalía concreta, no recitar un lema de normalización.

**Caso:** un estudiante figura matriculado en una asignatura inexistente. **Evidencia:** regla que debe rechazarlo o detectarlo, registro inválido de ejemplo y resultado esperado. Si ejecutas SQL local, identifica el motor: el comportamiento de SQLite local no prueba Azure SQL.

<a id="dp-900-unit-3"></a>

## 3. Decidir quién opera la base

Compara Azure SQL Database, Managed Instance y SQL Server en VM para una app nueva y una migración. Enumera dependencias de compatibilidad, red e identidad, mantenimiento y expectativas de recuperación. Añade una opción de motor de código abierto si la aplicación existente lo exige. Separa una recomendación justificada de afirmar que un producto es siempre mejor.

**Caso:** el inventario de migración incluye un componente que necesita acceso al sistema operativo invitado. **Evidencia:** preguntas de compatibilidad, tabla de responsabilidades y plan de prueba de concepto con criterios de éxito. No hace falta desplegar: señala qué supuestos siguen pendientes de comprobar antes de aceptar el destino.

<a id="dp-900-unit-4"></a>

## 4. Conciliar una canalización pequeña

Prepara seis eventos sintéticos de descarga: incluye un identificador duplicado y un registro sin asignatura. Define entrada válida, evento único y condición de finalización. Dibuja una ruta ETL y otra ELT, situando la validación y el almacén de rechazados en ambas. Explica cuándo un lote satisface el retraso permitido y cuándo podría justificarse streaming.

**Caso:** el total del panel no coincide con las filas del origen. **Evidencia:** recuentos de origen, duplicados, rechazados y aceptados con explicación reproducible. Asigna responsable y respuesta para una ejecución fallida. Un estado de canalización correcto no demuestra que sus totales de negocio lo sean.

<a id="dp-900-unit-5"></a>

## 5. Definir una medida analítica fiable

Elige el nivel de detalle del informe, por ejemplo un evento de descarga completada, y define un hecho con contexto de asignatura y fecha. Especifica zona horaria, tratamiento de eventos tardíos y frescura. Explica qué parte guarda, cuál transforma, cuál aporta el modelo semántico y cuál muestra el informe. Compara lago, almacén o lakehouse según el trabajo necesario, sin quedarte en una etiqueta comercial.

**Entrega final:** matriz de almacenamiento, esquema relacional, conciliación de canalización e informe mensual ficticio con definición de su medida. Explica los papeles de Fabric, Synapse y Power BI. Señala una duda para la guía oficial; un informe ficticio correcto no demuestra operación en la nube ni preparación suficiente para el examen.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900) · [Apuntes de datos](../../es/04-storage.md)
