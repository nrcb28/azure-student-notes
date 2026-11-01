# 认证：十六条学习路线

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

[通用笔记](../../zh/README.md) · [来源记录](../../CERTIFICATION-SOURCES.md)

十六条考试学习路线，每条都有解释决策的指南、十个带答案的原创案例，以及要求提交证据的五单元练习册。先选择你想弄懂的领域，不必同时学完所有路线。

| 路线 | 方向 | 指南 | 案例 | 练习册 |
|---|---|---|---|---|
| AZ-900 | Azure 基础 | [阅读](AZ-900.md) | [10 个案例](AZ-900-cases.md) | [5 个单元](AZ-900-workbook.md) |
| AZ-104 | Azure 管理 | [阅读](AZ-104.md) | [10 个案例](AZ-104-cases.md) | [5 个单元](AZ-104-workbook.md) |
| AZ-305 | 解决方案架构 | [阅读](AZ-305.md) | [10 个案例](AZ-305-cases.md) | [5 个单元](AZ-305-workbook.md) |
| AZ-400 | 交付与 DevOps | [阅读](AZ-400.md) | [10 个案例](AZ-400-cases.md) | [5 个单元](AZ-400-workbook.md) |
| DP-900 | 数据基础 | [阅读](DP-900.md) | [10 个案例](DP-900-cases.md) | [5 个单元](DP-900-workbook.md) |
| SC-900 | 安全、身份与合规 | [阅读](SC-900.md) | [10 个案例](SC-900-cases.md) | [5 个单元](SC-900-workbook.md) |
| AZ-700 | Azure 网络 | [阅读](AZ-700.md) | [10 个案例](AZ-700-cases.md) | [5 个单元](AZ-700-workbook.md) |
| DP-300 | Azure SQL 管理 | [阅读](DP-300.md) | [10 个案例](DP-300-cases.md) | [5 个单元](DP-300-workbook.md) |
| AI-901 | Microsoft Foundry AI | [阅读](AI-901.md) | [10 个案例](AI-901-cases.md) | [5 个单元](AI-901-workbook.md) |
| SC-200 | 安全运营 | [阅读](SC-200.md) | [10 个案例](SC-200-cases.md) | [5 个单元](SC-200-workbook.md) |
| SC-300 | 身份与访问管理 | [阅读](SC-300.md) | [10 个案例](SC-300-cases.md) | [5 个单元](SC-300-workbook.md) |
| AZ-140 | Azure Virtual Desktop | [阅读](AZ-140.md) | [10 个案例](AZ-140-cases.md) | [5 个单元](AZ-140-workbook.md) |
| AI-103 | AI 应用与智能体开发 | [阅读](AI-103.md) | [10 个案例](AI-103-cases.md) | [5 个单元](AI-103-workbook.md) |
| DP-700 | Fabric 数据工程 | [阅读](DP-700.md) | [10 个案例](DP-700-cases.md) | [5 个单元](DP-700-workbook.md) |
| SC-100 | 网络安全架构 | [阅读](SC-100.md) | [10 个案例](SC-100-cases.md) | [5 个单元](SC-100-workbook.md) |
| AZ-120 | Azure 上的 SAP 工作负载 | [阅读](AZ-120.md) | [10 个案例](AZ-120-cases.md) | [5 个单元](AZ-120-workbook.md) |

## 从哪里开始

AZ-900 用于建立整体认识。DP-900 先讲数据和工作负载，再进入 DP-300。SC-900 不仅涉及 Azure，也包括 Microsoft 365 的安全、身份与合规。AZ-104 提供深入 AZ-700 的运维基础；AZ-305 和 AZ-400 补充设计与交付。这是学习建议，不是官方先决条件。

## 本次扩充内容

DP-900、SC-900、AZ-700、DP-300 在八种语言中都有对应的讲解、案例和交付要求。其他路线以前的补充笔记仍有篇幅差异。每种语言 160 个场景，合计 1280 个语言版本；它们不是实际考试题目。

## 使用训练器复习

自评训练器支持选择十六条路线，也能把案例导出到 Anki。将自己的解释与答案对照，再评价记忆情况。选择题迷你测验仍保留原来四条路线的八道题。

```bash
python tools/study.py demo --lang zh --exam AI-103
python tools/study.py study --lang zh --exam DP-700 --limit 5
python tools/study.py export --lang zh --exam SC-100 --output exports/zh-sc100.tsv
```

## 来源与范围

原有参考资料查阅于 2026 年 10 月 27 日，四条新路线查阅于 2026 年 10 月 30 日。预约前请到 Microsoft Learn 核对考试目标、可用情况、语言和要求。考试代码与认证不同，Expert 认证可能要求其他证书。这里不保证通过，也不声称已在 Azure 执行练习。

[训练器](../../zh/18-study-trainer.md) · [迷你测验](../../zh/19-mini-quiz.md) · [Anki](../../flashcards/zh.tsv) · [网络实验](network-lab.md) · [ADR](ADR-template.md)

## AI、安全运营、身份与虚拟桌面

AI-901、SC-200、SC-300、AZ-140 每条路线新增八种语言的指南、十个案例和五个单元。AI-901 包含 Microsoft Foundry 实现，SC-200 讲调查与响应，SC-300 深入 Entra，AZ-140 覆盖虚拟桌面与应用。这四条路线的来源查阅于 2026 年 11 月 1 日。

## 应用 AI、数据工程、安全架构与 SAP

AI-103、DP-700、SC-100、AZ-120 每条路线新增八种语言的指南、十个案例和五个单元，深入 Foundry 开发、Fabric 工程、安全能力与 SAP 基础设施。来源查阅于 2026 年 11 月 1 日。认证条件与页面更新时间分别核对。
