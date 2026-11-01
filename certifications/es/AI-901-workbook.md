# AI-901 · Cuaderno avanzado común

[Guía](AI-901.md) · [Diez casos](AI-901-cases.md) · [Índice](README.md)

Cinco unidades equivalentes en los idiomas de estudio. Trabaja sin conexión con apuntes universitarios, prompts, transcripciones y respuestas candidatas inventados. Etiqueta cada salida candidata como **sintética** y cada resultado esperado como **predicción**. No subas material real de estudiantes. Este cuaderno no implementa nada ni demuestra cobertura completa del examen. Comprobación de referencias: **1 de noviembre de 2026**; [objetivos vigentes desde el 15 de abril de 2026](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901).

<a id="ai-901-unit-1"></a>

## 1. Define cinco contratos de IA

Escribe un contrato para responder una pregunta de clase, otro para extraer una fecha de entrega, otro para analizar comentarios, otro para aceptar una pregunta hablada y otro para describir un diagrama. Especifica modalidad de entrada, datos permitidos, forma de salida, errores inaceptables y alternativa ante fallos. Compara respuestas generativas, análisis de texto, voz, visión y Content Understanding según lo que producen. Incluye una solicitud de generación de imágenes para distinguir creación e interpretación.

**Escenario:** un compañero propone un solo modelo de imágenes para todas las funciones. **Evidencia:** una matriz de cinco filas con una capacidad justificada y una alternativa descartada por fila. Añade preguntas de selección de modelos sobre modalidades, opciones de implementación, idioma y parámetros admitidos. Marca detalles desconocidos para verificarlos en documentación actual sin inventar límites.

<a id="ai-901-unit-2"></a>

## 2. Escribe prompts fundamentados y reglas de acceso

Inventa tres pasajes breves: un apunte permitido, un cuaderno privado y una página permitida con una instrucción de exportar documentos. Asigna identificadores estables de fuente y dos estudiantes con distintas listas de acceso. Escribe prompts de sistema y usuario que pidan una respuesta respaldada, preserven los límites de las fuentes y permitan abstenerse. La recuperación debe filtrar según el acceso del solicitante antes de construir el contexto; el prompt no puede aportar ese límite de seguridad.

**Escenario:** una pregunta no tiene respuesta en los pasajes permitidos. **Evidencia:** una abstención esperada, un rechazo de acceso prohibido y una respuesta sintética resistente a inyección. Anota qué afirmaciones respalda cada fuente. Explica por qué una cita o un detector de ataques por sí solos no establecen veracidad, privacidad ni permiso.

<a id="ai-901-unit-3"></a>

## 3. Sigue un cliente ligero sin llamadas a la nube

Dibuja una solicitud desde un cliente Python al punto de conexión de Foundry y la implementación configurada previstos, seguida de una respuesta o error. Distingue identidad, autorización, destino y selección de implementación. Esboza pseudocódigo que lea configuración protegida, obtenga credenciales adecuadas, envíe entradas permitidas, compruebe errores y salidas, y presente un resultado seguro. Etiqueta el esquema como **pseudocódigo**, no código ejecutable del SDK. Explica dónde podrían aparecer diccionarios, iteración, excepciones y llamadas asíncronas.

**Escenario:** la autenticación funciona, pero el recurso seleccionado deniega la operación. **Evidencia:** una lista de diagnóstico sin datos sensibles y comportamiento esperado ante acceso denegado, espera agotada, salida vacía y configuración inválida. Compara cómo expresan la misma tarea REST, SDK y CLI. Identifica el [inicio rápido actual del SDK](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) que seguirías después en la nube.

<a id="ai-901-unit-4"></a>

## 4. Valida la extracción multimodal

Inventa una hoja de tareas con fecha final, otra sin fecha, un diagrama con una unidad ilegible y una pregunta hablada con ruido. Define un esquema de plazos con tipos, política de valores ausentes y referencias de fuente. Produce salidas sintéticas deliberadamente erróneas: fecha supuesta, unidad incorrecta y término técnico mal oído. Localiza el fallo en extracción, interpretación visual, reconocimiento o razonamiento posterior. Describe una ruta de reconocimiento de voz y una alternativa multimodal directa compatible.

**Escenario:** una salida es JSON válido, pero contradice la hoja. **Evidencia:** resultados separados de validación de esquema y fuente, reglas de revisión de ambigüedades y una alternativa accesible de texto. Incluye cómo [Content Understanding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) podría procesar documentos, imágenes, audio y vídeo. No uses la confianza como sustituto de la evidencia.

<a id="ai-901-unit-5"></a>

## 5. Evalúa un agente único con herramientas limitadas

Diseña un agente de búsqueda de apuntes con instrucciones, modelo elegido, recuperación limitada al solicitante y sin herramientas de modificación. Define la solicitud y el resultado de su herramienta de búsqueda y cómo un cliente identifica al agente y mantiene el contexto de conversación. Crea una matriz de fallos con al menos seis filas: respuesta respaldada, evidencia ausente, documento denegado, inyección, plazos contradictorios y espera agotada de herramienta. Añade resultados esperados antes de escribir dos respuestas sintéticas alternativas por fila.

**Evidencia final:** entrega contratos, prompts, listas de acceso, esquema del cliente, comprobaciones de extracción y matriz puntuada. Puntúa por separado respaldo factual, citas, abstención o rechazo, privacidad, validez de esquema y permisos de herramientas. Explica una revisión de prompt y su contrapartida. Enumera la práctica real pendiente: implementar un modelo e interactuar en el portal, crear un cliente de chat con SDK, probar un agente único en el portal y crear su cliente. La puntuación sin conexión prepara ese trabajo.
