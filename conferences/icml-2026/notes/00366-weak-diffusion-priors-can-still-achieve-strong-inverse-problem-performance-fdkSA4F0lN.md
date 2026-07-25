# Weak Diffusion Priors Can Still Achieve Strong Inverse-Problem Performance

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fdkSA4F0lN
- Authors: Jing Jia; Wei Yuan; Sifan Liu; Liyue Shen; Guanyang Wang
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: diffusion model;inverse problem;prior
- Source URL: https://openreview.net/forum?id=fdkSA4F0lN
- PDF URL: https://openreview.net/pdf?id=fdkSA4F0lN

## Abstract

Can a diffusion model trained on bedrooms recover human faces? Diffusion models are widely used as priors for inverse problems, but standard approaches usually assume a high-fidelity model trained on data that closely match the unknown signal. In practice, one often must use a mismatched or low-fidelity diffusion prior. Surprisingly, these weak priors often perform nearly as well as full-strength, in-domain baselines. We study when and why inverse solvers are robust to weak diffusion priors. Through extensive experiments, we find that weak priors succeed when measurements are highly informative (e.g., many observed pixels), and we identify regimes where they fail. To explain this behavior, we combine Bayesian-consistency theory with local-correlation analysis: the theory gives conditions under which high-dimensional measurements make the posterior concentrate near the true signal, while the correlation analysis shows that weak and stronger natural-image priors can share similar local spatial structure. These results provide a principled justification on when weak diffusion priors can be used reliably. Code is available at https://github.com/jjia131/weak-diffusion-priors-inverse-problem.

## One-Sentence Claim

Weak or mismatched diffusion priors can solve inverse problems well when measurements are informative enough and the prior shares local natural-image structure with the target domain.

## Problem

Diffusion priors are widely used for inverse problems, but standard practice assumes that the generative prior is high-quality and trained on data close to the unknown signal. In real deployments, users often have only mismatched or low-fidelity priors.

The paper asks why a prior trained on the wrong or weaker domain can still recover signals such as faces, and where that surprising robustness breaks down.

## Core Contribution

The core contribution is an empirical and theoretical explanation of when weak diffusion priors work. The paper identifies measurement informativeness as the key regime variable: when observations strongly constrain the solution, even a weak prior can guide reconstruction nearly as well as an in-domain model.

It combines Bayesian consistency theory with local-correlation analysis, arguing that high-dimensional measurements can concentrate the posterior near the true signal while weak and strong natural-image priors may share enough local spatial statistics to be useful.

## Method

The work studies inverse solvers with mismatched or low-fidelity diffusion priors across measurement regimes. Bayesian-consistency theory provides conditions under which enough measurements dominate prior mismatch, while local-correlation analysis compares structural overlap between weak and strong priors.

The method therefore separates two sources of success: information from the measurement operator and transferable local image statistics from the prior.

## Experiments and Evidence

Evidence reported in the abstract:

- Extensive experiments with weak, mismatched, and in-domain diffusion priors.
- Weak priors often nearly match full-strength in-domain baselines.
- Success when measurements are highly informative, such as many observed pixels.
- Identification of failure regimes.
- Bayesian-consistency theory and local-correlation analysis explaining the behavior.
- Code release at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: inverse tasks, weak-prior domains, measurement thresholds, and failure examples.

## Limits and Failure Modes

- Weak priors fail when measurements are too sparse or ambiguous.
- Local spatial correlation may not transfer across domains with different geometry or semantics.
- Bayesian consistency explains high-information regimes but may not cover practical finite-sample solver failures.
- Reconstructions may look plausible while losing identity, pathology, or other fine semantic details.

## Deep Themes

**The likelihood can rescue the prior.** In inverse problems, enough measurement information can overcome substantial prior mismatch.

**Weak models can carry useful local structure.** A prior need not encode the exact target distribution to regularize reconstruction.

**Reliability is regime-dependent.** The paper turns "weak priors work" into a conditional statement about measurement informativeness and structural overlap.

## Subthemes

- Mismatched diffusion priors.
- Measurement-dominated inverse problems.
- Bayesian posterior concentration.
- Local natural-image correlations.
- Failure regimes for weak generative priors.

## Connections to Other Papers

Connects to MOG, KPE/KTS, Tilt Matching, Dimension-Free Diffusion Sampling, and Local Diffusion Composition. It also links to Noisy Sample Compression and Source Screening because all ask when imperfect sources still contain enough structure to be useful.

## Notes for Cross-Paper Synthesis

This paper adds nuance to the generative-prior theme: stronger priors are not always necessary when external evidence is strong, suggesting a tradeoff between model fidelity and observation informativeness.
