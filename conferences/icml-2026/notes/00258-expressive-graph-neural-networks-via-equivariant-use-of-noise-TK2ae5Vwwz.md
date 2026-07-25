# Expressive Graph Neural Networks via Equivariant Use of Noise

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: TK2ae5Vwwz
- Authors: Xiyuan Wang; Muhan Zhang
- Primary area: deep_learning->graph_neural_networks
- Keywords: Graph Neural Network;Expressivity
- Source URL: https://openreview.net/forum?id=TK2ae5Vwwz
- PDF URL: https://openreview.net/pdf?id=TK2ae5Vwwz

## Abstract

Expressivity has been a major focus in the design of Graph Neural Networks (GNNs), yet a significant gap persists between theoretical universal expressivity and practical performance. While many expressive GNNs are efficient and achieve strong results, they often focus on specific graph properties and lack theoretical expressivity for general graph tasks. Conversely, theoretically universal-expressive models often suffer from high computational costs or poor generalization, limiting their real-world applicability. To bridge this gap, we introduce Equivariant Noise GNNs (ENGNNs), a framework that utilizes random noise features to enhance the expressivity of GNNs. Crucially, unlike prior methods that naively use noise, we enforce equivariance to nodewise noise transformations, such as orthogonal transformations. We prove that this property reduces the model's theoretical sample complexity, thereby improving generalization. Our framework simultaneously reaches theoretical universal expressivity, maintains the linear scalability of standard Message-Passing Neural Networks in practice, and achieves performance comparable to computationally expensive, high-expressivity models. Extensive experiments confirm strong performance across node, link, subgraph, and graph-level prediction tasks, demonstrating that the equivariant use of noise provides a powerful and practical pathway for building expressive GNNs. Our code is available at \url{https://github.com/MuLabPKU/EquivNoiseGNN}.

## One-Sentence Claim

Equivariant random-noise features can give GNNs universal expressivity while preserving message-passing-like scalability and improving generalization relative to naive noise injection.

## Problem

GNN research faces a persistent expressivity-practicality tradeoff. Standard message-passing GNNs scale well and generalize, but cannot express all graph functions. Highly expressive or universal models often pay steep computational costs or generalize poorly.

Noise has been used to distinguish nodes and break symmetries, but naive noise injection can create instability or sample complexity problems because the model may learn arbitrary noise-coordinate artifacts.

## Core Contribution

The paper introduces Equivariant Noise GNNs, or ENGNNs, which augment graphs with random noise features while enforcing equivariance to nodewise transformations of that noise, such as orthogonal transformations. The claim is that this preserves the useful symmetry-breaking power of noise while reducing sample complexity and improving generalization.

ENGNNs aim to satisfy three goals simultaneously: universal expressivity, linear scalability comparable to standard message passing in practice, and competitive empirical performance against heavier expressive GNNs.

## Method

ENGNNs attach random noise features to nodes but constrain the architecture so outputs transform equivariantly under allowed transformations of the noise. This prevents the model from depending on arbitrary coordinate choices in the noise space while still using noise to disambiguate graph structures that message passing alone cannot distinguish.

The theory studies sample complexity under the equivariance constraint. The empirical framework evaluates the same idea across node, link, subgraph, and graph-level prediction tasks.

## Experiments and Evidence

Evidence includes:

- A theoretical expressivity result claiming universal expressivity.
- A sample-complexity argument showing equivariant noise improves generalization compared with unconstrained noise usage.
- Experiments across node prediction, link prediction, subgraph tasks, and graph-level prediction.
- Performance comparable to more computationally expensive high-expressivity models while retaining practical linear scalability.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact universality class, allowed noise groups, architecture equations, benchmark list, and wall-clock/memory comparisons.

## Limits and Failure Modes

- Random-noise methods can have variance across samples or seeds; the abstract does not specify inference-time averaging or stability.
- Universal expressivity may apply under assumptions that are stronger than real deployment settings.
- Equivariance constraints reduce arbitrary dependence on noise coordinates but may limit useful learned asymmetries in some tasks.
- Linear scalability "in practice" needs inspection for constants, hidden dimensions, and noise-feature sizes.

## Deep Themes

**Symmetry breaking needs symmetry control.** Noise helps distinguish graph structures, but the model must be invariant/equivariant to irrelevant noise-coordinate choices.

**Expressivity and generalization are jointly architectural.** The paper does not accept universal expressivity alone as sufficient; it pairs it with sample-complexity control.

**Randomness becomes a structured representation resource.** Noise is not merely regularization; it is an equivariant input channel for expanding graph distinguishability.

## Subthemes

- Universal expressivity under practical scaling constraints.
- Orthogonal equivariance over nodewise noise transformations.
- Noise as a graph isomorphism-breaking device.
- Sample-complexity-aware architecture design.

## Connections to Other Papers

Connects directly to RECM and other symmetry-adaptive papers: both argue that equivariance should be controlled rather than blindly enforced. It also links to graph adaptation work such as PSAHS, which modifies graph structure to improve learning, and to representation-geometry papers where constraints on latent coordinates improve generalization.

## Notes for Cross-Paper Synthesis

ENGNNs add another instance of a broad pattern: models increasingly use auxiliary degrees of freedom, such as noise, adapters, memories, or latent variables, but must quotient out arbitrary coordinate choices so those degrees of freedom do not become shortcuts.
