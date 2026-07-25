# Joint Learning in the Gaussian Single Index Model

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: xf1OYJfvqj
- Authors: Loucas Pillaud-Vivien; Adrien Schertzer
- Primary area: optimization->nonconvex
- Keywords: Representation Learning; Nonlinear Regression; Single-Index Models; Optimization; Gradient Descent
- Source URL: https://openreview.net/forum?id=xf1OYJfvqj
- PDF URL: https://openreview.net/pdf?id=xf1OYJfvqj

## Abstract

We consider the problem of jointly learning a one-dimensional projection and a univariate function in high-dimensional Gaussian models. Specifically, we study predictors of the form $f(x)=\varphi^\star(\langle  w^\star, x \rangle)$, where both the direction $w^\star \in \mathcal{S}_{d-1}$, the sphere of $\mathbb{R}^d$, and the function $\varphi^\star: \mathbb{R} \to \mathbb{R}$ are learned from Gaussian data. This setting captures a fundamental non-convex problem at the intersection of representation learning and nonlinear regression. We analyze the gradient flow dynamics of a natural alternating scheme and prove convergence, with a rate controlled by the information exponent reflecting the *Gaussian regularity* of the function $\varphi^\star$. Strikingly, our analysis shows that convergence still occurs even when the initial direction is negatively correlated with the target. On the practical side, we demonstrate that such joint learning can be effectively implemented using a Reproducing Kernel Hilbert Space (RKHS) adapted to the structure of the problem, enabling efficient and flexible estimation of the univariate function. Our results offer both theoretical insight and practical methodology for learning low-dimensional structure in high-dimensional settings.

## One-Sentence Claim

Joint learning in Gaussian single-index models can converge under an alternating gradient-flow scheme, with rates controlled by the Gaussian regularity of the learned univariate function.

## Problem

Single-index models reduce high-dimensional nonlinear regression to learning a direction and a one-dimensional link function, but jointly learning both is nonconvex.

The problem sits between representation learning and nonlinear regression: recover the projection direction w* and the scalar function phi* from Gaussian data.

## Core Contribution

The paper analyzes gradient-flow dynamics for a natural alternating scheme that jointly learns the direction and the univariate function.

It proves convergence with a rate governed by an information exponent reflecting Gaussian regularity, and shows convergence can occur even when the initial direction is negatively correlated with the target.

## Method

The theoretical setup assumes predictors of the form f(x) = phi*(<w*, x>) with Gaussian inputs. The alternating scheme updates the direction and function in a coupled nonconvex system.

On the practical side, the paper implements the univariate function in an RKHS adapted to the problem structure, enabling flexible estimation.

## Experiments and Evidence

The abstract reports convergence analysis and practical implementation with an adapted RKHS.

It emphasizes the surprising result that negative initial correlation does not prevent convergence, which suggests the dynamics can escape some intuitive bad starts.

## Limits and Failure Modes

The results are specialized to Gaussian single-index structure and may depend strongly on the regularity of phi*. Real data may violate Gaussianity, single-index assumptions, or one-dimensional latent structure.

Because this note is abstract-only, details still need checking: exact alternating scheme, information exponent definition, sample complexity, RKHS construction, finite-sample experiments, and robustness to model misspecification.

## Deep Themes

- Low-dimensional structure in high-dimensional data: representation learning can be analyzable when the latent form is constrained.
- Nonconvex dynamics with benign convergence: alternating learning can work beyond positive initialization.
- Function regularity controls optimization: Gaussian regularity shapes convergence rates.
- Theory-to-method bridge: RKHS implementation turns the model analysis into an estimator.

## Subthemes

- Gaussian single-index models.
- Alternating gradient flow.
- Information exponent.
- RKHS-adapted univariate regression.

## Connections to Other Papers

This connects to alignment-sensitive spectral algorithms, Adam degeneracy, and neural tangent/kernel theory papers through fine-grained analysis of optimization under structured assumptions.

It also relates to causal representation and low-dimensional representation learning work because both seek recoverable structure in high-dimensional observations.

## Notes for Cross-Paper Synthesis

This paper adds a tractable representation-learning theme: high-dimensional learning becomes provable when the unknown representation has a narrow geometric form.
