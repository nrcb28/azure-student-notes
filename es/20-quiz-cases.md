# 32 escenarios para practicar

[←](19-mini-quiz.md) · [CLI](../QUIZ.md)

Es una práctica breve: no es un examen oficial ni completo y el resultado no predice si aprobarás.

<a id="quiz-q01"></a>

## AZ-900 · Control del sistema operativo

Una aplicación de laboratorio necesita instalar su propio controlador del kernel de Linux. ¿Qué opción de alojamiento cumple mejor ese requisito?

- **A.** Ejecutar la aplicación en Microsoft 365.
- **B.** Usar una máquina virtual de Azure con una imagen de Linux compatible.
- **C.** Desplegarla en un entorno de ejecución administrado de App Service.
- **D.** Incluir el controlador en una Azure Function estándar.

<details>
<summary>Por qué:</summary>

**B. Usar una máquina virtual de Azure con una imagen de Linux compatible.**

La clave es poder administrar el sistema operativo invitado. Una VM de Azure compatible permite gestionar ese entorno y sus controladores, pero también deja su mantenimiento en manos del equipo. Una plataforma administrada de aplicaciones no sirve para este caso si no ofrece el control del kernel que se necesita.

- **A.** Microsoft 365 ofrece software listo para usar; no aloja controladores de kernel arbitrarios.
- **C.** El entorno administrado de App Service no permite la administración necesaria del kernel invitado.
- **D.** Una Function estándar no concede el control necesario para instalar ese controlador.

[Fuente:](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) · [Para repasar:](03-compute.md)

</details>

<a id="quiz-q02"></a>

## AZ-900 · Escalado horizontal y sesiones

Una API de apuntes añade instancias detrás de un balanceador. Cualquier instancia puede sustituirse, pero los usuarios deben conservar sus sesiones. Ahora las sesiones solo están en la memoria de cada instancia. ¿Qué habría que cambiar?

- **A.** Aumentar la CPU de todas las instancias.
- **B.** Mantener las sesiones en memoria y activar únicamente afinidad de sesión.
- **C.** Mover el estado de las sesiones a un almacén externo compartido adecuado.
- **D.** Asignar una IP pública a cada instancia.

<details>
<summary>Por qué:</summary>

**C. Mover el estado de las sesiones a un almacén externo compartido adecuado.**

Al escalar horizontalmente, las peticiones se reparten entre instancias. El estado importante de una sesión no puede depender solo de la memoria de una de ellas. Un almacén externo adecuado permite recuperarlo desde una instancia de reemplazo. La afinidad por sí sola no conserva la memoria de una instancia que desaparece. La aplicación también debe gestionar el acceso al almacén y sus posibles fallos.

- **A.** Más CPU no conserva la memoria cuando se sustituye la instancia.
- **B.** La afinidad también pierde la sesión si desaparece la instancia elegida.
- **D.** Una IP pública no aporta un estado de sesión compartido o duradero.

[Fuente:](https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/scale-out) · [Para repasar:](01-fundamentals.md)

</details>

<a id="quiz-q03"></a>

## AZ-104 · Acceso a los datos de almacenamiento

Un usuario tiene Contributor en una cuenta de almacenamiento. Una petición Blob con su identidad de Entra llega al servicio, pero se rechaza por falta de permisos sobre los datos. Solo necesita leer blobs de un contenedor. ¿Qué solución sigue el principio de mínimo privilegio?

- **A.** Asignar Storage Blob Data Reader con el ámbito de ese contenedor.
- **B.** Asignar Owner en toda la suscripción.
- **C.** Abrir todos los puertos de entrada.
- **D.** Entregar al usuario la clave de la cuenta de almacenamiento.

<details>
<summary>Por qué:</summary>

**A. Asignar Storage Blob Data Reader con el ámbito de ese contenedor.**

Los permisos de administración y los permisos sobre los datos Blob son distintos. Storage Blob Data Reader permite la lectura solicitada, y el ámbito del contenedor limita la concesión a lo necesario. El caso ya identifica una falta de autorización sobre los datos: conceder administración general o cambiar la red no es una respuesta proporcionada.

- **B.** Owner en la suscripción supera la necesidad de leer un solo contenedor.
- **C.** Abrir puertos no concede la autorización que falta sobre los datos.
- **D.** Una clave de cuenta da un acceso mucho más amplio del necesario.

[Fuente:](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access) · [Para repasar:](06-identity.md)

</details>

<a id="quiz-q04"></a>

## AZ-104 · Herencia de permisos RBAC

Un usuario tiene Reader asignado directamente en una VM y también pertenece a un grupo con Reader en la suscripción. Eliminas solo la asignación directa de la VM. El usuario sigue pudiendo leerla. ¿Por qué?

- **A.** Azure da Reader en todas las VM a todos los usuarios automáticamente.
- **B.** Una etiqueta del grupo de recursos restaura la asignación eliminada.
- **C.** Para quitar un rol siempre hay que eliminar la VM.
- **D.** La asignación del grupo sigue concediendo acceso heredado.

<details>
<summary>Por qué:</summary>

**D. La asignación del grupo sigue concediendo acceso heredado.**

Eliminar una asignación no elimina los permisos obtenidos mediante otra. Como el grupo tiene Reader en la suscripción, sus miembros pueden heredar ese acceso a la VM. Conviene revisar asignaciones directas, pertenencia a grupos y ámbitos superiores antes de interpretar el acceso restante como un fallo del servicio o conceder más permisos.

- **A.** No existe una concesión universal de Reader a todos los usuarios.
- **B.** Las etiquetas clasifican recursos; no recrean asignaciones de roles.
- **C.** Quitar un rol no exige eliminar el recurso protegido.

[Fuente:](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview) · [Para repasar:](06-identity.md)

</details>

<a id="quiz-q05"></a>

## AZ-305 · Objetivos de recuperación

Un diseño solo conserva puntos válidos de recuperación de la base de datos una vez cada 24 horas. El negocio ahora exige perder como máximo una hora de datos recientes tras un desastre. ¿Qué cambio resuelve directamente esa diferencia?

- **A.** Aumentar la CPU del servidor de la API.
- **B.** Diseñar puntos de protección de datos recuperables separados por una hora como máximo y validar la recuperación.
- **C.** Añadir un presupuesto con alertas de costes.
- **D.** Cambiar el nombre del grupo de recursos a production.

<details>
<summary>Por qué:</summary>

**B. Diseñar puntos de protección de datos recuperables separados por una hora como máximo y validar la recuperación.**

El RPO expresa en tiempo cuántos datos recientes se pueden perder. Tener únicamente puntos diarios no permite cumplir un objetivo de una hora. El diseño debe generar estados recuperables con la frecuencia necesaria y comprobar que se pueden restaurar. Más CPU o una etiqueta de costes no cambian la antigüedad de los datos disponibles para recuperar.

- **A.** La CPU de la API no aumenta la frecuencia de protección de los datos.
- **C.** Un presupuesto avisa del gasto, no de la pérdida de datos.
- **D.** El nombre del grupo de recursos no cambia la frecuencia de los puntos de recuperación.

[Fuente:](https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery) · [Para repasar:](10-architecture.md)

</details>

<a id="quiz-q06"></a>

## AZ-305 · DNS para conexiones privadas

Se ha desactivado el acceso público a un servicio de almacenamiento y existe un punto de conexión privado. El cliente sigue resolviendo el nombre del servicio a su IP pública. La ruta de red privada está disponible. ¿Qué revisarías primero?

- **A.** Dar al cliente Owner en la suscripción.
- **B.** Fijar permanentemente la IP pública en la configuración.
- **C.** Las zonas DNS privadas, sus vínculos y el reenvío que usa ese cliente.
- **D.** Aumentar indefinidamente los reintentos de la aplicación.

<details>
<summary>Por qué:</summary>

**C. Las zonas DNS privadas, sus vínculos y el reenvío que usa ese cliente.**

El cliente resuelve un destino distinto del que necesita la conexión privada. Revisa la configuración DNS privada recomendada para el servicio y cómo accede a ella este cliente, incluidos vínculos y reenvío. Sigue usando el nombre del servicio. Corregir DNS no concede por sí mismo permisos sobre los datos, pero más privilegios o reintentos sin límite tampoco arreglan esta discrepancia.

- **A.** Owner no cambia cómo resuelve nombres el cliente.
- **B.** La dirección pública es el destino equivocado cuando el acceso público está desactivado.
- **D.** Repetir peticiones no corrige una configuración DNS errónea.

[Fuente:](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) · [Para repasar:](05-networking.md)

</details>

<a id="quiz-q07"></a>

## AZ-400 · Promoción del artefacto probado

Un pipeline prueba una imagen de contenedor y después vuelve a compilar desde el código para producción con dependencias que pueden cambiar. ¿Cómo asegurar que producción recibe la imagen que superó las pruebas?

- **A.** Volver a probar únicamente los comentarios del código.
- **B.** Usar la etiqueta latest sin registrar a qué imagen apunta.
- **C.** Omitir las pruebas porque el commit del código no ha cambiado.
- **D.** Promover la misma imagen probada, identificada por un digest inmutable.

<details>
<summary>Por qué:</summary>

**D. Promover la misma imagen probada, identificada por un digest inmutable.**

El mismo commit puede producir resultados distintos si cambian las herramientas, las dependencias o las imágenes base. Promover la imagen ya probada evita esa diferencia de recompilación. Un digest inmutable identifica el artefacto concreto, mientras que una etiqueta puede cambiar de destino. La configuración de cada entorno sigue necesitando validación y gestión controlada.

- **A.** Los comentarios del código no identifican el artefacto compilado.
- **B.** Una etiqueta mutable puede apuntar después a otra imagen.
- **C.** Que el commit sea el mismo no demuestra que la recompilación produzca una imagen idéntica.

[Fuente:](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-concepts) · [Para repasar:](12-devops.md)

</details>

<a id="quiz-q08"></a>

## AZ-400 · Señales de un despliegue canario

Un despliegue canario muestra CPU y memoria normales, pero las descargas de documentos devuelven archivos incorrectos. ¿En qué debería basarse la decisión de continuar el despliegue?

- **A.** En señales de funcionamiento correcto y un criterio definido para detener o revertir el despliegue.
- **B.** Solo en la CPU, porque una infraestructura sana demuestra que los resultados son correctos.
- **C.** En usar una VM mayor antes de revisar los archivos devueltos.
- **D.** En borrar registros antiguos para que el panel se vea más limpio.

<details>
<summary>Por qué:</summary>

**A. En señales de funcionamiento correcto y un criterio definido para detener o revertir el despliegue.**

Una versión puede consumir pocos recursos y aun así dar resultados incorrectos. Para promoverla hacen falta señales de la operación que realiza el usuario, además de métricas de infraestructura. Un criterio definido de parada o reversión permite actuar sobre esas señales. También hay que revisar la compatibilidad de los datos: revertir el código no deshace automáticamente los cambios de datos perjudiciales de esa versión.

- **B.** CPU y memoria no demuestran que los usuarios reciban los documentos correctos.
- **C.** Más capacidad de cómputo no corrige por sí sola una salida errónea de la aplicación.
- **D.** Borrar evidencias dificulta investigar y no corrige los resultados.

[Fuente:](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments) · [Para repasar:](12-devops.md)

</details>

<a id="quiz-q09"></a>

## DP-900 · Cargas transaccionales

El servicio de matrícula de una universidad debe reservar la última plaza de un laboratorio y crear la matrícula del estudiante como una sola operación coherente. ¿Qué descripción de carga se ajusta mejor a este requisito?

- **A.** Una carga analítica que agrupa las matrículas por semestre.
- **B.** Una carga por lotes que concilia cada noche las actualizaciones independientes de plazas.
- **C.** Una carga transaccional que confirma conjuntamente los cambios relacionados.
- **D.** Una carga de streaming que publica eventos separados de plaza y matrícula sin coordinar sus confirmaciones.

<details>
<summary>Por qué:</summary>

**C. Una carga transaccional que confirma conjuntamente los cambios relacionados.**

El requisito describe una operación concreta cuyos cambios relacionados deben completarse o fallar juntos. Ese comportamiento es transaccional: otra solicitud no debe reservar la misma última plaza mientras discrepan los registros de matrícula y capacidad. Los informes históricos constituyen trabajo analítico con otros patrones de acceso. Los eventos y la conciliación posterior pueden apoyar una arquitectura más amplia, pero las actualizaciones independientes no garantizan la coherencia exigida.

- **A.** La agrupación por semestre responde a preguntas históricas; no coordina los cambios de reserva y matrícula necesarios para esta solicitud en curso.
- **B.** La conciliación nocturna deja un intervalo durante el que pueden discrepar las plazas y matrículas, incumpliendo el requisito de coherencia inmediata.
- **D.** Publicar eventos puede informar a otros sistemas, pero confirmarlos por separado no convierte por sí solo los dos cambios de origen en atómicos.

[Fuente:](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing) · [Para repasar:](../certifications/es/DP-900.md)

</details>

<a id="quiz-q10"></a>

## DP-900 · Orden de ETL y ELT

Un equipo de investigación extrae los registros de descargas de ayer, elimina identificadores no válidos mediante un servicio de procesamiento y después carga los registros depurados en su almacén de informes. ¿Qué descripción corresponde a ese orden?

- **A.** ETL, porque la transformación ocurre antes de cargar el destino de informes.
- **B.** ELT, porque cualquier flujo que termina en un almacén transforma dentro de ese almacén.
- **C.** Streaming, porque los registros de descargas procedían originalmente de eventos de la aplicación.
- **D.** Solo orquestación, porque coordinar los pasos elimina la necesidad de transformar.

<details>
<summary>Por qué:</summary>

**A. ETL, porque la transformación ocurre antes de cargar el destino de informes.**

ETL significa extraer, transformar y después cargar el destino previsto. Aquí se tratan los identificadores no válidos antes de que el almacén de informes reciba los registros depurados. En ELT, primero se cargan los datos y después se transforman con el procesamiento del destino. La colección delimitada de ayer es una entrada por lotes. Un orquestador puede coordinar estas actividades, pero orquestación y transformación describen responsabilidades distintas.

- **B.** ELT requiere cargar antes de transformar en el destino; elegir un almacén como destino no determina por sí solo ese orden.
- **C.** El origen en eventos no convierte el procesamiento posterior en streaming; este trabajo procesa una colección diaria delimitada, no registros que llegan continuamente.
- **D.** La orquestación coordina dependencias y recuperación; eliminar identificadores no válidos modifica los datos y sigue siendo una responsabilidad de transformación independiente.

[Fuente:](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl) · [Para repasar:](../certifications/es/DP-900.md)

</details>

<a id="quiz-q11"></a>

## SC-900 · Categorías de factores de MFA

Un estudiante compara diseños de inicio de sesión. ¿Qué ejemplo combina un factor de conocimiento con uno de posesión, suponiendo que el dispositivo autenticador está registrado y su aprobación es obligatoria?

- **A.** Una contraseña seguida de una respuesta memorizada a una pregunta de seguridad.
- **B.** Una contraseña universitaria seguida de otra contraseña memorizada para el servicio.
- **C.** Una contraseña seguida de un PIN memorizado introducido en la misma web, sin un autenticador vinculado a un dispositivo.
- **D.** Una contraseña seguida de una aprobación mediante el dispositivo autenticador registrado del estudiante.

<details>
<summary>Por qué:</summary>

**D. Una contraseña seguida de una aprobación mediante el dispositivo autenticador registrado del estudiante.**

Una contraseña representa algo que el estudiante sabe; controlar un dispositivo autenticador registrado aporta un factor de posesión. Exigir ambos combina categorías diferentes. Dos secretos memorizados siguen siendo factores de conocimiento aunque sus valores sean distintos. Esta clasificación no hace que todos los métodos de MFA resistan igual el phishing: la selección del método, el registro, la recuperación y la aplicación efectiva también importan para la política universitaria.

- **A.** Tanto la contraseña como la respuesta memorizada son factores de conocimiento; añadir otra comprobación de conocimiento no aporta el factor de posesión requerido.
- **B.** Usar contraseñas distintas puede separar credenciales, pero ambas siguen siendo secretos memorizados y, por tanto, pertenecen a la misma categoría de factor.
- **C.** La pregunta excluye un autenticador vinculado al dispositivo: introducir el PIN como otro secreto web aporta conocimiento, no prueba de posesión del dispositivo.

[Fuente:](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks) · [Para repasar:](../certifications/es/SC-900.md)

</details>

<a id="quiz-q12"></a>

## SC-900 · Tratamiento de datos con Purview

Una universidad debe detectar identificadores de estudiantes en actividades compatibles de uso compartido de documentos y advertir o restringir el uso compartido externo cuando coincida una regla configurada. ¿Qué capacidad de Purview responde más directamente al requisito?

- **A.** Auditoría, utilizada únicamente para registrar que se produjo la actividad de uso compartido.
- **B.** Prevención de pérdida de datos con una directiva cuyo ámbito esté definido y probado adecuadamente.
- **C.** Retención, configurada para conservar los documentos durante siete años.
- **D.** Una etiqueta de confidencialidad llamada Confidencial, sin configurar protección ni DLP.

<details>
<summary>Por qué:</summary>

**B. Prevención de pérdida de datos con una directiva cuyo ámbito esté definido y probado adecuadamente.**

DLP evalúa información confidencial y actividades coincidentes frente a directivas configuradas, y puede advertir o restringir acciones compatibles. El diseño debe definir ubicaciones, condiciones de detección, destinatarios, excepciones y respuesta prevista. Auditoría aporta evidencias de actividad; retención gestiona el ciclo de vida del contenido; una etiqueta comunica clasificación o aplica protección configurada. El nombre de una etiqueta no establece por sí solo la restricción de uso compartido externo descrita.

- **A.** Auditoría facilita la investigación al registrar actividades; registrar un uso compartido no proporciona por sí solo la advertencia o restricción de directiva solicitada.
- **C.** Conservar un documento durante un periodo definido regula su ciclo de vida, pero no determina si debe permitirse esta actividad de uso compartido externo.
- **D.** El nombre de una etiqueta no configura una restricción; la protección o una directiva DLP adecuada debe implementar el comportamiento previsto de uso compartido.

[Fuente:](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) · [Para repasar:](../certifications/es/SC-900.md)

</details>

<a id="quiz-q13"></a>

## AZ-700 · Enrutamiento por prefijo más largo

Una VM de laboratorio tiene dos rutas efectivas activas: una ruta definida por el usuario 0.0.0.0/0 hacia un dispositivo de red y una ruta del sistema 10.20.0.0/16 por emparejamiento de redes virtuales. No hay otra más específica. ¿Qué próximo salto se selecciona para 10.20.7.5?

- **A.** El emparejamiento de redes virtuales, porque el prefijo /16 coincidente es más específico.
- **B.** El dispositivo de red, porque las rutas definidas por el usuario siempre superan a cualquier ruta del sistema.
- **C.** Ambos próximos saltos, porque Azure duplica los paquetes por todas las rutas coincidentes.
- **D.** Ningún próximo salto, porque los prefijos coincidentes superpuestos invalidan la tabla de rutas.

<details>
<summary>Por qué:</summary>

**A. El emparejamiento de redes virtuales, porque el prefijo /16 coincidente es más específico.**

Azure selecciona primero la ruta coincidente con el prefijo más largo. El destino pertenece a 10.20.0.0/16, más específico que 0.0.0.0/0, por lo que el paquete utiliza la ruta activa de emparejamiento. La preferencia según el origen de ruta importa cuando los prefijos aplicables tienen igual longitud; no convierte una ruta predeterminada del usuario en dominante universal. Seleccionar un próximo salto tampoco establece permisos de firewall ni acceso a la aplicación.

- **B.** La preferencia por origen no anula aquí la selección del prefijo más largo; la ruta predeterminada del usuario es menos específica que la de emparejamiento.
- **C.** El enrutamiento normal por destino selecciona la ruta coincidente preferida; no copia un paquete a todos los próximos saltos cuyos prefijos coinciden.
- **D.** Los prefijos superpuestos son normales en las tablas de rutas; una ruta predeterminada puede coexistir con rutas más específicas sin invalidar la tabla.

[Fuente:](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview) · [Para repasar:](../certifications/es/AZ-700.md)

</details>

<a id="quiz-q14"></a>

## AZ-700 · Cifrado de ExpressRoute

Una universidad utiliza ExpressRoute y exige cifrado desde su dispositivo VPN del campus hasta una puerta de enlace VPN de Azure. ExpressRoute debe seguir siendo la red subyacente. ¿Qué diseño satisface más directamente ese límite de protección?

- **A.** Activar MACsec en enlaces compatibles de ExpressRoute Direct y considerar que esa protección física cubre todo el trayecto del campus a la puerta de enlace.
- **B.** Usar emparejamiento privado de ExpressRoute sin otro mecanismo de cifrado, porque el enrutamiento privado cifra todas las cargas útiles.
- **C.** Usar un túnel IPsec compatible sobre ExpressRoute y validar el enrutamiento, la compatibilidad de las puertas de enlace y el rendimiento requerido.
- **D.** Activar TLS solo entre la aplicación de Azure y su base de datos, dejando sin cifrar el trayecto del campus a la puerta de enlace.

<details>
<summary>Por qué:</summary>

**C. Usar un túnel IPsec compatible sobre ExpressRoute y validar el enrutamiento, la compatibilidad de las puertas de enlace y el rendimiento requerido.**

ExpressRoute proporciona conectividad privada, pero no cifra automáticamente las cargas útiles. Una superposición IPsec compatible puede proteger la conexión indicada entre el dispositivo VPN del campus y la puerta de enlace VPN de Azure usando ExpressRoute como red subyacente. MACsec protege enlaces físicos compatibles de ExpressRoute Direct, un límite distinto. La propuesta también debe validar enrutamiento, puertas de enlace compatibles, capacidad y comportamiento ante fallos.

- **A.** MACsec protege enlaces físicos compatibles de Direct; ese segmento no cubre por sí solo todo el límite solicitado entre dispositivo del campus y puerta de enlace.
- **B.** El emparejamiento privado modifica la conectividad y el enrutamiento, pero no cifra automáticamente la carga útil de la conexión requerida del campus a la puerta de enlace.
- **D.** TLS entre aplicación y base de datos protege otro segmento; deja sin atender el límite exigido entre dispositivo VPN del campus y puerta de enlace de Azure.

[Fuente:](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-about-encryption) · [Para repasar:](../certifications/es/AZ-700.md)

</details>

<a id="quiz-q15"></a>

## DP-300 · Restauración de SQL a un momento dado

A las 14:20, una universidad descubre una actualización destructiva confirmada a las 13:00 en Azure SQL Database. El cambio llegó a la réplica. La retención automática incluye las 12:59 y se busca ese estado previo con la menor pérdida evitable. ¿Qué plan encaja mejor?

- **A.** Promover la réplica sincronizada actual y suponer que desaparece la actualización confirmada.
- **B.** Restaurar las 12:59 en una base de datos nueva, validarla y planificar la reconexión controlada de la aplicación y la conciliación de datos posteriores.
- **C.** Restaurar una copia retenida de hace dos días aunque esté disponible el punto de recuperación requerido de las 12:59.
- **D.** Realizar una restauración a un momento dado y suponer que Azure sobrescribe producción y redirige automáticamente todos los clientes.

<details>
<summary>Por qué:</summary>

**B. Restaurar las 12:59 en una base de datos nueva, validarla y planificar la reconexión controlada de la aplicación y la conciliación de datos posteriores.**

La restauración a un momento dado recupera un estado retenido anterior a la transacción destructiva. En Azure SQL Database crea una base de datos, por lo que la validación y la reconexión controlada forman parte del plan. También debe decidirse explícitamente cómo tratar la actividad legítima posterior. La réplica sincronizada ya contiene la actualización incorrecta; promoverla no recupera la corrección histórica ni el estado del momento solicitado.

- **A.** La réplica ya recibió el cambio destructivo confirmado; promover esa copia actual no recupera el estado correcto anterior de la base de datos.
- **C.** La copia más antigua descarta historia innecesariamente cuando la retención indicada permite el punto previo requerido y se busca minimizar la pérdida evitable.
- **D.** La restauración a un momento dado crea una base de datos; el equipo debe validarla y gestionar conexiones, sin suponer una sustitución automática.

[Fuente:](https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups) · [Para repasar:](../certifications/es/DP-300.md)

</details>

<a id="quiz-q16"></a>

## DP-300 · Límites de cifrado de SQL

Una aplicación de investigación debe impedir que los administradores de bases de datos lean determinados valores de participantes al consultar tablas. Solo el cliente de confianza puede descifrarlos, y los administradores no deben tener sus claves. ¿Qué enfoque encaja mejor?

- **A.** Activar TDE y mantener el acceso habitual de consulta de los administradores.
- **B.** Exigir TLS entre cliente y base de datos sin cifrar los valores seleccionados en el límite del cliente.
- **C.** Aplicar enmascaramiento dinámico de datos manteniendo amplios privilegios de consulta para los administradores.
- **D.** Usar Always Encrypted configurado adecuadamente, con un cliente compatible y claves controladas por separado.

<details>
<summary>Por qué:</summary>

**D. Usar Always Encrypted configurado adecuadamente, con un cliente compatible y claves controladas por separado.**

Always Encrypted permite que clientes compatibles cifren y descifren valores confidenciales mientras las claves permanecen fuera del acceso del motor de base de datos. La universidad debe validar el controlador, las operaciones permitidas y la administración separada de claves. TDE protege archivos en reposo; TLS protege la conexión; el enmascaramiento cambia la presentación de consultas. Por sí solos, esos controles no cumplen la exclusión de administradores especificada.

- **A.** TDE protege los archivos de base de datos en reposo; los administradores con derechos normales de consulta aún pueden obtener valores legibles mediante el motor.
- **B.** TLS protege los datos mientras viajan por la conexión, pero no impide por sí solo que un administrador autorizado consulte los valores almacenados.
- **C.** El enmascaramiento modifica la presentación de resultados para ciertos usuarios; no establece un límite criptográfico frente a administradores con amplios privilegios de base de datos.

[Fuente:](https://learn.microsoft.com/en-us/azure/azure-sql/database/security-overview) · [Para repasar:](../certifications/es/DP-300.md)

</details>

<a id="quiz-q17"></a>

## AI-901 · Identidad del cliente de Foundry

El cliente de Foundry de un estudiante usa el punto de conexión y el nombre de implementación documentados, pero no tiene credenciales configuradas para la carga que llama. ¿Qué debe añadir el diseño para establecer un llamador autorizado?

- **A.** Sustituir el nombre de implementación por el del modelo del catálogo y seguir sin credenciales.
- **B.** Configurar una credencial compatible para la carga y conceder a esa identidad el acceso mínimo requerido.
- **C.** Cambiar de REST a un SDK y mantener al llamador sin autenticar.
- **D.** Copiar en el cliente la URL del portal de un administrador que accedió correctamente como prueba de permisos de la carga.

<details>
<summary>Por qué:</summary>

**B. Configurar una credencial compatible para la carga y conceder a esa identidad el acceso mínimo requerido.**

Un punto de conexión indica adónde va la solicitud y una implementación identifica el modelo configurado; ninguno establece quién llama. El cliente necesita autenticación compatible y la identidad resultante necesita permisos mínimos adecuados. El SDK y la generación de API también deben coincidir. Los secretos deben quedar fuera de cuadernos y código fuente; el acceso de un administrador humano al portal no se transfiere automáticamente a la aplicación.

- **A.** El nombre de un modelo del catálogo y el de una implementación tienen funciones distintas; cambiar el texto no autentica la carga ni concede acceso.
- **C.** Un SDK encapsula contratos de solicitud compatibles, pero cambiar bibliotecas cliente no elimina los requisitos de autenticación y autorización del servicio.
- **D.** Una URL del portal identifica una ubicación; la sesión autenticada del administrador en el navegador no establece la identidad ni los permisos de la carga independiente.

[Fuente:](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) · [Para repasar:](../certifications/es/AI-901.md)

</details>

<a id="quiz-q18"></a>

## AI-901 · Fundamentación y respaldo de afirmaciones

Un asistente de apuntes indica una fecha de entrega y cita el PDF correcto, pero el pasaje recuperado solo define un algoritmo. La aplicación debe responder fechas únicamente desde pasajes permitidos que las respalden. ¿Cuál es la mejor respuesta?

- **A.** Recuperar un pasaje que respalde la fecha o indicar que las evidencias disponibles son insuficientes.
- **B.** Aceptar la fecha porque citar el documento correcto demuestra todas las afirmaciones de la respuesta.
- **C.** Fijar la temperatura de generación en cero y aceptar la misma fecha sin comprobar otro pasaje.
- **D.** Aceptar la fecha si el modelo declara una confianza alta, aunque el pasaje no la respalde.

<details>
<summary>Por qué:</summary>

**A. Recuperar un pasaje que respalde la fecha o indicar que las evidencias disponibles son insuficientes.**

La fundamentación exige evidencias que respalden la afirmación concreta, no solo una cita a un documento relacionado. La definición del algoritmo no establece una fecha de entrega. La recuperación debe buscar un pasaje autorizado con la fecha y sus condiciones; de lo contrario, el asistente debe abstenerse. La generación determinista y la confianza declarada no crean evidencias ausentes. La evaluación debe comparar cada afirmación relevante con el texto citado.

- **B.** Una cita al documento correcto puede señalar un pasaje irrelevante; identificar el documento no basta para respaldar la fecha indicada en la respuesta.
- **C.** Reducir la temperatura cambia la variabilidad de generación, pero no convierte la definición de un algoritmo en evidencia que respalde una fecha ausente.
- **D.** La confianza del modelo puede ser incorrecta; la regla explícita de la aplicación sigue exigiendo un pasaje permitido que respalde la fecha concreta.

[Fuente:](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators) · [Para repasar:](../certifications/es/AI-901.md)

</details>

<a id="quiz-q19"></a>

## SC-200 · Evidencias temporales del SOC

Registros sintéticos de una misma cuenta verificada muestran actividad de correo a las 10:02 UTC, ingerida a las 10:20, y un inicio de sesión a las 10:08, ingerido a las 10:09. Ambos relojes de evento son fiables. ¿Qué conclusión permiten por sí solos?

- **A.** El inicio de sesión ocurrió primero porque su registro llegó antes al área de trabajo.
- **B.** El correo causó el inicio de sesión y demuestra que la cuenta está comprometida.
- **C.** Debe descartarse la hora del evento de correo porque su ingesta se retrasó.
- **D.** La actividad de correo precedió al inicio de sesión, pero la causalidad y el compromiso requieren más evidencias.

<details>
<summary>Por qué:</summary>

**D. La actividad de correo precedió al inicio de sesión, pero la causalidad y el compromiso requieren más evidencias.**

Las marcas de tiempo fiables sitúan el correo antes del inicio de sesión. Las horas de ingesta describen cuándo llegaron los registros; distintos retrasos pueden invertir su orden de llegada. Verificar una cuenta común ayuda a correlacionarlos, pero no demuestra que el correo causara el inicio ni que alguno fuera malicioso. El analista debe conservar ambos campos temporales, investigar la actividad circundante y expresar los límites de las evidencias.

- **A.** El orden de ingesta describe la llegada de la recopilación, no el orden de actividad; los tiempos fiables sitúan el correo antes del inicio.
- **B.** Una cuenta común y una secuencia temporal justifican investigar, pero no establecen por sí solas un vínculo causal, actividad maliciosa ni compromiso confirmado.
- **C.** Una ingesta retrasada no invalida necesariamente una hora de evento fiable; conserve ambos campos e investigue el retraso en vez de descartar evidencias.

[Fuente:](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender) · [Para repasar:](../certifications/es/SC-200.md)

</details>

<a id="quiz-q20"></a>

## SC-200 · Idempotencia de acciones de respuesta

Un playbook de Sentinel crea un ticket universitario de incidente, pero se pierde la respuesta de éxito. Un reintento podría crear otro ticket para la misma acción aprobada. ¿Qué control del flujo aborda mejor este fallo?

- **A.** Aumentar el tiempo de espera y suponer que una respuesta ausente siempre significa que no existe ningún ticket.
- **B.** Generar un identificador de acción nuevo en cada reintento para que todas las solicitudes parezcan independientes.
- **C.** Persistir una clave de incidente y acción junto con el estado del ticket, y conciliar o reutilizar el resultado existente al reintentar.
- **D.** Eliminar duplicados solo de los registros de alerta entrantes, permitiendo repetir la creación de tickets sin comprobar estados.

<details>
<summary>Por qué:</summary>

**C. Persistir una clave de incidente y acción junto con el estado del ticket, y conciliar o reutilizar el resultado existente al reintentar.**

La idempotencia hace que repetir la misma acción lógica conserve su resultado previsto en vez de producir otro efecto. Una clave duradera de incidente y acción, el estado registrado y la referencia externa permiten encontrar o conciliar trabajo existente. Una respuesta perdida deja un resultado desconocido hasta comprobarlo. El flujo también necesita reintentos limitados, responsable y permisos adecuados; deduplicar alertas no controla por sí solo la ejecución de acciones.

- **A.** Un plazo mayor puede reducir algunos fallos, pero perder la respuesta sigue dejando incertidumbre sobre si el ticket externo ya se creó.
- **B.** Un identificador nuevo presenta el reintento como trabajo diferente e impide que el flujo reconozca la misma acción lógica ya intentada anteriormente.
- **D.** Deduplicar alertas controla los registros de entrada; un paso posterior reintentado aún puede duplicar tickets si la ejecución no comprueba su propio estado.

[Fuente:](https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer) · [Para repasar:](../certifications/es/SC-200.md)

</details>

<a id="quiz-q21"></a>

## SC-300 · Acceso condicional en modo de solo informe

Una universidad prueba una directiva de acceso condicional en modo de solo informe. La evaluación indica que un inicio de sesión no cumpliría el requisito de concesión propuesto, pero el inicio tiene éxito. Ninguna otra directiva exige ese control. ¿Cuál es la mejor explicación?

- **A.** Los permisos de la aplicación siempre anulan una denegación de acceso condicional aplicada.
- **B.** El control propuesto ya se ha aplicado porque el modo de solo informe lo evalúa.
- **C.** El modo de solo informe registra la evaluación de la directiva sin aplicar su requisito de concesión.
- **D.** El modo de solo informe permite el primer inicio que incumple y bloquea automáticamente el siguiente.

<details>
<summary>Por qué:</summary>

**C. El modo de solo informe registra la evaluación de la directiva sin aplicar su requisito de concesión.**

El modo de solo informe evalúa la directiva y registra el resultado previsto sin aplicar sus controles. Un inicio correcto puede coexistir con evidencias de que el requisito propuesto fallaría al aplicarse. El equipo debe revisar casos permitidos y denegados previstos, identidades afectadas, exclusiones y recuperación administrativa antes del despliegue aprobado. Los permisos de aplicación son un límite de autorización separado y no anulan un fallo de acceso condicional aplicado.

- **A.** Tener acceso a la aplicación no anula automáticamente una denegación de acceso condicional aplicada; el modo indicado explica este inicio de sesión correcto.
- **B.** Evaluar y aplicar son distintos: el modo de solo informe registra lo que ocurriría, sin demostrar que se haya aplicado el requisito de concesión.
- **D.** El modo de solo informe no permite un primer intento para después aplicar controles automáticamente; la aplicación exige cambiar la configuración correspondiente de la directiva.

[Fuente:](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only) · [Para repasar:](../certifications/es/SC-300.md)

</details>

<a id="quiz-q22"></a>

## SC-300 · Notificaciones de federación de cargas

Un trabajo de compilación universitario usa federación de identidades de carga. Falla el intercambio de tokens: el sujeto del token externo difiere en mayúsculas del sujeto federado configurado. El emisor y la audiencia coinciden. ¿Qué cambio corrige esa discrepancia identificada?

- **A.** Conceder Propietario de la suscripción a la carga sin cambiar el sujeto federado.
- **B.** Alinear exactamente el sujeto configurado con la notificación entrante prevista y verificar por separado los permisos mínimos de la identidad sobre los recursos.
- **C.** Añadir asignaciones SCIM de aprovisionamiento de usuarios para el nombre del repositorio en vez de corregir la credencial federada.
- **D.** Aumentar la duración del token externo sin cambiar el sujeto que no coincide.

<details>
<summary>Por qué:</summary>

**B. Alinear exactamente el sujeto configurado con la notificación entrante prevista y verificar por separado los permisos mínimos de la identidad sobre los recursos.**

Las credenciales federadas comparan emisor, sujeto y audiencia de confianza con la aserción entrante; deben coincidir, incluidas las mayúsculas. Corregir la relación del sujeto prevista aborda la discrepancia descrita sin introducir un secreto de cliente almacenado. Un intercambio correcto autentica la carga, pero no concede acceso arbitrario a recursos. La identidad resultante sigue necesitando permisos asignados por separado y con el ámbito adecuado para las operaciones reales de compilación.

- **A.** Los permisos de recursos regulan qué puede hacer una identidad autenticada; un rol amplio no corrige una notificación discrepante que impide intercambiar tokens.
- **C.** SCIM gestiona aprovisionamiento y atributos de cuentas; no sustituye las comprobaciones de emisor, sujeto y audiencia federados del intercambio de tokens de esta carga.
- **D.** Cambiar la duración modifica la vigencia del token, pero no hace coincidir su sujeto sensible a mayúsculas con la credencial federada configurada.

[Fuente:](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) · [Para repasar:](../certifications/es/SC-300.md)

</details>

<a id="quiz-q23"></a>

## AZ-140 · Permisos de perfiles de AVD

Un estudiante abre una sesión agrupada asignada de Azure Virtual Desktop, pero FSLogix recibe acceso denegado en su carpeta de perfil SMB. Tiene acceso al recurso compartido, mientras los permisos NTFS de la carpeta lo deniegan. ¿Qué corrección responde mejor a las evidencias?

- **A.** Corregir los permisos NTFS de la carpeta manteniendo el aislamiento adecuado entre usuarios y validar el montaje del perfil como ese estudiante.
- **B.** Conceder al estudiante un rol Colaborador más amplio del plano de control de Azure sin cambiar los permisos de la carpeta.
- **C.** Reasignar el grupo de aplicaciones de escritorio y suponer que la asignación también concede acceso NTFS al perfil.
- **D.** Recrear la imagen del host de sesión conservando la misma ruta de perfil y los permisos NTFS que deniegan acceso.

<details>
<summary>Por qué:</summary>

**A. Corregir los permisos NTFS de la carpeta manteniendo el aislamiento adecuado entre usuarios y validar el montaje del perfil como ese estudiante.**

Acceder a un perfil SMB exige tanto acceso al recurso compartido como permisos del sistema de archivos. Las evidencias identifican una denegación NTFS; corregir el acceso previsto preservando el aislamiento de otros estudiantes aborda el fallo inmediato. Pruebe con la identidad afectada e inspeccione el montaje de FSLogix. La asignación del escritorio y la administración de recursos son límites distintos; abrir una sesión no demuestra acceso al perfil persistente.

- **B.** Un rol de administración del plano de control no corrige por sí solo la denegación NTFS identificada en la carpeta SMB del perfil del estudiante.
- **C.** La asignación del grupo de aplicaciones ofrece el escritorio al usuario, pero no concede por sí sola el acceso necesario al sistema de archivos de perfiles.
- **D.** Sustituir el host manteniendo el acceso denegado a la misma carpeta deja intacto el fallo identificado de permisos de almacenamiento en la nueva sesión.

[Fuente:](https://learn.microsoft.com/en-us/fslogix/how-to-configure-storage-permissions) · [Para repasar:](../certifications/es/AZ-140.md)

</details>

<a id="quiz-q24"></a>

## AZ-140 · Margen de capacidad ante fallos de AVD

Un laboratorio sintético de AVD necesita 60 sesiones simultáneas. Las pruebas admiten un máximo de 10 sesiones por host sano. Todos deben estar listos antes de clase y mantener 60 sesiones tras fallar cualquiera de ellos. ¿Cuál es el número mínimo de hosts preparados?

- **A.** Seis hosts.
- **B.** Cinco hosts.
- **C.** Ocho hosts.
- **D.** Siete hosts.

<details>
<summary>Por qué:</summary>

**D. Siete hosts.**

La demanda medida exige seis hosts sanos: 60 dividido entre 10 sesiones por host. Un host adicional preparado aporta margen para un fallo y deja seis disponibles después. Por tanto, siete es el mínimo con estos supuestos explícitos. El plan real también debe considerar arranque, modo de purga, capacidad degradada, carga de almacenamiento al iniciar sesión y permisos; arrancar otro host más tarde no cumple la preparación previa a clase.

- **A.** Seis hosts cubren la demanda solo mientras todos estén sanos; perder uno deja capacidad para 50 sesiones con el límite medido por host.
- **B.** Cinco hosts ofrecen únicamente 50 sesiones incluso antes de un fallo, así que no pueden atender a los 60 estudiantes simultáneos con estos supuestos.
- **C.** Ocho hosts cumplirían el requisito, pero siete ya conservan seis hosts sanos tras un fallo; por tanto, ocho supera el mínimo solicitado.

[Fuente:](https://learn.microsoft.com/en-us/azure/virtual-desktop/autoscale-create-assign-scaling-plan) · [Para repasar:](../certifications/es/AZ-140.md)

</details>

<a id="quiz-q25"></a>

## AI-103 · Revocación de acceso en la recuperación

Un estudiante pierde permisos sobre un cuaderno de investigación, pero un asistente conserva pasajes en caché. La política exige acceso vigente antes de enviar cualquier pasaje al modelo. La aplicación no puede establecer la vigencia de los permisos. ¿Qué comportamiento cumple la política?

- **A.** Enviar el pasaje en caché eliminando su cita para no nombrar el cuaderno.
- **B.** Seguir sirviendo el pasaje en caché hasta la próxima actualización programada del índice.
- **C.** Enviar el pasaje con una instrucción para que el modelo no revele material al que el estudiante no tenga acceso.
- **D.** Retener el pasaje hasta verificar el acceso y aplicar autorización vigente a los resultados de recuperación y caché.

<details>
<summary>Por qué:</summary>

**D. Retener el pasaje hasta verificar el acceso y aplicar autorización vigente a los resultados de recuperación y caché.**

La política sitúa la autorización antes del acceso del modelo, también para contenido en caché. Si no puede establecerse la vigencia del permiso, retener el pasaje preserva ese límite. La aplicación debe validar recuperación y caché frente a revocaciones, cambios de grupos e índices obsoletos. Una instrucción o cita eliminada no revierte la exposición al modelo. Las funciones nativas de permisos y los filtros personalizados necesitan comprobaciones independientes de capacidad y aplicación.

- **A.** Eliminar una cita cambia la presentación, pero el contenido no autorizado del cuaderno seguiría llegando al modelo y disponible para generar la respuesta.
- **B.** Una actualización programada deja una brecha que incumple la política de permisos vigentes, especialmente si los pasajes en caché sobreviven a cambios del índice.
- **C.** La instrucción delega la decisión de acceso en la generación después de revelar contenido; no impone el límite exigido antes de que llegue al modelo.

[Fuente:](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) · [Para repasar:](../certifications/es/AI-103.md)

</details>

<a id="quiz-q26"></a>

## AI-103 · Resultados desconocidos de herramientas

Una herramienta de agente aprobada solicita crear un único uso compartido de apuntes. El backend acepta una clave de operación estable, pero la respuesta agota el tiempo y el uso compartido puede existir. Hay una consulta de estado. ¿Qué debe hacer después la aplicación?

- **A.** Registrar un resultado desconocido, conciliar el estado mediante la clave de operación y reutilizarla si hace falta un reintento compatible.
- **B.** Reintentar inmediatamente con una clave nueva para que el backend trate la solicitud como una acción diferente.
- **C.** Marcar la operación como definitivamente fallida y descartar la clave porque no llegó una respuesta.
- **D.** Pedir al modelo que deduzca el éxito de su solicitud anterior y declarar la finalización sin consultar el backend.

<details>
<summary>Por qué:</summary>

**A. Registrar un resultado desconocido, conciliar el estado mediante la clave de operación y reutilizarla si hace falta un reintento compatible.**

Un tiempo de espera agotado tras enviar la solicitud no demuestra si ocurrió el efecto. Conservar un estado desconocido explícito y una clave estable permite consultar el backend y conciliar antes de otra escritura. Si admite reintentos, la misma clave lógica preserva la idempotencia prevista. Siguen siendo necesarias aprobación y validación de argumentos; la llamada propuesta por el modelo no demuestra que el backend completara el uso compartido autorizado.

- **B.** Una clave nueva convierte el reintento en otra operación, que puede crear otro uso compartido si la primera solicitud ya se confirmó correctamente.
- **C.** No recibir respuesta significa resultado incierto, no fallo definitivo; descartar la clave también elimina el identificador disponible para conciliar el estado.
- **D.** La solicitud generada describe el trabajo previsto; solo las evidencias del backend pueden confirmar si realmente se creó el uso compartido solicitado.

[Fuente:](https://learn.microsoft.com/en-us/azure/architecture/patterns/asynchronous-request-reply) · [Para repasar:](../certifications/es/AI-103.md)

</details>

<a id="quiz-q27"></a>

## DP-700 · Orden de eliminaciones incrementales

Una carga de matrículas de Fabric procesa la secuencia de origen 98, que elimina la matrícula E. Después llega una actualización retrasada de E con secuencia 94. Las secuencias del origen determinan el orden de los cambios y puede haber una nueva matrícula legítima posterior. ¿Qué regla de combinación conserva el estado correcto?

- **A.** Aplicar la actualización 94 porque llegó más recientemente a la canalización.
- **B.** Ignorar permanentemente cualquier cambio futuro de E tras observar una eliminación.
- **C.** Conservar la información de eliminación y versión 98, rechazar la actualización 94 por antigua y permitir un cambio posterior válido.
- **D.** Descartar el punto de control y reproducir estrictamente el orden de llegada sin comparar versiones.

<details>
<summary>Por qué:</summary>

**C. Conservar la información de eliminación y versión 98, rechazar la actualización 94 por antigua y permitir un cambio posterior válido.**

La secuencia del origen determina el orden válido de los cambios: la actualización 94 no debe resucitar una matrícula eliminada en la 98. Conservar eliminación y versión permite que una combinación idempotente rechace cambios obsoletos y acepte versiones posteriores válidas. El orden de llegada no sustituye al del origen. Se necesitan claves estables, comparación determinista de versiones y progreso duradero; volver a procesar entradas sin esas reglas no corrige el problema de orden.

- **A.** La llegada puede diferir del orden de cambios del origen; aplicar la actualización antigua resucitaría incorrectamente una matrícula eliminada por un cambio posterior.
- **B.** Una prohibición permanente también rechazaría una nueva matrícula legítima posterior; la combinación debe comparar versiones, no impedir todo cambio futuro para esa clave.
- **D.** Reproducir el mismo orden de llegada sin comprobar versiones puede repetir la resurrección; eliminar el punto de control no establece el orden de negocio autorizado.

[Fuente:](https://learn.microsoft.com/en-us/fabric/data-engineering/delta-lake-change-data-feed) · [Para repasar:](../certifications/es/DP-700.md)

</details>

<a id="quiz-q28"></a>

## DP-700 · Rutas de acceso de Fabric

Un informe universitario aplica correctamente restricciones por fila y tiene una etiqueta de confidencialidad. El mismo analista puede leer archivos subyacentes con detalle estudiantil por una ruta de OneLake para la que tiene permisos. La política solo permite totales por módulo. ¿Qué debe cambiar y validar el ingeniero?

- **A.** Renombrar la etiqueta como Muy confidencial y suponer que su nombre aplica las restricciones por fila del informe a la lectura directa de archivos.
- **B.** Restringir la ruta subyacente a los permisos mínimos necesarios y probar como el analista los totales permitidos y el detalle denegado.
- **C.** Ocultar la tabla detallada del informe sin cambiar los permisos directos del analista sobre archivos.
- **D.** Conceder un rol de área de trabajo más amplio para que las restricciones por fila del informe rijan automáticamente todas las rutas.

<details>
<summary>Por qué:</summary>

**B. Restringir la ruta subyacente a los permisos mínimos necesarios y probar como el analista los totales permitidos y el detalle denegado.**

Una restricción del informe o motor de consultas no rige automáticamente una ruta independiente de archivos. El ingeniero debe alinear permisos de área de trabajo, elemento, motor y archivos con la política y probar cada ruta prevista como el analista. Una etiqueta aporta contexto de gobierno o protección configurada, pero su nombre no implementa autorización equivalente en todas partes. Ampliar permisos puede abrir otras rutas en vez de cerrar esta brecha.

- **A.** Cambiar el nombre de clasificación no configura el límite independiente de archivos ni hace que las restricciones del motor del informe se apliquen automáticamente en OneLake.
- **C.** Ocultar contenido del informe solo cambia esa presentación; el analista conserva la ruta directa indicada a los archivos subyacentes con detalle de estudiantes.
- **D.** Un rol de área de trabajo más amplio aumenta el acceso; no convierte las restricciones del informe en una regla universal para todos los motores y archivos.

[Fuente:](https://learn.microsoft.com/en-us/fabric/security/permission-model) · [Para repasar:](../certifications/es/DP-700.md)

</details>

<a id="quiz-q29"></a>

## SC-100 · Responsabilidad del riesgo residual

Un arquitecto documenta que la plataforma propuesta de apuntes conserva un riesgo material de interrupción tras aplicar controles viables. Seguridad recomienda continuar, pero el gobierno exige aceptación del riesgo de negocio. ¿Quién debe autorizar la aceptación de ese riesgo residual?

- **A.** El analista del SOC que puede cerrar el ticket de seguridad relacionado.
- **B.** El responsable del riesgo de negocio con autoridad decisoria adecuada, registrando la exposición y las condiciones de revisión.
- **C.** El proveedor del producto, porque su puntuación de cumplimiento sustituye la decisión de negocio de la universidad.
- **D.** El administrador de nube, únicamente porque puede desplegar los recursos.

<details>
<summary>Por qué:</summary>

**B. El responsable del riesgo de negocio con autoridad decisoria adecuada, registrando la exposición y las condiciones de revisión.**

El riesgo residual sigue siendo exposición de negocio después de elegir controles técnicos. El responsable autorizado debe decidir si es aceptable usando las evidencias del arquitecto sobre impacto, supuestos de probabilidad, alternativas y brechas restantes. La decisión debe incluir alcance, condiciones de revisión y responsabilidad. Las recomendaciones de seguridad, los permisos de despliegue y las evaluaciones del proveedor informan la decisión, pero no otorgan automáticamente la autoridad universitaria requerida para aceptar riesgos.

- **A.** Cerrar un ticket operativo es un permiso del flujo de trabajo; no establece autoridad para aceptar una exposición material de negocio de la universidad.
- **C.** La evaluación de un proveedor puede orientar controles, pero no sustituye la decisión responsable de la universidad sobre su propio riesgo operativo restante.
- **D.** Poder desplegar recursos es autoridad técnica; el escenario exige por separado un responsable de negocio autorizado para aceptar el riesgo residual de interrupción.

[Fuente:](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/govern/assess-cloud-risks) · [Para repasar:](../certifications/es/SC-100.md)

</details>

<a id="quiz-q30"></a>

## SC-100 · Validación de objetivos de recuperación

Un ejercicio fija un RTO de dos horas y un RPO de 15 minutos. La interrupción empieza a las 11:00 UTC. Las lecturas autorizadas se restablecen a las 12:30 con datos solo hasta las 10:40. Estos son los límites de medición acordados. ¿Qué evaluación es correcta?

- **A.** Se cumplen ambos objetivos porque el servicio volvió antes de dos horas.
- **B.** Se cumple el RPO, pero se incumple el RTO.
- **C.** Se incumplen ambos porque cualquier pérdida de datos viola el RTO.
- **D.** Se cumple el RTO, pero se incumple el RPO porque el punto recuperado es 20 minutos anterior a la interrupción.

<details>
<summary>Por qué:</summary>

**D. Se cumple el RTO, pero se incumple el RPO porque el punto recuperado es 20 minutos anterior a la interrupción.**

El RTO mide la interrupción aceptable: las lecturas autorizadas vuelven tras 90 minutos, dentro del objetivo de dos horas. El RPO mide pérdida reciente aceptable: recuperar hasta las 10:40 ante una interrupción a las 11:00 deja 20 minutos, más que los 15 permitidos. Son comprobaciones independientes; cumplir una no implica cumplir la otra. El ejercicio debe registrar ambas medidas y las dependencias que permitieron reanudar la operación definida.

- **A.** Restablecer el servicio dentro del plazo cumple solo el RTO; la brecha independiente de 20 minutos del punto recuperado sigue superando el RPO indicado.
- **B.** La interrupción dura 90 minutos, menos de dos horas, mientras la brecha de datos de 20 minutos supera 15; esta opción invierte los resultados.
- **C.** El RTO trata la duración de la interrupción, no si se pierden datos; los 90 minutos medidos cumplen ese objetivo pese al incumplimiento del RPO.

[Fuente:](https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recover-hadr-overview) · [Para repasar:](../certifications/es/SC-100.md)

</details>

<a id="quiz-q31"></a>

## AZ-120 · Aislamiento y escritor único de SAP

En un ejercicio de clúster SAP HANA se pierde comunicación con el primario y el secundario no puede aislarlo mediante fencing. No se confirma que el primario haya dejado de aceptar escrituras. ¿Qué respuesta protege mejor la integridad antes de la toma de control?

- **A.** Desactivar fencing y promover el secundario para que el panel muestre inmediatamente los recursos en ejecución.
- **B.** Promover el secundario porque el último estado correcto de replicación demuestra que el primario anterior ya no puede escribir.
- **C.** Seguir el procedimiento compatible de incidentes para restaurar o verificar fencing y confirmar el aislamiento del escritor anterior antes de permitir escrituras tras la toma de control.
- **D.** Mover la dirección virtual de servicio al secundario dejando sin cambios la capacidad incierta de escritura del primario.

<details>
<summary>Por qué:</summary>

**C. Seguir el procedimiento compatible de incidentes para restaurar o verificar fencing y confirmar el aislamiento del escritor anterior antes de permitir escrituras tras la toma de control.**

Perder comunicación no demuestra que el primario se haya detenido. Fencing aísla un nodo que no puede continuar con seguridad, protege el requisito de escritor único y reduce el riesgo de primarios simultáneos. El equipo debe investigar fencing y cuórum compatibles, preservar evidencias de estado y confirmar el aislamiento antes de permitir escrituras. El estado de replicación o mover una dirección no aíslan al nodo; desactivar fencing elimina una protección crítica.

- **A.** Desactivar fencing elimina el mecanismo que aísla un escritor incierto; la disponibilidad aparente puede lograrse a costa de tener primarios en conflicto.
- **B.** Un resultado anterior de replicación describe el movimiento de datos en ese momento; no demuestra que el primario inaccesible haya dejado de aceptar escrituras ahora.
- **D.** Mover una dirección virtual cambia una ruta de clientes, pero no impide por sí solo que el primario anterior escriba mediante otras sesiones o rutas.

[Fuente:](https://learn.microsoft.com/en-us/azure/sap/workloads/sap-hana-high-availability) · [Para repasar:](../certifications/es/AZ-120.md)

</details>

<a id="quiz-q32"></a>

## AZ-120 · Escrituras de SAP después del cambio

Una migración universitaria de SAP abre el destino para compras y los usuarios crean pedidos nuevos. El origen sin cambios permanece aislado. Un problema posterior de validación lleva a considerar una reversión. ¿Qué plan protege mejor las nuevas transacciones de negocio?

- **A.** Congelar escrituras, establecer el estado de referencia de los datos, preservar las transacciones del destino y acordar conciliación o migración inversa compatible antes de reabrir un escritor.
- **B.** Apuntar DNS al origen sin cambios y suponer que contiene los nuevos pedidos del destino.
- **C.** Sobrescribir el destino desde el origen antiguo y reabrir compras sin identificar las transacciones creadas después del cambio.
- **D.** Reabrir origen y destino para escrituras mientras los usuarios deciden más tarde qué pedidos conservar.

<details>
<summary>Por qué:</summary>

**A. Congelar escrituras, establecer el estado de referencia de los datos, preservar las transacciones del destino y acordar conciliación o migración inversa compatible antes de reabrir un escritor.**

Una vez que el destino acepta escrituras, revertir es también una decisión sobre datos. Volver al origen sin cambios puede abandonar pedidos nuevos; abrir ambos lados puede bifurcar transacciones. El procedimiento debe congelar escrituras, preservar evidencias y datos nuevos, elegir un estado de referencia y usar conciliación o movimiento inverso compatible con los responsables de negocio. La validación y el control de escritor único deben preceder a reabrir compras.

- **B.** DNS redirige clientes, pero no copia al origen sin cambios los pedidos posteriores al cambio; volver atrás por sí solo puede abandonar esas transacciones.
- **C.** Sobrescribir desde el origen obsoleto puede destruir pedidos legítimos del destino; antes hay que identificar y preservar los cambios de negocio posteriores al cambio.
- **D.** Permitir escrituras en ambos entornos crea historiales de transacciones divergentes, dificulta la conciliación y rompe el control requerido de un escritor autorizado.

[Fuente:](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/migrate/execute-migration) · [Para repasar:](../certifications/es/AZ-120.md)

</details>
