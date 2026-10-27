# 治理与合规

[目录](README.md) · [认证考试](../certifications/zh/README.md)

RBAC 决定谁能操作，Policy 规定资源必须满足的条件。有创建 VM 的权限，也可能因区域策略被拒绝。

Audit 报告不合规，Deny 拒绝指定请求。Modify 和 DeployIfNotExists 需要适当身份、权限和设置；现有资源可能需要修正任务，而不会立即全部改变。

标签用于分类，不是安全边界，也不总是自动继承。管理锁不能代替数据权限或备份。

Defender for Cloud 与 Sentinel 处理不同问题。提供商具备合规认证，不代表自己的应用自动合规。

**练习：**先用审计了解影响、负责人和例外，再考虑强制拒绝。每项例外都应有原因和复查条件，不能永久成为绕过规则的通道。

---

[←](06-identity.md) · [→](08-observability.md) · [English](../en/07-governance.md)

## Microsoft Learn 补充内容 · policy

修正任务通过分配的身份与权限，对现有资源应用 modify 或 deployIfNotExists。修改定义不自动更新所有相关授权。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources) · [Microsoft Learn 补充内容](15-microsoft-learn.md#learn-policy)
