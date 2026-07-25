# Base Models Know How to Reason, Thinking Models Learn When

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 2BniakOS4q
- Authors: Constantin Venhoff; Iván Arcuschin; Philip Torr; Arthur Conmy; Neel Nanda
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: Chain of Thought;Reasoning models;Sparse Autoencoders;Steering
- Source URL: https://openreview.net/forum?id=2BniakOS4q
- PDF URL: https://openreview.net/pdf?id=2BniakOS4q

## Abstract

What do different *thinking* language models learn during training?
We introduce *constructive model diffing*, a framework for understanding fine-tuned models by constructing the base-to-fine-tuned difference from interpretable components, producing hybrid models whose performance recovery measures how well the components capture the diff.
For thinking models, we decompose the diff into *reasoning mechanisms* (category-specific vectors that induce reasoning behaviors in the base model) and *reasoning heuristics* (a classifier determining when each mechanism fires).
To ground this decomposition, we use Sparse Autoencoders to discover interpretable taxonomies of reasoning behaviors.
Across nine model configurations (four RL-trained, four SFT-distilled from a larger thinking model, and one mixed), we find a striking difference: hybrid models recover much more performance for RL-trained models than for SFT-trained or mixed ones. This indicates that RL primarily teaches models to apply sophisticated heuristics to pre-existing base capabilities, while SFT-based distillation teaches the base model new mechanisms.
These results offer a new lens on what different training paradigms teach, with implications for efficient reasoning model development.

## One-Sentence Claim

Constructive model diffing suggests RL-trained thinking models mainly learn when to invoke pre-existing reasoning mechanisms, while SFT distillation teaches new mechanisms.

## Problem

It is unclear what different thinking-model training paradigms actually add to base LLMs: new reasoning mechanisms, better routing/heuristics, or both.

## Core Contribution

The paper introduces constructive model diffing, decomposing base-to-fine-tuned differences into interpretable reasoning mechanisms and reasoning heuristics, then measuring how much hybrid models recover fine-tuned performance.

## Method

Sparse autoencoders discover interpretable taxonomies of reasoning behaviors. The method constructs hybrid models from mechanism vectors and heuristics that determine when those mechanisms fire, then evaluates performance recovery.

## Experiments and Evidence

Across nine model configurations, hybrid models recover much more performance for RL-trained models than for SFT-distilled or mixed models. The abstract interprets this as RL teaching heuristics over existing capabilities, while SFT teaches new mechanisms.

## Limits and Failure Modes

Full-text checks needed: SAE interpretability quality, model/task selection, causal validity of mechanism vectors, and whether the RL-versus-SFT distinction holds across larger proprietary models.

## Deep Themes

- Reasoning fine-tuning can change routing rather than capability substrate.
- Interpretability is being used to compare training paradigms.
- Base models may contain latent reasoning mechanisms that post-training learns to deploy.

## Subthemes

- Constructive model diffing.
- Sparse autoencoders.
- Reasoning mechanisms versus heuristics.
- RL versus SFT.
- Thinking models.

## Connections to Other Papers

Connects to The Tell-Tale Norm, Steer Like the LLM, and RAGEN-2 through internal reasoning diagnostics and control.

## Notes for Cross-Paper Synthesis

This paper sharpens a major theme: reasoning improvements may come less from adding entirely new cognition and more from learning triggers, policies, and interfaces for capabilities already latent in the base model.

## Full-Text Upgrade

Source used: `conferences/icml-2026/text/00015-base-models-know-how-to-reason-thinking-models-learn-when-2BniakOS4q-arxiv.txt`.

Additional verified details:

- The full text reports that hybrid models recover roughly 76% of the RL-trained base-to-thinking gap but only about 11% of the SFT-distilled gap.
- Constructive model diffing has two explicit components: category vectors as reasoning mechanisms and an SAE-derived heuristic that decides when to deploy them.
- SAEs are trained on sentence-level activations from reasoning traces and are used to construct taxonomies of reasoning behavior.
- The studied set includes four RL-trained Open-Reasoner-Zero models, four SFT-distilled DeepSeek-R1 variants, and one mixed QwQ-32B model.
- Negative-control ablations show that trained category vectors and SAE-based category/position selection matter for hybrid recovery.
- The authors argue that the mixed SFT+RL model resembles distilled models more than RL-trained models in this analysis.

Refined limits:

- The lower recovery for SFT-distilled models may reflect limitations of the SAE taxonomy or hybrid construction rather than all SFT-induced changes.
- The method depends on interpretable and causally meaningful SAE categories.
