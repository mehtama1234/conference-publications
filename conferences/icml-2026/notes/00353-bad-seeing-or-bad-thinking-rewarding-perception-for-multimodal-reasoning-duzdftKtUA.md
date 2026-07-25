# Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: duzdftKtUA
- Authors: Haozhe Wang; Qixin Xu; Changpeng Wang; Taofeng Xue; Chong Peng; Wenhu Chen; Fangzhen Lin
- Primary area: applications->computer_vision
- Keywords: Multimodal Reasoning
- Source URL: https://openreview.net/forum?id=duzdftKtUA
- PDF URL: https://openreview.net/pdf?id=duzdftKtUA

## Abstract

Achieving robust perception-reasoning synergy is a central goal for advanced Vision-Language Models (VLMs). Recent advancements have pursued this goal via architectural designs or agentic workflows. However, these approaches are often limited by static textual reasoning or complicated by the significant compute and engineering burden of external agentic complexity. Worse, this heavy investment does not yield proportional gains, often witnessing a "seesaw effect" on perception and reasoning. This motivates a fundamental rethinking of the true bottleneck. In this paper, we argue that the root cause of this trade-off is an ambiguity in modality credit assignment: when a VLM fails, is it due to flawed perception ("bad seeing") or flawed logic ("bad thinking")?
To resolve this, we introduce a reinforcement learning framework that improves perception-reasoning synergy by reliably rewarding the perception fidelity. We explicitly decompose the generation process into interleaved perception and reasoning steps. This decoupling enables targeted supervision on perception. Crucially, we introduce Perception Verification (PV), leveraging a "blindfolded reasoning" proxy to reward perceptual fidelity independently of reasoning outcomes. Furthermore, to scale training across free-form VL tasks, we propose Structured Verbal Verification, which replaces high-variance LLM judging with structured algorithmic execution. These techniques are integrated into a Modality-Aware Credit Assignment (MoCA) mechanism, which routes rewards to the specific source of error -- either bad seeing or bad thinking -- enabling a single VLM to achieve simultaneous performance gains across a wide task spectrum.

## One-Sentence Claim

MoCA improves multimodal reasoning by separating perceptual errors from reasoning errors and routing reinforcement signals to the right failure source.

## Problem

Vision-language models often show a perception-reasoning tradeoff: interventions that improve reasoning can degrade perception, while stronger perceptual grounding does not automatically improve logic. Existing agentic workflows add external complexity but do not reliably solve this credit-assignment problem.

The paper asks how to determine whether a failure comes from bad seeing or bad thinking, and how to train on that distinction.

## Core Contribution

The contribution is a reinforcement learning framework for modality-aware credit assignment. It decomposes generation into interleaved perception and reasoning steps, introduces Perception Verification through a blindfolded-reasoning proxy, and uses Structured Verbal Verification to replace high-variance LLM judging with structured algorithmic execution.

The resulting MoCA mechanism routes rewards to perceptual fidelity or reasoning quality rather than treating the entire answer as one undifferentiated outcome.

## Method

The model's generation is decomposed into perception steps and reasoning steps. Perception Verification asks whether the perceptual information is faithful independently of the final reasoning path, using a blindfolded reasoning proxy to isolate what can be inferred without visual access.

Structured Verbal Verification turns free-form outputs into structured checks that can be executed algorithmically. MoCA then assigns reward to the modality-specific source of success or failure.

## Experiments and Evidence

Evidence reported in the abstract:

- Simultaneous gains across a wide spectrum of vision-language tasks.
- Reduced perception-reasoning "seesaw effect."
- Perception fidelity rewarded independently from reasoning outcomes.
- Structured verification used to scale beyond LLM-as-judge evaluation.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: task suite, reward decomposition implementation, blindfolded proxy construction, and RL training stability.

## Limits and Failure Modes

- The seeing/thinking boundary may be ambiguous when visual perception and logical inference are tightly coupled.
- Structured verbal verification may cover only tasks whose outputs can be reliably parsed and executed.
- Blindfolded reasoning proxies may leak dataset priors and misattribute errors.
- Reward routing can amplify verifier mistakes if modality labels are wrong.

## Deep Themes

**Credit assignment is moving inside multimodal cognition.** The paper treats perception and reasoning as separable training targets.

**Verification becomes supervision.** Instead of merely evaluating outputs, verification produces targeted rewards.

**Agentic complexity is being internalized.** The method tries to get the benefits of tool-like verification without relying on large external workflows.

## Subthemes

- Perception Verification.
- Blindfolded-reasoning proxy.
- Structured Verbal Verification.
- Modality-aware reward routing.
- Perception-reasoning tradeoff in VLMs.

## Connections to Other Papers

Connects to Agent0-VL, VenusBench-Mobile, Real-Time Visual Attribution, UniMapping, and Monitoring Monitorability. It also echoes When to Trust the Cheap Check: both papers convert imperfect verification signals into controlled decisions or rewards.

## Notes for Cross-Paper Synthesis

MoCA adds a fine-grained alignment pattern: rather than rewarding final outcomes, train models on localized process variables that explain why the outcome succeeded or failed.
