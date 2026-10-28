# AZ-305 · Cuaderno avanzado común

[←](README.md) · [Núcleo común de estudio](../../es/16-common-core.md) · [Laboratorios avanzados](../../es/17-advanced-labs.md)

Este bloque tiene los mismos objetivos, escenarios y entregables en los ocho idiomas. La equivalencia se comprueba por unidades y evidencias, no por número de palabras. Las guías anteriores siguen disponibles como explicación complementaria.

<a id="az-305-unit-1"></a>

## 1. Convertir necesidades en restricciones

Define usuarios, crecimiento, residencia, privacidad, rendimiento, RTO, RPO, presupuesto y capacidad operativa. Separa requisito verificado de supuesto. Una frase como siempre disponible necesita operación y ventana de medición.

**Caso:** cinco facultades comparten red pero tienen datos privados. **Evidencia:** límites de administración y datos, propietarios y un requisito que obliga a separar componentes. No elijas una arquitectura empresarial por su tamaño.

<a id="az-305-unit-2"></a>

## 2. Diseñar datos y estado

Compara consultas, transacciones, compatibilidad, consistencia y recuperación. JSON no determina el motor. Escalar lecturas no aumenta necesariamente escrituras. Define qué estado pertenece a la aplicación, a la sesión o al documento.

**Caso:** una caché acelera lecturas pero sirve permisos antiguos. **Evidencia:** estrategia de invalidación, expiración y respuesta ante caída del caché. Explica qué datos no deberían confiar en una copia desactualizada.

<a id="az-305-unit-3"></a>

## 3. Diseñar recuperación completa

Asigna RTO y RPO por dato y servicio. Incluye restauración de capacidad, credenciales, permisos, DNS y configuración. La replicación puede propagar daños lógicos. Compara activo-activo y activo-pasivo con costes y complejidad.

**Caso:** vuelve Key Vault pero no las integraciones necesarias. **Evidencia:** orden de recuperación y prueba del consumidor autorizado. Documenta dependencias que no se restauran automáticamente y un método seguro de ensayo.

<a id="az-305-unit-4"></a>

## 4. Elegir ejecución y comunicación

Compara VM, PaaS, contenedores y tareas batch con control, duración y operación. Una cola desacopla, pero introduce estados y duplicados. Diseña timeout, retry acotado e idempotencia antes de aumentar consumidores.

**Caso:** respuesta de guardado perdida y mensaje repetido. **Evidencia:** identificador estable, límite de reintentos y manejo de procesamiento parcial. Justifica cuándo necesitas un clúster y cuándo una plataforma más simple basta.

<a id="az-305-unit-5"></a>

## 5. Migrar con decisión documentada

Inventaría dependencias y uso, valida compatibilidad, realiza piloto y diseña transferencia inicial, cambios posteriores, cutover y rollback. Determina cómo demostrar integridad y cuándo retirar el origen. Una VM sin su dependencia de archivos no completa una migración.

**Entrega final:** dos ADR, diseño de red y recuperación y tabla de riesgos. Cada decisión incluye alternativa razonable, consecuencia, prueba y condición de revisión. Cambia presupuesto o residencia y vuelve a evaluar.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305) · [AZ-305](AZ-305.md)
