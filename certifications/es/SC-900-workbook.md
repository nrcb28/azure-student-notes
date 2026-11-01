# SC-900 · Cuaderno de decisiones y evidencia

[Guía](SC-900.md) · [Diez casos](SC-900-cases.md) · [Índice](README.md)

Cinco unidades propias para aplicar los mismos objetivos en cada idioma. Usa una universidad ficticia y datos sintéticos. Son ejercicios de diseño sin conexión: no se afirma despliegue de políticas, modificación de un tenant ni ejecución completada en Azure.

<a id="sc-900-unit-1"></a>

## 1. Dibujar responsabilidades y límites de confianza

Dibuja navegador, proveedor de identidad, aplicación y almacén de documentos. En cada límite, describe qué se verifica y quién opera el control correspondiente. Separa las tareas de plataforma del proveedor de las decisiones de la organización sobre usuarios, compartición, configuración y datos. Explica por qué una red del campus no demuestra que deba confiarse en una petición.

**Caso:** un invitado debe leer apuntes publicados, pero nunca soluciones sin publicar. **Evidencia:** un diagrama y una tabla con dos operaciones permitidas y dos denegadas, sus responsables y las observaciones necesarias para verificarlas. **Entrega:** una página que distinga resultados esperados de los realmente observados. No pruebes contra un tenant real para este ejercicio.

<a id="sc-900-unit-2"></a>

## 2. Diseñar una decisión de acceso

Especifica tipo de identidad, aplicación, acción solicitada y permiso mínimo. Propón un requisito de autenticación y explica sus categorías de factores y su resistencia al phishing. Describe qué señales de acceso condicional importarían y qué comprobaciones de aplicación seguirían siendo necesarias. Documenta ámbito, exclusiones, recuperación y dependencias de licencias en vez de escribir «activar MFA para todos».

**Caso:** una profesora invitada accede a material desde un dispositivo personal. **Evidencia:** decisiones esperadas para una petición permitida, un método de autenticación insuficiente y una petición fuera de sus permisos. **Entrega:** una matriz de acceso razonada. Mantén el ejercicio hipotético; no cambies controles del tenant ni trates observaciones de solo informe como decisiones aplicadas.

<a id="sc-900-unit-3"></a>

## 3. Separar privilegio, permiso y riesgo

Escribe tres preguntas: quién puede activar un rol privilegiado, quién debe conservar acceso a un proyecto y qué comportamiento de identidad merece investigación. Relaciónalas con los conceptos correspondientes de PIM, revisión de acceso y riesgo de identidad. Define un ámbito y duración de rol sin asumir que un rol amplio de corta duración sea automáticamente mínimo.

**Caso:** una antigua integrante continúa en un grupo, mientras un administrador necesita acceso temporal de mantenimiento. **Evidencia:** origen de permisos, decisión del dueño del recurso, proceso de activación propuesto y registros separados de comportamiento sospechoso, si existe. **Entrega:** un pequeño runbook con quién aprueba cada decisión y cómo confirmar su finalización. No crees asignaciones privilegiadas como parte del cuaderno.

<a id="sc-900-unit-4"></a>

## 4. Planificar detección y una respuesta acotada

Elige una cadena de ataque hipotética que incluya correo, identidad y una carga de trabajo. Lista los eventos necesarios para apoyar o descartar la hipótesis. Explica dónde ayuda la correlación de Defender XDR y dónde serían relevantes los conectores, análisis y orquestación de Sentinel. Marca los datos ausentes; un resultado vacío no demuestra que un evento nunca ocurriera.

**Caso:** aparece actividad sospechosa de inicio de sesión tras un correo de phishing. **Evidencia:** cronología, cobertura de fuentes, analista responsable y una notificación propuesta antes de acciones que interrumpan el servicio. **Entrega:** tabla de detección y respuesta con falsos positivos y recuperación. No se ingieren datos, activan servicios de pago ni bloquean cuentas automáticamente en este ejercicio.

<a id="sc-900-unit-5"></a>

## 5. Seguir el ciclo de vida del dato sensible

Sigue un documento sintético desde su creación hasta uso interno, compartición, investigación y eliminación final. Distingue clasificación, protección configurada, tratamiento DLP, retención, evidencia de auditoría y eDiscovery. Registra las cargas y licencias asumidas detrás de cada capacidad. Una puntuación de cumplimiento no sustituye la determinación de las obligaciones reales de la organización.

**Caso:** una hoja ficticia de soluciones debe seguir privada hasta publicarse y hay mensajes que preservar para una investigación. **Evidencia:** decisiones de tratamiento, registros de actividad necesarios, supuestos de retención y un responsable. **Entrega:** tabla del ciclo de vida que explique por qué una sola etiqueta, registro o copia de seguridad no satisface todo. Trata las obligaciones legales como requisitos proporcionados por un responsable autorizado.

[Guía de Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900)
