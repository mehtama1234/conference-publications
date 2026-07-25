# Provably Explaining Neural Additive Models

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 040ClRXMf3
- Authors: Shahaf Bassan; Yizhak Yisrael Elboher; Tobias Ladner; Volkan Şahin; Jan Kretinsky; Matthias Althoff; Guy Katz
- Primary area: interpretability and explainable AI
- Keywords: explainability;XAI;explainable AI;formal verification;sufficient explanations
- Source URL: https://openreview.net/forum?id=040ClRXMf3
- PDF URL: https://openreview.net/pdf?id=040ClRXMf3

## Abstract

Despite significant progress in post-hoc explanation methods for neural
networks, many remain heuristic and lack provable guarantees. A key approach
for obtaining explanations with provable guarantees is by identifying a
cardinally-minimal subset of input features which by itself is provably
sufficient to determine the prediction. However, for standard neural networks,
this task is often computationally infeasible, as it demands a worst-case
exponential number of verification queries in the number of input features,
each of which is NP-hard.
  In this work, we show that for Neural Additive Models (NAMs), a recent and
more interpretable neural network family, we can efficiently generate
explanations with such guarantees. We present a new model-specific algorithm
for NAMs that generates provably cardinally-minimal explanations using only a
logarithmic number of verification queries
  in the number of input features, after a parallelized preprocessing step with
logarithmic runtime in the required precision is applied to each small
univariate NAM component.
  Our algorithm not only makes the task of obtaining cardinally-minimal
explanations feasible, but even outperforms existing algorithms designed to
find the relaxed variant of subset-minimal explanations - which may be larger
and less informative but easier to compute - despite our algorithm solving a
much more difficult task.
  Our experiments demonstrate that, compared to previous algorithms, our
approach provides provably smaller explanations than existing works and
substantially reduces the computation time. Moreover, we show that our
generated provable explanations offer benefits that are unattainable by
standard sampling-based techniques typically used to interpret NAMs.

## One-Sentence Claim

For Neural Additive Models, provably cardinally-minimal sufficient explanations can be generated efficiently with logarithmically many verification queries after parallel preprocessing.

## Problem

Many post-hoc explanations are heuristic and lack guarantees. Provably sufficient minimal feature subsets are attractive, but for standard neural networks they can require exponentially many NP-hard verification queries, making strong guarantees impractical.

## Core Contribution

The paper gives a model-specific algorithm for NAMs that efficiently computes cardinally-minimal explanations with provable guarantees. It solves a stronger explanation problem than subset-minimal methods while reportedly producing smaller explanations faster.

## Method

The algorithm exploits the additive structure of NAMs. After parallel preprocessing each univariate component with logarithmic runtime in the required precision, it uses only logarithmically many verification queries in the number of input features to identify a cardinally-minimal sufficient subset.

## Experiments and Evidence

The abstract reports that the method produces provably smaller explanations than previous algorithms, substantially reduces computation time, and offers benefits unavailable to standard sampling-based NAM interpretation methods.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect the exact NAM assumptions, verification oracle, precision dependence, feature interactions excluded by additivity, and whether explanations remain useful for correlated real-world features. The guarantees may not transfer to non-additive architectures.

## Deep Themes

- Provable interpretability for structured model classes.
- Efficient sufficient explanations.
- Formal verification as explanation infrastructure.
- Model-specific guarantees over generic heuristics.

## Subthemes

- Neural Additive Models.
- Cardinally-minimal explanations.
- Verification queries.
- Parallel preprocessing.
- Sampling-based explanation limits.

## Connections to Other Papers

Connects to interpretability-as-intervention papers such as LVLM saliency diagnostics and persistent homology, and to formal theory papers where structure reduces an otherwise intractable problem.

## Notes for Cross-Paper Synthesis

This paper illustrates a recurring tradeoff: strong guarantees become feasible when the model class is constrained enough. Interpretability may be less about universal explanation methods and more about architectures whose structure makes explanations certifiable.
