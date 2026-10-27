# Recursos y disponibilidad

Azure Resource Manager es la capa de administración con la que desplegamos y gestionamos recursos. El portal, Azure CLI y las plantillas utilizan esa capa.

## Organización

- **Tenant de Microsoft Entra:** directorio de identidades asociado a las suscripciones.
- **Grupo de administración:** ámbito para gobernar varias suscripciones.
- **Suscripción:** ámbito de administración, cuotas y facturación.
- **Grupo de recursos:** recursos con un ciclo de vida relacionado.
- **Recurso:** una red, una base de datos, una VM, etc.

El tenant no es un contenedor de recursos del mismo tipo que un grupo de recursos. Los permisos pueden heredarse desde grupos de administración hasta recursos, según el ámbito asignado.

Un recurso pertenece a un grupo de recursos a la vez. Mover recursos tiene restricciones: no todos los tipos admiten los mismos movimientos.

## Regiones y zonas

Una región es un área geográfica con centros de datos. Una zona de disponibilidad agrupa uno o varios centros de datos con alimentación, refrigeración y red independientes dentro de una región.

- La región del grupo de recursos corresponde a sus metadatos; sus recursos pueden estar en otras regiones.
- Las opciones de zonas dependen del servicio y de la región.
- Tener dos instancias no garantiza que estén distribuidas entre zonas.
- Las regiones emparejadas no implican replicación automática de cualquier recurso.

## SLA y bloqueos

El SLA define compromisos y condiciones de un servicio. La disponibilidad de nuestra aplicación también depende de su diseño y dependencias.

Los bloqueos de administración pueden prevenir cambios o eliminaciones accidentales. No sustituyen a RBAC ni a las copias, y su efecto no cubre todas las operaciones sobre datos.

**Caso de clase:** separar desarrollo y producción por grupos de recursos facilita la limpieza. Separarlos por suscripción puede aportar un aislamiento administrativo mayor.

**Repaso:** ¿la ubicación del grupo obliga a ubicar allí la VM? No.

## Ejemplo de ciclo de vida

La web y su almacenamiento de pruebas se crean y eliminan juntos. Tiene sentido agruparlos. Una red compartida por varios proyectos puede necesitar un grupo y responsables propios: borrarla con una aplicación afectaría a otras.

Las etiquetas pueden identificar propietario y entorno, pero hay que mantenerlas. No asumas que las de un grupo aparecen automáticamente en cada recurso.

## Qué comprobar antes de mover un recurso

Comprobaría si el tipo permite el movimiento, sus dependencias, el destino y los permisos. Los identificadores pueden cambiar y las automatizaciones que los usan necesitan revisión. Cambiar de región no equivale a cambiar de grupo.

Los bloqueos y políticas del destino también pueden influir. Un ensayo o validación previa reduce sorpresas, pero no justifica prometer una operación sin impacto para cualquier recurso.

**Ejercicio:** la universidad solicita separar el gasto de dos facultades sin romper una red compartida. Propón una estructura y explica qué separa facturación, administración y ciclo de vida.

---

[Índice](README.md) · [Otro idioma](../en/02-resources.md) · [Anterior](01-fundamentals.md) · [Siguiente](03-compute.md)

## Ampliación desde Microsoft Learn · landing

Una landing zone organiza fundamentos de identidad, conectividad, administración y gobierno para alojar cargas. Los equipos de plataforma y aplicación pueden tener responsabilidades diferentes. Un acelerador aporta un punto de partida, no sustituye los requisitos de la organización.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) · [Ampliación desde Microsoft Learn](15-microsoft-learn.md#learn-landing)
