# Практика · VNet / NSG

[Содержание](README.md) · [English](../en/network-lab.md)

Практики используют Bash, Azure CLI и Bicep в тестовой подписке. При подготовке материалов они не выполнялись в Azure. Возможно создание реальных ресурсов и расходов. Сначала прочитай удаление.

Нужны права на группу и ресурсы. Для Blob требуется роль данных, например Storage Blob Data Contributor в необходимой области. Contributor управления не всегда достаточно. Не выдавай Owner на всю подписку ради обхода ошибки.

[Сетевая конфигурация](../../labs/network.bicep) создаёт VNet, две подсети и NSG без VM, gateway и публичного IP. Предскажи правила: web 10.30.1.5 к data 10.30.2.5 на TCP 443 разрешает приоритет 100; TCP 22 запрещает 110. Прочий входящий трафик из подсети data также запрещён.

Правило 110 предшествует стандартному разрешению VirtualNetwork. Это учебный выбор, не универсальное правило рабочей среды. Без VM и слушающего процесса реальное подключение не доказано.

## 1. Проверить и развернуть

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

## 2. Проверить конфигурацию

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

## 3. Удалить и подтвердить

```bash
az resource list --resource-group "$NET_RG" --output table
az group delete --name "$NET_RG"
az group exists --name "$NET_RG"
```

Должны существовать две подсети; data ссылается на NSG. Проверь приоритеты 100 и 110. Список пользовательских правил не равен всем действующим правилам.

Разделяй прогноз, наблюдаемую конфигурацию и тест подключения. Последний не выполнялся. Удаление относится ко всей учебной группе и должно подтверждаться false.
