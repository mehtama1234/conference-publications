# From Feasible to Practical: Pareto-Optimal Synthesis Planning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: qpPf5mI1qn
- Authors: Friedrich Hastedt; Dongda Zhang; Antonio Del rio chanona
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Retrosynthesis planning;Multi-objective optimization;Pareto optimality;A* search;Computer-aided synthesis planning
- Source URL: https://openreview.net/forum?id=qpPf5mI1qn
- PDF URL: https://openreview.net/pdf?id=qpPf5mI1qn

## Abstract

Current computer-aided synthesis planning (CASP) methods often treat retrosynthesis as solved once a single feasible route is identified, focusing primarily on convergence or shortest-path metrics. This view is misaligned with real-world practice, where chemists must balance competing objectives such as cost, sustainability, toxicity, and overall yield. To address this, we formulate synthesis planning as a multi-objective search problem and introduce MORetro$^\ast$, an algorithm that generates a Pareto front of synthesis routes to explicitly capture trade-offs between user-defined criteria. MORetro$^\ast$ uses weighted scalarization and solution-informed sampling to efficiently navigate the combinatorial search space and prioritize promising trade-offs. Building on multi-objective A$^\ast$-search, we provide optimality guarantees showing that, for a fixed single-step model, MORetro$^\ast$ recovers the true Pareto front under admissibility. Across multiple retrosynthesis benchmarks, MORetro$^\ast$ produces diverse, high-quality Pareto fronts, uncovering solutions overlooked by single-objective approaches and better aligning CASP outputs with industrial decision-making.

## One-Sentence Claim

MORetro* reframes retrosynthesis planning as multi-objective search, generating Pareto fronts of routes that trade off cost, sustainability, toxicity, yield, and other user-defined criteria.

## Problem

Computer-aided synthesis planning often stops once it finds a feasible retrosynthetic route, optimizing convergence or shortest-path metrics. This is misaligned with chemistry practice, where a feasible route may be impractical due to cost, toxicity, low yield, unsustainable reagents, or operational constraints.

Chemists need tradeoff sets, not single routes. A route planner should surface diverse Pareto-optimal alternatives so users can choose according to context-specific priorities.

## Core Contribution

The paper formulates synthesis planning as a multi-objective search problem and introduces MORetro*, an algorithm that generates Pareto fronts of synthesis routes. It uses weighted scalarization and solution-informed sampling to navigate the combinatorial search space efficiently.

Building on multi-objective A* search, the authors provide optimality guarantees: for a fixed single-step model and admissibility conditions, MORetro* recovers the true Pareto front.

## Method

MORetro* treats each synthesis route as a vector of objective values rather than a single score. Weighted scalarization explores different tradeoff directions, while solution-informed sampling prioritizes promising regions of the route space.

The algorithm extends A*-style search to the multi-objective setting, maintaining candidate routes and Pareto dominance relationships so that the output is a frontier of nondominated plans.

## Experiments and Evidence

The abstract reports results across multiple retrosynthesis benchmarks, where MORetro* produces diverse, high-quality Pareto fronts, finds solutions overlooked by single-objective methods, and better matches industrial decision-making.

Full-paper reading should verify objective definitions, admissible heuristics, single-step retrosynthesis model assumptions, runtime, route-validity checks, and expert/industrial relevance of the generated fronts.

## Limits and Failure Modes

The guarantee is conditional on a fixed single-step model and admissibility. If the single-step retrosynthesis model misses reactions or assigns poor feasibility scores, the Pareto front is optimal only relative to that flawed model.

Multi-objective outputs can also be cognitively demanding. A large Pareto front needs good visualization and user preference elicitation to become practically useful.

## Deep Themes

- From feasibility to decision quality: scientific planning should optimize practical tradeoffs, not only find any answer.
- Pareto-front generation: uncertainty and preference diversity are represented as a set of alternatives.
- Search with guarantees in chemical design: A*-style structure brings optimality to learned retrosynthesis planning.
- User-defined objectives: planning systems become configurable to industrial priorities.

## Subthemes

- Cost, sustainability, toxicity, and yield are competing objectives.
- Single-objective planners can hide useful alternatives.
- Solution-informed sampling accelerates combinatorial route search.
- Practical CASP requires decision support, not just route discovery.

## Connections to Other Papers

This paper connects to FIDIA, PAR, and DeCoDe through scientific design and chemistry. It also connects to feasible payoff set estimation because both output sets that preserve tradeoffs or ambiguity rather than collapsing to one solution.

It fits with OPUS and data-selection work around utility-aware optimization: the objective should reflect actual downstream use.

## Notes for Cross-Paper Synthesis

The synthesis point is that "one feasible answer" is often the wrong artifact. In chemistry, games, and causal inference, the useful output may be a frontier or set that supports downstream choice.
