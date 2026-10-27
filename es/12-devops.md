# DevOps e infraestructura como código

DevOps reúne prácticas de desarrollo y operación para entregar cambios de forma fiable. Instalar una herramienta de pipelines no crea ese proceso por sí solo.

## Flujo de trabajo

```text
Rama → Pull request → Comprobaciones → Entorno de pruebas
     → Revisión → Producción → Observación
```

- **Integración continua:** integrar cambios con compilación y comprobaciones.
- **Entrega continua:** mantener cambios preparados para desplegar.
- **Despliegue continuo:** publicar automáticamente los cambios que pasan las condiciones.
- **Artefacto:** salida versionada del proceso, como un paquete o imagen.

Conviene desplegar el mismo artefacto probado, no recompilar algo potencialmente diferente para producción.

## Infraestructura como código

Bicep describe recursos de Azure de forma declarativa. Terraform utiliza proveedores y mantiene un estado que relaciona la configuración con los recursos.

- Versionar cambios y revisar diferencias.
- Parametrizar entorno, región y nombres.
- Mantener secretos fuera de archivos versionados.
- Revisar el plan o what-if antes de aplicar.
- Detectar cambios manuales que alejan la infraestructura del código.

Bicep no mantiene un archivo de estado equivalente al de Terraform. Ambos enfoques requieren conocer los recursos que describen.

## Identidad de las automatizaciones

OIDC permite federar identidades entre GitHub Actions y Azure sin guardar una credencial duradera de aplicación. Requiere configurar la aplicación o identidad, la credencial federada, permisos en Azure y permisos del workflow.

No basta con añadir id-token: write al YAML: también debe existir la confianza correspondiente en Azure.

## Despliegues y vuelta atrás

Los slots de App Service pueden facilitar pruebas e intercambios si el plan los admite. Las revisiones de Container Apps permiten gestionar versiones según configuración.

Volver atrás el código no revierte necesariamente una migración de base de datos. Diseñar cambios compatibles y probar recuperación.

**Caso de clase:** revisar primero los archivos Bicep, desplegar en desarrollo y validar una petición completa.

**Repaso:** un pipeline verde no demuestra por sí solo que la aplicación funciona para el usuario.

---

[Índice](README.md) · [Otro idioma](../en/12-devops.md) · [Anterior](11-messaging.md) · [Siguiente](13-laboratorios.md)
