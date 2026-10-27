# Identity and security

Security starts with knowing who accesses what and with which permissions. Encryption matters, but it does not prevent an authorised identity from misusing data.

## Identities

Microsoft Entra ID, formerly Azure AD, is an identity service. It is not the same as Active Directory Domain Services: do not assume it provides the same protocols and functions as a traditional domain.

- **Authentication:** proving who you are.
- **Authorisation:** deciding what you can do.
- **MFA:** using additional authentication factors.
- **Conditional Access:** making access decisions using signals and conditions, subject to licensing and configuration.
- **Managed identity:** an Azure-managed workload identity.

## Azure RBAC

An assignment combines an identity, a role, and a scope. Permissions generally inherit from higher scopes.

| Role | Main idea |
|---|---|
| Reader | View resources |
| Contributor | Manage resources without granting RBAC role assignments |
| Owner | Manage resources and grant access |
| Storage Blob Data Reader | Read blob data within the assigned scope |

Management and data access are different planes. Permission to modify a storage account does not equal permission to read every object.

## Secrets

Key Vault stores secrets, keys, and certificates. Applications need authorisation to use them. Managed identity can avoid keeping service passwords in configuration.

A **system-assigned identity** shares its resource's lifecycle. A **user-assigned identity** exists independently and can be attached to several resources.

## Notes application

The API gets a managed identity with data permissions limited to the required container. Students authenticate, but the application also checks which documents each user can modify.

**Common mistake:** checking only that a user is signed in. The application must also check access to the requested object.

**Review:** successful authentication does not grant administrative permissions.

---

[Contents](README.md) · [Other language](../es/06-identity.md) · [Previous](05-networking.md) · [Next](07-governance.md)
