# RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: PO2iULmu5e
- Authors: Zhehao Huang; Yuhang Liu; Baijiong Lin; Yixin Lou; Zhengbao He; Hanling Tian; Tao Li; Xiaolin Huang
- Primary area: foundation or frontier models, including LLMs
- Keywords: Large Reasoning Model;Instruction Following;Model Merging;Null-Space
- Source URL: https://openreview.net/forum?id=PO2iULmu5e
- PDF URL: https://openreview.net/pdf?id=PO2iULmu5e

## Abstract

Large reasoning models (LRMs) excel at a long chain of reasoning but often fail to faithfully follow instructions regarding output format, constraints, or specific requirements. We investigate whether this gap can be closed by integrating an instruction-tuned model (ITM) into an LRM. Analyzing their differences in parameter space, namely task vectors, we find that their principal subspaces are nearly orthogonal across key modules, suggesting a lightweight merging with minimal interference. However, we also demonstrate that naïve merges are fragile because they overlook the output format mismatch between LRMs (with explicit *thinking* and *response* segments) and ITMs (answers-only). We introduce **RAIN-Merging** (Reasoning-Aware Instruction-attention guided Null-space projection Merging), a gradient-free method that integrates instruction following while preserving thinking format and reasoning performance. First, with a small reasoning calibration set, we project the ITM task vector onto the null space of forward features at thinking special tokens, which preserves the LRM's structured reasoning mechanisms. Second, using a small instruction calibration set, we estimate instruction attention to derive module-specific scaling that amplifies instruction-relevant components and suppresses leakage. Across four instruction-following benchmarks and nine reasoning & general capability benchmarks, RAIN-Merging substantially improves instruction adherence while maintaining reasoning quality. The gains are consistent across model scales and architectures, translating to improved performance in agent settings.

## One-Sentence Claim

RAIN-Merging improves instruction following in large reasoning models by merging instruction-tuned task vectors through reasoning-aware null-space projection and module-specific scaling while preserving thinking format.

## Problem

Large reasoning models often produce strong long-chain reasoning but fail to follow output-format constraints or specific instructions.

Instruction-tuned models handle formatting better, but naive merging can damage reasoning because LRMs use explicit thinking/response segments while ITMs are usually answers-only.

## Core Contribution

The paper introduces RAIN-Merging, a gradient-free model-merging method for integrating instruction-following ability into LRMs.

It leverages the observation that LRM and ITM task-vector principal subspaces are nearly orthogonal across key modules, enabling lightweight merging with reduced interference.

## Method

RAIN-Merging first uses a small reasoning calibration set to project the ITM task vector onto the null space of forward features at thinking special tokens. This is intended to preserve structured reasoning mechanisms.

It then uses an instruction calibration set to estimate instruction attention and derive module-specific scaling, amplifying instruction-relevant components while suppressing leakage.

## Experiments and Evidence

The abstract reports evaluation across four instruction-following benchmarks and nine reasoning/general-capability benchmarks.

RAIN-Merging substantially improves instruction adherence while maintaining reasoning quality. Gains are consistent across model scales and architectures and transfer to agent settings.

## Limits and Failure Modes

Null-space projection depends on calibration coverage. If thinking-token features do not capture all reasoning mechanisms, merging may still degrade subtle capabilities. The method also assumes task-vector orthogonality that may not hold across all model families.

Because this note is abstract-only, details still need checking: task-vector construction, calibration sizes, null-space computation, instruction-attention scaling, models tested, and agent-setting evaluations.

## Deep Themes

- Behavior-preserving model merging: capability transfer should avoid interfering with reasoning format.
- Parameter-space modularity: near-orthogonal task-vector subspaces suggest separable behavioral directions.
- Reasoning-format preservation: instruction tuning must respect special structure in LRMs' thinking/response outputs.
- Gradient-free adaptation: model editing can improve behavior without full fine-tuning.

## Subthemes

- Task vectors.
- Null-space projection.
- Instruction-attention scaling.
- LRM instruction following.

## Connections to Other Papers

This connects to WSM checkpoint merging, self-souping, GRAM modular pretraining, and model editing work.

It also relates to SafeDPO and Train-before-Test because all examine how adaptation changes model behavior while trying to preserve core capability.

## Notes for Cross-Paper Synthesis

RAIN-Merging adds to the adaptation-with-preservation theme: improving one behavior increasingly requires explicit protection of another model subsystem.
