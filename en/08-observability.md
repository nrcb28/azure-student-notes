# Monitoring and troubleshooting

When an application fails, saying the server is running tells us very little. We need to see requests, dependencies, and user impact.

## Signals

- **Metrics:** numerical series such as CPU usage or error counts.
- **Logs:** records with context about what happened.
- **Traces:** relationships between operations in a distributed request.

Azure Monitor provides monitoring capabilities. Application Insights helps observe applications. Log Analytics queries records with KQL when data reaches the relevant tables.

## Example query

If Application Insights sends requests to a workspace's AppRequests table:

```kusto
AppRequests
| where TimeGenerated > ago(1h)
| summarize Requests = sum(ItemCount),
            Failed = sumif(ItemCount, Success == false)
  by bin(TimeGenerated, 5m)
| order by TimeGenerated asc
```

The schema depends on the data source and query context. Other experiences may use a requests table with different column names. ItemCount helps account for sampling where applicable.

## Useful alerts

An alert needs a condition, a scope, and an action. An action group defines notifications or actions.

I would prioritise sustained failures or user-relevant latency over constant alerts about small CPU variations.

- **Service Health:** incidents, maintenance, and advisories affecting Azure services you use.
- **Resource Health:** the health of a particular resource.
- **Public Azure status:** a more general incident view.

## Troubleshooting method

1. Establish when the problem started and who is affected.
2. Check the latest change.
3. Follow a request and inspect dependencies.
4. Test the hypothesis with data.
5. Fix the issue and verify recovery.

**Common mistake:** logging tokens, passwords, or complete documents for debugging. Logged data must be limited and protected.

**Review:** low CPU usage does not rule out a slow database.

## Worked example: averages hide problems

Nine requests take 100 ms and one takes ten seconds. The mean poorly represents the person waiting ten seconds. Inspect distributions, percentiles, and volume without overinterpreting tiny samples.

Compare versions with request count, routes, and time window in mind. Fewer errors alongside disappearing traffic may be bad news.

## Observability costs

Maximum-verbosity logging can increase costs and expose data. Choose categories, suitable sampling, retention, and access.

OpenTelemetry can support consistent instrumentation. Runtime and integration matter; old SDK examples need support checks.

**Exercise:** define document upload success, latency, and processing-time signals. Specify thresholds, windows, and actions rather than relying only on CPU.

---

[Contents](README.md) · [Other language](../es/08-observability.md) · [Previous](07-governance.md) · [Next](09-costs.md)
