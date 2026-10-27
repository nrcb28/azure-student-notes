# Repaso con respuestas

Intenta responder antes de desplegar cada solución. Estas preguntas son originales de estudio, no preguntas oficiales de examen.

## 1. ¿Qué responsabilidad permanece en SaaS?

<details>
<summary>Ver respuesta</summary>

Gestionar adecuadamente identidades, accesos, datos y las opciones disponibles del producto.

</details>

## 2. ¿Vertical u horizontal al añadir instancias?

<details>
<summary>Ver respuesta</summary>

Horizontal. Añadir capacidad a una instancia es vertical.

</details>

## 3. ¿Un grupo de recursos puede contener recursos en regiones distintas?

<details>
<summary>Ver respuesta</summary>

Sí. Su ubicación no obliga a ubicar allí todos sus recursos.

</details>

## 4. ¿Dos VM garantizan tolerancia al fallo de una zona?

<details>
<summary>Ver respuesta</summary>

No. Importan su distribución, configuración y las dependencias de la aplicación.

</details>

## 5. ¿Cuándo elegir App Service frente a una VM?

<details>
<summary>Ver respuesta</summary>

Cuando el runtime y requisitos encajan y queremos reducir administración del sistema operativo.

</details>

## 6. ¿Un contenedor necesita Kubernetes?

<details>
<summary>Ver respuesta</summary>

No. Hay alternativas como Container Instances, Container Apps o plataformas compatibles con contenedores.

</details>

## 7. ¿Dónde guardarías PDFs y sus metadatos?

<details>
<summary>Ver respuesta</summary>

PDFs en Blob Storage; metadatos consultables en una base de datos adecuada.

</details>

## 8. ¿ZRS equivale a backup?

<details>
<summary>Ver respuesta</summary>

No. La redundancia por zonas no recupera por sí sola versiones anteriores borradas o dañadas.

</details>

## 9. ¿El peering entre VNets es transitivo?

<details>
<summary>Ver respuesta</summary>

No automáticamente. A-B y B-C no implican conectividad A-C.

</details>

## 10. ¿Private Endpoint desactiva el acceso público?

<details>
<summary>Ver respuesta</summary>

No necesariamente. Hay que revisar la configuración del servicio y DNS.

</details>

## 11. ¿Contributor siempre puede leer blobs?

<details>
<summary>Ver respuesta</summary>

No. Las acciones de administración y las de datos se autorizan de forma diferenciada.

</details>

## 12. ¿Qué aporta una identidad administrada?

<details>
<summary>Ver respuesta</summary>

Permite autenticar la carga frente a servicios compatibles sin almacenar credenciales de aplicación; aún necesita permisos.

</details>

## 13. ¿Policy o RBAC para exigir etiquetas?

<details>
<summary>Ver respuesta</summary>

Policy. RBAC controla quién puede ejecutar acciones.

</details>

## 14. ¿Asignar una política corrige todos los recursos existentes?

<details>
<summary>Ver respuesta</summary>

No. Depende del efecto, sus permisos y las tareas de remediación.

</details>

## 15. ¿Una CPU baja demuestra que la API funciona bien?

<details>
<summary>Ver respuesta</summary>

No. Puede esperar una base de datos, una red o una dependencia lenta.

</details>

## 16. ¿Un presupuesto garantiza no superar el gasto?

<details>
<summary>Ver respuesta</summary>

No. Es una herramienta de seguimiento y alertas, no un límite automático universal.

</details>

## 17. ¿Desasignar una VM elimina todos sus costes?

<details>
<summary>Ver respuesta</summary>

No. Los discos y otros recursos pueden seguir generando cargos.

</details>

## 18. ¿Qué diferencia hay entre RTO y RPO?

<details>
<summary>Ver respuesta</summary>

RTO: tiempo objetivo de recuperación. RPO: pérdida de datos tolerable medida en tiempo.

</details>

## 19. ¿Por qué hacer idempotente un consumidor?

<details>
<summary>Ver respuesta</summary>

Porque puede recibir o procesar mensajes repetidos sin que deban duplicarse sus efectos.

</details>

## 20. ¿Event Grid y Event Hubs son intercambiables?

<details>
<summary>Ver respuesta</summary>

No. Event Grid distribuye eventos; Event Hubs ingiere flujos de eventos con otro modelo de consumo.

</details>

## 21. ¿OIDC funciona con añadir una línea al workflow?

<details>
<summary>Ver respuesta</summary>

No. Requiere confianza federada y permisos configurados en Azure y en el workflow.

</details>

## 22. ¿Volver atrás el código revierte una migración de datos?

<details>
<summary>Ver respuesta</summary>

No necesariamente. Hay que diseñar compatibilidad y recuperación de datos.

</details>

## 23. ¿Compilar Bicep demuestra que un despliegue funcionará?

<details>
<summary>Ver respuesta</summary>

No. No verifica por sí solo cuotas, permisos, políticas ni toda la disponibilidad regional.

</details>

## 24. ¿Qué comprobarías antes de borrar un grupo?

<details>
<summary>Ver respuesta</summary>

Que sea el grupo dedicado de la práctica y qué recursos contiene. El borrado afecta a todos sus recursos.

</details>
