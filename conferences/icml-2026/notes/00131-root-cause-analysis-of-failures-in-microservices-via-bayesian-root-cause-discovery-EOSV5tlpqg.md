# Root Cause Analysis of Failures in Microservices via Bayesian Root Cause Discovery

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: EOSV5tlpqg
- Authors: Kenneth Lee; Zihan Zhou; Murat Kocaoglu
- Primary area: general_machine_learning->causality
- Keywords: root cause analysis;causal discovery
- Source URL: https://openreview.net/forum?id=EOSV5tlpqg
- PDF URL: https://openreview.net/pdf?id=EOSV5tlpqg

## Abstract

Modern cloud systems rely on architectures with many interconnected microservices, which enable scalability and flexibility but make troubleshooting failures difficult. Identifying the root cause requires navigating complex dependencies, often beyond the capacity of domain experts. Causal models offer a principled approach to root cause analysis (RCA), but prior methods are typically sample inefficient, as they assume access to the full causal graph or require large numbers of post-failure interventions. We introduce Bayesian Root Cause Discovery (BRCD), which leverages a partial causal structure (a CPDAG learned during the pre-failure period) and performs Bayesian inference without enumerating all DAGs from each interventional Markov equivalence class ($\mathcal{I}$-MEC) for each root cause candidate. Using a recent uniform DAG sampling framework (Wienöbst et al., 2023), BRCD provides the first statistical consistency guarantees for nonparametric RCA, with both identifiability and finite-sample posterior bounds under $\varepsilon$-vanishing approximation. Empirically, across synthetic benchmarks and three microservice systems (Online Boutique, Sockshop, Petshop), BRCD achieves state-of-the-art top-$l$ accuracy while remaining effective in low-failure-sample regimes and scaling to large graphs.

## One-Sentence Claim

Bayesian Root Cause Discovery identifies failure causes in microservice systems by combining pre-failure partial causal structure with Bayesian inference over intervention-equivalence classes.

## Problem

Microservice failures are difficult to troubleshoot because dependencies are complex, while existing causal RCA methods often need full causal graphs or many post-failure interventions.

## Core Contribution

The paper introduces BRCD, a nonparametric Bayesian RCA method with identifiability, finite-sample posterior bounds, and scalability to large microservice graphs.

## Method

BRCD starts from a CPDAG learned before failure, uses uniform DAG sampling to avoid enumerating all DAGs in each interventional Markov equivalence class, and performs Bayesian inference for root-cause candidates.

## Experiments and Evidence

The abstract reports state-of-the-art top-l accuracy on synthetic benchmarks and three microservice systems: Online Boutique, Sockshop, and Petshop, including low-failure-sample regimes.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: CPDAG learning reliability, intervention assumptions, posterior approximation, and deployment observability requirements.

## Deep Themes

- Operational ML systems need causal diagnosis under sparse failure data.
- Pre-failure structure can reduce post-failure intervention burden.
- Root-cause analysis is becoming probabilistic and graph-structural.

## Subthemes

- Microservice RCA.
- Causal discovery.
- Bayesian inference.
- CPDAGs.
- Interventional Markov equivalence.
- Low-sample failure diagnosis.

## Connections to Other Papers

Connects to causal discovery, software reliability, CVE-Factory, and executable operations benchmarks through ML for production system diagnosis.

## Notes for Cross-Paper Synthesis

BRCD adds an operations-causality theme: real systems need causal methods that work with partial graphs and few failure samples.
