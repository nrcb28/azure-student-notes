# AZ-400 · 10 casos con respuestas razonadas

[Guía](AZ-400.md) · [Índice](README.md)

Preguntas originales para estudiar. No son preguntas oficiales ni filtradas. Antes de abrir la respuesta, identifica el requisito, descarta una alternativa y explica cómo comprobarías tu decisión.

## 1. El artefacto de producción se recompila después de pruebas. ¿Qué riesgo hay?

<details>
<summary>Razonamiento</summary>

Diferencias de dependencias, herramientas o entradas. Promover el artefacto probado y versionado reduce esa distancia.

</details>

## 2. Una migración borra una columna y falla el despliegue. ¿Basta rollback de imagen?

<details>
<summary>Razonamiento</summary>

No. El esquema y los datos pueden haber cambiado. Preparar compatibilidad, secuencia de migración y recuperación.

</details>

## 3. Un secreto estuvo en Git durante minutos. ¿Primer paso?

<details>
<summary>Razonamiento</summary>

Revocar o rotar y analizar exposición. Borrar el commit no invalida copias del secreto.

</details>

## 4. Un PR externo necesita ejecutar scripts en runner con acceso interno. ¿Qué revisar?

<details>
<summary>Razonamiento</summary>

Confianza, aislamiento, permisos, persistencia y eventos. El contenido del PR puede ejecutar código; no exponer acceso privilegiado sin diseño seguro.

</details>

## 5. El canary tiene CPU normal, pero resultados incorrectos. ¿Qué faltó?

<details>
<summary>Razonamiento</summary>

Señales funcionales y criterios de promoción. La salud de infraestructura no prueba corrección de negocio.

</details>

## 6. Una prueba pasa al quinto intento. ¿Qué hacemos?

<details>
<summary>Razonamiento</summary>

Investigar la intermitencia y preservar evidencia. Repetir hasta verde no convierte el sistema en fiable.

</details>

## 7. Hay id-token: write, pero Azure rechaza el login. ¿Qué verificar?

<details>
<summary>Razonamiento</summary>

Emisor, sujeto, audiencia, confianza federada e identidad configurada. Después revisar autorización. El permiso del workflow no crea toda la confianza.

</details>

## 8. El equipo entrega más, pero tarda más en recuperar. ¿Es mejora clara?

<details>
<summary>Razonamiento</summary>

No necesariamente. Evaluar velocidad y estabilidad juntas, con definiciones consistentes y sin premiar una sola métrica.

</details>

## 9. Un caché antiguo rompe compilaciones. ¿Qué revisar?

<details>
<summary>Razonamiento</summary>

Clave, entradas, versión de herramientas y alcance. Un caché acelera; no debería sustituir una fuente correcta ni un artefacto publicado.

</details>

## 10. Un postmortem termina en tener más cuidado. ¿Qué falta?

<details>
<summary>Razonamiento</summary>

Acción concreta, responsable, plazo y forma de verificarla. La conclusión debe cambiar el sistema o proceso de manera comprobable.

</details>

## Autoevaluación

Por caso: 1 punto por identificar el requisito, 1 por justificar la elección y 1 por proponer una comprobación. Máximo 30. Esta escala es propia para orientar el repaso; no predice la puntuación del examen. Si fallas, vuelve al bloque concreto y redacta un ejemplo distinto.
