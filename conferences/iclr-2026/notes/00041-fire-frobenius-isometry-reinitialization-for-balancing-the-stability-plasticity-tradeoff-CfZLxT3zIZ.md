# FIRE: Frobenius-Isometry Reinitialization for Balancing the Stability–Plasticity Tradeoff

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: CfZLxT3zIZ
- Authors: Isaac Han; Sangyeon Park; Seungwon Oh; Donghu Kim; Hojoon Lee; KyungJoong Kim
- Primary area: transfer learning, meta learning, and lifelong learning
- Keywords: stability-plasticity tradeoff;continual learning
- Source URL: https://openreview.net/forum?id=CfZLxT3zIZ
- PDF URL: https://openreview.net/pdf?id=CfZLxT3zIZ

## Abstract

Deep neural networks trained on nonstationary data must balance stability (i.e., retaining prior knowledge) and plasticity (i.e., adapting to new tasks). Standard reinitialization methods, which reinitialize weights toward their original values, are widely used but difficult to tune: conservative reinitializations fail to restore plasticity, while aggressive ones erase useful knowledge. We propose FIRE, a principled reinitialization method that explicitly balances the stability–plasticity tradeoff. FIRE quantifies stability through Squared Frobenius Error (SFE), measuring proximity to past weights, and plasticity through Deviation from Isometry (DfI), reflecting weight isotropy. The reinitialization point is obtained by solving a constrained optimization problem, minimizing SFE subject to DfI being zero, which is efficiently approximated by Newton–Schulz iteration. FIRE is evaluated on continual visual learning (CIFAR-10 with ResNet-18), language modeling (OpenWebText with GPT-0.1B), and reinforcement learning (HumanoidBench with SAC and Atari games with DQN). Across all domains, FIRE consistently outperforms both naive training without intervention and standard reinitialization methods, demonstrating effective balancing of the stability–plasticity tradeoff.

## One-Sentence Claim

FIRE balances continual-learning stability and plasticity by reinitializing weights to stay close to past knowledge while restoring isometric, plastic weight geometry.

## Problem

Models trained on nonstationary data must retain old knowledge while adapting to new tasks. Standard reinitialization methods are hard to tune because conservative resets fail to restore plasticity and aggressive resets erase useful knowledge.

The problem is to choose a principled reinitialization point that trades off proximity to past weights against geometric conditions that support new learning.

## Core Contribution

The paper proposes FIRE, Frobenius-Isometry Reinitialization. It formalizes stability with Squared Frobenius Error to past weights and plasticity with Deviation from Isometry.

The reinitialization target is obtained by minimizing SFE subject to zero DfI, approximated efficiently with Newton-Schulz iteration.

## Method

FIRE sets up a constrained optimization problem over weights. The objective keeps weights near prior values, while the constraint restores isometry to improve plasticity.

Newton-Schulz iteration approximates the isometric reinitialization efficiently enough to apply across visual learning, language modeling, and reinforcement learning.

## Experiments and Evidence

The abstract reports evaluations on CIFAR-10 with ResNet-18, OpenWebText with GPT-0.1B, HumanoidBench with SAC, and Atari with DQN.

Across these domains, FIRE outperforms naive training without intervention and standard reinitialization methods.

## Limits and Failure Modes

The isometry target may not be equally appropriate for all layers, architectures, or optimizer regimes. Reinitialization can still disrupt specialized representations if applied too broadly.

Because this note is abstract-only, details still need checking: when FIRE is triggered, layer coverage, Newton-Schulz cost, continual-task schedules, ablations of SFE/DfI, and interaction with replay or regularization.

## Deep Themes

- Stability-plasticity as constrained geometry: retaining knowledge and restoring learnability become measurable objectives.
- Reinitialization beyond heuristics: resets can be optimized rather than tuned by hand.
- Isometry as plasticity proxy: weight geometry affects future learning capacity.
- Cross-domain continual learning: the same intervention is tested in vision, language, and RL.

## Subthemes

- Squared Frobenius Error.
- Deviation from Isometry.
- Newton-Schulz reinitialization.
- Continual visual, language, and RL learning.

## Connections to Other Papers

This connects to CompSLOT, local redundancy plasticity, and continual-learning papers through preserving useful structure while enabling adaptation.

It also relates to optimizer-state papers such as LoRA-Pre and Beyond Muon because geometric constraints on weights or updates become tools for stable training.

## Notes for Cross-Paper Synthesis

FIRE adds a geometry-control view of lifelong learning: plasticity can be actively restored without fully sacrificing stability.
