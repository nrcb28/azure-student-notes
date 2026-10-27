# 资源与可用性

[目录](README.md) · [认证考试](../certifications/zh/README.md)

订阅是管理、配额和计费的重要边界。管理组对多个订阅应用治理规则。资源组组织生命周期相关的资源。Entra 租户是身份目录，不是普通资源容器。

资源组的位置用于其元数据，不强制所有资源位于同一区域。可用区在一个区域内提供物理隔离，具体支持取决于服务。

**例子：**开发和生产分开，共享网络有独立负责人。删除一个应用时不能顺便删除所有团队使用的网络。

移动前检查资源类型、依赖、权限和标识符变化。跨资源组移动不等于通用的跨区域迁移。

**练习：**不要只说有两个实例，而要说明设计能够应对哪种故障，以及哪些依赖仍是单点。

---

[←](01-fundamentals.md) · [→](03-compute.md) · [English](../en/02-resources.md)

## Microsoft Learn 补充内容 · landing

Landing zone 组织身份、连接、管理和治理基础。平台与负载可能有不同负责人。加速器不能代替组织需求。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) · [Microsoft Learn 补充内容](15-microsoft-learn.md#learn-landing)
