# Causal Structure Learning in Hawkes Processes with Complex Latent Confounder Networks

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: mA78uXqcnl
- Authors: Songyao Jin; Biwei Huang
- Primary area: causal reasoning
- Keywords: Hawkes processes;causal discovery;latent subprocess model;structure learning;time series
- Source URL: https://openreview.net/forum?id=mA78uXqcnl
- PDF URL: https://openreview.net/pdf?id=mA78uXqcnl

## Abstract

Multivariate Hawkes process provides a powerful framework for modeling temporal dependencies and event-driven interactions in complex systems. While existing methods primarily focus on uncovering causal structures among observed subprocesses, real-world systems are often only partially observed, with latent subprocesses posing significant challenges. In this paper, we show that continuous-time event sequences can be represented by a discrete-time causal model as the time interval shrinks, and we leverage this insight to establish necessary and sufficient conditions for identifying latent subprocesses and the causal influences. Accordingly, we propose a two-phase iterative algorithm that alternates between inferring causal relationships among discovered subprocesses and uncovering new latent subprocesses, guided by path-based conditions that guarantee identifiability. Experiments on both synthetic and real-world datasets show that our method effectively recovers causal structures despite the presence of latent subprocesses.

## One-Sentence Claim

The paper identifies latent subprocesses and causal influences in partially observed Hawkes processes by connecting continuous-time event sequences to limiting discrete-time causal models.

## Problem

Multivariate Hawkes processes model temporal event interactions, but real systems are often only partially observed. Latent subprocesses can confound apparent dependencies among observed events, making causal structure learning unreliable if hidden event sources are ignored.

## Core Contribution

The paper establishes necessary and sufficient identifiability conditions for latent subprocesses and causal influences in Hawkes processes, then proposes a two-phase iterative algorithm for discovering both observed causal relationships and new latent subprocesses.

## Method

The method uses the insight that continuous-time event sequences can be represented by a discrete-time causal model as the interval shrinks. It alternates between causal relationship inference among discovered subprocesses and latent subprocess discovery, guided by path-based identifiability conditions.

## Experiments and Evidence

Synthetic and real-world experiments reportedly show that the method recovers causal structures despite latent subprocesses. The theoretical evidence is the necessary/sufficient identifiability analysis.

## Limits and Failure Modes

Identifiability may depend on assumptions about event resolution, path conditions, stationarity, excitation kernels, and the latent network class. Real-world event logs may have missingness, censoring, or aggregation that violates those assumptions. Full-text review should check the exact discrete-time limit, latent-subprocess conditions, algorithm convergence, and real-data ground truth.

## Deep Themes

- Causal discovery under latent temporal confounding.
- Hawkes processes as event-causal models.
- Discrete-time limits for continuous-time identification.
- Iterative latent structure discovery.

## Subthemes

- Latent subprocess models.
- Path-based identifiability.
- Temporal point process causality.
- Partial observability.
- Structure learning in event streams.

## Connections to Other Papers

Connects to the Hawkes representer theorem paper through efficient/theoretical Hawkes modeling, to causal discovery papers, and to broader uncertainty/latent-variable themes where hidden causes must be explicitly modeled rather than absorbed into observed correlations.

## Notes for Cross-Paper Synthesis

This paper adds a causal version of the hidden-structure theme: event data are not enough unless the method can infer which unobserved subprocesses explain observed temporal dependencies.
