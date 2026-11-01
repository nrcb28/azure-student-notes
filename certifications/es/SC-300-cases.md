# SC-300 · 10 casos con respuestas razonadas

[Guía](SC-300.md) · [Cuaderno](SC-300-workbook.md) · [Índice](README.md)

Preguntas originales sobre una aplicación universitaria ficticia de apuntes, no preguntas oficiales del examen. Explica el límite de acceso, rechaza un atajo inadecuado e identifica pruebas. Todos los resultados son hipotéticos; no se han realizado cambios en un inquilino real ni ejecuciones en la nube.

## 1. Un administrador de usuarios departamental no puede leer un contenedor privado de apuntes. ¿Ampliamos su rol de directorio?

<details>
<summary>Respuesta</summary>

Primero identifica si la acción fallida corresponde a administración del directorio, recursos Azure, datos de almacenamiento o permisos de aplicación. Un rol de directorio limitado mediante una unidad administrativa no concede todos los derechos sobre recursos del departamento. Ampliarlo resolvería el límite equivocado. En este diseño, relaciona identidad conectada, operación, ámbito y rol de datos o derecho de aplicación aplicable. Las pruebas deben explicar por qué se permite o deniega esa lectura sin convertir al administrador departamental en administrador de todo el inquilino.

</details>

## 2. Quitamos la asignación directa de un estudiante a la aplicación, pero conserva acceso. ¿Falla la retirada?

<details>
<summary>Respuesta</summary>

Una retirada no demuestra que desaparecieran todas las concesiones. Examina asignaciones mediante grupos, origen de la pertenencia, roles de aplicación, recursos compartidos por la aplicación e identidad e inquilino utilizados. Según el recurso, también importan herencia y sesiones existentes. No elimines la cuenta como primer diagnóstico. Crea un diagrama de vías de concesión y distingue el estado de asignación de la decisión observada en la aplicación. Una explicación útil identifica la vía restante, su propietario y las pruebas necesarias para confirmar su retirada.

</details>

## 3. Una universidad asociada informa de un MFA correcto. ¿Pueden todos sus profesores abrir soluciones inéditas?

<details>
<summary>Respuesta</summary>

No. Confiar en una notificación MFA compatible mediante configuración entrante entre inquilinos puede satisfacer un requisito de autenticación con ámbito; no concede acceso a todos los recursos universitarios. Examina las configuraciones aplicables de ambas organizaciones, la identidad del profesor en el inquilino de recursos, la aplicación y sus derechos. También importan restricciones de invitación y ciclo de vida. Registraría una asignatura permitida y una solución inédita denegada. Las pruebas deben distinguir la garantía de autenticación aceptada de la autorización independiente sobre un documento concreto.

</details>

## 4. Los nuevos editores no pueden registrar claves de paso. ¿Debe soporte recopilar contraseñas en una hoja de cálculo?

<details>
<summary>Respuesta</summary>

No. Diseña un proceso aprobado de registro inicial y recuperación con métodos compatibles, posiblemente un Pase de acceso temporal para usuarios elegibles. Comprueba ámbito de directiva, dispositivos, verificación de identidad, duración, uso y entrega segura. Un TAP es sensible y temporal; no debe aparecer en el cuaderno ni convertirse en credencial permanente compartida. El entregable describe registro y caducidad esperados, además del responsable de recuperación. Registrar una clave de paso exige después comprobar que se aplica la directiva prevista de intensidad de autenticación al acceder.

</details>

## 5. Una directiva de Acceso condicional de solo informe registra errores. ¿Ha protegido la aplicación bloqueando esas solicitudes?

<details>
<summary>Respuesta</summary>

La evaluación de solo informe no aplica los controles propuestos. Sus resultados ayudan a planificar, pero no prueban que esa directiva bloqueara solicitudes. Comprueba identidades y recursos destinatarios, condiciones, exclusiones, otras directivas y detalles del evento. Documenta por separado el resultado esperado con aplicación efectiva y el observado en solo informe. Antes de un despliegue autorizado en otro contexto, el diseño debe incluir piloto, recuperación, responsable de reversión y licencias. Aquí únicamente creamos ese plan y una matriz de accesos permitidos y denegados.

</details>

## 6. Aparece un inicio de sesión inusual y un antiguo profesor conserva acceso. ¿Basta una directiva de riesgo?

<details>
<summary>Respuesta</summary>

Son decisiones distintas. El riesgo de inicio de sesión se refiere a la solicitud; el riesgo de usuario, a un posible compromiso de la identidad. Investiga detecciones y contexto antes de considerar malicioso un inicio inusual. Determinar si el profesor aún necesita acceso corresponde al propietario del derecho y al proceso de baja o revisión. Una directiva de riesgo no decide esa necesidad. Mantén una cronología de investigación y otra decisión sobre acceso, con responsables y pruebas previstas. Retirar acceso obsoleto no resuelve por sí solo un posible compromiso.

</details>

## 7. El indexador nocturno solicita un permiso delegado. ¿Puede leer todos los apuntes sin un usuario?

<details>
<summary>Respuesta</summary>

Un permiso delegado depende del contexto de un usuario conectado y del modelo de permisos de la API. Una carga sin interacción necesita identidad de aplicación y permisos de aplicación compatibles, o permisos de recursos mediante identidad administrada. Solicitar permisos también es distinto de conceder consentimiento. Compara objeto de aplicación, entidad de servicio local, API, consentimientos y ámbito. No sustituyas esto por la contraseña de un profesor. El diseño debe explicar el conjunto mínimo de apuntes, la necesidad, quién aprueba el acceso y cómo se revisa.

</details>

## 8. La identidad federada de compilación recibe un token, pero falla el despliegue. ¿Creamos un secreto permanente?

<details>
<summary>Respuesta</summary>

Primero separa validación de la aserción externa, emisión del token de Entra y autorización del recurso. Comprueba emisor, sujeto y audiencia frente a las notificaciones esperadas, incluidas mayúsculas, sin registrar tokens reales. Después examina rol mínimo y ámbito de despliegue de la entidad resultante. Recibir un token no demuestra permiso para modificar el destino. Un secreto permanente añadiría mantenimiento sin explicar el fallo. Entrega una tabla hipotética de notificaciones y permisos con un contexto de compilación previsto, otro rechazado y pruebas necesarias en cada límite.

</details>

## 9. SSO con SAML funciona, pero permanece una cuenta invitada caducada en la plataforma. ¿SSO retira cuentas?

<details>
<summary>Respuesta</summary>

La federación SSO y el aprovisionamiento de cuentas cumplen funciones diferentes. SAML puede autenticar mientras un conector SCIM crea, actualiza o desactiva cuentas por separado. Revisa ámbito, correspondencias, cambios de origen, registros y comportamiento de retirada compatible con el destino. No deduzcas eliminación por la caducidad de un paquete o por un inicio correcto. El registro de gobernanza debe nombrar responsables y distinguir retirada del derecho Entra del estado de la cuenta destino. Un fallo de aprovisionamiento necesita seguimiento y pruebas observables de finalización.

</details>

## 10. Un administrador revisado es elegible en PIM y el panel no muestra fallos. ¿Está probado su acceso de mantenimiento?

<details>
<summary>Respuesta</summary>

Una revisión puede justificar conservar elegibilidad, pero activación y asignación activa siguen siendo independientes. Comprueba rol exacto, ámbito, requisitos, aprobación, duración y licencias. Un panel vacío también depende de cobertura, ingesta, retención, filtros y permisos; no demuestra mantenimiento correcto ni ausencia de fallos. Registra activación y operación permitida esperadas, junto con una denegación fuera de ámbito. Conserva decisión de revisión, pruebas de activación y análisis hipotético de registros como entregables distintos, sin afirmar que se ha ejecutado una operación.

</details>

[Guía oficial](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) · [Fuentes técnicas y explicaciones](SC-300.md)
