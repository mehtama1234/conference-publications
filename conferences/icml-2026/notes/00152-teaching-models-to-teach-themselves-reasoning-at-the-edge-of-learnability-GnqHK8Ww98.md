# Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: GnqHK8Ww98
- Authors: Shobhita Sundaram; John Quan; Ariel Kwiatkowski; Kartik Ahuja; Yann Ollivier; Julia Kempe
- Primary area: deep_learning->large_language_models
- Keywords: reasoning;LLMs;reinforcement learning;self-play;self-improvement
- Source URL: https://openreview.net/forum?id=GnqHK8Ww98
- PDF URL: https://openreview.net/pdf?id=GnqHK8Ww98

## Abstract

RL methods for scaling large reasoning models stall on datasets with low initial success rates, and thus little training signal. We investigate a fundamental question:Can a pretrained LLM leverage latent knowledge to generate an automated curriculum  for problems it cannot solve? We explore this with SOAR: An asymmetric self-play framework that uses meta-RL to surface these pedagogical signals. A teacher model proposes synthetic problems for a student model, and is rewarded with its improvement on a subset of hard problems, thus grounding the curriculum in real student progress rather than intrinsic proxy rewards. Our study on the hardest subsets of math benchmarks (0/128 success) reveals three core findings. First, it is possible to realize bilevel meta-RL that unlocks learning under sparse, binary rewards by sharpening a latent capacity of pretrained models to generate useful problems. Second, grounded rewards outperform intrinsic learnability rewards used in prior LLM self-play, reliably avoiding typical instability and diversity collapse modes. Third, the structure and well-posedness of questions are more critical for learning progress than solution correctness. Our results suggest that the ability to generate useful stepping stones does not require the preexisting ability to solve the hard problems, paving a principled path to escape reasoning plateaus without additional curated data.

## One-Sentence Claim

SOAR uses asymmetric self-play and meta-RL to let a teacher model generate curricula that help a student improve on reasoning problems it initially cannot solve.

## Problem

RL for reasoning stalls on hard datasets with near-zero initial success because sparse binary rewards provide little training signal.

## Core Contribution

The paper introduces SOAR, a teacher-student framework where the teacher is rewarded by student improvement on hard problems rather than intrinsic proxy rewards.

## Method

A teacher proposes synthetic problems for a student; meta-RL optimizes the teacher based on grounded student progress on hard benchmark subsets, sharpening latent pretrained capacity for useful problem generation.

## Experiments and Evidence

The abstract reports results on hardest math benchmark subsets with 0/128 success, showing that grounded rewards avoid instability and diversity collapse, and that question structure and well-posedness matter more than solution correctness.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: teacher/student models, meta-RL stability, curriculum filtering, task transfer, and whether generated curricula introduce hidden leakage.

## Deep Themes

- Models may teach themselves with stepping-stone problems before solving target tasks.
- Curriculum quality can be grounded in student progress rather than proxy diversity.
- Learnability depends on question structure, not only answer correctness.

## Subthemes

- Self-play.
- Meta-RL.
- Reasoning curricula.
- Sparse binary rewards.
- Self-improvement.
- Edge of learnability.

## Connections to Other Papers

Connects to TTT-Discover, MaxRL, RGR-GRPO, LALP, and ThreadWeaver through reasoning improvement under scarce reward signal.

## Notes for Cross-Paper Synthesis

SOAR strengthens the curriculum-as-control theme: hard reasoning can be unlocked by generating learnable intermediate tasks rather than adding curated answers.
