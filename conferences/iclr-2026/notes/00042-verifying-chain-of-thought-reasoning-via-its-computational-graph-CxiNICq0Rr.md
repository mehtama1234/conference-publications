# Verifying Chain-of-Thought Reasoning via Its Computational Graph

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: CxiNICq0Rr
- Authors: Zheng Zhao; Yeskendir Koishekenov; Xianjun Yang; Naila Murray; Nicola Cancedda
- Primary area: interpretability and explainable AI
- Keywords: Mechanistic Interpretability;Chain-of-Thought Reasoning;Attribution Graphs
- Source URL: https://openreview.net/forum?id=CxiNICq0Rr
- PDF URL: https://openreview.net/pdf?id=CxiNICq0Rr

## Abstract

Current Chain-of-Thought (CoT) verification methods predict reasoning correctness based on outputs (black-box) or activations (gray-box), but offer limited insight into \textit{why} a computation fails. We introduce a white-box method: \textbf{Circuit-based Reasoning Verification (CRV)}. We hypothesize that attribution graphs of correct CoT steps, viewed as \textit{execution traces} of the model's latent reasoning circuits, possess distinct structural fingerprints from those of incorrect steps. By training a classifier on structural features of these graphs, we show that these traces contain a powerful signal of reasoning errors. Our white-box approach yields novel scientific insights unattainable by other methods. (1) We demonstrate that structural signatures of error are highly predictive, establishing the viability of verifying reasoning directly via its computational graph. (2) We find these signatures to be highly domain-specific, revealing that failures in different reasoning tasks manifest as distinct computational patterns. (3) We provide evidence that these signatures are not merely correlational; by using our analysis to guide targeted interventions on individual transcoder features, we successfully correct the model's faulty reasoning. Our work shows that, by scrutinizing a model's computational process, we can move from simple error detection to a deeper, causal understanding of LLM reasoning.

## One-Sentence Claim

Circuit-based Reasoning Verification detects and can help correct CoT errors by classifying structural fingerprints in attribution graphs of the model's latent reasoning computation.

## Problem

CoT verification methods often use final outputs or activations to predict correctness, but they provide limited insight into why reasoning fails.

The problem is to verify reasoning through the actual computational process rather than treating CoT as only text or activations.

## Core Contribution

The paper introduces CRV, Circuit-based Reasoning Verification, a white-box method using attribution graphs as execution traces of latent reasoning circuits.

It shows that structural graph features distinguish correct from incorrect reasoning steps, that error signatures are domain-specific, and that graph-guided interventions on transcoder features can correct faulty reasoning.

## Method

CRV constructs attribution graphs for CoT steps and extracts structural features from those graphs. A classifier learns to identify reasoning errors from graph structure.

The analysis then uses the error signatures to target interventions on individual transcoder features, testing whether the signatures are causally related to failure.

## Experiments and Evidence

The abstract reports that structural signatures of error are highly predictive.

It also reports domain-specific failure patterns and successful targeted interventions that correct model reasoning, supporting a causal interpretation beyond correlation.

## Limits and Failure Modes

White-box graph methods require access to model internals and attribution/transcoder machinery, which may be expensive or unavailable for closed models.

Because this note is abstract-only, details still need checking: graph construction, feature set, model size, reasoning tasks, classifier protocol, intervention method, and false-positive behavior.

## Deep Themes

- Reasoning verification as circuit analysis: correctness is checked in the computational graph.
- Execution traces for latent reasoning: attribution graphs become process evidence.
- Domain-specific failure mechanisms: errors in different tasks have different computational fingerprints.
- From detection to correction: interpretability becomes intervention.

## Subthemes

- Attribution graph structure.
- CoT step verification.
- Transcoder-feature interventions.
- White-box reasoning diagnostics.

## Connections to Other Papers

This connects to Information Flow, DAVE, transformer association dynamics, and Assistant Axis through internal computation diagnostics.

It also relates to ASAG, PonderLM-2, Ctrl-R, and coverage theory because all focus on reasoning process quality rather than only final answers.

## Notes for Cross-Paper Synthesis

CRV is a strong interpretability-as-intervention example: process-level explanations can become tools for repairing reasoning.
