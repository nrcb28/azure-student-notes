# 演習 · VNet / NSG

[目次](README.md)

Bash、Azure CLI、Bicep と試験用サブスクリプションを使います。実リソースと費用が生じ得ます。これらの演習は Azure で実行済みではありません。グループとリソースの管理権限に加え、Blob 操作には必要な範囲の Storage Blob Data Contributor などが必要です。権限不足を Owner の一括付与で解決しないでください。最初に削除手順まで読み、コードはリポジトリのルートから実行します。

[network.bicep](../../labs/network.bicep) は VNet、二つの subnet、NSG を作り、VM、gateway、公開 IP は作りません。10.30.1.5 から 10.30.2.5 の TCP443 は優先度100で許可、TCP22 は110で拒否します。その他の VirtualNetwork からの受信も110で拒否します。これは教育用の条件で、本番へ無条件にコピーしません。

## 1. 確認して作成

```bash
az login
AZURE_NET_SUBSCRIPTION='REPLACE_WITH_TEST_SUBSCRIPTION_ID'
az account set --subscription "$AZURE_NET_SUBSCRIPTION"
az account show --query '{name:name,id:id}' --output table

NET_RG="rg-notes-network-$(date -u +%Y%m%d%H%M%S)"
NET_LOCATION='westeurope'
az group create --name "$NET_RG" --location "$NET_LOCATION" \
  --tags project=notes-app environment=lab

az bicep build --file labs/network.bicep --stdout > /dev/null

az deployment group validate --resource-group "$NET_RG" \
  --template-file labs/network.bicep

az deployment group what-if --resource-group "$NET_RG" \
  --template-file labs/network.bicep

# After reviewing proposed operations:
az deployment group create --resource-group "$NET_RG" \
  --template-file labs/network.bicep
```

## 2. 構成を確認

```bash
az network vnet subnet list --resource-group "$NET_RG" \
  --vnet-name vnet-notes-lab \
  --query '[].{name:name,prefix:addressPrefix,nsg:networkSecurityGroup.id}' \
  --output table

az network nsg rule list --resource-group "$NET_RG" \
  --nsg-name nsg-notes-lab \
  --query '[].{name:name,priority:priority,access:access,port:destinationPortRange}' \
  --output table
```

## 3. 削除して確認

```bash
az resource list --resource-group "$NET_RG" --output table
az group delete --name "$NET_RG"
az group exists --name "$NET_RG"
```

二つの subnet と data の NSG 参照、優先度100/110を確認します。カスタム規則の一覧は全有効規則と同じではありません。VM と待ち受け処理がないため、実通信は試験していません。予測、観測した構成、通信試験を区別します。専用グループの削除後は false を確認します。
