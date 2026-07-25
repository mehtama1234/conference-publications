# Information Flow Reveals When to Trust Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: vd8HzoFZ7v
- Authors: Rui Xu; Yi Chen; Jiujiu Chen; Sihong Xie
- Primary area: deep_learning->large_language_models
- Keywords: uncertainty quantification;retrieval-augmented generation
- Source URL: https://openreview.net/forum?id=vd8HzoFZ7v
- PDF URL: https://openreview.net/pdf?id=vd8HzoFZ7v

## Abstract

In retrieval-augmented generation, language models can generate incorrect responses if they fail to utilize query-relevant content from the retrieved evidence. This shifts the focus of uncertainty quantification (UQ) toward assessing contextual grounding, i.e., whether predictions are supported by query-relevant tokens. Recent UQ methods unpack language models to characterize how inputs are processed. Nevertheless, these methods focus on a few layers and overlook the whole progressive propagation within the model, thereby failing to fully capture the grounding dynamics essential for reliable uncertainty estimation. We use information flow to build a layer-wise trace that reveals each context token’s contribution to the output, providing an interpretable basis for assessing reliability. From this analysis, we introduce two measures to calibrate prediction confidence. The first, \textit{simulatability}, posits that a prediction is more likely to be correct when context token contributions align closely with their true relevance. The second, \textit{concentration}, asserts that a response is more likely to be correct when it is derived from a narrow, focused subset of tokens. Experiments show that our method achieves an average AUROC of 0.709, exceeding the runner-up performance of 0.676, while maintaining moderate computational cost.

## One-Sentence Claim

Layer-wise information flow through context tokens reveals whether RAG answers are grounded, enabling confidence calibration via simulatability and concentration.

## Problem

Retrieval-augmented generation can fail even when relevant evidence is retrieved, because the model may not use the query-relevant content when generating its answer. Uncertainty quantification therefore needs to assess contextual grounding, not only output probability or verbal confidence.

Recent methods inspect internal processing but often focus on a few layers, missing progressive propagation of evidence through the model.

## Core Contribution

The paper uses information flow to trace each context token's contribution to the output across layers. This gives an interpretable basis for judging whether the answer is supported by relevant evidence.

It introduces two confidence measures: simulatability, where correctness is more likely when token contributions align with true relevance, and concentration, where correctness is more likely when the response draws from a narrow focused token subset.

## Method

The method builds a layer-wise contribution trace from input context tokens to the generated output. The trace is compared with query-relevance information to determine whether grounding is plausible.

Simulatability measures alignment between contribution and true relevance. Concentration measures how focused the contributing evidence is. These measures calibrate prediction confidence for RAG.

## Experiments and Evidence

The abstract reports average AUROC 0.709, exceeding runner-up 0.676, with moderate computational cost. This indicates better discrimination between correct and incorrect RAG predictions.

Full-paper reading should verify datasets, relevance labels, information-flow computation, layer aggregation, baseline methods, and whether concentration fails on questions requiring broad evidence synthesis.

## Limits and Failure Modes

The method depends on reliable relevance labels or proxies for simulatability. Some correct answers require dispersed evidence, so high concentration may not always mean reliability.

Information-flow attributions can be model- and architecture-dependent. Better AUROC helps calibration, but the method does not itself force the model to use evidence.

## Deep Themes

- Grounding as internal evidence flow: trust depends on whether relevant tokens causally contribute.
- Layer-wise UQ: reliability signals emerge across propagation, not one layer snapshot.
- Simulatability and concentration: two interpretable axes for RAG confidence.
- Retrieval is not enough: evidence must be used, not merely present.

## Subthemes

- Context token attribution supports uncertainty estimation.
- Focused evidence often indicates stronger grounding.
- Broad evidence tasks may complicate concentration heuristics.
- Moderate cost matters for practical RAG monitoring.

## Connections to Other Papers

This paper connects to DecodeShare, Assistant Axis, and temporal graph memory explainability through runtime internal traces. It also relates to hallucination rate-distortion: external retrieval can change the memory problem, but only if information flow reaches the output.

It fits the interpretability-as-intervention theme, even though the present method is mainly diagnostic.

## Notes for Cross-Paper Synthesis

The synthesis point is that trust in LLMs is becoming process-based. A correct-looking RAG answer is less trustworthy if the model's internal flow ignored the relevant evidence.
