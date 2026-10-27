# DevOps 与基础设施即代码

[目录](README.md) · [认证考试](../certifications/zh/README.md)

CI 通过构建和检查集成变更。持续交付保持随时可发布；持续部署自动发布满足条件的变更。

将经过测试的同一个制品推广到后续环境，记录版本和 digest。重新构建可能引入依赖或工具差异。

Bicep 描述 Azure 资源，Terraform 的状态文件需要保护。Plan 和 what-if 有帮助，但不无条件保证后续成功。OIDC 也需要联合信任、身份和授权。

**回滚：**旧镜像不能恢复被删除的数据库列。设计兼容迁移和数据恢复，不让不可信 PR 在有生产权限的持久 runner 上执行。

**练习：**关联 issue、PR、测试、制品和发布，定义晋级及回滚条件。文档本地检查命令为 python tools/check_docs.py。

---

[←](11-messaging.md) · [→](13-laboratorios.md) · [English](../en/12-devops.md)

## Microsoft Learn 补充内容 · whatif

What-if 预测而不应用变更。权限、表达式和依赖可能导致部分部署无法分析。不完整结果不等于没有变更。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if) · [Microsoft Learn 补充内容](15-microsoft-learn.md#learn-whatif)

## Microsoft Learn 补充内容 · slots

Slot 具有自己的主机名和应用。复制设置不等于复制内容、私有连接和全部依赖。Swap 包含准备及预热。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) · [Microsoft Learn 补充内容](15-microsoft-learn.md#learn-slots)

## Microsoft Learn 补充内容 · checks

Azure Pipelines 资源所有者在 YAML 外管理 approvals 和 checks。阶段开始前，必须满足其使用资源的检查。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops) · [Microsoft Learn 补充内容](15-microsoft-learn.md#learn-checks)

## 有界重试与幂等性

重试适合暂时故障，不能修复无效凭据或错误请求。限制次数和总时长，并检查 SDK 已有重试。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) · [有界重试与幂等性](15-microsoft-learn.md#learn-retry)
