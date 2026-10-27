# Plantilla ADR: decisión de arquitectura

[Certificaciones](README.md) · [English](../en/ADR-template.md)

## Título y estado

Una frase concreta. Estado: propuesta, aceptada o sustituida. Fecha y responsables.

## Contexto

Qué problema se resuelve y qué restricciones no podemos ignorar. Distinguir hechos de supuestos.

## Requisitos verificables

Disponibilidad, rendimiento, recuperación, residencia, seguridad, operación y presupuesto. Indicar cuáles todavía necesitan confirmación.

## Opciones

Comparar al menos dos alternativas razonables. No construir una alternativa artificialmente mala para justificar la elegida.

| Criterio | Opción A | Opción B |
|---|---|---|
| Cumplimiento de requisitos | Evidencia pendiente | Evidencia pendiente |
| Operación | Trabajo necesario | Trabajo necesario |
| Coste | Unidades y supuestos | Unidades y supuestos |
| Recuperación | Procedimiento | Procedimiento |
| Límites | Limitaciones | Limitaciones |

## Decisión

Qué se elige, por qué y qué requisito decide.

## Consecuencias

Ventajas, trabajo adicional, riesgos aceptados y mecanismos de mitigación.

## Validación

Qué prueba o medición confirmará el supuesto principal. Quién la ejecuta y qué resultado se considera aceptable.

## Condición de revisión

Cambio de carga, normativa, equipo, precio, soporte o requisito que obliga a revisar.

## Ejemplo breve

Elegimos una API administrada para reducir mantenimiento del SO porque el equipo es pequeño y el runtime es compatible. Revisaremos la decisión si aparece una dependencia que exige acceso al kernel. Antes de aceptar, probaremos carga, conectividad y recuperación de configuración.
