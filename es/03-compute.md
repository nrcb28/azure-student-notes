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

---

[Índice](README.md) · [Otro idioma](../en/03-compute.md) · [Anterior](02-resources.md) · [Siguiente](04-storage.md)
