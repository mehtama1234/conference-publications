# PhotoAgent: Exploratory Visual Aesthetic Planning with Large Vision Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Ws8swqL5ob
- Authors: Mingde Yao; Zhiyuan You; King Man Tam; Menglu Wang; Tianfan Xue
- Primary area: applications->computer_vision
- Keywords: image enhancement; image composition; edit
- Source URL: https://openreview.net/forum?id=Ws8swqL5ob
- PDF URL: https://openreview.net/pdf?id=Ws8swqL5ob

## Abstract

With the recent fast development of generative models, instruction-based image editing has shown great potential in generating high-quality images. However, the quality of editing highly depends on carefully designed instructions, placing the burden of task decomposition and sequencing entirely on the user. To achieve autonomous image editing, we present PhotoAgent, a system that advances image editing through explicit aesthetic planning. Specifically, PhotoAgent formulates autonomous image editing as a long-horizon decision-making problem. It reasons over user aesthetic intent, plans multi-step editing actions via tree search, and iteratively refines results through closed-loop execution with memory and visual feedback, without requiring step-by-step user prompts. To support reliable evaluation in real-world scenarios, we introduce UGC-Edit, an aesthetic evaluation benchmark consisting of 7,000 photos and a learned aesthetic reward model. We also construct a test set containing 1,017 photos to systematically assess autonomous photo editing performance. Extensive experiments demonstrate that PhotoAgent significantly outperforms existing methods in both instruction faithfulness and visual quality across a diverse range of editing scenarios.

## One-Sentence Claim

PhotoAgent turns autonomous image editing into long-horizon aesthetic planning with tree search, memory, visual feedback, and learned aesthetic rewards.

## Problem

Instruction-based image editing can produce high-quality results, but it depends heavily on carefully decomposed user instructions. Users often must decide the edit sequence, prompt wording, and refinement steps themselves.

The paper asks how an agent can infer aesthetic intent and autonomously plan multi-step edits without requiring step-by-step prompts.

## Core Contribution

The paper introduces PhotoAgent, an autonomous image-editing system that uses explicit aesthetic planning. It reasons about user intent, plans editing actions through tree search, executes in closed loop with memory and visual feedback, and iteratively refines the image.

It also introduces UGC-Edit, an aesthetic evaluation benchmark with 7,000 photos and a learned aesthetic reward model, plus a 1,017-photo test set for autonomous photo editing.

## Method

PhotoAgent formulates editing as long-horizon decision-making. At each step, it considers candidate edits, uses tree search to plan action sequences, executes edits, observes visual feedback, and updates memory before further refinement.

The reward/evaluation side uses learned aesthetic scoring to judge visual quality and guide comparison across real-world user-generated photos.

## Experiments and Evidence

Evidence reported in the abstract:

- UGC-Edit benchmark with 7,000 photos.
- Learned aesthetic reward model.
- 1,017-photo test set.
- Experiments across diverse editing scenarios.
- Significant gains over existing methods in instruction faithfulness and visual quality.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: editing tools, tree-search branching, reward-model training, baselines, and human preference evaluation.

## Limits and Failure Modes

- Aesthetic rewards can encode subjective or dataset-specific preferences.
- Tree search may be expensive if edit tools are slow.
- Autonomous edits may over-optimize visual appeal while changing user intent.
- Closed-loop visual feedback depends on reliable image understanding after each edit.

## Deep Themes

**Creative editing is becoming agentic planning.** The model plans and sequences edits instead of just executing a single instruction.

**Aesthetic quality needs explicit reward models.** Evaluation and planning both depend on operationalizing visual preference.

**Memory and feedback turn generation into control.** PhotoAgent treats editing as iterative state refinement.

## Subthemes

- Long-horizon image-edit planning.
- Tree search over visual edits.
- Closed-loop visual feedback.
- Learned aesthetic reward models.
- User-generated photo benchmark.

## Connections to Other Papers

Connects to TG-RAG, TerminalTraj, and tau2-bench through process-controlled agents. It also links to RelaxFlow and OCE because all control generative visual models with structured objectives beyond raw prompting.

## Notes for Cross-Paper Synthesis

PhotoAgent strengthens a clear pattern: generation is shifting from one-shot prompting to agentic control loops with planning, reward feedback, and memory.
