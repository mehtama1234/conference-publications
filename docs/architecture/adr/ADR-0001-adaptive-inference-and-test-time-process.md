# ADR-0001: Treat Inference as an Adaptive Runtime Process

## Status

Proposed

## Date

2026-07-24

## Theme

Adaptive inference, test-time process control, and compute allocation.

## Context

The ICML/ICLR 2026 corpus shows a consistent shift away from treating inference as a single model call. The stronger pattern is that inference is becoming a runtime process: the system may search, branch, retrieve, call tools, verify partial results, revise, allocate more compute to difficult cases, preserve useful partial trajectories, truncate poor trajectories, and decide when to stop.

This matters for any future platform that supports agents, long-horizon tasks, research workflows, software automation, enterprise workflows, scientific reasoning, or embodied systems. In these settings, a response is not only a text artifact. It is the result of a controlled process that uses resources, touches tools, changes state, and accumulates evidence.

The platform therefore cannot model inference as:

```text
input -> model -> output
```

It must model inference as:

```text
goal
  -> plan / policy
  -> observations
  -> tool calls
  -> intermediate artifacts
  -> verification / scoring signals
  -> revision / branching / stopping
  -> final output and final state
```

## Relevant Papers

### THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning

THOR treats reasoning as a tool-integrated process. It optimizes both final-answer success and step-level tool/code success, and uses immediate tool feedback for self-correction during inference.

Platform implication: tool calls are not incidental logs. They are part of the inference state and must be captured, scored, and made available to controllers and verifiers.

### The Tell-Tale Norm

This paper uses hidden-state magnitude as a model-internal signal for reasoning intensity, then applies that signal to guide test-time recursion, steering, and response selection.

Platform implication: inference controllers should be able to consume runtime signals. These signals may come from model internals, confidence scores, verifier feedback, retrieval quality, tool errors, uncertainty estimates, or environment state.

### h1: Bootstrapping LLMs to Reason over Longer Horizons via Reinforcement Learning

h1 composes short-horizon tasks into longer dependency chains and trains with curriculum RL. The relevant lesson is that long-horizon success depends on preserving useful signal over many dependent steps.

Platform implication: long-horizon workflows should expose dependency depth, intermediate milestones, and horizon budgets. A platform should not make tasks long merely by adding tokens.

### Base Models Know How to Reason, Thinking Models Learn When

This paper suggests that RL-trained thinking models may mostly learn when to invoke reasoning mechanisms already present in the base model, while SFT distillation may add new mechanisms.

Platform implication: orchestration is capability. The runtime should help decide when to plan, retrieve, call tools, verify, ask for human review, or stop.

### T3 / Reducing Belief Deviation in Reinforcement Learning for Active Reasoning

T3 detects excessive belief deviation in active reasoning trajectories and preserves useful prefixes while truncating weak tails.

Platform implication: the platform should localize trajectory quality over time. A run may be partially successful even when the final result fails.

### Semantic-Aware Diffusion LLM Inference / AdaBlock-dLLM

This line adapts decoding block size based on semantic or confidence dynamics instead of using a fixed decoding schedule.

Platform implication: inference granularity should be configurable and adaptive. The runtime should support policies that vary step size, branching, verification frequency, and compute allocation by task state.

## Decision

The platform will treat inference as a first-class adaptive runtime process, not as a fixed model invocation.

This requires a platform abstraction for an `InferenceRun` with explicit state, steps, control policy, budget, trace, tool calls, intermediate artifacts, verifier signals, and stopping conditions.

## Design Principles

### 1. Inference Is a Policy

Every nontrivial run should have an inference policy. The policy decides:

```text
which context to load
which tool to call
when to branch
when to verify
when to revise
when to escalate
when to stop
how much budget to spend
```

The policy may be static, learned, model-driven, verifier-driven, or human-configured.

### 2. Runtime Signals Are Control Inputs

The controller should be able to use signals such as:

```text
model confidence
tool result validity
retrieval coverage
missing evidence
verifier pass/fail
state-change mismatch
uncertainty
cost/budget remaining
human-review requirement
trajectory drift
```

These signals should not be buried in logs. They should be typed outputs available to the inference policy.

### 3. Tool Calls Are Part of Reasoning

Tool calls should be represented as structured steps:

```text
tool name
input
output
latency
cost
side effects
success/failure
evidence produced
state changed
```

Tool use should be scored separately from final output where appropriate.

### 4. Intermediate Artifacts Are First-Class

The platform should support intermediate artifacts such as:

```text
plans
subgoals
retrieval bundles
evidence packets
partial proofs
code snippets
tool outputs
state snapshots
draft responses
verification reports
```

These artifacts allow process evaluation, replay, debugging, and improvement.

### 5. Stopping Is a Decision

Stopping should be explicit and explainable. A run may stop because:

```text
goal satisfied
budget exhausted
confidence sufficient
verifier passed
missing evidence cannot be resolved
human review required
policy boundary reached
trajectory quality degraded
```

Premature stopping and over-computation should both be measurable failure modes.

### 6. Branching and Revision Must Be Bounded

Adaptive inference can explode in cost if uncontrolled. Branching, self-correction, retries, and search should be governed by budgets:

```text
max steps
max tokens
max wall-clock time
max tool calls
max verifier calls
max branch width
max branch depth
max human escalations
```

### 7. Process Quality Is Separate From Final Quality

The platform should distinguish:

```text
bad process, bad result
bad process, good result
good process, bad result
good process, good result
```

This separation is important because lucky final answers should not be treated as robust capability, and good partial trajectories should produce useful improvement signals.

## Proposed Platform Abstractions

### InferenceRun

Represents one execution of a model/agent/controller against a goal.

Required fields:

```text
run_id
goal
input_context
policy_id
model_id
toolset_id
budget
initial_state
steps
artifacts
verifier_results
final_output
final_state
stop_reason
cost_summary
trace_hash
```

### InferenceStep

Represents one unit of runtime action.

Example step types:

```text
model_call
tool_call
retrieval
verification
branch
merge
revision
state_update
human_escalation
stop
```

Required fields:

```text
step_id
parent_step_id
step_type
input
output
signals
side_effects
cost
latency
status
```

### InferencePolicy

Defines how the runtime chooses the next step.

Policy types:

```text
fixed_sequence
planner_controller
verifier_gated
tree_search
confidence_adaptive
tool_feedback_adaptive
human_review_gated
learned_policy
```

### RuntimeSignal

Typed signal emitted by a model, tool, verifier, or monitor.

Examples:

```text
confidence_low
evidence_missing
tool_failed
verifier_failed
policy_violation_risk
state_mismatch
trajectory_drift
budget_near_limit
human_review_required
```

### StopReason

Stop reasons must be recorded as structured values rather than free text.

Examples:

```text
goal_completed
verified_success
budget_exhausted
insufficient_evidence
policy_blocked
human_escalation
controller_abort
trajectory_degraded
tool_unavailable
```

## Platform Requirements

### R1: Trace Every Nontrivial Run

The platform must capture step-level traces for agentic, tool-using, long-horizon, or high-stakes runs.

### R2: Make Budgets Explicit

Every adaptive run must have budgets for tokens, tool calls, wall-clock time, retries, and branch depth where applicable.

### R3: Support Verifier-Gated Progression

The platform should allow policies such as:

```text
do not proceed to final answer until evidence verifier passes
do not mutate state until policy verifier passes
do not send external message until human review passes
```

### R4: Preserve Intermediate Artifacts

Intermediate artifacts should be persisted and addressable by later verifiers, monitors, and improvement loops.

### R5: Separate Outcome Score From Process Score

Scoring systems should support both:

```text
final outcome score
process quality score
```

### R6: Make Adaptive Decisions Auditable

For every branch, retry, tool call, escalation, or stop decision, the platform should record the signal or policy condition that triggered it.

### R7: Enable Replay

Where possible, runs should be replayable with the same input state, tool fixtures, model configuration, and policy settings.

## Consequences

### Positive

- Supports long-horizon and agentic tasks more naturally than one-shot model calls.
- Makes tool use, verification, and revision inspectable.
- Produces better failure diagnostics.
- Enables budget-aware evaluation.
- Supports process-level improvement loops.
- Makes future benchmark and world-environment work easier to integrate.

### Negative

- More complex runtime model.
- More storage for traces and artifacts.
- More difficult privacy and retention controls.
- Higher engineering burden for replayable tool fixtures.
- Risk of over-instrumentation if applied to trivial tasks.

### Mitigations

- Use tiered tracing: lightweight traces for ordinary calls, full traces for agentic/high-stakes runs.
- Add retention policies for sensitive artifacts.
- Define budget defaults per task class.
- Make replay optional when external tools are inherently non-deterministic.
- Keep the one-shot call path available for simple tasks.

## Failure Modes To Track

The platform should make these failure modes observable:

```text
premature_stop
overthinking_or_wasteful_search
wrong_tool_selected
tool_result_ignored
tool_error_unhandled
missing_evidence
unsupported_revision
bad_branch_selected
trajectory_drift
state_update_without_verification
policy_gate_skipped
budget_exhaustion
human_escalation_missed
```

## Example Runtime Flow

```text
goal received
  -> retrieve relevant context
  -> draft plan
  -> verify plan has required evidence targets
  -> call tools
  -> collect evidence artifacts
  -> branch if evidence conflicts
  -> run verifier
  -> revise if verifier fails
  -> stop when verifier passes or human escalation required
  -> emit final answer, trace, cost summary, and process score
```

## Acceptance Criteria

This ADR is implemented when the platform can:

1. Represent a run as a sequence of typed inference steps.
2. Attach tool calls, verifier outputs, intermediate artifacts, and runtime signals to the run.
3. Enforce explicit budgets on adaptive inference.
4. Record structured stop reasons.
5. Score process quality separately from final output quality.
6. Replay or approximate replay for controlled environments.
7. Generate failure labels from trace and verifier results.

## Open Questions

1. Which task classes require full adaptive inference by default?
2. What is the minimum trace format that still supports useful debugging?
3. Which runtime signals should be standardized first?
4. How should sensitive tool outputs be redacted while preserving auditability?
5. Should inference policies be versioned independently from model versions?
6. How should the platform compare two runs with different costs but similar quality?
7. What should be the default branch/retry strategy for tool-using agents?

## Source Notes

- `analysis/syntheses/consolidated-theme-writeup.md`
- `analysis/syntheses/initial-deep-theme-map.md`
- `conferences/iclr-2026/notes/poster-00014-thor-tool-integrated-hierarchical-optimization-via-rl-for-mathematical-reasoning-0Af7UiJISU.md`
- `conferences/icml-2026/notes/00002-the-tell-tale-norm-ell-2-magnitude-as-a-signal-for-reasoning-dynamics-in-large-language-mo-03ZTlJuX0y.md`
- `conferences/icml-2026/notes/00015-base-models-know-how-to-reason-thinking-models-learn-when-2BniakOS4q.md`
- `conferences/icml-2026/notes/00023-h1-bootstrapping-llms-to-reason-over-longer-horizons-via-reinforcement-learning-3BW15kSPfN.md`
- `conferences/iclr-2026/notes/00191-reducing-belief-deviation-in-reinforcement-learning-for-active-reasoning-r8hzDA3pUY.md`
- `analysis/syntheses/iclr-poster-batch-004-synthesis.md`
