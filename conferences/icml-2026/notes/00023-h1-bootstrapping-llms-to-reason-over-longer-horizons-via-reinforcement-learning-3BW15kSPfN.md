# h1: Bootstrapping LLMs to Reason over Longer Horizons via Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 3BW15kSPfN
- Authors: Alesia Ivanova; Sumeet Ramesh Motwani; Ziyang Cai; Philip Torr; Riashat Islam; Shital Shah; Christian Schroeder de Witt; Charles London
- Primary area: deep_learning->foundation_models
- Keywords: long-horizon training;reasoning;large language models;post-training;reinforcement learning
- Source URL: https://openreview.net/forum?id=3BW15kSPfN
- PDF URL: https://openreview.net/pdf?id=3BW15kSPfN

## Abstract

Large language models excel at short-horizon reasoning tasks, but performance drops as reasoning horizon lengths increase. In this work, we introduce a scalable method to bootstrap long-horizon reasoning capabilities using only existing, abundant short-horizon data. Our approach synthetically composes simple problems into complex, multi-step dependency chains of arbitrary length. We train models on this data using outcome-only rewards under a curriculum that automatically increases in complexity, allowing RL training to be scaled much further without saturating. Empirically, our method generalizes remarkably well: curriculum training on composed 6th-grade level math problems improves accuracy on longer, competition-level benchmarks. It also transfers significantly to diverse out-of-distribution ReasoningGym domains and long-context benchmarks, indicating broader generalization. Importantly, our long-horizon improvements are significantly higher than baselines even at high pass@k, showing that models can learn new reasoning paths under RL. Theoretically, we show that curriculum RL with outcome rewards could achieve an exponential improvement in sample complexity over full-horizon training, providing training signal comparable to dense supervision. h1 therefore introduces an efficient path towards scaling RL for long-horizon problems using only existing data.

## One-Sentence Claim

h1 bootstraps long-horizon LLM reasoning by composing abundant short-horizon tasks into dependency chains and training with outcome-only RL under an automatically lengthening curriculum.

## Problem

LLMs can solve short-horizon reasoning tasks but degrade as the number of dependent reasoning steps grows. Directly collecting dense long-horizon supervision is expensive, and naive outcome-only training at long horizons provides too little reward signal.

## Core Contribution

The paper introduces a synthetic composition method for generating arbitrary-length reasoning chains from short-horizon data, combines it with curriculum RL, and provides theoretical sample-complexity analysis for why curriculum training can beat direct full-horizon training.

## Method

Atomic tasks are chained so later subproblems depend on earlier answers. Models are trained with GRPO-style outcome-only rewards under a stagewise curriculum that increases horizon length as the policy improves.

## Experiments and Evidence

The abstract reports that training on composed 6th-grade math problems improves longer competition-level benchmarks, transfers to ReasoningGym and long-context benchmarks, and yields gains beyond baselines even at high pass@k.

## Full-Text Upgrade

The full text emphasizes that the method is meant to internalize long-horizon reasoning paths rather than rely on test-time search. The key experimental contrast is against length-1 RLVR and non-curricular long-horizon training: the curriculum repeatedly introduces a new difficulty level only after shorter dependencies become learnable, preserving useful outcome-reward signal.

A concrete result reported in the text is that one base model moves from 20.07% to 37.76% accuracy with curriculum up to horizon 3, with larger relative gains on harder horizons. The paper also reports improvements even at pass@128, which the authors interpret as evidence that curriculum RL teaches new reasoning paths rather than merely eliciting already-sampled base-model solutions. The theory section models direct full-horizon outcome-only training as exponentially inefficient in horizon length and argues curriculum training can reduce sample complexity to polynomial under its simplified skill model.

## Limits and Failure Modes

Limits to watch: the synthetic dependency-chain construction may not cover all real long-horizon reasoning structures; outcome-only RL still depends on reliable final-answer checking; and the theory uses a simplified skill model whose assumptions need comparison against richer reasoning tasks.

## Deep Themes

- Long-horizon reasoning can be trained from short-horizon data if composition creates dependencies.
- Curriculum design can substitute for dense supervision by preserving reward signal.
- RL post-training may learn new reasoning paths when the task distribution is scaled carefully.

## Subthemes

- Long-horizon reasoning.
- Synthetic task composition.
- Outcome-only reinforcement learning.
- Curriculum learning.
- ReasoningGym transfer.
- Sample-complexity theory.

## Connections to Other Papers

Connects to Base Models Know How to Reason by probing whether post-training elicits or creates reasoning behavior. It also connects to The Tell-Tale Norm, RAGEN-2, and DMPO as part of the broader cluster on reasoning-oriented RL and process diagnostics.

## Notes for Cross-Paper Synthesis

h1 adds a strong curriculum theme: scalable reasoning post-training may depend less on finding rare long-horizon datasets and more on composing existing data into dependency structures with controlled difficulty growth.
