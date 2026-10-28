# 进阶实验

[←](README.md) · [共同学习核心](16-common-core.md)

八语版本具有相同三个实验。模拟器本地运行，其他需要测试订阅、Azure CLI 和权限，未在这里实际运行 Azure。资源和保留数据可能收费。从根目录执行，先读清理。

<a id="advanced-lab-1"></a>

## 1. 恢复并比较字节

只创建专用组和账户。模板关闭 versioning 与分层 namespace，使 undelete 无需提升版本；Blob/容器软删除保留七天，禁用共享密钥和匿名 Blob，保留需验证的公共网络。

需要管理权限和此账户适当的数据角色，如 Storage Blob Data Contributor。模板不分配角色，等待传播，不授予订阅级 Owner。

脚本创建新容器、写入合成文本，只删除这个 Blob，再恢复并比较。预期 RECOVERY_OK，随后删除本次容器，但仍可能有保留数据。记录失败阶段，不泄漏秘密或修改生产保护。

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

## 2. 只检查不授权

使用资源 ID 和 principal object ID，不是 client ID。脚本只读取该主体的分配，包含继承作用域；不是完整有效访问计算。组、条件、拒绝、临时激活以及数据/网络控制需另外分析。

提交角色、范围、条件和目标操作。空输出不证明完全没有访问，也不要为了产生输出创建角色分配。

[Script](../labs/inspect-access.sh)

```bash
export LAB_SCOPE=$(az storage account show --name "$LAB_STORAGE" \
  --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" --query id -o tsv)
export LAB_PRINCIPAL_ID='REPLACE_WITH_PRINCIPAL_OBJECT_ID'
bash labs/inspect-access.sh
```

<a id="advanced-lab-3"></a>

## 3. 模拟响应丢失

不需要网络、凭据或云资源。SQLite 保存后第一次响应丢失，客户端重试。三次预算下 naive 保存两份，idempotent 一份，permanent 不写入也不重试。仅计算等待，不实际睡眠。

一次预算可能没有成功确认却已有写入。解释异常不等于操作未发生。七项本地测试检查行为及脚本保护，不证明 Azure 可用。

[Simulator](../labs/retry_lab.py)

```bash
python labs/retry_lab.py --attempts 3
python labs/retry_lab.py --attempts 1
python -m unittest discover -s tools -p 'test_*lab*.py' -v
```

<a id="advanced-lab-4"></a>

## 4. 清理与提交

列出专用组并确认删除，最后检查 false。删除容器不保证保留已到期。排查错误和锁，不 purge 共享资源。

提交预期、观察、所用权限、内容比较、角色解释和模拟结果。区分本地检查与云测试。



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
