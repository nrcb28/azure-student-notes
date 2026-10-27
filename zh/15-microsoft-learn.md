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
