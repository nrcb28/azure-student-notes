# 八个场景练习

[←](19-mini-quiz.md) · [CLI](../QUIZ.md)

这只是小型练习，不是官方试题或完整模拟考试，也不能根据结果预测是否通过考试。

<a id="quiz-q01"></a>

## AZ-900 · 操作系统与运行环境的控制

实验用应用必须安装自己的 Linux 内核驱动。哪种托管方式最符合这个要求？

- **A.** 在 Microsoft 365 中运行应用。
- **B.** 使用采用兼容 Linux 镜像的 Azure 虚拟机。
- **C.** 部署到 App Service 的托管运行时。
- **D.** 把驱动放进普通的 Azure Function。

<details>
<summary>思路：</summary>

**B. 使用采用兼容 Linux 镜像的 Azure 虚拟机。**

关键是能管理来宾操作系统。兼容的 Azure VM 允许团队管理系统环境和驱动，同时也把操作系统的维护责任留给团队。托管应用平台虽然方便，但如果不开放所需的内核控制能力，就无法满足这个要求。

- **A.** Microsoft 365 是可以直接使用的软件，并不是安装任意内核驱动的运行环境。
- **C.** App Service 的托管运行时不提供这里需要的来宾内核管理能力。
- **D.** 普通的 Function 不提供这里需要的内核驱动控制能力。

[Microsoft Learn：](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) · [建议复习章节：](03-compute.md)

</details>

<a id="quiz-q02"></a>

## AZ-900 · 水平扩展与状态

笔记 API 在负载均衡器后面增加了多个实例。任何实例都可能被替换，但用户会话必须保留。目前会话只放在各实例的内存中。应该改什么？

- **A.** 增加每个实例的 CPU。
- **B.** 继续把会话放在内存中，只开启会话粘滞路由。
- **C.** 把会话状态移到合适的共享外部存储中。
- **D.** 给每个实例分配一个公网 IP 地址。

<details>
<summary>思路：</summary>

**C. 把会话状态移到合适的共享外部存储中。**

水平扩展会把请求分散到多个实例，因此重要的会话状态不能只依赖某个实例的内存。合适的外部存储能让替换后的实例重新读取状态。粘滞路由无法在原实例消失后保住它的内存。应用还需要处理访问外部状态服务时的连接和故障问题。

- **A.** 增加 CPU 无法在实例被替换后保留它的内存。
- **B.** 被固定选中的实例一旦消失，即使有粘滞路由，会话仍然会丢失。
- **D.** 公网地址不提供共享或持久的会话状态。

[Microsoft Learn：](https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/scale-out) · [建议复习章节：](01-fundamentals.md)

</details>

<a id="quiz-q03"></a>

## AZ-104 · 存储数据权限

用户拥有某个存储帐户的 Contributor 角色。使用该用户 Entra 身份发出的 Blob 请求已到达服务，但因缺少数据权限而被拒绝。用户只需要读取一个容器中的 Blob。符合最小权限原则的做法是什么？

- **A.** 在该容器的作用域内分配 Storage Blob Data Reader 角色。
- **B.** 在整个订阅上分配 Owner 角色。
- **C.** 开放所有入站网络端口。
- **D.** 把存储帐户密钥发给用户。

<details>
<summary>思路：</summary>

**A. 在该容器的作用域内分配 Storage Blob Data Reader 角色。**

资源管理权限与 Blob 数据权限是两回事。Storage Blob Data Reader 提供所需的读取能力，容器作用域又把授权限制在实际需求内。题目已经说明问题在数据权限，因此授予广泛的管理权或修改无关的网络配置，都不是适度的解决办法。

- **B.** 订阅级 Owner 远超“读取一个容器”的需求。
- **C.** 开放端口不会补上缺少的数据操作授权。
- **D.** 帐户密钥提供的访问范围比这里的需求大得多。

[Microsoft Learn：](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access) · [建议复习章节：](06-identity.md)

</details>

<a id="quiz-q04"></a>

## AZ-104 · RBAC 权限继承

用户既有直接分配给某台 VM 的 Reader 角色，也属于一个在订阅作用域拥有 Reader 的组。你只删除了 VM 上的直接角色分配，但用户仍能读取这台 VM。原因是什么？

- **A.** Azure 自动给所有用户分配所有 VM 的 Reader。
- **B.** 资源组标签恢复了已删除的角色分配。
- **C.** 删除角色之前总是必须先删除 VM。
- **D.** 组的角色分配仍然通过继承授予访问权限。

<details>
<summary>思路：</summary>

**D. 组的角色分配仍然通过继承授予访问权限。**

删除一个角色分配，不会消除从其他分配中获得的权限。组在订阅作用域拥有 Reader，所以成员仍可继承对 VM 的读取权限。在把问题归咎于服务故障或继续加权限之前，先检查直接分配、组成员身份和上级作用域。

- **A.** 不存在给所有用户统一授予 Reader 的规则。
- **B.** 标签用于分类资源，不会重新创建角色分配。
- **C.** 删除角色分配不要求删除它所保护的资源。

[Microsoft Learn：](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview) · [建议复习章节：](06-identity.md)

</details>

<a id="quiz-q05"></a>

## AZ-305 · 恢复目标与 RPO

当前设计每 24 小时才保留一个成功且可恢复的数据库恢复点。业务现在要求灾难后最多只能丢失最近 1 小时的数据。哪个改动能直接弥补这个差距？

- **A.** 增加 API 服务器的 CPU。
- **B.** 设计间隔不超过 1 小时的可恢复数据保护点，并验证恢复过程。
- **C.** 添加一个费用预警预算。
- **D.** 把资源组重命名为 production。

<details>
<summary>思路：</summary>

**B. 设计间隔不超过 1 小时的可恢复数据保护点，并验证恢复过程。**

RPO 用时间表示可以接受丢失多少最近的数据。每天一次的恢复点无法独自满足 1 小时的目标。数据保护设计必须足够频繁地产生可恢复状态，并验证这些状态确实能恢复。提高应用算力或修改费用标签，都不会改变现有恢复数据的新旧程度。

- **A.** API 的 CPU 不会提高恢复数据的保护频率。
- **C.** 预算针对支出发出预警，不会减少数据丢失。
- **D.** 资源组名称不会改变恢复点的生成频率。

[Microsoft Learn：](https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery) · [建议复习章节：](10-architecture.md)

</details>

<a id="quiz-q06"></a>

## AZ-305 · 专用连接的 DNS

存储服务已禁用公共访问，也已建立专用终结点。但客户端仍把服务主机名解析为公网 IP，其他专用网络路径则可用。首先应该排查什么？

- **A.** 给客户端分配订阅级 Owner。
- **B.** 永久硬编码公网 IP。
- **C.** 客户端使用的专用 DNS 区域、链接和转发配置。
- **D.** 无限增加应用的重试次数。

<details>
<summary>思路：</summary>

**C. 客户端使用的专用 DNS 区域、链接和转发配置。**

客户端解析出的目的地址，与预期的专用连接不一致。应检查该服务推荐的专用 DNS 配置，以及客户端如何访问这套 DNS，包括区域链接和转发。连接时仍应使用服务主机名。修好 DNS 本身不会授予数据权限，但无关的管理权和无限重试也修不好这个解析问题。

- **A.** Owner 不会改变客户端的名称解析。
- **B.** 公共访问被禁用后，公网地址不是预期的连接目的地。
- **D.** 重复请求无法修复每次都返回同样错误结果的 DNS 配置。

[Microsoft Learn：](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) · [建议复习章节：](05-networking.md)

</details>

<a id="quiz-q07"></a>

## AZ-400 · 提升已测试构件

流水线先测试一个容器镜像，然后使用可能变化的依赖从源码重新构建生产镜像。怎样确保生产环境拿到的就是通过测试的镜像？

- **A.** 只重新测试源码注释。
- **B.** 使用 latest 标签，但不记录它指向哪个镜像。
- **C.** 因为源码提交没变，所以跳过测试。
- **D.** 提升同一个已测试镜像，并用不可变摘要标识它。

<details>
<summary>思路：</summary>

**D. 提升同一个已测试镜像，并用不可变摘要标识它。**

即使源码提交相同，工具、依赖或基础镜像变化后，构建结果也可能不同。直接提升已测试的镜像，可以避免重新构建带来的差异。不可变摘要标识的是实际构件，而标签以后可能指向别处。环境配置仍需要单独验证，并以受控方式管理。

- **A.** 源码注释无法标识已经构建出的镜像。
- **B.** 可变标签以后可能指向另一个镜像。
- **C.** 提交没有变化，不能证明重新构建的产物也完全一样。

[Microsoft Learn：](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-concepts) · [建议复习章节：](12-devops.md)

</details>

<a id="quiz-q08"></a>

## AZ-400 · 金丝雀发布的判断信号

一次金丝雀发布的 CPU 和内存正常，但下载文档时会返回错误的文件。是否继续部署，应该依据什么？

- **A.** 反映功能正确性的信号，以及事先定义的停止或回滚条件。
- **B.** 只看 CPU，因为基础设施健康就说明结果正确。
- **C.** 检查返回文件之前，先换更大的 VM。
- **D.** 删除旧日志，让仪表板看起来更清爽。

<details>
<summary>思路：</summary>

**A. 反映功能正确性的信号，以及事先定义的停止或回滚条件。**

发布版本可能运行得很轻松，却给用户返回错误的业务结果。继续推广时，需要能反映用户操作是否正确的信号，而不只是基础设施利用率。预先定义停止或回滚条件，才能把这些证据用于决策。还要检查数据兼容性：回退应用代码，并不会自动撤销这次发布造成的有害数据修改。

- **B.** CPU 和内存正常不能证明用户拿到的文档正确。
- **C.** 增加算力本身不能修复应用的错误输出。
- **D.** 删除证据只会让调查更困难，并不能纠正结果。

[Microsoft Learn：](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments) · [建议复习章节：](12-devops.md)

</details>
