# AI-103 · Advanced developer workbook

[Guide](AI-103.md) · [Ten cases](AI-103-cases.md) · [Contents](README.md)

Five matching units use invented university notes and offline request/response fixtures. Label candidate outputs **synthetic** and expected behaviour **prediction**. No cloud resources, credentials, real student records, or service measurements are needed. These exercises develop selected implementation skills without claiming complete coverage. Checked **1 November 2026** against [objectives effective 16 April 2026](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103).

<a id="ai-103-unit-1"></a>

## 1. Freeze a client contract and deployment decision

**Scenario:** the notes app must return a grounded answer from a Python backend during peak revision traffic. Define request and response fixtures with identity context, request ID, course, outcome, answer, citations, and error categories. Include invalid JSON, denied access, timeout, and partial output. Create a compatibility manifest for resource/project, endpoint type, deployment name, API generation, package versions, and credential approach, using current [SDK guidance](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview).

**Evidence:** compare two hypothetical model candidates on quality, supported features, capacity, latency, and resource usage; mark unknowns for later verification. **Deliverable:** a typed contract sketch, four failure fixtures, and a justified deployment decision without fabricated limits or prices.

<a id="ai-103-unit-2"></a>

## 2. Design retrieval through access revocation

**Scenario:** two students share a notebook until one student's access is revoked. Invent six passages, including an assignment qualifier split across a proposed chunk boundary. Define document and chunk IDs, versions, source locations, ACL metadata, and an index/embedding version. Compare keyword, vector, and hybrid retrieval predictions. Draw caller authentication, permission filtering, retrieval, cache lookup, and model context in their actual order.

**Evidence:** a before-and-after access table covering index propagation, cached chunks, and conversation memory, plus one unsupported citation and one missing-evidence response. **Deliverable:** a retrieval design with a permission freshness policy, invalidation rule, and four regression cases. Explain how [Search access patterns](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) affect the implementation choice.

<a id="ai-103-unit-3"></a>

## 3. Trace an approved tool with an uncertain result

**Scenario:** a notes agent proposes sharing one permitted document with a study group. Define the tool schema, caller scope, exact approval payload, operation key, status store, timeout budget, and conversation ownership. Sketch **pseudocode** for validate → authorise → approve → execute → reconcile → report; it is an application design, not executable SDK code. Add a planner/retriever handoff that preserves the same permissions.

**Evidence:** traces for rejection, successful execution, duplicate delivery, expired approval, and a response lost after backend success. **Deliverable:** a state-transition table and redacted trace showing why a retry cannot duplicate the share. Connect the design to the current [function-calling boundary](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling).

<a id="ai-103-unit-4"></a>

## 4. Validate multimodal fields and meaning

**Scenario:** an assignment sheet contains draft and final deadlines, a graph has an unreadable axis, and a spoken question contains “mutex.” Define separate text, speech, visual-understanding, media-generation, and extraction contracts. Write a Content Understanding field schema with precise descriptions, types, null handling, and source references. Construct flawed synthetic outputs: swapped deadlines, an invented unit, and a misheard technical term.

**Evidence:** separate schema, source, semantic, and accessibility checks, including a confident wrong field and a text correction fallback. **Deliverable:** five annotated fixtures and a review policy calibrated with labelled examples. Check [analyser design](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/best-practices) and [document grounding availability](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/document/analyzer-improvement), keeping modality and API limitations explicit.

<a id="ai-103-unit-5"></a>

## 5. Evaluate and rehearse a rollback

**Scenario:** a candidate release changes prompts, tool schemas, and an embedding model. Score eight fixed cases: supported answer, missing source, revoked access, injection, wrong citation, ambiguous deadline, tool timeout, and duplicate action. Keep retrieval quality, claim support, safety, permission compliance, and latency predictions separate. Describe a bounded rollout and metrics that would trigger recovery.

**Evidence:** a comparison sheet, a compatible release manifest, a sanitised telemetry schema, and a rollback sequence restoring client, index, prompt, and tools together. **Deliverable:** a reviewable release packet plus a list of measurements still requiring an authorised cloud lab. Use [evaluation guidance](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation) to distinguish offline predictions from observed deployment evidence; do not report synthetic scores as Azure results.
