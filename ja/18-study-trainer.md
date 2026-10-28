# Azure 不要の学習トレーナー

[←](README.md) · [Anki](../flashcards/ja.tsv)

各言語40ケース、認定ごとに10ケースを練習します。Python3.9以降と標準ライブラリだけで動き、利用時のクラウド契約、追加パッケージ、通信は不要です。

```bash
python tools/study.py demo --lang ja --exam AZ-104
python tools/study.py study --lang ja --exam AZ-104 --limit 5
```

## 1. 自分で答える

問題を読み、考えて Enter。説明と比較し、0忘れた・1難しい・2良い・3簡単で評価します。qで終了し、完了した評価は保存されます。自己評価であり、自動採点や認定点数ではありません。

## 2. 苦手を復習

通常は期限到来を優先し、新規も出します。weakは難しい評価や過去の忘却、randomは混合です。進捗は言語別で、書いた回答は保存しません。

## 3. 進捗と計画

statsは新規、期限、定着、忘却を試験別に表示します。定着は連続二回2以上という目安で、合格準備の証明ではありません。planは一ケース約四分の案で、実際の期限予測ではありません。

## 4. 間隔

0は十分後に戻り連続回数をリセット。1は翌日でリセット。2は一日、三日、その後倍増。3は四日から2.5倍、最大365日。独自の簡単な規則で、FSRSや記憶保証ではありません。

## 5. Anki へ

準備済みデッキを取得するか選択出力します。UTF-8で問題、説明、タグの三列です。Anki進捗は独立し、取込プレビューと列対応を確認します。

## 6. 自分のデータ

既定の.study-progress.jsonはGit対象外です。--progressで場所を変更できます。アトミック書込と同時セッション保護を使い、破損JSONを上書きしません。履歴移動にはコピーを保管します。

```bash
python tools/study.py study --lang ja --mode weak --limit 5
python tools/study.py stats --lang ja
python tools/study.py plan --lang ja --days 7 --minutes 20
python tools/study.py export --lang ja --exam AZ-104 --output exports/ja-az104.tsv
python tools/study.py doctor --lang ja
```

[CLI reference](../TRAINER.md) · [Anki decks](../flashcards/README.md)
