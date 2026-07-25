# Even Faster Kernel Matrix Linear Algebra via Density Estimation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ueNIrBXz7R
- Authors: Rikhav Shah; Sandeep Silwal; Haike Xu
- Primary area: theory->everything_else
- Keywords: Kernel Matrix;Sub-quadratic algorithms;Power Method;Matrix Vector Product;Gaussian kernel
- Source URL: https://openreview.net/forum?id=ueNIrBXz7R
- PDF URL: https://openreview.net/pdf?id=ueNIrBXz7R

## Abstract

This paper studies the use of *kernel density estimation* (KDE) for linear algebraic tasks involving the *kernel matrix* of a collection of $n$ data points in $\mathbb{R}^d$.
In particular, we improve upon the best existing algorithms for computing the following up to $(1+\varepsilon)$ relative error for a Gaussian kernel matrix and other kernels: matrix-vector products, matrix-matrix products, the spectral norm, and sum of all entries. The runtimes of our algorithms depend linearly on the dimension $d$, sub-quadratically in the number of points $n$, and polynomially on the target error $\varepsilon$. Importantly, the dependence on $n$ in each case is far lower when accessing the kernel matrix through KDE queries as opposed to reading individual entries. Our improvements over existing best algorithms (particularly those of [Backurs et al. ICML `21]) for these tasks reduce the polynomial dependence on $\varepsilon$, and additionally decrease the dependence on $n$ in the case of computing the sum of all entries of the kernel matrix. For example, we reduce the power of $1/\epsilon$ from $\approx 7.7$ to $\approx 3.2$ for a $1-\varepsilon$ relative error estimation of the spectral norm of a Gaussian kernel matrix. We complement our upper bounds with several lower bounds for related problems, which provide (conditional) quadratic time hardness results and additionally hint at the limits of KDE based approaches for the problems we study.

## One-Sentence Claim

Kernel density estimation queries can accelerate Gaussian-kernel matrix-vector, matrix-matrix, spectral-norm, and entry-sum computations with subquadratic dependence on n and improved epsilon dependence.

## Problem

Kernel matrices arise throughout machine learning, but explicit n-by-n access is expensive. Many linear-algebra tasks over kernel matrices, such as matrix-vector products and spectral norm estimation, become bottlenecks at large n.

The paper asks whether KDE query access can support faster algorithms than reading individual kernel entries, especially for Gaussian and related kernels.

## Core Contribution

The paper improves the best known algorithms for several kernel matrix linear algebra tasks up to relative error. The runtimes are linear in dimension d, subquadratic in number of points n, and polynomial in epsilon.

It improves dependence on epsilon over prior ICML 2021 algorithms and reduces n-dependence for summing all entries. For Gaussian spectral norm estimation, it lowers the power of 1/epsilon from about 7.7 to about 3.2.

## Method

The algorithms access the kernel matrix through KDE queries rather than individual entries. KDE aggregates kernel contributions efficiently, enabling faster approximations for matrix products, spectral norm, and total mass.

The paper also provides lower bounds for related problems, including conditional quadratic-time hardness results that clarify where KDE-based acceleration may stop.

## Experiments and Evidence

The abstract presents algorithmic upper bounds and lower bounds. The main evidence is theoretical runtime improvement for matrix-vector products, matrix-matrix products, spectral norm, and sum of entries under Gaussian and other kernels.

Full-paper reading should verify kernel classes, KDE oracle assumptions, approximation guarantees, lower-bound conditions, and whether practical implementations match asymptotic gains.

## Limits and Failure Modes

The speedups depend on access to efficient KDE queries. If KDE preprocessing or query costs are high in practice, gains may not materialize for all datasets.

Relative-error guarantees may also depend on kernel parameters, data geometry, and numerical conditioning. Lower bounds indicate that not all kernel algebra tasks can be accelerated the same way.

## Deep Themes

- Query-model algorithm design: changing matrix access from entries to KDE queries changes complexity.
- Subquadratic kernel computation: large kernel methods need aggregate approximations.
- Epsilon dependence matters: practical approximation algorithms can be dominated by error-parameter powers.
- Upper and lower bounds together: the paper maps both possibilities and limits of KDE access.

## Subthemes

- Gaussian kernels are the central case.
- Spectral norm estimation benefits strongly from improved epsilon exponents.
- Sum-of-entries computation gets better n-dependence.
- Conditional hardness clarifies limits of kernel acceleration.

## Connections to Other Papers

This paper connects to efficiency and theory work such as DHSA, STAR-KV, FFCC, and MoE compression, but at the algorithmic linear-algebra level. It also relates to Gaussian-process and kernel-method infrastructure behind probabilistic ML.

It fits a recurring theme: the right access pattern or computational primitive can change what large-scale method is feasible.

## Notes for Cross-Paper Synthesis

The synthesis point is that efficiency is often model-access dependent. Kernel matrices are expensive if accessed entrywise, but KDE queries expose aggregate structure that algorithms can exploit.
