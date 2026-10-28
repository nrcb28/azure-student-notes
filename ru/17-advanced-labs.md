# Углублённые практики

[←](README.md) · [Общее учебное ядро](16-common-core.md)

Три эквивалентные практики на восьми языках. Симуляция локальна, остальные требуют тестовую подписку, Azure CLI и права. Здесь в Azure не запускались. Ресурсы и хранение могут стоить денег. Работай из корня и сначала прочитай очистку.

<a id="advanced-lab-1"></a>

## 1. Восстановить файл и сравнить байты

Создай только отдельные группу и аккаунт. Шаблон выключает versioning и иерархическое пространство для undelete без продвижения версий. Включает семь дней soft delete blobs/контейнеров, отключает общие ключи и публичные blobs, сохраняет аутентифицируемый публичный endpoint.

Нужны управление и роль данных, например Storage Blob Data Contributor этого аккаунта. Шаблон не выдаёт роли. Дождись распространения без глобального Owner.

Скрипт создаёт новый контейнер, пишет синтетический текст, удаляет только этот blob, восстанавливает и сравнивает. Ожидается RECOVERY_OK. Затем удаляет свой контейнер, но данные могут храниться дальше. Записывай этап ошибки без секретов; production не менять.

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

## 2. Просмотреть без назначения

Используй ID ресурса и object ID principal, не client ID. Скрипт читает назначения этому principal с наследуемыми областями. Это не полный эффективный доступ: группы, условия, запреты, временная активация и данные/сеть проверяются отдельно.

Сдай роль, область, условие и нужное действие. Пустая таблица не доказывает полное отсутствие доступа. Не создавай назначение ради результата.

[Script](../labs/inspect-access.sh)

```bash
export LAB_SCOPE=$(az storage account show --name "$LAB_STORAGE" \
  --resource-group "$LAB_RG" --subscription "$LAB_SUBSCRIPTION" --query id -o tsv)
export LAB_PRINCIPAL_ID='REPLACE_WITH_PRINCIPAL_OBJECT_ID'
bash labs/inspect-access.sh
```

<a id="advanced-lab-3"></a>

## 3. Симулировать потерю ответа

Без сети, секретов и облака. SQLite сохраняет, первый ответ теряется, клиент повторяет. При трёх попытках naive хранит два документа, idempotent один, permanent не пишет и не повторяет. Задержки вычисляются без сна.

Одна попытка может оставить запись без подтверждённого успеха. Исключение не означает отсутствие операции. Семь локальных тестов проверяют поведение и ограничения, не доступность Azure.

[Simulator](../labs/retry_lab.py)

```bash
python labs/retry_lab.py --attempts 3
python labs/retry_lab.py --attempts 1
python -m unittest discover -s tools -p 'test_*lab*.py' -v
```

<a id="advanced-lab-4"></a>

## 4. Очистка и результат

Просмотри отдельную группу, подтверди удаление и проверь false. Удаление контейнера не завершает любое остаточное хранение. Проверь блокировки и ошибки, не очищай общие ресурсы через purge.

Сдай ожидаемое, наблюдаемое, права, сравнение, трактовку ролей и симуляцию. Разделяй локальные и облачные проверки.



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
