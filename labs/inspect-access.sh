#!/usr/bin/env bash
# Read-only, direct-principal assignments including inherited scopes.
set -euo pipefail
: "${LAB_SUBSCRIPTION:?Set the test subscription ID}"
: "${LAB_SCOPE:?Set the resource or resource-group ID}"
: "${LAB_PRINCIPAL_ID:?Set the principal object ID, not application client ID}"

[[ "$LAB_PRINCIPAL_ID" =~ ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ ]] || {
  echo "Expected UUID principal object ID" >&2; exit 2;
}
case "$LAB_SCOPE" in
  /subscriptions/"$LAB_SUBSCRIPTION"/*) ;;
  *) echo "Scope must belong to the supplied subscription" >&2; exit 2 ;;
esac
az account show --subscription "$LAB_SUBSCRIPTION" --query '{name:name,id:id,tenantId:tenantId}' -o table
az role assignment list --subscription "$LAB_SUBSCRIPTION" --scope "$LAB_SCOPE" --include-inherited \
  --query "[?principalId=='$LAB_PRINCIPAL_ID'].{role:roleDefinitionName,scope:scope,condition:condition}" -o table
printf 'Assignment inventory only: group memberships, conditions, deny assignments and data/network controls need separate analysis.\n'
