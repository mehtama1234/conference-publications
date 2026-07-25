# DecodeShare: Tracing the Shared Subspace of LLM Decode-Time Decisions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: txdOohIkYJ
- Authors: Zishan Shao; Lixun Zhang; Kangning Cui; Yixiao Wang; Ting Jiang; Hancheng Ye; Qinsi Wang; Zhixu Du; Yuzhe Fu; Fan Yang; Danyang Zhuo; Yiran Chen; Hai Helen Li
- Primary area: deep_learning->large_language_models
- Keywords: large language models;KV-cached decoding;activation steering;decode-time representations;shared subspace;prefill-decode mismatch;causal intervention
- Source URL: https://openreview.net/forum?id=txdOohIkYJ
- PDF URL: https://openreview.net/pdf?id=txdOohIkYJ

## Abstract

Large language models (LLMs) handle many tasks with one set of parameters, but under KV-cached inference it is unclear what task-general structure, if any, is used at $\textit{decode time}$ rather than during $\textit{prefill}$. We propose $\textbf{DecodeShare}$, a protocol that identifies a low-dimensional subspace consistently shared across tasks in decode-time hidden states, and then tests its causal role by removing that subspace only during decoding. In our experiments, disturbing the discovered shared subspace degrades decision performance far more than disturbing either a prefill-derived or random subspace under the same intervention budget. We further show this decode-shared subspace has practical consequences for activation steering: common steering directions can overlap the task-general decode channel. Projecting out this shared subspace directly separates the functional roles of the two components, while evaluating steering vectors at decode-time yields more reliable signal for downstream deployment than prefill-based proxies. Despite its compactness, the shared subspace can serve as a high-leverage causal channel at decode time. Code is available at: https://github.com/Zishan-Shao/decodeshare.git.

## One-Sentence Claim

DecodeShare identifies a compact task-general hidden-state subspace used during KV-cached decoding, showing that decode-time representations are causal for decisions and more reliable for steering analysis than prefill proxies.

## Problem

LLMs use one parameter set for many tasks, but under KV-cached inference it is unclear which shared structures operate during decoding rather than prefill. Many interpretability and steering analyses rely on prefill-derived signals, which may not reflect the representations that drive token-by-token decisions.

The paper targets this prefill-decode mismatch and asks whether there is a low-dimensional subspace shared across tasks specifically at decode time.

## Core Contribution

DecodeShare is a protocol for identifying a low-dimensional subspace consistently shared across tasks in decode-time hidden states. The paper then tests causality by removing that subspace only during decoding.

The core finding is that disturbing the decode-shared subspace degrades decision performance more than disturbing prefill-derived or random subspaces under the same intervention budget. It also shows that activation-steering directions can overlap this task-general decode channel.

## Method

The method collects decode-time hidden states across tasks and identifies a shared low-dimensional subspace. It performs causal intervention by projecting out or disturbing that subspace during decoding while controlling intervention budget.

For steering analysis, the method compares prefill-derived and decode-time signals and separates common steering directions from the shared decode subspace by projection.

## Experiments and Evidence

The abstract reports stronger performance degradation when removing the discovered decode-time shared subspace than when removing prefill-derived or random subspaces. It also reports practical implications for activation steering, including more reliable signal when steering vectors are evaluated at decode time.

Full-paper reading should verify task suite, dimensionality selection, intervention controls, model families, and whether the shared subspace is stable across prompts and decoding settings.

## Limits and Failure Modes

Low-dimensional shared subspaces may depend on the selected task set and model family. A subspace that is task-general within one evaluation suite may not generalize to unrelated domains or long conversations.

Projecting out shared directions can affect multiple functions at once, making causal interpretation subtle. The subspace may be necessary for decision performance but not semantically uniform.

## Deep Themes

- Decode-time interpretability: the decisive representation may emerge during cached generation rather than prompt processing.
- Shared subspaces as causal channels: compact latent directions can carry task-general decision information.
- Prefill-decode mismatch: analysis based on prompt-time states may mislead deployment-time steering.
- Steering vector disentanglement: task-general channels can overlap with intervention directions.

## Subthemes

- KV-cached inference creates distinct computational phases.
- Causal removal tests are stronger than correlation with hidden states.
- Projection can separate steering components with different roles.
- Compact subspaces can have high leverage over output decisions.

## Connections to Other Papers

DecodeShare connects to Assistant Axis, activation steering, Prompt Steering Replacement, and LatentMAS through internal representation control. It also relates to PoLar and DHSA because all intervene at inference time rather than changing base weights.

It complements MAP and MiniAppBench by emphasizing that deployment-time behavior depends on the actual inference protocol.

## Notes for Cross-Paper Synthesis

The synthesis point is that interpretability must follow runtime. For LLMs, decode-time causal channels may matter more for deployed behavior than prefill-time summaries.
