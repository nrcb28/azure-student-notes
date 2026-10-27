# Практика · Azure CLI / Bicep

[Содержание](README.md) · [English](../en/13-laboratorios.md)

Практики используют Bash, Azure CLI и Bicep в тестовой подписке. При подготовке материалов они не выполнялись в Azure. Возможно создание реальных ресурсов и расходов. Сначала прочитай удаление.

Нужны права на группу и ресурсы. Для Blob требуется роль данных, например Storage Blob Data Contributor в необходимой области. Contributor управления не всегда достаточно. Не выдавай Owner на всю подписку ради обхода ошибки.

## 1. Проверить подписку

В корне репозитория выполни вход и замени идентификатор-заглушку. Проверь имя и ID до создания учебной группы. Сохраняй переменные в той же оболочке. При необходимости выбери разрешённый регион.

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

## 2. Скомпилировать, проверить и развернуть

Прочитай [конфигурацию Bicep](../labs/storage.bicep). Она создаёт Standard_LRS, требует HTTPS, отключает анонимные blobs и общие ключи. Публичный сетевой endpoint остаётся включённым; аутентификация обязательна. Частная сеть, копирование и RBAC не настраиваются.

Компиляция проверяет синтаксис; validate и what-if требуют Azure. Изучи изменения до создания. Имена, квоты и Policy ещё могут помешать. publicBlobs и sharedKey должны быть false.

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

## 3. Создать частный контейнер со своим удостоверением

При отсутствии роли данных попроси назначение только в нужной области. Распространение может занять время. auth-mode login использует удостоверение CLI без получения ключа аккаунта. В списке должен появиться notes.

403 может относиться к правам или ограничениям сервиса. Не открывай сеть без диагностики.

```bash
az storage container create --account-name "$LAB_STORAGE" \
  --name notes --auth-mode login --public-access off

az storage container list --account-name "$LAB_STORAGE" \
  --auth-mode login --query '[].name' --output table
```

## 4. Удалить учебную группу

Проверь список. Команда удаляет группу и все её ресурсы: используй только группу этой практики. Подтверди запрос CLI и дождись завершения.

```bash
az resource list --resource-group "$LAB_RG" --output table
az group delete --name "$LAB_RG"
```

## 5. Подтвердить удаление

Ожидается false. Иначе проверь блокировки, ошибки и права. Нельзя просто считать ресурсы удалёнными.

```bash
az group exists --name "$LAB_RG"
```
