# AZ-802 · Cuaderno Windows Server basado en evidencias

[Guía](AZ-802.md) · [10 casos razonados](AZ-802-cases.md) · [Índice](README.md)

Cinco unidades equivalentes reúnen las siete áreas de AZ-802. Usa el laboratorio universitario aislado e inventado `lab.example.test`. Entrega una decisión y evidencia revisables, no una lista de ajustes copiados de un vídeo. Son ejercicios propuestos para Windows: no se afirma ejecución en AD, Hyper-V o Azure, restauración ni aplicación de controles. Sin laboratorio compatible, entrega diseño y observaciones previstas, identificados como tales, en lugar de inventar resultados.

Mantén un registro por unidad: estado inicial, hipótesis, explicación alternativa, consulta de solo lectura elegida, cambio propuesto, observación esperada, resultado real si se ejecuta y condición de detención/reversión. Anota edición/versión, módulos, derechos necesarios e identidad destino. Elimina secretos y datos personales. La matriz de requisitos de la guía acompaña sus comandos; ningún ejemplo concede autoridad para inspeccionar otro sistema.

<a id="az-802-unit-1"></a>

## 1. Seguir un cambio de identidad hasta el acceso

**Escenario:** LAB-DC1 acepta una nueva pertenencia al grupo de investigación, pero un cliente del edificio remoto sigue sin entrar en `\\LAB-FS1\LabNotes`. El cliente selecciona LAB-DC2. Otra propuesta instala un RODC en una sede con menor protección física.

**Investigación:** dibuja bosque/dominio, dos controladores escribibles, RODC, resolvers, sitios y subredes. Marca quién aceptó el cambio y a quién consulta el cliente. Identifica replicación, SRV relevantes, jerarquía de tiempo, token del usuario y límites share/NTFS. Elige comprobaciones ordenadas que distingan directorio sin actualizar de permisos efectivos incorrectos. Incluye una observación que refutaría tu primera hipótesis.

Utiliza las consultas de inventario, resolución/tiempo y replicación de la guía únicamente desde el contexto Windows adecuado. Para Group Policy, separa ámbito, procesamiento y resultado. Para el RODC, define cuentas ordinarias que necesitan acceso desconectado, cuentas que deben quedar denegadas, administración delegada y respuesta ante pérdida. Verifica la directiva efectiva de replicación de contraseñas y qué cuentas permite almacenar en caché, sin suponer que el nombre de un grupo lo demuestra.

**Evidencia:** topología con límites de identidad; consultas saneadas con contexto y hora; cronología del objeto; controlador previsto y observado; par de pruebas de acceso permitido/denegado; y decisión de caché RODC sin contraseñas.

**Entregable y límites:** redacta un diagnóstico de una página con reparación acotada. Conserva configuración original de resolver, sitio y directivas antes del cambio autorizado. Detente si controlador o espacio de nombres quedan fuera del laboratorio desechable. No amplíes privilegios, incautes FSMO ni resetees todas las cuentas para ocultar el síntoma. El éxito exige convergencia del cambio y acceso estrictamente previsto, manteniendo denegado al otro usuario.

<a id="az-802-unit-2"></a>

## 2. Revisar administración remota y recuperación de VM

**Escenario:** el operador llega a un servidor miembro pero falla hacia un segundo recurso. Se propone delegar credenciales reutilizables y ejecutar JEA en un DC. Por otro lado, falla la consistencia Production de una VM y se crea un Standard. Hay dos hosts de 64 GiB, reserva sintética de 12 GiB por host y doce invitados de 4 GiB fijos asignados a cada uno.

**Investigación:** dibuja saltos de autenticación, protocolos, identidades efectivas y operación necesaria. Compara un diseño compatible con riesgos de CredSSP y límites de protocolo de la delegación. Revisa comandos/parámetros JEA, grupos de ejecución, auditoría y ubicación; explica por qué la cuenta virtual predeterminada de un DC excede una tarea limitada de servicio miembro. En Arc, identifica por separado autoridad de extensiones Azure y permisos locales.

Usa inventario de VM, conmutadores, memoria y checkpoints para explicar red y recuperación. Compara checkpoint, Replica, clúster y backup según el fallo cubierto. Distingue Production de ProductionOnly y comprueba el tipo real. En el cálculo sintético, cada host usa normalmente 48 + 12 = 60 GiB; reunir los 24 invitados en uno exigiría 96 + 12 = 108 GiB. Declara supuestos y demuestra por qué caber normalmente no prueba capacidad tras perder un host.

**Evidencia:** esquema de permisos y saltos; revisión de endpoint restringido; camino conmutador/invitado; cálculo de memoria; metadatos reales si están disponibles; y copia independiente prevista para restauración.

**Entregable y límites:** propone administración compatible con permisos acotados y mecanismos de recuperación separados. Detente si delegar expone una identidad privilegiada real o desconoces los requisitos de consistencia. Registra configuración previa y acceso de recuperación. No borres AVHDX, afirmes que Replica repara corrupción lógica ni llames backup independiente a un checkpoint del mismo almacenamiento. Ejecutar un comando y recuperar un servicio con seguridad requieren validaciones distintas.

<a id="az-802-unit-3"></a>

## 3. Diagnosticar el camino de cliente a archivos

**Escenario:** los clientes nuevos no obtienen IP, pero siguen funcionando concesiones antiguas. Tras corregir la red de forma aprobada, un investigador llega al recurso compartido y recibe denegación de carpeta. El servidor está registrado en File Sync y tiene archivos por niveles. También hay un reenviador DNS condicional y un segundo DHCP sin configurar.

**Investigación:** sigue VLAN/relay, ámbito autorizado, exclusiones/reservas, opciones y capacidad libre. Define qué añade probar una asignación nueva frente a un cliente existente. Distingue segundo servidor de relación failover compatible configurada. Sigue resolver, espacio de nombres, destino condicional, camino de vuelta y puerto de aplicación; una respuesta DNS correcta no demuestra conexión SMB utilizable.

Registra después usuario real, permisos compartidos, herencia NTFS y contexto de grupos. Prueba una identidad permitida y otra que debe seguir denegada. En Azure Files separa identidad compatible, autorización del recurso compartido y permisos de directorio/archivo. Inventaría endpoints File Sync, supuestos de caché, backups retenidos independientes y procedimiento compatible. Rechaza expresamente restaurar/clonar/revertir sistema o VM registrados como recuperación genérica de File Sync.

**Evidencia:** hoja de asignación IP; esquemas de resolver y rutas; observaciones share/ACL sin secretos; criterios permitido/denegado; mapa de endpoints; y punto histórico elegido con dependencias.

**Entregable y límites:** explica fallo de red y fallo de permisos como hallazgos distintos. Conserva ámbito y ACL previos. Detente ante rangos superpuestos, ampliación de permisos no prevista o recuperación que depende de una copia sin proteger. El éxito exige configuración válida para el cliente nuevo, acceso para el usuario correcto, bloqueo del usuario denegado y una copia protegida identificada, no simplemente otro endpoint sincronizado.

<a id="az-802-unit-4"></a>

## 4. Diseñar seguridad por rol sin perder recuperación

**Escenario:** hay Windows Server 2022 y 2025, miembros, un DC y servidor de archivos. Se propone una única línea base OSConfig, exponer SMB sobre QUIC sin revisar certificados y compartir una contraseña LAPS en un informe. Se llama reversión completa a retirar la línea base.

**Investigación:** prepara una matriz de rol/versión antes de elegir controles. La guía OSConfig revisada se dirige a Windows Server 2025: registra módulo, escenario, diferencias esperadas, reinicio y posibles conflictos con GPO u otra gestión. Prueba el rol adecuado. Explica por qué retirar gestión no reconstruye necesariamente el estado anterior. Conserva ese estado protegido y otra vía autorizada de administración.

En LAPS separa rotación, destino de respaldo, consulta permitida, auditoría y recuperación. Documenta condiciones DSRM cuando correspondan sin obtener ni publicar contraseñas. Para SMB sobre QUIC comprueba servidor/cliente exactos: la guía revisada indica Server 2022 Datacenter: Azure Edition o ediciones Server 2025, con clientes Windows 11. Revisa confianza, nombres y clave privada del certificado y camino UDP permitido, conservando autorización share/archivo. QUIC no la sustituye.

**Evidencia:** matriz de roles/versiones; controles con soporte documentado; diferencias de ajustes y condición de reversión; roles de consulta permitidos/denegados; revisión saneada del certificado; y pruebas de acceso aisladas.

**Entregable y límites:** redacta un cambio por fases con responsables de recuperación. Detente ante una línea base incompatible, pérdida del único acceso de gestión, requisito de certificado pendiente o secreto real en evidencias. Tramita una exposición de credenciales existente mediante el procedimiento de respuesta. Cumplimiento, característica instalada y aplicación demostrada son observaciones diferentes.

<a id="az-802-unit-5"></a>

## 5. Seguir un evento ausente y ensayar recuperación AD

**Escenario:** el servidor Arc aparece conectado y AMA envía Heartbeat, pero un evento System requerido solo existe localmente. En otra simulación se borra un objeto AD sin Recycle Bin previamente habilitado. Hay backup de directorio compatible. El equipo plantea dos horas de recuperación y necesita más evidencia que «la VM arranca».

**Investigación:** sigue un evento local saneado por extensión/servicio AMA, DCR, asociación, selección de origen, destino e intervalo de consulta. Separa identidad de máquina, hora del evento y llegada. Diseña una prueba que distinga falta en origen, configuración de recogida y consulta a tabla/workspace equivocados. Explica qué demuestran Arc conectado y Heartbeat y qué dejan pendiente.

Para recuperar AD identifica objetos/dependencias, backup compatible, responsable, credenciales DSRM protegidas y alcance adecuado. Distingue objeto de Recycle Bin, recuperación autoritativa/no autoritativa, SYSVOL y bosque completo. Escoge procedimiento compatible con el fallo; no conviertas un borrado de objeto en reversión automática de DC o incautación FSMO. Ensaya orden de dependencias, efecto sobre replicación, validación y regreso seguro de servicios.

**Evidencia:** recorrido origen-destino; registro temporal de hipótesis; inventario de puntos recuperables; tiempos previstos identificados como estimaciones; y aceptación de objeto, autenticación, replicación, directivas y aplicación afectada.

**Entregable y límites:** entrega procedimientos separados de supervisión y recuperación. Conserva DCR/asociación originales. Detente si alcance o copia autoritativa no están claros. Registra interrupción del negocio y antigüedad de datos para distinguir RTO y RPO. Solo marca una operación completada cuando el laboratorio autorizado la ejecute y aporte las observaciones previstas. Este repositorio no afirma restauración Windows/AD ni resultado medido de dos horas.

Termina contestando los [diez casos](AZ-802-cases.md) sin abrir sus respuestas. En cada dificultad identifica evidencia ausente o límites confundidos y vuelve al apartado correspondiente de la [guía](AZ-802.md). Este cuaderno ofrece práctica seleccionada, no cobertura exhaustiva ni predicción de aprobar.
