# AZ-140 · 10 casos con respuestas razonadas

[Guía](AZ-140.md) · [Cuaderno](AZ-140-workbook.md) · [Índice](README.md)

Escenarios originales de un aula universitaria, no preguntas oficiales. Explica el requisito y la evidencia antes de abrir cada respuesta. Las soluciones son razonamientos de diseño; no acreditan despliegues en Azure.

## 1. Cuarenta estudiantes necesitan escritorios intercambiables y un investigador su máquina dedicada. ¿Deben recibir todos un pool personal?

<details>
<summary>Respuesta</summary>

Evaluaría un pool compartido con sistema multisesión compatible para el alumnado y asignación personal para el investigador. Dedicar máquinas a todos puede consumir capacidad innecesaria; obligar al investigador a usar un puesto intercambiable podría incumplir su requisito. La asignación personal sigue necesitando el derecho sobre el recurso publicado. Registra medidas de carga, licencias, densidad prevista y la persistencia requerida por el investigador. La evidencia útil incluye modelo de asignación y cálculo de capacidad, no solamente número de VM.

</details>

## 2. Un estudiante tiene Contributor, ve las VM en Azure, pero su lista de recursos AVD está vacía. ¿Qué revisarías?

<details>
<summary>Respuesta</summary>

Revisa identidad y asignación al grupo de aplicaciones, asociación del grupo con el pool previsto y registro en el workspace. Administrar VM no publica automáticamente un escritorio al usuario. Comprueba también que el cliente se suscribe al workspace correcto con la cuenta esperada. Registra pertenencia a grupos, derecho efectivo y diagnósticos de la fuente de recursos con sus horas. Abrir un puerto de entrada de la VM o conceder Owner sobre la suscripción no explica ni corrige una relación de publicación ausente.

</details>

## 3. El proyecto quiere hosts unidos a Entra, pero una app antigua requiere servicios de dominio. ¿Entra ID sustituye automáticamente a AD DS?

<details>
<summary>Respuesta</summary>

No. Separa los requisitos concretos de autenticación y directorio de la app de la autenticación de la fuente AVD. Entra ID, AD DS y Entra Domain Services ofrecen capacidades distintas; elegir una unión del host no elimina dependencias de la aplicación. Comprueba combinaciones admitidas, autenticación del almacenamiento de perfiles, gestión de políticas y SSO antes de diseñar. Entrega un inventario de dependencias y un flujo de autenticación compatible. El acceso condicional no aporta un protocolo de dominio ausente ni acceso a sus controladores.

</details>

## 4. El equipo propone abrir TCP 3389 público para reparar cualquier conexión AVD. ¿Lo exige la conexión inversa?

<details>
<summary>Respuesta</summary>

No. La conexión inversa básica usa conectividad saliente HTTPS/TCP del cliente y del host hacia el servicio. Investiga destinos requeridos, DNS, TLS, proxy, salud del agente y etapa fallida. Shortpath es una opción separada de transporte UDP con requisitos propios; no justifica publicar RDP. Para un diseño de listener administrado, documenta alcance privado y puerto UDP elegido. La evidencia debe identificar la dependencia concreta bloqueada y proponer una corrección acotada, en lugar de una apertura amplia sin diagnóstico.

</details>

## 5. Los clientes del campus usan UDP y los domésticos recurren a TCP. ¿Demuestra un fallo del host?

<details>
<summary>Respuesta</summary>

No. Compara clientes, redes y opciones Shortpath. Una VPN del campus puede dar alcance privado directo, mientras un NAT o firewall doméstico impide una ruta UDP concreta. Revisa versiones, políticas UDP, acceso STUN/TURN, disponibilidad en la nube y transporte negociado. La alternativa de conexión inversa puede conservar la sesión con rendimiento distinto. Registra hora, latencia, pérdidas y observaciones de rutas correctas y fallidas. El listener administrado UDP 3390 no es requisito de todas las conexiones Shortpath por red pública.

</details>

## 6. Tras cambiar la identidad de SMB aparecen perfiles temporales aunque el inicio de sesión funciona. ¿Reconstruir todas las VM arreglaría la causa?

<details>
<summary>Respuesta</summary>

Primero revisa logs de montaje FSLogix y la ruta de autenticación del almacenamiento. Verifica ubicación del contenedor, DNS, permisos de recurso compartido y NTFS, Kerberos compatible y cifrado. Autenticarse en AVD y acceder al archivo de perfil son etapas separadas. Reconstruir hosts sin corregir una dependencia compartida reproduce el fallo. Conserva contenedores afectados e investiga sesiones o bloqueos antes de recuperar. La evidencia debe mostrar el error de montaje preciso y una operación de perfil permitida con la identidad prevista.

</details>

## 7. Un estudiante abre dos sesiones independientes y la segunda no puede montar el contenedor. ¿Debe borrarse el bloqueo inmediatamente?

<details>
<summary>Respuesta</summary>

No trates el bloqueo como algo desechable. La configuración estándar del perfil FSLogix admite una conexión al contenedor; los escenarios concurrentes tienen requisitos y límites de aplicaciones adicionales. Identifica sesiones activas y desconectadas, host propietario y estado real del bloqueo antes de declarar un recurso obsoleto. Coordina un cierre controlado y protege el trabajo sin guardar. Registra horas y logs. Si el diseño necesita concurrencia, requiere configuración compatible y validación, no escrituras simultáneas arbitrarias al mismo contenedor.

</details>

## 8. El editor se publica como RemoteApp pero falla en la mitad de los hosts. ¿Publicar el icono instala la aplicación?

<details>
<summary>Respuesta</summary>

Publicar una RemoteApp gobierna acceso y presentación; no demuestra que cada host elegible pueda ejecutarla. Compara versiones de imagen, dependencias instaladas y método de entrega. En App Attach, revisa compatibilidad del paquete, acceso al almacenamiento, asignaciones al pool y al usuario, y registro del paquete. Compara el mismo usuario en un host correcto y uno afectado sin modificar asignaciones de producción. La entrega debe explicar la diferencia y proponer una corrección gradual de paquete o imagen con una alternativa que funcione.

</details>

## 9. Llegan 48 estudiantes, caben doce sesiones por host y debe tolerarse un fallo. ¿Bastan cuatro hosts y Start VM on Connect?

<details>
<summary>Respuesta</summary>

Cuatro hosts sanos ofrecen exactamente 48 sesiones bajo la medida indicada: no dejan margen para perder uno. Cinco disponibles permiten mantener 48 sesiones después de un fallo. Start VM on Connect no garantiza que los hosts de reserva estén sanos y listos antes de la llegada simultánea. Modela arranque, sesiones máximas, balanceo, horario de escalado, exclusiones de drenaje y capacidad de perfiles. Entrega una tabla normal y degradada, con tiempos de arranque previstos. Valida la densidad con cargas representativas antes de usarla operativamente.

</details>

## 10. Otra región tiene VM, pero el alumnado no recupera su entorno. ¿Qué falta para afirmar que se ha recuperado el servicio?

<details>
<summary>Respuesta</summary>

Un inventario de VM no demuestra recuperación del escritorio. Traza identidad y DNS, publicación de recursos, aplicaciones, red, acceso y coherencia de perfiles, y API de apuntes. Define objetivos de recuperación de perfiles y datos por separado. Usa identificador de correlación, diagnósticos, eventos del host y logs FSLogix para localizar la primera etapa fallida. La simulación debe asignar operadores, supuestos de capacidad y retorno a la región principal, y exigir un flujo del estudiante funcional. Son comprobaciones previstas hasta obtener observaciones en un ejercicio autorizado.

</details>

Las referencias, fechas de objetivos y límites están en la [guía](AZ-140.md). Convierte el razonamiento en diagramas y evidencias con el [cuaderno](AZ-140-workbook.md).
