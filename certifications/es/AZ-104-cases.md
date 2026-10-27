# AZ-104 · 10 casos con respuestas razonadas

[Guía](AZ-104.md) · [Índice](README.md)

Preguntas originales para estudiar. No son preguntas oficiales ni filtradas. Antes de abrir la respuesta, identifica el requisito, descarta una alternativa y explica cómo comprobarías tu decisión.

## 1. Quitas Reader de un recurso y el usuario conserva lectura. ¿Qué investigar?

<details>
<summary>Razonamiento</summary>

Asignaciones heredadas, grupos, identidad utilizada y propagación. No conceder otro rol para intentar quitar acceso.

</details>

## 2. Un administrador crea Storage pero recibe 403 al listar blobs. ¿Qué mirar?

<details>
<summary>Razonamiento</summary>

Método de autenticación, rol de datos, ámbito y controles del servicio. Contributor de administración no garantiza acceso a los datos.

</details>

## 3. Una web integrada con VNet sigue siendo accesible públicamente. ¿Es contradictorio?

<details>
<summary>Razonamiento</summary>

No. La integración de App Service es para tráfico saliente. Revisar entrada, endpoint privado y restricciones por separado.

</details>

## 4. Un balanceador muestra todos los backends unhealthy. ¿Qué comprobar?

<details>
<summary>Razonamiento</summary>

Puerto y respuesta del sondeo, proceso escuchando, reglas y destino configurado. Un backend existente no es necesariamente saludable.

</details>

## 5. A conecta por peering con B y B con C. A no llega a C. ¿Qué falta entender?

<details>
<summary>Razonamiento</summary>

El peering no es transitivo automáticamente. Diseñar conexión o tránsito compatible, rutas y seguridad, sin agregar permisos aleatorios.

</details>

## 6. Bicep compila y Azure deniega el despliegue. ¿Qué revisar?

<details>
<summary>Razonamiento</summary>

Políticas, permisos, cuotas, nombres, parámetros y disponibilidad. La compilación local no verifica todos esos controles remotos.

</details>

## 7. Un backup termina correctamente. ¿Podemos asegurar RTO de 30 minutos?

<details>
<summary>Razonamiento</summary>

No sin medir restauración y dependencias. Hay que recuperar servicio, no solo demostrar que existe una copia.

</details>

## 8. DNS devuelve IP pública después de crear endpoint privado. ¿Qué revisar?

<details>
<summary>Razonamiento</summary>

Zona privada, enlaces, reenvío y resolución del cliente. Crear el endpoint no configura automáticamente cada consumidor.

</details>

## 9. Una VM apagada sigue generando gasto. ¿Qué distinguir?

<details>
<summary>Razonamiento</summary>

Estado detenido frente a desasignado y costes de discos y recursos asociados. Verificar estado y componentes antes de dar por terminada la práctica.

</details>

## 10. Una política corrige recursos nuevos pero no antiguos. ¿Por qué puede pasar?

<details>
<summary>Razonamiento</summary>

Efecto, alcance, evaluación y remediación de existentes. No toda política modifica ni remedia automáticamente cada recurso.

</details>

## Autoevaluación

Por caso: 1 punto por identificar el requisito, 1 por justificar la elección y 1 por proponer una comprobación. Máximo 30. Esta escala es propia para orientar el repaso; no predice la puntuación del examen. Si fallas, vuelve al bloque concreto y redacta un ejemplo distinto.
