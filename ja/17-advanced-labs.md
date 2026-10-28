# 発展演習

[←](README.md) · [共通学習コア](16-common-core.md)

八言語で同じ三つの演習です。シミュレーションはローカル、残りは試験用サブスクリプション、Azure CLI、権限が必要です。ここでは Azure で未実行です。資源と保持に費用が生じ得ます。ルートから実行し先に削除手順を読みます。

<a id="advanced-lab-1"></a>

## 1. 復元前後のバイト比較

専用グループとアカウントだけを作ります。テンプレートは versioning と階層 namespace を無効にし、版の昇格なしで undelete します。Blob/コンテナーを七日保持し、共有キーと公開 Blob を無効化しますが認証付き公開ネットは残ります。

管理権限と、この account の Storage Blob Data Contributor などのデータ権限が必要です。自動付与はしません。反映を待ち、全体 Owner は与えません。

新コンテナーに合成テキストを書き、その Blob だけ削除、復元、比較します。期待は RECOVERY_OK。そのコンテナーも削除しますが保持は残り得ます。失敗段階を秘密なしで記録し、本番設定を変えません。

[Bicep](../labs/protected-storage.bicep) · [Script](../labs/blob-recovery.sh)

```bash
az login
export LAB_SUBSCRIPTION='REPLACE_WITH_TEST_SUBSCRIPTION_ID'
az account show --subscription "$LAB_SUBSCRIPTION" --query '{name:name,id:id}' -o table
export LAB_RG="rg-notes-recovery-$(date -u +%Y%m%d%H%M%S)"
export LAB_STORAGE="notes$(date -u +%y%m%d%H%M%S)$RANDOM"
az group create --name "$LAB_RG" --location westeurope \
  --subscription "$LAB_SUBSCRIPTION" --tags environment=lab project=notes-recovery

az deployment group what-if --resource-group "$LAB_RG" \
  --subscription "$LAB_SUBSCRIPTION" --template-file labs/protected-storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

# Review proposed changes before running create.
az deployment group create --resource-group "$LAB_RG" \
  --subscription "$LAB_SUBSCRIPTION" --template-file labs/protected-storage.bicep \
  --parameters storageAccountName="$LAB_STORAGE"

# Run after the required data permissions have been provided.
bash labs/blob-recovery.sh
```

<a id="advanced-lab-2"></a>

## 2. 付与せず調べる

資源 ID と principal の object ID を使い、client ID と混同しません。スクリプトはその principal の割り当てと継承範囲を読むだけです。グループ、条件、拒否、一時有効化、データ/ネット制御を含む完全な有効権限計算ではありません。

Role、scope、condition、必要操作を提出します。空の一覧でも全アクセスなしとは言えません。表示のための権限付与はしません。

[Script](../labs/inspect-access.sh)

```bash
export LAB_SCOPE=$(az storage account show --name "$LAB_STORAGE" \
  --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" --query id -o tsv)
export LAB_PRINCIPAL_ID='REPLACE_WITH_PRINCIPAL_OBJECT_ID'
bash labs/inspect-access.sh
```

<a id="advanced-lab-3"></a>

## 3. 応答消失を模擬する

ネット、秘密、cloud は不要です。SQLite 保存後、最初の応答が消え再試行します。三回指定では naive が二文書、idempotent が一文書、permanent は書込も再試行もありません。待機時間は計算だけです。

一回では成功確認がなくても書込が残り得ます。例外と未実行は同じではありません。七つのローカル試験は挙動と保護を確認し、Azure 可用性を保証しません。

[Simulator](../labs/retry_lab.py)

```bash
python labs/retry_lab.py --attempts 3
python labs/retry_lab.py --attempts 1
python -m unittest discover -s tools -p 'test_*lab*.py' -v
```

<a id="advanced-lab-4"></a>

## 4. 清掃と提出

専用グループを一覧確認し、削除に同意して false を確認します。コンテナー削除でも保持が終わるとは限りません。エラーとロックを調べ、共有資源を purge しません。

期待、観測、権限、比較、ロール解釈、模擬出力を提出し、ローカルと cloud を区別します。



```bash
case "$LAB_RG" in
  rg-notes-recovery-*) ;;
  *) echo "Not a dedicated recovery lab group"; exit 2 ;;
esac
az resource list --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" -o table
az group delete --name "$LAB_RG" --subscription "$LAB_SUBSCRIPTION"
az group exists --name "$LAB_RG" --subscription "$LAB_SUBSCRIPTION"
```

[Microsoft Learn: Blob soft delete](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-enable) · [Restore](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-manage) · [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-cli)
