# Compute and containers

Choosing where code runs is about dividing work between our team and the platform. More control usually brings more maintenance.

| Service | Typical fit |
|---|---|
| Virtual Machines | Operating system control and specific software |
| VM Scale Sets | Groups of machines with coordinated configuration and scaling |
| App Service | Web applications and APIs |
| Functions | Event-triggered functions |
| Container Instances | Containers without operating a cluster |
| Container Apps | Container applications with managed revisions and scaling |
| AKS | Managed Kubernetes, with customer operational responsibilities |

## What remains our responsibility

With a VM, we maintain the operating system and application. App Service delegates more administration to the platform, but we still manage application dependencies, access, and settings.

A container packages an application and its dependencies. It is not a complete VM: traditional containers share the host operating system's kernel.

AKS manages part of Kubernetes. We still need to consider upgrades, networking, permissions, policies, and capacity.

## Functions and serverless

Serverless means we do not directly manage the servers. It does not mean zero cost, no limits, or infinite scaling.

Startup behaviour, connectivity, execution duration, and billing depend on the plan. I would check those constraints before choosing it for long-running jobs.

## Choosing for our API

I would start with App Service if its runtime fits. If we already have a container image and need independent components, I would consider Container Apps. I would choose AKS when we actually need Kubernetes.

**Common mistake:** putting three apps in the same App Service Plan and assuming completely independent capacity. They can share the plan's resources.

**Review:** using Docker does not require deploying Kubernetes.

## Successful deployment, broken application

The platform starts a container, but the application listens on a different port or starts too slowly. Resource creation can succeed while requests fail.

Check ports, processes, startup logs, configuration, and health checks. Then validate a request across real dependencies.

## Image and configuration

Separating image from configuration supports promoting one artifact between environments. Do not embed secrets in image layers: later file deletion may leave them in history.

Version pinning helps reproduce problems. Using latest everywhere makes the running code and dependencies harder to identify.

**Reasoned choice:** an occasional containerised task may not justify a permanent cluster. Check startup, duration, connectivity, and plan constraints when evaluating alternatives.

---

[Contents](README.md) · [Other language](../es/03-compute.md) · [Previous](02-resources.md) · [Next](04-storage.md)

## Microsoft Learn expansion · slots

A deployment slot has its own hostname and runs an application. Copying settings does not clone content, private networking, or every dependency. Swaps include preparation and warm-up steps.

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) · [Microsoft Learn expansion](15-microsoft-learn.md#learn-slots)
