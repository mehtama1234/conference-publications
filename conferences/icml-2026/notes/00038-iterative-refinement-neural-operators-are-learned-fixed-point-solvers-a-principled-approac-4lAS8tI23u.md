# Iterative Refinement Neural Operators are Learned Fixed-Point Solvers: A Principled Approach to Spectral Bias Mitigation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 4lAS8tI23u
- Authors: Xiaotian Liu; Shuyuan Shang; Xiaopeng Wang; Pu Ren; Yaoqing Yang
- Primary area: deep_learning->everything_else
- Keywords: Neural Operators;Scientific Machine Learning;Spectral Bias
- Source URL: https://openreview.net/forum?id=4lAS8tI23u
- PDF URL: https://openreview.net/pdf?id=4lAS8tI23u

## Abstract

Neural operators serve as fast, data-driven surrogates for scientific modeling but typically rely on a monolithic, single-pass inference procedure that struggles to resolve high-frequency details, a limitation known as spectral bias. We introduce the Iterative Refinement Neural Operator (IRNO), which augments pre-trained operators with a learned refinement module iteratively applied via fixed-point iteration. IRNO decomposes the prediction into a coarse initialization followed by successive residual corrections, paralleling classical numerical solvers. Under mild assumptions, we establish contraction of the induced operator, ensuring convergence to a unique fixed point. To explicitly target high-frequency errors, we propose a progressive spectral loss that adaptively increases penalty on high-frequency components over refinement steps during training. 
Across physical systems, IRNO consistently lowers error, with up to 56.05\% improvement on turbulent flow. On Active Matter, spectral analysis reveals that, relative to base operator, the normalized error ratios decrease to 27.72–36.10\% in low-, 5.07–6.68\% in mid-, and 1.48–2.04\% in high-frequencies, remaining stable beyond the trained iteration count.

## One-Sentence Claim

IRNO turns neural-operator inference into a learned fixed-point refinement process, reducing spectral bias by iteratively correcting residual high-frequency errors.

## Problem

Neural operators are fast surrogates for physical systems but usually perform monolithic single-pass prediction, which tends to miss high-frequency details due to spectral bias.

## Core Contribution

The paper introduces Iterative Refinement Neural Operators, adds a learned residual refinement module to pretrained operators, proves local fixed-point convergence under contraction assumptions, and trains with a progressive spectral loss.

## Method

A base neural operator provides a coarse prediction. A shared refinement module is iteratively applied to the current estimate to predict residual corrections. Training includes fixed-point regularization and a spectral loss that increasingly emphasizes high-frequency components over refinement steps.

## Experiments and Evidence

The abstract reports consistent error reduction across physical systems, up to 56.05% improvement on turbulent flow, and strong mid/high-frequency error reductions on Active Matter that remain stable beyond the trained iteration count.

## Full-Text Upgrade

The full text frames IRNO as a function-space fixed-point solver rather than a larger one-shot network. The update module learns iteration-invariant residual dynamics, and the analysis gives contraction-style convergence with a possible residual floor controlled by fixed-point bias. This explains why extra test-time iterations can continue improving or remain stable beyond the training cutoff.

Experiments cover Turbulent Radiative Layer, Active Matter, ERA5 super-resolution, and irregular-mesh rollout settings. IRNO transfers across base operators such as FNO, TFNO, WDSR, and RIGNO, suggesting it learns residual-correction geometry rather than only memorizing one architecture's errors. The spectral analysis reports especially large reductions in mid- and high-frequency bands, matching the method's stated purpose of mitigating spectral bias.

## Limits and Failure Modes

Limits to watch: convergence is local and assumption-dependent; repeated iterations add inference cost; the residual floor depends on learned fixed-point bias; and stability under severe distribution shift or very long rollout horizons needs continued testing.

## Deep Themes

- Neural surrogates are being recast as learned numerical solvers.
- Test-time iteration can improve scientific predictions without retraining the base operator.
- Spectral bias can be attacked through staged residual correction rather than architecture alone.

## Subthemes

- Neural operators.
- Fixed-point solvers.
- Spectral bias.
- Progressive spectral loss.
- Residual refinement.
- Scientific surrogate modeling.

## Connections to Other Papers

Connects to Frozen-PINN and physical dynamical solvers through solver-inspired scientific ML. It also links to quantized diffusion error propagation as another iterative process where errors must be corrected over steps.

## Notes for Cross-Paper Synthesis

IRNO adds a learned-solver theme: many ML systems for science are moving toward hybrid forms that borrow convergence, residual, and frequency ideas from numerical analysis.
