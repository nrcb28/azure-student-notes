# 架构与恢复

[目录](README.md) · [认证考试](../certifications/zh/README.md)

架构从用户、数据、需求、预算和团队运维能力开始，不是服务越多越好。

笔记应用可以包含 API、元数据库、Blob、队列和文档处理器。这只是概念模型，不是完整生产配置。

RTO 是目标恢复时间，RPO 用时间表示可接受的近期数据损失。数据库恢复成功，但 DNS、权限和连接字符串还指向旧环境，服务仍然不可用。

设计超时、退避重试、幂等处理和部分失败。恢复测试要隔离，避免发送真实邮件或覆盖生产数据。

**ADR：**记录背景、可验证需求、备选方案、决策、后果、验证方法和复查条件。不要把某个产品名称当成自动满足 RTO/RPO 的证据，必须测试完整恢复路径。

---

[←](09-costs.md) · [→](11-messaging.md) · [English](../en/10-architecture.md)

## Microsoft Learn 补充内容 · landing

Landing zone 组织身份、连接、管理和治理基础。平台与负载可能有不同负责人。加速器不能代替组织需求。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) · [Microsoft Learn 补充内容](15-microsoft-learn.md#learn-landing)

## 区分 Blob 的保护层级

软删除在已配置的保留期内保存被删除对象，但本身不保护容器或整个账户的删除。这些风险必须分别设计。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview) · [区分 Blob 的保护层级](15-microsoft-learn.md#learn-blob-recovery)

## 有界重试与幂等性

重试适合暂时故障，不能修复无效凭据或错误请求。限制次数和总时长，并检查 SDK 已有重试。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) · [有界重试与幂等性](15-microsoft-learn.md#learn-retry)

## 恢复 Key Vault 及其依赖

软删除支持保留期内恢复，但恢复 vault 不会自动重建某些集成，例如 RBAC 分配与 Event Grid 订阅。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview) · [恢复 Key Vault 及其依赖](15-microsoft-learn.md#learn-vault-recovery)
