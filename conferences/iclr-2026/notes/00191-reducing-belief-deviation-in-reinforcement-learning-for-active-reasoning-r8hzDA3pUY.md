# Reducing Belief Deviation in Reinforcement Learning for Active Reasoning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: r8hzDA3pUY
- Authors: Deyu Zou; Yongqiang Chen; Jianxiang Wang; Garry YANG; Mufei Li; Qing Da; James Cheng; Pan Li; Yu Gong
- Primary area: foundation or frontier models, including LLMs
- Keywords: Large language models;LLM reasoning;Agentic multi-turn reasoning
- Source URL: https://openreview.net/forum?id=r8hzDA3pUY
- PDF URL: https://openreview.net/pdf?id=r8hzDA3pUY

## Abstract

Active reasoning requires large language models (LLMs) to interact with external sources and strategically gather information to solve problems. Central to this process is belief tracking: maintaining a coherent understanding of the problem state and the missing information toward the solution. However, due to limited reasoning capabilities, LLM-based agents often suffer from belief deviation: they struggle to correctly model beliefs, lose track of problem states, and fall into uninformative or repetitive actions. Once this happens, errors compound and reinforcement learning (RL) training fails to properly credit the crucial exploratory steps.  To address this issue, we propose to track the deviation of model beliefs and develop $\mathbf{T^3}$, a simple yet effective method that detects excessive belief deviation and truncates trajectories during training to remove uninformative tails. By preserving credit for informative prefixes, $\mathbf{T^3}$ systematically improves policy optimization. Across 5 challenging tasks, $\mathbf{T^3}$ consistently enhances training stability, token efficiency, and final performance, achieving up to 30\% gains while cutting rollout tokens by roughly 25\%. These results highlight belief control as a key principle for developing robust and generalizable LLM-based active reasoners.

## One-Sentence Claim

T3 improves RL training for active reasoning agents by detecting belief deviation and truncating uninformative trajectory tails so credit remains focused on useful exploratory prefixes.

## Problem

Active reasoning agents must track what they know, what remains missing, and which external actions could reduce uncertainty. When belief tracking drifts, agents repeat low-value actions or lose the problem state, and RL credit assignment can reward or punish the wrong parts of a trajectory.

## Core Contribution

The paper identifies belief deviation as a key failure mode in multi-turn LLM reasoning and proposes T3, a trajectory truncation method that removes tails with excessive belief deviation during training.

## Method

T3 tracks model belief deviation over active reasoning trajectories. When deviation becomes excessive, it truncates the trajectory, discarding uninformative or repetitive tails while preserving the informative prefix for policy optimization. This aims to stabilize RL credit assignment.

## Experiments and Evidence

Across five challenging tasks, the abstract reports improved training stability, token efficiency, and final performance, with up to 30 percent gains and about 25 percent fewer rollout tokens.

## Limits and Failure Modes

Belief deviation measurement may be task-specific, and aggressive truncation could remove late recovery steps or exploratory detours that would have succeeded. Full-text review should check deviation metrics, truncation thresholds, RL algorithm details, task suite, and whether improvements persist under harder external-tool environments.

## Deep Themes

- Belief tracking for active reasoning.
- Process diagnostics for RL credit assignment.
- Token-efficient agent training.
- Multi-turn reasoning stability.

## Subthemes

- Trajectory tail truncation.
- Informative prefix preservation.
- Repetitive action suppression.
- Belief deviation detection.
- Active information gathering.

## Connections to Other Papers

Connects to DECS, LoongRL, MemAgent, and BIRD-INTERACT through process-level reasoning control, and to agent benchmark papers where interaction quality and state tracking determine performance.

## Notes for Cross-Paper Synthesis

T3 reinforces the idea that RL for agents needs diagnostics over the trajectory, not only final rewards. The useful training signal may be the point where reasoning starts to drift.
