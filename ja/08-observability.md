# 監視とトラブルシューティング

[目次](README.md) · [認定試験](../certifications/ja/README.md)

メトリック、ログ、トレースは別の情報を示します。Azure Monitor が監視機能を提供し、Application Insights がアプリを観測します。Log Analytics では収集されたログを KQL で調べます。

CPU が低くても DB 待ちで遅いことがあります。平均だけでなく分布、パーセンタイル、件数を見ます。少数の標本を過大評価しません。

アラートには信号、しきい値、期間、対処を定義します。Service Health と Resource Health の対象も区別します。

**方法：**影響と開始時刻、直前の変更、要求と依存先、仮説の検証、修正後の確認という順で進めます。トークンや文書全文をログに残さず、保持期間と費用も管理します。

---

[←](07-governance.md) · [→](09-costs.md) · [English](../en/08-observability.md)

## Microsoft Learn の補足 · dcr

DCR は対応する収集とルーティングを定義し、変換でデータを絞ったり変更したりできます。すべての diagnostic settings の代わりではありません。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview) · [Microsoft Learn の補足](15-microsoft-learn.md#learn-dcr)
