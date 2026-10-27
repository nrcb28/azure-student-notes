# 复习 · 24

[目录](README.md)

考试领域和权重依据2026年10月27日核查的官方英语指南。不同考试语言和日期可能有更新，请在报考前确认。这是独立学习材料，不保证覆盖全部考题或通过考试。

## 1. 需要内核控制怎么办？

<details>
<summary>答案</summary>

评估满足要求的 VM，不假设 Web 平台具有相同控制能力。

</details>

## 2. MFA 会授予文档权限吗？

<details>
<summary>答案</summary>

不会。身份验证与授权不同。

</details>

## 3. 公共 endpoint 就是匿名访问吗？

<details>
<summary>答案</summary>

不一定，仍可以要求身份和权限。

</details>

## 4. 增加实例属于哪种扩展？

<details>
<summary>答案</summary>

横向扩展；增加单实例能力是纵向扩展。

</details>

## 5. 副本能恢复所有删除吗？

<details>
<summary>答案</summary>

不能，需要保留以前状态的机制。

</details>

## 6. 如何限制部署区域？

<details>
<summary>答案</summary>

使用作用域和效果合适的 Policy。

</details>

## 7. 预算停止全部支出吗？

<details>
<summary>答案</summary>

不会，主要用于跟踪和告警。

</details>

## 8. CPU 低但 API 很慢。

<details>
<summary>答案</summary>

检查数据库、网络、依赖和等待。

</details>

## 9. 网络慢但要迁移大量数据。

<details>
<summary>答案</summary>

按时间、支持和安全比较网络传输与 Data Box。

</details>

## 10. 部署成功就足够了吗？

<details>
<summary>答案</summary>

不够，还要验证实际功能和依赖。

</details>

## 11. 移除 Reader 后仍能访问。

<details>
<summary>答案</summary>

检查组、继承分配和实际身份。

</details>

## 12. Contributor 无法读取 Blob。

<details>
<summary>答案</summary>

检查数据角色及身份验证方式。

</details>

## 13. VNet integration 后 Web 仍公开。

<details>
<summary>答案</summary>

区分出站集成和入站控制。

</details>

## 14. backend 显示 unhealthy。

<details>
<summary>答案</summary>

检查 probe 端口、响应、进程和过滤。

</details>

## 15. 有 A-B、B-C 对等互连，A-C 不通。

<details>
<summary>答案</summary>

对等互连不会自动传递。

</details>

## 16. Bicep 编译通过但部署被拒绝。

<details>
<summary>答案</summary>

检查 Policy、权限、配额和可用性。

</details>

## 17. 备份成功能保证 RTO 吗？

<details>
<summary>答案</summary>

不能，必须测量完整恢复时间。

</details>

## 18. 有 private endpoint 却解析为公共 IP。

<details>
<summary>答案</summary>

检查 DNS 区域、链接、转发及客户端解析。

</details>

## 19. VM 停止后仍有费用。

<details>
<summary>答案</summary>

区分停止、取消分配及磁盘等成本。

</details>

## 20. Policy 未修复旧资源。

<details>
<summary>答案</summary>

检查效果和所需修正任务。

</details>

## 21. RPO 为零就表示 RTO 为零？

<details>
<summary>答案</summary>

不是，数据损失和恢复时间独立。

</details>

## 22. JSON 加复杂事务该如何选择？

<details>
<summary>答案</summary>

按查询和需求选择数据库，而不是传输格式。

</details>

## 23. 小团队为一个 API 选择 AKS。

<details>
<summary>答案</summary>

比较 Kubernetes 必要性、能力、成本和备选。

</details>

## 24. 境外复制与境内存储要求冲突。

<details>
<summary>答案</summary>

检查副本、备份、日志和依赖的位置。

</details>
