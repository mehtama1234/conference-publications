# Guaranteed Optimal Compositional Explanations for Neurons

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: MHiiwC3oFR
- Authors: Biagio La Rosa; Leilani H. Gilpin
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: compositional explanations; informed search algorithms; spatial activation alignment; explainable artificial intelligence;
- Source URL: https://openreview.net/forum?id=MHiiwC3oFR
- PDF URL: https://openreview.net/pdf?id=MHiiwC3oFR

## Abstract

Compositional explanations are a family of methods that aim to describe the spatial alignment between neurons' receptive field activations and concepts through logical rules, typically computed via a search over all possible concept combinations. Since computing the spatial alignment over the entire state space is computationally infeasible, the literature commonly adopts assumptions related to the structure of the combinations and beam search to restrict the state space. However, beam search cannot provide any theoretical guarantees of optimality, and it remains unclear how close current explanations are to the true optimum. In this theoretical paper, we address this gap by introducing the first framework for computing guaranteed optimal compositional explanations over the entire state space spanned by the adopted assumptions. Specifically, we propose: (i) a decomposition that identifies the factors influencing the spatial alignment, (ii) a heuristic to estimate the alignment at any stage of the search, and (iii) the first algorithm that can compute optimal compositional explanations in a time comparable to exhaustive beam search. Using this framework,  we demonstrate that 10-40\% of explanations previously obtained with beam search are suboptimal when overlapping concepts are involved. Finally, we evaluate a beam-search variant guided by our proposed decomposition and heuristic, showing that it matches or improves runtime over prior methods while offering greater flexibility in hyperparameters and computational resources.

## One-Sentence Claim

The paper gives the first framework for guaranteed optimal compositional neuron explanations over the assumed concept-combination state space, revealing that many beam-search explanations are suboptimal.

## Problem

Compositional neuron explanations require searching concept combinations, but exhaustive alignment over the full state space is infeasible and beam search gives no optimality guarantees.

## Core Contribution

The paper decomposes factors affecting spatial activation alignment, designs a heuristic for estimating alignment during search, and provides an algorithm that computes optimal compositional explanations in time comparable to beam search.

## Method

The framework searches the entire state space implied by the adopted structural assumptions using the decomposition and heuristic to guide informed search while preserving optimality guarantees.

## Experiments and Evidence

The abstract reports that 10-40% of previously beam-search-derived explanations are suboptimal when concepts overlap, and that a guided beam-search variant matches or improves runtime while increasing flexibility.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: adopted explanation assumptions, search complexity, concept set construction, spatial alignment metric, model/dataset scope, and user-facing interpretability validation.

## Deep Themes

- Interpretability methods need optimality guarantees, not only plausible explanations.
- Search assumptions define the explanation space.
- Overlapping concepts expose failures in heuristic explanation search.

## Subthemes

- Compositional explanations.
- Neuron interpretability.
- Spatial activation alignment.
- Informed search.
- Beam search limitations.
- Explainable AI.

## Connections to Other Papers

Connects to M-CBE, FlashTrace, and interpretability-as-intervention papers through the demand for faithful, efficient, and guaranteed explanations.

## Notes for Cross-Paper Synthesis

This paper adds a guarantee-oriented interpretability theme: explanation quality should be audited against the search optimum, not judged only by whether the explanation seems coherent.
