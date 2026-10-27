# Messaging and events

A direct HTTP request requires the receiver to be available at that moment. A queue lets one component leave work for another to process later.

## Choosing a service

| Service | Typical problem |
|---|---|
| Storage Queues | Simple work queues |
| Service Bus | Messaging with queues, topics, and enterprise features |
| Event Grid | Distributing events about something that happened |
| Event Hubs | Ingesting large event streams, such as telemetry |

I would not automatically replace an order queue with Event Hubs. Its partition, retention, and consumer model solves a different problem.

In Service Bus, a queue distributes work among consumers. A topic supports publishing to subscriptions for different recipients, with filters where appropriate.

## Delivery and duplicates

Do not assume a message will execute exactly once. A consumer might finish the work and fail before acknowledging receipt.

To generate a thumbnail:

1. The message includes the document identifier.
2. The consumer checks whether the expected output already exists.
3. It processes and stores the result consistently.
4. It acknowledges the message after completion.

Idempotency prevents repetition from incorrectly changing the outcome. Broker duplicate detection does not replace the full application design.

## Failing messages

Limit retries and investigate causes. Dead-letter and poison-message handling vary by service; not every service provides the same automatic mechanisms.

For a work queue, I would monitor message age as well as count. Ten messages stuck for hours can be worse than a thousand processed in seconds.

**Class project:** uploading a PDF returns quickly while analysis runs in the background. The interface must show that processing is still underway.

**Review:** asynchronous processing improves decoupling, but adds states and failure modes to handle.

---

[Contents](README.md) · [Other language](../es/11-messaging.md) · [Previous](10-architecture.md) · [Next](12-devops.md)
