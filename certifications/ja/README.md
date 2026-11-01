# 認定資格：12 の学習ルート

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

[一般ノート](../../ja/README.md) · [出典一覧](../../CERTIFICATION-SOURCES.md)

12 の試験ルートに、それぞれ判断の理由を学ぶガイド、解答つきの独自ケース 10 問、成果物を確認する 5 単元のワークブックを用意した。まず理解したい分野から選ぼう。

| ルート | 分野 | ガイド | ケース | ワークブック |
|---|---|---|---|---|
| AZ-900 | Azure の基礎 | [読む](AZ-900.md) | [10 ケース](AZ-900-cases.md) | [5 単元](AZ-900-workbook.md) |
| AZ-104 | Azure の管理 | [読む](AZ-104.md) | [10 ケース](AZ-104-cases.md) | [5 単元](AZ-104-workbook.md) |
| AZ-305 | ソリューション設計 | [読む](AZ-305.md) | [10 ケース](AZ-305-cases.md) | [5 単元](AZ-305-workbook.md) |
| AZ-400 | デリバリーと DevOps | [読む](AZ-400.md) | [10 ケース](AZ-400-cases.md) | [5 単元](AZ-400-workbook.md) |
| DP-900 | データの基礎 | [読む](DP-900.md) | [10 ケース](DP-900-cases.md) | [5 単元](DP-900-workbook.md) |
| SC-900 | セキュリティ・ID・コンプライアンス | [読む](SC-900.md) | [10 ケース](SC-900-cases.md) | [5 単元](SC-900-workbook.md) |
| AZ-700 | Azure ネットワーク | [読む](AZ-700.md) | [10 ケース](AZ-700-cases.md) | [5 単元](AZ-700-workbook.md) |
| DP-300 | Azure SQL の管理 | [読む](DP-300.md) | [10 ケース](DP-300-cases.md) | [5 単元](DP-300-workbook.md) |
| AI-901 | Microsoft Foundry の AI | [読む](AI-901.md) | [10 ケース](AI-901-cases.md) | [5 単元](AI-901-workbook.md) |
| SC-200 | セキュリティ運用 | [読む](SC-200.md) | [10 ケース](SC-200-cases.md) | [5 単元](SC-200-workbook.md) |
| SC-300 | ID とアクセス管理 | [読む](SC-300.md) | [10 ケース](SC-300-cases.md) | [5 単元](SC-300-workbook.md) |
| AZ-140 | Azure Virtual Desktop | [読む](AZ-140.md) | [10 ケース](AZ-140-cases.md) | [5 単元](AZ-140-workbook.md) |

## どこから始めるか

AZ-900 で全体像をつかむ。DP-900 は DP-300 に進む前のデータと処理の基礎になる。SC-900 は Azure に加えて Microsoft 365 のセキュリティ、ID、コンプライアンスも扱う。AZ-104 は AZ-700 の運用の土台となり、AZ-305 と AZ-400 は設計とデリバリーを深める。これは学習順の提案で、公式の受験要件ではない。

## 今回の追加内容

DP-900、SC-900、AZ-700、DP-300 は、8 言語で対応する解説・ケース・成果物をそろえた。他ルートの以前の補足ノートは長さが異なる。各言語 120 シナリオ、全体で 960 の言語版がある。実際の試験問題ではない。

## トレーナーで復習

自己評価トレーナーで 12 ルートを選び、ケースを Anki に書き出せる。自分の説明を解答と比べ、思い出せた度合いを評価する。選択式ミニクイズは、従来の 4 ルートに関する 8 問のままである。

```bash
python tools/study.py demo --lang ja --exam AI-901
python tools/study.py study --lang ja --exam SC-200 --limit 5
python tools/study.py export --lang ja --exam SC-300 --output exports/ja-sc300.tsv
```

## 出典と範囲

以前の参照日は 2026 年 10 月 27 日、今回の 4 ルートは 2026 年 10 月 30 日。予約前に Microsoft Learn で目標、提供状況、試験言語、要件を確認しよう。試験コードと認定資格は異なり、Expert 資格には別の資格が必要な場合がある。合格や Azure での実行を保証・主張するものではない。

[トレーナー](../../ja/18-study-trainer.md) · [ミニクイズ](../../ja/19-mini-quiz.md) · [Anki](../../flashcards/ja.tsv) · [ネットワーク演習](network-lab.md) · [ADR](ADR-template.md)

## AI・運用・ID・仮想デスクトップ

AI-901、SC-200、SC-300、AZ-140 に、ガイド・10 ケース・5 単元を各ルートの 8 言語版で追加した。AI-901 は Microsoft Foundry での実装、SC-200 は調査と対応、SC-300 は Entra の詳細、AZ-140 は仮想デスクトップとアプリを扱う。これら 4 ルートの出典確認日は 2026 年 11 月 1 日。
