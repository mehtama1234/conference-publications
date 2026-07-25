# Skill Neologisms: Towards Skill-based Continual Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 5VgZUEpK6W
- Authors: Antonin Berthon; Nicolás Astorga; Mihaela van der Schaar
- Primary area: deep_learning->large_language_models
- Keywords: Large Language Models; Skills Neologisms; Skill Composition; Skill-based Continual Learning
- Source URL: https://openreview.net/forum?id=5VgZUEpK6W
- PDF URL: https://openreview.net/pdf?id=5VgZUEpK6W

## Abstract

Modern LLMs show mastery over an ever-growing range of skills, as well as the ability to compose them flexibly. However, extending model capabilities to new skills in a scalable manner is an open problem: fine-tuning and parameter-efficient variants risk catastrophic forgetting, while context-based approaches have limited expressiveness and are constrained by the model's effective context. 
We explore *skill neologisms*--soft tokens integrated in the model's vocabulary and optimized to improve capabilities over a specific skill--as a way to selectively acquire new skills without weight updates. We first observe that pre-trained LLMs already exhibit tokens associated with procedural knowledge. We then show on a controlled synthetic task that skill neologisms can be learned to improve model capabilities on specific skills while being composable with out-of-distribution skills, and that independently trained skill neologisms can be composed zero-shot. Finally, we validate zero-shot composition of independently learned skill neologisms on the more realistic natural language setting of the Skill-Mix benchmark. These results suggest that skill neologisms may provide a scalable path towards skill-based continual learning.

## One-Sentence Claim

Skill neologisms let frozen LLMs acquire and compose new procedural skills by adding trainable soft tokens to the vocabulary instead of updating model weights.

## Problem

LLMs can compose many existing skills, but adding new skills through fine-tuning risks catastrophic forgetting, while purely context-based methods are limited by context capacity and expressiveness.

## Core Contribution

The paper proposes vocabulary-integrated soft skill tokens as a path to skill-based continual learning, showing that independently learned skill tokens can compose zero-shot with other skills.

## Method

A skill neologism is a set of trainable soft tokens appended to the tokenizer and embedding matrix. The base LLM weights remain frozen; only the new token embeddings are optimized on skill-centered data and then inserted into prompts where the skill is needed.

## Experiments and Evidence

The abstract reports evidence from naturally occurring procedural tokens, controlled synthetic composition tasks, and the Skill-Mix benchmark, including zero-shot composition of independently learned skill neologisms.

## Full-Text Upgrade

The full text makes the distinction from prompt tuning precise: the soft tokens are integrated as vocabulary elements rather than only prepended continuous prompts. This lets the model interact with the new skill through ordinary in-context composition. The authors define properties for skill-based continual learning: acquiring new skills without forgetting, composing with out-of-distribution skills, and composing multiple independently learned skills zero-shot.

The paper first motivates the idea by showing that pretrained tokens such as operation names can encode procedural knowledge when sufficiently represented in pretraining. In synthetic tasks, skill neologisms outperform prompt tuning on OOD compositions despite optimizing the same number of soft tokens, suggesting that semantic placement inside prompts matters. The paper further validates zero-shot composition on Skill-Mix.

## Limits and Failure Modes

Limits to watch: skill-token capacity is a bottleneck; skills must be learnable from token-level supervision; composition quality may depend on base-model compositional ability; and the method still needs broader validation for complex real-world skills beyond controlled and benchmarked settings.

## Deep Themes

- Continual learning can happen through new vocabulary interfaces rather than weight updates.
- Procedural knowledge can be packaged as composable tokens.
- Frozen foundation models may be extended by learning small, semantically placed adapters.

## Subthemes

- Skill-based continual learning.
- Soft tokens.
- Vocabulary expansion.
- Procedural knowledge.
- Zero-shot skill composition.
- Catastrophic forgetting avoidance.

## Connections to Other Papers

Connects to CompSLOT and continual-learning papers through modular acquisition without forgetting. It also links to activation/steering work because small learned interfaces can control latent capabilities without full fine-tuning.

## Notes for Cross-Paper Synthesis

Skill neologisms add a modular-adaptation theme: model capability expansion may increasingly happen through compact, composable interfaces rather than monolithic parameter updates.
