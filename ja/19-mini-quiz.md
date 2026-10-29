# ミニクイズ：選んだ理由まで復習する

[←](README.md) · [CLI](../QUIZ.md) · [GitHub で問題を読む](20-quiz-cases.md)

独自に作った 8 つのシナリオで、Azure の判断を練習する。AZ-900、AZ-104、AZ-305、AZ-400 の各学習ルートに 2 問ずつあり、8 言語で同じ内容を扱う。選択肢をシャッフルし、解説、誤答の理由、復習する章、Microsoft Learn の出典を確認できる。出典リンクは英語版を使っている。

## 始める

Python 3.9+ · es / en / it / de / fr / ru / ja / zh

```bash
python tools/quiz.py demo --lang ja
python tools/quiz.py run --lang ja --exam AZ-104 --count 2
```

## 解説つきで練習

practice モードでは、回答の直後に正解と解説を表示する。A〜D で回答し、S または Enter でスキップ、Q で終了する。試験ルートを指定したり、複数のルートを組み合わせたりできる。まず自分で理由を考えてから答えると、単なる暗記になりにくい。

```bash
python tools/quiz.py run --lang ja --exam AZ-900 --exam AZ-104 --count 4 --seed 42
```

## 任意の制限時間で模擬練習

exam モードでは、セッションが終わるまで解説を表示しない。任意で制限時間を付けられるが、入力待ちを自動で止めるタイマーではない。Enter を押した時点で時間を確認し、期限後の回答は受け付けない。スキップした問題や終了時点で答えていない問題も、結果の分母に含まれる。

```bash
python tools/quiz.py run --lang ja --mode exam --count 8 --minutes 12 --report .study-reports/first-quiz.json
```

## 間違いを復習

review は保存済みの JSON レポートを開き、初期設定では不正解と未回答を解説つきで振り返る。--all を付ければ正解も確認できる。トピック別の結果から、どの章を読み直すか決めよう。レポートには当時の問題、選択肢、回答、解説が保存されるため、問題集が更新されても過去の復習内容は変わらない。

```bash
python tools/quiz.py review --lang ja --report .study-reports/first-quiz.json
python tools/quiz.py review --lang ja --report .study-reports/first-quiz.json --all
python tools/quiz.py review --lang ja --report .study-reports/first-quiz.json --json
```

## 個人レポート

Python の標準ライブラリだけで動き、ネットワーク接続や Azure の資格情報は使わない。個人レポートは通常 .study-reports/ に保存され、このフォルダーは Git の対象外になっている。別の保存先を選んだ場合は、自分で共有範囲を確認する。既存ファイルは上書きしない。--lang は復習画面の表示を変えるが、保存された問題自体の言語は変えない。

## 結果の意味

これは 8 問の小さな演習であり、公式問題、試験全体の模擬、合格予測ではない。4 つの学習ルートの全範囲は網羅していない。同じ問題を覚えるだけで終わらず、解説の前提を確認し、出典や章の内容に戻って考え直そう。Azure へのデプロイや実際の操作能力を、この点数で確認することはできない。

```bash
python tools/quiz.py doctor --lang ja
```

[CLI](../QUIZ.md) · [GitHub で問題を読む](20-quiz-cases.md) · [Microsoft Learn](../QUIZ-SOURCES.md)
