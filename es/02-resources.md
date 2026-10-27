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

---

[Índice](README.md) · [Otro idioma](../en/02-resources.md) · [Anterior](01-fundamentals.md) · [Siguiente](03-compute.md)
