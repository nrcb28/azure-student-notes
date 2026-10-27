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

## Worked example: access seems impossible to remove

We remove Reader directly from a resource, but the user still sees it. Group membership or another inherited assignment may provide access.

Inspect account, tenant, direct assignments, groups, and inherited permissions. Consider propagation and existing sessions. Removing one assignment does not remove all access.

## Directory roles and Azure roles

Managing Entra users and administering VMs use different authorisation mechanisms and scopes. Do not grant broad directory permissions to solve blob access.

Workload identities need review too. Managed identity removes a stored credential under our management, but excessive permissions remain excessive.

**Exercise:** define access for a student reading personal documents and a thumbnail worker. Explain application checks and each component's Azure permissions.

---

[Contents](README.md) · [Other language](../es/06-identity.md) · [Previous](05-networking.md) · [Next](07-governance.md)

## Microsoft Learn expansion · sas

A Blob user delegation SAS is signed using a delegation key obtained through Entra ID. Issuing one requires permission to obtain that key; possessing a blob URL does not grant that permission. Design the signature and access constraints together.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli) · [Microsoft Learn expansion](15-microsoft-learn.md#learn-sas)

## Evidence-based RBAC diagnosis

Resource administration does not imply role-assignment authority or data access. Creating assignments needs the corresponding action at the correct scope, and conditions can restrict permitted roles or principals.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting) · [Evidence-based RBAC diagnosis](15-microsoft-learn.md#learn-rbac-diagnosis)

## Recovering Key Vault does not restore every integration

Soft delete supports recovery of vaults and supported objects during retention. Recovering a deleted vault does not automatically restore certain integrations such as RBAC assignments and Event Grid subscriptions; review and recreate them where needed.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview) · [Recovering Key Vault does not restore every integration](15-microsoft-learn.md#learn-vault-recovery)
