# DevOps и инфраструктура как код

[Содержание](README.md) · [Сертификации](../certifications/ru/README.md)

DevOps объединяет разработку и эксплуатацию для надёжных изменений. CI интегрирует с проверками и сборкой. Непрерывная доставка сохраняет готовность к выпуску, непрерывное развёртывание публикует автоматически по условиям.

Продвигаем один проверенный артефакт. Версии и digest помогают установить, что именно работало.

Bicep описывает ресурсы Azure; Terraform хранит состояние, которое нужно защищать. Plan и what-if полезны, но не гарантируют любую будущую операцию. OIDC убирает долгоживущий секрет, но требует федеративного доверия и прав.

**Откат:** старый код не воссоздаёт удалённый столбец БД. Нужны совместимые миграции и проверенное восстановление.

Привилегированный runner не должен бесконтрольно запускать недоверенный код.

**Задание:** свяжи issue, PR, тесты, артефакт и выпуск. Определи условия продвижения и отката. Локальная проверка: python tools/check_docs.py.

---

[Назад](11-messaging.md) · [Далее](13-laboratorios.md) · [English](../en/12-devops.md)

## Дополнение Microsoft Learn · whatif

What-if прогнозирует изменения без применения. Права, зависимости и выражения могут ограничить анализ. Неполный результат не доказывает отсутствие изменений.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if) · [Дополнение Microsoft Learn](15-microsoft-learn.md#learn-whatif)

## Дополнение Microsoft Learn · slots

У слота есть hostname и действующее приложение. Копирование настроек не клонирует содержимое, частную сеть и все зависимости. Swap включает подготовку и прогрев.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) · [Дополнение Microsoft Learn](15-microsoft-learn.md#learn-slots)

## Дополнение Microsoft Learn · checks

В Azure Pipelines владельцы ресурсов управляют approvals и checks вне YAML. До этапа должны пройти проверки используемых ресурсов.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops) · [Дополнение Microsoft Learn](15-microsoft-learn.md#learn-checks)

## Ограниченные повторы и идемпотентность

Повторы помогают временным сбоям, но не неправильным учётным данным или запросам. Ограничиваем число и общее время, учитываем встроенные повторы SDK.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) · [Ограниченные повторы и идемпотентность](15-microsoft-learn.md#learn-retry)
