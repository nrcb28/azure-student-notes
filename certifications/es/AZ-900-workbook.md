# AZ-900 · Cuaderno avanzado común

[←](README.md) · [Núcleo común de estudio](../../es/16-common-core.md) · [Laboratorios avanzados](../../es/17-advanced-labs.md)

Este bloque tiene los mismos objetivos, escenarios y entregables en los ocho idiomas. La equivalencia se comprueba por unidades y evidencias, no por número de palabras. Las guías anteriores siguen disponibles como explicación complementaria.

<a id="az-900-unit-1"></a>

## 1. Repartir responsabilidades

Compara tres propuestas para la misma API: VM, plataforma administrada y software ya contratado. Enumera sistema operativo, dependencias, datos, acceso y recuperación. No marques ninguna opción como libre de responsabilidad. El criterio es el control necesario y el trabajo que el equipo puede asumir.

**Caso:** una biblioteca obliga a instalar un controlador del sistema. Explica qué opción deja de encajar y por qué. **Evidencia:** una matriz de responsabilidades y una alternativa descartada por un requisito concreto.

<a id="az-900-unit-2"></a>

## 2. Disponibilidad y límites

Distingue fallo de proceso, instancia, zona y región. Dos instancias pueden compartir dependencias críticas. Explica qué ocurre con sesiones y documentos cuando una petición llega a otra instancia. No prometas disponibilidad de toda la app a partir del SLA de un componente.

**Caso:** cuatro APIs dependen de una única base sin recuperación definida. **Evidencia:** dibujo del recorrido completo, punto débil identificado y prueba propuesta para validarlo.

<a id="az-900-unit-3"></a>

## 3. Elegir datos y conectividad

Separa objetos, metadatos relacionales y archivos compartidos. Para cada uno define lectura, escritura, autorización y recuperación. Distingue acceso público de anónimo, y DNS privado de permisos. Una conexión correcta no concede por sí sola acceso a datos.

**Caso:** el profesor abre un enlace de documento, pero otro usuario obtiene 403. **Evidencia:** tres hipótesis separadas para red, identidad y autorización, y el dato que confirmaría cada una.

<a id="az-900-unit-4"></a>

## 4. Gobernar y estimar

Usa RBAC para acciones de identidades, Policy para condiciones y etiquetas para clasificación. Un presupuesto sirve para seguimiento, no para asegurar una parada universal. Estima capacidad, operaciones, transferencia, registros y copias con supuestos explícitos.

**Caso:** el proyecto solo debe desplegarse en regiones aprobadas y atribuir gasto por facultad. **Evidencia:** regla de gobierno, rol mínimo y tabla de unidades de coste, sin inventar tarifas.

<a id="az-900-unit-5"></a>

## 5. Explicar y comprobar

Describe cómo distingues despliegue, funcionamiento y recuperación. Un recurso creado no prueba que un estudiante descargue. Una copia creada no prueba que se restaure a tiempo. Elige señales de negocio además de CPU.

**Entrega final:** diagrama de la app, cinco decisiones justificadas, fallo tolerado, responsabilidades restantes y plan de limpieza. Responde otra vez cambiando un requisito. Si la respuesta nunca cambia, revisa si realmente estás razonando.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) · [AZ-900](AZ-900.md)
