# 存储与数据

[目录](README.md) · [认证考试](../certifications/zh/README.md)

PDF 等对象适合 Blob Storage，共享文件考虑 Azure Files，VM 磁盘使用 Managed Disks。关系和事务需求适合评估关系数据库。API 使用 JSON 并不自动意味着应该选择文档数据库。

LRS 在本地复制，ZRS 跨可用区复制。GRS/GZRS 的跨区域复制是异步的，最新写入可能尚未到达次要区域。

冗余、版本、软删除和备份处理不同风险。Archive 可能需要解冻，不适合立即读取的文件。

**应用：**PDF 放 Blob，标题和权限等元数据放数据库。只恢复文件却缺少元数据会造成不一致。将 SAS 当作凭据保护，限制权限和期限，并区分管理权限与数据访问权限。

---

[←](03-compute.md) · [→](05-networking.md) · [English](../en/04-storage.md)

## Microsoft Learn 补充内容 · sas

Blob user delegation SAS 使用通过 Entra ID 获取的委派密钥。获取密钥需要权限，知道 URL 并不足以签发。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli) · [Microsoft Learn 补充内容](15-microsoft-learn.md#learn-sas)
