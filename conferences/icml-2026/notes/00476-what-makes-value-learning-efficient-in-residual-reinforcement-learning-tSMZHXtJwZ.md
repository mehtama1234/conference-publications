# What Makes Value Learning Efficient in Residual Reinforcement Learning?

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: tSMZHXtJwZ
- Authors: Guozheng Ma; Lu Li; Haoyu Wang; Zixuan Liu; Pierre-Luc Bacon; Dacheng Tao
- Primary area: reinforcement_learning->deep_rl
- Keywords: residual reinforcement learning;value learning;sample efficiency;critic warmup;normalization
- Source URL: https://openreview.net/forum?id=tSMZHXtJwZ
- PDF URL: https://openreview.net/pdf?id=tSMZHXtJwZ

## Abstract

Residual reinforcement learning (RL) enables stable online refinement of expressive pretrained policies by freezing the base and learning only bounded corrections. However, value learning in residual RL poses unique challenges that remain poorly understood. In this work, we identify two key bottlenecks: cold start pathology, where the critic lacks knowledge of the value landscape around the base policy, and structural scale mismatch, where the residual contribution is dwarfed by the base action. Through systematic investigation, we uncover the mechanisms underlying these bottlenecks, revealing that simple yet principled solutions suffice: base-policy transitions serve as an essential value anchor for implicit warmup, and critic normalization effectively restores representation sensitivity for discerning value differences. Based on these insights, we propose DAWN (Data-Anchored Warmup and Normalization), a minimal approach targeting efficient value learning in residual RL. By addressing these bottlenecks, DAWN demonstrates substantial efficiency gains across diverse benchmarks, policy architectures, and observation modalities.

## One-Sentence Claim

DAWN improves residual RL value learning by anchoring critics on base-policy transitions and normalizing critic representations so bounded residual actions remain value-discernible.

## Problem

Residual RL refines a pretrained policy by freezing the base policy and learning bounded corrective actions. This is attractive because it preserves stable base behavior while enabling online improvement, but value learning becomes unusually difficult.

The paper identifies two bottlenecks: cold start pathology, where the critic does not understand the value landscape around the base policy, and structural scale mismatch, where the residual action's contribution is small compared with the base action. Without addressing these, residual policies may be safe but sample-inefficient.

## Core Contribution

The paper provides a systematic explanation of why value learning is hard in residual RL and proposes DAWN, Data-Anchored Warmup and Normalization. DAWN uses base-policy transitions as value anchors and critic normalization to restore sensitivity to residual-induced value differences.

The contribution is deliberately minimal: rather than a large new residual policy architecture, it isolates two value-learning pathologies and shows simple targeted fixes.

## Method

Base-policy transitions provide implicit critic warmup by exposing the value function near the behavior that the residual policy will initially refine. This prevents the critic from starting blind in the neighborhood most relevant to safe online improvement.

Critic normalization rescales representations or targets so that the relatively small residual component is not drowned by the base action. Together, anchoring and normalization make value gradients informative for bounded corrections.

## Experiments and Evidence

The abstract reports substantial efficiency gains across diverse benchmarks, policy architectures, and observation modalities. The evidence is positioned as systematic investigation plus broad empirical validation.

Full-paper reading should verify which residual RL baselines were used, how warmup data is collected, normalization details, sample-efficiency metrics, and whether gains hold when the base policy is weak or miscalibrated.

## Limits and Failure Modes

DAWN assumes the base policy is useful enough to anchor value learning. If the base policy is poor, unsafe, or far from optimal regions, anchoring critics near it may slow discovery of qualitatively different behaviors.

Normalization can also mask scale information if poorly designed. The method improves residual correction, but it does not eliminate exploration or distribution-shift issues in online RL.

## Deep Themes

- Base policies as learning anchors: pretrained behavior supplies a local value landscape for refinement.
- Residual scale sensitivity: small corrections require critics that can resolve fine value differences.
- Minimal fixes for sample efficiency: targeted diagnostics can outperform complex algorithmic changes.
- Safe online adaptation: residual RL sits between imitation and unrestricted policy improvement.

## Subthemes

- Cold critics are especially harmful when action changes are bounded.
- Value representation normalization changes what residual effects are visible.
- Residual RL efficiency depends on critic design as much as policy design.
- Observation-modality robustness matters for general residual-refinement claims.

## Connections to Other Papers

DAWN connects to Conformal Policy Control, JitRL, and post-training policy-gradient theory. All study how to improve a policy around an existing safe or pretrained behavior without uncontrolled exploration.

It also relates to SOL and ScaleMoE in the RL scaling cluster, but focuses on critic learning efficiency rather than hierarchy or capacity.

## Notes for Cross-Paper Synthesis

The synthesis point is that refinement methods depend on the base system as a reference geometry. Whether in RL, LLM post-training, or safety calibration, improvement is easiest near behavior the model already supports.
