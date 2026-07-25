# CoEvol-NO: State and Coordinate Co-Evolution with an Error-Driven Predictor-Corrector Paradigm for Neural Operator Transformer

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: pG9Wn3Aheq
- Authors: Jianqiao Zeng; Ruocheng Wang; Yanzhi Liu; Hao Xiong; Junchi Yan
- Primary area: applications
- Keywords: Neural Operator;Differential Equations;Attention
- Source URL: https://openreview.net/forum?id=pG9Wn3Aheq
- PDF URL: https://openreview.net/pdf?id=pG9Wn3Aheq

## Abstract

Despite the fast progress in neural operator learning, long-sequence modeling still is a standing challenge whereby latent states have been introduced with techniques well derived.  Diverging from existing methods that treat latent states as transient variables or decoupled representations, CoEvol-NO introduces a persistent state to establish a co-evolutionary framework, where the latent state and mesh sequence are updated jointly and bidirectionally. Inspired by classical numerical methods, we model the layer-wise state evolution as a Predictor-Corrector (PC) process. Specifically, a "Predictor'' generates a tentative target, followed by a "Corrector'' that refines the persistent state via an {error-driven update mechanism}. Furthermore, our theoretical analysis reveals that the widely used \textit{direct substitution} and \textit{residual update} paradigms are essentially {first-order approximations} of this error-driven correction under different loss assumptions. We theoretically prove that CoEvol-NO achieves strict linear time complexity. Extensive experiments on five standard benchmarks and two large-scale industrial design tasks demonstrate that CoEvol-NO consistently achieves state-of-the-art (SOTA) performance.

## One-Sentence Claim

CoEvol-NO improves long-sequence neural operator modeling by jointly evolving persistent latent states and mesh coordinates through an error-driven predictor-corrector process with linear complexity.

## Problem

Neural operators are powerful for learning solution maps of differential equations, but long-sequence modeling remains difficult. Existing latent-state methods often treat states as transient variables or decoupled representations, limiting their ability to maintain coherent dynamics across long sequences.

The challenge is to model evolving physical fields and their coordinate/mesh structure together while keeping computation scalable enough for large industrial tasks.

## Core Contribution

The paper introduces a co-evolutionary neural operator Transformer in which persistent latent state and mesh sequence are updated jointly and bidirectionally. It frames layer-wise state evolution as a predictor-corrector process inspired by classical numerical methods.

The theoretical contribution is to show that common direct-substitution and residual-update paradigms can be viewed as first-order approximations of the proposed error-driven correction under different loss assumptions.

## Method

CoEvol-NO uses a Predictor to generate a tentative target and a Corrector to refine the persistent state via an error-driven update. The state is persistent across layers rather than discarded as a transient hidden variable.

The model co-evolves state and coordinates/mesh sequence, allowing changes in one to inform updates in the other. The authors prove strict linear time complexity, positioning the architecture for long sequences and large-scale design tasks.

## Experiments and Evidence

The abstract reports state-of-the-art performance on five standard benchmarks and two large-scale industrial design tasks. It also reports theoretical linear-time complexity and a unifying analysis of direct-substitution and residual updates.

Full-paper reading should inspect benchmark identities, industrial task details, sequence lengths, mesh resolutions, ablations for predictor/corrector components, and wall-clock/runtime scaling.

## Limits and Failure Modes

The method's gains likely depend on how well the persistent state captures the relevant physical dynamics. If the state update accumulates errors, long-sequence prediction could drift despite the corrective mechanism.

The framework is inspired by numerical methods, but learned predictor-corrector updates may not inherit stability guarantees of classical solvers unless explicitly proven. Industrial-task generality should be checked beyond the reported domains.

## Deep Themes

- Neural operators as learned numerical methods: architecture borrows predictor-corrector structure from classical solvers.
- Persistent latent state: long-sequence modeling benefits when memory is a maintained object, not a transient activation.
- Coordinate-state co-evolution: physical fields and discretization geometry are modeled together.
- Theory unifies architectural heuristics: residual and substitution updates become first-order approximations of a broader correction rule.

## Subthemes

- Error-driven correction provides a principled update signal.
- Linear complexity is central for long sequence and industrial settings.
- Mesh-aware updates reflect the geometry of differential-equation data.
- Persistent state can reduce the mismatch between neural sequence models and evolving physical systems.

## Connections to Other Papers

CoEvol-NO connects to MERLIN, WestWorld, and Excited Pfaffians as structured scientific/physical-domain models. All three use domain structure to scale across time, morphology, or quantum state.

It also relates to the scaling-law and stochastic Transformer theory papers because it studies layer-wise dynamics rather than treating the network as a static function approximator.

## Notes for Cross-Paper Synthesis

The synthesis point is that scientific ML increasingly looks like hybridization between neural representation learning and classical numerical structure. CoEvol-NO makes the solver metaphor explicit through predictor-corrector dynamics.
