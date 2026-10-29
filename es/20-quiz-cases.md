# Ocho escenarios para practicar

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
