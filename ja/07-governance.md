# ガバナンスとコンプライアンス

[目次](README.md) · [認定試験](../certifications/ja/README.md)

RBAC は誰が操作できるか、Policy はリソースが満たす条件を扱います。VM 作成権限があってもリージョン制限で拒否されます。

Audit は報告、Deny は対象要求を拒否します。Modify と DeployIfNotExists には適切な設定や権限が必要で、既存リソースには修復タスクが必要な場合があります。

タグは分類用で、セキュリティ境界ではありません。常に自動継承されるわけでもありません。管理ロックも全データ操作やバックアップの代わりにはなりません。

**演習：**まず監査で影響を把握し、所有者と例外の理由を決めてから拒否を検討します。プロバイダーの認証だけで自分のアプリが準拠するわけではありません。

---

[←](06-identity.md) · [→](08-observability.md) · [English](../en/07-governance.md)

## Microsoft Learn の補足 · policy

修復タスクは既存リソースに modify または deployIfNotExists を適用し、割り当ての ID と権限を使います。定義変更で全権限が自動更新されるわけではありません。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources) · [Microsoft Learn の補足](15-microsoft-learn.md#learn-policy)
