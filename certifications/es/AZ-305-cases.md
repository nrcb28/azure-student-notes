# AZ-305 · 10 casos con respuestas razonadas

[Guía](AZ-305.md) · [Índice](README.md)

Preguntas originales para estudiar. No son preguntas oficiales ni filtradas. Antes de abrir la respuesta, identifica el requisito, descarta una alternativa y explica cómo comprobarías tu decisión.

## 1. Una solución exige RPO cero y RTO de una hora. ¿Son incompatibles?

<details>
<summary>Razonamiento</summary>

No por definición: pérdida de datos y tiempo de recuperación son distintos. Hay que validar una solución concreta que satisfaga ambos bajo fallos definidos.

</details>

## 2. La aplicación usa JSON y transacciones complejas. ¿Qué dato decide la base?

<details>
<summary>Razonamiento</summary>

Consultas, relaciones, transacciones y distribución. JSON de transporte no obliga a elegir una base documental.

</details>

## 3. El equipo pide AKS para una API simple y tiene poca experiencia. ¿Qué discutir?

<details>
<summary>Razonamiento</summary>

Necesidad de Kubernetes, operación, alternativas y coste total. No descartarlo por principio, pero exigir una razón proporcional a su complejidad.

</details>

## 4. Una copia regional funciona, pero no se permiten datos fuera del país. ¿Qué falta?

<details>
<summary>Razonamiento</summary>

Verificar ubicación de réplicas, copias, logs y dependencias. Resiliencia no autoriza incumplir residencia.

</details>

## 5. El sistema secundario no tiene secretos ni DNS preparados. ¿Basta replicar VM?

<details>
<summary>Razonamiento</summary>

No. La recuperación incluye identidad, configuración, red, nombres y dependencias. Medir el recorrido completo.

</details>

## 6. Se quiere acelerar lectura con caché. ¿Qué nuevo problema aparece?

<details>
<summary>Razonamiento</summary>

Coherencia, expiración e invalidación. Determinar tolerancia a datos antiguos y comportamiento ante caída o vaciado del caché.

</details>

## 7. Se migra una base en una noche, pero hay escrituras continuas. ¿Qué definir?

<details>
<summary>Razonamiento</summary>

Transferencia inicial, captura o sincronización de cambios compatible, ventana de corte, validación y rollback. Copiar una vez no basta.

</details>

## 8. Un informe histórico ralentiza matrículas. ¿Qué alternativa investigar?

<details>
<summary>Razonamiento</summary>

Separar analítica de transacciones, revisar consultas e integración. No escalar todo sin conocer el patrón.

</details>

## 9. ¿Qué falta en una arquitectura que solo muestra servicios?

<details>
<summary>Razonamiento</summary>

Requisitos, límites, identidad, datos, fallos, operación, costes y validación. El dibujo comunica estructura, no prueba adecuación.

</details>

## 10. El presupuesto baja, pero fiabilidad no cambia. ¿Qué responder?

<details>
<summary>Razonamiento</summary>

Comparar alternativas y costes con evidencia; explicar tensiones y negociar si no hay solución validada. No prometer los mismos objetivos automáticamente.

</details>

## Autoevaluación

Por caso: 1 punto por identificar el requisito, 1 por justificar la elección y 1 por proponer una comprobación. Máximo 30. Esta escala es propia para orientar el repaso; no predice la puntuación del examen. Si fallas, vuelve al bloque concreto y redacta un ejemplo distinto.
