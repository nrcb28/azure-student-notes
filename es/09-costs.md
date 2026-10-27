# Costes y optimización

No elegiría una arquitectura solo por el precio que aparece junto al servicio. Hay que contar almacenamiento, operaciones, red, monitorización y tiempo de mantenimiento.

## De dónde sale la factura

- Capacidad de cómputo reservada o consumida, según el servicio.
- Espacio ocupado y operaciones de almacenamiento.
- Transferencias y procesamiento de red aplicables.
- Bases de datos, copias y retención.
- Ingesta y retención de logs.
- Licencias y planes adicionales.

Las tarifas dependen de región, moneda, contrato y momento. Estos apuntes no incluyen precios fijos.

## Herramientas

La calculadora de precios ayuda a estimar escenarios. Cost Management permite analizar gasto real y tendencias. Un presupuesto puede avisar de umbrales, pero no detiene automáticamente todos los recursos.

Los datos de facturación pueden tener retraso. No usaría el presupuesto como único mecanismo para evitar gasto inesperado.

## Decisiones que sí ayudan

1. Medir el uso antes de aumentar tamaño.
2. Eliminar recursos de prueba que ya no se necesitan.
3. Elegir retención y redundancia según requisitos.
4. Programar apagado o desasignación cuando encaje.
5. Revisar compromisos de consumo solo con una carga suficientemente predecible.

Las reservas y savings plans tienen condiciones distintas: no hay que asumir que cualquier recurso o consumo queda cubierto. Spot puede ser útil para trabajo interrumpible, pero la capacidad puede retirarse.

## La trampa de las VM

Apagar desde el sistema operativo puede dejar una VM asignada. Al desasignarla deja de facturarse el cómputo correspondiente, pero discos y otros recursos pueden seguir cobrando.

**Caso de clase:** para un laboratorio corto, un servicio sobredimensionado puede costar más por estar olvidado que por la práctica en sí.

**Repaso:** ¿sin peticiones significa sin coste? Depende del servicio y del plan.

## Ejemplo de comparación sin inventar tarifas

Para una alternativa A y otra B, modelaría coste como capacidad base más consumo más datos y operación. Después variaría horas, tráfico y retención.

Una opción puede ganar con uso estable y perder con uso ocasional. Añadir recuperación regional también cambia almacenamiento, red y pruebas. La arquitectura barata sin cumplir requisitos no es una comparación válida.

## Higiene del laboratorio

Al terminar, revisar grupos y recursos creados. Una VM eliminada puede dejar discos o direcciones según opciones y procedimiento. En otros servicios, revisar planes, registros y retención.

La facturación puede tardar en reflejar cambios. Conservar evidencias de eliminación ayuda a distinguir coste residual de recursos que siguen activos.

**Ejercicio:** prepara tres escenarios, bajo, esperado y alto, sin poner cifras de precio no verificadas. Enumera las unidades a medir y qué parte de la factura cambia en cada uno.

---

[Índice](README.md) · [Otro idioma](../en/09-costs.md) · [Anterior](08-observability.md) · [Siguiente](10-architecture.md)
