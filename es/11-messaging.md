# Mensajería y eventos

Una petición HTTP directa obliga a que el receptor esté disponible en ese momento. Una cola permite dejar trabajo pendiente para que otro componente lo procese después.

## Qué elegir

| Servicio | Problema habitual |
|---|---|
| Storage Queues | Colas de trabajo sencillas |
| Service Bus | Mensajería con colas, temas y características empresariales |
| Event Grid | Distribuir eventos sobre algo que ha ocurrido |
| Event Hubs | Ingerir grandes flujos de eventos, como telemetría |

No elegiría Event Hubs como sustituto automático de una cola de pedidos. Su modelo de particiones, retención y consumidores responde a otro tipo de problema.

En Service Bus, una cola distribuye trabajo entre consumidores. Un tema permite publicar y crear suscripciones para diferentes destinatarios, con filtros cuando corresponda.

## Entrega y duplicados

No hay que asumir que cada mensaje se ejecutará exactamente una vez. Un consumidor puede completar el trabajo y fallar antes de confirmar su recepción.

Para generar una miniatura:

1. El mensaje incluye el identificador del documento.
2. El consumidor comprueba si ya existe el resultado esperado.
3. Procesa y guarda de forma consistente.
4. Confirma el mensaje cuando ha terminado.

La idempotencia evita que una repetición cambie indebidamente el resultado. La detección de duplicados de un broker no sustituye todo el diseño de idempotencia.

## Mensajes que fallan

Limitar reintentos y estudiar las causas. Los mecanismos de dead-letter o mensajes problemáticos varían por servicio; no todos ofrecen lo mismo automáticamente.

En una cola de trabajo, monitorizaría la antigüedad de los mensajes además de su cantidad. Diez mensajes bloqueados durante horas pueden ser peores que mil procesados en segundos.

**Caso de clase:** subir el PDF devuelve una respuesta rápida; el análisis se hace en segundo plano. La interfaz debe mostrar que el documento sigue procesándose.

**Repaso:** la asincronía mejora el desacoplamiento, pero añade estados y fallos que gestionar.

---

[Índice](README.md) · [Otro idioma](../en/11-messaging.md) · [Anterior](10-architecture.md) · [Siguiente](12-devops.md)
