# Incremental BPE Tokenization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ZbWgrDzCQo
- Authors: Shenghu Jiang; Ruihao Gong
- Primary area: deep_learning->large_language_models
- Keywords: Byte Pair Encoding;Tokenization;Incremental Algorithm;LLM Efficiency;Streaming Inference;Worst-Case Complexity
- Source URL: https://openreview.net/forum?id=ZbWgrDzCQo
- PDF URL: https://openreview.net/pdf?id=ZbWgrDzCQo

## Abstract

We propose a novel algorithm for incremental Byte Pair Encoding (BPE) tokenization.
The algorithm processes each input byte in **worst-case** $\mathcal{O}(\log^2 t)$ time,
leading to an overall complexity of $\mathcal{O}(n \log^2 t)$,
where $n$ is the input length and $t$ is the maximum token length.
The algorithm incrementally maintains BPE tokenization results for every prefix of the input text,
implementing the standard BPE merge procedure defined by a fixed set of merge rules.
This enables efficient partial tokenization in streaming settings.
Functioning as a drop-in replacement for standard BPE,
our approach achieves a speedup of up to ${\sim}3\times$ over Hugging Face's tokenizers,
and demonstrates significant latency reductions over OpenAI's tiktoken on pathological inputs.
We further introduce an eager output algorithm that enables streaming output,
emitting tokens as soon as token boundaries are determined during incremental tokenization.
Overall, our results demonstrate that BPE tokenization can be performed incrementally
with strong worst-case guarantees,
while providing practical latency benefits in modern large language model pipelines.
The source code is available at https://github.com/ModelTC/mtc-inc-bpe.

## One-Sentence Claim

Incremental BPE maintains exact standard BPE tokenization for every input prefix with worst-case logarithmic per-byte updates, enabling low-latency streaming tokenization.

## Problem

BPE tokenization is normally applied to complete strings, but modern LLM systems increasingly process streaming inputs and outputs. Re-tokenizing prefixes or handling pathological inputs can create latency spikes, and practical tokenizers may lack strong worst-case guarantees.

The paper asks whether standard fixed-rule BPE can be performed incrementally while preserving exact merge semantics.

## Core Contribution

The paper proposes an incremental BPE algorithm that processes each input byte in worst-case O(log^2 t) time and O(n log^2 t) total time, where t is maximum token length. It maintains tokenization results for every prefix under the standard BPE merge procedure.

It also introduces an eager output algorithm that emits tokens as soon as token boundaries are determined. The implementation is a drop-in replacement and achieves up to about 3x speedup over Hugging Face tokenizers plus large latency reductions over tiktoken on pathological inputs.

## Method

The algorithm maintains the current BPE merge structure as bytes arrive, updating only the affected local region instead of recomputing tokenization from scratch. Data structures enforce worst-case update bounds relative to the maximum token length.

The eager-output variant tracks when future bytes can no longer alter a token boundary, allowing safe streaming emission.

## Experiments and Evidence

Evidence reported in the abstract:

- Worst-case O(log^2 t) processing per byte.
- Exact maintenance of standard BPE tokenization for every prefix.
- Drop-in replacement behavior.
- Up to roughly 3x speedup over Hugging Face tokenizers.
- Significant latency reduction over tiktoken on pathological inputs.
- Eager streaming output algorithm.
- Code release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: data structures, memory overhead, merge-rule assumptions, Unicode handling, and benchmark inputs.

## Limits and Failure Modes

- Benefits may be largest for streaming/pathological cases rather than ordinary batch tokenization.
- Worst-case bounds depend on maximum token length t.
- Integration with production tokenization libraries may require careful compatibility testing.
- Tokenizers with normalization or special-token preprocessing may complicate exact incremental behavior.

## Deep Themes

**Small preprocessing algorithms shape LLM latency.** Tokenization can be a real bottleneck in streaming systems.

**Exactness and worst-case guarantees matter for infrastructure.** The algorithm preserves BPE semantics while controlling pathological behavior.

**Streaming requires prefix-native computation.** The system maintains valid state after each byte rather than waiting for a full input.

## Subthemes

- Incremental BPE.
- Prefix tokenization maintenance.
- Worst-case tokenizer complexity.
- Eager token emission.
- Streaming LLM inference infrastructure.

## Connections to Other Papers

Connects to WeDLM, ME Ensemble, FlashSinkhorn, FlashOptim, and other efficiency papers through infrastructure-level latency reduction. It also links to test-time control papers because streaming generation changes how systems can intervene during decoding.

## Notes for Cross-Paper Synthesis

Incremental BPE adds an infrastructure detail to the efficiency theme: some bottlenecks are below the model, in the exact algorithms that feed and decode it.
