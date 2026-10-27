# Labs: understand before deploying

These labs use Azure CLI from Bash. They have not been run against a live subscription as part of these notes. They create resources that may incur costs. They do not use passwords or automatically grant permissions.

## Prerequisites

- Azure CLI and an authorised account in a test subscription.
- Permission to create the resource group and storage account.
- For data operations, Storage Blob Data Contributor at a suitable scope. Management Contributor does not guarantee data access.
- Check subscription policies, quotas, and allowed regions.
- For Bicep, have the Azure CLI Bicep compiler available.

## 1. Check the subscription and create a group

Run from the repository root:

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

Choose a different region if your subscription requires it. Keep LAB_RG in this shell session for cleanup.

**Check:** the group exists, is tagged, and contains no resources yet.

## 2. Review and deploy storage with Bicep

[storage.bicep](../labs/storage.bicep) creates a Standard_LRS account, disables anonymous blob access, and disables shared-key authentication. Its public network endpoint remains enabled: authentication is still required. It does not configure private networking, backups, or RBAC.

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

**Expected result:** publicBlobs and sharedKey are false. Name uniqueness, policies, and regional availability can still cause failures.

Compilation checks syntax. Validate and what-if need Azure and do not prove that every later operation will succeed.

## 3. Create a private container using your identity

If you lack the data role, ask an administrator to assign Storage Blob Data Contributor at this account's scope. Do not broaden permissions across the subscription to complete the lab. Role propagation can take time.

```bash
az storage container create --account-name "$LAB_STORAGE" \
  --name notes --auth-mode login --public-access off

az storage container list --account-name "$LAB_STORAGE" \
  --auth-mode login --query '[].name' --output table
```

**Check:** notes appears. An authorisation error does not necessarily require a networking change: distinguish connectivity from data permissions.

**Question:** why use --auth-mode login? To use the Azure CLI identity without requesting an account key.

## 4. Guided troubleshooting without more resources

For a slow API, write one hypothesis for each case:

| Symptom | What I would check |
|---|---|
| Name does not resolve | DNS and private zones |
| Connection times out | Routes, NSGs, firewalls, and endpoints |
| Returns 401 | Authentication and token |
| Returns 403 | Authorisation and service access controls |
| Returns 500 | Logs, dependencies, and latest change |
| Queue keeps growing | Consumer capacity, failures, and message age |

Status codes are clues, not definitive diagnoses. A particular service may respond differently.

## 5. Cleanup

Use only the dedicated group you just created. This command deletes the group and all its resources:

```bash
az resource list --resource-group "$LAB_RG" --output table
az group delete --name "$LAB_RG"
```

Confirm when prompted by Azure CLI. After completion:

```bash
az group exists --name "$LAB_RG"
```

It should return false. If locks, permission failures, or retained resources interfere, inspect the result rather than assuming everything was deleted.

## Suggested submission

A screenshot without sensitive data and a paragraph explaining what you deployed, the permissions required, how you checked the settings, and how you cleaned up.
