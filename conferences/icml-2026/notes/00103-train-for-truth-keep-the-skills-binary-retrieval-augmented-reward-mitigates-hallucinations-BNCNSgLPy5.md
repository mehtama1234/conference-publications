# Train for Truth, Keep the Skills: Binary Retrieval-Augmented Reward Mitigates Hallucinations

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: BNCNSgLPy5
- Authors: Tong Chen; Akari Asai; Luke Zettlemoyer; Hannaneh Hajishirzi; Faeze Brahman
- Primary area: deep_learning->large_language_models
- Keywords: hallucination;factuality;reinforcement learning;retrieval-augmented generation
- Source URL: https://openreview.net/forum?id=BNCNSgLPy5
- PDF URL: https://openreview.net/pdf?id=BNCNSgLPy5

## Abstract

Modern post-trained language models are increasingly capable, but remain prone to extrinsic hallucinations.
We target the utility degradation issue that prior hallucination-reduction methods often struggle to avoid, and propose online RL with Binary Retrieval-Augmented Reward (Binary RAR) to reduce hallucinations while preserving general capabilities.
Binary RAR assigns a reward of 1 if a response contains no factual contradictions with retrieved evidence, and 0 otherwise. 
We theoretically show that this method reduces the probability of error-containing responses while preserving the distribution of error-free responses. This helps preserve the model’s capabilities, whereas other methods often degrade them.
We evaluate Binary RAR on multiple widely used models. On Qwen3-8B, it reduces long-form hallucination rates by 39.3\% and short-form hallucination rates by 54.4\%, outperforming supervised learning and preference optimization baselines.
Our error analysis shows that continuous factuality rewards (e.g., VeriScore) can be exploited via reward hacking by producing fewer or more generic claims, whereas Binary RAR is more robust and better preserves general capabilities, including instruction following, math, and coding.

## One-Sentence Claim

Binary Retrieval-Augmented Reward reduces hallucinations by rewarding only responses with no contradictions to retrieved evidence while preserving the distribution of error-free responses.

## Problem

Hallucination-reduction methods often improve factuality at the cost of general utility, causing models to become generic, less capable, or worse at instruction following, math, and coding.

## Core Contribution

The paper proposes online RL with Binary RAR and gives theoretical support that it reduces error-containing outputs without distorting error-free response behavior.

## Method

Binary RAR retrieves evidence and assigns reward 1 if the response contains no factual contradictions with that evidence, otherwise 0. The binary design avoids continuous factuality-reward incentives to make fewer or vaguer claims.

## Experiments and Evidence

The abstract reports Qwen3-8B hallucination reductions of 39.3% on long-form and 54.4% on short-form tasks, outperforming supervised learning and preference optimization baselines while preserving instruction following, math, and coding.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: retrieval quality, contradiction judge, evidence coverage, domain robustness, and whether binary rewards miss unsupported but non-contradictory claims.

## Deep Themes

- Factuality rewards should avoid incentives for generic or low-information answers.
- Retrieval can ground RL rewards without collapsing general skills.
- Capability preservation is part of hallucination mitigation.

## Subthemes

- Hallucination reduction.
- Retrieval-augmented rewards.
- Binary factuality signals.
- Online RL.
- Reward hacking.
- Capability preservation.

## Connections to Other Papers

Connects to DR Tulu, RGR-GRPO, RLHF reward-hacking work, and deep-research evaluation through factuality-aware agent training.

## Notes for Cross-Paper Synthesis

Binary RAR adds a reward-design theme: coarser binary rewards can sometimes preserve incentives better than fine-grained scores that invite reward hacking.
