# Monitorización y diagnóstico

Cuando una aplicación falla, decir que el servidor está encendido aporta poco. Necesitamos ver la petición, sus dependencias y el efecto sobre el usuario.

## Señales

- **Métricas:** series numéricas, como CPU o número de errores.
- **Logs:** registros con contexto sobre lo ocurrido.
- **Trazas:** relación entre operaciones de una petición distribuida.

Azure Monitor reúne capacidades de monitorización. Application Insights ayuda a observar aplicaciones. Log Analytics permite consultar registros mediante KQL cuando los datos se envían a las tablas correspondientes.

## Ejemplo de consulta

Si Application Insights envía peticiones a la tabla AppRequests de un workspace:

```kusto
AppRequests
| where TimeGenerated > ago(1h)
| summarize Requests = sum(ItemCount),
            Failed = sumif(ItemCount, Success == false)
  by bin(TimeGenerated, 5m)
| order by TimeGenerated asc
```

El esquema depende del origen y del contexto de consulta. En otras experiencias puede aparecer la tabla requests con nombres de columnas distintos. ItemCount ayuda a tener en cuenta el muestreo cuando corresponde.

## Alertas útiles

Una alerta necesita una condición, un ámbito y una acción. Un action group define notificaciones o acciones.

Preferiría alertar por errores sostenidos o latencia relevante para el usuario antes que generar avisos constantes por pequeñas variaciones de CPU.

- **Service Health:** incidencias, mantenimiento y avisos que afectan a servicios de Azure utilizados.
- **Resource Health:** estado de un recurso concreto.
- **Estado público de Azure:** visión más general de incidentes.

## Método de diagnóstico

1. Delimitar cuándo empezó y a quién afecta.
2. Comprobar el último cambio.
3. Seguir una petición y revisar dependencias.
4. Validar la hipótesis con datos.
5. Corregir y comprobar recuperación.

**Error frecuente:** registrar tokens, contraseñas o documentos completos para depurar. Hay que limitar y proteger los datos registrados.

**Repaso:** una CPU baja no descarta una base de datos lenta.

## Ejemplo resuelto: la media esconde el problema

Nueve peticiones tardan 100 ms y una tarda 10 segundos. La media no describe bien la experiencia de quien espera diez segundos. Miraría distribución, percentiles y volumen, sin interpretar un percentil de una muestra minúscula como evidencia sólida.

Para comparar versiones, mantendría contexto: número de peticiones, rutas y periodo. Una caída de errores acompañada de una caída total del tráfico puede ser una mala noticia.

## Coste de observar

Enviar todos los logs con máxima verbosidad puede elevar coste y exponer datos. Elegir categorías, muestreo cuando sea adecuado, retención y acceso.

OpenTelemetry puede ayudar a instrumentar señales de forma consistente. Su configuración depende del runtime y de la integración: los ejemplos de SDK antiguos necesitan revisión de soporte.

**Ejercicio:** define tres señales para la subida de documentos: éxito, latencia y tiempo de procesamiento. Explica umbral, periodo y acción sin utilizar solamente la CPU.

---

[Índice](README.md) · [Otro idioma](../en/08-observability.md) · [Anterior](07-governance.md) · [Siguiente](09-costs.md)

## Ampliación desde Microsoft Learn · dcr

Las data collection rules describen recogida y encaminamiento en escenarios compatibles. Pueden incluir transformaciones para filtrar o modificar datos antes del destino. No todas las señales usan el mismo camino; no hay que confundir DCR con una sustitución universal de diagnostic settings.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview) · [Ampliación desde Microsoft Learn](15-microsoft-learn.md#learn-dcr)
