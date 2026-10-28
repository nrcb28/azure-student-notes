# AZ-400 · 共通の発展ワークブック

[←](README.md) · [共通学習コア](../../ja/16-common-core.md) · [発展演習](../../ja/17-advanced-labs.md)

八言語で目標、ケース、提出物を対応させています。同等性は語数ではなく学習単位と検証する証拠で確認します。以前のガイドも補足説明として残します。

<a id="az-400-unit-1"></a>

## 1. 追跡と Git

必要性、issue、PR、commit、build、成果物、配置を関連付けます。指標境界を揃え、行や commit 数で人を評価しません。公開頻度と保守版で branch を選びます。

**ケース：**共有公開版の取消。**証拠：**revert と履歴書換え、データへの影響。秘密の露出はまず失効や更新を行います。

<a id="az-400-unit-2"></a>

## 2. 試験と成果物

一度 build し識別済みの結果を昇格します。版、digest、元を記録します。リスク別に試験を組み合わせ、coverage を良い assertion の保証とみなしません。

**ケース：**コード不変で昨日だけ成功。**証拠：**固定されない道具、依存、基本 image を調査。不安定試験を成功まで繰り返して隠さず、cache と成果物を分けます。

<a id="az-400-unit-3"></a>

## 3. Runner の ID と境界

信頼コード、PR 入力、workflow 権限、cloud 範囲を分けます。自前 runner は隔離、更新、清掃が必要です。OIDC にも精密な信頼と認可が残ります。

**ケース：**外部 PR が内部実行 script を変更。**証拠：**本番アクセスのない実行、ID 制限、リソース制御。Pipeline コードは無害とは限りません。

<a id="az-400-unit-4"></a>

## 4. 公開と回復

Rolling、blue-green、canary、rings、flag を比較します。対象、機能信号、観測時間、停止基準を定めます。Swap は全依存を隔離しません。対応可能なら後方互換移行を設計します。

**ケース：**CPU 正常で結果が誤り。**証拠：**業務信号と rollback 条件。旧 image で削除列が戻らない理由も説明します。

<a id="az-400-unit-5"></a>

## 5. 運用を閉じる

Context と版を telemetry へ渡し、記録データを保護します。警告担当と期間を定めます。Resource approval は編集可能な YAML 条件だけではありません。

**提出：**全 pipeline、意味のある試験、固定成果物、昇格設計。ローカル simulator を別 retry 設定で再実行。Postmortem に対策、担当、検証を付けます。

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400) · [AZ-400](AZ-400.md)
