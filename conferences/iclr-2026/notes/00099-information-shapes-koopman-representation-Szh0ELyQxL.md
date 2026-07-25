# Information Shapes Koopman Representation

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: Szh0ELyQxL
- Authors: Xiaoyuan Cheng; Wenxuan Yuan; Yiming Yang; Yuanzhao Zhang; Sibo Cheng; Yi He; Zhuo Sun
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: Koopman Operator;Latent subspace reconstruction;representation for physical systems
- Source URL: https://openreview.net/forum?id=Szh0ELyQxL
- PDF URL: https://openreview.net/pdf?id=Szh0ELyQxL

## Abstract

The Koopman operator provides a powerful framework for modeling dynamical systems and has attracted growing interest from the machine learning community. However, its infinite-dimensional nature makes identifying suitable finite-dimensional subspaces challenging, especially for deep architectures. We argue that these difficulties come from suboptimal representation learning, where latent variables fail to balance expressivity and simplicity. This tension is closely related to the information bottleneck (IB) dilemma: constructing compressed representations that are both compact and predictive. Rethinking Koopman learning through this lens, we demonstrate that latent mutual information promotes simplicity, yet an overemphasis on simplicity may cause latent space to collapse onto a few dominant modes. In contrast, expressiveness is sustained by the von Neumann entropy, which prevents such collapse and encourages mode diversity. This insight leads us to propose an information-theoretic Lagrangian formulation that explicitly balances this tradeoff. Furthermore, we propose a new algorithm based on the Lagrangian formulation that encourages both simplicity and expressiveness, leading to a stable and interpretable Koopman representation. Beyond quantitative evaluations, we further visualize the learned manifolds under our representations, observing empirical results consistent with our theoretical predictions. Finally, we validate our approach across a diverse range of dynamical systems, demonstrating improved performance over existing Koopman learning methods.

## One-Sentence Claim

This paper uses an information-theoretic Lagrangian to balance simplicity and expressiveness in learned Koopman representations, preventing collapse while improving dynamical-system modeling.

## Problem

Koopman operators provide a linear operator view of nonlinear dynamics, but the relevant operator is infinite-dimensional.

Deep Koopman methods must identify finite-dimensional latent subspaces that are both compact and predictive. Poor representation learning can either overcompress dynamics or become unnecessarily complex.

## Core Contribution

The paper reframes Koopman representation learning through the information bottleneck dilemma.

It argues that latent mutual information promotes simplicity but can collapse onto dominant modes, while von Neumann entropy sustains mode diversity. The proposed information-theoretic Lagrangian balances these forces.

## Method

The method optimizes a Lagrangian that explicitly trades off compactness and expressiveness in the latent Koopman subspace.

The resulting algorithm encourages stable and interpretable representations, with latent mutual information and von Neumann entropy serving complementary roles.

## Experiments and Evidence

The abstract reports quantitative evaluations across diverse dynamical systems.

It also visualizes learned manifolds and finds empirical behavior consistent with the theoretical predictions, improving over existing Koopman learning methods.

## Limits and Failure Modes

Estimating information quantities in deep latent spaces can be difficult, and von Neumann entropy may depend on representation choices. Physical systems with discontinuities, chaos, or hidden forcing may still challenge finite-dimensional Koopman approximations.

Because this note is abstract-only, details still need checking: exact Lagrangian, information estimators, dynamical systems tested, baseline methods, stability metrics, and interpretability evidence.

## Deep Themes

- Information-shaped dynamics representations: compactness and expressiveness must be balanced explicitly.
- Koopman subspace discovery: representation learning is the bottleneck for finite-dimensional operator models.
- Entropy against mode collapse: preserving diverse dynamical modes improves stability and interpretability.
- Theory-guided physical modeling: information principles structure learned representations for scientific systems.

## Subthemes

- Koopman operator.
- Information bottleneck.
- Von Neumann entropy.
- Latent subspace reconstruction.

## Connections to Other Papers

This connects to TD-JEPA, Linear Recurrent Memory, SFA, and Wasserstein GPCA through structured latent representations.

It also relates to physics/scientific modeling papers that use theory-guided objectives to stabilize learned dynamics.

## Notes for Cross-Paper Synthesis

The paper adds to a recurring representation theme: useful latent spaces must preserve enough modes for downstream dynamics while discarding irrelevant complexity.
