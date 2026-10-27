# Microsoft Learn から学ぶ実践的な補足

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

出典確認日：2026年10月27日。公式説明を学習用に書き直し、独自のケースを加えました。以下の確認は Azure で実行済みではありません。

<a id="learn-sas"></a>

## 1. Entra ID による SAS

Blob の user delegation SAS は、Entra ID で取得する委任キーを使います。取得権限が必要で、URL を知っているだけでは発行できません。

**例：**PDF を短時間ダウンロードさせるなら、対象、読み取り権限、期限を限定します。ログに URL を残さず、期限、認可、ネットワークを分けて診断します。漏えい時の失効方法は SAS の種類に合わせます。

[Microsoft Learn · Storage: user delegation SAS](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

<a id="learn-dns"></a>

## 2. プライベート DNS を追う

クライアントはサービス名を private endpoint の IP に解決する必要があります。インターフェイス作成だけで全 resolver は設定されません。適切なゾーンはサービスごとに違います。

**例：**VM では成功し大学から失敗するなら、回答、ゾーンリンク、転送、経路を比較します。公開ゾーン全体を不用意に置き換えず、IP をコードに固定しません。名前解決はデータ権限を与えません。

[Microsoft Learn · Private endpoint DNS](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

<a id="learn-policy"></a>

## 3. 評価と修復を分ける

修復タスクは既存リソースに modify または deployIfNotExists を適用し、割り当ての ID と権限を使います。定義変更で全権限が自動更新されるわけではありません。

**例：**古い設定が非準拠なら効果、範囲、ID、ロールを確認し、小さい対象で修復します。Deny を万能な変換機能とみなしません。

[Microsoft Learn · Policy remediation](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

<a id="learn-dcr"></a>

## 4. DCR と収集経路

DCR は対応する収集とルーティングを定義し、変換でデータを絞ったり変更したりできます。すべての diagnostic settings の代わりではありません。

**例：**VM イベントがなければ、agent、関連付け、入力、flow、出力、schema を確認します。全件送信は費用と露出を増やし、絞り過ぎると調査の証拠が消えます。

[Microsoft Learn · Azure Monitor data collection rules](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview)

<a id="learn-whatif"></a>

## 5. What-if の限界

What-if は変更を適用せず予測します。権限、式、依存関係により分析できない部分があります。不完全な結果は変更なしの証明ではありません。

**例：**Ignore や未評価モジュールを NoChange と扱わず、診断を読み分離します。コンパイル、検証、予測、実行後試験を分け、未分析部分もレビューします。

[Microsoft Learn · Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

<a id="learn-slots"></a>

## 6. Slot は動くアプリ

Slot には独自の名前と実行中のアプリがあります。設定コピーは内容、プライベート接続、全依存先の複製ではありません。Swap は準備と warm-up を含みます。

**例：**staging が本当のメールを送るなら、接続、ID、固有設定、起動処理を確認します。ユーザートラフィックがゼロでも処理は走れます。逆 swap でも破壊的 DB 移行は戻りません。

[Microsoft Learn · App Service deployment slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)

<a id="learn-landing"></a>

## 7. Landing zone の責任分担

Landing zone は ID、接続、管理、ガバナンスの土台を組織します。基盤とワークロードの担当は分かれ得ます。Accelerator は要件の代わりではありません。

**例：**五学部でネットワークを共有するなら、所有者、境界、権限、方針、費用を決めます。小さい演習へ大企業向け構成を理由なくコピーしません。

[Microsoft Learn · Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)

<a id="learn-checks"></a>

## 8. Checks と公開権限

Azure Pipelines のリソース所有者は YAML 外で approvals と checks を管理します。段階開始前に利用リソースの検査を満たす必要があります。

**例：**独立レビューと公開時間帯を定め、対象、承認者、期限、拒否を設定します。変更と期限切れも試します。緑の pipeline は全 service connection の利用許可ではありません。

[Microsoft Learn · Azure Pipelines approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops)

---

[Source register](../LEARN-SOURCES.md) · [Attribution](../ATTRIBUTION.md)

<a id="learn-blob-recovery"></a>

## 9. Blob の保護レベルを分ける

論理削除は設定済みの保持期間中に削除オブジェクトを保存します。それだけでコンテナーやアカウント全体の削除を保護するわけではありません。

**例：**ノートのコンテナーを削除した場合、Blob の保護だけで復旧可能とは言えません。事前にコンテナー保護と必要なバックアップを確認します。

**手順：**対象、時刻、すでに設定されていた保持、復旧用 ID を特定します。内容と権限を検証し DB メタデータと照合します。削除後に有効化しても、以前の状態が保存されていたことにはなりません。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview)

<a id="learn-retry"></a>

## 10. 制限付きの再試行と冪等性

再試行は一時的な障害向けで、無効な資格情報や要求を直しません。回数と総時間を制限し、SDK 内部の再試行も確認します。

**例：**文書保存後に応答が消えると、繰り返しで重複する可能性があります。安定した ID と整合的な結果確認が必要です。

**手順：**原因を分類し、適用される待機指示と期限を定めます。回復と回数超過を分け、秘密は記録しません。多層の再試行による実要求数を計算します。再試行の集中は過負荷を悪化させ得ます。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)

<a id="learn-rbac-diagnosis"></a>

## 11. 証拠に基づく RBAC 診断

リソース管理はロール付与やデータアクセスと同じではありません。適切な操作と範囲が必要で、条件が付与先やロールを制限する場合があります。

**例：**割り当てボタンが無効なら、Owner を求める前にアカウント、テナント、範囲、割り当て権限を確認します。

**手順：**失敗操作、実 ID、リソースを記録します。グループ、直接と継承、条件、管理面とデータ面を確認します。反映と認証更新も考え、失敗した最小操作を再検査して理由を残します。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting)

<a id="learn-vault-recovery"></a>

## 12. Key Vault と依存先の復旧

論理削除は保持期間内の復旧を支援します。Vault を戻しても RBAC 割り当てや Event Grid サブスクリプションなどが自動復旧するわけではありません。

**例：**Vault が見えても API が読めないなら、ID、権限、利用側設定を確認します。

**手順：**対象と利用側を棚卸しし、保護を事前に準備します。復旧と purge を分けます。許可された purge は対象を戻す選択肢を失わせるため、場当たり的な掃除に使いません。制限と保護も確認し、正当な利用側の完全な要求で検証します。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview)
