# DP-300 · Cuaderno operativo común

[Guía](DP-300.md) · [Diez casos](DP-300-cases.md) · [Índice](README.md)

Cinco unidades con los mismos objetivos y evidencias en los ocho idiomas. Puedes realizar el diseño sin Azure. Separa el comportamiento esperado de lo que hayas observado. No se afirma ejecución en Azure ni cobertura completa del examen.

<a id="dp-300-unit-1"></a>

## 1. Justificar plataforma y migración

Escribe una tabla de requisitos de la app: funciones de base necesarias, acceso al sistema operativo, dependencias de instancia, interrupción de escrituras admisible, mantenimiento y recuperación. Compara SQL Database, Managed Instance y SQL Server en una VM según esos requisitos, sin premiar nombres que te resultan familiares.

**Caso:** una tarea existente depende de una herramienta del sistema operativo. **Evidencia:** indica si sigue siendo necesaria, un destino o rediseño admitido y cómo comprobar compatibilidad. **Entrega:** secuencia con transferencia inicial, parada de escrituras, validación, transición, responsable de vuelta y tratamiento de escrituras posteriores. Terminar la copia no es el criterio de aceptación.

<a id="dp-300-unit-2"></a>

## 2. Separar límites de acceso y confidencialidad

Dibuja la ruta desde la identidad de la app hasta una operación permitida sobre una tabla. Marca DNS, red, autenticación, principal de base y permisos del objeto. Separa aplicación, despliegue y administración de emergencia. Indica qué datos pueden aparecer en consultas, registros, exportaciones y copias.

**Caso:** la conexión privada funciona, pero la aplicación no puede leer su tabla. **Evidencia:** identidad, base, objeto y operación denegada; no amplíes la red pública para sustituir el diagnóstico. **Entrega:** permisos mínimos y comparación de cifrado de transporte, TDE, Always Encrypted y enmascaramiento frente a un requisito concreto. Incluye recuperación y responsables de claves.

<a id="dp-300-unit-3"></a>

## 3. Diagnosticar una regresión medida

Inventa dos periodos comparables de una consulta de permisos, con duración, lecturas, CPU, concurrencia e identidad del plan. Relaciona el cambio con una hipótesis y nombra una observación que la contradiga. Incluye bloqueos y duración de transacciones junto al historial disponible de Query Store; una métrica normal o un operador de plan que parece caro no prueban por sí solos la causa.

**Caso:** un índice mejora lecturas y empeora importaciones. **Evidencia:** resultados anteriores y posteriores de ambas operaciones con carga representativa. **Entrega:** un experimento reversible, umbrales de aceptación, pasos de vuelta y límites de la evidencia. No propongas reducir archivos o terminar todas las sesiones como mantenimiento rutinario.

<a id="dp-300-unit-4"></a>

## 4. Hacer la automatización observable y repetible

Clasifica una tarea nocturna por trabajo y plataforma. Compara SQL Agent para SQL Server o Managed Instance compatibles con Elastic Jobs para tareas T-SQL de SQL Database. Especifica identidad, destinos, calendario, tiempo máximo, presupuesto de reintentos y aviso de fallo. Las dependencias externas pueden requerir un orquestador más amplio.

**Caso:** la tarea confirma sus cambios y pierde la respuesta de éxito. **Evidencia:** explica cómo repetir sin duplicar resultados y cómo confirma la finalización un operador. **Entrega:** tabla de estados pendiente, en ejecución, completado e incierto, además de una prueba con datos sintéticos. Invocar correctamente el programador no equivale a verificar el resultado de negocio.

<a id="dp-300-unit-5"></a>

## 5. Recuperar los datos y el servicio completo

Define incidentes separados para borrado accidental y caída regional. Elige estados recuperables y mecanismos de disponibilidad según el problema que resuelven. Expresa RPO y RTO para la app e identifica permisos, capacidad de destino, endpoint, DNS, autenticación y dependencias. La replicación puede propagar un cambio confirmado no deseado.

**Caso:** el nuevo primario está sano, pero los usuarios no descargan apuntes. **Evidencia:** comprobación funcional y secuencia medida que incluya reconexión. **Entrega:** plan de validación de una restauración aislada, decisión sobre la copia válida antes del retorno y responsables de limpiar datos retenidos. Marca los tiempos como ESPERADOS hasta observarlos en un entorno adecuado: un ejercicio de mesa no mide la recuperación de Azure.

[Objetivos oficiales](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300) · [Guía y fuentes técnicas](DP-300.md)
