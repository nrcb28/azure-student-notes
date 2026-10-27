# Storage and data

I would first consider how data will be read and written, then choose a product.

| Requirement | Option to investigate |
|---|---|
| PDFs, images, and objects | Blob Storage |
| Shared files | Azure Files |
| A VM disk | Managed Disks |
| Relationships, constraints, and SQL transactions | Azure SQL Database or managed PostgreSQL |
| Distributed models suited to its APIs | Azure Cosmos DB |

## Blob Storage

Blobs are organised into containers inside a storage account. A blob container is unrelated to a Docker container.

Access tiers trade storage costs against access costs. Archived data can require rehydration before reading; I would not choose Archive for documents users expect to open immediately.

## Redundancy

- **LRS:** several copies within a physical location in the primary region.
- **ZRS:** copies across zones in the primary region.
- **GRS:** geographical replication to a secondary region.
- **GZRS:** combines zone redundancy in the primary region with geographical replication.

Geographical replication is asynchronous: recent writes can be lost during a failure. Read access to the secondary depends on the selected option and service state.

## Databases

A managed database does not fix missing indexes, expensive queries, or poorly managed connections. I would measure queries and latency before increasing capacity.

For our app, PDFs would go in Blob Storage. The database would hold the title, course, author, and object reference. File storage and metadata queries serve different purposes.

## Protection

Prefer identities and suitable data permissions. If using SAS tokens, restrict permissions and lifetime and treat them as credentials. Add soft delete, versioning, or backups where supported and justified by requirements.

**Review:** redundancy and backups address different risks. A deletion can propagate between replicas.

## Worked example: deleting notes

A user deletes a document accidentally. Replicas may reflect that deletion. Recovery needs a feature or copy retaining an earlier state, sufficient retention, and a known procedure.

Recovering only the PDF may leave metadata missing. Maintain consistency between the object and database using stable identifiers and reconciliation.

## Performance and security

Larger database capacity does not always fix an unindexed query. Inspect rows read, plans, duration, and concurrency. For objects, examine operations and read patterns before changing tiers.

A SAS URL can grant access to whoever holds it. Limit permissions, lifetime, and distribution.

**Exercise:** recover a document deleted ten days ago. State the prior configuration, metadata recovery, and permission checks required.

---

[Contents](README.md) · [Other language](../es/04-storage.md) · [Previous](03-compute.md) · [Next](05-networking.md)

## Microsoft Learn expansion · sas

A Blob user delegation SAS is signed using a delegation key obtained through Entra ID. Issuing one requires permission to obtain that key; possessing a blob URL does not grant that permission. Design the signature and access constraints together.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli) · [Microsoft Learn expansion](15-microsoft-learn.md#learn-sas)

## Blob recovery: choose the protection level

Blob soft delete retains deleted objects for the configured period. It does not by itself protect deletion of the container or entire account. Distinguish object, container, and account risks and prepare appropriate protection.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview) · [Blob recovery: choose the protection level](15-microsoft-learn.md#learn-blob-recovery)
