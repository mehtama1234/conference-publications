# MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 3eTr9dGwJv
- Authors: Yuanchen Ju; Yongyuan Liang; Yen-Jen Wang; Gireesh Nandiraju; Yuanliang Ju; Seungjae Lee; Qiao Gu; Elvis Hsieh; Furong Huang; Koushil Sreenath
- Primary area: applications to robotics, autonomy, planning
- Keywords: Scene Graph;Task Planning;Spatial Understanding;Mobile Manipulation
- Source URL: https://openreview.net/forum?id=3eTr9dGwJv
- PDF URL: https://openreview.net/pdf?id=3eTr9dGwJv

## Abstract

Mobile manipulators in households must both navigate and manipulate. This requires a compact, semantically rich scene representation that captures where objects are, how they function, and which parts are actionable. Scene graphs are a natural choice, yet prior work often separates spatial and functional relations, treats scenes as static snapshots without object states or temporal updates, and overlooks information most relevant for accomplishing the current task. To overcome these shortcomings, we introduce MomaGraph, a unified scene representation for embodied agents that integrates spatial-functional relationships and part-level interactive elements. However, advancing such a representation requires both suitable data and rigorous evaluation, which have been largely missing. To address this, we construct MomaGraph-Scenes, the first large-scale dataset of richly annotated, task-driven scene graphs in household environments, and design MomaGraph-Bench, a systematic evaluation suite spanning six reasoning capabilities from high-level planning to fine-grained scene understanding. Built upon this foundation, we further develop MomaGraph-R1, a 7B vision–language model trained with reinforcement learning on MomaGraph-Scenes. MomaGraph-R1 predicts task-oriented scene graphs and serves as a zero-shot task planner under a Graph-then-Plan framework. Extensive experiments show that our model achieves state-of-the-art results among open-source models, reaching 71.6% accuracy on the benchmark (+11.4% over the best baseline), while generalizing across public benchmarks and transferring effectively to real-robot experiments. More visualizations and robot demonstrations are available at https://momagraph.github.io/.

## One-Sentence Claim

MomaGraph gives embodied agents a task-oriented scene-graph representation and VLM planner that integrate spatial, functional, state, and part-level action information for household mobile manipulation.

## Problem

Household mobile manipulators need compact scene representations for navigation and manipulation, but prior scene graphs often separate spatial and functional relations, ignore object states and temporal updates, and omit task-relevant part affordances.

## Core Contribution

The paper introduces MomaGraph, MomaGraph-Scenes, MomaGraph-Bench, and MomaGraph-R1: respectively a unified scene-graph representation, a richly annotated household dataset, a six-capability evaluation suite, and a 7B VLM trained with RL for task-oriented graph prediction and planning.

## Method

MomaGraph represents household scenes with spatial-functional relationships and part-level interactive elements. MomaGraph-R1 predicts task-oriented scene graphs and uses a Graph-then-Plan framework for zero-shot task planning.

## Experiments and Evidence

The abstract reports 71.6% benchmark accuracy, +11.4% over the best baseline among open-source models, generalization across public benchmarks, and transfer to real-robot experiments.

## Limits and Failure Modes

PDF checks needed: annotation schema, robot domains, temporal update fidelity, failure under perception noise, and whether Graph-then-Plan scales to cluttered or dynamic homes.

## Deep Themes

- Embodied AI needs structured world models, not only end-to-end policies.
- Scene representations are becoming task-conditioned and state-aware.
- VLMs are being trained to produce intermediate planning artifacts.

## Subthemes

- Embodied task planning.
- Scene graphs.
- Mobile manipulation.
- Part affordances.
- Graph-then-plan VLMs.

## Connections to Other Papers

Connects to FlashWorld, Visual Symbolic Mechanisms, LIMSSR, and other multimodal/world-model papers. It provides a robotics-facing counterpart to generative 3D scene and VLM spatial reasoning work.

## Notes for Cross-Paper Synthesis

MomaGraph supports the pattern that intermediate structured representations are becoming central for embodied reasoning: the model does not only answer; it constructs a task-relevant world graph.

## Full-Text Upgrade

Source used: `conferences/iclr-2026/text/00014-momagraph-state-aware-unified-scene-graphs-with-vision-language-models-for-embodied-task-planning-3eTr9dGwJv-arxiv.txt`.

Additional verified details:

- MomaGraph explicitly represents task-specific scene graphs with relevant objects, parts, and spatial-functional relationships.
- MomaGraph-R1 is trained from Qwen-2.5-VL-7B with reinforcement learning and a graph-alignment reward.
- The graph captures state changes and can prune irrelevant object parts, letting the graph evolve from ambiguous to task-specific.
- MomaGraph-Bench contains 294 indoor scenes, 1,446 multi-view images, 352 task-oriented scene graphs, and 1,315 multi-choice VQA questions.
- Unified spatial-functional graphs outperform spatial-only and functional-only variants in the reported motivation experiments.
- Graph-then-Plan improves performance across evaluated models, suggesting the graph intermediate representation is broadly helpful.
- Real-robot deployment uses active perception with head-pose adjustment before graph prediction and planning.

Refined limits:

- The evaluation is centered on household mobile manipulation; other robotics domains may need different graph schemas.
- Graph quality depends on perception and the model's ability to keep task relevance while pruning.
