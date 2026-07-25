# Gaussian certified unlearning in high dimensions: A hypothesis testing approach

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 0FJYicpOj0
- Authors: Aaradhya Pandey; Arnab Auddy; Haolin Zou; Arian Maleki; Sanjeev Kulkarni
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: Machine unlearning in high dimensions;Proportional asymptotics;High dimensional statistical theory;Privacy–accuracy tradeoff;Hypothesis testing;Gaussian noise calibration;Newton method
- Source URL: https://openreview.net/forum?id=0FJYicpOj0
- PDF URL: https://openreview.net/pdf?id=0FJYicpOj0

## Abstract

Machine unlearning seeks to efficiently remove the influence of selected data while preserving generalization. Significant progress has been made in low dimensions, \textcolor{blue}{where the dimension of the parameter} $p$ is  much smaller than \textcolor{blue}{the sample size} $n$, but high dimensions, including proportional regimes $p \sim n$, pose serious theoretical challenges as standard optimization assumptions of $\Omega(1)$ strong convexity and $O(1)$ smoothness of the per-example loss $f$ rarely hold simultaneously in proportional regimes $p\sim n$.
In this work, we introduce $\varepsilon$-Gaussian certifiability, a canonical and robust notion well-suited to high-dimensional regimes, that optimally captures a broad class of noise adding mechanisms. Then we theoretically analyze the performance of a widely used unlearning algorithm based on one step of the Newton method in the high-dimensional setting described above. Our analysis shows that a single Newton step, followed by a well-calibrated Gaussian noise, is sufficient to achieve both privacy and accuracy in this setting. This result stands in sharp contrast to the only prior work that analyzes machine unlearning in high dimensions \citet{zou2025certified}, which relaxes some of the standard optimization assumptions for high-dimensional applicability, but operates under the notion of $\varepsilon$-certifiability. That work concludes %that a single Newton step is insufficient even for removing a single data point, and
that at least two steps are required to ensure both privacy and accuracy. Our result leads us to conclude that the discrepancy in the number of steps arises because of the sub optimality of the notion of $\varepsilon$-certifiability and its incompatibility with noise adding mechanisms, which $\varepsilon$-Gaussian certifiability is able to overcome optimally.

## One-Sentence Claim

High-dimensional certified unlearning can be achieved with one Newton update plus calibrated Gaussian noise if the guarantee is framed as epsilon-Gaussian certifiability rather than the older epsilon-certifiability notion.

## Problem

Machine unlearning needs to remove selected training points without retraining from scratch, but existing theory is much weaker in proportional high-dimensional regimes where parameter count is comparable to sample size. Standard strong-convexity and smoothness assumptions become unrealistic there, making prior low-dimensional guarantees a poor fit.

## Core Contribution

The paper proposes epsilon-Gaussian certifiability as a guarantee tailored to noise-adding unlearning mechanisms and uses it to show that a single Newton step followed by Gaussian noise can simultaneously preserve privacy and accuracy in high dimensions.

## Method

The method is theoretical. It studies a standard one-step Newton unlearning update under proportional high-dimensional asymptotics, then calibrates additive Gaussian noise and analyzes the resulting privacy/accuracy behavior through a hypothesis-testing style certification lens.

## Experiments and Evidence

Evidence in the abstract is primarily theoretical: the claimed result contrasts with prior high-dimensional certified unlearning theory that required at least two steps. The key evidence to verify in the PDF is the exact asymptotic regime, assumptions on the loss/model, and whether empirical simulations support the theory.

## Limits and Failure Modes

Likely limitations to check: dependence on Gaussian noise mechanisms, assumptions needed for the high-dimensional analysis, applicability beyond convex or locally well-behaved objectives, and whether the certification notion is accepted as operationally meaningful for deployed unlearning.

## Deep Themes

- Safety/privacy mechanisms are becoming mathematically formalized rather than purely empirical.
- Efficiency and privacy are linked: one-step unlearning is valuable because retraining and multi-step removal are expensive.
- The choice of certification definition can change what is considered possible.

## Subthemes

- Certified unlearning.
- Privacy-accuracy tradeoff.
- High-dimensional asymptotics.
- Noise calibration.
- Hypothesis-testing view of ML guarantees.

## Connections to Other Papers

Connects to the broader safety/privacy cluster and to efficiency-oriented papers that reduce retraining cost. It should be compared with other 2026 work on unlearning, privacy-preserving learning, and robustness certificates.

## Notes for Cross-Paper Synthesis

This is an example of a deeper 2026 pattern: deployment constraints create new theory problems. The paper reframes a practical compliance/safety requirement as a statistical certification problem, and the main novelty comes from changing the guarantee to match the mechanism.

## Full-Text Upgrade

Source used: `conferences/iclr-2026/text/00001-gaussian-certified-unlearning-in-high-dimensions-a-hypothesis-testing-approach-0FJYicpOj0-arxiv.txt`.

Additional verified details:

- The paper formalizes two objectives for unlearning: protect user privacy and preserve model accuracy.
- Privacy is cast through a hypothesis-testing lens: an adversary observes an unlearning output and tries to distinguish whether a removed subset was actually removed.
- The proposed guarantee is named `(phi, epsilon)-GPAR`, abbreviated from Gaussian Probabilistically certified Approximate data Removal / Gaussian certifiability.
- The accuracy metric is Generalized Error Divergence, focused on prediction-level degradation.
- The theoretical setup studies generalized linear models in a proportional high-dimensional regime where `n, p -> infinity` and `n / p -> gamma`.
- The core algorithm is a one-step Newton update from the original estimator on the leave-out objective, followed by additive Gaussian noise.
- Theorem 2 establishes Gaussian certifiability for suitable noise variance under stated assumptions.
- Theorem 3 establishes that, with that variance, generalization degradation vanishes in the high-dimensional setting.
- Simulations compare Gaussian-Newton and Laplace-Newton behavior: the extracted text reports Gaussian unlearning GED decaying roughly at order `p^-0.5`, while Laplace perturbation does not show the same decay for the tested removals.

Refined limits:

- The full text frames the theory as a foundational GLM step rather than a direct guarantee for neural networks or LLMs.
- The authors explicitly discuss that Newton-based unlearning is used in practice for more complex models, but the paper's rigorous result is not yet that broad.
- The accuracy criterion is prediction-level; upstream properties of the model after unlearning may require other metrics.
