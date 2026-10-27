# 实验 · Azure CLI / Bicep

[目录](README.md)

使用 Bash、Azure CLI、Bicep 和测试订阅。可能创建真实资源并产生费用。这些实验未在 Azure 实际运行。除资源组和资源管理权限外，Blob 操作还需要适当作用域的数据角色，例如 Storage Blob Data Contributor。不要通过给整个订阅授予 Owner 来绕过问题。先阅读清理步骤，从仓库根目录执行代码。

## 1. 检查订阅

替换为自己的测试订阅 ID，核对名称与 ID。创建专用组，并在同一 shell 保留变量。确认区域符合订阅要求。

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

## 2. 验证并创建配置

[storage.bicep](../labs/storage.bicep) 创建 Standard_LRS，要求 HTTPS，关闭匿名 Blob 与共享密钥。公共网络仍开启，但必须验证身份。不创建 private endpoint、备份或 RBAC。编译只检查语法，validate 与 what-if 需要远程环境。阅读变更后再创建，检查 publicBlobs 和 sharedKey 为 false。

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

## 3. 使用身份创建容器

缺少数据角色时，只申请必要作用域的权限，等待传播。auth-mode login 使用 CLI 身份，不获取账户密钥。确认列表出现 notes。遇到403要检查授权和服务控制，不要无原因开放网络。

```bash
az storage container create --account-name "$LAB_STORAGE" \
  --name notes --auth-mode login --public-access off

az storage container list --account-name "$LAB_STORAGE" \
  --auth-mode login --query '[].name' --output table
```

## 4. 删除专用组

核对资源列表。此操作删除组内所有资源，只对本实验新建的组执行。响应 CLI 确认并等待完成。

```bash
az resource list --resource-group "$LAB_RG" --output table
az group delete --name "$LAB_RG"
```

## 5. 确认删除

期望结果为 false。否则检查锁、错误和权限，不要未经确认就认为清理完成。

```bash
az group exists --name "$LAB_RG"
```
