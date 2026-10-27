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
