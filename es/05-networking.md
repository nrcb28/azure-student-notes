# Redes y conectividad

Una red que deja pasar tráfico no es necesariamente una red bien configurada. Hay que saber qué ruta toma la conexión, cómo se resuelve el nombre y qué reglas la permiten.

## Piezas básicas

- **VNet:** red virtual privada.
- **Subred:** parte del espacio de direcciones de una VNet.
- **NSG:** reglas de filtrado con estado para subredes o interfaces.
- **Tabla de rutas:** determina el siguiente salto de determinados destinos.
- **Peering:** conecta redes virtuales; no es transitivo automáticamente.
- **DNS:** convierte nombres en direcciones.

Si A tiene peering con B y B con C, A no tiene necesariamente conectividad con C. Tampoco conviene usar rangos de direcciones solapados si vamos a conectar redes.

## Conectar con otros entornos

VPN Gateway permite conexiones cifradas a través de Internet. ExpressRoute ofrece conectividad privada mediante un proveedor, pero no implica cifrado de extremo a extremo por sí sola.

Un **Private Endpoint** proporciona una interfaz con dirección privada para acceder a un servicio compatible. Hay que revisar DNS y acceso público. Un **service endpoint** es otro mecanismo: no introduce una IP privada equivalente para el servicio.

## Repartir tráfico

| Servicio | Criterio |
|---|---|
| Load Balancer | TCP/UDP, capa 4 |
| Application Gateway | HTTP/HTTPS, capa 7, opciones de WAF |
| Front Door | Entrada global para aplicaciones web |
| Traffic Manager | Selección de destino mediante DNS |

Traffic Manager no transporta el tráfico de la aplicación como un proxy. Las cachés DNS influyen en el cambio de destino.

## Diagnóstico de clase

Si la API no llega a la base de datos:

1. Comprobar el nombre y su resolución DNS.
2. Revisar la ruta y la conectividad al puerto.
3. Revisar NSG, firewall y acceso público o privado.
4. Comprobar autenticación y permisos.
5. Leer errores y métricas antes de cambiar reglas.

**Error frecuente:** abrir todos los puertos para que funcione y olvidarse de cerrarlos.

## Ejemplo resuelto: privado en el dibujo, público en la conexión

Se crea un private endpoint, pero el portátil sigue resolviendo el nombre a una dirección pública. La aplicación puede continuar entrando por la ruta pública si sigue habilitada, o fallar si se deshabilita sin preparar la resolución privada.

El diagnóstico empieza por consultar qué dirección obtiene el cliente y si dispone de una ruta hacia ella. Después se revisa el acceso del servicio. No cambiaría el código para usar una IP fija sin estudiar nombres y certificados.

## NSG y aplicación

Un NSG permite un puerto; no demuestra que haya un proceso escuchando. Un firewall del sistema operativo o una configuración de la aplicación también puede bloquear.

Con NSG en subred e interfaz, revisar reglas efectivas. Un número de prioridad menor se evalúa antes, y los filtros son con estado.

**Ejercicio:** dibujar ida y vuelta entre una VM local, VPN, VNet y un servicio privado. Marca DNS, rutas, filtros y autenticación como comprobaciones diferentes.

---

[Índice](README.md) · [Otro idioma](../en/05-networking.md) · [Anterior](04-storage.md) · [Siguiente](06-identity.md)
