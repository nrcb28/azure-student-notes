# Identidad y seguridad

La seguridad empieza por saber quién accede, a qué y con qué permisos. Cifrar datos es importante, pero no evita que una identidad autorizada los utilice indebidamente.

## Identidades

Microsoft Entra ID, antes Azure AD, es un servicio de identidad. No es lo mismo que Active Directory Domain Services: no hay que dar por hecho que ofrece los mismos protocolos y funciones de un dominio tradicional.

- **Autenticación:** demostrar quién eres.
- **Autorización:** determinar qué puedes hacer.
- **MFA:** utilizar factores adicionales para autenticar.
- **Acceso condicional:** aplicar decisiones basadas en señales y condiciones, según licencias y configuración.
- **Identidad administrada:** identidad de una carga de trabajo gestionada por Azure.

## Azure RBAC

Una asignación combina identidad, rol y ámbito. Los permisos suelen heredarse desde ámbitos superiores.

| Rol | Idea principal |
|---|---|
| Reader | Consultar recursos |
| Contributor | Administrar recursos sin conceder asignaciones de roles RBAC |
| Owner | Administrar recursos y conceder acceso |
| Storage Blob Data Reader | Leer datos de blobs según el ámbito |

Administración y acceso a datos son planos distintos. Un permiso para modificar una cuenta de almacenamiento no equivale a permiso para leer todos sus objetos.

## Secretos

Key Vault almacena secretos, claves y certificados. La aplicación necesita autorización para usarlos. Si podemos acceder mediante identidad administrada, evitamos guardar una contraseña de servicio en configuración.

Una identidad **asignada por el sistema** está ligada al ciclo de vida del recurso. Una **asignada por el usuario** existe de forma independiente y puede asociarse a varios recursos.

## Aplicación de apuntes

La API recibe una identidad administrada con permiso de datos limitado al contenedor necesario. Los estudiantes se autentican, pero la aplicación también comprueba qué documentos puede modificar cada usuario.

**Error frecuente:** comprobar solo que el usuario ha iniciado sesión. También hay que comprobar que puede acceder al objeto solicitado.

**Repaso:** autenticarse correctamente no concede permisos de administración.

---

[Índice](README.md) · [Otro idioma](../en/06-identity.md) · [Anterior](05-networking.md) · [Siguiente](07-governance.md)
