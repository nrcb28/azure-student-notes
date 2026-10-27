# 网络与连接

[目录](README.md) · [认证考试](../certifications/zh/README.md)

VNet 是虚拟网络，子网划分地址空间。NSG 提供有状态流量过滤，DNS 解析名称。允许端口不证明有进程监听。

对等互连不自动传递。VPN Gateway 提供加密隧道；ExpressRoute 提供专用连接，但不自动意味着端到端加密。

Private endpoint 需要分别检查私有 DNS、路由和公共访问设置。Load Balancer 处理 TCP/UDP，Application Gateway 处理区域 Web，Front Door 提供全球 Web 入口，Traffic Manager 基于 DNS 选择目标。

**诊断：**按名称、解析地址、路由、过滤、端口、身份验证和授权逐步排查。不要通过开放所有端口掩盖问题。客户端必须能够解析并到达私有地址，创建 endpoint 本身不会配置所有客户端。

---

[←](04-storage.md) · [→](06-identity.md) · [English](../en/05-networking.md)

## Microsoft Learn 补充内容 · dns

客户端必须将服务名解析为 private endpoint 的 IP。创建网卡不会自动配置全部解析器，推荐区域因服务而异。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) · [Microsoft Learn 补充内容](15-microsoft-learn.md#learn-dns)
