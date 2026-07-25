# Characterizing the Discrete Geometry of ReLU Networks

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: TgLW2DiRDG
- Authors: Blake B. Gaines; Jinbo Bi
- Primary area: learning theory
- Keywords: Polyhedrons;Geometry;ReLU;Activations
- Source URL: https://openreview.net/forum?id=TgLW2DiRDG
- PDF URL: https://openreview.net/pdf?id=TgLW2DiRDG

## Abstract

It is well established that ReLU networks define continuous piecewise-linear functions, and that their linear regions are polyhedra in the input space. These regions form a complex that fully partitions the input space. The way these regions fit together is fundamental to the behavior of the network, as nonlinearities occur only at the boundaries where these regions connect. However, relatively little is known about the geometry of these complexes beyond bounds on the total number of regions, and calculating the complex exactly is intractable for most networks. In this work, we prove new theoretical results about these complexes that hold for all fully-connected ReLU networks, specifically about their connectivity graphs in which nodes correspond to regions and edges exist between each pair of regions connected by a face. We find that the average degree of this graph is upper bounded by twice the input dimension regardless of the width and depth of the network, and that the diameter of this graph has an upper bound that does not depend on input dimension, despite the number of regions increasing exponentially with input dimension. We corroborate our findings through experiments with networks trained on both synthetic and real-world data, which provide additional insight into the geometry of ReLU networks.

## One-Sentence Claim

This paper characterizes ReLU network linear-region complexes through connectivity graphs, proving sparse average degree and dimension-independent diameter bounds.

## Problem

ReLU networks define continuous piecewise-linear functions whose linear regions partition input space into polyhedral complexes. Nonlinear behavior occurs at the boundaries between these regions.

Most prior understanding focuses on counting regions, while the way regions connect is less understood and exact computation is usually intractable.

## Core Contribution

The paper proves new results about connectivity graphs of linear-region complexes for fully connected ReLU networks.

It shows the average degree is upper bounded by twice the input dimension regardless of width and depth, and the graph diameter has an upper bound independent of input dimension despite exponentially many regions.

## Method

The analysis studies the graph whose nodes are linear regions and whose edges connect regions sharing a face.

Theoretical bounds characterize how local adjacency and global traversal behave across all fully connected ReLU networks, and experiments inspect trained networks on synthetic and real data.

## Experiments and Evidence

The abstract reports experiments on synthetic and real-world trained networks that corroborate and enrich the theoretical geometry results.

The evidence suggests region complexes have constrained connectivity structure even when the number of regions grows explosively.

## Limits and Failure Modes

The results cover fully connected ReLU networks and may not directly transfer to convolutional, residual, attention, or normalization-heavy architectures.

Because this note is abstract-only, details still need checking: exact diameter bound, proof assumptions, empirical region-estimation method, datasets, and relation to training dynamics.

## Deep Themes

- Discrete geometry of neural functions: piecewise-linear regions form structured complexes, not just large counts.
- Connectivity over capacity: how regions touch may matter more than how many exist.
- Architecture-independent constraints: some geometric properties hold regardless of width and depth.
- Theory for nonlinear boundaries: ReLU nonlinearity is understood through polyhedral adjacency.

## Subthemes

- ReLU linear regions.
- Polyhedral complexes.
- Region connectivity graph.
- Diameter and average-degree bounds.

## Connections to Other Papers

This connects to scaling-law spectra, floating-point expressivity, and representation-geometry theory papers.

It also relates to interpretability work because region adjacency describes where model behavior changes.

## Notes for Cross-Paper Synthesis

This paper adds a discrete-geometry theme: neural network complexity is not only measured by size or region count, but by the topology of how local linear behaviors connect.
