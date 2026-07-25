# Provable Bounds for the Learnability of Sample-Compressible Families from Noisy Samples

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fRonOqrKWT
- Authors: Arefe Boushehrian; Amir Najafi
- Primary area: theory->learning_theory
- Keywords: PAC-learnability;robust distribution learning;sample compression;noisy samples
- Source URL: https://openreview.net/forum?id=fRonOqrKWT
- PDF URL: https://openreview.net/pdf?id=fRonOqrKWT

## Abstract

Learning distribution families over $\mathbb{R}^d$ is a fundamental problem in unsupervised learning and statistics. A central question in this setting is whether a given family of distributions possesses sufficient structure to be (at least) information-theoretically learnable and, if so, to characterize its sample complexity. In 2018, Ashtiani et al. (2018) reformulated sample compressibility as a structural property of distribution classes, proving that it guarantees PAC-learnability. This discovery subsequently enabled a series of recent advancements in deriving nearly tight sample complexity bounds for various high-dimensional open problems. It has been further conjectured that the converse also holds: every learnable class admits a sample compression scheme, making the two notions to be equivalent. In this work, we establish that sample compressible families remain learnable even from perturbed samples, subject to a set of minimax-necessary and sufficient conditions. In particular, we assume samples are corrupted by an additive independent noise model, and theoretically derive sample complexity bounds for general sample compressible classes in arbitrary dimensions with respect to both $\ell_2$-norm and total variation distance.

## One-Sentence Claim

Sample-compressible distribution families remain PAC-learnable under additive independent noise exactly under minimax-necessary and sufficient conditions.

## Problem

Distribution learning over high-dimensional spaces often relies on structural assumptions to avoid impossible sample complexity. Sample compression is one such structure: a distribution class is learnable if representative samples can summarize it compactly.

The paper asks whether this structure survives realistic corruption, where observations are perturbed by independent additive noise.

## Core Contribution

The paper proves learnability bounds for general sample-compressible distribution classes from noisy samples in arbitrary dimensions. It gives minimax-necessary and sufficient conditions and derives sample complexity under both l2-norm and total-variation metrics.

This extends the sample-compression view of distribution learning from clean observations to perturbed observations.

## Method

The framework assumes additive independent noise corrupts samples from the target distribution. The analysis characterizes when the compressed structure remains recoverable despite convolution or perturbation by the noise distribution.

The results are information-theoretic: they establish when learnability is possible and the sample complexity required, rather than proposing a narrowly engineered estimator.

## Experiments and Evidence

Evidence reported in the abstract:

- General sample-compressible classes in arbitrary dimensions.
- Additive independent noise model.
- Minimax-necessary and sufficient conditions.
- Sample complexity bounds for l2-norm and total variation distance.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: exact noise assumptions, compression parameters, metric definitions, and constants.

## Limits and Failure Modes

- Additive independent noise may not cover structured, adversarial, or data-dependent corruption.
- Information-theoretic learnability does not guarantee computationally efficient learning.
- General bounds may be loose for specific distribution families.
- Total-variation guarantees under noise can be sensitive to deconvolution assumptions.

## Deep Themes

**Structure must survive corruption.** Learnability depends not only on the clean class but on how noise interacts with its compressed representation.

**Compression is a unifying statistical primitive.** The paper treats sample compression as a bridge between high-dimensional structure and PAC learnability.

**Robustness can be characterized minimax-tight.** The work identifies when noisy learning is possible rather than only proposing robust heuristics.

## Subthemes

- Sample-compressible distribution classes.
- Robust distribution learning.
- Additive independent noise.
- Minimax learnability conditions.
- l2 and total-variation sample complexity.

## Connections to Other Papers

Connects to Source Screening, CreDRO, Finite Test Certification, Jacobi Spectral Reconstruction, and noisy-label purification work. It adds a distribution-learning counterpart to the corpus's broader theme of robustness under corrupted evidence.

## Notes for Cross-Paper Synthesis

This paper strengthens the statistical-foundations thread: many 2026 papers ask which forms of structure remain useful when the observations, tests, sources, or labels are degraded.
