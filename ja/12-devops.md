# DevOps と IaC

[目次](README.md) · [認定試験](../certifications/ja/README.md)

CI は変更をビルドと検査で統合します。継続的デリバリーは公開可能な状態を保ち、継続的デプロイは条件を満たした変更を自動公開します。

検証した同じアーティファクトを昇格させます。バージョンや digest を記録し、何が動いたか追えるようにします。

Bicep は Azure リソースを記述し、Terraform の状態は保護が必要です。Plan や what-if は役立ちますが、成功を無条件には保証しません。OIDC にも信頼設定と権限が必要です。

**ロールバック：**以前のコードでは削除した DB 列は戻りません。互換性のある移行と復旧を準備します。特権 runner に未信頼コードを実行させません。ローカル検査は python tools/check_docs.py です。

---

[←](11-messaging.md) · [→](13-laboratorios.md) · [English](../en/12-devops.md)

## Microsoft Learn の補足 · whatif

What-if は変更を適用せず予測します。権限、式、依存関係により分析できない部分があります。不完全な結果は変更なしの証明ではありません。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if) · [Microsoft Learn の補足](15-microsoft-learn.md#learn-whatif)

## Microsoft Learn の補足 · slots

Slot には独自の名前と実行中のアプリがあります。設定コピーは内容、プライベート接続、全依存先の複製ではありません。Swap は準備と warm-up を含みます。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) · [Microsoft Learn の補足](15-microsoft-learn.md#learn-slots)

## Microsoft Learn の補足 · checks

Azure Pipelines のリソース所有者は YAML 外で approvals と checks を管理します。段階開始前に利用リソースの検査を満たす必要があります。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops) · [Microsoft Learn の補足](15-microsoft-learn.md#learn-checks)

## 制限付きの再試行と冪等性

再試行は一時的な障害向けで、無効な資格情報や要求を直しません。回数と総時間を制限し、SDK 内部の再試行も確認します。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) · [制限付きの再試行と冪等性](15-microsoft-learn.md#learn-retry)
