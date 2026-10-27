# 计算与容器

[目录](README.md) · [认证考试](../certifications/zh/README.md)

需要操作系统控制时考虑 VM；兼容的 Web/API 考虑 App Service；事件触发代码考虑 Functions。Container Instances 和 Container Apps 可以运行容器，而不必自行管理 Kubernetes 集群。只有需求足以证明其运维成本时才选择 AKS。

容器不是完整虚拟机。Serverless 仍有启动、时长、网络、配额和费用条件。

**诊断：**容器成功启动并不代表应用可用。检查端口、进程、配置、启动日志、健康检查，再测试经过实际依赖的完整请求。

将镜像与环境配置分开，不把秘密写进镜像层。即使后续删除文件，旧层仍可能保留内容。固定版本或 digest 比可变的 latest 更方便复现问题。

---

[←](02-resources.md) · [→](04-storage.md) · [English](../en/03-compute.md)

## Microsoft Learn 补充内容 · slots

Slot 具有自己的主机名和应用。复制设置不等于复制内容、私有连接和全部依赖。Swap 包含准备及预热。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) · [Microsoft Learn 补充内容](15-microsoft-learn.md#learn-slots)
