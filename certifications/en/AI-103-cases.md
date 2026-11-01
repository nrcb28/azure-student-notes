# AI-103 · 10 developer cases with reasoned answers

[Guide](AI-103.md) · [Workbook](AI-103-workbook.md) · [Contents](README.md)

Original university notes application scenarios, not exam questions. All proposed outputs and timings are hypothetical. Explain the implementation decision and the evidence you need before opening each answer. Reference check: **1 November 2026**.

## 1. A Python sample imports successfully but its response has no expected property. Should the team change the deployment until it works?

<details>
<summary>Answer</summary>

First inspect the installed SDK version, API generation, operation, endpoint, and documented response shape. Import success proves little about compatibility with a copied sample. Pin a coherent dependency set and map a sanitised response fixture into the app's own contract. Distinguish a missing property from an authentication failure or unknown deployment. Changing the model cannot repair a client that reads the wrong object. Record the documentation URL and package versions, then verify a real call only in a separately authorised lab.

</details>

## 2. A larger model improves summaries but doubles hypothetical latency during revision week. Which model should ship?

<details>
<summary>Answer</summary>

Use the same representative evaluation set and load assumptions for both candidates. Measure support, citation accuracy, abstention, structured output, latency distribution, throughput, and resource usage. Decide which requirements are mandatory before comparing averages. A smaller model might handle ordinary questions while a bounded escalation handles difficult ones, but that routing also needs evaluation. Include retrieval time and retries in the budget. Neither model size nor one attractive summary establishes the best deployment; record a justified quality, capacity, latency, and cost tradeoff without inventing prices.

</details>

## 3. A student loses access to a shared notebook, but cached chunks still answer their question. Is the index filter sufficient?

<details>
<summary>Answer</summary>

The full retrieval path must enforce current access before context reaches the model. Inspect permission propagation to child chunks, index updates, conversation memory, and caches. Cache keys need appropriate identity and permission context, and revocation requires invalidation or another freshness control. A correct index query cannot protect a response served from an older unrestricted cache. Write a policy for acceptable permission freshness and fail closed when it cannot be met. Demonstrate the denial with two synthetic identities and a before-and-after revocation trace.

</details>

## 4. An answer cites the correct lecture PDF but attributes a deadline to a paragraph that only defines an algorithm. Does citation presence pass evaluation?

<details>
<summary>Answer</summary>

No. Validate that the cited passage and version actually support the claim. Source existence, source relevance, and claim support are separate checks. Inspect whether retrieval omitted the assignment page, whether chunking lost context, or whether generation invented a date despite sufficient evidence. The app should abstain when its authorised passages lack the deadline. Keep the failed example in regression evaluation and score citation correctness independently from readability. A source link that opens successfully is useful navigation, but cannot establish that the answer is grounded.

</details>

## 5. An agent times out after requesting a sharing tool; the backend already created the share. Should the client retry immediately?

<details>
<summary>Answer</summary>

Treat the outcome as unknown until reconciled. Give the approved application operation a stable idempotency key and record its status independently of the model response. Query or recover that status before resubmitting; retries must not create another share. Bind approval to the exact documents, recipients, and versions, then recheck authorisation at execution. Distinguish a tool deadline from the overall agent budget. Capture redacted correlation identifiers so the trace connects request, approval, backend completion, and lost response without exposing student content.

</details>

## 6. A planner agent delegates to a retrieval agent that can read every course. Does the planner's restricted prompt preserve student permissions?

<details>
<summary>Answer</summary>

The handoff must carry a trusted caller context, and the retrieval tool must enforce that caller's permissions. A planner prompt cannot constrain a privileged downstream service reliably. Define each agent's role, tool scope, allowed handoff fields, memory ownership, and termination budget. Pass only authorised evidence back to the planner and prevent one student's conversation from reusing another's memory. Test a denied course request and an injected handoff. Delegating work may divide responsibilities, but it must never silently enlarge the end user's access.

</details>

## 7. The app needs a description of a graph and a new revision poster. Can both requests use the same visual contract?

<details>
<summary>Answer</summary>

Define separate contracts for understanding existing evidence and creating new media, even if one platform supports both. The graph response needs support from visible labels, units, and relationships, with abstention for unreadable regions. The poster needs generation controls, appropriate source rights, safety checks, and review of generated text and diagrams. Video variants also need segment or editing semantics. Test alt text for usefulness and avoid inferring invisible details. A compelling generated illustration cannot validate a statement about the original lecture graph.

</details>

## 8. Speech recognition changes “mutex” to “music,” and translation then produces fluent nonsense. Should only the translation prompt be revised?

<details>
<summary>Answer</summary>

Inspect the stages against their separate contracts. An upstream recognition error can become fluent but incorrect translated text and a wrong answer. Build examples with technical vocabulary, noise, negation, and interruptions; preserve a text correction path and check the selected service's supported domain customisation. If a direct multimodal design has no exposed transcript, evaluate the same meaning preservation end to end. Record language-specific failures instead of averaging them away. A prompt revision is justified only after identifying the stage and measuring its effect.

</details>

## 9. Content Understanding returns a high-confidence draft deadline in `final_due_date`. Can the calendar proposal proceed?

<details>
<summary>Answer</summary>

The value violates the intended field semantics despite its confidence. Define the final-submission field clearly, inspect its grounding in the document, and compare with labelled draft/final examples. Validate format, missing values, and consistency with other milestones. Route unresolved ambiguity to review; confidence is an estimate rather than a business-rule decision. Verify that the selected API and configuration expose the evidence needed. A downstream calendar or sharing action also needs its own authorisation and approval, independently of extraction quality or valid JSON.

</details>

## 10. A release changes the prompt, embedding model, and tool response schema; citation failures increase. Is reverting the prompt enough?

<details>
<summary>Answer</summary>

Use the release manifest to identify all changed components and their compatibility. A new embedding representation may require reindexing, while an old client may misread a new tool result. Compare traces and regression cases to locate the failure, then restore a compatible known-good set or execute the documented migration. Define rollback triggers for grounding, access, tool errors, and latency before rollout. Retain version identifiers in sanitised telemetry. Reverting one visible prompt cannot reliably repair changes in retrieval representations or application response contracts.

</details>

Sources: [current objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103), [SDKs and endpoints](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview), [evaluation](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation), [document access](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview), [function calling](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling), [analyser design](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/best-practices), [confidence and grounding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/document/analyzer-improvement).
