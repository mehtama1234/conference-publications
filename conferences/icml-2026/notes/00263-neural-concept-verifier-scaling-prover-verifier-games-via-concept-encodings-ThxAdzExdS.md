# Neural Concept Verifier: Scaling Prover-Verifier Games via Concept Encodings

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ThxAdzExdS
- Authors: Berkant Turan; Suhrab Asadulla; David Steinmann; Kristian Kersting; Wolfgang Stammer; Sebastian Pokutta
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: Interpretability;Prover-Verifier Games;Concept Bottleneck Models;Concept Explanation;XAI
- Source URL: https://openreview.net/forum?id=ThxAdzExdS
- PDF URL: https://openreview.net/pdf?id=ThxAdzExdS

## Abstract

While *Prover-Verifier Games* (PVGs) offer a promising path toward verifiability in nonlinear classification models, they have not yet been applied to complex inputs such as high-dimensional images. 
Conversely, expressive *concept encodings* effectively allow to translate such data into interpretable concepts but are often utilised in the context of low-capacity linear predictors.
In this work, we push towards real-world verifiability by combining the strengths of both approaches. We introduce *Neural Concept Verifier (NCV)*, a unified framework combining PVGs for formal verifiability with concept encodings to handle complex, high-dimensional inputs in an interpretable way. NCV achieves this by utilizing recent minimally supervised concept discovery models to extract structured concept encodings from raw inputs. A *prover* then selects a subset of these encodings, which a *verifier*, implemented as a nonlinear predictor, uses exclusively for decision-making.
Our evaluations show that NCV outperforms classic concept-based models and pixel-based PVG classifier baselines on high-dimensional, logically complex datasets and helps mitigate shortcut behavior. Overall, we demonstrate NCV as a promising step toward concept-level, verifiable AI.

## One-Sentence Claim

Neural Concept Verifier scales prover-verifier games to high-dimensional images by translating raw inputs into structured concept encodings and letting a prover expose only selected concepts to a nonlinear verifier.

## Problem

Prover-verifier games offer a route to verifiable model decisions, but they have not been broadly applied to complex image inputs. Concept encodings can make images interpretable, but they are often paired with low-capacity linear predictors that struggle on logically complex tasks.

The paper asks how to combine formal verifiability with expressive prediction on high-dimensional data.

## Core Contribution

The paper introduces Neural Concept Verifier, a framework that joins concept discovery with prover-verifier games. Minimally supervised concept discovery models extract structured concept encodings from raw inputs. A prover selects a subset of those concepts, and a nonlinear verifier must make decisions using only the selected concept information.

This design aims to preserve interpretability and verifiability while retaining enough predictive capacity for complex image tasks.

## Method

NCV has three conceptual stages:

- Extract concept encodings from high-dimensional inputs.
- Let the prover choose a subset of encodings as the explanation/evidence channel.
- Let a nonlinear verifier classify using only that subset.

The prover-verifier structure pressures the evidence channel to be sufficient and checkable, while concept encodings make the evidence human-meaningful.

## Experiments and Evidence

Evidence reported in the abstract:

- Evaluation on high-dimensional, logically complex datasets.
- NCV outperforms classic concept-based models.
- NCV outperforms pixel-based prover-verifier classifier baselines.
- The framework helps mitigate shortcut behavior.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: concept discovery method, verifier capacity, game objective, datasets, shortcut metrics, and human concept quality.

## Limits and Failure Modes

- Verifiability depends on the quality and completeness of discovered concepts.
- A nonlinear verifier can reintroduce opacity even when its inputs are concept-level.
- A strategic prover may select concepts that are predictive but not causally faithful unless the game objective prevents this.
- Scaling to open-world images may require stronger concept discovery than benchmark settings provide.

## Deep Themes

**Interpretability needs an evidence protocol.** NCV does not just expose concepts; it structures a game where selected concepts become the verifier's exclusive evidence.

**Concept bottlenecks are becoming more expressive.** The paper moves beyond linear concept predictors toward nonlinear verification over concept encodings.

**Shortcut mitigation can be cast as constrained evidence selection.** If decisions must pass through selected concepts, shortcuts can become easier to detect or suppress.

## Subthemes

- Prover-verifier games for high-dimensional data.
- Minimally supervised concept discovery.
- Nonlinear concept-level verification.
- Selective evidence channels.
- Concept bottlenecks for shortcut mitigation.

## Connections to Other Papers

Connects to visual MI, Neuron-Basis Circuits, DISCO, and DOUBT because all try to expose or constrain the evidence a model uses. It also links to agent and reasoning evaluation papers where process transparency matters as much as final-answer accuracy.

## Notes for Cross-Paper Synthesis

NCV highlights a recurring design move: force decisions through a structured intermediate object, such as concepts, memories, tables, value modules, or causal dependencies, so model behavior can be inspected and controlled.
