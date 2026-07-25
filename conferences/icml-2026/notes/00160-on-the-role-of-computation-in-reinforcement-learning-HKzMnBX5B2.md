# On the Role of Computation in Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: HKzMnBX5B2
- Authors: Raj Ghugare; Michał Bortkiewicz; Alicja Ziarko; Benjamin Eysenbach
- Primary area: reinforcement_learning
- Keywords: Reinforcement Learning;Recurrent Networks;Horizon generalization;Computation theory.
- Source URL: https://openreview.net/forum?id=HKzMnBX5B2
- PDF URL: https://openreview.net/pdf?id=HKzMnBX5B2

## Abstract

How does the amount of compute available to a reinforcement learning (RL) policy affect its learning? Can policies using a fixed amount of parameters, still benefit from additional compute? The standard RL framework does not provide a language to answer these questions formally. Empirically, deep RL policies are often parameterized as neural networks with static architectures, conflating the amount of compute and the number of parameters. In this paper, we formalize compute bounded policies and prove that policies which use more compute can solve problems and generalize to longer-horizon tasks that are outside the scope of policies with less compute. Building on prior work in algorithmic learning and model-free planning, we propose a minimal architecture that can use a variable amount of compute. Our experiments complement our theory. On a set 31 different tasks spanning online and offline RL, we show that $(1)$ this architecture achieves stronger performance simply by using more compute, and $(2)$ stronger generalization on longer-horizon test tasks compared to standard feedforward networks or deep residual network using upto 5 times more parameters.

## One-Sentence Claim

Compute-bounded RL formalizes how policies with fixed parameter counts can gain capability and horizon generalization by using more computation at decision time.

## Problem

Standard RL theory and neural policy design often conflate model size with computation, leaving little formal language for understanding policies that spend variable compute while keeping parameters fixed.

## Core Contribution

The paper defines compute-bounded policies, proves that extra compute expands solvable and generalizable task classes, and proposes a minimal variable-compute architecture for RL.

## Method

Building on algorithmic learning and model-free planning, the authors formalize policies with bounded computation and compare a variable-compute architecture against static feedforward and residual policies.

## Experiments and Evidence

The abstract reports theory showing compute can solve problems beyond lower-compute policies, plus experiments on 31 online and offline RL tasks where using more compute improves performance and longer-horizon generalization, even compared with residual networks using up to five times more parameters.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: compute metric, architecture details, task suite composition, inference-time cost, stopping rules, and whether extra compute remains useful under real-time robotic constraints.

## Deep Themes

- Test-time computation as a distinct axis of RL capability.
- Horizon generalization through algorithmic processing, not only larger policies.
- Formal abstractions catching up to practical adaptive inference.

## Subthemes

- Compute-bounded policies.
- Recurrent architectures.
- Model-free planning.
- Online and offline RL.
- Long-horizon generalization.
- Parameters versus inference compute.

## Connections to Other Papers

Connects to test-time scaling papers, SOAR, and long-context sequence-modeling work that separates stored capacity from computation used during deployment. It also complements Posterior BC by focusing on finetuning/deployment dynamics rather than static pretrained accuracy.

## Notes for Cross-Paper Synthesis

This paper adds a clean RL example of a broad 2026 pattern: capability increasingly depends on controllable inference-time process, not just the frozen parameter count or training objective.
