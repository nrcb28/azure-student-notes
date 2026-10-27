# ネットワークと接続

[目次](README.md) · [認定試験](../certifications/ja/README.md)

VNet をサブネットに分け、NSG で通信を制御します。DNS は名前を解決します。ポート許可だけではアプリが待ち受けている証明になりません。

ピアリングは自動的に推移的にはなりません。VPN Gateway は暗号化トンネル、ExpressRoute はプライベート接続です。後者が自動的にエンドツーエンド暗号化を意味するわけではありません。

Private endpoint では DNS、経路、公開アクセス設定を別々に確認します。Load Balancer は TCP/UDP、Application Gateway は地域内 Web、Front Door はグローバル Web、Traffic Manager は DNS ベースです。

**診断：**名前、IP、経路、フィルター、ポート、認証、認可の順に切り分けます。全ポートを開けて済ませないこと。

---

[←](04-storage.md) · [→](06-identity.md) · [English](../en/05-networking.md)

## Microsoft Learn の補足 · dns

クライアントはサービス名を private endpoint の IP に解決する必要があります。インターフェイス作成だけで全 resolver は設定されません。適切なゾーンはサービスごとに違います。

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) · [Microsoft Learn の補足](15-microsoft-learn.md#learn-dns)
