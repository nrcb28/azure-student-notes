# 演習 · Azure CLI / Bicep

[目次](README.md)

Bash、Azure CLI、Bicep と試験用サブスクリプションを使います。実リソースと費用が生じ得ます。これらの演習は Azure で実行済みではありません。グループとリソースの管理権限に加え、Blob 操作には必要な範囲の Storage Blob Data Contributor などが必要です。権限不足を Owner の一括付与で解決しないでください。最初に削除手順まで読み、コードはリポジトリのルートから実行します。

## 1. サブスクリプションを確認

プレースホルダーを自分の試験用 ID に置き換え、名前と ID を確認します。専用グループを作り、変数を同じ shell に保持します。地域の許可条件も確認します。

```bash
az login
az account list --output table

# Replace this value before continuing.
AZURE_LAB_SUBSCRIPTION='REPLACE_WITH_TEST_SUBSCRIPTION_ID'
az account set --subscription "$AZURE_LAB_SUBSCRIPTION"
az account show --query '{name:name,id:id}' --output table

LAB_RG="rg-notes-lab-$(date -u +%Y%m%d%H%M%S)"
LAB_LOCATION='westeurope'
az group create --name "$LAB_RG" --location "$LAB_LOCATION" \
  --tags project=notes-app environment=lab

# Confirm this is a newly created, empty group.
az resource list --resource-group "$LAB_RG" --output table
```

## 2. 構成を検証して作成

[storage.bicep](../labs/storage.bicep) は Standard_LRS を作り、HTTPS を要求し、匿名 Blob と共有キーを無効にします。公開ネットワークは有効でも認証が必要です。Private endpoint、バックアップ、RBAC は作りません。コンパイルは構文、validate と what-if はリモート検査です。変更を読んでから作成し、publicBlobs と sharedKey が false か確認します。

```bash
# 22 lowercase alphanumeric characters; must be globally unique.
LAB_STORAGE="notes$(date -u +%y%m%d%H%M%S)$(printf '%05d' "$RANDOM")"

az bicep build --file labs/storage.bicep --stdout > /dev/null

az deployment group validate --resource-group "$LAB_RG" \
  --template-file labs/storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

az deployment group what-if --resource-group "$LAB_RG" \
  --template-file labs/storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

# Continue after reviewing the proposed changes.
az deployment group create --resource-group "$LAB_RG" \
  --template-file labs/storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

az storage account show --resource-group "$LAB_RG" --name "$LAB_STORAGE" \
  --query '{name:name,publicBlobs:allowBlobPublicAccess,sharedKey:allowSharedKeyAccess}' \
  --output table
```

## 3. ID でコンテナーを作成

不足するデータロールは必要範囲だけに付与してもらいます。反映に時間がかかる場合があります。auth-mode login は CLI の ID を使い、キーを取得しません。notes が一覧に出ることを確認します。403 なら権限とサービス制御を調べ、理由なくネットワークを開きません。

```bash
az storage container create --account-name "$LAB_STORAGE" \
  --name notes --auth-mode login --public-access off

az storage container list --account-name "$LAB_STORAGE" \
  --auth-mode login --query '[].name' --output table
```

## 4. 専用グループの削除

一覧を確認します。この操作はグループ内のすべてを削除します。演習用に作ったグループだけを指定し、CLI の確認に応答して完了を待ちます。

```bash
az resource list --resource-group "$LAB_RG" --output table
az group delete --name "$LAB_RG"
```

## 5. 削除を確認

false が期待値です。異なるならロック、エラー、権限を調べます。実際の削除を確かめずに終えません。

```bash
az group exists --name "$LAB_RG"
```
