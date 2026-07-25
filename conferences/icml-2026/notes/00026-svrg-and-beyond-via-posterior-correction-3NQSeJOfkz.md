# SVRG and Beyond via Posterior Correction

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 3NQSeJOfkz
- Authors: Nico Daheim; Thomas Möllenhoff; Ming Liang Ang; Mohammad Emtiyaz Khan
- Primary area: probabilistic_methods->variational_inference
- Keywords: variational learning;bayesian deep learning;variance reduction;stochastic optimization;convex optimization
- Source URL: https://openreview.net/forum?id=3NQSeJOfkz
- PDF URL: https://openreview.net/pdf?id=3NQSeJOfkz

## Abstract

Stochastic Variance Reduced Gradient (SVRG) and its variants aim to speed-up training by using gradient corrections. Originally proposed over a decade ago, these methods have never been connected to any Bayesian method at a fundamental level. Here, we fill this gap and derive surprising new connections of SVRG to a recently proposed Bayesian method called `posterior correction'. Our main contribution is to show that SVRG can be recovered as a special case of posterior-correction over isotropic-Gaussian posteriors. Novel extensions of SVRG are automatically obtained by using more flexible exponential-family posteriors. We derive two new such extensions by using Gaussian families: a Newton-like variant with novel Hessian corrections, and an Adam-like extension that scales to large problems. Our work is the first to connect SVRG to Bayes and use it to speed-up training.

## One-Sentence Claim

SVRG can be derived as posterior correction over isotropic Gaussian posteriors, and that Bayesian view yields Newton-like and Adam-like variance-reduction extensions.

## Problem

SVRG and related gradient-correction methods are widely used for variance reduction, but they have lacked a fundamental connection to Bayesian learning methods that could explain or generalize them.

## Core Contribution

The paper connects SVRG to posterior correction, recovers SVRG as a special case, and uses more flexible exponential-family posterior choices to derive new SVRG-style algorithms.

## Method

It applies posterior correction within variational/Bayesian learning rules. With isotropic Gaussian posteriors, the mean update recovers SVRG; with richer Gaussian families, the same framework produces Hessian-corrected Newton-like variants and diagonal-covariance Adam-like variants.

## Experiments and Evidence

The abstract reports that the Adam-like extension scales to large problems and speeds training.

## Full-Text Upgrade

The full text frames SVRG as a knowledge-transfer mechanism: a full-batch reference gradient corrects noisy minibatch gradients, and posterior correction gives the same structure in natural-parameter space. The paper explicitly states that SVRG is equivalent to a posterior-correction method when the posterior family is isotropic Gaussian, with model parameters replaced by the Gaussian mean.

The "beyond SVRG" part is not just rhetorical. Using full Gaussian posteriors introduces stochastic variance-reduced Hessian corrections, yielding a Newton-like update that differs from typical Newton-SVRG work focused only on gradient correction. Using diagonal Gaussians produces an IVON-PoCo/Adam-like extension intended for larger deep-learning problems, including image classifiers and LLM-style training settings.

## Limits and Failure Modes

Limits to watch: posterior-family choice controls the derived algorithm; full Hessian correction may be expensive; and the deep-learning scalability case depends on diagonal or otherwise approximate Gaussian structure.

## Deep Themes

- Optimization algorithms can be reinterpreted as approximate Bayesian updates.
- Variance reduction becomes a form of posterior knowledge transfer.
- Bayesian structure can generate new optimizer variants rather than only provide uncertainty estimates.

## Subthemes

- SVRG.
- Posterior correction.
- Variational Bayes.
- Exponential-family posteriors.
- Hessian correction.
- Adam-like stochastic optimization.

## Connections to Other Papers

Connects to DiReCT and the Jacobian-spectra paper through optimization geometry. It also links to theory-unifies-engineering papers where a familiar practical algorithm is recovered from a more general mathematical framework.

## Notes for Cross-Paper Synthesis

This paper adds to a recurring pattern: mature optimization heuristics are being reframed through richer theory in ways that produce concrete extensions, not just post-hoc explanations.
