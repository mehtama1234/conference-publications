# ScaleMoE: Mixture-of-Experts for Scalable Continuous Control in Actor-Critic Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: oVS7o5jKJF
- Authors: Yi Ma; Chenjun Xiao; Hongyao Tang; Yaodong Yang; Jinyi Liu; Jing Liang; Jiye Liang
- Primary area: reinforcement_learning->deep_rl
- Keywords: Deep Reinforcement Learning;Mixture of Experts
- Source URL: https://openreview.net/forum?id=oVS7o5jKJF
- PDF URL: https://openreview.net/pdf?id=oVS7o5jKJF

## Abstract

Scaling network remains a bottleneck in deep reinforcement learning (RL): simply enlarging actor–critic networks destabilizes training and soon saturates performance. Although recent monolithic architectures such as SimBa and BRC have shown that carefully designed inductive biases can enable positive scaling up to a certain size, their improvements plateau soon as model parameters grow further. This work introduces ScaleMoE, a scalable RL architecture that integrates Mixture-of-Experts (MoE) modules into both the actor and critic of modern continuous control algorithms.  Two complementary gating schemes are studied: output-level aggregation of per-expert policies and Q-functions, and feature-level fusion of expert representations before a shared head. We instantiate ScaleMoE on two representative monolithic RL baselines: the single-task method SimBa and the multi-task method BRC. Experiments across the DeepMind Control Suite, MetaWorld, and HumanoidBench show that progressively increasing the number of experts (up to 64) yields substantial improvements in returns, significantly outperforming monolithic networks of comparable or even greater parameter counts. Results demonstrate that ScaleMoE provides an   efficient and effective scaling axis for deep RL in continuous control.

## One-Sentence Claim

ScaleMoE makes actor-critic continuous-control networks scale by replacing monolithic enlargement with expert specialization in both policy and value models.

## Problem

Deep RL does not reliably benefit from simply making actor-critic networks larger. Larger monolithic networks can destabilize training, saturate returns, and waste parameters even when supervised learning and LLMs often scale predictably.

Recent architectures such as SimBa and BRC improve scaling through inductive bias, but their gains plateau as size grows. Continuous control therefore needs a scaling axis that increases useful capacity without destabilizing actor-critic optimization.

## Core Contribution

ScaleMoE integrates Mixture-of-Experts modules into both actor and critic networks for continuous-control RL. The paper studies two gating schemes: output-level aggregation over per-expert policies/Q-functions and feature-level fusion of expert representations before shared heads.

The contribution is to show that expert count can be a productive scaling dimension for RL. Increasing experts up to 64 improves returns and can beat monolithic networks with comparable or greater parameter counts.

## Method

The method augments existing strong actor-critic baselines rather than replacing them wholesale. ScaleMoE is instantiated on SimBa for single-task control and BRC for multi-task control, letting the authors test whether MoE improves modern monolithic architectures.

Output-level aggregation allows different experts to propose policies or Q estimates whose outputs are combined. Feature-level fusion instead routes and combines expert hidden representations before a shared decision head, separating representational specialization from final action/value prediction.

## Experiments and Evidence

The abstract reports experiments on DeepMind Control Suite, MetaWorld, and HumanoidBench. Performance improves as the number of experts grows up to 64, and ScaleMoE substantially outperforms monolithic networks of comparable or larger parameter count.

Full-paper verification should inspect learning curves, variance across seeds, compute-normalized comparisons, router behavior, expert utilization, and whether gains persist across sparse-reward or high-dimensional tasks.

## Limits and Failure Modes

MoE introduces routing instability, expert imbalance, and additional hyperparameters. In RL, these risks are amplified by nonstationary data and bootstrapped value learning. Poor gating could destabilize training even if total capacity is high.

Deployment cost also depends on how many experts are active per step and whether expert specialization creates brittle behavior under distribution shift. The abstract emphasizes returns, but robustness and safety of learned control policies remain to be checked.

## Deep Themes

- Conditional capacity for RL: useful scaling comes from specialization rather than uniform network growth.
- Actor and critic co-scaling: both policy and value models need added capacity for stable improvements.
- MoE as an RL scaling axis: expert count becomes analogous to model width/depth in supervised scaling.
- Architecture over brute-force parameters: parameter count alone is not the right scaling variable for continuous control.

## Subthemes

- Output-level and feature-level gates encode different assumptions about where specialization should occur.
- Multi-task control naturally benefits from expert routing, but single-task scaling is also tested.
- RL scaling must be judged by stability and sample efficiency, not only final return.
- Expert specialization may serve as implicit decomposition of dynamics, skills, or task regimes.

## Connections to Other Papers

ScaleMoE connects to WestWorld through scalable robotics/control architectures that use conditional specialization. WestWorld routes by system and morphology for world modeling; ScaleMoE routes actor/critic capacity for policy learning.

It also connects to MoE compression work in this batch: one paper expands RL capacity with experts, while another prunes expert channels for efficient LLM deployment. Together they show MoE as both an opportunity and a systems burden.

## Notes for Cross-Paper Synthesis

The key pattern is that RL may need its own scaling laws and architecture families. MoE gives continuous control a way to scale useful capacity without the failure mode of oversized monoliths.
