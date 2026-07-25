# Offline Reinforcement Learning of High-Quality Behaviors Under Robust Style Alignment

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: jxdjDmWpNX
- Authors: Mathieu Petitbois; Rémy Portelas; Sylvain Lamprier
- Primary area: reinforcement_learning->batchoffline
- Keywords: Reinforcement Learning;Diversity in RL;Offline RL
- Source URL: https://openreview.net/forum?id=jxdjDmWpNX
- PDF URL: https://openreview.net/pdf?id=jxdjDmWpNX

## Abstract

We study offline reinforcement learning of style-conditioned policies using explicit style supervision via subtrajectory labeling functions. In this setting, aligning style with high task performance is particularly challenging due to distribution shift and inherent conflicts between style and reward. Existing methods, despite introducing numerous definitions of style, often fail to reconcile these objectives effectively. To address these challenges, we propose a unified definition of behavior style and instantiate it into a practical framework. Building on this, we introduce Style-Conditioned Implicit Q-Learning (SCIQL), which leverages offline goal-conditioned RL techniques, such as hindsight relabeling and value learning, and combine it with a new Gated Advantage Weighted Regression mechanism to efficiently optimize task performance while preserving style alignment. Experiments demonstrate that SCIQL achieves superior performance on both objectives compared to prior offline methods. Code, datasets and visuals are available in: https://mathieu-petitbois.github.io/projects/sciql/.

## One-Sentence Claim

SCIQL learns offline style-conditioned policies that preserve explicit behavior style while optimizing high task performance under distribution shift.

## Problem

Offline RL with style-conditioned policies must balance two goals: high reward and adherence to a specified style. These goals can conflict, and distribution shift makes it hard to optimize performance without drifting away from style.

Existing methods define style in many ways but often fail to reconcile style alignment with task quality.

## Core Contribution

The paper proposes a unified definition of behavior style using explicit style supervision through subtrajectory labeling functions. It introduces Style-Conditioned Implicit Q-Learning, which combines offline goal-conditioned RL techniques with a new Gated Advantage Weighted Regression mechanism.

The result is a practical framework that improves both task performance and style alignment relative to prior offline methods.

## Method

SCIQL uses hindsight relabeling and value learning from goal-conditioned offline RL to exploit available trajectories. Gated Advantage Weighted Regression controls when high-advantage actions should influence policy updates while preserving style constraints.

Subtrajectory labeling functions provide explicit style supervision at a finer temporal granularity than whole-trajectory labels.

## Experiments and Evidence

Evidence reported in the abstract:

- Unified definition of behavior style.
- Style supervision through subtrajectory labeling functions.
- SCIQL combines implicit Q-learning, hindsight relabeling, value learning, and gated advantage-weighted regression.
- Superior performance on both task reward and style alignment compared with prior offline methods.
- Code, datasets, and visuals released at the listed project URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: environments, style labels, reward-style conflict settings, and metrics.

## Limits and Failure Modes

- Explicit labeling functions may be hard to design for subtle or subjective styles.
- Style and reward may be fundamentally incompatible in some tasks.
- Offline support limits can prevent safe extrapolation to high-performing styled behaviors.
- Gating criteria may need tuning across datasets.

## Deep Themes

**Control objectives are multi-attribute.** Policies must optimize reward and behavioral style jointly.

**Style needs temporal supervision.** Subtrajectory labels make alignment more precise than whole-episode descriptors.

**Offline RL must manage distribution shift and identity of behavior.** The method tries to improve without leaving the desired style manifold.

## Subthemes

- Style-conditioned offline RL.
- Subtrajectory labeling functions.
- Gated Advantage Weighted Regression.
- Hindsight relabeling.
- Reward-style tradeoff.

## Connections to Other Papers

Connects to TG-DT, Distributional IRL, RePO, and alignment-feedback papers. It extends preference/style alignment into offline control rather than LLM text generation.

## Notes for Cross-Paper Synthesis

SCIQL contributes a control-side alignment theme: desired behavior is not only about success, but about preserving qualitative style under optimization pressure.
