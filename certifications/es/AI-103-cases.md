# AI-103 · 10 casos de desarrollo con respuestas razonadas

[Guía](AI-103.md) · [Cuaderno](AI-103-workbook.md) · [Contenido](README.md)

Escenarios originales de una aplicación universitaria de apuntes; no son preguntas de examen. Todas las salidas y tiempos propuestos son hipotéticos. Explica la decisión de implementación y la evidencia necesaria antes de abrir cada respuesta. Referencias comprobadas el **1 de noviembre de 2026**.

## 1. Un ejemplo de Python importa correctamente, pero su respuesta carece de una propiedad esperada. ¿Debe el equipo cambiar de implementación hasta que funcione?

<details>
<summary>Respuesta</summary>

Inspecciona primero la versión instalada del SDK, generación de API, operación, punto de conexión y estructura documentada de respuesta. Importar correctamente demuestra poco sobre la compatibilidad con un ejemplo copiado. Fija dependencias coherentes y transforma una respuesta de ejemplo sin datos sensibles al contrato propio de la aplicación. Distingue una propiedad ausente de un fallo de autenticación o una implementación desconocida. Cambiar de modelo no repara un cliente que lee el objeto equivocado. Registra URL de documentación y versiones de paquetes; verifica una llamada real solo en un laboratorio autorizado por separado.

</details>

## 2. Un modelo mayor mejora los resúmenes, pero duplica la latencia hipotética durante los exámenes. ¿Qué modelo debería publicarse?

<details>
<summary>Respuesta</summary>

Usa el mismo conjunto representativo de evaluación y las mismas hipótesis de carga para ambos candidatos. Mide respaldo, exactitud de citas, abstención, salida estructurada, distribución de latencia, rendimiento y recursos. Decide qué requisitos son obligatorios antes de comparar promedios. Un modelo pequeño podría atender preguntas normales y una derivación acotada las difíciles, pero ese enrutamiento también necesita evaluación. Incluye recuperación y reintentos en el presupuesto. Ni el tamaño ni un resumen atractivo establecen la mejor implementación; documenta un equilibrio justificado entre calidad, capacidad, latencia y coste sin inventar precios.

</details>

## 3. Un estudiante pierde acceso a un cuaderno compartido, pero los fragmentos en caché siguen respondiendo. ¿Basta el filtro del índice?

<details>
<summary>Respuesta</summary>

Toda la ruta de recuperación debe aplicar permisos actuales antes de que el contexto llegue al modelo. Inspecciona propagación a fragmentos secundarios, actualizaciones de índice, memoria de conversación y cachés. Las claves de caché necesitan un contexto apropiado de identidad y permisos, y una revocación exige invalidación u otro control de vigencia. Una consulta correcta al índice no protege una respuesta servida desde una caché antigua sin restricciones. Define la vigencia aceptable de permisos y deniega acceso si no se cumple. Demuestra la denegación con dos identidades sintéticas y una traza antes y después de revocar.

</details>

## 4. Una respuesta cita el PDF correcto, pero atribuye una fecha a un párrafo que solo define un algoritmo. ¿La presencia de una cita supera la evaluación?

<details>
<summary>Respuesta</summary>

No. Valida que el pasaje y su versión respalden realmente la afirmación. Existencia de fuente, pertinencia y respaldo son comprobaciones distintas. Inspecciona si la recuperación omitió la página de la tarea, si la división perdió contexto o si la generación inventó una fecha pese a disponer de evidencia suficiente. La aplicación debe abstenerse cuando sus pasajes autorizados carecen de la fecha. Conserva el fallo en las pruebas de regresión y puntúa las citas por separado de la legibilidad. Un enlace que se abre ayuda a navegar, pero no demuestra fundamentación.

</details>

## 5. Un agente agota el tiempo tras solicitar compartir; el backend ya creó el acceso. ¿Debe el cliente reintentar inmediatamente?

<details>
<summary>Respuesta</summary>

Trata el resultado como desconocido hasta reconciliarlo. Asigna a la operación aprobada una clave estable de idempotencia y registra su estado independientemente de la respuesta del modelo. Consulta o recupera ese estado antes de reenviar; los reintentos no deben crear otro acceso. Vincula la aprobación a documentos, destinatarios y versiones exactos, y vuelve a comprobar autorización al ejecutar. Distingue el plazo de la herramienta del presupuesto total del agente. Recoge identificadores de correlación depurados para conectar solicitud, aprobación, finalización y respuesta perdida sin exponer contenido del estudiante.

</details>

## 6. Un agente planificador delega en otro de recuperación que puede leer todas las asignaturas. ¿El prompt restringido del planificador conserva los permisos del estudiante?

<details>
<summary>Respuesta</summary>

La transferencia debe llevar un contexto confiable del solicitante, y la herramienta de recuperación debe aplicar sus permisos. Un prompt del planificador no limita de forma fiable un servicio posterior privilegiado. Define roles, alcance de herramientas, campos permitidos en transferencias, propiedad de memoria y presupuesto de terminación. Devuelve al planificador solo evidencia autorizada e impide reutilizar memoria de otro estudiante. Prueba una solicitud a una asignatura denegada y una transferencia con inyección. Delegar puede repartir responsabilidades, pero nunca debe ampliar silenciosamente el acceso del usuario final.

</details>

## 7. La aplicación necesita describir una gráfica y crear un cartel de repaso. ¿Pueden usar el mismo contrato visual?

<details>
<summary>Respuesta</summary>

Define contratos separados para comprender evidencia existente y crear medios nuevos, aunque una plataforma admita ambas cosas. La respuesta sobre la gráfica necesita respaldo en etiquetas, unidades y relaciones visibles, y abstención en zonas ilegibles. El cartel requiere controles de generación, derechos adecuados sobre fuentes, controles de seguridad y revisión de texto y diagramas generados. Las variantes de vídeo necesitan además semántica de segmentos o edición. Evalúa la utilidad del texto alternativo y evita inferir detalles invisibles. Una ilustración convincente no valida afirmaciones sobre la gráfica original.

</details>

## 8. El reconocimiento cambia «mutex» por «music» y la traducción produce después un sinsentido fluido. ¿Basta revisar el prompt de traducción?

<details>
<summary>Respuesta</summary>

Inspecciona cada etapa contra su contrato. Un error anterior de reconocimiento puede convertirse en una traducción fluida pero incorrecta y en una mala respuesta. Construye ejemplos con vocabulario técnico, ruido, negaciones e interrupciones; conserva una vía de corrección textual y comprueba la personalización especializada admitida por el servicio. Si el diseño multimodal directo no expone transcripción, evalúa de extremo a extremo la misma conservación del significado. Registra fallos por idioma en lugar de ocultarlos en promedios. Revisa un prompt solo después de identificar la etapa y medir el efecto.

</details>

## 9. Content Understanding devuelve con confianza alta la fecha del borrador en `final_due_date`. ¿Puede continuar la propuesta de calendario?

<details>
<summary>Respuesta</summary>

El valor incumple el significado previsto del campo pese a su confianza. Define claramente la entrega final, inspecciona su fundamentación en el documento y compara ejemplos etiquetados de borrador y entrega final. Valida formato, valores ausentes y coherencia con otros hitos. Envía las ambigüedades no resueltas a revisión; la confianza es una estimación, no una decisión de negocio. Verifica que la API y configuración elegidas exponen la evidencia necesaria. Una acción posterior de calendario o compartir también necesita autorización y aprobación propias, independientemente de la calidad de extracción o de un JSON válido.

</details>

## 10. Una publicación cambia prompt, modelo de embeddings y esquema de respuesta de herramientas; aumentan los fallos de citas. ¿Basta revertir el prompt?

<details>
<summary>Respuesta</summary>

Usa el manifiesto de publicación para identificar todos los componentes cambiados y su compatibilidad. Una nueva representación de embeddings puede exigir reindexación, mientras un cliente antiguo puede interpretar mal un resultado nuevo. Compara trazas y casos de regresión para localizar el fallo; restaura después un conjunto compatible conocido o ejecuta la migración documentada. Define antes del despliegue gradual activadores de reversión para fundamentación, acceso, errores de herramientas y latencia. Conserva versiones en telemetría depurada. Revertir un prompt visible no repara de forma fiable cambios de recuperación o contratos de respuesta.

</details>

Fuentes: [objetivos actuales](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103), [SDK y puntos de conexión](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview), [evaluación](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation), [acceso a documentos](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview), [llamadas a funciones](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling), [diseño de analizadores](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/best-practices), [confianza y fundamentación](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/document/analyzer-improvement).
