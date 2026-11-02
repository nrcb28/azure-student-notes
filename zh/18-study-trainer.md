# 无需 Azure 的学习训练器

[←](README.md) · [Anki](../flashcards/zh.tsv)

每种语言160个案例，每项认证10个。只需 Python3.9或更高和标准库，不需要云账户、外部包或使用时联网。

```bash
python tools/study.py demo --lang zh --exam AZ-104
python tools/study.py study --lang zh --exam AZ-104 --limit 5
```

默认显示时区 Europe/Madrid 需要操作系统的 IANA 时区数据。如果没有这些数据，请在 demo 或 study 命令后加 --timezone UTC，无需额外安装包。

## 1. 自己作答

阅读并思考，回车显示解释。比较后自评：0忘记、1困难、2良好、3简单。q退出，已完成评价逐条保存。这是自评，不是自动批改或认证分数。

## 2. 复习薄弱项

默认优先到期卡，再加入新卡。weak选择困难或有遗忘历史的案例，random随机混合。进度按语言分开，不保存书面答案。

## 3. 进度和计划

stats按考试显示新卡、到期、巩固和遗忘。巩固表示连续两次至少2分，不证明考试准备度。plan建议每案例约四分钟，不预测实际复习期限。

## 4. 间隔规则

0 在十分钟后返回并重置连续次数；1 在次日返回并重置。评分 2 和 3 共用连续成功复习次数。选择 2 时，首次成功安排一天，第二次安排三天，此后将上一次间隔翻倍。选择 3 时，首次成功安排四天；此后将上一次间隔乘以 2.5，舍入到整天，且至少为四天。两种评分的上限都是 365 天。更换评分不会重置连续次数：先选 3 再选 2，间隔会先是四天，再是三天。这是简单自定义规则，不是 FSRS 或记忆保证。

## 5. 导出到 Anki

下载现成牌组或导出选择，UTF-8三列为问题、解释、标签。Anki进度独立，导入时确认预览和列映射。

## 6. 你的数据

默认.study-progress.json不进入Git。--progress可改路径。原子写入和并发保护避免覆盖，损坏JSON不会被替换。迁移历史时保留备份。

```bash
python tools/study.py study --lang zh --mode weak --limit 5
python tools/study.py stats --lang zh
python tools/study.py plan --lang zh --days 7 --minutes 20
python tools/study.py export --lang zh --exam AZ-104 --output exports/zh-az104.tsv
python tools/study.py doctor --lang zh
```

[CLI reference](../TRAINER.md) · [Anki decks](../flashcards/README.md)

## 迷你测验：把选择背后的理由也弄懂

[迷你测验：把选择背后的理由也弄懂](19-mini-quiz.md) · [在 GitHub 阅读题目](20-quiz-cases.md)
