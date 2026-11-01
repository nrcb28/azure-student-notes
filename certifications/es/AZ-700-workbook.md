# AZ-700 · Cuaderno avanzado común

[Guía](AZ-700.md) · [10 casos](AZ-700-cases.md) · [Índice](README.md) · [Laboratorio de red](network-lab.md)

Cinco unidades con los mismos objetivos, escenarios y entregables en los ocho idiomas. Son ejercicios de diseño y diagnóstico. Una predicción no es una observación en Azure y no se atribuyen nuevos despliegues.

<a id="az-700-unit-1"></a>

## 1. Preparar un plan de direcciones y dependencias

Diseña redes de campus, hub, web y datos para la aplicación de apuntes. Haz inventario de rangos antes de elegir nuevos CIDR y reserva espacio para crecimiento y subredes específicas de cada servicio. Explica por qué un /24 ordinario tiene menos direcciones IPv4 asignables en Azure que su cantidad bruta. No asumas que un servicio delegado cabe en cualquier subred vacía.

**Caso:** un colaborador usa un rango solapado con el hub propuesto. **Evidencia:** tabla de propietario, prefijo, finalidad, condiciones y margen de crecimiento. **Entrega:** diseño corregido sin solapamiento, conflicto eliminado y una condición que todavía debas confirmar en la documentación actual del servicio.

<a id="az-700-unit-2"></a>

## 2. Trazar una petición y su respuesta

Dibuja una llamada de API desde la spoke web, pasando por un dispositivo de inspección, hasta otra red. Anota prefijo de destino, siguiente salto y opciones de reenvío en cada paso. Dibuja la respuesta por separado: la inspección con estado y la traducción pueden hacer fallar una ruta asimétrica que parezca razonable. El peering por sí solo no convierte un hub en router de tránsito.

**Caso:** tras cambiar una UDR, el origen envía peticiones sin recibir respuesta. **Evidencia:** rutas que compiten y siguiente salto efectivo en cada sentido. **Entrega:** una hipótesis comprobable, observación que la confirme y condición para deshacer el cambio propuesto.

<a id="az-700-unit-3"></a>

## 3. Diagnosticar el acceso privado por capas

Describe cómo un cliente del campus resuelve el nombre de Storage mediante el DNS y reenvío elegidos. Identifica subrecurso, dirección privada, aprobación del private endpoint y restricciones de red previstas. Separa resolución, alcance de red, TLS y permisos de datos: comprobar uno no demuestra los demás.

**Caso:** el acceso público está deshabilitado y el cliente sigue resolviendo una IP pública. **Evidencia:** nombre, recorrido del resolver, dirección obtenida y destino privado esperado. **Entrega:** propuesta para corregir DNS y comprobaciones posteriores de rutas y acceso autenticado a datos. Explica por qué no conviene fijar permanentemente una IP pública como solución.

<a id="az-700-unit-4"></a>

## 4. Elegir controles de entrega y protección

Compara un servicio TCP, una web regional y una web global. Elige candidatos según protocolo, alcance, rutas y comportamiento ante fallos, no por una etiqueta de producto memorizada. Incluye sondeos y certificados. Distingue selección DNS de proxy de peticiones, e inspección WAF de filtrado de red y protección de disponibilidad frente a DDoS.

**Caso:** el backend supera el probe, pero descarga documentos incorrectos. **Evidencia:** qué comprueba el sondeo y qué valida una operación real. **Entrega:** breve registro de decisión con una alternativa descartada y una señal funcional que detendría la promoción de una versión defectuosa.

<a id="az-700-unit-5"></a>

## 5. Diseñar y verificar la recuperación híbrida

Planifica conectividad principal y de respaldo del campus. Enumera fallos correlacionados, cambios de rutas, cifrado, capacidad y dependencias de la aplicación. La privacidad de ExpressRoute no demuestra cifrado predeterminado. Concreta el tramo que necesita protección y un diseño compatible; no supongas las mismas opciones para todos los tipos de circuito.

**Caso:** falla la conexión principal mientras muchos estudiantes descargan apuntes. **Evidencia:** ida y vuelta esperadas, supuestos de capacidad de respaldo y criterios medibles de recuperación. **Entrega:** plan de prueba aislada, vuelta a la normalidad y columnas esperado frente a observado. Sin entorno autorizado, entrega el diseño y marca las observaciones como no probadas.

[Guía oficial](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700) · [Explicaciones técnicas](AZ-700.md)
