# Welfare-Optimal Classification with Accuracy Auctions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: MA1LUDNA3s
- Authors: Bana Sadi; Eden Saig; Nir Rosenfeld
- Primary area: theory->game_theory
- Keywords: accuracy auctions;welfare maximization
- Source URL: https://openreview.net/forum?id=MA1LUDNA3s
- PDF URL: https://openreview.net/pdf?id=MA1LUDNA3s

## Abstract

Prediction algorithms are increasingly used to inform decisions about humans, but maximizing accuracy—the standard learning objective—is not necessarily optimal for this purpose. Instead, we propose optimizing social welfare, defined as the average gain users receive from correct predictions. Welfare enables to express, and therefore account for, heterogeneity in how much users benefit from accuracy. But since these valuations are private and users can benefit from overreporting them, learning must simultaneously elicit truthful values and optimize welfare with respect to them. To this end, we propose a novel learning algorithm that incorporates a truthful auction. We show how to compute allocations and prices efficiently, and bound the number of paying users—which surprisingly is independent of the sample size. We conclude with experiments on real and synthetic data that demonstrate our algorithm and explore the connections between welfare and accuracy.

## One-Sentence Claim

The paper replaces accuracy maximization with welfare-optimal classification by using truthful auctions to elicit users' private values for correct predictions.

## Problem

Prediction systems affecting humans optimize average accuracy, but users benefit unequally from correct predictions and may strategically misreport those private values if welfare is used.

## Core Contribution

The paper proposes a learning algorithm with a truthful auction that jointly elicits valuations, optimizes welfare, computes allocations/prices efficiently, and bounds the number of paying users independently of sample size.

## Method

The algorithm treats correct-prediction value as private user information, designs an auction mechanism for truthful reporting, and optimizes classification decisions according to social welfare rather than uniform accuracy.

## Experiments and Evidence

The abstract reports experiments on real and synthetic data demonstrating the algorithm and exploring welfare-accuracy relationships.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: valuation model, incentive-compatibility assumptions, fairness implications, pricing mechanics, budget balance, and applicability when users cannot pay or valuations are socially sensitive.

## Deep Themes

- Accuracy is not the same as social utility.
- ML decisions over humans require incentive-aware preference elicitation.
- Welfare objectives expose heterogeneity hidden by average metrics.

## Subthemes

- Game theory.
- Accuracy auctions.
- Welfare maximization.
- Strategic reporting.
- Human-centered classification.
- Allocations and prices.

## Connections to Other Papers

Connects to evaluation and alignment papers that question raw accuracy as the correct objective, and to preference/feedback work where user values must be elicited rather than assumed.

## Notes for Cross-Paper Synthesis

This paper broadens the evaluation-objective theme: what counts as good prediction depends on whose utility is affected and whether values can be truthfully elicited.
