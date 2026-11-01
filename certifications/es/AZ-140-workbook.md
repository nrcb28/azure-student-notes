# AZ-140 · Cuaderno avanzado común

[Guía](AZ-140.md) · [10 casos](AZ-140-cases.md) · [Índice](README.md)

Cinco unidades equivalentes entre idiomas. Trabaja sin conexión con la app de apuntes y el aula virtual. Identifica las predicciones como tales: no se despliega nada, no se cambia un tenant y no se acredita preparación para producción.

<a id="az-140-unit-1"></a>

## 1. Relacionar recursos, usuarios y responsabilidades

Dibuja un aula compartida para 48 estudiantes y un escritorio personal para un investigador. Identifica pools, hosts, grupos de aplicaciones, registro en workspace y asignaciones. Separa broker y gateway de Microsoft de imágenes, VM, red, identidad y almacenamiento del cliente. Explica por qué multisesión compatible no equivale a asignación personal.

**Caso:** un estudiante ve VM en Azure, pero no recibe escritorios. **Evidencia:** diagrama de relaciones, derecho efectivo al grupo, cuenta prevista del cliente y supuestos de licencia. **Entrega:** tres primeras comprobaciones, una escalada de roles que rechazas y un responsable por dependencia administrada por el cliente. Relaciona el diseño con los [fundamentos de cómputo](../../es/03-compute.md).

<a id="az-140-unit-2"></a>

## 2. Trazar identidad y transporte por separado

Compara unión a Entra, AD DS y Entra Domain Services según una app heredada y la autenticación del almacenamiento. Dibuja autenticación de la fuente, derecho, sesión y archivos como etapas distintas. Añade HTTPS saliente de conexión inversa y una ruta UDP Shortpath concreta. Explica alcance privado del listener y cómo ICE/STUN o TURN cambian requisitos.

**Caso:** en campus se conecta bien; desde casa aparecen otra petición de contraseña y lentitud. **Evidencia:** versión del cliente, unión, supuestos de SSO y acceso condicional, transporte, DNS y observaciones de latencia necesarias. **Entrega:** dos hipótesis independientes y pruebas que las confirmarían, sin publicar TCP 3389. Repasa los [fundamentos de red](../../es/05-networking.md).

<a id="az-140-unit-3"></a>

## 3. Proteger perfiles y publicar una app utilizable

Diseña contenedores FSLogix persistentes fuera de hosts compartidos reemplazables. Documenta compatibilidad de identidad/Kerberos, permisos de recurso compartido y NTFS, capacidad, picos de acceso, conexión única y objetivos de copia y restauración. Distingue preferencias del perfil de datos oficiales de apuntes. Compara imagen y paquete App Attach compatible, explicando por separado la publicación RemoteApp.

**Caso:** se llega al escritorio con perfil temporal y no arranca el editor. **Evidencia:** error de montaje, propietario de sesiones, permisos, imagen, acceso al paquete y asignaciones. **Entrega:** árbol de fallos con ramas separadas de perfil y aplicación, propuesta de recuperación segura y criterios para conservar trabajo existente del usuario.

<a id="az-140-unit-4"></a>

## 4. Publicar imágenes y calcular capacidad del aula

Redacta un plan versionado con sistema compatible, agentes, seguridad, apps, usuarios de validación, drenaje y vuelta atrás. Con un límite medido de doce sesiones por host, calcula capacidad para 48 estudiantes durante el fallo de uno. Distingue el método del plan de escalado de Start VM on Connect; incluye arranque, salud, sesiones máximas y almacenamiento.

**Caso:** llega un parche antes de clase y ya falta un host. **Evidencia:** tabla de capacidad con cinco hosts, versiones, lista de validación, sesiones y exclusiones de mantenimiento. **Entrega:** despliegue gradual que conserve capacidad suficiente, criterios de vuelta atrás y política explícita para quienes siguen conectados al reducir recursos.

<a id="az-140-unit-5"></a>

## 5. Simular fallos de acceso y recuperación

Sigue una conexión sintética con horas UTC, usuario seudonimizado, recurso, host y correlación. Especifica diagnósticos, métricas del host, logs FSLogix y observaciones de experiencia necesarios. Explica por qué un intento que nunca llega al servicio puede no dejar registro AVD. Añade identidad, DNS, paquetes, perfiles y API a un diseño de recuperación en otra región.

**Caso:** la clase de las 09:00 no recupera perfiles tras un fallo de almacenamiento. **Evidencia:** checkpoints previstos, sesión normal de comparación, objetivos del perfil, capacidad disponible y responsables de costes continuos de VM, discos, red, almacenamiento, monitorización y licencias. **Entrega:** cronología, hipótesis de primer fallo, criterios de recuperación y retorno, y separación clara entre predicción y observación.

Usa las seis referencias técnicas de la [guía](AZ-140.md) para cuestionar supuestos. Son ejercicios propios, sin cobertura exhaustiva de objetivos oficiales ni garantía de aprobar.
