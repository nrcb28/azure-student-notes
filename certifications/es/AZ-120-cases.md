# AZ-120 · 10 casos con respuestas razonadas

[Guía](AZ-120.md) · [Cuaderno](AZ-120-workbook.md) · [Índice](README.md)

Escenarios originales de una universidad con sistemas empresariales, no preguntas oficiales. Explica decisión y evidencia antes de abrir cada respuesta. Las comprobaciones propuestas son trabajo de diseño sin conexión; no se afirma ejecución de Azure ni SAP.

## 1. La universidad añade dos servidores de aplicaciones, pero mantiene una sola VM ASCS y una sola VM HANA. ¿Ha eliminado los puntos únicos de fallo importantes?

<details>
<summary>Respuesta</summary>

No. La redundancia de aplicaciones no protege servicios centrales ni base de datos. Inventaría cada SID y distingue ASCS, ERS, instancias de aplicaciones, HANA, archivos compartidos y dependencias. Propón diseños de alta disponibilidad admitidos para servicios centrales y base de datos, con responsables y rutas de reconexión del cliente. La evidencia debe incluir un diagrama de dependencias y el efecto previsto de perder cada componente. Comprueba también la capacidad restante de aplicaciones. Contar VM no demuestra que una compra sobreviva a perder coordinación o datos.

</details>

## 2. Una VM más barata tiene el mismo número de núcleos que la propuesta para HANA. ¿Basta para sustituirla?

<details>
<summary>Respuesta</summary>

No. Comprueba certificación SAP HANA para el tipo preciso de VM, carga, versión de SO, base de datos y modelo de despliegue. Compara memoria medida, crecimiento, SAPS relevantes de aplicaciones, rendimiento de almacenamiento, latencia del registro y límites de red. Verifica capacidad regional y cuotas. La evidencia es una combinación admitida y una hoja de dimensionamiento con margen ante fallos, no una comparación de CPU. Una estimación menor de infraestructura no decide compatibilidad; estos apuntes tampoco acreditan licencias SAP ni capacidad productiva suficiente.

</details>

## 3. El equipo de red afirma que ExpressRoute cifra todas las conexiones SAP. ¿Debe aceptarlo el documento de arquitectura?

<details>
<summary>Respuesta</summary>

No. Conectividad privada y cifrado son propiedades distintas. Dibuja la ruta campus-Azure, entrega del proveedor, rutas de Azure, endpoints de aplicación y límites del cifrado elegido. Especifica cifrado admitido de la aplicación u otra solución adecuada donde la directiva lo requiera; verifica las capacidades concretas. Documenta también DNS, autenticación, resiliencia de rutas y flujos permitidos. La evidencia debe identificar qué tráfico se cifra, dónde empieza y termina la protección y cómo comprobarla. Un circuito privado no demuestra confidencialidad de extremo a extremo de todos los protocolos.

</details>

## 4. Un estudiante coloca ambos nodos de alta disponibilidad en un PPG y afirma que también resisten un fallo de zona. ¿Qué razonamiento debe corregir?

<details>
<summary>Respuesta</summary>

Separa proximidad para latencia de aislamiento para resiliencia. Un PPG restringe la proximidad física y no aporta aislamiento entre zonas. Elige ubicación admitida según recuperación requerida y evalúa latencia entre nodos y comportamiento de replicación. Si los PPG están justificados, aplícalos dentro de sus restricciones y documenta limitaciones de asignación. La evidencia incluye dominios de fallo, latencia medida o expresamente supuesta, capacidad restante y secuencia de toma de control. Ni PPG ni zonas configuran por sí solos un clúster SAP o una conmutación de base de datos segura.

</details>

## 5. HANA tiene mucho espacio libre, pero las compras se ralentizan durante los puntos de guardado. ¿Basta con añadir capacidad de disco?

<details>
<summary>Respuesta</summary>

Investiga rendimiento, latencia y colas de datos y registros, además del límite global de E/S de la VM. Los puntos de guardado pueden competir con escrituras del registro aunque sobre espacio. Revisa distribución admitida, sistema de archivos, discos, demanda del volumen compartido y tiempos de carga antes de cambiar nada. Caché y Write Accelerator deben seguir las instrucciones concretas, no una receta universal. La evidencia es una cronología correlacionada de carga y E/S con configuración propuesta admitida. Considera las mediciones pendientes hasta que una prueba autorizada las produzca.

</details>

## 6. Un clúster no puede aislar su nodo par tras un fallo de comunicación. ¿Desactivar fencing recuperaría un servicio seguro?

<details>
<summary>Respuesta</summary>

No. Eliminar fencing permite primarios incompatibles y pone en peligro la integridad. Conserva evidencia y sigue el procedimiento de incidente mientras investigas cuórum, comunicación, permisos y conectividad del agente, o la configuración SBD admitida. Confirma que el nodo supuestamente fallido no puede seguir escribiendo antes de tomar el control. La evidencia incluye estado del clúster, tiempos, resultados del aislamiento, replicación y primario autorizado. La corrección restablece aislamiento y decisiones admitidos. Ver recursos arrancados no demuestra que el servicio SAP pueda aceptar escrituras con seguridad.

</details>

## 7. Una actualización financiera errónea ya llegó a ambas réplicas HANA. ¿Por qué sigue siendo útil una copia protegida de ayer?

<details>
<summary>Respuesta</summary>

La replicación mantiene disponibilidad, pero copia errores lógicos. Una copia protegida y una cadena de registros utilizable permiten recuperar un punto anterior aceptable, según la restauración admitida. Establece RPO aprobado por negocio, dependencias, retención y transacciones posteriores legítimas que requieran conciliación. Confirma coherencia de aplicación; una instantánea genérica de VM no basta automáticamente. La evidencia incluye punto elegido, disponibilidad de copias y registros, restauración aislada, comprobaciones de base de datos y validación de negocio. Replicar correctamente no recupera exactitud histórica si ambas copias contienen el mismo error.

</details>

## 8. El cambio a producción supera comprobaciones básicas y los usuarios crean pedidos nuevos. ¿Basta con devolver DNS al origen intacto para revertir?

<details>
<summary>Respuesta</summary>

Eso abandonaría o bifurcaría transacciones nuevas. El procedimiento necesita otra decisión tras empezar las escrituras: volver a congelarlas, identificar datos que constituyen la fuente de verdad, preservar nuevas transacciones y evaluar conciliación o migración inversa admitidas. Incluye aprobación de negocio, colas de interfaces, sincronización final, aislamiento del origen y validación antes de reabrir cualquiera. La evidencia es una cronología del propietario de las escrituras y una decisión de tratamiento de datos, no instrucciones DNS solamente. El ensayo debe distinguir reversión antes de reabrir escrituras y recuperación posterior, con plazos y responsables.

</details>

## 9. El portal de investigación no llega a SAP RISE. ¿Debe su operador editar NSG en la suscripción de SAP con su rol Azure universitario?

<details>
<summary>Respuesta</summary>

Primero respeta la matriz contractual de responsabilidades. SAP gestiona RISE en su propio entorno Azure; un rol de la suscripción universitaria no controla esos recursos. Traza DNS, rutas, peering o conectividad, firewall, identidad e interfaz SAP acordada del portal, asignando cada comprobación a su responsable. Coordina cambios y escalado del lado SAP con SAP. La evidencia debe mostrar el punto de transferencia fallido y las responsabilidades de ambas partes. RISE no elimina obligaciones del cliente sobre sus integraciones, seguridad o ruta de red hacia una interfaz disponible.

</details>

## 10. La región de recuperación tiene una copia actual de la base de datos y VM encendidas, pero compras sigue sin funcionar. ¿Qué falta validar?

<details>
<summary>Respuesta</summary>

Valida servicios centrales, orden de arranque de aplicaciones, identidad, DNS, nombres virtuales, rutas, secretos, archivos compartidos, interfaces y capacidad admitida suficiente. Compara punto recuperable y tiempo previsto con RPO y RTO de negocio. Impide que el primario original escriba independientemente. Define una compra y un intercambio de interfaz correctos como aceptación, seguidos de retorno controlado al principal. La evidencia incluye responsables, orden de dependencias, estado de replicación, tiempos previstos y criterios de validación. Tener infraestructura en marcha es solo una parte de recuperar el servicio SAP universitario.

</details>

Las fechas de objetivos y seis referencias técnicas primarias están en la [guía](AZ-120.md). Desarrolla diagramas y procedimientos revisables con el [cuaderno](AZ-120-workbook.md).
