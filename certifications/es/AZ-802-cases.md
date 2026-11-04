# AZ-802 · 10 casos con respuestas razonadas

[Guía](AZ-802.md) · [Cuaderno de cinco unidades](AZ-802-workbook.md) · [Índice](README.md)

Son escenarios originales de un laboratorio universitario, no preguntas oficiales. Antes de abrir la respuesta, plantea una hipótesis, otra explicación posible y la evidencia necesaria. Las consultas propuestas corresponden a un laboratorio Windows autorizado; no se afirma ejecución ni recuperación de producción. Cada pregunta incluye el escenario completo para conservar el contexto en el entrenador y en Anki.

## 1. Tras un cambio de red del aula, un cliente de dominio resuelve webs públicas pero no encuentra su controlador. Usa un DNS público; el DNS de AD previsto es accesible y sus registros SRV son correctos. El reloj del cliente está bien. ¿La primera reparación debería restablecer las contraseñas de todos los estudiantes?

<details>
<summary>Respuesta</summary>

No. La evidencia apunta primero al camino de resolución del cliente. Resolver nombres públicos no demuestra que se descubran los registros privados de AD. Anota resolver, consulta SRV y resultado, y compáralos con la configuración DNS aprobada del laboratorio. La corrección adecuada recupera el camino que conoce AD y valida descubrimiento, acceso al controlador e inicio de sesión afectado antes de ampliar el cambio.

Los supuestos de servidor sano y tiempo correcto delimitan esta investigación; no significan que todos los fallos reales de autenticación procedan de DNS. Si el descubrimiento funciona pero la autenticación falla, continúa con error exacto, estado de cuenta, protocolo y canal seguro. Conserva un antes/después con horas y controlador realmente seleccionado. Resetear todas las contraseñas cambiaría estado ajeno sin resolver el desajuste y podría ocultar evidencia útil. La reversión consiste en recuperar la configuración registrada si el cambio aprobado rompe otra resolución necesaria, no en dejar una mezcla de resolvers públicos y privados cuyo comportamiento no se ha entendido.

</details>

## 2. Un cambio de grupo de investigación aparece en LAB-DC1 pero no en el controlador del edificio remoto. Los clientes usan este segundo controlador, la replicación informa de fallos relacionados con DNS y sigue denegado el acceso a un recurso compartido nuevo. ¿Conviene añadir al usuario a otro grupo privilegiado?

<details>
<summary>Respuesta</summary>

No. Las versiones distintas del directorio y el fallo de replicación ofrecen una explicación concreta que investigar antes de ampliar privilegios. Anota cuándo cambió el grupo, qué controlador aceptó el cambio, cuál selecciona el cliente y qué errores aparecen. Revisa registros DNS y resolvers de los asociados de replicación, conectividad y requisitos de autenticación. Comprueba la asociación de la subred remota al sitio previsto, pero no supongas que cambiar una programación arregla un fallo DNS.

Tras una reparación compatible, verifica que esa pertenencia concreta llega al controlador relevante. Después obtén un nuevo contexto de sesión/token del usuario adecuado y prueba el recurso con su identidad: convergencia del directorio y renovación de autorización son comprobaciones distintas. Si sigue fallando, revisa permisos compartidos y del sistema de archivos. Mantén el grupo limitado y documenta una prueba permitida y otra denegada. Añadir un grupo privilegiado ajeno podría ocultar el síntoma, dejar rota la replicación y ampliar acceso. El entregable es una cronología de cambio y acceso, con observaciones previstas identificadas hasta obtener resultados reales del laboratorio.

</details>

## 3. Un aula de una sede aislada utilizará un RODC. Se propone almacenar allí las contraseñas de administradores privilegiados de la universidad para acceder durante cortes WAN. La protección física es menor que en el centro de datos. ¿Qué debe exigir la revisión?

<details>
<summary>Respuesta</summary>

Rechaza que un RODC haga segura cualquier credencial almacenada. Revisa directiva de replicación de contraseñas, pertenencias permitidas y denegadas efectivas, administración delegada y respuesta ante pérdida. Las cuentas privilegiadas deben quedar fuera de esa caché de sucursal. Si una cuenta está permitida y denegada bajo la directiva efectiva, prevalece la denegación. Identifica qué cuentas ordinarias necesitan realmente acceso desconectado y comprueba el resultado, sin fiarte solo del nombre de un grupo.

El diseño debe distinguir autenticación de usuarios almacenados de operaciones que necesitan un controlador escribible, incluidos cambios nuevos del directorio. Define servicios disponibles durante el corte y una vía de administración aprobada que no debilite el dominio. La evidencia incluye amenazas asumidas, cuentas seleccionadas, decisiones efectivas de caché, conectividad y procedimiento ante pérdida del equipo. No publiques contraseñas ni contenido de caché. Recuperarse exige considerar credenciales afectadas y servidor comprometido; reemplazar el hardware no demuestra que los secretos del directorio hayan permanecido protegidos.

</details>

## 4. Un servidor conectado a Azure Arc sigue fallando en un trabajo remoto desde B hacia el servidor de archivos C. Se propone delegación amplia de credenciales y una cuenta virtual JEA por defecto en un controlador. La tarea solo necesita una operación de servicio limitada. ¿Justifica Arc este diseño?

<details>
<summary>Respuesta</summary>

No. Arc crea una relación de administración con Azure; no une el servidor a AD ni crea una confianza, y tampoco delega automáticamente las credenciales del operador hacia C. Dibuja primer y segundo salto, protocolo, identidad efectiva y operación exacta. Diagnostica el límite de autenticación o autorización que falla. Una primera sesión correcta no demuestra que el segundo recurso acepte la identidad prevista.

Revisa opciones compatibles de segundo salto y sus límites. CredSSP añade exposición de credenciales; la delegación restringida no resuelve de forma genérica un segundo salto WinRM-a-WinRM. En JEA, inspecciona conjuntamente identidad de ejecución, usuarios, comandos, parámetros y auditoría. La cuenta virtual por defecto en un DC puede tener privilegios Domain Admin, desproporcionados para una tarea limitada. Prefiere ubicación administrativa apropiada y derechos de ejecución expresamente restringidos. La evidencia es un diagrama de permisos y saltos con operaciones permitidas y denegadas, no un comando que funciona usando credenciales reutilizables de administrador. Los permisos para extensiones de un controlador administrado con Arc también necesitan revisión separada.

</details>

## 5. Una VM usa checkpoints Production, pero falla la consistencia del invitado y el host crea un Standard. Un estudiante lo presenta como backup independiente y coherente con la aplicación. Checkpoint y discos de VM comparten almacenamiento. ¿Qué afirmaciones hay que corregir?

<details>
<summary>Respuesta</summary>

Corrige tanto la consistencia como el límite de protección. Production puede permitir recurrir a Standard: el ajuste solicitado aporta menos evidencia que el tipo real y el resultado del procesamiento del invitado. Si la práctica exige Production sin esa alternativa, evalúa ProductionOnly y corrige integración/VSS o los requisitos de congelación del sistema de archivos que correspondan. Que se rechace crear un checkpoint inadecuado es evidencia útil; aceptar otro silenciosamente no es equivalente.

Incluso un checkpoint Production correcto no constituye por sí mismo un backup retenido independiente. Su cadena puede perderse con el almacenamiento de la VM, y recuperar la aplicación exige un método de consistencia y restauración compatible. Conserva backup protegido, retención y validación de restauración si el requisito lo pide. Inspecciona metadatos y margen de espacio mediante herramientas compatibles; no borres AVHDX a mano. Explica por separado si buscas revertir un cambio desechable, sobrevivir a perder host/almacenamiento o recuperar un estado histórico válido. Cada objetivo necesita evidencia distinta y quizá otro mecanismo.

</details>

## 6. Los equipos existentes del aula siguen funcionando, pero los nuevos no reciben dirección. El DHCP autorizado es accesible mediante un relay operativo y el ámbito afectado no tiene concesiones libres. Hay otro servidor instalado, sin relación de failover. ¿Qué permite concluir la investigación?

<details>
<summary>Respuesta</summary>

La evidencia identifica agotamiento del ámbito como problema inmediato de las asignaciones nuevas. Los clientes existentes pueden continuar según sus concesiones; su funcionamiento no demuestra capacidad para asignar otra IP. Revisa rango, exclusiones, reservas, concesiones activas y subred real antes de proponer una ampliación aprobada. Investiga patrones inesperados, pero no elimines concesiones indiscriminadamente ni invadas un rango superpuesto.

Instalar un segundo servidor no coordina las concesiones. Si se necesita disponibilidad, diseña una relación DHCP failover compatible para los ámbitos adecuados, entendiendo modo, estado, comportamiento de concesiones y recuperación. No actives copias no coordinadas del mismo rango. La evidencia incluye inventario del ámbito, direcciones disponibles, relay y una prueba con cliente realmente nuevo además de otro existente. Capacidad y failover tratan fallos distintos: una relación sana no permite ignorar un pool insuficiente. Registra el ámbito anterior y detén el cambio si el rango propuesto entra en conflicto con enrutamiento u otra autoridad de asignación.

</details>

## 7. Una estudiante tiene el permiso SMB previsto, pero NTFS deniega la carpeta del proyecto. Azure File Sync está sano y hay archivos por niveles en el endpoint de servidor. ¿Otorgar Azure Contributor y llamar backup a la copia sincronizada resuelve ambos problemas?

<details>
<summary>Respuesta</summary>

No. Sigue la ruta e identidad reales de Windows. La denegación NTFS sigue importando aunque exista acceso al recurso compartido. Corrige autorización de carpeta con grupos y aislamiento apropiados; prueba a la estudiante afectada y a otra que deba seguir sin acceso. Un rol de administración de recursos Azure no repara automáticamente la ACL ni demuestra acceso a datos SMB. Comprueba acceso efectivo, no lo deduzcas de una sola entrada.

Trata la recuperación por separado. Una sincronización sana puede propagar borrados, y los archivos por niveles quizá no constituyan una copia local completa e independiente. Identifica endpoint de nube, backups retenidos utilizables, dependencias y procedimiento compatible. Revertir o clonar un servidor registrado de File Sync desde una imagen de sistema o checkpoint no es una recuperación genérica compatible. La evidencia debe mostrar decisión share/NTFS, estado de endpoints y niveles, y plan para un punto histórico. Recuperar acceso hoy y recuperar datos después de otro error son resultados diferentes: ninguno debe afirmarse sin su prueba o diseño explícitamente identificado.

</details>

## 8. Hay Windows Server 2022 y 2025. Se propone aplicar a todos una línea base OSConfig de 2025 y garantizar que retirarla restaura cualquier ajuste previo. Además, una contraseña LAPS obtenida aparece en un informe compartido. ¿Qué debe cambiar?

<details>
<summary>Respuesta</summary>

Separa compatibilidad, recuperación del cambio y tratamiento de secretos. La guía OSConfig revisada se dirige a Windows Server 2025; no presentes la misma configuración como compatible con los equipos 2022. Registra versiones, ajustes por rol y grupo piloto. Identifica GPO u otra administración que pueda entrar en conflicto, inspecciona configuración efectiva y planifica reinicio y validación de acceso. Retirar la línea base no garantiza reconstruir cada valor anterior: conserva estado previo y procedimiento de recuperación revisado.

LAPS permite rotación controlada, respaldo y recuperación autorizada. Copiar una contraseña a un informe de amplia lectura rompe ese límite. Trátalo mediante el procedimiento de incidente/cambio apropiado, retira la exposición y rota cuando corresponda; publica únicamente evidencia saneada de directivas y autorización. Las credenciales de recuperación deben estar protegidas y seguir disponibles durante el fallo previsto. La evidencia debe demostrar despliegue compatible, roles permitidos y denegados de consulta, auditoría y recuperación, no una contraseña en claro ni una captura de cumplimiento tomada como prueba de toda protección.

</details>

## 9. Un servidor Arc aparece conectado y el workspace contiene Heartbeat recientes del agente, pero faltan los eventos Windows System requeridos. Estos existen localmente. ¿La consulta vacía demuestra que Windows no generó fallos?

<details>
<summary>Respuesta</summary>

No. El caso ya establece que existen eventos relevantes en origen. Conexión de Arc y Heartbeat son observaciones distintas de entregar el origen de eventos seleccionado. Confirma máquina, intervalo, workspace y tabla previstos; después inspecciona extensión/servicio AMA, DCR asociada, selección de eventos, destino y configuración realmente recibida. Crear una DCR sin asociarla a la máquina no basta para recopilar sus datos.

Usa un identificador y hora de evento local saneados para seguir un registro por el recorrido propuesto. Distingue ausencia en origen, fallo de recogida, transporte/configuración y consulta dirigida al destino incorrecto. Separa momento del evento de llegada y contempla retraso de ingesta documentado, sin dar cualquier demora por aceptable. La evidencia incluye registro local, identidad de máquina, asociación y contexto de consulta, seguidos de una prueba de llegada esperada. No reinstales todos los agentes como primer paso: cambia estado y puede borrar contexto útil sin corregir la selección o asociación que falta.

</details>

## 10. Un estudiante borra un objeto AD importante y descubre que Recycle Bin no estaba habilitado antes. Propone devolver un controlador de producción a un checkpoint normal e incautar todos los FSMO. Hay backup de directorio compatible y responsable de recuperación asignado. ¿Cuál es el proceso de decisión más seguro?

<details>
<summary>Respuesta</summary>

Recurre al procedimiento documentado y conserva evidencia de borrado, replicación y backup. Activar Recycle Bin después no crea mágicamente un estado recuperable anterior. Determina objeto y dependencias afectados, backup utilizable y alcance antes de elegir el método. Un error sobre un objeto no justifica por sí solo recuperar todo el bosque ni incautar roles ajenos.

El responsable debe seleccionar los pasos autoritativos o no autoritativos compatibles con el fallo real, incluido DSRM cuando corresponda, credenciales protegidas y consideraciones SYSVOL. Una reversión genérica de VM no sustituye ese plan. Documenta estado autoritativo, implicaciones de replicación, validación y condiciones para que el antiguo titular pueda volver a conectarse si realmente se necesita incautar un rol FSMO. Verifica objetos, autenticación, replicación y servicio afectado, sin detenerte en «la VM arranca». En este repositorio se entrega una simulación de escritorio con decisiones explícitas: no se han ejecutado restauraciones de directorio, incautaciones ni mediciones de recuperación.

</details>

Las referencias y condiciones de versión están en la [guía](AZ-802.md). Desarrolla evidencia y cambios controlados en el [cuaderno](AZ-802-workbook.md).
