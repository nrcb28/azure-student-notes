# SC-300 · Cuaderno de decisiones de acceso y gobernanza

[Guía](SC-300.md) · [Diez casos](SC-300-cases.md) · [Índice](README.md)

Cinco unidades originales sin conexión para una aplicación universitaria ficticia de apuntes. Utiliza identidades y documentos sintéticos. No cambies directivas, crees credenciales, actives roles ni conectes telemetría real. Los entregables describen decisiones esperadas; no se afirma ejecución en la nube.

<a id="sc-300-unit-1"></a>

## 1. Seguir acceso efectivo y orígenes de identidad

Representa inquilino, suscripción, aplicación y almacén de documentos. Separa roles de directorio, ámbito de unidad administrativa, roles de recursos y datos Azure, y derechos de aplicación. Incluye vías directas y por grupos e identifica quién controla la pertenencia. Para identidad híbrida, registra origen autoritativo y supuestos de sincronización y autenticación; no interpretes sincronización como concesión.

**Escenario:** un estudiante pierde una asignación directa pero aún lee una carpeta. **Pruebas:** diagrama con dos posibles vías de concesión y registros para distinguirlas. **Entregable:** matriz de seis filas para estudiante, invitado, editor, administrador, indexador y antiguo miembro, con ámbito mínimo y una denegación esperada por identidad.

<a id="sc-300-unit-2"></a>

## 2. Diseñar autenticación y Acceso condicional

Especifica método compatible, registro y responsable de recuperación. Explica resistencia al phishing y cómo un TAP podría iniciar el registro de un usuario elegible sin almacenar códigos reales. Describe destinatarios, condiciones, controles de concesión y sesión, exclusiones, licencias y recuperación de emergencia. Separa evaluaciones de solo informe de resultados aplicados.

**Escenario:** un profesor visitante utiliza dispositivo personal y un editor maneja soluciones inéditas. **Pruebas:** tres solicitudes esperadas con identidades, métodos, dispositivos o recursos diferentes; explica confianza entre inquilinos aparte del derecho de aplicación. **Entregable:** matriz de directivas propuesta y nota de despliegue con criterios de piloto, revisión, recuperación y reversión. No se habilita nada en un inquilino real.

<a id="sc-300-unit-3"></a>

## 3. Elegir y limitar identidades de cargas de trabajo

Compara registro de aplicación, entidad de servicio e identidad administrada para el indexador. Explica permisos delegados y de aplicación, consentimiento y ámbito de recursos. En una compilación externa ficticia, documenta emisor, sujeto y audiencia previstos con valores inventados. Explica por qué emitir un token no prueba permiso de despliegue.

**Escenario:** el indexador lee solo apuntes publicados y la compilación actualiza solo su aplicación de pruebas. **Pruebas:** una operación permitida y otra rechazada por carga, responsable de permisos y fecha de revisión. **Entregable:** tabla de elección de identidad y esquema de confianza federada sin contraseñas, secretos, tokens reales ni órdenes de despliegue. Registra supuestos no verificados como preguntas para el responsable.

<a id="sc-300-unit-4"></a>

## 4. Construir el ciclo de vida de derechos y privilegios

Separa elegibilidad PIM, activación y duración activa de las revisiones periódicas. Propón un paquete de acceso para profesores visitantes y automatización compatible de altas, cambios y bajas. Distingue federación SSO y aprovisionamiento SCIM; explica cómo confirmar la retirada en destino. Enumera licencias específicas y responsables de fallos de automatización.

**Escenario:** termina el semestre de un profesor y un administrador necesita mantenimiento temporal. **Pruebas:** decisión de caducidad, revisión del propietario, propuesta de activación limitada y registro de finalización del aprovisionamiento en destino. **Entregable:** tabla con desencadenador, aprobador, derecho, duración, revisión, retirada prevista, pruebas y excepciones. Una revisión completada no prueba activación de rol.

<a id="sc-300-unit-5"></a>

## 5. Explicar un fallo con pruebas delimitadas

Separa riesgo de usuario, riesgo de inicio, evaluación de directivas, cambios de directorio y fallos de aprovisionamiento. Elige registros y describe supuestos de diagnóstico, retención, acceso y esquema. Anota qué permite y qué no permite establecer el agregado de la consulta KQL hipotética de la guía. Añade Private Access, Internet Access o perfil Microsoft solo si corresponde a la ruta del recurso.

**Escenario:** un invitado no abre una asignatura y el panel no muestra fallos coincidentes. **Pruebas:** cronología hipotética, lagunas, campos de correlación y dos explicaciones alternativas. **Entregable:** diagnóstico de una página y lista de pruebas que conecte identidad, red, directiva, derecho y aprovisionamiento. Marca resultados como esperados; no se ejecutan consultas ni pruebas en inquilinos.

[Guía de Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) · [Fundamentos de identidad](../../es/06-identity.md)
