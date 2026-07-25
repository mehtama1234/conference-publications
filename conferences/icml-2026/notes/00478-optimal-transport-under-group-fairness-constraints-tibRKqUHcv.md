# Optimal Transport under Group Fairness Constraints

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: tibRKqUHcv
- Authors: Linus Bleistein; Mathieu Dagréou; Francisco Andrade; Thomas Boudou; Aurélien Bellet
- Primary area: social_aspects->fairness
- Keywords: Optimal transport;group fairness;matching
- Source URL: https://openreview.net/forum?id=tibRKqUHcv
- PDF URL: https://openreview.net/pdf?id=tibRKqUHcv

## Abstract

Ensuring fairness in matching algorithms is a key challenge in allocating scarce resources and positions. Focusing on Optimal Transport (OT), we introduce a novel notion of group fairness requiring that the probability of matching two individuals from any two given groups in the OT plan satisfies a predefined target. We first propose a modified Sinkhorn algorithm to compute perfectly fair transport plans efficiently. Since exact fairness can significantly degrade matching quality in practice, we then develop two relaxation strategies. The first one involves solving a penalized OT problem, for which we derive novel finite-sample complexity guarantees. Our second strategy leverages bilevel optimization to learn a ground cost that induces a fair OT solution, and we establish a bound on the deviation of fairness when matching unseen data. Finally, we present empirical results illustrating the performance of our approaches and the trade-off between fairness and transport cost.

## One-Sentence Claim

Group-fair optimal transport can be enforced or relaxed by constraining group-pair matching probabilities, with efficient fair Sinkhorn computation, penalized guarantees, and learned costs for unseen data.

## Problem

Optimal transport is widely used for matching and allocation, but unconstrained transport plans can reproduce or amplify unfair group-level allocations. In scarce-resource settings, fairness cannot be an afterthought because the matching plan directly determines who is paired with whom or assigned opportunities.

Exact fairness targets may also degrade matching quality, so practical methods need a way to trace the cost-fairness tradeoff rather than only impose hard constraints.

## Core Contribution

The paper introduces a group fairness notion for OT: the probability of matching individuals from any pair of groups in the transport plan should satisfy a predefined target.

It proposes a modified Sinkhorn algorithm for perfectly fair transport, a penalized OT relaxation with finite-sample complexity guarantees, and a bilevel method that learns a ground cost inducing fair OT on unseen data with a bound on fairness deviation.

## Method

The exact method modifies Sinkhorn-style computation to enforce group-pair constraints in the transport plan. This provides efficient computation when perfect fairness is required.

The first relaxation adds a fairness penalty to the OT objective, allowing transport quality and fairness to trade off. The second learns a ground cost through bilevel optimization so that solving OT under that cost yields fairer plans even for future data.

## Experiments and Evidence

The abstract reports empirical results illustrating performance and the tradeoff between fairness and transport cost. Theoretical evidence includes finite-sample complexity for penalized OT and unseen-data fairness-deviation bounds for learned costs.

Full-paper reading should verify fairness target definitions, group-pair constraints, sample complexity dependencies, datasets, and how cost-fairness tradeoff curves are evaluated.

## Limits and Failure Modes

Group-level targets require normative choices about which matching proportions are fair. The framework enforces declared targets, but it does not determine them.

Fairness constraints can reduce matching quality, and learned costs may generalize poorly if deployment populations shift. Intersectional or continuous sensitive attributes may require richer formulations.

## Deep Themes

- Fairness as transport-plan constraint: fairness is imposed directly on allocation probabilities.
- Cost-fairness Pareto reasoning: exact fairness may be too expensive, so relaxations expose tradeoffs.
- Learning fair costs: fairness can be encoded into the ground metric used by downstream OT.
- Finite-sample fairness guarantees: fairness claims must generalize beyond observed matching data.

## Subthemes

- Group-pair probabilities are the basic fairness unit.
- Sinkhorn algorithms can be modified for fairness constraints.
- Penalized OT gives tunable relaxation.
- Bilevel cost learning targets unseen-data fairness.

## Connections to Other Papers

This paper connects to Fair Posthoc Control, adaptive social bias, and FedARC through fairness under distributional or structural constraints. It also links to Wasserstein-flow papers through the optimal-transport geometry.

It complements MORetro* because both explicitly model tradeoffs rather than optimizing a single scalar objective.

## Notes for Cross-Paper Synthesis

The synthesis point is that fairness can be made native to the optimization object. Here it is not a post-hoc metric; it is a constraint on the transport plan itself.
