# AZ-120 · Cuaderno avanzado común

[Guía](AZ-120.md) · [10 casos](AZ-120-cases.md) · [Índice](README.md)

Cinco unidades equivalentes entre idiomas. Trabaja sin conexión con el entorno SAP ficticio de compras y finanzas y su portal de investigación. No se proporciona ni afirma licencia, despliegue Azure, ejecución SAP o preparación productiva. Distingue supuestos y resultados previstos de evidencia observada.

<a id="az-120-unit-1"></a>

## 1. Inventariar responsabilidades y capacidad admitida

Dibuja SID de producción y desarrollo, servidores de aplicaciones, ASCS/ERS o SCS, HANA, archivos compartidos, identidad, DNS e interfaces. Asigna responsables de infraestructura, SO, Basis, base de datos, seguridad y validación de negocio. Explica por qué servidores redundantes dejan otros puntos únicos de fallo. Prepara dimensionamiento con SAPS relevantes, memoria, crecimiento, rendimiento, latencia y margen ante fallos; condiciona la SKU a certificación y compatibilidad.

**Escenario:** una VM más barata coincide en núcleos, pero no tiene evidencia de soporte HANA. **Evidencia:** dependencias, combinación VM/SO/base de datos/almacenamiento admitida, cuotas regionales supuestas y responsable de licencias. **Entregable:** decisión arquitectónica con aceptación y mediciones pendientes. Repasa [fundamentos de cómputo](../../es/03-compute.md).

<a id="az-120-unit-2"></a>

## 2. Diseñar ubicación, red y almacenamiento HANA

Dibuja rutas admitidas entre aplicación y base de datos, administración, replicación, copia, campus y reenvío DNS. Separa ExpressRoute privado del cifrado seleccionado. Compara aislamiento por zonas con restricciones PPG usando supuestos explícitos de latencia. Planifica `/hana/data`, `/hana/log` y `/hana/shared`, sistemas de archivos admitidos, límites de E/S de disco y VM y decisiones específicas de caché o Write Accelerator.

**Escenario:** un punto de guardado coincide con compras lentas y se propone un dispositivo de inspección entre aplicación SAP y base de datos. **Evidencia:** flujos, ubicación, presupuesto de latencia previsto, funciones de volúmenes y observaciones de E/S necesarias. **Entregable:** alternativa admitida con compromisos de capacidad y dominios de fallo. Repasa [fundamentos de red](../../es/05-networking.md).

<a id="az-120-unit-3"></a>

## 3. Separar conmutación segura de recuperación histórica

Explica HANA System Replication, control de clúster admitido, protección ASCS/SCS, ERS, cuórum, fencing, nombres virtuales y sondas del equilibrador. Dibuja el único escritor permitido tras una partición de red. Define RPO/RTO de negocio, copias coherentes con la carga, registros utilizables, retención y dependencias. Muestra por qué replicar copia errores y una instantánea sin coordinación no demuestra coherencia.

**Escenario:** no se puede aislar al nodo par y un error financiero ya se replicó. **Evidencia:** decisiones previstas del clúster, dependencias de fencing, regla que determina qué copia constituye la fuente de verdad, copias/registros y validación de restauración. **Entregable:** procedimientos distintos de HA y restauración, rechazando desactivar fencing e incluyendo conciliación de negocio después de recuperar datos históricos.

<a id="az-120-unit-4"></a>

## 4. Redactar el procedimiento de migración e integración

Evalúa soporte del origen, versiones, interfaces, ritmo de cambios, transferencia, interrupción y compatibilidad del destino. Justifica una migración admitida. Define ensayo, congelación de escrituras, sincronización final, aislamiento del origen, cambios DNS/interfaces, comprobaciones técnicas, aceptación de negocio y reapertura. Para RISE, asigna responsabilidades de integración del cliente y gestión SAP mediante contrato, sin suponer acceso a suscripciones.

**Escenario:** se crean pedidos tras el cambio y después falla el portal. **Evidencia:** cronología de escrituras, colas, puntos de transferencia, controles de validación y responsables. **Entregable:** reversión antes de nuevas escrituras y decisión distinta de conciliación o migración inversa después, con escalado a SAP si la frontera fallida pertenece a RISE.

<a id="az-120-unit-5"></a>

## 5. Revisar operaciones y ensayar recuperación regional

Revisa un cambio IaC ficticio: soporte de imagen, ubicación, almacenamiento, referencias a secretos, dependencias y diferencias destructivas. Escalona actualizaciones con orden consciente del clúster y criterios de reversión. Especifica recopilación Azure Monitor, proveedores SAP, evidencia de base de datos y clúster, responsables de alertas y retención. Recupera el servicio completo en otra región: identidad, red, servicios centrales, aplicaciones, datos, integraciones y sincronización de retorno.

**Escenario:** una interrupción regional coincide con compras y una propuesta de cambio de tamaño pendiente. **Evidencia:** dependencias, RPO/RTO previstos, capacidad degradada, replicación, validaciones de negocio y responsables de costes continuados de cómputo/almacenamiento/red/monitorización. **Entregable:** ejercicio de incidente y revisión del cambio que distingan controles previstos de pruebas ejecutadas.

Usa las seis referencias técnicas de la [guía](AZ-120.md) para cuestionar supuestos. Estos ejercicios originales seleccionan conceptos útiles; no cubren todos los objetivos oficiales ni garantizan aprobar.
