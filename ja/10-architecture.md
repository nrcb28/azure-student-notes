# アーキテクチャと復旧

[目次](README.md) · [認定試験](../certifications/ja/README.md)

利用者、データ、要件、予算、運用能力から設計します。サービス数が多いほど良いとは限りません。

ノートアプリは API、メタデータ DB、Blob、キュー、文書処理で考えられます。ただし図だけでは本番の設定は完成しません。

RTO は復旧までの目標時間、RPO は許容する直近のデータ損失を時間で表したものです。データが戻っても DNS、権限、接続先が古ければサービスは戻りません。

タイムアウト、間隔をあけた再試行、冪等性、部分障害を考えます。復旧テストは隔離します。

**ADR：**背景、要件、代案、決定、影響、検証、見直し条件を記録します。RTO/RPO を製品名だけで保証したことにしません。

---

[←](09-costs.md) · [→](11-messaging.md) · [English](../en/10-architecture.md)

## Microsoft Learn の補足 · landing

Landing zone は ID、接続、管理、ガバナンスの土台を組織します。基盤とワークロードの担当は分かれ得ます。Accelerator は要件の代わりではありません。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) · [Microsoft Learn の補足](15-microsoft-learn.md#learn-landing)

## Blob の保護レベルを分ける

論理削除は設定済みの保持期間中に削除オブジェクトを保存します。それだけでコンテナーやアカウント全体の削除を保護するわけではありません。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview) · [Blob の保護レベルを分ける](15-microsoft-learn.md#learn-blob-recovery)

## 制限付きの再試行と冪等性

再試行は一時的な障害向けで、無効な資格情報や要求を直しません。回数と総時間を制限し、SDK 内部の再試行も確認します。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) · [制限付きの再試行と冪等性](15-microsoft-learn.md#learn-retry)

## Key Vault と依存先の復旧

論理削除は保持期間内の復旧を支援します。Vault を戻しても RBAC 割り当てや Event Grid サブスクリプションなどが自動復旧するわけではありません。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview) · [Key Vault と依存先の復旧](15-microsoft-learn.md#learn-vault-recovery)
