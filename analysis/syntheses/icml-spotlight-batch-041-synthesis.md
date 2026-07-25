# ICML 2026 Spotlight Batch 041 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 201-205:

- Focus and Dilution: The Multi-stage Learning Process of Attention
- Mitigating Hallucinations in Large Vision-Language Models via Causal Route Gating
- Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models
- OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning
- Second-Order Smooth Planning with Optimal-Transport Bellman Smoothing

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 200.

## Emerging Pattern 1: Attention Behavior Has Stage Structure

The focus-dilution paper explains attention learning as repeated cycles: early rank-one condensation, frequency-driven focus, mass redistribution, and symmetry breaking into new embedding directions. This gives a mechanistic training-dynamics account rather than a static architectural explanation.

This connects to PoPE, Robust Filter Attention, and NSE theory. The common direction is to explain model behavior through underlying dynamics, not just final learned representations.

## Emerging Pattern 2: Multimodal Reliability Depends on Causal Routes

Causal route gating argues that LVLM hallucination can happen even when visual tokens receive attention, because the text route dominates the final decision. The method suppresses only prior-dominant text routes while preserving visual routes.

This links tightly to VGS and FlowGuard. The multimodal cluster is converging on route/component decomposition: visual evidence, language priors, and fused decisions must be separately tracked.

## Emerging Pattern 3: Safety Features Can Persist Beneath Failed Behavior

The jailbreak mechanisms paper finds that attacks suppress early compromised heads but leave mid-layer safety-aligned activations available. Reading those robust harmful features can support training-free detection.

This complements tail-risk estimation and route gating. Safety is increasingly analyzed as a causal pathway problem: whether internal safety evidence exists, whether it is suppressed, and whether it controls output decisions.

## Emerging Pattern 4: Robotics Generalization Needs Embodiment-Balanced Data

OXE-AugE addresses a concrete imbalance in Open X-Embodiment, where a few robot types dominate. Its augmentation pipeline adds diverse embodiments and improves fine-tuned generalist policies on unseen robot-gripper combinations.

This links to XR-1, Posterior Behavioral Cloning, VOTP, and APB. Cross-embodiment generalization depends on dataset morphology and data balance, not just model scale.

## Emerging Pattern 5: Planning Efficiency Comes From Higher-Order Smoothness

SecondOrderSmoothCruiser shows that the local Taylor remainder order controls sample complexity and uses OT-smoothed Bellman backups to move from first-order epsilon^-4 to second-order epsilon^-3 complexity.

This connects to NonZero, compute-bounded RL, and OT-DRO. The broader planning theme is that mathematical smoothing and problem structure can reduce simulator or search budgets.

## Cross-Batch Links

- Focus-dilution, PoPE, and Robust Filter Attention all expose attention/position behavior through mathematical dynamics.
- Causal route gating, VGS, FlowGuard, and 3ViewSense address multimodal failures by creating explicit grounding interfaces.
- Robust harmful features, tail-risk estimation, and jailbreak/safety papers all move safety evaluation toward internal and distributional diagnostics.
- OXE-AugE and XR-1 build complementary robotics scale stories: one through embodiment-balanced data, the other through unified motion representations.
- SecondOrderSmoothCruiser, NonZero, and compute-bounded RL all treat planning/search compute as a resource shaped by mathematical structure.

## Deep Theme Update

Batch 041 is about causal and structural control: training dynamics follow stages, hallucinations follow route competition, jailbreaks suppress specific heads, robot transfer depends on embodiment balance, and planner sample complexity depends on smoothness order. Each paper identifies a hidden mechanism and turns it into a control handle.
