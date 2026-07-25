# Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: OJsGhlTayF
- Authors: Shankar Padmanabhan; Mustafa Omer Gul; Tanya Goyal
- Primary area: deep_learning->large_language_models
- Keywords: Continual learning;catastrophic forgetting;Large language models;instruction-tuned models;domain adaptation;distillation
- Source URL: https://openreview.net/forum?id=OJsGhlTayF
- PDF URL: https://openreview.net/pdf?id=OJsGhlTayF

## Abstract

Post-training endows pretrained LLMs with a variety of desirable skills, including instruction-following, reasoning, and others. However, these post-trained LLMs only encode knowledge up to a cut-off date, necessitating continual adaptation. Unfortunately, existing solutions cannot simultaneously learn new knowledge from an adaptation document corpora and mitigate the forgetting of earlier learned capabilities.
To address this, we introduce Distillation via Split Contexts (DiSC), a simple context-distillation based approach for continual knowledge adaptation. DiSC derives student and teacher distributions by conditioning on distinct segments of the training example and minimizes the KL divergence between the shared tokens. This allows us to efficiently apply context-distillation without requiring explicit generation steps during training. 
We run experiments on four post-trained models and two adaptation domains. Compared to prior finetuning and distillation methods for continual adaptation, DiSC consistently reports the best trade-off between learning new knowledge and mitigating forgetting of previously learned skills like instruction-following, reasoning, and factual knowledge.

## One-Sentence Claim

DiSC updates LLM parametric knowledge from adaptation documents while retaining post-training skills by distilling between distributions conditioned on split context segments.

## Problem

Post-trained LLMs need continual knowledge updates after their cutoff date, but standard fine-tuning and distillation methods can forget instruction-following, reasoning, and earlier factual capabilities.

## Core Contribution

The paper introduces Distillation via Split Contexts, a context-distillation approach that avoids explicit generation during training and improves the tradeoff between new knowledge learning and capability retention.

## Method

DiSC conditions student and teacher distributions on distinct segments of a training example and minimizes KL divergence over shared tokens, enabling efficient context distillation from adaptation corpora.

## Experiments and Evidence

The abstract reports experiments on four post-trained models and two adaptation domains where DiSC outperforms prior fine-tuning and distillation methods on the new-knowledge versus forgetting tradeoff.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: adaptation domains, retention benchmarks, context split strategy, compute cost, hallucination effects, and whether updates can overwrite incorrect prior knowledge.

## Deep Themes

- Continual knowledge adaptation must preserve post-training capabilities.
- Context can create teacher/student signals without explicit generation.
- Knowledge freshness and capability retention are coupled deployment requirements.

## Subthemes

- Continual learning.
- Parametric knowledge updates.
- Context distillation.
- Catastrophic forgetting.
- Instruction-following retention.
- Domain adaptation.

## Connections to Other Papers

Connects to MemoryBench, GR-LoRA, Nevo-CRL, and safe fine-tuning work through long-term adaptation without forgetting.

## Notes for Cross-Paper Synthesis

DiSC adds a knowledge-maintenance theme: deployed LLMs need ways to absorb new corpora without erasing the post-training behaviors that make them usable.
