# AZ-400 · Cuaderno avanzado común

[←](README.md) · [Núcleo común de estudio](../../es/16-common-core.md) · [Laboratorios avanzados](../../es/17-advanced-labs.md)

Este bloque tiene los mismos objetivos, escenarios y entregables en los ocho idiomas. La equivalencia se comprueba por unidades y evidencias, no por número de palabras. Las guías anteriores siguen disponibles como explicación complementaria.

<a id="az-400-unit-1"></a>

## 1. Trazabilidad y Git

Relaciona necesidad, issue, PR, commit, build, artefacto y despliegue. Define métricas con inicio y fin coherentes. No midas personas por líneas o commits. Elige ramas según frecuencia y versiones mantenidas.

**Caso:** hay que revertir una versión compartida. **Evidencia:** explicar revert frente a reescritura de historia y documentar efecto en datos. Si hubo un secreto, revocarlo o rotarlo antes de confiar en una eliminación de archivos.

<a id="az-400-unit-2"></a>

## 2. Pruebas y artefactos

Construye una vez y promueve el resultado identificado. Registra versión, digest cuando corresponda y origen. Combina unitarias, integración, end-to-end y carga según riesgos. Cobertura es ejecución, no prueba automática de buenas aserciones.

**Caso:** ayer funcionaba sin cambios y hoy no. **Evidencia:** revisar herramientas, dependencias y bases no fijadas. Un test intermitente necesita diagnóstico, no solo repetir hasta verde. Distingue caché de artefacto.

<a id="az-400-unit-3"></a>

## 3. Identidad y límites del runner

Separa código confiable, entradas del PR, permisos del workflow y alcance cloud. Los runners propios necesitan aislamiento, actualización y limpieza. OIDC elimina secretos duraderos, pero exige confianza y autorización precisas.

**Caso:** un PR externo modifica un script que correrá en una red interna. **Evidencia:** ruta de ejecución sin acceso de producción, restricciones de identidad y controles del recurso. No supongas que un archivo de pipeline es inocuo.

<a id="az-400-unit-4"></a>

## 4. Desplegar y recuperar

Compara rolling, blue-green, canary, rings y feature flags. Define población, señales funcionales, tiempo de observación y parada. Un swap no crea una copia independiente de todas las dependencias. Diseña migraciones compatibles con versiones anteriores cuando encaje.

**Caso:** canary con CPU normal y resultados incorrectos. **Evidencia:** señal de negocio que lo detecta y criterio de rollback. Explica por qué volver a una imagen no recupera una columna eliminada.

<a id="az-400-unit-5"></a>

## 5. Cerrar el ciclo operativo

Asegura propagación de contexto, versión en telemetría y protección de datos registrados. Define dueño de alertas y ventanas. Las aprobaciones de recursos no son una simple condición editable por quien escribe YAML.

**Entrega final:** pipeline diseñado de punta a punta, prueba significativa, artefacto fijo y estrategia de promoción. Ejecuta el simulador local, explica fallos y duplica el ejercicio cambiando la política de retry. Postmortem con acción, responsable y comprobación.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400) · [AZ-400](AZ-400.md)
