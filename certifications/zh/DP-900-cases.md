# DP-900 · 十个案例与推理答案

[指南](DP-900.md) · [练习册](DP-900-workbook.md) · [目录](README.md)

以下是原创练习场景，不是实际考试题。先说明要求，再排除一种替代方案，并描述应收集的证据。没有声称已经在云中部署。

## 1. 笔记应用保存 PDF 和可搜索的归属元数据，两者必须放进同一张 SQL 表吗？

<details>
<summary>推理过程</summary>

不必。一种合理方案是在 Blob Storage 保存 PDF 对象，在数据库保存归属和课程关系。重点是解释访问与一致性的边界：文件上传可能成功，元数据更新却失败。应定义可恢复的工作流，以及发现孤立文件的办法。如果要求足以支持，把两者放进数据库也可能合理；但“所有数据都必须是一行 SQL 记录”不是好的起点。

</details>

## 2. JSON 文件有可选的嵌套属性，缺少一些字段就属于非结构化数据吗？

<details>
<summary>推理过程</summary>

JSON 可以表示半结构化数据：即使记录不同，键和嵌套仍然提供组织。缺少字段不会消除这种结构。把表示方式、数据质量和存储选择分开判断。要确认缺失字段意味着合法情况、未知值还是导入错误，并说明消费者应该怎样处理。文档数据库可能适合访问模式，但单凭存在 JSON，不能决定架构。

</details>

## 3. 每条选课记录都重复课程名称和教师，规范化可以防止什么问题？

<details>
<summary>推理过程</summary>

课程改名时，可能只更新部分选课行，其他行仍保留旧值。用稳定键标识 Courses 记录，再由 Enrolments 引用，可以减少这种更新异常。要解释所需约束和通过连接重建结果的过程。这不意味着任何位置都禁止重复：分析快照可能有意保留历史描述。先说明讨论的是当前事务事实，还是历史报告模型。

</details>

## 4. 报告查询拖慢线上选课，把图表移到 Power BI 就会自动消除数据库压力吗？

<details>
<summary>推理过程</summary>

不会。效果取决于模型怎样获取和刷新数据。报告仍可能查询业务源，或者产生昂贵的刷新任务。选方案前先明确新鲜度、查询模式和源端容量。整理后的分析副本可能隔离部分工作，但也引入刷新延迟和管道责任。应该测量源端负载并定义“最新”的含义，不能假设换一种可视化工具就改变了底层访问。

</details>

## 5. 既有 SQL Server 应用依赖操作系统组件，Azure SQL Database 总能直接替换它吗？

<details>
<summary>推理过程</summary>

不能。选择目标前要清点这些组件及其他依赖。Azure SQL Database、Managed Instance 和 Azure VM 上的 SQL Server 有不同的管理与兼容边界。VM 提供操作系统访问，但团队要承担更多维护。Managed Instance 可能满足部分实例级要求，却未必支持所有外部依赖。应准备兼容清单和迁移测试计划；数据库引擎熟悉，不证明完整应用无需修改就能运行。

</details>

## 6. 同学认为 Azure Table Storage 名字带 Table 就有外键，你会怎样纠正设计？

<details>
<summary>推理过程</summary>

Table Storage 是非关系实体存储，不是托管关系 SQL 服务。不能从名字推断它提供关系连接或外键约束。先列出实际的读取、更新、关联和一致性要求，再比较合适的实体模型与关系设计。有效证据是一份完整例子：展示如何根据选课记录找到课程，以及如何防止或发现无效引用。产品名称只是调查线索，不能替代能力核对。

</details>

## 7. 夜间处理已能按时提供次日早晨的报告，是否应该为了“先进”而改成流处理？

<details>
<summary>推理过程</summary>

先看业务允许的延迟。如果可靠的夜间批处理准时提供所需结果，流处理可能只增加运维工作，而不改变用户能作出的决定。如果工作人员必须在几分钟内响应过载，就为这个要求评估更低延迟的路径。无论采用哪种方式，都要处理重复记录、输入不完整和重试。比较端到端新鲜度与失败恢复，不只比较某个处理组件运行得有多频繁。

</details>

## 8. 原始数据先加载到仓库，再在仓库里清洗，这叫 ETL 吗？仓库是否让验证变得多余？

<details>
<summary>推理过程</summary>

这个顺序属于 ELT：先加载，再利用目标的处理能力转换。ETL 则在加载到预定目标前完成转换。两者都不能免除数据契约与检查。要定义无效记录去向、哪些转换可以重复，以及接受记录总数如何与源端核对。即使分析师只看到清洗后的模型，受限原始数据仍需访问控制；查询方便不等于底层记录安全或正确。

</details>

## 9. 仪表板统计下载事件，重试产生重复事件 ID，COUNT(*) 一定等于已完成下载数吗？

<details>
<summary>推理过程</summary>

只有数据定义保证每个被计数的行对应一次完成的下载时才成立。重复投递可能使 COUNT(*) 偏大。先定义业务事件、稳定标识、完成条件和报告区间，再按定义去重或聚合。保留拒绝和重复数量，使调整可解释。用包含一个重复 ID 和一次未完成下载的小数据集测试。图表看似合理，不证明度量回答了用户真正的问题。

</details>

## 10. 六条课程记录适合文档模型，这能证明 Cosmos DB 是唯一合理的存储吗？

<details>
<summary>推理过程</summary>

不能。许多服务都能保存六条记录；这个例子只说明能够表达它们。要比较预计查询、关系、更新行为、一致性、运维要求和团队技能。约束与关联实体占主导时，关系数据库可能更简单；其他访问模式可能适合文档模型。记录偏好方案的一条理由，以及什么条件会使你改选。基础学习应训练推理，而不是给每个 JSON 例子贴一个数据库产品标签。

</details>

来源：[官方目标](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)、[Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview)、[存储](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)、[ETL/ELT](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl)、[Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview)。
