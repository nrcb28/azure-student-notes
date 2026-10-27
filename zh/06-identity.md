# 身份与安全

[目录](README.md) · [认证考试](../certifications/zh/README.md)

身份验证确认你是谁，授权决定你能做什么。MFA 加强登录，并不授予文档权限。

Azure RBAC 结合身份、角色和作用域。Reader 读取，Contributor 管理资源但不能授予 RBAC 角色，Owner 还可以授予访问。目录角色和资源角色不同。

托管身份减少自行保存应用凭据的需要，但仍需要授权。Key Vault 管理秘密、密钥和证书。

**例子：**删除资源上的 Reader 后仍能访问，可能来自组成员身份或上层作用域继承。先确认实际身份和所有分配，不要直接认定系统失效。

登录后的学生也不应该通过修改 URL 中的 ID 编辑别人的笔记。应用必须针对每个对象进行授权检查。

---

[←](05-networking.md) · [→](07-governance.md) · [English](../en/06-identity.md)

## Microsoft Learn 补充内容 · sas

Blob user delegation SAS 使用通过 Entra ID 获取的委派密钥。获取密钥需要权限，知道 URL 并不足以签发。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli) · [Microsoft Learn 补充内容](15-microsoft-learn.md#learn-sas)

## 依据证据排查 RBAC

管理资源不等于能够分配角色或读取数据。需要正确操作和作用域，条件还可能限制可授予角色与对象。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting) · [依据证据排查 RBAC](15-microsoft-learn.md#learn-rbac-diagnosis)

## 恢复 Key Vault 及其依赖

软删除支持保留期内恢复，但恢复 vault 不会自动重建某些集成，例如 RBAC 分配与 Event Grid 订阅。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview) · [恢复 Key Vault 及其依赖](15-microsoft-learn.md#learn-vault-recovery)
