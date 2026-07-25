# RefineStat: Efficient Exploration for Probabilistic Program Synthesis

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: SAl337ZX5d
- Authors: Madhav Kanda; Shubham Ugare; Sasa Misailovic
- Primary area: probabilistic methods (Bayesian methods, variational inference, sampling, UQ, etc.)
- Keywords: Probabilistic Programming;Constrained Generation
- Source URL: https://openreview.net/forum?id=SAl337ZX5d
- PDF URL: https://openreview.net/pdf?id=SAl337ZX5d

## Abstract

Probabilistic programming offers a powerful framework for modeling uncertainty, yet statistical model discovery in this domain entails navigating an immense search space under strict domain‐specific constraints. When small language models are tasked with generating probabilistic programs, they frequently produce outputs that suffer from both syntactic, and semantic errors, such as flawed inference constructs. Motivated by probabilistic programmers’ domain expertise and debugging strategies, we introduce RefineStat, a language model–driven framework that enforces semantic constraints ensuring synthesized programs contain valid distributions, well‐formed parameters, and then applies diagnostic‐aware refinement by resampling prior or likelihood components whenever reliability checks fail. We evaluate RefineStat on multiple probabilistic-programming code-generation tasks using smaller language models (SLMs) and find that it produces programs that are both syntactically sound and statistically reliable, often matching or surpassing those from closed-source large language models (e.g., OpenAI o3).

## One-Sentence Claim

RefineStat improves probabilistic-program synthesis with small language models by enforcing semantic constraints and diagnostic-aware resampling of unreliable prior or likelihood components.

## Problem

Probabilistic programming can express uncertainty-rich statistical models, but discovering valid programs requires searching a huge constrained space.

Small language models often generate programs with syntax errors, invalid distributions, malformed parameters, or flawed inference constructs.

## Core Contribution

The paper introduces RefineStat, an LM-driven framework for probabilistic program synthesis.

It encodes probabilistic-programmer debugging strategies by enforcing semantic constraints and refining specific model components when diagnostics fail.

## Method

RefineStat checks generated probabilistic programs for valid distributions, well-formed parameters, and statistical reliability.

When reliability checks fail, it resamples prior or likelihood components rather than regenerating the entire program, making exploration more targeted and efficient.

## Experiments and Evidence

The abstract reports evaluation across multiple probabilistic-programming code-generation tasks using smaller language models.

RefineStat produces syntactically sound and statistically reliable programs, often matching or surpassing closed-source large models such as OpenAI o3.

## Limits and Failure Modes

Semantic checks can only enforce known constraints. Subtle model misspecification, identifiability issues, or domain-inappropriate priors may remain even when a program passes diagnostics.

Because this note is abstract-only, details still need checking: target probabilistic language, diagnostic tests, resampling strategy, SLM backbones, task set, and statistical reliability metrics.

## Deep Themes

- Constraint-guided code generation: domain semantics can make small models competitive with larger systems.
- Local repair over full regeneration: search improves when failed components are targeted directly.
- Statistical reliability as synthesis objective: probabilistic programs must be valid models, not just executable code.
- Domain expertise as scaffolding: expert debugging strategies become algorithmic constraints.

## Subthemes

- Probabilistic program synthesis.
- Semantic constraints.
- Diagnostic-aware refinement.
- Prior and likelihood resampling.

## Connections to Other Papers

This connects to AlgoVeri, WebDevJudge, HGM, and coding-agent papers through constrained program generation and verification.

It also relates to AstaBench because scientific agents need reliable statistical code, not only plausible text outputs.

## Notes for Cross-Paper Synthesis

RefineStat adds a verification-first programming theme: small models can do hard code synthesis when domain checks and local repair structure the search.
