# Local Covariate Selection for Average Causal Effect Estimation without Pretreatment and Causal Sufficiency Assumptions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: qZVcGlU5lN
- Authors: Zeyu Liu; Zheng Li; Feng Xie; Yan Zeng; Hao Zhang; Kun Zhang
- Primary area: general_machine_learning->causality
- Keywords: Causal Effect;Covariate Selection;Latent Variables;Local Learning;Causal Discovery
- Source URL: https://openreview.net/forum?id=qZVcGlU5lN
- PDF URL: https://openreview.net/pdf?id=qZVcGlU5lN

## Abstract

Causal effect estimation is a fundamental task in many scientific fields. Selecting appropriate covariates for adjustment is crucial for obtaining unbiased causal effects. However, most existing methods either rely on learning the global causal structure, assume the absence of latent variables, or impose the pretreatment assumption-restricts covariates to those unaffected by the treatment or outcome. These assumptions are often unrealistic in real-world scenarios, and global structure learning can be computationally intensive and inefficient.
To address these challenges, we first characterize the local existence boundary of adjustment sets for causal effect estimation. Based on this characterization, we develop a novel local learning method for covariate selection in nonparametric causal effect estimation. This method accommodates the presence of latent variables and eliminates the need for the pretreatment assumption.
We prove that the proposed method is both sound and complete under standard assumptions. Its effectiveness is validated through extensive experiments on both synthetic and real-world datasets.

## One-Sentence Claim

Average causal effects can be estimated with sound and complete local covariate selection even without pretreatment or causal sufficiency assumptions, avoiding full global causal discovery.

## Problem

Covariate adjustment is central to causal effect estimation, but choosing the right adjustment set is difficult. Many methods assume covariates are pretreatment variables, assume no latent variables, or require learning a global causal graph.

These assumptions are often unrealistic. Real datasets may include post-treatment or outcome-affected variables, hidden confounders, and large causal systems where global structure learning is expensive and fragile.

## Core Contribution

The paper characterizes the local existence boundary of adjustment sets for average causal effect estimation. Based on that characterization, it develops a local learning method for covariate selection in nonparametric causal effect estimation.

The method accommodates latent variables and removes the pretreatment assumption. The authors prove soundness and completeness under standard assumptions, making the contribution both methodological and identification-theoretic.

## Method

Instead of reconstructing the entire causal graph, the method focuses on local structure relevant to the treatment, outcome, and candidate covariates. The local existence-boundary characterization determines when a valid adjustment set exists.

The covariate-selection procedure then searches locally for adjustment variables sufficient for unbiased effect estimation, even in the presence of latent variables and variables that may not satisfy pretreatment restrictions.

## Experiments and Evidence

The abstract reports soundness and completeness proofs plus extensive validation on synthetic and real-world datasets. The empirical claim is that local selection is effective without global discovery or strong no-latent-variable assumptions.

Full-paper reading should inspect the precise standard assumptions, oracle tests or conditional-independence procedures used, robustness to finite-sample errors, and the real-world datasets.

## Limits and Failure Modes

Soundness and completeness depend on assumptions that may fail in practice, such as faithfulness-like conditions or reliable local independence tests. Latent variables are accommodated, but not arbitrary causal ambiguity.

Local methods can be more efficient than global discovery, but they may still be sensitive to finite-sample statistical errors near the treatment/outcome neighborhood.

## Deep Themes

- Local causal identification: effect estimation need not require full graph recovery.
- Relaxing pretreatment assumptions: valid adjustment can be characterized more generally.
- Hidden-variable-aware covariate selection: causal methods are moving beyond causal sufficiency.
- Sound-complete procedures: the paper prioritizes exact identification guarantees over heuristic adjustment.

## Subthemes

- Adjustment-set existence has a local boundary.
- Nonparametric causal effect estimation benefits from structural covariate selection.
- Global causal discovery can be unnecessary overhead.
- Realistic causal workflows must allow latent variables.

## Connections to Other Papers

This paper connects to evolutionary selection causal modeling and other identification papers through sound/complete causal criteria. It also relates to feasible payoff set estimation: both infer latent structural constraints from partial observations.

It fits the broader theme of replacing brittle global modeling with local structure sufficient for the downstream decision.

## Notes for Cross-Paper Synthesis

The synthesis point is local sufficiency. Several papers avoid solving a full impossible problem by identifying the smaller structure needed for the target quantity: adjustment sets, payoff sets, or relevant feature manifolds.
