# Beyond Language Modeling: An Exploration of Multimodal Pretraining

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: xAKrRYm6pc
- Authors: Shengbang Tong; David Fan; John Nguyen; Ellis L Brown II; Gaoyue Zhou; Shengyi Qian; Boyang Zheng; Théophane Vallaeys; Rob Fergus; Naila Murray; Marjan Ghazvininejad; Mike Lewis; Nicolas Ballas; Amir Bar; Michael Rabbat; Jakob Verbeek; Luke Zettlemoyer; Koustuv Sinha; Yann LeCun; Saining Xie
- Primary area: deep_learning
- Keywords: multimodal pretraining;modality competition;diffusion transformers;representation autoencoder;scaling laws
- Source URL: https://openreview.net/forum?id=xAKrRYm6pc
- PDF URL: https://openreview.net/pdf?id=xAKrRYm6pc

## Abstract

The visual world offers a critical axis for advancing foundation models beyond language. Despite growing interest in this direction, the design space for native multimodal models remains opaque. We provide empirical clarity through controlled, from-scratch pretraining experiments, isolating the factors that govern multimodal pretraining without interference from language pretraining. We adopt the Transfusion framework, using next-token prediction for language and diffusion for vision, to train on diverse data including text, video, image-text pairs, and even action-conditioned video. Our experiments yield four key insights: (i) Representation Autoencoder (RAE) provides an optimal unified visual representation by excelling at both visual understanding and generation; (ii) visual and language data are complementary and yield synergy for downstream capabilities; (iii) unified multimodal pretraining leads naturally to world modeling, with capabilities emerging from general training; and (iv) Mixture-of-Experts (MoE) enables efficient and effective multimodal scaling while naturally inducing modality specialization. Through IsoFLOP analysis, we compute scaling laws for both modalities and uncover a scaling asymmetry: vision is significantly more data-hungry than language. We demonstrate that the MoE architecture harmonizes this scaling asymmetry by providing the high model capacity required by language while accommodating the data-intensive nature of vision, paving the way for truly unified multimodal models.

## One-Sentence Claim

Controlled from-scratch multimodal pretraining shows that vision and language are complementary but scale asymmetrically, with MoE architectures helping unify data-hungry vision and capacity-hungry language.

## Problem

Native multimodal foundation models are increasingly important, but the design space is opaque because many systems inherit confounds from language pretraining, pretrained visual encoders, or mixed training recipes.

The problem is to isolate what actually governs multimodal pretraining when models learn language, images, video, image-text pairs, and action-conditioned video together from scratch.

## Core Contribution

The paper provides controlled empirical clarity using the Transfusion framework, next-token prediction for language, and diffusion for vision.

It identifies four central findings: RAEs work well as unified visual representations; visual and language data are complementary; unified multimodal pretraining naturally yields world-modeling capabilities; and MoE enables efficient scaling while inducing modality specialization.

## Method

The authors train from-scratch multimodal models on diverse data types under controlled conditions. Transfusion combines autoregressive language modeling with diffusion-based visual modeling.

They use IsoFLOP analysis to compare scaling behavior across modalities and study how MoE capacity allocation handles different vision and language scaling needs.

## Experiments and Evidence

The abstract reports that Representation Autoencoders provide a strong unified visual representation for both understanding and generation.

It also reports modality synergy, emergent world modeling from unified pretraining, natural modality specialization in MoE, and a scaling asymmetry where vision is significantly more data-hungry than language.

## Limits and Failure Modes

From-scratch controlled experiments can clarify mechanisms but may not fully capture industrial-scale data mixtures, proprietary curation, or instruction-tuning effects.

Because this note is abstract-only, details still need checking: model sizes, data composition, compute budgets, downstream tasks, RAE variants, action-conditioned video setup, MoE routing statistics, and exact scaling-law fits.

## Deep Themes

- Multimodal pretraining as first-principles design: remove language-pretraining confounds to study modality interactions.
- Scaling asymmetry: modalities demand different balances of data and capacity.
- MoE as modality harmonizer: sparse capacity can specialize naturally across modalities.
- World modeling as emergent multimodal capability: video and action-conditioned data push models beyond static perception.

## Subthemes

- Representation Autoencoders for unified visual tokens.
- Transfusion-style language plus diffusion training.
- IsoFLOP multimodal scaling laws.
- Vision-language complementarity.

## Connections to Other Papers

This connects to SplAttN, DroneDINO, EgoTactile, and Mind-Omni through the broader question of how visual, linguistic, and embodied signals should share representations.

It also links to ScaleMoE and routed expert work because MoE appears as a way to match heterogeneous modality scaling laws.

## Notes for Cross-Paper Synthesis

This paper strengthens the multimodal scaling theme: unified foundation models need architectures and data schedules that respect modality-specific scaling behavior rather than forcing all modalities through a language-centric recipe.
