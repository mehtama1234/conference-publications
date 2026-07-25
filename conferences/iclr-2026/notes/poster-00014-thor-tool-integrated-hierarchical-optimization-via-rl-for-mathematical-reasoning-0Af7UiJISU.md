# THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 0Af7UiJISU
- Authors: Qikai Chang; Zhenrong Zhang; Pengfei Hu; Jun Du; Jiefeng Ma; Yicheng Pan; Jianshu Zhang; Quan Liu; Jianqing Gao
- Primary area: other topics in machine learning (i.e., none of the above)
- Keywords: Large Language Models;Mathematical Problem Solving;Tool-Integrated Reasoning;Reinforcement Learning
- Source URL: https://openreview.net/forum?id=0Af7UiJISU
- PDF URL: https://openreview.net/pdf?id=0Af7UiJISU

## Abstract

Large Language Models (LLMs) have made remarkable progress in mathematical reasoning, but still continue to struggle with high-precision tasks like numerical computation and formal symbolic manipulation. Integrating external tools has emerged as a promising approach to bridge this gap. Despite recent advances, existing methods struggle with three key challenges: constructing tool-integrated reasoning data, performing fine-grained optimization, and enhancing inference. To overcome these limitations, we propose THOR (Tool-Integrated Hierarchical Optimization via RL). First, we introduce TIRGen, a multi-agent based pipeline for constructing high-quality datasets of tool-integrated reasoning paths, aligning with the policy and generalizing well across diverse models. Second, to perform fine-grained hierarchical optimization, we introduce an RL strategy that jointly optimizes for both episode-level problem solving and step-level code generation. This is motivated by our key insight that the success of an intermediate tool call is a strong predictor of the final answer's correctness. Finally, THOR incorporates a self-correction mechanism that leverages immediate tool feedback to dynamically revise erroneous reasoning paths during inference. Our approach demonstrates strong generalization across diverse models, performing effectively in both reasoning and non-reasoning models. It further achieves state-of-the-art performance for models of a similar scale on multiple mathematical benchmarks, while also delivering consistent improvements on code benchmarks. Our code will be publicly available at https://github.com/JingMog/THOR.

## One-Sentence Claim

THOR improves mathematical reasoning by training tool-integrated reasoning paths with hierarchical RL over both final answers and intermediate code/tool-call success.

## Problem

LLMs still struggle with high-precision numerical computation and symbolic manipulation. Tool use can help, but existing methods face difficulties constructing tool-integrated reasoning data, optimizing intermediate steps, and correcting errors during inference.

## Core Contribution

The paper contributes THOR, a tool-integrated hierarchical RL framework. It includes TIRGen, a multi-agent pipeline for constructing tool-integrated reasoning paths; a joint episode-level and step-level RL strategy; and a self-correction mechanism that uses immediate tool feedback at inference time.

## Method

TIRGen builds high-quality reasoning paths aligned with the policy. THOR then optimizes for final problem-solving success and intermediate code-generation/tool-call success, motivated by the claim that successful intermediate tool calls predict final correctness. At inference, immediate tool feedback triggers dynamic revision of erroneous reasoning paths.

## Experiments and Evidence

The abstract reports strong generalization across diverse reasoning and non-reasoning models, state-of-the-art performance for similarly sized models on multiple mathematical benchmarks, and consistent improvements on code benchmarks. Code is reported available at the listed GitHub repository.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect tool environment, benchmark suite, reward definitions, data-generation quality control, and whether step-level rewards induce shortcut code calls. Tool-integrated reasoning can become brittle when tools fail, have latency, or return misleading errors.

## Deep Themes

- Tool-integrated mathematical reasoning.
- Hierarchical RL over process and outcome.
- Intermediate tool-call success as credit signal.
- Self-correction from executable feedback.

## Subthemes

- THOR.
- TIRGen.
- Step-level code generation rewards.
- Episode-level problem solving.
- Dynamic inference-time revision.

## Connections to Other Papers

Connects to Tool-Augmented SSMs through external-tool use, to VERINA and CRAMF through formal/mathematical reasoning infrastructure, and to T3 through credit assignment over reasoning trajectories.

## Notes for Cross-Paper Synthesis

THOR adds to the process-supervision theme: final-answer RL is too coarse when intermediate tool calls determine correctness. The model is trained and corrected at the level where reasoning actually fails.
