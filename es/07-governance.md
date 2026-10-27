# Gobierno y cumplimiento

Gobernar un entorno consiste en establecer reglas y comprobar que se cumplen. En un proyecto pequeño evita despistes; en una organización permite trabajar a muchos equipos sin depender de configuraciones manuales.

## RBAC frente a Policy

- **RBAC:** quién puede ejecutar una acción.
- **Azure Policy:** qué condiciones deben cumplir los recursos.

Una persona puede tener permiso para crear una VM y que una política impida crearla en una región no permitida.

Las definiciones de Policy expresan reglas. Una iniciativa agrupa definiciones relacionadas. Las asignaciones determinan el ámbito donde se aplican.

## Efectos

- **Audit:** informa de incumplimientos.
- **Deny:** bloquea determinadas solicitudes que incumplen la regla.
- **Modify:** puede modificar propiedades compatibles.
- **DeployIfNotExists:** puede desplegar recursos relacionados cuando faltan.

Los efectos de modificación o despliegue requieren configuración y permisos adecuados. Para recursos existentes puede ser necesaria una tarea de remediación; asignar una política no significa corregirlo todo de inmediato.

## Organización práctica

Usaría nombres predecibles y etiquetas como:

| Etiqueta | Ejemplo |
|---|---|
| project | notes-app |
| environment | dev |
| owner | student-team |
| costCenter | training |

Las etiquetas no se heredan automáticamente en todos los casos. No guardaría secretos ni datos personales en ellas.

## Seguridad y cumplimiento

Microsoft Defender for Cloud ayuda con postura de seguridad y protección de cargas, según configuración y planes. Microsoft Sentinel se centra en capacidades SIEM y SOAR. No son herramientas intercambiables.

Que Azure disponga de una certificación no convierte automáticamente nuestra aplicación en conforme. También cuentan el tratamiento de datos, los permisos, los procesos y las obligaciones aplicables.

**Caso de clase:** empezar con políticas de auditoría para entender el impacto antes de imponer denegaciones amplias.

**Repaso:** una regla que limita regiones pertenece a Policy, no a una etiqueta.

## Ejemplo resuelto: pasar de auditoría a cumplimiento

Una universidad descubre recursos en regiones no aprobadas. Asignar una denegación puede impedir nuevos cambios incompatibles, pero no mueve automáticamente todos los recursos existentes.

Primero identificaría recursos, responsables y excepciones justificadas. Después planificaría cambios y verificaría efectos. Una exención debe tener motivo y revisión; no convertirla en un bypass permanente.

## Responsabilidad operativa

Cada recomendación debería terminar en una decisión: corregir, aceptar temporalmente o investigar. Registrar un hallazgo sin responsable no cambia el riesgo.

Conviene distinguir evidencia técnica de cumplimiento formal. Una política puede comprobar una propiedad del recurso, pero no demuestra por sí sola que todos los procesos y datos cumplen obligaciones aplicables.

**Ejercicio:** escribe una regla para exigir environment y otra para limitar regiones. Explica ámbito, efecto, recursos existentes y excepción. Después indica qué harías si la regla bloquea un servicio que solo está disponible en otra región.

---

[Índice](README.md) · [Otro idioma](../en/07-governance.md) · [Anterior](06-identity.md) · [Siguiente](08-observability.md)
