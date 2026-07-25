# ICML 2026 Spotlight Batch 092 Synthesis

Papers covered: 00456-00460.

## Batch Thesis

This batch is about replacing point answers with structured decision objects. Feasible payoff estimation returns a set of games consistent with observed behavior; local causal covariate selection finds only the adjustment structure needed for a target effect; embedding translation exposes confidence and composability across vector spaces; MORetro* returns a Pareto front of synthesis routes; and ConFlux reorganizes multivariate time series into unified patch tokens for forecasting.

The common thread is that the output should preserve the structure of downstream uncertainty or choice. A single payoff, covariate list, embedding mapping, synthesis route, or variable ordering is often too brittle unless it is grounded in the relevant geometry, assumptions, or tradeoff frontier.

## Cross-Paper Themes

### 1. Set-Valued Outputs Are More Honest Than Point Estimates

The inverse-game paper estimates feasible payoff sets rather than one payoff matrix. MORetro* produces Pareto fronts rather than one route. Local covariate selection identifies valid adjustment sets under relaxed assumptions.

These papers recognize that when multiple explanations or plans are compatible with the evidence, collapsing to one answer can hide risk. The model should expose the set of viable alternatives or the boundary of identifiability.

### 2. Local Structure Can Replace Global Reconstruction

The causal paper avoids learning a full global graph by characterizing local adjustment-set existence. Embedding translation uses localized HMoE adaptation rather than one global translator. ConFlux reduces cross-variable entanglement by sorting and patching local channel neighborhoods.

The batch supports a broad pattern: solving the full global problem is often unnecessary if the local structure relevant to the task is correctly identified.

### 3. Geometry Governs Interoperability

Embedding translation is explicitly geometric, with error bounds and confidence metrics for OOD, mixing, and chaining. ConFlux imposes a geometry over variables through sorting and patching. Functional ANOVA from the previous batch uses categorical Fourier structure, and JoSE uses an action manifold.

Across these papers, representation layout is not cosmetic. It determines whether translation, forecasting, explanation, or control is stable.

### 4. Practical Scientific Tools Need User-Aligned Objectives

MORetro* moves retrosynthesis from feasible route discovery to industrially relevant tradeoffs like cost, sustainability, toxicity, and yield. ConFlux targets zero-shot and efficient forecasting over diverse public datasets. The causal paper targets effect estimation without unrealistic pretreatment and sufficiency assumptions.

The shared pressure is operational realism: methods are judged by whether they match how scientists, engineers, or analysts actually make decisions.

## Deep Subthemes

### Inverse Game Ambiguity

Observed equilibrium play does not uniquely identify payoffs. Estimating feasible sets gives downstream users a principled uncertainty object for counterfactual analysis and mechanism design.

### Local Causal Sufficiency

Causal effect estimation can sometimes avoid global graph learning. The relevant object is the local boundary of valid adjustment, especially when latent variables and post-treatment covariates are possible.

### Composable Embedding Infrastructure

Embedding translation must support OOD inputs, mixed sources, and chained mappings. This turns embedding alignment into a reliability and infrastructure problem rather than a one-off regression task.

### Pareto Retrosynthesis

Real synthesis planning is multi-objective. Pareto fronts are a more useful artifact than shortest feasible routes because chemists must choose among competing practical constraints.

### Variate Tokenization

ConFlux shows that token design is an inductive bias for structured temporal data. Sorting and patching variables reduce attention complexity while preserving cross-channel signal.

## Common Pattern

The batch's deepest pattern is structure-preserving compression of uncertainty. Whether the object is a game, causal graph, embedding space, synthesis search tree, or multivariate signal, the method keeps the parts of the structure needed for downstream decisions and compresses away the rest.
