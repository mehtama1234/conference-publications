# The Tell-Tale Norm: $\ell_2$ Magnitude as a Signal for Reasoning Dynamics in Large Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 03ZTlJuX0y
- Authors: Jinyang Zhang; Hongxin Ding; Yue Fang; Weibin Liao; Muyang Ye; Junfeng Zhao; Yasha Wang
- Primary area: deep_learning->large_language_models
- Keywords: LLM reasoning;reasoning dynamics;LLM interpretability
- Source URL: https://openreview.net/forum?id=03ZTlJuX0y
- PDF URL: https://openreview.net/pdf?id=03ZTlJuX0y

## Abstract

Recent work has sought to understand Large Language Models (LLMs) reasoning, yet a principled, model-intrinsic signal that captures its *layer-wise reasoning dynamics* remains underexplored. We bridge this gap by demonstrating that **the $\ell_2$ norm of hidden states serves as an endogenous signal of the model's reasoning intensity**. Using Sparse Autoencoders (SAEs) as a diagnostic probe, we observe that LLMs' internal reasoning is marked by a sharp increase in reasoning feature activations concentrated in late layers. Motivated by this pattern, we establish a formal link between reasoning intensity and the model's latent geometry and theoretically prove that the $\ell_2$ norm of hidden states bounds the activation strength of SAE reasoning features. Empirical correlation analysis and causal interventions further prove $\ell_2$ norm as a faithful indicator, where heightened norms consistently correspond to critical reasoning steps. We then introduce three test-time scaling techniques guided by $\ell_2$ norms: Adaptive Layer-wise Reasoning Recursion, (ii) Endogenous Reasoning State Steering, and (iii) $\ell_2$-guided Response Selection, which requires no additional training or data and is compatible with advanced inference engines. Experiments across model architectures and benchmarks show that $\ell_2$-norm-based techniques significantly improve reasoning performance, offering a principled yet simple lens to perceive and control LLM latent reasoning dynamics. Our codes are available at https://github.com/zjy1298/The-Tell-Tale-Norm.

## One-Sentence Claim

The L2 norm of LLM hidden states acts as a model-intrinsic signal of reasoning intensity and can guide training-free test-time reasoning improvements.

## Problem

LLM reasoning is hard to observe directly, and existing analyses lack a simple endogenous signal that tracks layer-wise reasoning dynamics and can be used for control.

## Core Contribution

The paper links hidden-state L2 magnitude to reasoning-feature activation, validates it with sparse autoencoders, correlation analysis, and causal interventions, then uses it for three test-time scaling methods.

## Method

Sparse autoencoders diagnose late-layer reasoning-feature activations. Theoretical analysis connects L2 norm to bounds on SAE reasoning feature strength. The resulting signal guides Adaptive Layer-wise Reasoning Recursion, Endogenous Reasoning State Steering, and L2-guided response selection.

## Experiments and Evidence

The abstract claims empirical and causal evidence that higher norms correspond to critical reasoning steps, and that norm-guided techniques improve reasoning across architectures and benchmarks without extra training or data.

## Limits and Failure Modes

PDF checks needed: whether the L2 signal generalizes across model families and token types, whether norm spikes sometimes indicate uncertainty or verbosity rather than reasoning, and whether interventions add meaningful compute overhead.

## Deep Themes

- Interpretability signals are being turned into control knobs.
- Test-time scaling can be guided by endogenous model dynamics.
- Reasoning is increasingly studied as a latent process, not merely output correctness.

## Subthemes

- LLM reasoning dynamics.
- Sparse autoencoder probes.
- Hidden-state geometry.
- Training-free steering.
- Test-time response selection.

## Connections to Other Papers

Connects to RAGEN-2 through reasoning diagnostics, and to activation-steering work through latent interventions at inference time.

## Notes for Cross-Paper Synthesis

This reinforces a cross-conference pattern: internal model measurements are becoming actionable. The paper does not just explain reasoning; it uses the signal to allocate computation and steer outputs.
