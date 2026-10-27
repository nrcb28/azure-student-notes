# Ampliación práctica desde Microsoft Learn

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

Revisión: 27 de octubre de 2026. Son explicaciones reescritas de documentación oficial, con ejemplos propios de la aplicación universitaria. Los ejemplos plantean comprobaciones; no se han desplegado en Azure. Las referencias enlazadas permiten revisar requisitos y cambios.

<a id="learn-sas"></a>

## 1. SAS basada en identidad

Una user delegation SAS para Blob se firma mediante una clave de delegación obtenida con Entra ID. Emitirla requiere permisos para obtener esa clave; tener un enlace de un blob no concede ese derecho. La firma y las restricciones de acceso deben diseñarse conjuntamente.

**Caso:** un estudiante necesita descargar un PDF durante unos minutos. Limitaríamos recurso, lectura y duración. Evitaríamos que la URL acabara en logs o capturas. Si falla, revisaríamos expiración, permisos y red por separado. Antes de emitirla, decidiríamos cómo responder ante una filtración y qué opciones de revocación admite ese tipo de SAS.

[Microsoft Learn · Storage: user delegation SAS](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

<a id="learn-dns"></a>

## 2. DNS privado: seguir el nombre

El cliente debe resolver el nombre del servicio a la IP del private endpoint. Crear la interfaz privada no configura por sí solo todos los resolutores. La zona recomendada depende del servicio; no conviene reemplazar indiscriminadamente una zona pública completa.

**Caso:** desde una VM funciona, desde la universidad no. Compararíamos respuestas DNS, enlaces de zona, reenvío y ruta desde cada origen. Mantendríamos el nombre de servicio en lugar de fijar una IP en el código. Una resolución privada correcta tampoco concede permisos sobre datos.

[Microsoft Learn · Private endpoint DNS](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

<a id="learn-policy"></a>

## 3. Remediación: evaluar no es corregir

Las tareas de remediación aplican las operaciones de modify o el despliegue de deployIfNotExists a recursos existentes. Utilizan la identidad administrada de la asignación y sus permisos. Cambiar una definición no actualiza automáticamente todos los permisos asociados.

**Caso:** exigimos una configuración y los recursos anteriores siguen incumpliendo. Revisaríamos efecto, ámbito, identidad y roles antes de lanzar remediación sobre un grupo piloto. Guardaríamos el resultado por recurso. Deny no es una herramienta que transforme cualquier recurso antiguo para hacerlo conforme.

[Microsoft Learn · Policy remediation](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

<a id="learn-dcr"></a>

## 4. DCR: decidir qué datos llegan

Las data collection rules describen recogida y encaminamiento en escenarios compatibles. Pueden incluir transformaciones para filtrar o modificar datos antes del destino. No todas las señales usan el mismo camino; no hay que confundir DCR con una sustitución universal de diagnostic settings.

**Caso:** faltan eventos de una VM. Revisaríamos agente, asociación de regla, origen, flujo, destino y esquema antes de escribir una alerta. Enviar todo aumenta coste y puede exponer datos. Una transformación que elimina campos útiles también puede dejar una investigación sin evidencia.

[Microsoft Learn · Azure Monitor data collection rules](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview)

<a id="learn-whatif"></a>

## 5. What-if: revisar límites del análisis

What-if anticipa cambios sin aplicarlos. Tiene requisitos de permisos y límites de análisis; ciertas dependencias o expresiones pueden impedir evaluar partes del despliegue. Un resultado incompleto no demuestra ausencia de cambios.

**Caso:** el plan muestra Ignore o un módulo sin analizar. Leeríamos diagnósticos y aislaríamos el módulo; no lo trataríamos como NoChange. Separaríamos compilación local, validación remota, previsión y prueba posterior. La aprobación de un cambio debe considerar lo que el análisis no pudo comprobar.

[Microsoft Learn · Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

<a id="learn-slots"></a>

## 6. Slots: una versión viva con dependencias

Un deployment slot tiene su propio hostname y ejecuta una aplicación. Copiar ajustes no equivale a clonar contenido, red privada o todas las dependencias. Durante el swap se aplican pasos de preparación y calentamiento.

**Caso:** staging envía correos reales. Revisaríamos conexiones, ajustes específicos, identidad y tareas de inicio antes de intercambiar. Que el slot reciba cero tráfico de usuarios no impide que ejecute procesos propios. Revertir el swap tampoco revierte automáticamente una migración destructiva de la base.

[Microsoft Learn · App Service deployment slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)

<a id="learn-landing"></a>

## 7. Landing zones: plataforma y carga

Una landing zone organiza fundamentos de identidad, conectividad, administración y gobierno para alojar cargas. Los equipos de plataforma y aplicación pueden tener responsabilidades diferentes. Un acelerador aporta un punto de partida, no sustituye los requisitos de la organización.

**Caso:** cinco facultades comparten servicios de red y mantienen aplicaciones independientes. Definiríamos propietarios, permisos, límites de suscripción, políticas y costes. No desplegaríamos una arquitectura empresarial completa para una práctica pequeña solo porque existe una plantilla. Documentaríamos qué se comparte y qué se aísla.

[Microsoft Learn · Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)

<a id="learn-checks"></a>

## 8. Checks: quién controla la publicación

En Azure Pipelines, los responsables de recursos administran approvals y checks fuera del YAML de la pipeline. Antes de una etapa deben satisfacerse los controles de sus recursos. Una condición escrita por el autor no equivale a esa separación de responsabilidades.

**Caso:** producción exige revisión independiente y una ventana horaria. Definiríamos recurso protegido, revisores, plazo y tratamiento del rechazo. Probaríamos qué ocurre si el código cambia o un check expira. Un pipeline verde no concede permiso para utilizar cualquier conexión de servicio.

[Microsoft Learn · Azure Pipelines approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops)

---

[Source register](../LEARN-SOURCES.md) · [Attribution](../ATTRIBUTION.md)

<a id="learn-blob-recovery"></a>

## 9. Recuperar blobs: elegir el nivel de protección

La eliminación temporal de blobs conserva objetos eliminados durante la retención configurada. No protege por sí sola una eliminación del contenedor o de toda la cuenta. Hay que distinguir objeto, contenedor y servicio, y preparar protección para cada riesgo.

**Caso:** una estudiante elimina el contenedor de apuntes. Saber que los blobs tenían soft delete no demuestra que podamos recuperar el contenedor. Antes del incidente debemos comprobar la protección de contenedores y otras opciones de copia adecuadas al escenario.

**Procedimiento de estudio:** identifica qué se borró, cuándo ocurrió, qué retención existía y con qué identidad se restaurará. Recupera en un entorno controlado cuando sea posible, verifica contenido y permisos, y reconcilia metadatos de la base. Documenta qué queda fuera de protección. Activar una función después del borrado no equivale a haber conservado el estado anterior.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview)

<a id="learn-retry"></a>

## 10. Reintentos: no repetir cualquier fallo

Un retry ayuda frente a fallos transitorios; no corrige credenciales inválidas ni una solicitud mal construida. Debe tener intentos y tiempos acotados. Revisar los reintentos que ya realiza el SDK evita multiplicarlos entre capas.

**Caso:** el procesador registra un documento, pero pierde la respuesta. Repetir puede crear otro registro si la operación no es idempotente. Usaría un identificador estable y una comprobación consistente del resultado.

**Diseño:** clasifica el fallo, respeta las indicaciones de espera del servicio cuando correspondan y define un plazo total. Separa fallos iniciales recuperados de agotamiento de intentos. Registra información útil sin secretos. Si varias capas repiten, calcula el número real de solicitudes y el efecto sobre la dependencia. Una tormenta de reintentos puede empeorar la saturación en lugar de mejorar disponibilidad.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)

<a id="learn-rbac-diagnosis"></a>

## 11. Diagnóstico de RBAC con evidencia

Poder administrar un recurso no implica poder conceder roles ni acceder a sus datos. Para crear asignaciones se requiere la acción correspondiente en el ámbito adecuado, y pueden existir condiciones que limiten qué roles o identidades se permiten.

**Caso:** el botón de asignar rol está deshabilitado. Antes de pedir Owner, confirmaría cuenta, tenant, ámbito y capacidad de asignación. Un rol muy amplio puede ocultar la causa y dejar privilegios permanentes.

**Lista de trabajo:** anota operación fallida, identidad efectiva, recurso y ámbito; revisa asignaciones directas y heredadas, grupos y condiciones; distingue plano de administración y de datos. Considera propagación o renovación de credenciales según el caso. Prueba de nuevo la operación mínima que falló, no una acción distinta. Guarda la evidencia que explique por qué se concedió o negó el acceso.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting)

<a id="learn-vault-recovery"></a>

## 12. Recuperar Key Vault no restaura todas las integraciones

Soft delete permite recuperar el almacén y objetos compatibles dentro de su periodo. Recuperar un almacén eliminado no recupera automáticamente determinadas integraciones, como asignaciones RBAC y suscripciones Event Grid, que deben revisarse y recrearse cuando corresponda.

**Caso:** el vault reaparece, pero la API no puede leer su secreto. El nombre visible no prueba que los permisos y dependencias estén recuperados. Revisaría identidad, acceso y configuración de la aplicación.

**Runbook:** inventaría objetos y consumidores, configura protección y responsabilidades antes del incidente, distingue recuperar de purgar, y valida una petición completa después. No uses purge como limpieza improvisada: elimina la posibilidad de recuperar el objeto purgado cuando está permitido. Comprueba también las protecciones y restricciones que pueden impedir purgar. La prueba termina cuando el consumidor autorizado funciona, no al ver el recurso en el portal.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview)
