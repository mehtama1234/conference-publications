# Balancing Understanding and Generation in Discrete Diffusion Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: pZNo1YWT5x
- Authors: Yue Liu; Yuzhong Zhao; Zheyong Xie; Qixiang Ye; Jianbin Jiao; Yao Hu; Shaosheng Cao; Yunfan Liu
- Primary area: deep_learning->foundation_models
- Keywords: Discrete Diffusion Model;Diffusion Language Model;Language Modeling
- Source URL: https://openreview.net/forum?id=pZNo1YWT5x
- PDF URL: https://openreview.net/pdf?id=pZNo1YWT5x

## Abstract

In discrete generative modeling, two dominant paradigms demonstrate divergent capabilities: Masked Diffusion Language Models (MDLM) excel at semantic understanding and zero-shot generalization, whereas Uniform-noise Diffusion Language Models (UDLM) achieve strong few-step generation quality, yet neither attains balanced performance across both dimensions. To address this, we propose XDLM, which bridges the two paradigms via a stationary noise kernel. XDLM offers two key contributions: it provides (1) a principled theoretical unification of MDLM and UDLM, recovering each paradigm as a special case; and (2) an alleviated memory bottleneck enabled by an algebraic simplification of the posterior probabilities. Experiments demonstrate that XDLM advances the Pareto frontier between understanding capability and generation quality. Quantitatively, XDLM surpasses UDLM by 5.4 points on zero-shot text benchmarks and outperforms MDLM in few-step image generation (FID 54.1 vs. 80.8).  When scaled to tune an 8B-parameter large language model, XDLM achieves 15.0 MBPP in just 32 steps, effectively doubling the baseline performance. Finally, analysis of training dynamics reveals XDLM’s superior potential for long-term scaling. Code is available at [https://github.com/MzeroMiko/XDLM](https://github.com/MzeroMiko/XDLM).

## One-Sentence Claim

XDLM unifies masked and uniform-noise discrete diffusion with a stationary noise kernel, improving the tradeoff between semantic understanding and few-step generation while reducing posterior-memory cost.

## Problem

Discrete diffusion models have split into paradigms with different strengths. Masked diffusion language models perform well on semantic understanding and zero-shot generalization, while uniform-noise diffusion language models produce better few-step generation, but neither balances both dimensions.

The problem is to find a principled diffusion formulation that can recover both approaches as special cases while improving the Pareto frontier between understanding and generation.

## Core Contribution

The paper proposes XDLM, a discrete diffusion model built around a stationary noise kernel. The kernel provides a theoretical unification of MDLM and UDLM and recovers each as a special case.

It also introduces an algebraic simplification of posterior probabilities that alleviates a memory bottleneck. The contribution is therefore both conceptual and practical: unify the noise process and make the resulting model more scalable.

## Method

XDLM uses a stationary noise kernel to bridge masked and uniform-noise diffusion. By changing the kernel setting, the model can emulate the behavior of existing paradigms while occupying intermediate points in the design space.

The posterior simplification reduces memory required for training or inference. This matters because discrete diffusion over vocabularies can create expensive posterior computations, especially when scaling to large language models.

## Experiments and Evidence

The abstract reports that XDLM advances the Pareto frontier between understanding and generation. It beats UDLM by 5.4 points on zero-shot text benchmarks, beats MDLM in few-step image generation with FID 54.1 versus 80.8, and reaches 15.0 MBPP in 32 steps when tuning an 8B-parameter LLM, roughly doubling baseline performance.

It also reports training-dynamics analysis suggesting better long-term scaling potential. Full-paper reading should verify benchmark details, diffusion step counts, compute budgets, text/image setup, and how the 8B tuning experiment is configured.

## Limits and Failure Modes

Balancing understanding and generation may require task-specific kernel choices, and the best Pareto point may vary across text, image, code, and multimodal settings. A unified framework does not guarantee one default configuration dominates all regimes.

Discrete diffusion language models still face adoption challenges relative to autoregressive decoding, including serving stack maturity, sampling latency, and integration with existing inference infrastructure.

## Deep Themes

- Unified diffusion design space: MDLM and UDLM become endpoints of a broader kernel family.
- Understanding-generation Pareto frontier: model design is judged by balanced capability rather than a single metric.
- Algebraic efficiency: theoretical simplification reduces a concrete memory bottleneck.
- Diffusion LLM scaling: discrete diffusion is positioned as a serious large-language-model training and inference paradigm.

## Subthemes

- Stationary noise kernels provide controllable corruption dynamics.
- Few-step generation and zero-shot understanding pull on different design choices.
- Posterior-memory cost is a bottleneck for vocabulary-scale diffusion.
- Code-generation results suggest diffusion language models can compete beyond text likelihood.

## Connections to Other Papers

XDLM connects to JustGRPO and DMPO-style diffusion language model papers through the emerging diffusion-LLM thread. It also relates to TabSwift in this batch as an attempt to find a better accuracy/efficiency/capability tradeoff inside a foundation-model family.

Its theoretical unification theme connects to ambiguity-averse MDPs and CoEvol-NO: all three recast existing methods as special cases of a more general formalism.

## Notes for Cross-Paper Synthesis

XDLM contributes to the corpus-wide pattern of balancing axes rather than optimizing one number: understanding versus generation, memory versus capability, and theory versus deployable computation.
