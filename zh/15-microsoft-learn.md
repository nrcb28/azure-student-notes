# 来自 Microsoft Learn 的实践补充

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

来源核查日期：2026年10月27日。官方说明经过重新表述，并加入独立案例。以下检查未在 Azure 中实际执行。

<a id="learn-sas"></a>

## 1. 基于 Entra ID 的 SAS

Blob user delegation SAS 使用通过 Entra ID 获取的委派密钥。获取密钥需要权限，知道 URL 并不足以签发。

**案例：**允许短时间下载 PDF 时，限制资源、读取权限和期限，避免 URL 进入日志。分别排查过期、授权和网络。泄漏后的撤销方式应依据 SAS 类型设计。

[Microsoft Learn · Storage: user delegation SAS](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

<a id="learn-dns"></a>

## 2. 跟踪私有 DNS

客户端必须将服务名解析为 private endpoint 的 IP。创建网卡不会自动配置全部解析器，推荐区域因服务而异。

**案例：**VM 能访问，大学网络不能访问，应比较 DNS 答复、区域链接、转发和路由。不随意覆盖整个公共区域，也不把 IP 写死在代码里。正确解析不授予数据权限。

[Microsoft Learn · Private endpoint DNS](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

<a id="learn-policy"></a>

## 3. 区分评估和修正

修正任务通过分配的身份与权限，对现有资源应用 modify 或 deployIfNotExists。修改定义不自动更新所有相关授权。

**案例：**旧配置仍不合规，先检查效果、作用域、身份和角色，再在试点组执行并记录结果。Deny 并不是自动转换所有旧资源的工具。

[Microsoft Learn · Policy remediation](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

<a id="learn-dcr"></a>

## 4. DCR 与采集路径

DCR 定义受支持的采集和路由，也能通过转换过滤或修改数据。它不是所有 diagnostic settings 的通用替代。

**案例：**缺少 VM 事件时，检查代理、关联、来源、数据流、目标和结构。收集所有数据增加费用和暴露，过滤过度又可能丢失排障证据。

[Microsoft Learn · Azure Monitor data collection rules](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview)

<a id="learn-whatif"></a>

## 5. What-if 的分析边界

What-if 预测而不应用变更。权限、表达式和依赖可能导致部分部署无法分析。不完整结果不等于没有变更。

**案例：**不要把 Ignore 或未评估模块当作 NoChange。阅读诊断并隔离模块，区分编译、验证、预测和部署后测试。审批也应考虑尚未检查的部分。

[Microsoft Learn · Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

<a id="learn-slots"></a>

## 6. Slot 是运行中的应用

Slot 具有自己的主机名和应用。复制设置不等于复制内容、私有连接和全部依赖。Swap 包含准备及预热。

**案例：**staging 发送真实邮件时，检查连接、身份、slot 专属设置和启动任务。用户流量为零不阻止后台运行，反向 swap 也不能撤销破坏性数据库迁移。

[Microsoft Learn · App Service deployment slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)

<a id="learn-landing"></a>

## 7. Landing zone 的责任划分

Landing zone 组织身份、连接、管理和治理基础。平台与负载可能有不同负责人。加速器不能代替组织需求。

**案例：**五个学院共享网络，需要明确所有者、边界、权限、策略和成本。不要因为有模板，就把完整企业架构搬进小实验。

[Microsoft Learn · Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)

<a id="learn-checks"></a>

## 8. Checks 与发布权限

Azure Pipelines 资源所有者在 YAML 外管理 approvals 和 checks。阶段开始前，必须满足其使用资源的检查。

**案例：**生产要求独立审阅和时间窗口，就应定义资源、审批人、期限和拒绝处理，并测试变更与超时。绿色 pipeline 不代表拥有所有 service connection 的使用权。

[Microsoft Learn · Azure Pipelines approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops)

---

[Source register](../LEARN-SOURCES.md) · [Attribution](../ATTRIBUTION.md)

<a id="learn-blob-recovery"></a>

## 9. 区分 Blob 的保护层级

软删除在已配置的保留期内保存被删除对象，但本身不保护容器或整个账户的删除。这些风险必须分别设计。

**案例：**学生删除笔记容器，不能仅凭 Blob 启用了软删除就认定容器可恢复。应提前检查容器保护和适合场景的备份。

**步骤：**确定删除对象、时间、事前保留设置和恢复身份。验证内容与权限，再核对数据库元数据。删除后启用功能，不等于以前的状态已经保存。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview)

<a id="learn-retry"></a>

## 10. 有界重试与幂等性

重试适合暂时故障，不能修复无效凭据或错误请求。限制次数和总时长，并检查 SDK 已有重试。

**案例：**文档已保存但响应丢失，重复操作可能创建重复记录。使用稳定标识及一致性结果检查。

**步骤：**分类失败，遵守适用的等待提示，设定总截止时间。区分最终恢复和尝试耗尽，不记录秘密。多层重试时计算实际请求量；重试风暴可能加重过载。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)

<a id="learn-rbac-diagnosis"></a>

## 11. 依据证据排查 RBAC

管理资源不等于能够分配角色或读取数据。需要正确操作和作用域，条件还可能限制可授予角色与对象。

**案例：**分配按钮禁用时，先检查账户、租户、范围和分配权限，不要直接申请 Owner。

**步骤：**记录失败操作、实际身份和资源。检查组、直接与继承分配、条件、管理与数据平面，考虑传播和登录更新。重新测试同一最小失败操作，保留允许或拒绝的原因。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting)

<a id="learn-vault-recovery"></a>

## 12. 恢复 Key Vault 及其依赖

软删除支持保留期内恢复，但恢复 vault 不会自动重建某些集成，例如 RBAC 分配与 Event Grid 订阅。

**案例：**vault 已显示但 API 无法读取秘密，需要检查身份、授权及使用方配置。

**步骤：**提前盘点对象与消费者并准备保护。区分恢复和 purge；允许的 purge 会消除对象的恢复机会，不应当作临时清理方法。检查相关保护和限制，最后通过授权消费者的一次完整请求验证，而不只看门户显示。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview)
