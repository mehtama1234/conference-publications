# Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: kMuQBgPIdg
- Authors: Zhiyu Mou; Yiqin Lv; Miao Xu; Cheems Wang; Yixiu Mao; Jinghao Chen; Qichen Ye; Chao Li; Rongquan Bai; Chuan Yu; Jian Xu; Bo Zheng
- Primary area: applications to robotics, autonomy, planning
- Keywords: auto-bidding;offline reinforcement learning;generative decision making
- Source URL: https://openreview.net/forum?id=kMuQBgPIdg
- PDF URL: https://openreview.net/pdf?id=kMuQBgPIdg

## Abstract

Auto-bidding serves as a critical tool for advertisers to improve their advertising performance. Recent progress has demonstrated that AI-Generated Bidding (AIGB), which learns a conditional generative planner from offline data, achieves superior performance compared to typical offline reinforcement learning (RL)-based auto-bidding methods. However, existing AIGB methods still face a performance bottleneck due to their inherent inability to explore beyond the static offline dataset. To address this, we propose AIGB-Pearl (Planning with EvaluAtor via RL),  a novel method that integrates generative planning and policy optimization. The core of AIGB-Pearl lies in constructing a trajectory evaluator for scoring generation quality and designing a provably sound KL-Lipschitz-constrained score maximization scheme to ensure safe and efficient generalization beyond the offline dataset. A practical algorithm incorporating the synchronous coupling technique is further devised to ensure the model regularity required by the proposed scheme. Extensive experiments on both simulated and real-world advertising systems demonstrate the state-of-the-art performance of our approach.

## One-Sentence Claim

AIGB-Pearl improves generative auto-bidding by adding an offline trajectory evaluator and constrained policy search that lets generated bidding plans safely generalize beyond the static offline dataset.

## Problem

Generative auto-bidding planners can imitate high-quality offline trajectories, but static offline data limits exploration and creates a performance ceiling. Pure offline RL must also avoid unsafe extrapolation in high-stakes advertising systems where generated bids affect budgets and returns.

## Core Contribution

The paper introduces AIGB-Pearl, integrating generative planning with policy optimization through a trajectory evaluator and a provably sound KL-Lipschitz-constrained score-maximization scheme. It also provides a practical synchronous-coupling algorithm to maintain the regularity assumptions needed by the scheme.

## Method

The method trains or constructs an offline evaluator to score generated bidding trajectories, then searches for policies or generated plans that maximize evaluator score while constrained by KL and Lipschitz regularity. Synchronous coupling is used to make the practical generative-policy update conform to the theoretical safe-generalization conditions.

## Experiments and Evidence

The abstract reports extensive experiments on simulated and real-world advertising systems, with state-of-the-art performance over existing AI-generated bidding and offline-RL auto-bidding baselines.

## Limits and Failure Modes

Offline evaluators can be biased, and score maximization can exploit evaluator errors if constraints are insufficient. Real ad systems are nonstationary, multi-agent, budget-constrained, and affected by auction dynamics, so deployment validity depends on calibration and guardrails. Full-text review should check evaluator training data, off-policy evaluation assumptions, constraint proofs, online A/B evidence, and failure analysis under distribution shift.

## Deep Themes

- Generative decision-making beyond imitation.
- Offline reward evaluation as a search guide.
- Safe extrapolation beyond static logs.
- Constrained policy optimization for commercial autonomy.

## Subthemes

- KL-Lipschitz-constrained score maximization.
- Trajectory evaluators for generated plans.
- Synchronous coupling for regularity.
- Auto-bidding and budgeted decision systems.
- Offline-to-real-world policy improvement.

## Connections to Other Papers

Connects to ExDM through generative models for control, to AutoEP through evaluator-guided search, and to offline RL and reward-model papers through the tension between optimizing learned scores and staying inside reliable support.

## Notes for Cross-Paper Synthesis

This paper fits the broader pattern of adding a verifier or evaluator around a generative model. The system gains power by searching beyond logged behavior, but its trustworthiness hinges on explicit constraints and evaluator reliability.
