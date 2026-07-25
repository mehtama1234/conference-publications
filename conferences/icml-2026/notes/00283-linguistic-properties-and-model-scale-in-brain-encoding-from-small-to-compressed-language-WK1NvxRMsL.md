# Linguistic Properties and Model Scale in Brain Encoding: From Small to Compressed Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: WK1NvxRMsL
- Authors: SUBBA REDDY OOTA; Vijay Rowtula; Satya Sai Srinath Namburi GNVV; Khushbu Pahwa; Anant Khandelwal; Manish Gupta; Tanmoy Chakraborty; Bapi Raju Surampudi
- Primary area: applications->neuroscience_cognitive_science
- Keywords: brain encoding;fMRI;light weight language models;larger language models;quantization;linguistic properties;flash-holmes benchmark
- Source URL: https://openreview.net/forum?id=WK1NvxRMsL
- PDF URL: https://openreview.net/pdf?id=WK1NvxRMsL

## Abstract

Recent work has shown that scaling large language models (LLMs) improves their alignment with human brain activity, yet it remains unclear what drives these gains or which representational properties are responsible. Although larger models often yield better task performance and brain alignment, they are  increasingly difficult to analyze mechanistically. This raises a fundamental question: \emph{what is the minimal model capacity required to capture brain-relevant representations?} To address this question, we systematically investigate how constraining model scale and numerical precision affects brain alignment. We compare full-precision LLMs, small language models (SLMs), and compressed variants (quantized and pruned) by predicting fMRI responses during naturalistic language comprehension. Across model families up to 14B parameters, we find that 3B SLMs achieve brain predictivity indistinguishable from larger LLMs, whereas 1B models degrade substantially, particularly in semantic language regions. Brain alignment is remarkably robust to compression: most quantization and pruning methods preserve neural predictivity, with GPTQ as a consistent exception. Linguistic probing reveals a dissociation between task performance and brain predictivity: compression degrades discourse, syntax, and morphology, yet brain predictivity remains largely unchanged.  Overall, brain alignment saturates at modest model scales and is resilient to compression, challenging common assumptions about neural scaling and motivating compact models for brain-aligned language modeling.

## One-Sentence Claim

Brain alignment for language comprehension saturates around 3B-parameter models and is largely robust to quantization and pruning, challenging simple neural-scaling assumptions.

## Problem

Larger language models often predict human brain activity better, but it is unclear whether scale itself drives neural alignment or which linguistic properties matter. Large models are also harder to analyze mechanistically.

The paper asks what minimal model capacity is needed to capture brain-relevant language representations and how compression affects fMRI encoding.

## Core Contribution

The paper systematically compares full-precision LLMs, small language models, and compressed models across families up to 14B parameters. It finds:

- 3B SLMs achieve brain predictivity indistinguishable from larger LLMs.
- 1B models degrade substantially, especially in semantic language regions.
- Brain alignment is robust to most quantization and pruning methods.
- GPTQ is a consistent exception.
- Compression can degrade linguistic probes for discourse, syntax, and morphology while leaving brain predictivity mostly unchanged.

## Method

The method uses brain encoding: model representations are used to predict fMRI responses during naturalistic language comprehension. The authors vary model scale and numerical precision, then compare neural predictivity with linguistic probing performance.

The dissociation between probe degradation and stable fMRI predictivity tests whether benchmark linguistic properties explain brain alignment.

## Experiments and Evidence

Evidence reported in the abstract:

- fMRI response prediction during naturalistic language comprehension.
- Model families up to 14B parameters.
- Comparisons among full-precision, quantized, and pruned variants.
- Brain alignment saturation at 3B parameters.
- Compression robustness except for GPTQ.
- Linguistic probing dissociation from brain predictivity.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: fMRI dataset, encoding model, voxel/ROI analysis, compression settings, and statistical equivalence tests.

## Limits and Failure Modes

- fMRI is spatially and temporally coarse; alignment may miss neural computations at finer resolution.
- Naturalistic language datasets may favor semantic over syntactic properties.
- Saturation at 3B may depend on model family, training data, or encoding pipeline.
- Probe tasks may not measure the linguistic properties actually used by the brain.

## Deep Themes

**Bigger is not always more brain-like.** Neural predictivity can saturate at modest scale.

**Compression can preserve task-relevant representations while harming probes.** Brain alignment and linguistic benchmark performance are separable.

**Mechanistic neuroscience benefits from smaller adequate models.** Compact models may be easier to analyze while retaining brain-relevant structure.

## Subthemes

- fMRI brain encoding.
- Scale saturation around 3B parameters.
- Quantization and pruning resilience.
- Task-performance versus brain-predictivity dissociation.
- Compact brain-aligned language modeling.

## Connections to Other Papers

Connects to SmoothSpike and efficiency papers because representation compression does not necessarily destroy useful function. It also links to interpretability and neuroscience papers such as FacRNN and AI Engram through compact representations of biological or model memory.

## Notes for Cross-Paper Synthesis

This paper adds an important counterweight to scaling narratives: for some alignment targets, the best research object may be the smallest model that preserves the relevant representation.
