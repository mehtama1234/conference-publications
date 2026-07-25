# The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: yRtgZ1K8hO
- Authors: Noah Amsel; David Persson; Christopher Musco; Robert M. Gower
- Primary area: optimization
- Keywords: polar decomposition;matrix sign;numerical linear algebra;muon;optimization;approximation theory
- Source URL: https://openreview.net/forum?id=yRtgZ1K8hO
- PDF URL: https://openreview.net/pdf?id=yRtgZ1K8hO

## Abstract

Computing the polar decomposition and the related matrix sign function has been a well-studied problem in numerical analysis for decades. Recently, it has emerged as an important subroutine  within the Muon algorithm for training deep neural networks.
However, the requirements of this application differ sharply from classical settings: deep learning demands GPU-friendly algorithms that prioritize high throughput over high precision. We introduce *Polar Express*, a new method for computing the polar decomposition. Like Newton–Schulz and other classical polynomial methods, our approach uses only matrix-matrix multiplications, making it 
very efficient on GPUs.
Inspired by earlier work of Chen \& Chow and Nakatsukasa \& Freund, *Polar Express* adapts the update rule at each iteration by solving a minimax optimization problem.
We prove that this strategy minimizes error in a worst-case sense, allowing *Polar Express* to converge as rapidly as possible both in the early iterations and asymptotically.
We also address finite-precision issues, making it practical to use in `bfloat16`. When integrated into Muon, our method yields consistent improvements in validation loss for a GPT-2 model on one to ten billion tokens from the FineWeb dataset, outperforming recent alternatives across a range of learning rates.

## One-Sentence Claim

Polar Express provides worst-case-optimal GPU-friendly matrix sign and polar-decomposition iterations, improving Muon optimizer performance for GPT-2 training in low precision.

## Problem

Classical polar-decomposition algorithms often prioritize high precision, but deep learning needs high-throughput GPU kernels and tolerates approximate low-precision computation. The Muon optimizer makes matrix sign computation a practical training subroutine, so faster and more stable approximations can directly affect model training.

## Core Contribution

The paper introduces Polar Express, a polynomial matrix-multiplication-only method whose iteration rule is adaptively chosen by solving a minimax optimization problem. It proves worst-case error optimality for rapid early and asymptotic convergence and addresses finite-precision use in `bfloat16`.

## Method

Like Newton-Schulz methods, Polar Express uses matrix-matrix multiplications suited to GPUs. At each iteration, it adapts the update rule using minimax approximation ideas inspired by Chen and Chow and by Nakatsukasa and Freund, targeting worst-case matrix sign error reduction under practical precision constraints.

## Experiments and Evidence

The abstract reports consistent validation-loss improvements when Polar Express is integrated into Muon for GPT-2 training on one to ten billion FineWeb tokens. It also reports outperformance over recent alternatives across a range of learning rates.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect exact matrix dimensions, optimizer settings, overhead versus loss gains, stability under different architectures, and sensitivity to low-precision rounding. A method optimized for Muon may be less relevant where matrix sign computations are not the training bottleneck.

## Deep Themes

- Numerical linear algebra as training infrastructure.
- GPU-friendly approximate matrix functions.
- Optimizer subroutines tuned for deep learning workloads.
- Worst-case approximation with low-precision practicality.

## Subthemes

- Polar decomposition.
- Matrix sign function.
- Muon optimizer.
- Minimax iteration design.
- `bfloat16` finite precision.

## Connections to Other Papers

Connects to efficiency-as-capability papers such as PGM, GLASS Flows, and MotionStream through algorithmic reformulation for practical throughput, and to optimization-theory notes through finite-regime behavior that matters in modern training loops.

## Notes for Cross-Paper Synthesis

Polar Express is an infrastructure paper in the strongest sense: it improves model training by revisiting a numerical primitive under the constraints of current accelerators. It fits the broader pattern that capability gains often come from reworking the substrate, not only model architecture.
