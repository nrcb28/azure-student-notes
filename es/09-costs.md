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

---

[Índice](README.md) · [Otro idioma](../en/09-costs.md) · [Anterior](08-observability.md) · [Siguiente](10-architecture.md)
