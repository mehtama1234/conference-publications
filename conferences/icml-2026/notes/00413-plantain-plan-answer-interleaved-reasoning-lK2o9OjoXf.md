# PLANTAIN: Plan-Answer Interleaved Reasoning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: lK2o9OjoXf
- Authors: Anthony Liang; Jonathan Berant; Adam Fisch; Abhimanyu Goyal; Kalpesh Krishna; Jacob Eisenstein
- Primary area: deep_learning->large_language_models
- Keywords: Reasoning;Post-training;Inference-time Alignment
- Source URL: https://openreview.net/forum?id=lK2o9OjoXf
- PDF URL: https://openreview.net/pdf?id=lK2o9OjoXf

## Abstract

Reasoning models often spend significant time generating hidden reasoning before any visible response, which can waste user time when the model starts from a false premise that could have been corrected early. Human speakers, in contrast, use lightweight incremental check-ins to maintain common ground, motivating *interleaved reasoning* (IR), where a model alternates between internal thinking and visible intermediate responses. We instantiate this idea with PLAINTAIN (Plan-Answer Interleaved Reasoning), a post-training recipe that teaches a model to externalize an explicit step-by-step plan before continuing its reasoning. This learned plan-first structure creates an interface for early feedback and intervention while preserving space for subsequent reasoning. Across challenging math, coding, text-to-SQL, and reading-comprehension benchmarks, PLAINTAIN improves pass@1 by roughly 6% on average while reducing time-to-first-response by over 60% relative to think-then-answer baselines.

## One-Sentence Claim

PLAINTAIN trains models to externalize plans before continuing reasoning, reducing time-to-first-response and enabling earlier user feedback without sacrificing final performance.

## Problem

Reasoning models often spend a long time generating hidden chains of thought before showing any response. If they start from a false premise, the user cannot correct them early, and time is wasted.

Humans maintain common ground through incremental check-ins, suggesting that models should alternate internal reasoning with visible intermediate responses.

## Core Contribution

The paper introduces interleaved reasoning and instantiates it with PLAINTAIN, a post-training recipe that teaches models to output an explicit step-by-step plan before continuing reasoning.

This plan-first interface allows early feedback and intervention while preserving room for subsequent reasoning. The abstract reports improved pass@1 and much lower time-to-first-response.

## Method

PLAINTAIN post-trains models on a plan-answer interleaving structure. The model first produces a visible plan, then continues solving while the user or external system can potentially intervene.

The design changes the interaction protocol, not merely the final answer objective.

## Experiments and Evidence

Evidence reported in the abstract:

- Challenging math, coding, text-to-SQL, and reading-comprehension benchmarks.
- Roughly 6% average pass@1 improvement.
- More than 60% reduction in time-to-first-response relative to think-then-answer baselines.
- Learned plan-first structure for early feedback and intervention.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: training data format, feedback experiments, plan quality metrics, and whether visible plans leak incorrect reasoning.

## Limits and Failure Modes

- Bad plans can anchor users or the model toward wrong solutions.
- Plan visibility may expose sensitive intermediate reasoning in some settings.
- The benefit depends on whether users or systems actually provide early feedback.
- Plan-first formats may be less useful for tasks where planning overhead dominates.

## Deep Themes

**Reasoning should be interactive.** Visible intermediate plans create an intervention point.

**Latency is part of alignment.** Reducing time-to-first-response improves the human-model loop.

**Process structure can improve performance and usability.** The model's output protocol shapes both correctness and correction.

## Subthemes

- Interleaved reasoning.
- Plan-first post-training.
- Time-to-first-response.
- Early user feedback.
- Inference-time alignment.

## Connections to Other Papers

Connects to Critique-GRPO, Weak-Strong Verification, Monitoring Monitorability, MADQA, and RoTS. It extends the process-visible reasoning theme into user interaction.

## Notes for Cross-Paper Synthesis

PLAINTAIN adds a human-loop timing theme: reasoning traces become more useful when surfaced early enough for correction, not only after completion.
