# Практические дополнения из Microsoft Learn

[Español](../es/README.md) · [English](../en/README.md) · [Italiano](../it/README.md) · [Deutsch](../de/README.md) · [Français](../fr/README.md) · [Русский](../ru/README.md) · [日本語](../ja/README.md) · [简体中文](../zh/README.md)

Источники проверены 27 октября 2026 года. Объяснения переработаны, примеры составлены самостоятельно. Предложенные проверки не выполнялись в Azure.

<a id="learn-sas"></a>

## 1. SAS через Entra ID

User delegation SAS для Blob использует ключ делегирования, полученный через Entra ID. Для получения ключа нужны права; знания URL недостаточно.

**Случай:** временное скачивание PDF. Ограничиваем ресурс, чтение и срок, не записываем чувствительный URL в журналы. Отдельно проверяем истечение, права и сеть. Планируем реакцию на утечку и отзыв с учётом типа SAS.

[Microsoft Learn · Storage: user delegation SAS](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli)

<a id="learn-dns"></a>

## 2. Проследить частный DNS

Клиент должен разрешать имя сервиса в IP private endpoint. Создание интерфейса не настраивает все DNS-серверы. Рекомендуемая зона зависит от сервиса.

**Случай:** из VM работает, из университета нет. Сравниваем ответы, связи зон, пересылку и маршруты. Не заменяем целую публичную зону без анализа и не фиксируем IP в коде. Корректный DNS не выдаёт права на данные.

[Microsoft Learn · Private endpoint DNS](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

<a id="learn-policy"></a>

## 3. Оценка и исправление

Remediation применяет modify или deployIfNotExists к существующим ресурсам через удостоверение назначения и его права. Изменение определения не обновляет автоматически все разрешения.

**Случай:** старые ресурсы всё ещё не соответствуют. Проверяем эффект, область, удостоверение и роли; исправляем пилотную группу и сохраняем результаты. Deny не преобразует любую старую конфигурацию автоматически.

[Microsoft Learn · Policy remediation](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources)

<a id="learn-dcr"></a>

## 4. DCR и сбор данных

Data collection rules описывают сбор и маршрутизацию в поддерживаемых сценариях. Преобразования могут фильтровать или менять данные до назначения. Это не универсальная замена diagnostic settings.

**Случай:** нет событий VM. Проверяем агент, связь правила, источник, поток, назначение и схему. Сбор всего увеличивает стоимость и раскрытие; чрезмерная фильтрация уничтожает полезные свидетельства.

[Microsoft Learn · Azure Monitor data collection rules](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview)

<a id="learn-whatif"></a>

## 5. Ограничения what-if

What-if прогнозирует изменения без применения. Права, зависимости и выражения могут ограничить анализ. Неполный результат не доказывает отсутствие изменений.

**Случай:** Ignore или непроверенный модуль. Читаем диагностику и изолируем модуль, не приравниваем к NoChange. Различаем компиляцию, валидацию, прогноз и последующую проверку. Ревью учитывает непроанализированные части.

[Microsoft Learn · Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if)

<a id="learn-slots"></a>

## 6. Слоты — работающие приложения

У слота есть hostname и действующее приложение. Копирование настроек не клонирует содержимое, частную сеть и все зависимости. Swap включает подготовку и прогрев.

**Случай:** staging рассылает настоящие письма. Проверяем подключения, удостоверение, настройки слота и стартовые задачи. Нулевой пользовательский трафик не останавливает фоновые процессы. Обратный swap не отменяет разрушительную миграцию.

[Microsoft Learn · App Service deployment slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)

<a id="learn-landing"></a>

## 7. Landing zones и ответственность

Landing zones организуют удостоверения, подключения, администрирование и управление. У платформы и нагрузок могут быть разные владельцы. Акселератор не заменяет требования.

**Случай:** пять факультетов делят сеть и отдельно управляют приложениями. Определяем владельцев, границы, права, политики и расходы. Не копируем полную корпоративную платформу в маленькую практику без причины.

[Microsoft Learn · Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)

<a id="learn-checks"></a>

## 8. Checks и публикация

В Azure Pipelines владельцы ресурсов управляют approvals и checks вне YAML. До этапа должны пройти проверки используемых ресурсов.

**Случай:** рабочая среда требует независимого ревью и временного окна. Определяем ресурс, проверяющих, тайм-аут и отказ. Проверяем сроки и изменения. Зелёный pipeline не разрешает любую service connection.

[Microsoft Learn · Azure Pipelines approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops)

---

[Source register](../LEARN-SOURCES.md) · [Attribution](../ATTRIBUTION.md)
