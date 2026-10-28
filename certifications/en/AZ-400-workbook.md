# AZ-400 · Shared advanced workbook

[←](README.md) · [Common study core](../../en/16-common-core.md) · [Advanced labs](../../en/17-advanced-labs.md)

This block has the same objectives, scenarios, and deliverables in all eight languages. Equivalence is checked by learning units and evidence, not word count. Earlier guides remain complementary explanations.

<a id="az-400-unit-1"></a>

## 1. Traceability and Git

Link need, issue, PR, commit, build, artifact, and deployment. Define consistent metric boundaries. Do not measure people by lines or commits. Choose branching around release frequency and maintained versions.

**Case:** revert a shared release. **Evidence:** explain revert versus rewritten history and data impact. If a secret was exposed, revoke or rotate it before trusting file deletion.

<a id="az-400-unit-2"></a>

## 2. Tests and artifacts

Build once and promote the identified output. Record version, digest where appropriate, and source. Combine unit, integration, end-to-end, and load tests by risk. Coverage measures execution rather than automatically good assertions.

**Case:** it worked yesterday without code changes. **Evidence:** examine unpinned tools, dependencies, and base images. Investigate flaky tests rather than repeating until green. Distinguish caches and artifacts.

<a id="az-400-unit-3"></a>

## 3. Runner identity and boundaries

Separate trusted code, PR inputs, workflow permissions, and cloud scope. Self-hosted runners need isolation, patching, and cleanup. OIDC removes long-lived secrets but still requires precise trust and authorisation.

**Case:** an external PR changes an internally executed script. **Evidence:** a path without production access, identity restrictions, and resource controls. Pipeline code is not inherently harmless.

<a id="az-400-unit-4"></a>

## 4. Deploy and recover

Compare rolling, blue-green, canary, rings, and feature flags. Define population, functional signals, observation window, and stop criteria. Swaps do not isolate every dependency. Design backward-compatible migrations where suitable.

**Case:** normal canary CPU but incorrect results. **Evidence:** a business signal and rollback criterion. Explain why an old image cannot restore a deleted column.

<a id="az-400-unit-5"></a>

## 5. Close the operational loop

Propagate context, include versions in telemetry, and protect logged data. Assign alert owners and windows. Resource approvals are not merely author-editable YAML conditions.

**Final submission:** complete pipeline design, meaningful test, fixed artifact, and promotion strategy. Run the local simulator, explain failures, and repeat with a different retry policy. Postmortem actions need owners and verification.

[Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400) · [AZ-400](AZ-400.md)
