# SC-100 · Cuaderno de arquitectura de seguridad

[Guía](SC-100.md) · [Diez casos](SC-100-cases.md) · [Contenido](README.md) · [English](../en/SC-100-workbook.md)

Cinco unidades originales sin conexión para el servicio universitario ficticio de apuntes. Usa activos, identidades, incidentes y evidencias inventados. Produce propuestas arquitectónicas y resultados de simulaciones de mesa; no cambies inquilinos, ejecutes ataques, despliegues recursos ni conectes telemetría real. No se afirma ejecución en la nube ni eficacia de controles.

<a id="sc-100-unit-1"></a>

## 1. Establecer criticidad y cobertura de controles

**Escenario:** la universidad añade respuestas no publicadas a una aplicación que antes solo guardaba apuntes públicos. Identifica operaciones críticas, propietarios de datos, amenazas probables e impactos. Distingue el mapa de capacidades MCRA, requisitos MCSB, responsabilidades de plataforma CAF y revisión de cargas Well-Architected. Explicita supuestos sin inventar un inventario completo.

**Evidencias:** diagrama hipotético de activos, tres riesgos prioritarios, límites actuales de control e información pendiente. Incluye un requisito que no pueda evaluarse únicamente con un resultado de Azure Policy.

**Entregable:** tabla con requisito, control, ámbito, responsable, evidencia, carencia y criterio de aceptación. Añade un ADR breve que compare dos opciones e identifique quién puede aceptar el riesgo residual.

<a id="sc-100-unit-2"></a>

## 2. Delimitar identidad, red y privilegios

**Escenario:** usuarios del campus, visitantes, administradores, una canalización de despliegue y un agente acceden a partes diferentes del servicio. Dibuja límites de identidad, aplicación, red y administración entre campus y nubes. Especifica permisos mínimos, activación privilegiada, recuperación y responsables de credenciales o federación. Comprueba funciones y licencias de los controles propuestos para agentes.

**Evidencias:** seis autorizaciones o denegaciones esperadas, dependencias de DNS privado, supuestos de acceso público y explicación de cómo se mantiene la autorización cuando existe conectividad.

**Entregable:** diagrama de confianza y matriz de acceso con responsable, ámbito, ciclo de vida, registros y comportamiento ante fallos. Incluye una acción denegada al agente y una ruta administrativa de recuperación. Todo será ficticio.

<a id="sc-100-unit-3"></a>

## 3. Conectar detección y respuesta autorizada

**Escenario:** actividad sospechosa de identidad coincide con descargas documentales inusuales. Define capacidades SOC necesarias en identidad, dispositivos, aplicación, nube y SaaS. Relaciona dos caminos de amenaza prioritarios con técnicas pertinentes de MITRE ATT&CK, telemetría, correlación, clasificación inicial y contención. Explica responsabilidades de Sentinel y Defender XDR sin suponer visibilidad completa.

**Evidencias:** cronología sintética con orígenes, retraso de ingesta, retención supuesta, señal ausente y explicaciones alternativas. Identifica quién puede deshabilitar una identidad o interrumpir un servidor durante exámenes.

**Entregable:** matriz de cobertura y tabla de autoridad de respuesta con escalado, aprobación, reversión y conservación de evidencias. Marca detecciones y respuestas como propuestas, con las pruebas de aceptación necesarias antes de utilizarlas operativamente.

<a id="sc-100-unit-4"></a>

## 4. Proteger datos y los ciclos de software e IA

**Escenario:** un nuevo asistente recupera documentos y una canalización despliega su API. Clasifica información y representa límites de etiquetas, cifrado, DLP, retención y acceso de aplicación. Indica dónde falta soporte. Modela amenazas de dependencias, identidades de compilación, promoción de artefactos, inyección de instrucciones en documentos y acceso a herramientas.

**Evidencias:** una recuperación sintética legítima, un documento con una instrucción no confiable y una compilación ficticia no aprobada. Registra denegaciones esperadas sin producir instrucciones de explotación ni ejecutar pruebas.

**Entregable:** matriz de controles de datos y revisión del ciclo de vida con responsable, ámbito, procedencia, permisos, aprobación y evidencia de aceptación. Explica los riesgos separados que dejan detección, cifrado y correspondencias con estándares.

<a id="sc-100-unit-5"></a>

## 5. Ensayar recuperación y ordenar el programa

**Escenario:** ransomware afecta al almacén principal y a una cuenta privilegiada. Usa requisitos ficticios de RTO de dos horas y RPO de quince minutos. Traza identidad, plano de control, DNS, claves, configuración, metadatos, archivos y despliegue. Compara puntos protegidos con replicación, considerando corrupción y administración de copias comprometida.

**Evidencias:** orden de restauración de mesa, tiempos hipotéticos, comprobaciones de coherencia y una dependencia que impida lecturas autorizadas incluso después de recuperar archivos. Marca las mediciones como supuestas.

**Entregable:** plan de aceptación de recuperación y hoja de ruta de tres fases limitada a un semestre. Incluye responsables, esfuerzo estimado, dependencias, reversión, excepciones con caducidad y aprobación del riesgo restante. No se valida ninguna restauración u objetivo real.

[Guía oficial SC-100](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100) · [Plantilla ADR](ADR-template.md)
