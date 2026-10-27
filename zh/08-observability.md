# 监控与诊断

[目录](README.md) · [认证考试](../certifications/zh/README.md)

指标、日志和跟踪提供不同证据。Azure Monitor 提供监控能力，Application Insights 观察应用，Log Analytics 用 KQL 查询已收集的日志。

CPU 低不代表响应快，应用可能在等待数据库。平均值会掩盖少量慢请求，需要结合分布、百分位和请求数量，不能过度解释很小的样本。

有效告警需要信号、阈值、时间窗口和处理动作。Service Health 和 Resource Health 的范围不同。

**方法：**确定影响与开始时间，查看最近变更，追踪请求及依赖，用数据验证假设，修复后确认恢复。不记录令牌或完整文档。保留时间、采样和详细程度影响成本及隐私。OpenTelemetry 要匹配运行时和集成方式。

---

[←](07-governance.md) · [→](09-costs.md) · [English](../en/08-observability.md)

## Microsoft Learn 补充内容 · dcr

DCR 定义受支持的采集和路由，也能通过转换过滤或修改数据。它不是所有 diagnostic settings 的通用替代。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview) · [Microsoft Learn 补充内容](15-microsoft-learn.md#learn-dcr)
