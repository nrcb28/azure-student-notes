# ストレージとデータ

[目次](README.md) · [認定試験](../certifications/ja/README.md)

PDF は Blob Storage、共有ファイルは Azure Files、VM のディスクは Managed Disks が候補です。関係やトランザクションが必要ならリレーショナル DB を検討します。JSON を送るだけで文書 DB に決まるわけではありません。

LRS はローカル、ZRS はゾーン間で複製します。GRS/GZRS の地域間複製は非同期なので、新しい書き込みがまだ複製されていない可能性があります。

冗長化とバックアップは別です。削除も複製され得ます。バージョン、論理削除、保持期間を設計します。

**例：**PDF だけ戻してもメタデータがなければ不整合です。ファイルと DB の整合性まで確認します。SAS は資格情報として保護し、権限と期限を限定します。

---

[←](03-compute.md) · [→](05-networking.md) · [English](../en/04-storage.md)

## Microsoft Learn の補足 · sas

Blob の user delegation SAS は、Entra ID で取得する委任キーを使います。取得権限が必要で、URL を知っているだけでは発行できません。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli) · [Microsoft Learn の補足](15-microsoft-learn.md#learn-sas)

## Blob の保護レベルを分ける

論理削除は設定済みの保持期間中に削除オブジェクトを保存します。それだけでコンテナーやアカウント全体の削除を保護するわけではありません。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview) · [Blob の保護レベルを分ける](15-microsoft-learn.md#learn-blob-recovery)
