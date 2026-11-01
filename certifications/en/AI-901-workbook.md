# AI-901 · Common advanced workbook

[Guide](AI-901.md) · [Ten cases](AI-901-cases.md) · [Contents](README.md)

Five matching units across the study languages. Work offline with invented university notes, prompts, transcripts, and candidate responses. Label every candidate output **synthetic** and every expected outcome **prediction**. Do not upload real student material. This workbook deploys nothing and does not establish complete exam coverage. Reference check: **1 November 2026**; [objectives effective 15 April 2026](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901).

<a id="ai-901-unit-1"></a>

## 1. Define five AI contracts

Write one contract each for answering a course question, extracting an assignment deadline, analysing feedback text, accepting a spoken question, and describing a diagram. Specify input modality, permitted data, output shape, unacceptable errors, and a fallback. Compare generative answers, text analysis, speech, vision, and Content Understanding by what they produce. Include one image-generation request so that creation is distinguished from interpretation.

**Scenario:** a teammate proposes one image model for every feature. **Evidence:** a five-row decision matrix with a justified capability choice and a rejected alternative for each row. Add model-selection questions about modalities, deployment options, language, and supported parameters. Keep unknown service details marked for verification in current documentation rather than inventing limits.

<a id="ai-901-unit-2"></a>

## 2. Write grounded prompts and access rules

Invent three short passages: a permitted lecture note, a private notebook, and a permitted page containing an instruction to export documents. Assign stable source identifiers and two students with different access lists. Write system and user prompts that ask for a source-supported answer, preserve source boundaries, and allow abstention. Retrieval must filter by the caller's access before constructing the context; the prompt cannot supply that security boundary.

**Scenario:** a question has no answer in the permitted passages. **Evidence:** an expected abstention, a forbidden-access refusal, and a synthetic injection-resistant answer. Annotate which claims each source supports. Explain why a citation or an attack detector alone cannot establish truth, privacy, or permission.

<a id="ai-901-unit-3"></a>

## 3. Trace a lightweight client without cloud calls

Draw a request from a Python client to the intended Foundry endpoint and configured deployment, followed by a response or error. Distinguish identity, authorisation, destination, and deployment selection. Sketch pseudocode that reads protected configuration, obtains an appropriate credential, sends permitted input, checks errors and output, and renders a safe result. Label the sketch **pseudocode**, not executable SDK code. Explain where dictionaries, iteration, exceptions, and asynchronous calls might appear.

**Scenario:** authentication succeeds but the selected resource denies the operation. **Evidence:** a sanitised troubleshooting checklist and expected client behaviour for denied access, timeout, empty output, and invalid configuration. Compare how REST, SDK, and CLI express the same task. Identify the current [SDK quickstart](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) you would follow during later cloud practice.

<a id="ai-901-unit-4"></a>

## 4. Validate multimodal extraction

Invent an assignment sheet with a final deadline, a second sheet with no date, a diagram with an unreadable unit, and a noisy spoken question. Define a deadline schema with field types, missing-value policy, and source references. Produce deliberately flawed synthetic outputs: a guessed date, a wrong unit, and a misheard technical term. Locate the failure in extraction, visual interpretation, recognition, or downstream reasoning. Describe a speech-to-text pipeline and a supported direct multimodal alternative.

**Scenario:** an output is valid JSON but contradicts the sheet. **Evidence:** separate schema and source-validation results, review rules for ambiguity, and a text-accessibility fallback. Include how [Content Understanding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) could process document, image, audio, and video inputs. Do not treat confidence as a substitute for evidence.

<a id="ai-901-unit-5"></a>

## 5. Evaluate a single agent with limited tools

Design one notes-search agent with instructions, a model choice, caller-scoped retrieval, and no modification tools. Define the request and result of its search tool and how a client identifies the agent and maintains conversation context. Create a failure matrix with at least six rows: supported answer, missing evidence, denied document, injection, conflicting deadline, and tool timeout. Add expected outcomes before writing two competing synthetic answers for each row.

**Final evidence:** submit the contracts, prompts, access lists, client sketch, extraction checks, and scored matrix. Score factual support, citations, abstention/refusal, privacy, schema validity, and tool permissions separately. Explain one prompt revision and its tradeoff. List remaining hands-on work: model deployment and portal interaction, an actual SDK chat client, a portal-tested single agent, and its client. Offline scoring is preparation for that work.
