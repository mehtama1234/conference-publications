# Navigating the Latent Space Dynamics of Neural Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: Zunww3FHPU
- Authors: Marco Fumero; Luca Moschella; Emanuele Rodolà; Francesco Locatello
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: Representation learning;latent vector field;autoencoders;memorization and generalization;attractor
- Source URL: https://openreview.net/forum?id=Zunww3FHPU
- PDF URL: https://openreview.net/pdf?id=Zunww3FHPU

## Abstract

Neural networks transform high-dimensional data into compact, structured representations, often modeled as elements of a lower dimensional latent space. In this paper, we present an alternative interpretation of neural models as dynamical systems acting on the latent manifold. Specifically, we show that autoencoder models implicitly define a _latent vector field_ on the manifold, derived by iteratively applying the encoding-decoding map, without any additional training. We observe that standard training procedures introduce inductive biases that lead to the emergence of attractor points within this vector field.
Drawing on this insight, we propose to leverage the vector field as a _representation_ for the network, providing a novel tool to analyze the properties of the model and the data. This representation enables to: $(i)$ analyze the generalization and memorization regimes of neural models, even throughout training; $(ii)$ extract prior knowledge encoded in the network's parameters from the attractors, without requiring any input data; $(iii)$ identify out-of-distribution samples from their trajectories in the vector field.
We further validate our approach on vision foundation models, showcasing the applicability and effectiveness of our method in real-world scenarios.

## One-Sentence Claim

This paper interprets autoencoders as latent dynamical systems whose induced vector fields reveal memorization, generalization, prior knowledge, and out-of-distribution behavior.

## Problem

Neural representations are often treated as static points in latent space, but model behavior can also be understood through how representations move under repeated encode-decode application.

The field needs tools to analyze generalization, memorization, and encoded prior knowledge without relying only on external datasets or downstream probes.

## Core Contribution

The paper shows that autoencoder models implicitly define a latent vector field on the data manifold without additional training.

It proposes using that vector field as a representation of the network and data, enabling analysis of training regimes, attractors, and OOD trajectories.

## Method

The method repeatedly applies the encoding-decoding map and studies the resulting movement in latent space.

Training-induced inductive biases produce attractor points in this vector field. These attractors and trajectories are then used to inspect memorization/generalization, extract parameter-encoded prior knowledge without input data, and flag OOD samples.

## Experiments and Evidence

The abstract reports validation on vision foundation models.

The approach is shown to analyze model regimes during training, extract prior knowledge from attractors, and detect OOD samples from latent trajectories.

## Limits and Failure Modes

The method's interpretation depends on autoencoder structure and may not transfer directly to arbitrary transformers without encoder-decoder maps. Attractor analysis may also be sensitive to latent dimensionality and reconstruction quality.

Because this note is abstract-only, details still need checking: vector-field definition, attractor extraction, model classes, OOD benchmarks, training-time analysis, and comparisons to representation probes.

## Deep Themes

- Latent dynamics over static embeddings: model representations can be analyzed as vector fields.
- Attractors as prior knowledge: parameterized models encode structure that can be extracted without data.
- Memorization-generalization geometry: trajectories reveal whether samples fall into learned basins.
- Training-free model analysis: repeated model application becomes a diagnostic instrument.

## Subthemes

- Latent vector fields.
- Autoencoder dynamics.
- Attractor analysis.
- OOD trajectory detection.

## Connections to Other Papers

This connects to TD-JEPA, Koopman representation, LLM DNA, Hubble, and representation-geometry papers.

It also relates to interpretability work because latent dynamics expose internal model behavior without modifying the model.

## Notes for Cross-Paper Synthesis

This paper adds a latent-dynamics diagnostic theme: model behavior can be represented by flows and attractors in latent space, not just by outputs or embeddings.
