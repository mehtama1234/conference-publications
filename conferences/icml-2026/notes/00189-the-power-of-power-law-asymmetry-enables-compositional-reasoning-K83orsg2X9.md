# The Power of Power Law: Asymmetry Enables Compositional Reasoning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: K83orsg2X9
- Authors: Zixuan Wang; Xingyu Dang; Jason D. Lee; Kaifeng Lyu
- Primary area: deep_learning->theory
- Keywords: Power Law;Compositional Reasoning
- Source URL: https://openreview.net/forum?id=K83orsg2X9
- PDF URL: https://openreview.net/pdf?id=K83orsg2X9

## Abstract

Natural language data follows a power-law distribution, with most knowledge and skills appearing at very low frequency. While a common intuition suggests that reweighting or curating data toward a uniform distribution may help models better learn these long-tail skills, we find a counterintuitive result: across a wide range of compositional reasoning tasks, such as state tracking and multi-step arithmetic, training under power-law distributions consistently outperforms training under uniform distributions. To understand this advantage, we introduce a minimalist skill-composition task and show that learning under a power-law distribution provably requires significantly less training data. Our theoretical analysis reveals that power law sampling induces a beneficial asymmetry that improves the pathological loss landscape, which enables models to first acquire high-frequency skill compositions with low data complexity, which in turn serves as a stepping stone to efficiently learn rare long-tailed skills. Our results offer an alternative perspective on what constitutes an effective data distribution for training models.

## One-Sentence Claim

Power-law training distributions can improve compositional reasoning by creating beneficial asymmetry that lets frequent skill compositions become stepping stones for rare ones.

## Problem

Although uniform reweighting seems appealing for long-tail skills, it may remove structure in natural data distributions that helps models learn compositional reasoning efficiently.

## Core Contribution

The paper shows empirically and theoretically that power-law sampling can outperform uniform training on compositional reasoning tasks by improving the loss landscape and reducing data requirements.

## Method

The authors test power-law versus uniform distributions on state tracking and multi-step arithmetic, then introduce a minimalist skill-composition task where they prove lower data complexity under power-law sampling.

## Experiments and Evidence

The abstract reports consistent gains for power-law distributions across compositional reasoning tasks and theoretical evidence that high-frequency compositions are learned first and then support rare long-tail skill learning.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: task definitions, power-law exponents, model classes, proof assumptions, fairness for rare skills, and whether results hold at LLM pretraining scale.

## Deep Themes

- Natural distributional asymmetry can be a curriculum rather than a flaw.
- Long-tail generalization may require structured imbalance.
- Compositional reasoning emerges through staged acquisition of frequent then rare combinations.

## Subthemes

- Power-law data.
- Compositional reasoning.
- State tracking.
- Multi-step arithmetic.
- Long-tail skill learning.
- Loss landscape theory.

## Connections to Other Papers

Connects to Real-World Unsupervised Models through natural data distributions as inductive bias and to curriculum/reasoning papers such as SOAR through stepping-stone learning.

## Notes for Cross-Paper Synthesis

This paper complicates the data-curation theme: balancing data may not always help, because the original power-law structure can encode a useful learning order.
