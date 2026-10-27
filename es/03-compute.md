# Cómputo y contenedores

Elegir dónde ejecutar código consiste en repartir trabajo entre nuestro equipo y la plataforma. Más control suele traer más mantenimiento.

| Servicio | Encaje habitual |
|---|---|
| Virtual Machines | Control del sistema operativo y software específico |
| VM Scale Sets | Grupos de máquinas con configuración y escalado coordinados |
| App Service | Aplicaciones web y APIs |
| Functions | Funciones disparadas por eventos |
| Container Instances | Ejecución de contenedores sin administrar un clúster |
| Container Apps | Aplicaciones en contenedores con revisiones y escalado administrado |
| AKS | Kubernetes administrado, con responsabilidades operativas del cliente |

## Qué sigue siendo nuestro

En una VM hay que mantener el sistema operativo y la aplicación. En App Service dejamos más administración a la plataforma, pero seguimos gestionando dependencias de nuestra aplicación, acceso y configuración.

Un contenedor empaqueta una aplicación y sus dependencias. No es una VM completa: los contenedores tradicionales comparten el kernel del sistema anfitrión.

AKS administra parte de Kubernetes. No elimina la necesidad de configurar actualizaciones, red, permisos, políticas y capacidad.

## Functions y serverless

Serverless significa que no administramos directamente los servidores. No significa coste cero, ausencia de límites ni escalado infinito.

El arranque, la conectividad, la duración de ejecución y la facturación dependen del plan. Para trabajos largos, revisaría esos límites antes de elegir.

## Decisión para nuestra API

Empezaría por App Service si el runtime encaja. Si ya tenemos una imagen de contenedor y necesitamos componentes independientes, estudiaría Container Apps. Elegiría AKS cuando necesitemos Kubernetes de verdad.

**Error frecuente:** alojar tres apps en el mismo App Service Plan y asumir que tienen capacidad completamente independiente. Pueden compartir los recursos del plan.

**Repaso:** usar Docker no obliga a desplegar Kubernetes.

## Despliegue correcto, aplicación incorrecta

La plataforma inicia el contenedor, pero la aplicación escucha en otro puerto o tarda más de lo previsto en arrancar. El despliegue puede crear recursos y aun así dejar el servicio sin atender peticiones.

Comprobaría puerto, proceso, logs de inicio, configuración y comprobaciones de salud. Después validaría una petición que recorra las dependencias reales.

## Imagen y configuración

Separar imagen de configuración permite utilizar el mismo artefacto en varios entornos. Los secretos no deberían incorporarse a una capa de imagen: pueden permanecer en su historial aunque otro paso borre el archivo.

Fijar una versión ayuda a reproducir un problema. Usar latest en todos los despliegues hace más difícil saber qué código y dependencias se ejecutaban.

**Decisión razonada:** si solo necesitamos ejecutar una tarea ocasional empaquetada como contenedor, un clúster permanente puede añadir mantenimiento innecesario. Revisa arranque, duración, conectividad y plan antes de elegir una alternativa.

---

[Índice](README.md) · [Otro idioma](../en/03-compute.md) · [Anterior](02-resources.md) · [Siguiente](04-storage.md)
