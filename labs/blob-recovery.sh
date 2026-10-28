#!/usr/bin/env bash
# Only synthetic data in a dedicated lab account. No role assignments or purge.
set -euo pipefail
: "${LAB_SUBSCRIPTION:?Set the test subscription ID}"
: "${LAB_RG:?Set the dedicated recovery resource group}"
: "${LAB_STORAGE:?Set the storage account created by protected-storage.bicep}"

case "$LAB_RG" in
  rg-notes-recovery-*) ;;
  *) echo "Expected a dedicated rg-notes-recovery-* group" >&2; exit 2 ;;
esac

environment=$(az group show --name "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" --query tags.environment -o tsv)
[[ "$environment" == lab ]] || { echo "Group must carry environment=lab" >&2; exit 2; }

# Confirm ownership/location in the intended group without requesting keys.
az storage account show --name "$LAB_STORAGE" --resource-group "$LAB_RG" \
  --subscription "$LAB_SUBSCRIPTION" --query id -o tsv > /dev/null
enabled=$(az storage account blob-service-properties show --account-name "$LAB_STORAGE" \
  --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" \
  --query deleteRetentionPolicy.enabled -o tsv)
versioning=$(az storage account blob-service-properties show --account-name "$LAB_STORAGE" \
  --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" \
  --query isVersioningEnabled -o tsv)
[[ "$enabled" == true && "$versioning" == false ]] || {
  echo "Requires soft delete enabled and versioning explicitly disabled; no settings changed." >&2
  exit 2
}

scratch_dir=$(mktemp -d)
trap 'rm -rf "$scratch_dir"' EXIT
container="lab-recovery-$(date -u +%s)-$RANDOM"
created=$(az storage container create --account-name "$LAB_STORAGE" --name "$container" \
  --subscription "$LAB_SUBSCRIPTION" --auth-mode login --public-access off --query created -o tsv)
[[ "$created" == true ]] || { echo "Container already existed; stopping." >&2; exit 2; }
printf 'Synthetic university notes: recovery exercise.\n' > "$scratch_dir/original.txt"

az storage blob upload --account-name "$LAB_STORAGE" --container-name "$container" \
  --name sample.txt --file "$scratch_dir/original.txt" --auth-mode login \
  --subscription "$LAB_SUBSCRIPTION" --overwrite false -o none
az storage blob delete --account-name "$LAB_STORAGE" --container-name "$container" \
  --name sample.txt --auth-mode login --subscription "$LAB_SUBSCRIPTION" -o none
az storage blob undelete --account-name "$LAB_STORAGE" --container-name "$container" \
  --name sample.txt --auth-mode login --subscription "$LAB_SUBSCRIPTION" -o none
az storage blob download --account-name "$LAB_STORAGE" --container-name "$container" \
  --name sample.txt --file "$scratch_dir/restored.txt" --auth-mode login \
  --subscription "$LAB_SUBSCRIPTION" -o none
cmp "$scratch_dir/original.txt" "$scratch_dir/restored.txt"
printf 'RECOVERY_OK: restored bytes match original. Container: %s\n' "$container"

# Only this run's newly-created container, never a pre-existing container.
az storage container delete --account-name "$LAB_STORAGE" --name "$container" \
  --auth-mode login --subscription "$LAB_SUBSCRIPTION" -o none
printf 'Lab container deleted. Soft-deleted data may remain for retention; remove the dedicated group separately.\n'
