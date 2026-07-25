# Learning Structured Reasoning via Tractable Trajectory Control

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: x6J7va4BYz
- Authors: Po-Nien Kung; Zhen Yang; Jeffrey Luo; Cheng-Fu Yang; Haikang Deng; Zi-Yi Dou; Yinfei Yang; Nanyun Peng; Zhe Gan; Kai-Wei Chang
- Primary area: reinforcement_learning->deep_rl
- Keywords: Reinforcement Learning;Large Language Models;Reasoning;Cognitive Behaviors
- Source URL: https://openreview.net/forum?id=x6J7va4BYz
- PDF URL: https://openreview.net/pdf?id=x6J7va4BYz

## Abstract

Large language models can exhibit emergent reasoning behaviors, often manifested as recurring lexical patterns (e.g., “wait,” indicating verification). However, complex reasoning trajectories remain sparse in unconstrained sampling, and standard RL often fails to guarantee the acquisition of diverse reasoning behaviors. We propose a systematic discovery and reinforcement of diverse reasoning patterns through structured reasoning, a paradigm that requires targeted exploration of specific reasoning patterns during the RL process.
To this end, we propose Ctrl-R, a framework for learning structured reasoning via tractable trajectory control that actively guides the rollout process, incentivizing the exploration of diverse reasoning patterns that are critical for complex problem-solving. The resulting behavior policy enables accurate importance-sampling estimation, supporting unbiased on-policy optimization. We further introduce a power-scaling factor on the importance-sampling weights, allowing the policy to selectively learn from exploratory, out-of-distribution trajectories while maintaining stable optimization.
Experiments demonstrate that Ctrl-R enables effective exploration and internalization of previously unattainable reasoning patterns, yielding consistent improvements across language and vision–language models on mathematical reasoning tasks.

## One-Sentence Claim

Ctrl-R improves reasoning RL by actively controlling rollouts toward diverse reasoning patterns and using importance sampling to learn from those exploratory trajectories without biased on-policy optimization.

## Problem

Complex reasoning behaviors in LLMs are sparse under unconstrained sampling. Standard RL can reinforce successful answers, but it may not reliably discover or internalize diverse reasoning patterns such as verification, backtracking, or other cognitive behaviors.

The problem is exploration: reasoning trajectories that would improve performance may be rare before the model has already learned them.

## Core Contribution

The paper proposes structured reasoning, where RL deliberately explores targeted reasoning patterns during rollout. Ctrl-R implements this through tractable trajectory control and then corrects for the controlled behavior policy with accurate importance-sampling estimates.

It also introduces a power-scaling factor on importance weights so learning can benefit from out-of-distribution exploratory trajectories while remaining stable.

## Method

Ctrl-R actively guides rollouts toward selected reasoning patterns. The resulting behavior policy is known or tractable enough to support unbiased on-policy optimization via importance sampling.

The power-scaling factor adjusts how strongly the learner uses exploratory trajectories, trading off stability against learning from behaviors that the current policy would rarely sample.

## Experiments and Evidence

The abstract reports consistent improvements across language and vision-language models on mathematical reasoning tasks.

It also reports that Ctrl-R enables exploration and internalization of reasoning patterns that were previously unattainable under ordinary sampling.

## Limits and Failure Modes

The approach depends on being able to specify or discover useful reasoning patterns. If the targeted patterns are shallow lexical markers rather than functional reasoning moves, the model may learn style without substance.

Because this note is abstract-only, details still need checking: pattern inventory, rollout controller, importance-weight variance, math benchmark suite, vision-language setup, and whether improvements persist under adversarial or out-of-domain problems.

## Deep Themes

- Reasoning as trajectory distribution: the process matters, not only the final answer.
- Exploration control for cognition: rare reasoning behaviors need targeted rollout support.
- Off-policy reasoning data with correction: importance sampling bridges guided exploration and on-policy RL.
- Internalization of cognitive behaviors: RL can make externally induced patterns part of the policy.

## Subthemes

- Verification markers such as "wait."
- Power-scaled importance weights.
- Structured reasoning pattern discovery.
- Mathematical reasoning in language and vision-language models.

## Connections to Other Papers

This connects to H1, RAGEN-2, DAWN, and reasoning dimensionality through RL-driven reasoning improvement and process-level diagnostics.

It also relates to Obfuscation Atlas because both study how RL pressure shapes trajectories, but Ctrl-R uses trajectory control to induce useful reasoning rather than detect deception.

## Notes for Cross-Paper Synthesis

The cross-paper point is that post-training increasingly targets trajectories rather than labels. Reasoning performance depends on which process modes the policy can explore and then stabilize.
