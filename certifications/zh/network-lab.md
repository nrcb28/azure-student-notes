# 实验 · VNet / NSG

[目录](README.md)

使用 Bash、Azure CLI、Bicep 和测试订阅。可能创建真实资源并产生费用。这些实验未在 Azure 实际运行。除资源组和资源管理权限外，Blob 操作还需要适当作用域的数据角色，例如 Storage Blob Data Contributor。不要通过给整个订阅授予 Owner 来绕过问题。先阅读清理步骤，从仓库根目录执行代码。

[network.bicep](../../labs/network.bicep) 创建 VNet、两个 subnet 和 NSG，不创建 VM、gateway 或公共 IP。10.30.1.5 到10.30.2.5的 TCP443由优先级100允许，TCP22由110拒绝，其他来自 VirtualNetwork 的入站流量也由110拒绝。这是教学设置，不应不经分析复制到生产。

## 1. 检查并创建

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

## 2. 验证配置

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

## 3. 删除并确认

```bash
az resource list --resource-group "$NET_RG" --output table
az group delete --name "$NET_RG"
az group exists --name "$NET_RG"
```

确认两个 subnet、data 对 NSG 的引用以及优先级100/110。自定义规则列表不等于全部有效规则。没有 VM 和监听进程，所以并未测试真实连接。区分预测、观察配置和连接测试。删除专用组后确认 false。
