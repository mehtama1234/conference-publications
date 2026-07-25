# It's All Just Vectorization: einx, a Universal Notation for Tensor Operations

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: QqvQ3iAdpC
- Authors: Florian Fervers; Sebastian Bullinger; Christoph Bodensteiner; Michael Arens
- Primary area: other topics in machine learning (i.e., none of the above)
- Keywords: Tensor notation;tensor programming;einx;einsum;einops
- Source URL: https://openreview.net/forum?id=QqvQ3iAdpC
- PDF URL: https://openreview.net/pdf?id=QqvQ3iAdpC

## Abstract

Tensor operations represent a cornerstone of modern scientific computing. However, the Numpy-like notation adopted by predominant tensor frameworks is often difficult to read and write and prone to so-called shape errors, i.a., due to following inconsistent rules across a large, complex collection of operations. Alternatives like einsum and einops have gained popularity, but are inherently restricted to few operations and lack the generality required for a universal model of tensor programming.

To derive a better paradigm, we revisit vectorization as a function for transforming tensor operations, and use it to both lift lower-order operations to higher-order operations, and conceptually decompose higher-order operations to lower-order operations and their vectorization.

Building on the universal nature of vectorization, we introduce einx, a universal notation for tensor operations. It uses declarative, pointful expressions that are defined by analogy with loop notation and represent the vectorization of tensor operations. The notation reduces the large APIs of existing frameworks to a small set of elementary operations, applies consistent rules across all operations, and enables a clean, readable and writable representation in code. We provide an implementation of einx that is embedded in Python and integrates seamlessly with existing tensor frameworks: https://github.com/REMOVED_FOR_REVIEW

## One-Sentence Claim

einx proposes a universal declarative notation for tensor operations by treating vectorization as the core abstraction behind higher-order tensor programming.

## Problem

Tensor operations are foundational to ML and scientific computing, but mainstream NumPy-style APIs can be hard to read and prone to shape errors because related operations follow inconsistent conventions.

Notation systems such as einsum and einops improve clarity for some operations, but they do not cover the full range of tensor programming.

## Core Contribution

The paper introduces einx, a universal notation for tensor operations embedded in Python and designed to integrate with existing tensor frameworks.

It reduces large tensor APIs to a small set of elementary operations governed by consistent vectorization rules.

## Method

The paper revisits vectorization as a transformation that lifts lower-order operations into higher-order tensor operations and decomposes higher-order operations into lower-order operations plus vectorization.

einx uses declarative, pointful expressions analogous to loop notation, making tensor intent explicit while preserving framework interoperability.

## Experiments and Evidence

The abstract emphasizes conceptual and software-system contribution rather than benchmark performance.

Evidence comes from the claimed generality, readability, and writability of the notation, plus an implementation integrated with existing tensor frameworks.

## Limits and Failure Modes

A universal notation must still be learnable by practitioners and must compile efficiently across backends. Some users may prefer specialized APIs for common cases if universal notation adds cognitive overhead.

Because this note is abstract-only, details still need checking: supported operations, syntax examples, backend coverage, static shape checking, performance overhead, and adoption comparisons with einsum/einops.

## Deep Themes

- Tensor notation as infrastructure: programming abstractions affect correctness and productivity in ML.
- Vectorization as universal model: many tensor operations can be explained through one conceptual transformation.
- Shape-error reduction: clearer notation is a reliability tool for scientific code.
- Declarative tensor programming: operation intent is specified at a higher level than index-heavy code.

## Subthemes

- einx.
- Vectorization.
- Tensor DSLs.
- Shape-safe programming.

## Connections to Other Papers

This connects to TileLang through programming abstractions for ML systems, though at a different layer: tensor notation versus kernel tiling.

It also relates to scientific-computing papers because reproducible research depends on readable, less error-prone array code.

## Notes for Cross-Paper Synthesis

einx adds to the infrastructure theme: not all progress is model-side; better notations can reduce implementation errors and make complex tensor programs maintainable.
