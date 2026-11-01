# AI-103 · Cuaderno avanzado de desarrollo

[Guía](AI-103.md) · [Diez casos](AI-103-cases.md) · [Contenido](README.md)

Cinco unidades equivalentes usan apuntes universitarios inventados y ejemplos de solicitudes y respuestas sin conexión. Marca las salidas candidatas como **sintéticas** y los comportamientos esperados como **predicciones**. No se necesitan recursos de nube, credenciales, expedientes reales ni mediciones del servicio. Los ejercicios desarrollan capacidades seleccionadas sin afirmar cobertura completa. Comprobado el **1 de noviembre de 2026** contra los [objetivos vigentes desde el 16 de abril de 2026](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103).

<a id="ai-103-unit-1"></a>

## 1. Fija un contrato de cliente y una decisión de implementación

**Escenario:** la aplicación debe devolver una respuesta fundamentada desde un backend de Python durante el pico de repaso. Define ejemplos de solicitud y respuesta con contexto de identidad, ID de solicitud, asignatura, resultado, respuesta, citas y categorías de error. Incluye JSON no válido, acceso denegado, tiempo agotado y salida parcial. Crea un manifiesto de compatibilidad con recurso/proyecto, tipo de punto de conexión, nombre de implementación, generación de API, versiones de paquetes y enfoque de credenciales, usando la [guía actual del SDK](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview).

**Evidencia:** compara dos candidatos hipotéticos en calidad, funciones admitidas, capacidad, latencia y recursos; señala incógnitas para verificarlas después. **Entregable:** esquema de contrato con tipos, cuatro ejemplos de fallo y una decisión justificada sin inventar límites o precios.

<a id="ai-103-unit-2"></a>

## 2. Diseña la recuperación hasta la revocación de acceso

**Escenario:** dos estudiantes comparten un cuaderno hasta que se revoca el acceso de uno. Inventa seis pasajes, incluido un matiz de una tarea separado por un límite propuesto de fragmento. Define ID de documentos y fragmentos, versiones, ubicaciones, metadatos ACL y versión de índice/embeddings. Compara predicciones de búsqueda por palabras, vectores e híbrida. Dibuja autenticación, filtrado de permisos, recuperación, consulta de caché y contexto del modelo en su orden real.

**Evidencia:** tabla de acceso antes y después que cubra propagación al índice, caché y memoria, más una cita sin respaldo y una respuesta sin evidencia. **Entregable:** diseño con política de vigencia, invalidación y cuatro casos de regresión. Explica cómo los [patrones de acceso de Search](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) afectan a la elección de implementación.

<a id="ai-103-unit-3"></a>

## 3. Traza una herramienta aprobada con resultado incierto

**Escenario:** un agente propone compartir un documento permitido con un grupo de estudio. Define esquema de herramienta, alcance del solicitante, contenido exacto de aprobación, clave de operación, almacén de estado, presupuesto de espera y propiedad de conversación. Esboza **pseudocódigo** para validar → autorizar → aprobar → ejecutar → reconciliar → informar; es diseño de aplicación, no código SDK ejecutable. Añade una transferencia entre planificador y recuperador que conserve los permisos.

**Evidencia:** trazas de rechazo, ejecución correcta, entrega duplicada, aprobación caducada y respuesta perdida tras éxito del backend. **Entregable:** tabla de estados y traza depurada que expliquen por qué un reintento no duplica el acceso compartido. Relaciona el diseño con el [límite actual de llamadas a funciones](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling).

<a id="ai-103-unit-4"></a>

## 4. Valida campos multimodales y significado

**Escenario:** una tarea tiene fechas de borrador y entrega final, una gráfica muestra un eje ilegible y una pregunta hablada contiene «mutex». Define contratos separados de texto, voz, comprensión visual, generación de medios y extracción. Escribe un esquema de campos de Content Understanding con descripciones precisas, tipos, tratamiento de nulos y referencias. Construye salidas sintéticas erróneas: fechas intercambiadas, una unidad inventada y un término mal reconocido.

**Evidencia:** comprobaciones separadas de esquema, fuente, significado y accesibilidad, incluido un campo erróneo con confianza alta y una alternativa de corrección textual. **Entregable:** cinco ejemplos anotados y una política de revisión calibrada con ejemplos etiquetados. Consulta [diseño de analizadores](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/best-practices) y [disponibilidad de fundamentación documental](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/document/analyzer-improvement), explicitando límites de modalidad y API.

<a id="ai-103-unit-5"></a>

## 5. Evalúa y ensaya una reversión

**Escenario:** una publicación candidata cambia prompts, esquemas de herramientas y un modelo de embeddings. Puntúa ocho casos fijos: respuesta respaldada, fuente ausente, acceso revocado, inyección, cita incorrecta, fecha ambigua, tiempo agotado de herramienta y acción duplicada. Separa calidad de recuperación, respaldo de afirmaciones, seguridad, cumplimiento de permisos y predicciones de latencia. Describe un despliegue gradual acotado y las métricas que activarían recuperación.

**Evidencia:** tabla comparativa, manifiesto compatible, esquema de telemetría depurada y secuencia de reversión que restaure juntos cliente, índice, prompt y herramientas. **Entregable:** paquete revisable de publicación y lista de mediciones pendientes de un laboratorio autorizado. Usa la [guía de evaluación](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation) para distinguir predicciones sin conexión y evidencia observada; no presentes puntuaciones sintéticas como resultados de Azure.
