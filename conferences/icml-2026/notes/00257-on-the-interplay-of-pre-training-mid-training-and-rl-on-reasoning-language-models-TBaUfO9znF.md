# On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: TBaUfO9znF
- Authors: Charlie Zhang; Graham Neubig; Xiang Yue
- Primary area: deep_learning->large_language_models
- Keywords: post-training;reinforcement learning;reasoning
- Source URL: https://openreview.net/forum?id=TBaUfO9znF
- PDF URL: https://openreview.net/pdf?id=TBaUfO9znF

## Abstract

Recent reinforcement learning (RL) techniques have yielded impressive reasoning improvements in language models, yet it remains unclear whether RL truly extends a model's reasoning ability beyond pre-training. A central challenge is the lack of control in modern training pipelines, where opaque pre-training data, underexplored mid-training, and complex RL interactions obscure causal effects. To resolve this ambiguity, we develop a controlled experimental framework that isolates the causal contributions of pre-training, mid-training, and RL-based post-training. Our approach employs synthetic reasoning tasks with explicit atomic operations, parseable step-by-step reasoning traces, and systematic manipulation of training distributions. We evaluate along: *extrapolative generalization* to more complex compositions and *contextual generalization* across surface contexts. Using this framework, we reconcile competing views on RL’s effectiveness: 1) RL produces true capability gains (pass@128) only when pre-training leaves sufficient headroom and RL data target the model’s *edge of competence*, tasks that are difficult but not yet out of reach. 2) Contextual generalization requires minimal yet sufficient pre-training exposure, after which RL reliably transfers. 3) Mid-training significantly enhances performance under fixed compute compared with RL alone, demonstrating its central but underexplored role. 4) Process-level rewards reduce reward hacking and improve reasoning fidelity. Together, these results clarify the interplay between pre-training, mid-training, and RL, offering a foundation for improving reasoning language models training strategies. Codes and data are avaialble at [Github](https://github.com/Interplay-LM-Reasoning/Interplay-LM-Reasoning) and [HuggingFace](https://huggingface.co/Interplay-LM-Reasoning)

## One-Sentence Claim

RL improves reasoning most when pre-training and mid-training place tasks near the model's edge of competence, making capability gains a pipeline interaction rather than a post-training-only effect.

## Problem

Reasoning gains from RL post-training are hard to interpret because current LLM pipelines combine opaque pre-training corpora, intermediate supervised or synthetic stages, and RL objectives. Without controlled training distributions, it is unclear whether RL teaches new reasoning skills, amplifies latent skills already acquired in pre-training, or mostly changes sampling behavior.

The paper targets this causal ambiguity: what does pre-training contribute, what does mid-training contribute, and when does RL genuinely extend reasoning ability?

## Core Contribution

The paper builds a controlled synthetic-reasoning framework with explicit atomic operations, parseable traces, and manipulated training distributions. It uses this framework to identify when each training phase matters:

- RL yields true pass@128 capability gains when pre-training leaves headroom and RL tasks sit at the model's edge of competence.
- Contextual generalization needs minimal but sufficient pre-training exposure, after which RL can transfer across surface contexts.
- Mid-training improves fixed-compute performance beyond RL alone.
- Process-level rewards reduce reward hacking and improve trace fidelity.

## Method

The method isolates training stages by using synthetic tasks whose operations and reasoning traces can be parsed. The authors vary pre-training exposure, mid-training, and RL data distributions, then evaluate extrapolative generalization to harder compositions and contextual generalization across surface forms.

This turns reasoning training into a controlled causal experiment: instead of asking whether a final model performs well, it asks which stage supplied which type of generalization capacity.

## Experiments and Evidence

Evidence comes from controlled comparisons across training-stage interventions:

- Extrapolative generalization to more complex operation compositions.
- Contextual generalization across changed surface contexts.
- Pass@128 gains used to separate latent-skill sampling improvements from broader capability gains.
- Comparisons of RL-only, mid-training, and combined regimes under fixed compute.
- Process-level reward experiments showing less reward hacking and better reasoning fidelity.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: task families, model sizes, reward design, compute matching, pass@k sampling setup, and definitions of "edge of competence."

## Limits and Failure Modes

- Synthetic tasks give causal control but may omit messy pre-training contamination, natural-language ambiguity, and real mathematical diversity.
- Edge-of-competence targeting could be difficult at scale without reliable difficulty estimators.
- Pass@128 gains may not translate to single-sample deployment reliability.
- Process rewards help fidelity but depend on the quality and completeness of trace parsing.

## Deep Themes

**Reasoning capability is staged.** The paper treats pre-training, mid-training, and RL as a coupled curriculum rather than independent modules.

**RL is most useful near the frontier of existing competence.** If tasks are too easy, RL has little to teach; if too hard, it lacks usable behavioral substrate.

**Evaluation should expose causal training mechanisms.** Controlled distributions and parseable traces convert vague post-training debates into testable causal claims.

## Subthemes

- Edge-of-competence data selection.
- Mid-training as an under-modeled capability phase.
- Process rewards as anti-hacking controls.
- Extrapolative versus contextual generalization.
- Pass@k as a lens on latent reasoning capacity.

## Connections to Other Papers

Strongly connects to MTS Difficulty and HOBIT because all three ask how training data should be chosen by difficulty and informativeness. It also links to alignment and feedback papers such as R2VPO, SVGT, and conditional DPO/RLHF work, where post-training outcomes depend on the geometry and signal quality of the update mechanism.

## Notes for Cross-Paper Synthesis

This paper reinforces a recurring 2026 pattern: post-training is not a magic final layer. Its effect depends on the competence distribution created upstream, the fidelity of feedback signals, and whether the training examples hit the model's current learning boundary.
