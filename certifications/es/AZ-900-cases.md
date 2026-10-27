# AZ-900 · 10 casos con respuestas razonadas

[Guía](AZ-900.md) · [Índice](README.md)

Preguntas originales para estudiar. No son preguntas oficiales ni filtradas. Antes de abrir la respuesta, identifica el requisito, descarta una alternativa y explica cómo comprobarías tu decisión.

## 1. Una API solo debe ejecutar código cuando llega un archivo. ¿Qué estudiarías primero?

<details>
<summary>Razonamiento</summary>

Funciones o ejecución por eventos, revisando duración, arranque, conectividad y plan. Una VM permanente no es obligatoria; tampoco se puede prometer coste cero.

</details>

## 2. La empresa quiere configurar su propio SO. ¿Qué modelo encaja?

<details>
<summary>Razonamiento</summary>

IaaS suele ofrecer ese control. PaaS delega más plataforma y puede no permitir la configuración requerida. Identifica el nivel de control, no una marca.

</details>

## 3. Se añaden tres instancias y los usuarios pierden sesión. ¿Qué revisar?

<details>
<summary>Razonamiento</summary>

Estado local de las sesiones y reparto de tráfico. El escalado horizontal necesita que el diseño soporte varias instancias, no solo crearlas.

</details>

## 4. Una URL de Storage es pública. ¿Puede cualquiera leer?

<details>
<summary>Razonamiento</summary>

No necesariamente. Red pública y acceso anónimo son distintos; revisar autenticación, autorización y configuración del servicio.

</details>

## 5. ¿Qué elegir para asignar gasto a un proyecto?

<details>
<summary>Razonamiento</summary>

Etiquetas y análisis de costes cuando los recursos y datos lo permitan. No confundir clasificación de gasto con permisos o límite automático de consumo.

</details>

## 6. Un usuario autenticado borra documentos de otro. ¿Falló necesariamente MFA?

<details>
<summary>Razonamiento</summary>

No. Es un problema de autorización de la operación y el objeto. MFA no decide qué documentos puede modificar.

</details>

## 7. ¿Qué servicio centraliza recomendaciones y cuál señales de operación?

<details>
<summary>Razonamiento</summary>

Advisor aporta recomendaciones; Monitor reúne capacidades de observación. Una recomendación no sustituye la evidencia del funcionamiento real.

</details>

## 8. La organización tiene Internet lento y debe trasladar gran volumen. ¿Qué comparar?

<details>
<summary>Razonamiento</summary>

Transferencias por red y opciones de dispositivos como Data Box, según compatibilidad y disponibilidad. Considerar volumen, plazo, seguridad y validación.

</details>

## 9. ¿Pueden existir controles de cumplimiento y aun así una app insegura?

<details>
<summary>Razonamiento</summary>

Sí. Comprobar propiedades no demuestra seguridad de toda la aplicación. Revisar permisos, lógica, datos y procesos además de políticas.

</details>

## 10. ¿Cómo demostrarías que has entendido el modelo compartido?

<details>
<summary>Razonamiento</summary>

Enumerando responsabilidades del proveedor y propias para una carga concreta, y explicando qué cambia entre VM, PaaS y SaaS.

</details>

## Autoevaluación

Por caso: 1 punto por identificar el requisito, 1 por justificar la elección y 1 por proponer una comprobación. Máximo 30. Esta escala es propia para orientar el repaso; no predice la puntuación del examen. Si fallas, vuelve al bloque concreto y redacta un ejemplo distinto.
