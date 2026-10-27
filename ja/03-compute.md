# コンピューティングとコンテナー

[目次](README.md) · [認定試験](../certifications/ja/README.md)

OS の制御が必要なら VM、対応する Web/API なら App Service、イベントで動く処理なら Functions を検討します。Container Instances と Container Apps は、独自の Kubernetes クラスターを管理せずにコンテナーを動かす選択肢です。AKS は要件が運用負担を正当化するときに選びます。

コンテナーは完全な VM ではありません。Serverless にも起動、時間、接続、料金の条件があります。

**診断：**起動成功だけで完了としません。ポート、プロセス、設定、ログ、正常性チェック、依存先まで通る要求を確認します。イメージに秘密を埋め込まず、設定を分けます。変更できる latest より、識別できるバージョンの方が再現に役立ちます。

---

[←](02-resources.md) · [→](04-storage.md) · [English](../en/03-compute.md)

## Microsoft Learn の補足 · slots

Slot には独自の名前と実行中のアプリがあります。設定コピーは内容、プライベート接続、全依存先の複製ではありません。Swap は準備と warm-up を含みます。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) · [Microsoft Learn の補足](15-microsoft-learn.md#learn-slots)
