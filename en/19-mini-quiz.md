# Mini quiz with reasoned marking

[←](README.md) · [CLI](../QUIZ.md) · [Read the questions on GitHub](20-quiz-cases.md)

Eight original scenarios, two for each route: AZ-900, AZ-104, AZ-305, and AZ-400. Questions, options, explanations, and interface are available in all eight languages. This small bank practises decisions from the notes; it is independent of Microsoft and does not reproduce real exam questions. Requires Python 3.9+ and its standard library. No Azure account or connection is needed.

## Start

Python 3.9+ · es / en / it / de / fr / ru / ja / zh

```bash
python tools/quiz.py demo --lang en
python tools/quiz.py run --lang en --exam AZ-104 --count 2
```

## Practice with feedback

In practice mode you see the explanation after each answer. Use A–D to choose, S or Enter to skip, and Q to finish. Option order changes; the answer is graded by its actual content. Each wrong answer has its own reason, a Microsoft Learn source, and a local chapter to revisit. Repeat --exam to combine routes; --count cannot exceed the distinct scenarios available in those routes. Omitting --count uses up to eight. A fixed --seed reproduces question and option order.

```bash
python tools/quiz.py run --lang en --exam AZ-900 --exam AZ-104 --count 4 --seed 42
```

## Exam mode with an optional timer

Exam mode postpones corrections until the session ends. --minutes adds an optional timer, including time spent reading feedback in practice mode. Terminal input is synchronous: when time expires, press Enter. The program checks elapsed time after input and rejects late answers; it does not interrupt a blocked input prompt. Quitting or reaching the limit leaves remaining questions unanswered, and they still count in the total. The result is a study aid, not an official score or a prediction of passing.

```bash
python tools/quiz.py run --lang en --mode exam --count 8 --minutes 12 --report .study-reports/first-quiz.json
```

## Review mistakes

Each session saves its questions, option order, selected answers, explanations, and references in a UTF-8 JSON report. Review uses those snapshots even if the question bank changes later. By default it shows wrong and unanswered questions; --all also includes correct ones. The summary shows the result per topic to guide your next reading. --json prints recomputed totals. Review --lang changes interface labels; saved questions keep their original language. Microsoft Learn sources link to their English originals; browser translations may be available.

```bash
python tools/quiz.py review --lang en --report .study-reports/first-quiz.json
python tools/quiz.py review --lang en --report .study-reports/first-quiz.json --all
python tools/quiz.py review --lang en --report .study-reports/first-quiz.json --json
```

## Personal reports

Default reports live in .study-reports/, excluded from Git. Every session gets a new filename; existing reports are never replaced. --report selects a custom path: keep custom reports outside version control yourself. Reports contain timestamps and selected options, not free-text answers or Azure credentials. No telemetry or network requests. Q, end-of-input, and Ctrl+C during questioning preserve completed choices in the final report. A forced termination or storage failure can still prevent saving; reports are saved at session end, not after every answer. Progress remains independent of the self-rating trainer.

## What the result means

Eight questions cannot cover a certification syllabus. Use the longer case banks, workbooks, and labs to justify decisions beyond choosing an option. Sources support the reasoning; they are not claims of full exam coverage. The doctor command checks structure, language coverage, matching answer indices, and local references; it does not verify translation quality or remote page availability. Imported reports are validated and their totals recomputed, but are editable personal files, not signed proof of an assessment.

```bash
python tools/quiz.py doctor --lang en
```

[CLI](../QUIZ.md) · [Read the questions on GitHub](20-quiz-cases.md) · [Microsoft Learn](../QUIZ-SOURCES.md)
