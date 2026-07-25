# Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: kdeiRledV6
- Authors: Shuyang Jiang; Yusheng Liao; Ya Zhang; Yanfeng Wang; Yu Wang
- Primary area: foundation or frontier models, including LLMs
- Keywords: efficient reasoning; curriculum sampling with decoupled reward
- Source URL: https://openreview.net/forum?id=kdeiRledV6
- PDF URL: https://openreview.net/pdf?id=kdeiRledV6

## Abstract

While large reasoning models trained with critic-free reinforcement learning and verifiable rewards (RLVR) represent the state-of-the-art, their practical utility is hampered by ``overthinking'', a critical issue where models generate excessively long reasoning paths without any performance benefit. Existing solutions that penalize length often fail, inducing performance degradation due to a fundamental misalignment between trajectory-level rewards and token-level optimization. In this work, we introduce a novel framework, DECS, built on our theoretical discovery of two previously unaddressed flaws in current length rewards: (1) the erroneous penalization of essential exploratory tokens and (2) the inadvertent rewarding of partial redundancy. Our framework's innovations include (i) a first-of-its-kind decoupled token-level reward mechanism that surgically distinguishes and penalizes redundant tokens, and (ii) a novel curriculum batch scheduling strategy to master the efficiency-efficacy equilibrium. Experimental results show DECS can achieve a dramatic reduction in reasoning tokens by over 50\% across seven benchmarks while simultaneously maintaining or even improving performance. It demonstrates conclusively that substantial gains in reasoning efficiency can be achieved without compromising a model's underlying reasoning power. Code is available at \url{https://github.com/pixas/DECS}.

## One-Sentence Claim

DECS reduces reasoning overthinking by separating redundant-token penalties from useful exploratory reasoning and scheduling curricula to preserve accuracy while cutting token use.

## Problem

RLVR-trained reasoning models often generate long reasoning traces that do not improve final correctness. Simple length penalties can damage performance because token-level optimization and trajectory-level rewards are misaligned: essential exploration may be penalized, while partially redundant reasoning may still be rewarded.

## Core Contribution

The paper identifies two flaws in existing length rewards and introduces a framework with decoupled token-level rewards plus curriculum batch scheduling. The key claim is that efficient reasoning can be trained without weakening the underlying reasoning skill.

## Method

DECS uses a token-level reward mechanism that distinguishes redundant reasoning tokens from necessary exploratory tokens, then applies curriculum scheduling to manage the efficiency-efficacy tradeoff during RL training. The framework is designed to align the local training signal with the desired shorter-but-correct trajectory behavior.

## Experiments and Evidence

Across seven benchmarks, the abstract reports more than 50 percent reduction in reasoning tokens while maintaining or improving task performance. The paper also provides code at the listed GitHub repository.

## Limits and Failure Modes

The distinction between exploratory and redundant tokens may be benchmark- and verifier-dependent. Excessive pressure for brevity could remove reasoning that helps robustness, uncertainty calibration, or interpretability. Full-text review should check reward definitions, token-labeling criteria, curriculum schedule, benchmark mix, and whether gains hold on genuinely hard out-of-distribution reasoning tasks.

## Deep Themes

- Reasoning efficiency without capability loss.
- Token-level reward design for RLVR.
- Process supervision through decoupled rewards.
- Curriculum scheduling for inference-cost control.

## Subthemes

- Overthinking reduction.
- Redundant-token penalties.
- Essential exploration preservation.
- Efficiency-efficacy equilibrium.
- Critic-free verifiable-reward training.

## Connections to Other Papers

Connects to Prophet and speculative decoding papers through inference-efficiency goals, to MemAgent through RL over reasoning process behavior, and to reward-modeling work through the need for local training signals that match global task objectives.

## Notes for Cross-Paper Synthesis

DECS fits the theme that test-time cost is now a first-class alignment target. The key idea is not simply shorter answers but reward decomposition that protects useful cognitive work while removing waste.
