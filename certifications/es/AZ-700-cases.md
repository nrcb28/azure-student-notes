# AZ-700 · 10 casos con respuestas razonadas

[Guía](AZ-700.md) · [Cuaderno](AZ-700-workbook.md) · [Índice](README.md)

Escenarios propios para aprender, no preguntas oficiales ni filtradas. Identifica el requisito, descarta una alternativa y concreta la evidencia antes de abrir la respuesta. No se afirma haberlos ejecutado en Azure.

## 1. El campus y una VNet nueva usan 10.70.0.0/16. ¿Un peering ordinario o una VPN hacen que las direcciones dejen de ser ambiguas?

<details>
<summary>Razonamiento</summary>

El solapamiento es un problema de diseño, no una regla allow que falta. Haz inventario de las redes reales y elige espacio sin solapamiento antes de montar peering o conectividad híbrida estándar. Existen diseños de traducción compatibles con determinados escenarios, pero añaden condiciones y hay que plantearlos expresamente. La dirección de un paquete que apunta al mismo rango privado no indica por sí sola a qué ubicación se refiere. La evidencia sería un inventario, un plan corregido y rutas previstas para cada destino.

</details>

## 2. A está emparejada con B y B con C, pero A no llega a C. ¿Deberías dar Owner a la VM de origen?

<details>
<summary>Razonamiento</summary>

No. El peering no es automáticamente transitivo y un rol de administración de Azure no crea un camino de red ausente. Decide si necesitas conexión directa o un diseño de tránsito compatible. Revisa rutas, reenvío y seguridad en ambos sentidos. Si interviene un gateway compartido, comprueba sus opciones concretas de tránsito, sin asumir que reenvía cualquier tráfico entre spokes. La evidencia útil es el recorrido completo del paquete y sus siguientes saltos efectivos, no un rol de administración más amplio.

</details>

## 3. Una ruta predeterminada nueva apunta al firewall, pero el tráfico de un prefijo más específico sale por otro lugar. ¿Están rotas todas las rutas de usuario?

<details>
<summary>Razonamiento</summary>

No necesariamente. Revisa todas las rutas aplicables y el destino real. No supongas que una ruta predeterminada amplia sustituye cualquier otra más específica. Compara prefijos, origen y siguiente salto efectivo según las reglas de selección de Azure. Confirma también que la tabla prevista esté asociada a la subred de origen. La evidencia debe mostrar prefijos que compiten y siguiente salto observado. Cambiar reglas de seguridad no demuestra qué ruta se ha seleccionado.

</details>

## 4. Las peticiones atraviesan un dispositivo con estado, pero las respuestas vuelven por otro camino. ¿Por qué puede fallar una conexión permitida?

<details>
<summary>Razonamiento</summary>

Un dispositivo con estado puede necesitar ver ambos lados de la conexión. Con rutas asimétricas, la respuesta puede evitar el dispositivo que registró el flujo o llegar a otro que no tenga ese estado. Revisa ida, vuelta, reenvío del dispositivo y traducciones de direcciones. No añadas excepciones de entrada al azar antes de contrastar esa hipótesis. Una entrega útil sería un diagrama con ambos caminos y observaciones de los extremos o de herramientas de diagnóstico compatibles.

</details>

## 5. Se desactiva el acceso público a Storage. La API dispone de private endpoint, pero sigue resolviendo la IP pública. ¿Qué revisarías primero?

<details>
<summary>Razonamiento</summary>

Investiga el camino DNS del cliente real: servidores configurados, zona privada, enlace a VNet y reenvío híbrido si existe. Conserva el nombre del servicio y haz que se resuelva de forma adecuada para la conexión privada prevista. Asignar Storage Blob Data Reader no corrige una respuesta DNS pública. Cuando funcionen resolución y rutas, verifica por separado la autorización de datos. Registra nombre, dirección, resolver utilizado, subrecurso del endpoint y una operación autenticada posterior como evidencias distintas.

</details>

## 6. El requisito exige cifrar los datos entre campus y Azure. ¿Contratar ExpressRoute demuestra por sí solo ese cifrado?

<details>
<summary>Razonamiento</summary>

No. La conectividad privada de ExpressRoute y el cifrado son propiedades distintas; su tráfico no se cifra de forma predeterminada. Concreta qué hay que proteger y dónde comienza y termina esa protección. MACsec es una opción compatible para enlaces ExpressRoute Direct y no está disponible automáticamente en cualquier circuito de proveedor. Un diseño IPsec adecuado puede responder a una necesidad de extremo a extremo. Compara compatibilidad y rendimiento, y documenta la gestión de claves. Un dibujo privado no prueba cifrado.

</details>

## 7. El equipo quiere selección regional mediante DNS y espera que cada petición pase por Traffic Manager. ¿Qué habría que corregir?

<details>
<summary>Razonamiento</summary>

Traffic Manager selecciona endpoints mediante DNS y no actúa como proxy de las peticiones. El cliente se conecta al destino elegido; las cachés pueden retrasar el efecto de un cambio DNS. Si el diseño necesita un proxy global para entregar HTTP, evalúa Azure Front Door frente a los requisitos. Para rutas HTTP regionales, evalúa Application Gateway. Dibuja la consulta DNS separada de la conexión de aplicación y explica cómo influye la información de salud en la selección.

</details>

## 8. Se habilita un service endpoint en una subred. ¿Por qué eso no demuestra que Storage tenga allí una dirección de private endpoint?

<details>
<summary>Razonamiento</summary>

Un service endpoint y un private endpoint son diseños distintos. Habilitar el primero no crea una interfaz de red privada para la cuenta de Storage dentro de esa subred. Comprueba configuración real del service endpoint, reglas de red del servicio y método de autenticación. Si el requisito pide una dirección privada de destino, evalúa un private endpoint compatible, con su DNS y acceso. Registra destino resuelto y configuración del recurso, sin tomar la palabra compartida «endpoint» como prueba de equivalencia.

</details>

## 9. Una regla deny nueva bloquea conexiones nuevas, pero una sesión establecida continúa. ¿Demuestra que el NSG ignora sus reglas?

<details>
<summary>Razonamiento</summary>

No. Los NSG son filtros con estado, así que un cambio puede no interrumpir un flujo existente de inmediato. Diferencia una conexión realmente nueva de una sesión reutilizada y revisa las reglas efectivas de subred e interfaz. Comprueba origen, destino, puerto, protocolo y prioridad en lugar de confiar en el nombre de la regla. La observación debe indicar si la prueba creó un flujo nuevo. Asignar roles más amplios o eliminar la VM no explicaría ese comportamiento.

</details>

## 10. Un dibujo incluye ExpressRoute y una VPN de respaldo. ¿Qué falta antes de afirmar que la aplicación tiene conectividad resiliente?

<details>
<summary>Razonamiento</summary>

Identifica fallos compartidos y valida el camino completo de respaldo. Revisa equipos del cliente, proveedores, ubicaciones de peering, gateways, anuncios, rutas de vuelta, capacidad del túnel, DNS y reconexión de la aplicación. Una segunda línea no demuestra que se seleccione correctamente al producirse un fallo. Propón una prueba aislada y autorizada, con resultados esperados y observados, criterios de recuperación y vuelta a la normalidad. Estos apuntes aportan el ejercicio de diseño; no afirman que se haya ejecutado ese failover.

</details>

La [guía](AZ-700.md) enlaza las fuentes técnicas y la referencia de examen consultada. Sigue con el [cuaderno](AZ-700-workbook.md) para convertir las respuestas en diagramas y evidencias.
