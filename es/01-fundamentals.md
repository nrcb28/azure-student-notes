# Fundamentos de nube

La nube permite solicitar cómputo, almacenamiento y otros servicios mediante interfaces de software. Por debajo siguen existiendo servidores, redes y discos. Lo que cambia es quién los opera y cómo accedemos a ellos.

## Lo que conviene distinguir

- **Escalabilidad:** capacidad de aumentar o reducir recursos.
- **Elasticidad:** adaptación de los recursos a la demanda, normalmente automatizada.
- **Alta disponibilidad:** reducir interrupciones mediante redundancia y mecanismos de recuperación.
- **Recuperación ante desastres:** restaurar el servicio tras un incidente grave.
- **Escalado vertical:** más capacidad en una instancia.
- **Escalado horizontal:** más instancias.

Una aplicación con estado guardado solo en memoria puede fallar al repartir peticiones entre varias instancias. Antes de escalar, hay que mirar cómo gestiona sesiones, archivos y conexiones.

## IaaS, PaaS y SaaS

| Modelo | Qué administramos | Ejemplo |
|---|---|---|
| IaaS | Sistema operativo, aplicaciones, datos y configuración | Virtual Machines |
| PaaS | Aplicación, datos y configuración disponible | App Service |
| SaaS | Usuarios, datos y opciones del producto | Microsoft 365 |

Microsoft se encarga de la infraestructura física. El cliente sigue teniendo responsabilidades sobre sus datos, identidades y configuración, incluso en SaaS.

## Pública, privada e híbrida

La nube pública ofrece servicios de un proveedor. Una nube privada dedica infraestructura a una organización. Una solución híbrida integra infraestructura local o privada con nube pública.

**Caso de clase:** si el objetivo es publicar una API, PaaS puede ahorrarnos la instalación del servidor. Si la práctica exige configurar Linux, una VM tiene más sentido.

**Error frecuente:** pensar que nube significa barato. La flexibilidad ayuda, pero hay que medir el uso.

**Repaso:** ¿añadir más CPU es escalado horizontal? No, es vertical.

## Ejemplo resuelto: un pico no se arregla solo con instancias

Tenemos dos instancias de API y una base que solo admite un número limitado de conexiones. Duplicar la API podría aumentar la presión sobre esa base. Antes de escalar, mediría conexiones, duración de consultas, CPU y tiempos de espera.

Si la API guarda archivos en su disco local, otra instancia puede no encontrarlos. Para escalar horizontalmente, movería esos archivos a almacenamiento compartido adecuado y revisaría sesiones y trabajos en segundo plano.

La prueba debe comparar antes y después con una carga representativa. Si solo comprobamos que hay cuatro instancias, hemos verificado capacidad desplegada, no mejora para el usuario.

### Coste frente a control

Una VM puede parecer más barata por hora que una solución administrada. Añadiría al cálculo actualizaciones, copias, monitorización y tiempo de recuperación. La opción administrada puede ahorrar trabajo, pero también tener mínimos de capacidad o límites relevantes.

**Ejercicio:** cambia el requisito de una API estándar por una aplicación que instala controladores propios. Explica por qué tu elección de plataforma cambia aunque los usuarios sean los mismos.

---

[Índice](README.md) · [Otro idioma](../en/01-fundamentals.md) · [Siguiente](02-resources.md)
