# Rare Event Analysis of Large Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 2RJN5vDHG0
- Authors: Jake McAllister Dorman; Edward Gillman; Dominic C Rose; Jamie F. Mair; Juan P. Garrahan
- Primary area: deep_learning->large_language_models
- Keywords: Large Language Models;LLMs;Large Deviation Theory;Rare Events;Monte Carlo;MCMC;AI safety;safety;readability
- Source URL: https://openreview.net/forum?id=2RJN5vDHG0
- PDF URL: https://openreview.net/pdf?id=2RJN5vDHG0

## Abstract

Being probabilistic models, during inference large language models (LLMs) display *rare events*: behaviour that is far from typical but highly significant. By definition all rare events are hard to see, but the enormous scale of LLM usage means that events completely unobserved during development are likely to become prominent in deployment. Here we present an end-to-end framework for the systematic analysis of rare events in LLMs. We provide a practical implementation spanning theory, efficient generation strategies, probability estimation and error analysis, which we illustrate with concrete examples. We outline extensions and applications to other models and contexts, highlighting the generality of the concepts and techniques presented here.

## One-Sentence Claim

Rare Event Analysis provides an end-to-end framework for systematically finding and estimating low-probability but deployment-relevant LLM behaviors.

## Problem

LLM deployment at massive scale makes rare behaviors important, even if they are unobserved during development. Standard sampling may miss these events by definition.

## Core Contribution

The paper adapts rare-event and large-deviation analysis to LLM inference, including generation strategies, probability estimation, and error analysis.

## Method

The framework combines theory with efficient generation and Monte Carlo/MCMC-style estimation to surface and quantify atypical model behaviors.

## Experiments and Evidence

The abstract says the framework is illustrated with concrete examples and is extensible to other models/contexts.

## Full-Text Upgrade

The full text frames rare-event analysis as three linked operations: defining the event, estimating the event probability, and exploring the structure/properties of event samples. This is an important distinction for safety: one can discover a strange behavior, quantify how often it appears under deployment sampling, and then characterize the surrounding behavioral region instead of treating the incident as a one-off anecdote.

The paper uses observables such as automated readability index to show how LLM completions can be biased toward atypical regions, then applies Monte Carlo, Markov Chain Monte Carlo, transition path sampling, and importance-sampling ideas to estimate tail probabilities and errors. The discussion emphasizes that MCMC proposal design, burn-in, correlation between chain samples, and estimator variance are not side details; they determine whether rare-event probability estimates are credible enough for deployment decisions.

## Limits and Failure Modes

Limits to watch: the framework inherits the hard parts of rare-event simulation, including proposal choice, chain mixing, high autocorrelation, long-context cost, and the need for a well-specified observable. For safety use, the most important unsolved layer may be event definition: the statistical machinery is only as useful as the behavioral property being measured.

## Deep Themes

- Safety evaluation must account for tail behavior, not only average behavior.
- Deployment scale changes which probabilities matter.
- Statistical physics/large-deviation tools are entering LLM analysis.

## Subthemes

- Rare events.
- Large deviation theory.
- Monte Carlo estimation.
- LLM safety.
- Tail-risk evaluation.

## Connections to Other Papers

Connects to SandboxEscapeBench, Invisible Safety Threat, and RAGEN-2 through safety-relevant behaviors that ordinary metrics can miss.

## Notes for Cross-Paper Synthesis

This paper adds a field-level theme: as LLMs scale in deployment, evaluation must shift from typical-case performance to tail-risk discovery and probability estimation.
