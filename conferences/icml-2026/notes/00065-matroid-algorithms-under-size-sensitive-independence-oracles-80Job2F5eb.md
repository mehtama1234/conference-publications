# Matroid Algorithms Under Size-Sensitive Independence Oracles

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 80Job2F5eb
- Authors: Kiarash Banihashem; MohammadTaghi Hajiaghayi; Mahdi JafariRaviz; Danny Mittal
- Primary area: optimization->discrete_and_combinatorial_optimization
- Keywords: Matroid Theory;Oracle Models;Approximation Algorithms
- Source URL: https://openreview.net/forum?id=80Job2F5eb
- PDF URL: https://openreview.net/pdf?id=80Job2F5eb

## Abstract

The standard oracle model for matroid algorithms assumes that each independence query can be answered in constant time, regardless of the size of the queried set. While this abstraction has underpinned much of the theoretical progress in matroid optimization, it masks the true computational effort required by these algorithms. In particular, for natural and widely studied classes such as graphic matroids, even a single independence query can require work linear in the size of the set, making the constant-time assumption implausible. We address this gap by introducing a size-sensitive cost model where the cost of a query $Q$ scales with $|Q|$. Nearly linear-time oracle implementations exist for broad families of matroids, and this refined abstraction therefore captures the true cost of query evaluation while allowing for a more faithful comparison between general matroids and their natural special cases. Within this framework we study three fundamental algorithmic tasks: finding a basis of a matroid, approximating its rank, and approximating its partition size. We establish tight results, proving nearly matching upper and lower bounds that show the optimal query cost is (up to logarithmic factors) quadratic in the size of the matroid. On the algorithmic side, our upper bounds are realized by explicit procedures that construct the desired solution. On the complexity side, our lower bounds are unconditional and already hold even for weaker distinguishing formulations of the problems. Finally, for matroids with maximum circuit size at most $c$, we show that the quadratic barrier can be broken, providing an algorithm that calculates the maximum-weight basis with expected query cost $\mathcal{O}(n^{2-1/c} \log n)$.

## One-Sentence Claim

Matroid algorithm complexity changes under size-sensitive independence oracles: fundamental tasks have nearly quadratic optimal query cost unless structural restrictions such as bounded circuit size apply.

## Problem

The standard matroid oracle model treats every independence query as constant cost, hiding the real work needed for natural matroids where checking a large queried set can take time proportional to its size.

## Core Contribution

The paper introduces a size-sensitive query-cost model and proves nearly matching upper and lower bounds for basis finding, rank approximation, and partition-size approximation, plus faster algorithms for bounded-circuit matroids.

## Method

The model charges each independence query by the size of the queried set. The paper proves unconditional lower bounds via hard matroid constructions and gives explicit algorithms whose total size-sensitive query cost nearly matches the bounds.

## Experiments and Evidence

The abstract reports tight results: optimal query cost is quadratic up to logarithmic factors for general matroids, while maximum-weight basis can be computed with expected query cost O(n^(2-1/c) log n) when maximum circuit size is at most c.

## Full-Text Upgrade

The full text motivates the model through graphic matroids, where independence corresponds to acyclicity and query checking is not plausibly constant time. It formalizes a size-sensitive independence oracle where query Q costs |Q|, making oracle complexity closer to actual runtime for broad matroid families with near-linear query implementations.

The paper separates rank estimation, basis finding, and partition-size computation. Lower bounds show that even approximate rank and weak distinguishing variants of partition size require quadratic total query cost. On the positive side, partition size can be computed in roughly quadratic query cost, and bounded-circumference matroids allow subquadratic expected query cost for maximum-weight basis via random sampling and fundamental-circuit elimination.

## Limits and Failure Modes

Limits to watch: the model is still stateless and abstracts away dynamic oracle implementations; lower bounds apply to the chosen size-sensitive model; and practical gains depend on whether real matroid oracles match the assumed linear-size query cost.

## Deep Themes

- Theoretical models should account for hidden computational costs.
- Oracle abstractions can overstate algorithmic efficiency.
- Structural restrictions can break otherwise fundamental complexity barriers.

## Subthemes

- Matroid optimization.
- Independence oracles.
- Size-sensitive query cost.
- Rank approximation.
- Partition size.
- Bounded circuit size.

## Connections to Other Papers

Connects to theory papers that revise classical abstractions for realistic computation, including language-generation feasibility and optimization-cost analyses.

## Notes for Cross-Paper Synthesis

This paper adds a modeling-assumption theme: when an abstraction hides the real cost driver, the right complexity theory changes.
