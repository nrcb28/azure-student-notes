# ADR template: architecture decision

[Certifications](README.md) · [Español](../es/ADR-template.md)

## Title and status

One concrete sentence. Status: proposed, accepted, or superseded. Record date and owners.

## Context

Problem and constraints. Separate facts from assumptions.

## Verifiable requirements

Availability, performance, recovery, residency, security, operations, and budget. Identify requirements still awaiting confirmation.

## Options

Compare at least two reasonable alternatives. Do not invent a weak alternative merely to justify the preferred choice.

| Criterion | Option A | Option B |
|---|---|---|
| Requirements | Evidence needed | Evidence needed |
| Operations | Required work | Required work |
| Cost | Units and assumptions | Units and assumptions |
| Recovery | Procedure | Procedure |
| Limits | Limitations | Limitations |

## Decision

Choice, reason, and the deciding requirement.

## Consequences

Benefits, additional work, accepted risks, and mitigations.

## Validation

Test the main assumption. Record who performs the test and the acceptable outcome.

## Review condition

Changes in load, rules, staffing, pricing, support, or requirements that trigger review.

## Short example

Choose a managed API platform to reduce operating system work because the team is small and the runtime fits. Review if a new dependency requires kernel access. Validate load, networking, and configuration recovery before acceptance.
