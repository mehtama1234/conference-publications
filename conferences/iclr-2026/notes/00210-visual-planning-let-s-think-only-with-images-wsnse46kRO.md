# Visual Planning: Let's Think Only with Images

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: wsnse46kRO
- Authors: Yi Xu; Chengzu Li; Han Zhou; Xingchen Wan; Caiqi Zhang; Anna Korhonen; Ivan Vulić
- Primary area: foundation or frontier models, including LLMs
- Keywords: visual planning
- Source URL: https://openreview.net/forum?id=wsnse46kRO
- PDF URL: https://openreview.net/pdf?id=wsnse46kRO

## Abstract

Recent advancements in Large Language Models (LLMs) and their multimodal extensions (MLLMs) have substantially enhanced machine reasoning across diverse tasks. However, these models predominantly rely on pure text as the medium for both expressing and structuring reasoning, even when visual information is present. In this work, we argue that language may not always be the most natural or effective modality for reasoning, particularly in tasks involving spatial and geometrical information. Motivated by this, we propose a new paradigm, Visual Planning, which enables planning through purely visual representations for these "vision-first'' tasks, as a supplementary channel to language-based reasoning. In this paradigm, planning is executed via sequences of images that encode step-by-step inference in the visual domain, akin to how humans sketch or visualize future actions. We introduce a novel reinforcement learning framework, Visual Planning via Reinforcement Learning (VPRL), empowered by GRPO for post-training large vision models, leading to substantial improvements in planning in a selection of representative visual navigation tasks, FrozenLake, Maze, and MiniBehavior. Our visual planning paradigm outperforms all other planning variants that conduct reasoning in the text-only space. Our results establish Visual Planning as a viable and promising supplement to language-based reasoning, opening new avenues for tasks that benefit from intuitive, image-based inference.

## One-Sentence Claim

Visual Planning proposes that spatial and geometric tasks can benefit from image-sequence reasoning, and trains large vision models with GRPO to plan directly in visual representations.

## Problem

LLMs and multimodal LLMs usually structure reasoning in text even when the task is primarily visual. For navigation, geometry, and spatial planning, text can be an unnatural bottleneck because the relevant intermediate states are often easier to express as sketches, images, or visual futures.

## Core Contribution

The paper introduces Visual Planning as a reasoning paradigm in which plans are represented as sequences of images rather than text. It also proposes Visual Planning via Reinforcement Learning, using GRPO to post-train large vision models for visual navigation tasks.

## Method

VPRL trains a model to generate step-by-step visual representations for planning. The reinforcement learning setup uses GRPO during post-training, encouraging image-based intermediate reasoning that supports downstream action or navigation decisions.

## Experiments and Evidence

The abstract reports substantial improvements on representative visual navigation tasks: FrozenLake, Maze, and MiniBehavior. It states that visual planning outperforms planning variants that reason only in text space.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should check how image plans are generated, how rewards are assigned to intermediate visual states, how action extraction works, and whether gains depend on simple grid-like environments. Visual-only reasoning may struggle where symbolic constraints, language instructions, or hidden state are essential.

## Deep Themes

- Modality-native reasoning.
- Visual intermediate states as plans.
- RL post-training for planning processes.
- Spatial reasoning beyond text chains.

## Subthemes

- Visual Planning.
- VPRL.
- GRPO for large vision models.
- Navigation tasks.
- Image-sequence inference.

## Connections to Other Papers

Connects to EmotionThinker through replacing generic text rationales with modality-grounded reasoning, to cadrille through spatial/geometric output structure, and to T3 through training intermediate trajectories rather than only final answers.

## Notes for Cross-Paper Synthesis

This paper sharpens a major corpus pattern: reasoning is becoming plural in medium. Text is one planning substrate, but 2026 papers increasingly ask whether the best intermediate representation is visual, acoustic, executable, topological, or otherwise domain-native.
