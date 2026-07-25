# Local Mechanisms of Compositional Generalization in Conditional Diffusion

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: XsfjvLhKAP
- Authors: Arwen Bradley
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: diffusion;composition;generalization
- Source URL: https://openreview.net/forum?id=XsfjvLhKAP
- PDF URL: https://openreview.net/pdf?id=XsfjvLhKAP

## Abstract

Conditional diffusion models appear capable of compositional generalization, i.e., generating convincing samples for out-of-distribution combinations of conditioners, but the mechanisms underlying this ability remain unclear. To make this concrete, we study length generalization, the ability to generate images with more objects than seen during training. In a controlled CLEVR setting (Johnson et al., 2017), we find that length generalization is achievable in some cases but not others, suggesting that models only sometimes learn the underlying compositional structure. We then investigate locality as a structural mechanism for compositional generalization. Prior works proposed score locality as a mechanism for creativity in unconditional diffusion models (Kamb & Ganguli, 2024; Niedoba et al., 2024), but did not address flexible conditioning or compositional generalization. In this paper, we prove an exact equivalence between a specific compositional structure (*conditional projective composition*) (Bradley et al., 2025) and scores with sparse dependencies on both pixels and conditioners (*local conditional scores*). This theory also extends to compositions of concepts (such as style+content) in feature-space. We validate our theory empirically: CLEVR models that succeed at length generalization exhibit local conditional scores, while those that fail do not. Furthermore, we show that a causal intervention explicitly enforcing local conditional scores enables length generalization in a previously failing model. Finally, we investigate feature-space compositionality in color-conditioned CLEVR, and find preliminary evidence of compositional structure and corresponding local mechanisms in SDXL.

## One-Sentence Claim

Conditional diffusion models length-generalize compositionally when their scores have sparse local dependencies on pixels and conditioners, and enforcing locality can cause generalization to emerge.

## Problem

Conditional diffusion models sometimes generate out-of-distribution combinations of conditioning factors, but the mechanisms behind this compositional generalization are unclear. Length generalization, generating more objects than seen during training, gives a concrete test case.

The paper asks when diffusion models learn underlying compositional structure rather than memorizing training-length patterns.

## Core Contribution

The paper studies CLEVR length generalization and finds it succeeds in some cases but not others. It then identifies locality as a mechanism: local conditional scores with sparse dependencies on pixels and conditioners are exactly equivalent to a specific compositional structure called conditional projective composition.

Empirically, models that length-generalize exhibit local conditional scores, while failing models do not. A causal intervention enforcing local conditional scores enables length generalization in a previously failing model. The theory also extends to feature-space style/content composition, with preliminary evidence in SDXL.

## Method

The method combines controlled diffusion experiments, theory, and intervention. It measures score dependencies in conditional diffusion models, proves equivalence between local conditional scores and projective composition, and edits or constrains a model to enforce locality.

CLEVR provides controlled object-count composition; feature-space experiments test whether the same mechanism appears in broader text-to-image models.

## Experiments and Evidence

Evidence reported in the abstract:

- Controlled CLEVR length-generalization experiments.
- Exact equivalence proof between conditional projective composition and local conditional scores.
- Empirical link between successful length generalization and local scores.
- Causal intervention enforcing local conditional scores in a failing model.
- Feature-space compositionality evidence in color-conditioned CLEVR and preliminary SDXL analysis.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: locality metric, intervention implementation, training distributions, and SDXL analysis scope.

## Limits and Failure Modes

- CLEVR is controlled and may not reflect natural-image compositional complexity.
- Locality may explain some composition types but not global relational constraints.
- Enforcing locality could harm tasks requiring long-range dependencies.
- SDXL evidence is preliminary per the abstract.

## Deep Themes

**Compositional generalization has local mechanisms.** Successful diffusion models exhibit sparse score dependencies rather than diffuse global entanglement.

**Mechanistic claims should support interventions.** The paper does not only observe locality; it enforces it to recover generalization.

**Diffusion score geometry explains behavior.** Compositionality is tied to the dependency structure of the learned score field.

## Subthemes

- Length generalization in conditional diffusion.
- Local conditional scores.
- Conditional projective composition.
- Causal enforcement of locality.
- Feature-space style/content composition.

## Connections to Other Papers

Connects to OCE, UDM-GRPO, RelaxFlow, and Flowers through geometric/vector-field views of generation. It also links to interpretability papers because the mechanism is made testable through causal intervention.

## Notes for Cross-Paper Synthesis

This paper adds a high-value mechanistic pattern: generalization is not just measured; it is traced to a local dependency property that can be intervened on.
