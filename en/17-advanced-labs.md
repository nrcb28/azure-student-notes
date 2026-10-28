# Advanced labs

[←](README.md) · [Common study core](16-common-core.md)

Three labs follow the same procedure in all eight languages. Simulation is local; the others require a test subscription, Azure CLI, and suitable permissions. They have not been run against Azure here. Resources and retained data can incur costs. Run from the root and read cleanup first.

<a id="advanced-lab-1"></a>

## 1. Recover a file and compare bytes

Create only the dedicated group and account below. The template disables versioning and hierarchical namespace so this exercise uses undelete without version promotion. It enables seven-day blob/container soft delete, disables shared keys and public blobs, and retains an authenticated public endpoint.

Deployment needs management permissions; data operations need an appropriate role such as Storage Blob Data Contributor for your identity on this account. The template grants no roles. Allow propagation where needed; do not grant subscription-wide Owner.

The script creates a new container, uploads synthetic text, deletes only that blob, restores it, and compares content. Expect RECOVERY_OK. It then deletes its container; retained data may remain. Record failing phase and error without secrets. Do not modify production protection.

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

## 2. Inspect assignments without granting roles

Get the resource ID and supply the principal object ID, not client ID. The script only reads and filters assignments to that principal, including inherited scopes. It is not a complete effective-access calculation: groups, conditions, denials, temporary activation, and data/network controls need separate analysis.

Submit role, scope, condition, and desired action. Empty output does not establish absence of all access. Do not create assignments just to obtain output.

[Script](../labs/inspect-access.sh)

```bash
export LAB_SCOPE=$(az storage account show --name "$LAB_STORAGE" \
  --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" --query id -o tsv)
export LAB_PRINCIPAL_ID='REPLACE_WITH_PRINCIPAL_OBJECT_ID'
bash labs/inspect-access.sh
```

<a id="advanced-lab-3"></a>

## 3. Simulate a lost response

No network, credentials, or cloud resources. SQLite stores a document and the first attempt loses its response. The client retries. With three attempts, expect naive to store two documents, idempotent one, and permanent to neither write nor retry. Delays are calculated, not slept.

One attempt can leave a write without confirmed success. Explain why an exception does not mean no operation occurred. Seven local tests verify behaviour and script guards, not Azure availability.

[Simulator](../labs/retry_lab.py)

```bash
python labs/retry_lab.py --attempts 3
python labs/retry_lab.py --attempts 1
python -m unittest discover -s tools -p 'test_*lab*.py' -v
```

<a id="advanced-lab-4"></a>

## 4. Cleanup and submission

List the dedicated group and confirm deletion when prompted. It should finish with false. Container deletion does not establish expiry of all retained data. Check errors and locks; never purge shared resources.

Submit expected and observed results, permission used, content comparison, role interpretation, and simulator output. Separate local verification from cloud testing.



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
