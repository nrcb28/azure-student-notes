# DP-700 · Cuaderno de ingeniería de datos sin conexión

[Guía](DP-700.md) · [Diez casos](DP-700-cases.md) · [Índice](README.md) · [English](../en/DP-700-workbook.md)

Cinco unidades con datos universitarios sintéticos. No requieren cuenta, capacidad de pago ni ejecución en Fabric. Conserva los mismos entregables en todas las ediciones. Marca resultados razonados como **ESPERADO**, observaciones locales como **OBSERVADO** y comprobaciones de plataforma no realizadas como **NO EJECUTADO**. El alcance de las fuentes y los límites de su comprobación están en la [guía](DP-700.md).

<a id="dp-700-unit-1"></a>

## 1. Dibujar el mapa de plataforma y responsables

Explica las diferencias entre inquilino, capacidad, área de trabajo, elemento, ubicación de OneLake y motor de ejecución. Dibuja el origen de matrículas, los archivos brutos de descargas, las tablas depuradas, el acceso directo al catálogo de biblioteca y el consumidor analítico. Decide dónde encajan lakehouse y warehouse, con un motivo concreto para cada elección. Declara la granularidad de cada tabla.

**Escenario:** la biblioteca controla el destino del acceso directo y cambia su política. **Evidencia:** documenta responsables, supuestos de autenticación interna o externa, permisos, contrato de esquema y efecto de eliminar el destino. **Entregable:** diagrama de dependencias y matriz de acceso. Incluye un requisito separado de conservación histórica; el acceso directo no satisface por sí solo respaldo ni recuperación.

<a id="dp-700-unit-2"></a>

## 2. Conciliar un registro incremental de cambios

Usa este registro sintético completo; `version` determina el orden autorizado del origen y `key` identifica una matrícula. Parte de un destino vacío. Conserva una marca de eliminación con versión. Reduce cada clave a su mayor versión, elimina duplicados idénticos y combina solo versiones más recientes. Los contenidos contradictorios con igual versión requieren cuarentena.

| key | version | operation | module |
|---|---:|---|---|
| E1 | 1 | upsert | CS101 |
| E2 | 1 | upsert | DB201 |
| E1 | 2 | upsert | AI301 |
| E1 | 2 | upsert | AI301 |
| E2 | 2 | delete | DB201 |
| E2 | 1 | upsert | DB201 |

**Escenario:** repite el registro tras perder la respuesta de éxito. **Evidencia esperada:** E1 sigue activa en AI301 con versión 2; E2 está eliminada con versión 2. El recuento activo es 1 tras ambas ejecuciones. **Entregable:** estados intermedios y reglas para confirmar progreso; explica por qué E2 versión 1 tardía no puede reactivarla.

<a id="dp-700-unit-3"></a>

## 3. Especificar reglas de calidad y tiempo del evento

Diseña un registro de descarga con identificador de evento, asignatura, tiempo del evento, llegada y versión del esquema. Define reglas de nulos, tipos, valores admitidos y duplicados. Explica la diferencia entre aprobar un campo opcional y aceptar registros inválidos. La cuarentena debe conservar un identificador reparable y un motivo, restringiendo el contenido sensible.

**Escenario:** un evento ocurre a las 23:59 UTC y llega a las 00:07 UTC del día siguiente; se declaran diez minutos de demora tolerada. **Evidencia esperada:** su día según el tiempo del evento es el anterior. Aceptarlo también requiere conocer la marca de agua del motor al llegar; ocho minutos de retraso de reloj no demuestran aceptación. **Entregable:** reglas de aceptación y corrección, conciliación, límites de ventanas, función del punto de control y comportamiento fuera de la demora permitida.

<a id="dp-700-unit-4"></a>

## 4. Diseñar un despliegue controlado

Describe una canalización que copia un intervalo acotado de matrículas, invoca validación y transformación y publica únicamente resultados aceptados. Elige SQL, PySpark o KQL para cada transformación pertinente y justifica el motor. Distingue el versionado Git de definiciones admitidas, el despliegue de contenido admitido y el movimiento de datos.

**Escenario:** el cuaderno de pruebas sigue apuntando al lakehouse de producción. **Evidencia:** inspecciona referencias de elementos, enlace de conexión, identidad, parámetros, dependencias de entorno y programaciones antes de ejecutar. **Entregable:** tabla de configuración de desarrollo/pruebas/producción, pruebas de lectores autorizados y denegados por rutas de informe y archivo, y pasos de reversión. Explica por qué una etiqueta de confidencialidad no implementa todo el diseño de permisos.

<a id="dp-700-unit-5"></a>

## 5. Diagnosticar una ejecución lenta ficticia

Crea una referencia de duración, recuentos de entrada y salida, rechazos, actualización y utilización de capacidad. Añade un incidente con igual volumen que tarde el doble. Incluye tres posibles causas: una combinación sesgada en Spark, muchos archivos pequeños y demanda simultánea de capacidad. Indica qué evidencias apoyarían o rechazarían cada explicación; inspecciona poda de particiones y consultas cuando corresponda.

**Escenario:** un reintento sigue a una escritura parcial. **Evidencia:** usa las reglas de versiones de la unidad 2 para demostrar si cambia el estado de negocio. **Entregable:** un experimento de optimización reversible con umbrales de aceptación y conciliación de corrección. Marca todos los tiempos de Fabric como NO EJECUTADO; el razonamiento sintético no establece rendimiento real, duración de recuperación ni un despliegue correcto en la nube.
