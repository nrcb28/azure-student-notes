# Study trainer without Azure

[←](README.md) · [Anki](../flashcards/en.tsv)

Practise the 40 cases in your language, ten per certification. Requires Python 3.9 or later and only its standard library. No cloud account, external packages, or connection during use.

```bash
python tools/study.py demo --lang en --exam AZ-104
python tools/study.py study --lang en --exam AZ-104 --limit 5
```

## 1. Test yourself

Read the question, think, and press Enter. Compare the explanation and rate: 0 forgotten, 1 hard, 2 good, 3 easy. q quits; completed ratings are saved individually. This is self-assessment, not automatic marking or an exam score.

## 2. Review difficulties

Default mode selects overdue and new cards, prioritising overdue reviews. weak selects rated hard cases or those with past lapses; random mixes the bank. Progress is separate per language. Written answers are not stored.

## 3. Progress and planning

stats shows new, due, consolidated, and lapses per exam. Consolidated means two consecutive ratings of at least 2, not exam readiness. plan suggests roughly four minutes per case rather than predicting future review dates.

## 4. Review intervals

0 returns in ten minutes and resets the streak; 1 returns tomorrow and resets it. 2 schedules one day, then three, then doubles. 3 starts at four days and multiplies by 2.5, capped at 365 days. This is a simple custom rule, not FSRS or a memory guarantee.

## 5. Take it to Anki

Download prepared decks or export a selection. Files use UTF-8 and three columns: question, explanation, and tags. Anki maintains independent progress. Check preview and column mapping during import.

## 6. Your data

Default progress is .study-progress.json, excluded from Git. Choose another path with --progress. Atomic writes reject stale concurrent sessions. Damaged JSON is not replaced. Keep backups if moving your review history.

```bash
python tools/study.py study --lang en --mode weak --limit 5
python tools/study.py stats --lang en
python tools/study.py plan --lang en --days 7 --minutes 20
python tools/study.py export --lang en --exam AZ-104 --output exports/en-az104.tsv
python tools/study.py doctor --lang en
```

[CLI reference](../TRAINER.md) · [Anki decks](../flashcards/README.md)

## Mini quiz with reasoned marking

[Mini quiz with reasoned marking](19-mini-quiz.md) · [Read the questions on GitHub](20-quiz-cases.md)
