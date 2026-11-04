# 迷你测验：把选择背后的理由也弄懂

[←](README.md) · [CLI](../QUIZ.md) · [在 GitHub 阅读题目](20-quiz-cases.md)

用 34 个原创场景练习 Azure 相关决策，[17 条学习路线](../certifications/zh/README.md)每条各 2 题，8 种语言覆盖相同内容，共 272 个语言版本。选项会打乱，解析包含思路、错误选项的问题、建议复习章节或认证指南和 Microsoft Learn 来源。来源链接使用英文页面。

## 开始

Python 3.9+ · es / en / it / de / fr / ru / ja / zh

```bash
python tools/quiz.py demo --lang zh
python tools/quiz.py run --lang zh --exam AZ-104 --count 2
```

不指定 --count 时，默认从可用场景中选择最多 8 题。使用 --count 34 且不加考试筛选，即可练习整个题库；每条单独路线仍只有 2 题。

```bash
python tools/quiz.py run --lang zh --mode exam --count 34
```

新增的 26 个场景链接到相同语言的认证指南，例如 [AI-103](../certifications/zh/AI-103.md)。最初的 8 个场景保留原有章节链接。扩展前保存的报告仍然兼容：review 使用各报告中保存的题目和引用快照。

## 带解析练习

practice 模式会在每次作答后立即显示答案和解析。输入 A–D 选择，S 或 Enter 跳过，Q 结束。可以限定一条考试学习路线，也可以组合多条路线。建议先想清楚理由再回答，避免只记住选项位置。

```bash
python tools/quiz.py run --lang zh --exam AZ-900 --exam AZ-104 --count 4 --seed 42
```

## 可选计时的考试模式

exam 模式会等到本轮结束后再显示解析。可以设置时间限制，但它不会自动打断等待输入：程序在按 Enter 提交时检查时间，超时答案不被接受。跳过的题，以及提前结束时尚未回答的题，仍然计入总题数。

```bash
python tools/quiz.py run --lang zh --mode exam --count 8 --minutes 12 --report .study-reports/first-quiz.json
```

## 复习错题

review 读取已保存的 JSON 报告，默认复习错题和未答题，并显示解析；加 --all 也能查看答对的题。按主题统计的结果可以帮助你决定先复习哪一章。报告保存当时的题目、选项、作答和解析，因此题库更新后，过去的复习记录也不会变成新题。

```bash
python tools/quiz.py review --lang zh --report .study-reports/first-quiz.json
python tools/quiz.py review --lang zh --report .study-reports/first-quiz.json --all
python tools/quiz.py review --lang zh --report .study-reports/first-quiz.json --json
```

## 个人报告

工具只用 Python 标准库，不访问网络，也不需要 Azure 凭据。个人报告默认保存在 .study-reports/，这个目录已被 Git 忽略。如果指定其他保存位置，需要自己确认是否会被共享。工具不会覆盖已有文件。复习时 --lang 改变界面语言，但保存的题目仍保留原来的语言。

## 分数的含义

每条路线只有 2 道练习题，共 34 题，不是官方题库、完整模拟考试或通过率预测，也不覆盖 17 条学习路线的全部范围。不要只把相同题目的答案背下来；应检查题目假设，回到章节和来源重新推理。这个分数也不能证明已经完成 Azure 部署或具备实际操作能力。

```bash
python tools/quiz.py doctor --lang zh
```

[CLI](../QUIZ.md) · [在 GitHub 阅读题目](20-quiz-cases.md) · [Microsoft Learn](../QUIZ-SOURCES.md)
