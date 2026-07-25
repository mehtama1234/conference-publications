# How RL Unlocks the Aha Moment in Geometric Interleaved Reasoning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: JT4zAf3zDs
- Authors: Xiangxiang Zhang; Caijun Jia; Siyuan Li; he dingyu; Xiya Xiong; Zheng Sun; Honghao He; Yuchen Wu; Bihui Yu; Linzhuang Sun; Cheng Tan; Jingxuan Wei
- Primary area: reinforcement_learning->deep_rl
- Keywords: Reinforcement Learning;Interleaved Reasoning;Geometric Problem Solving;Multimodal Alignment;Code-as-Action
- Source URL: https://openreview.net/forum?id=JT4zAf3zDs
- PDF URL: https://openreview.net/pdf?id=JT4zAf3zDs

## Abstract

Solving complex geometric problems inherently requires interleaved reasoning: a tight alternation between constructing diagrams and performing logical deductions. Although recent Multimodal Large Language Models (MLLMs) have demonstrated strong capabilities in visual generation and plotting, we identify a counter-intuitive and underexplored phenomenon. Naively applying Supervised Fine-Tuning (SFT) on interleaved plot–solution data leads to a substantial degradation in reasoning performance compared to text-only baselines. We argue that this failure stems from a fundamental limitation of SFT, which primarily induces distributional alignment: the model learns to reproduce the surface format of interleaved plotting but fails to internalize the causal dependency between the generated plot and reasoning steps. To overcome this limitation, we propose Faire (**F**unctional **a**lignment for **i**nterleaved **re**asoning), a reinforcement learning framework that enforces three casual constraints to move beyond superficial imitation toward functional alignment. Extensive experiments show that Faire induces a qualitative shift in model behavior in which the plotting is effectively internalized, yielding competitive performance on challenging geometric reasoning benchmarks.

## One-Sentence Claim

Faire uses reinforcement learning to make multimodal models functionally align plotting actions with geometric reasoning rather than merely imitate interleaved plot-solution formats.

## Problem

Geometry problem solving requires alternating between diagram construction and logical deduction, but supervised fine-tuning on interleaved plot-solution data can degrade reasoning because it learns surface format without causal dependence between plots and reasoning steps.

## Core Contribution

The paper identifies SFT's distributional-alignment failure in geometric interleaved reasoning and proposes an RL framework that enforces causal constraints for functional alignment.

## Method

Faire trains MLLMs with reinforcement learning under three causal constraints designed to ensure generated plots are useful intermediate actions for subsequent reasoning, moving beyond imitation of the interleaved trace format.

## Experiments and Evidence

The abstract reports extensive experiments showing a qualitative behavioral shift where plotting becomes internalized and performance becomes competitive on challenging geometric reasoning benchmarks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact causal constraints, reward design, benchmark suite, comparison to text-only baselines, code-as-action execution assumptions, and whether learned plotting transfers beyond geometry.

## Deep Themes

- Functional alignment is stronger than format imitation.
- Multimodal reasoning needs causal coupling between actions and deductions.
- RL can unlock behaviors that SFT suppresses or only superficially copies.

## Subthemes

- Geometric reasoning.
- Interleaved plotting and solving.
- Multimodal large language models.
- Code-as-action.
- Reinforcement learning for reasoning.
- Causal constraints.

## Connections to Other Papers

Connects to TRM, SOAR, CE-Graph, and LALP through process-level reasoning optimization. It also links to 3ViewSense by using explicit visual/spatial intermediates to improve reasoning.

## Notes for Cross-Paper Synthesis

Faire adds a strong warning for reasoning data pipelines: traces are not enough if the model learns trace shape without learning why each intermediate action matters.
