# The executive AI decision system

AI programs rarely fail because an organization lacks ideas. They fail because experiments accumulate without clear decision rights, evidence standards, operating limits, or a disciplined way to stop. An executive AI decision system turns activity into a repeatable management process: every consequential use of AI has an owner, a value hypothesis, an exposure tier, an evidence threshold, and a next decision date.

This chapter is practical guidance, not legal, financial, security, or investment advice.

## What the system must accomplish

The purpose is not to centralize every choice or slow down experimentation. It is to make the level of scrutiny proportional to the consequence of the decision.

A functioning system should make five things visible:

1. **What is being decided.** A specific choice, not a broad ambition such as “adopt AI.”
2. **Who owns the outcome.** One accountable business executive, supported by named technical and control owners.
3. **What must be true.** The assumptions and evidence threshold required to proceed.
4. **What authority the system receives.** The data, tools, actions, customers, employees, and financial commitments it may affect.
5. **When the decision will be revisited.** A review date and explicit conditions for scaling, redesigning, pausing, or stopping.

Without those elements, a pilot can run indefinitely while appearing successful simply because no one defined success, exposure, or an exit condition.

## Start with a decision, not a technology

Write the decision in one sentence:

> We are deciding whether to **[change a workflow or capability]** for **[defined users or stakeholders]** in order to **[measurable outcome]**, within **[time and operating boundary]**.

“Deploy a generative AI platform” is not yet a decision. “Allow 40 service agents to use an AI drafting assistant for two product lines for eight weeks, while agents retain approval authority, to test whether response time improves without reducing accuracy or customer trust” is decision-ready.

That sentence exposes the operating boundary. It also makes alternatives visible: improve the existing process, buy a narrower tool, redesign the workflow without AI, defer the decision, or do nothing.

## The executive AI decision canvas

Before funding or launch, complete a one-page canvas. If the team cannot complete it, the proposal is not ready for approval.

| Field | Required executive answer |
| --- | --- |
| Decision | What specific commitment or permission is being requested? |
| Outcome | What stakeholder or business result should change? |
| Baseline | What is the current performance, cost, quality, or risk? |
| Accountable owner | Which executive owns the outcome and trade-offs? |
| System owner | Who owns technical performance and lifecycle management? |
| Alternatives | What credible non-AI, narrower, or deferred options were considered? |
| Authority boundary | What may the AI read, produce, recommend, approve, change, or spend? |
| Evidence threshold | What must be demonstrated before launch and before scale? |
| Control design | Where are permissions, review, logging, monitoring, and human intervention built in? |
| Next decision | On what date will leaders scale, redesign, pause, or stop—and on what evidence? |

The canvas is not a business case, architecture document, risk assessment, or legal review. It is the common index that connects those materials to one accountable decision.

## Classify exposure before choosing the process

Use three practical tiers. Local policy and qualified control owners should refine the classification.

### Tier 1 — bounded assistance

The system drafts, summarizes, searches, or analyzes within a reversible workflow. A trained person reviews the output before it affects a customer, employee, transaction, regulated record, production system, or public claim.

The minimum gate is a named owner, approved data boundary, basic evaluation, user guidance, and a review date.

### Tier 2 — consequential recommendation

The system influences a material decision, prioritization, forecast, customer interaction, workforce action, security judgment, contract process, or allocation of resources—even if a person gives final approval.

The gate should include documented evaluation against the baseline, security and privacy review, legal or compliance input where relevant, failure testing, monitoring, an appeal or correction path, and a named person with authority to stop use.

### Tier 3 — delegated or agentic action

The system can take external action, change records, call tools, communicate without prior review, move money, modify production, or exercise credentials. Its potential impact may compound across repeated actions.

The gate should require explicit authority limits, least-privilege access, separation of duties, pre-deployment testing, complete action logging, spend and rate limits, runtime monitoring, rapid credential revocation, a tested shutdown path, and senior approval appropriate to the exposure.

The key principle is simple: classify the authority and consequence of the workflow, not the sophistication of the model. A technically simple system can still create Tier 3 exposure.

## Move through seven decision gates

### 1. Intake

Name the problem, intended user, affected stakeholders, proposed workflow, and requested decision. Reject technology-first proposals that cannot identify a meaningful outcome.

### 2. Triage

Assign the exposure tier. Identify whether personal data, confidential information, regulated activity, security-sensitive access, employment decisions, customer promises, financial reporting, or autonomous action is involved.

### 3. Design

Map the current workflow and the proposed workflow. Mark where data enters, where AI contributes, where a human exercises judgment, what systems can be changed, and what happens when the AI is unavailable or wrong.

### 4. Evidence plan

Define the baseline, evaluation set, quality measures, economic measures, risk indicators, affected-user feedback, and minimum evidence required for the next decision. Separate observed results from forecasts.

### 5. Pre-launch decision

The accountable owner accepts the value case and operating trade-offs. Technical and control owners confirm that required conditions are satisfied or record a specific exception. Unresolved dissent is documented and elevated to the person authorized to accept the residual exposure.

### 6. Operate and observe

Measure actual use, outcome quality, total cost, reliability, incidents, overrides, complaints, and unexpected behavior. A control that exists only in a policy document is not an operating control.

### 7. Scale, redesign, pause, or stop

Return on the promised date. Compare evidence with the baseline and approval conditions. Do not let a successful demonstration become an indefinite production service without a new decision.

## Use a dual scorecard: value and exposure

Review value and exposure in the same meeting. A project should not receive a green status because adoption increased while quality, cost, or risk remained unknown.

**Value indicators** may include adoption by the intended users, completion time, quality, revenue contribution, avoided cost, error reduction, customer experience, or capability gained. Use only measures that connect to the stated outcome.

**Exposure indicators** may include incorrect outputs, human overrides, unauthorized access attempts, security events, complaints, model or vendor changes, cost variance, latency, concentration risk, unresolved exceptions, and actions taken outside the intended boundary.

Keep forecasts, proxy measures, and observed outcomes visibly separate. “Users opened the tool” is adoption evidence; it is not proof of value.

## Make decision rights explicit

Avoid a committee in which everyone participates and no one is accountable.

- **Accountable business owner:** owns the outcome, funding case, workflow change, and decision to continue.
- **System owner:** owns technical performance, integration, evaluation, monitoring, and retirement.
- **Control authorities:** security, privacy, legal, compliance, finance, people, and risk leaders define or approve conditions within their mandates.
- **Operational owner:** ensures the redesigned workflow is usable, staffed, measured, and supported.
- **Affected-user representative:** brings evidence from the people who use the system or experience its decisions.
- **Escalation authority:** resolves exceptions or accepts residual exposure at the appropriate level.

Consultation does not transfer accountability. A business owner should not treat security approval as proof of business value, and a technical owner should not be asked to accept business or legal risk outside their authority.

## Set escalation triggers in advance

Escalation should be mechanical where possible. Trigger a review when:

- the AI receives new tools, credentials, data, users, markets, or authority;
- a human approval step is removed or routinely bypassed;
- actual cost or performance leaves the approved range;
- a material incident, complaint, security event, or control failure occurs;
- the vendor, model, hosting arrangement, or data terms change materially;
- observed outcomes differ significantly across affected groups;
- the team cannot reproduce the evidence used for approval; or
- the decision reaches its scheduled review date.

An escalation trigger is not an automatic verdict. It is a requirement to bring the decision back to the right owner with updated evidence.

## Establish a useful operating cadence

- **Weekly during a pilot:** adoption, defects, overrides, incidents, user feedback, cost, and open actions.
- **Monthly for operating systems:** outcome trend, exposure trend, vendor or model changes, exceptions, and scale decisions.
- **Quarterly at portfolio level:** funding shifts, duplicated capabilities, systemic dependencies, concentration, material risk, and retirement candidates.
- **Immediately after a material event:** contain the issue, preserve evidence, invoke the incident path, and reassess authority before resuming.

The board should receive decision-grade information about material strategy, value, capability, and exposure—not a catalogue of tools. See [Brief the board on AI with decision-grade evidence](../03-strategy-and-operations/board.md).

## A concise decision record

Record the following in a durable location:

```text
Decision:
Date and accountable owner:
Outcome and baseline:
Exposure tier and authority boundary:
Alternatives considered:
Evidence reviewed:
Required conditions and accepted exceptions:
Dissent or unresolved uncertainty:
Decision: approve / approve with conditions / redesign / pause / stop
Next review date:
Scale criteria:
Stop and escalation triggers:
```

The record should be short enough to use and precise enough that a future executive can understand what was known, what was assumed, and why the choice was reasonable at the time.

## Questions for the next executive meeting

- Which AI initiative currently has activity but no explicit decision owner?
- What authority has each live system actually received—not merely what the policy says it should have?
- Which proposal lacks a baseline or credible alternative?
- Where are forecast value and observed value being blurred?
- What would cause each initiative to stop, and who can make that call today?
- Which pilot has quietly become production without a new approval?
- What portfolio-level dependency could create simultaneous failure across several initiatives?

## Common failure patterns

- **Pilot theater:** demonstrations multiply while no operating decision is made.
- **Shared accountability:** a committee reviews the work, but no executive owns the outcome.
- **Control at the end:** security, privacy, legal, finance, or workforce implications are considered only after the workflow is designed.
- **Adoption as value:** usage is reported without quality, economic, or stakeholder outcomes.
- **Permanent exceptions:** temporary workarounds become the operating model.
- **No retirement path:** systems continue because stopping was never defined as a legitimate decision.

## Open Future Forum recommendation

**Recommendation:** bring one live decision—not a general AI topic—to a small, role-appropriate peer group. Ask peers to challenge the authority boundary, missing alternative, weakest assumption, escalation trigger, and evidence required to scale. Do not share confidential company information, personal information, credentials, non-public results, or regulated material. Peer discussion should improve the questions; accountable authority must remain inside the organization.

## Related handbook guides

- [Build and govern the AI initiative portfolio](../03-strategy-and-operations/portfolio.md)
- [Select use cases with executive discipline](../03-strategy-and-operations/use-case-selection.md)
- [Resolve the AI ownership vacuum](../03-strategy-and-operations/ownership.md)
- [Move AI governance into operating decisions](../03-strategy-and-operations/governance.md)
- [Govern AI agents as operating actors](../03-strategy-and-operations/agents.md)
- [Measure AI value without theater](../03-strategy-and-operations/roi.md)

## Public resources

- [Open Future Forum research](https://openfutureforum.com/research/)
- Watch: [How Executives Keep Up With AI Without Falling Behind](https://www.youtube.com/watch?v=KcZnCmXtcbE)
- [Executive Event Taxonomy on Hugging Face](https://huggingface.co/datasets/open-future-forum/executive-event-taxonomy)
