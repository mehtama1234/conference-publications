# World-Model Inspired Emotion-aware Token Refinement for Training-Free Multimodal Emotion Recognition

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ViQO8FlRFR
- Authors: Kejun Liu; Zhe Chen; Yuanyuan Liu; ke Wang; Yibing Zhan; Wei Xiang; Hongyan Zhang
- Primary area: applications->computer_vision
- Keywords: Multimodal Emotion Reasoning;Multimodal Large Language Model;Emotion Recognition
- Source URL: https://openreview.net/forum?id=ViQO8FlRFR
- PDF URL: https://openreview.net/pdf?id=ViQO8FlRFR

## Abstract

Multimodal Large Language Models (MLLMs) show promise for Multimodal Emotion Recognition (MER) but often remain unreliable because sparse emotional cues could be easily overwhelmed and affected by redundant context. While fine-tuning is effective, it is usually costly when using large models. Training-free methods like chain-of-thought reasoning provide a practical alternative, but they mostly rely on heuristic prompting to influence the model behaviors and do not explicitly focus on emotion relevant tokens internally, which would allow decision-relevant emotional tokens to be diluted by environmental noise, resulting in unstable predictions. To address this limitation without training, we rethink MER from a world-model perspective that treats emotion as a latent state inferred from noisy and redundant multimodal observations. Under frozen parameters, this view suggests that robustness depends on constraining why and how tokens contribute to inference.  Based on this insight, we propose WETR (World-Model inspired Emotion-aware Token Refinement), a training-free, plug-and-play regulator that reshapes token usage through two mechanisms: Noise-suppressed Token Selection (NTS), which suppresses redundant intra-modal noise, and State-strengthened Token Reweighting (STR), which amplifies decision-relevant emotional tokens. Experiments on multiple MER benchmarks demonstrate that WETR consistently improves accuracy and stability under frozen parameters, which also improves token-level interpretability.

## One-Sentence Claim

WETR improves frozen MLLM emotion recognition by treating emotion as a latent state and refining token usage to suppress redundant context while amplifying emotion-relevant evidence.

## Problem

Multimodal emotion recognition depends on sparse affective cues that can be overwhelmed by redundant visual, audio, or contextual information. Fine-tuning large MLLMs can improve reliability, but it is costly. Training-free prompting methods are cheaper, yet they mostly manipulate visible reasoning text and do not explicitly control which internal tokens drive the decision.

The paper asks how to make frozen MLLMs attend to emotion-relevant evidence without parameter updates.

## Core Contribution

The paper proposes WETR, World-Model inspired Emotion-aware Token Refinement, a training-free plug-and-play regulator. It reinterprets emotion as a latent state inferred from noisy multimodal observations and constrains token contribution through two mechanisms:

- Noise-suppressed Token Selection suppresses redundant intra-modal noise.
- State-strengthened Token Reweighting amplifies decision-relevant emotion tokens.

The result is improved accuracy, stability, and token-level interpretability under frozen parameters.

## Method

WETR operates at token level rather than by changing model weights. It selects tokens likely to carry emotion evidence, suppresses noisy or redundant tokens within modalities, and reweights tokens that strengthen the inferred latent emotional state.

The world-model framing matters because the method separates observed multimodal clutter from the hidden affective state the model should infer.

## Experiments and Evidence

Evidence reported in the abstract:

- Multiple multimodal emotion recognition benchmarks.
- Accuracy gains under frozen MLLM parameters.
- Improved prediction stability.
- Improved token-level interpretability.
- Training-free plug-and-play deployment.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: modalities used, benchmark names, token-selection scoring, stability metric, and whether gains hold across base MLLMs.

## Limits and Failure Modes

- Token-level emotion cues may be ambiguous or culturally context-dependent.
- Training-free reweighting depends on the base MLLM already encoding useful emotion features.
- Suppressing redundant context could remove situational evidence needed for affect inference.
- Interpretability claims need causal validation, not just token salience.

## Deep Themes

**Frozen models still need internal evidence control.** WETR does not add knowledge; it changes which tokens are allowed to dominate inference.

**Latent-state framing clarifies multimodal reasoning.** Emotion is treated as hidden state inferred from noisy observations.

**Training-free methods are becoming mechanistic.** Rather than prompt heuristics, the method intervenes on token selection and weighting.

## Subthemes

- Emotion-aware token selection.
- State-strengthened token reweighting.
- Training-free MLLM regulation.
- Sparse affective cues under redundant context.
- Token-level interpretability.

## Connections to Other Papers

Connects to DLMR, DOUBT, Table-GLS, and latent action supervision through explicit routing or weighting of multimodal evidence. It also links to TG-RAG because both steer frozen or largely fixed reasoning processes by injecting or emphasizing task-relevant guidance.

## Notes for Cross-Paper Synthesis

WETR reinforces the theme that long or multimodal context is not enough. Models need mechanisms that decide which pieces of context should actually control inference.
