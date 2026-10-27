# ID とセキュリティ

[目次](README.md) · [認定試験](../certifications/ja/README.md)

認証は本人確認、認可は許可する操作の判断です。MFA は認証を強くしますが、文書への権限を付与しません。

Azure RBAC は ID、ロール、スコープの組み合わせです。Reader は参照、Contributor は管理、Owner はアクセスの付与も可能です。ディレクトリのロールとリソースのロールは区別します。

マネージド ID は自分で保存するアプリ資格情報を減らしますが、権限は必要です。Key Vault はシークレット、鍵、証明書を扱います。

**例：**Reader を外してもアクセスできるなら、グループと継承された割り当てを確認します。ログイン済み学生でも、他人の文書を変更できないようアプリ側の認可が必要です。

---

[←](05-networking.md) · [→](07-governance.md) · [English](../en/06-identity.md)

## Microsoft Learn の補足 · sas

Blob の user delegation SAS は、Entra ID で取得する委任キーを使います。取得権限が必要で、URL を知っているだけでは発行できません。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli) · [Microsoft Learn の補足](15-microsoft-learn.md#learn-sas)

## 証拠に基づく RBAC 診断

リソース管理はロール付与やデータアクセスと同じではありません。適切な操作と範囲が必要で、条件が付与先やロールを制限する場合があります。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting) · [証拠に基づく RBAC 診断](15-microsoft-learn.md#learn-rbac-diagnosis)

## Key Vault と依存先の復旧

論理削除は保持期間内の復旧を支援します。Vault を戻しても RBAC 割り当てや Event Grid サブスクリプションなどが自動復旧するわけではありません。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview) · [Key Vault と依存先の復旧](15-microsoft-learn.md#learn-vault-recovery)
