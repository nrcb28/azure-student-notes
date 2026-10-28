# AZ-104 · Cuaderno avanzado común

[←](README.md) · [Núcleo común de estudio](../../es/16-common-core.md) · [Laboratorios avanzados](../../es/17-advanced-labs.md)

Este bloque tiene los mismos objetivos, escenarios y entregables en los ocho idiomas. La equivalencia se comprueba por unidades y evidencias, no por número de palabras. Las guías anteriores siguen disponibles como explicación complementaria.

<a id="az-104-unit-1"></a>

## 1. Trazar acceso efectivo

Anota identidad, tenant, suscripción, recurso, acción y ámbito. Revisa grupos, asignaciones directas, herencia, condiciones y propagación. Diferencia acciones de administración y datos. Crear roles requiere permisos propios; un Contributor no es automáticamente administrador de accesos.

**Caso:** la cuenta crea Storage y no lista blobs. **Evidencia:** explicación del permiso necesario y una comprobación mínima con la misma identidad. No uses Owner como prueba general ni cambies red sin una hipótesis.

<a id="az-104-unit-2"></a>

## 2. Proteger y recuperar datos

Elige protección por objeto, contenedor y cuenta. Registra lo que ya estaba habilitado antes del incidente. Con versionado, restaurar puede requerir seleccionar o promover una versión; no supongas un procedimiento único para todas las configuraciones.

**Caso:** un archivo de práctica se elimina y debe volver con el mismo contenido. **Evidencia:** configuración previa, hash antes y después, permisos comprobados y datos que siguen retenidos tras la limpieza.

<a id="az-104-unit-3"></a>

## 3. Leer infraestructura antes de modificar

Interpreta parámetros, recursos, dependencias, outputs y cambios previstos. Distingue compilar, validar, what-if y aplicar. Una operación exportada puede requerir limpieza antes de reutilizarla. Cuotas, regiones y políticas pueden impedir un despliegue sintácticamente correcto.

**Caso:** what-if no analiza un módulo. **Evidencia:** diagnóstico, alcance sin evaluar y decisión de resolverlo antes de aplicar. Revisa discos, red y configuración al cambiar tamaño o ubicación de una VM.

<a id="az-104-unit-4"></a>

## 4. Diagnosticar la ruta completa

Sigue DNS, IP, ruta, NSG, firewall del sistema, listener y autorización de aplicación. Las reglas son con estado y varias capas pueden filtrar. En el balanceador valida frontend, backend, regla y probe. En App Service separa entrada privada de integración saliente.

**Caso:** probe sano y petición real fallida. **Evidencia:** puerto y respuesta de cada comprobación, reglas aplicables y una hipótesis verificable. No equipares salud del probe con corrección funcional.

<a id="az-104-unit-5"></a>

## 5. Operar con evidencias

Define métrica, registro, alerta, acción y responsable. Confirma origen, asociación y destino de datos antes de culpar a la consulta. Para backup y Site Recovery, mide recuperación de la aplicación con identidad, DNS y dependencias.

**Entrega final:** ejecutar las prácticas de Storage y lectura de roles, registrar esperado frente a observado y proponer un runbook de recuperación. Separar comprobaciones locales de pruebas en Azure, y comprobar eliminación o retención residual.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104) · [AZ-104](AZ-104.md)
