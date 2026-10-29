# 无需 Azure 的学习训练器

[←](README.md) · [Anki](../flashcards/zh.tsv)

每种语言40个案例，每项认证10个。只需 Python3.9或更高和标准库，不需要云账户、外部包或使用时联网。

```bash
python tools/study.py demo --lang zh --exam AZ-104
python tools/study.py study --lang zh --exam AZ-104 --limit 5
```

## 1. 自己作答

阅读并思考，回车显示解释。比较后自评：0忘记、1困难、2良好、3简单。q退出，已完成评价逐条保存。这是自评，不是自动批改或认证分数。

## 2. 复习薄弱项

默认优先到期卡，再加入新卡。weak选择困难或有遗忘历史的案例，random随机混合。进度按语言分开，不保存书面答案。

## 3. 进度和计划

stats按考试显示新卡、到期、巩固和遗忘。巩固表示连续两次至少2分，不证明考试准备度。plan建议每案例约四分钟，不预测实际复习期限。

## 4. 间隔规则

0十分钟后返回并重置连续次数；1次日返回并重置。2先一天、再三天、随后翻倍。3从四天开始再乘2.5，最多365天。这是简单自定义规则，不是FSRS或记忆保证。

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
