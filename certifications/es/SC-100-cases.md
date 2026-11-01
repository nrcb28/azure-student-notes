# SC-100 · Diez casos de arquitectura

[Guía](SC-100.md) · [Cuaderno](SC-100-workbook.md) · [Contenido](README.md) · [English](../en/SC-100-cases.md)

Preguntas hipotéticas originales para la aplicación universitaria de apuntes. Explica requisito de negocio, límite del control, responsable y evidencia de aceptación antes de abrir la respuesta. Son ejercicios de diseño sin conexión, no preguntas oficiales del examen ni afirmaciones de controles ejecutados.

## 1. Un decano quiere la máxima puntuación de seguridad antes de proteger respuestas no publicadas. ¿Cómo se establecen las prioridades?

<details>
<summary>Respuesta</summary>

Empieza por el impacto de divulgar las respuestas y los caminos que podrían exponerlas. Identifica al propietario de los datos, accesos actuales, identidades privilegiadas, vías de uso compartido y evidencias disponibles. Una puntuación puede revelar carencias, pero no asigna las prioridades del negocio. Propón controles que reduzcan la exposición crítica y define aceptación mediante pruebas acotadas de acceso y evidencias revisables de configuración. Registra costes, riesgos residuales y la decisión autorizada del decano. Priorizar una recomendación ajena y de menor impacto exige una razón defendible, no solo subir la puntuación más fácilmente.

</details>

## 2. La API utiliza un punto de conexión privado. ¿Puede declararse completa la arquitectura de Confianza cero?

<details>
<summary>Respuesta</summary>

La conectividad privada limita un camino de red; no establece identidad, autorización de aplicación ni aislamiento integral. Comprueba si sigue activo el acceso público, cómo resuelven DNS el campus y el entorno de recuperación, y quién alcanza el punto privado. Después define autenticación de usuarios, permisos de cargas, requisitos de dispositivo aplicables y acceso por asignatura. Incluye administración y salidas. La aceptación debe contener solicitudes autorizadas y denegadas y evidencias para distinguir fallos de red de denegaciones de permisos. Documenta los límites pendientes en lugar de presentar una función como estrategia completa.

</details>

## 3. El indexador y el agente de IA comparten una cuenta administradora. ¿Qué debe cambiar en el diseño?

<details>
<summary>Respuesta</summary>

Asigna a cada carga una identidad diferenciable, responsable, ciclo de vida y límite de permisos. El indexador necesita documentos publicados permitidos; el agente, solo recuperación y herramientas necesarias. Evalúa identidades administradas, federación y controles de identidad de agente compatibles según esos requisitos. Elimina la dependencia de una cuenta humana y define caducidad o revocación. Autenticarse correctamente no debe implicar amplio acceso a datos o despliegues. Las evidencias de aceptación deben mostrar operaciones permitidas, denegaciones entre asignaturas, actividad atribuible y recuperación si una identidad deja de estar disponible.

</details>

## 4. Sentinel recibe alertas de nube, pero ningún evento del directorio del campus. ¿Es adecuada la arquitectura del SOC?

<details>
<summary>Respuesta</summary>

Depende de las amenazas prioritarias y la cobertura documentada. Si comprometer el directorio del campus afecta al servicio, su falta de telemetría representa una carencia relevante. Relaciona esa amenaza con señales esperadas, dependencias de ingesta, retención, detección, clasificación inicial y autoridad de contención. Explica la aportación de Defender XDR y Sentinel sin suponer visibilidad automática universal. Propón incorporación por fases o supervisión compensatoria con responsable y plazo. La aceptación exige eventos representativos utilizables y un recorrido de respuesta, no simplemente un conector habilitado o un panel poblado.

</details>

## 5. Una etiqueta de confidencialidad y discos cifrados se proponen como estrategia completa para datos estudiantiles. ¿Qué falta?

<details>
<summary>Respuesta</summary>

Aclara ubicaciones, clasificación, destinatarios y obligaciones de los datos. Comprueba qué configura realmente la etiqueta y qué clientes y repositorios respetan sus protecciones. El cifrado de disco protege un límite de almacenamiento, pero no impide que un servicio autorizado lea o exporte texto sin cifrar. Considera acceso acotado, restricciones de uso compartido, cobertura DLP, auditoría, retención, eliminación y administración de claves. Asigna evidencias y responsables a cada requisito, incluidas vías no compatibles. Privacidad y asesoría jurídica deben evaluar obligaciones; una etiqueta o puntuación no demuestra todos los requisitos legales.

</details>

## 6. Un documento subido por un profesor ordena al asistente enviar todos los archivos de la asignatura. ¿Qué límite importa?

<details>
<summary>Respuesta</summary>

El documento es contenido recuperado no confiable y no puede otorgar autoridad al modelo ni a sus herramientas. Restringe la recuperación al material permitido al usuario, limita la identidad del agente y aplica autorización de herramientas fuera de las instrucciones generadas por el modelo. Una herramienta de envío necesita una política deliberada de destinatarios y datos, más aprobación de divulgaciones relevantes cuando el diseño la exija. Evalúa detección de ataques como control adicional con supuestos de integración e idioma. Usa documentos sintéticos. Demuestra que sus instrucciones no amplían permisos de recuperación o herramientas.

</details>

## 7. Las copias nocturnas restauran archivos individuales, pero el servicio exige RPO de quince minutos. ¿Puede aprobarse el diseño?

<details>
<summary>Respuesta</summary>

Esa evidencia no basta. Los puntos nocturnos por sí solos no cumplen una pérdida máxima de quince minutos. Identifica cada origen y su mecanismo propuesto de recuperación, incluida coherencia entre documentos y metadatos. Evalúa también administración resistente al ransomware, retención y recuperación de claves. El RTO de dos horas necesita identidad, DNS, configuración y acceso al plano de control. El responsable debe financiar y validar un diseño que cumpla los objetivos o aprobar requisitos revisados con impacto explícito. Registra mediciones esperadas; este ejercicio sin conexión no demuestra rendimiento de restauración.

</details>

## 8. El equipo de plataforma aplica directivas a Azure. ¿Cómo se gestiona una excepción de SaaS departamental?

<details>
<summary>Respuesta</summary>

Primero establece si el ámbito de esa directiva puede gobernar el SaaS; no deduzcas cobertura de un resultado de cumplimiento de Azure. Relaciona el servicio departamental con los requisitos institucionales y evalúa controles propios, integración de identidad, tratamiento de datos, evidencias de auditoría y responsabilidades contractuales. Usa el modelo de responsabilidades de zonas de aterrizaje para aclarar plataforma y carga, sin suponer idéntica aplicación de controles. Si queda una carencia, registra controles compensatorios, responsable del riesgo, fecha de revisión y caducidad. La decisión debe explicar el efecto sobre todo el servicio.

</details>

## 9. Un artefacto firmado procede de un ejecutor con permisos amplios de producción. ¿Está protegida la cadena de suministro?

<details>
<summary>Respuesta</summary>

La firma apoya integridad y procedencia bajo supuestos de confianza definidos, pero no vuelve fiable una compilación autorizada comprometida. Revisa aprobación del código, dependencias, aislamiento del ejecutor, acceso a claves, promoción de artefactos y permisos de despliegue. Separa confianza de pruebas y producción; limita las declaraciones de federación y el ámbito cuando proceda. Define quién investiga una versión sospechosa y restaura una conocida como correcta. Las evidencias deben conectar revisión aprobada, artefacto promovido y despliegue autorizado, mostrando que una canalización no aprobada no modifica producción ni la política de firma.

</details>

## 10. La financiación cubre un semestre. ¿Cómo justifica el arquitecto un programa de seguridad por fases?

<details>
<summary>Respuesta</summary>

Ordena el trabajo según exposición crítica, dependencias, capacidad real de entrega y reducción prevista del riesgo. Proteger recuperación y administración privilegiada puede habilitar mejoras posteriores, pero justifica la secuencia frente a las amenazas universitarias. Compara opciones viables, licencias, carga operativa e interrupciones docentes. Asigna a cada fase responsable, criterios acotados de aceptación, evidencias, reversión y revisión fechada del riesgo residual. Documenta una alternativa y por qué se descartó en un ADR. Comprar es un hito; la eficacia validada de los controles y la aceptación autorizada del riesgo determinan la preparación.

</details>

[Guía oficial SC-100](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100)
