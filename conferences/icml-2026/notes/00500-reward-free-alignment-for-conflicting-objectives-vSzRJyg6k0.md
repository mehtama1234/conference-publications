# Reward-free Alignment for Conflicting Objectives

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: vSzRJyg6k0
- Authors: Peter Chen; Xiaopeng Li; Xi Chen; Tianyi Lin
- Primary area: deep_learning->large_language_models
- Keywords: Multi-Objective Alignment;Multi-Objective Optimization;LLM Preference Alignment;AI Safety
- Source URL: https://openreview.net/forum?id=vSzRJyg6k0
- PDF URL: https://openreview.net/pdf?id=vSzRJyg6k0

## Abstract

Direct alignment methods are increasingly used to align large language models (LLMs) with human preferences. However, many real-world alignment problems involve multiple conflicting objectives, where naive aggregation of preferences can lead to unstable training and poor trade-offs. In particular, weighted loss methods may fail to identify update directions that simultaneously improve all objectives, and existing multi-objective approaches often rely on explicit reward models, introducing additional complexity and distorting user-specified preferences. The contributions of this paper are two-fold. First, we propose a **R**eward-free **A**lignment framework for **C**onflicted **O**bjectives (RACO) that directly leverages pairwise preference data and resolves gradient conflicts via a novel clipped variant of conflict-averse gradient descent. We provide convergence guarantees to Pareto-critical points that respect user-specified objective weights, and further show that clipping can strictly improve convergence rate in the two-objective setting. Second, we improve our method using some heuristics and conduct experiments to demonstrate the compatibility of the proposed framework for LLM alignment. Both qualitative and quantitative evaluations on multi-objective summarization and safety alignment tasks across multiple LLM families (Qwen 3, Llama 3, Gemma 3) show that our method consistently achieves better Pareto trade-offs compared to existing multi-objective alignment baselines.

## One-Sentence Claim

RACO aligns LLMs under conflicting objectives without reward models by resolving preference-gradient conflicts through clipped conflict-averse descent toward user-weighted Pareto-critical points.

## Problem

Real alignment problems often involve multiple objectives, such as helpfulness, safety, style, and factuality, that conflict. Naively aggregating preferences with weighted losses can produce unstable training or poor tradeoffs because gradient directions may improve one objective while harming another.

Existing multi-objective alignment approaches often use explicit reward models, adding complexity and risking distortion of user-specified preferences. The paper seeks direct reward-free alignment from pairwise preference data.

## Core Contribution

The paper proposes RACO, Reward-free Alignment for Conflicted Objectives. It directly leverages pairwise preferences and resolves gradient conflicts through a clipped variant of conflict-averse gradient descent.

The theory provides convergence guarantees to Pareto-critical points respecting user-specified objective weights, and shows clipping can strictly improve convergence rate in the two-objective setting. Experiments show better Pareto tradeoffs across LLM families.

## Method

RACO forms objective-specific preference gradients from pairwise data. When gradients conflict, it modifies the update direction using clipped conflict-averse descent so that training moves toward a weighted Pareto-critical solution rather than a naive scalarized compromise.

Heuristics improve practical compatibility for LLM alignment. The method remains reward-free because it does not train or query explicit reward models.

## Experiments and Evidence

The abstract reports qualitative and quantitative evaluations on multi-objective summarization and safety alignment across Qwen 3, Llama 3, and Gemma 3. RACO consistently achieves better Pareto tradeoffs than existing multi-objective alignment baselines.

Full-paper reading should verify preference-data construction, objective definitions, Pareto metrics, stability curves, and how user weights are respected in practice.

## Limits and Failure Modes

Pairwise preferences must still reflect the intended objectives. Reward-free does not mean supervision-free, and conflicting human preferences may be inconsistent or underspecified.

Pareto-critical convergence is not the same as choosing the socially right tradeoff. User-specified weights can encode poor priorities, and deployment may require dynamic rather than fixed weights.

## Deep Themes

- Multi-objective alignment without reward models: preferences directly shape Pareto-aware updates.
- Gradient conflict as alignment bottleneck: objective disagreement appears in update geometry.
- User-weighted Pareto criticality: alignment target is a tradeoff surface, not one scalar optimum.
- Clipping for convergence: update constraints can improve multi-objective optimization rates.

## Subthemes

- Weighted losses may fail when gradients conflict.
- Reward models can distort preferences.
- Summarization and safety provide natural conflicting-objective settings.
- Pareto tradeoff quality is the central evaluation object.

## Connections to Other Papers

RACO connects to BLL-Loss, DPO/RLHF equivalence work, PLAINTAIN, and post-training policy-gradient theory through alignment objective design. It also pairs with the diffusion score-alignment paper in this batch: both avoid external rewards by moving alignment into the training objective.

It relates to MORetro* and fair OT because all optimize under explicit tradeoff/frontier structure.

## Notes for Cross-Paper Synthesis

The synthesis point is that alignment is increasingly multi-objective and geometry-aware. The central problem is no longer only preference learning, but conflict resolution among valid objectives.
