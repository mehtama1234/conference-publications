# Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: DfhMMHXDuu
- Authors: Zhibin Duan; Guowei Rong; Zhuo Li; Bo Chen; Mingyuan Zhou; Dandan Guo
- Primary area: probabilistic_methods->bayesian_models_and_methods
- Keywords: Reward Model;Reward Hacking;Large Language Model;Bayesian Deep Learning;Non-negative Factor Analysis;Uncertainty;Interpretable Model
- Source URL: https://openreview.net/forum?id=DfhMMHXDuu
- PDF URL: https://openreview.net/pdf?id=DfhMMHXDuu

## Abstract

Reward models learned from human preferences are central to aligning large language models (LLMs) via reinforcement learning from human feedback, yet they are often vulnerable to reward hacking due to noisy annotations and systematic biases such as response length or style. We propose Bayesian Non-Negative Reward Model (BNRM), a principled reward modeling framework that integrates non-negative factor analysis into Bradley–Terry (BT) preference model.BNRM represents rewards through a sparse, non-negative latent factor generative process that operates at two complementary levels: instance-specific latent variables induce disentangled reward representations, while sparsity over global latent factors acts as an implicit debiasing mechanism that suppresses spurious correlations. Together, this disentanglement-then-debiasing structure enables robust uncertainty-aware reward learning. To scale BNRM to modern LLMs, we develop an amortized variational inference network conditioned on deep model representations, allowing efficient end-to-end training. Extensive empirical results demonstrate that BNRM substantially mitigates reward over-optimization, improves robustness under distribution shifts, and yields more interpretable reward decompositions than strong baselines.

## One-Sentence Claim

BNRM mitigates RLHF reward hacking by modeling rewards as sparse non-negative latent factors with uncertainty-aware Bayesian preference learning.

## Problem

Reward models trained from noisy preferences can learn spurious biases such as response length or style, making RLHF vulnerable to over-optimization and reward hacking.

## Core Contribution

The paper proposes Bayesian Non-Negative Reward Modeling, integrating non-negative factor analysis into a Bradley-Terry preference model with amortized variational inference.

## Method

BNRM uses instance-specific latent variables for disentangled reward representations and sparse global non-negative factors for implicit debiasing. An inference network conditioned on deep model representations scales training end-to-end.

## Experiments and Evidence

The abstract reports reduced reward over-optimization, better robustness under distribution shifts, and more interpretable reward decompositions than strong baselines.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: factor interpretability, uncertainty calibration, preference datasets, RL loop results, and computational overhead.

## Deep Themes

- Reward models need disentanglement and uncertainty to resist hacking.
- Non-negative latent factors can make preference rewards more interpretable.
- Debiasing should be built into reward-model structure, not only post-hoc filtering.

## Subthemes

- RLHF.
- Reward hacking.
- Bayesian reward models.
- Non-negative factor analysis.
- Bradley-Terry preferences.
- Uncertainty-aware alignment.

## Connections to Other Papers

Connects to Binary RAR, RGR-GRPO, regularized RLHF social-choice analysis, and DPO/RLHF theory through reward-design and preference-optimization robustness.

## Notes for Cross-Paper Synthesis

BNRM strengthens the reward-model-structure theme: alignment failures can arise from latent reward factors and biases, so the reward model itself needs interpretable constraints.
