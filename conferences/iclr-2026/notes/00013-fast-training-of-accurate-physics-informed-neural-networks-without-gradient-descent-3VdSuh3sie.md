# Fast training of accurate physics-informed neural networks without gradient descent

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 3VdSuh3sie
- Authors: Chinmay Datar; Taniya Kapoor; Abhishek Chandra; Qing Sun; Erik Lien Bolager; Iryna Burak; Anna Veselovska; Massimo Fornasier; Felix Dietrich
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: physics-informed neural networks;extreme learning machines;random features;partial differential equations;optimization;training;causality;neural PDE solvers;optimization
- Source URL: https://openreview.net/forum?id=3VdSuh3sie
- PDF URL: https://openreview.net/pdf?id=3VdSuh3sie

## Abstract

Solving time-dependent Partial Differential Equations (PDEs) is one of the most critical problems in computational science. While Physics-Informed Neural Networks (PINNs) offer a promising framework for approximating PDE solutions, their accuracy and training speed are limited by two core barriers: gradient-descent-based iterative optimization over complex loss landscapes and non-causal treatment of time as an extra spatial dimension. We present Frozen-PINN, a novel PINN based on the principle of space-time separation that leverages random features instead of training with gradient descent, and incorporates temporal causality by construction. On nine PDE benchmarks, including challenges like extreme advection speeds, shocks, and high-dimensionality, Frozen-PINNs achieve superior training efficiency and accuracy over state-of-the-art PINNs, often by several orders of magnitude. Our work addresses longstanding training and accuracy bottlenecks of PINNs, delivering quickly trainable, highly accurate, and inherently causal PDE solvers, a combination that prior methods could not realize. Our approach challenges the reliance of PINNs on stochastic gradient-descent-based methods and specialized hardware, leading to a paradigm shift in PINN training and providing a challenging benchmark for the community.

## One-Sentence Claim

Frozen-PINN replaces gradient-descent PINN training with random-feature space-time separation and built-in temporal causality, yielding faster and more accurate time-dependent PDE solvers.

## Problem

PINNs are attractive for PDE solving but suffer from slow iterative optimization over difficult loss landscapes and from treating time non-causally as just another spatial dimension.

## Core Contribution

The paper introduces Frozen-PINN, a physics-informed neural solver that uses random features instead of gradient descent and enforces temporal causality through space-time separation.

## Method

Frozen-PINN freezes random features and trains without stochastic gradient descent. It separates space and time so the solver respects causal temporal structure by construction.

## Experiments and Evidence

The abstract reports nine PDE benchmarks, including extreme advection, shocks, and high-dimensional cases, with several-orders-of-magnitude gains in training efficiency and accuracy over state-of-the-art PINNs.

## Limits and Failure Modes

PDF checks needed: exact linear solve/random feature training procedure, memory scaling, benchmark details, robustness to boundary/initial conditions, and whether gains hold for stiff or chaotic PDEs.

## Deep Themes

- Scientific ML is challenging default gradient-descent assumptions.
- Causality and physical structure are being built into solver architecture.
- Fast solvers can come from changing the training paradigm, not just optimizing hardware.

## Subthemes

- Physics-informed neural networks.
- Random features.
- Space-time separation.
- Causal PDE solving.
- Gradient-free training.

## Connections to Other Papers

Connects to DS-TS, PAR, Quotient-Space Diffusion, and broader scientific ML. It also links to efficiency themes by replacing expensive iterative training with a faster structured alternative.

## Notes for Cross-Paper Synthesis

Frozen-PINN is another example of scientific-domain pressure producing method-level changes: the physics and time structure of the problem dictate the learning procedure.

## Full-Text Upgrade

Source used: `conferences/iclr-2026/text/00013-fast-training-of-accurate-physics-informed-neural-networks-without-gradient-descent-3VdSuh3sie-arxiv.txt`.

Additional verified details:

- The paper identifies two root causes of PINN failure: high-dimensional multi-objective loss optimization and non-causal treatment of time.
- Frozen-PINN uses a single-hidden-layer separable space-time ansatz with frozen spatial random features and time-dependent coefficients.
- The method samples spatial bases using ELM or SWIM, then reformulates the PDE into an ODE for the temporal coefficients.
- It decouples PDE, boundary, and initial-condition losses rather than optimizing one entangled PINN objective.
- The paper reports up to 4-5 orders of magnitude faster training than SOTA PINNs across nine PDE benchmarks.
- For linear advection, the text reports solving extremely high advection speeds up to `10^4` with relative L2 errors below `1e-4`, while other neural PDE solvers fail beyond much lower speeds.

Refined limits:

- The method's effectiveness depends on the random-feature basis and the PDE-to-ODE reformulation.
- Full assessment requires checking benchmark diversity, stiffness, high-dimensional scaling, and boundary-condition handling.
