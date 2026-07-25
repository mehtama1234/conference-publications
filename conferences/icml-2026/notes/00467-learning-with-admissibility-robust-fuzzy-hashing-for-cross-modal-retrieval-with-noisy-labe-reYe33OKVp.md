# Learning with Admissibility: Robust Fuzzy Hashing for Cross-Modal Retrieval with Noisy Labels

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: reYe33OKVp
- Authors: Xincheng Sun; Ruitao Pu; Guangsi Shi; Zhenwen Ren; Peng Hu; Yuan Sun
- Primary area: general_machine_learning->representation_learning
- Keywords: cross-modal hashing;multimodal retrieval;noisy labels
- Source URL: https://openreview.net/forum?id=reYe33OKVp
- PDF URL: https://openreview.net/pdf?id=reYe33OKVp

## Abstract

Recently, cross-modal hashing (CMH) has garnered significant attention due to its low storage costs and high retrieval efficiency. Most existing CMH methods implicitly assume the availability of high-quality annotations, which is often violated in real-world scenarios as label noise inevitably arises from human errors or non-expert annotations. To cope with noisy supervision, current noise-robust CMH methods mainly follow two paradigms, i.e., noise separation and label smoothing. They often discard the predicted noisy instances or smooth discriminative signals to mitigate the impact of noisy labels. However, aggressive separation leads to reduced data utilization, while smoothing weakens the discriminative capability regarding the true distribution of clean instances. To address these limitations, we propose a novel Robust Fuzzy Cross-modal Hashing framework (RFCMH) that introduces fuzzy set theory to endow the labels with admissibility, thereby obtaining reliable discriminative supervision from noisy labels. Specifically, we first leverage possibility and necessity measures to model the noisy labels. Subsequently, we propose Fuzzy Admissibility Refinement (FAR) to dynamically calibrate supervision signals, thereby preventing the model from being misled by false positives. Furthermore, we introduce Dual-Granularity Structural Alignment (DGSA) to enforce both cross-modal alignment and instance-level uniformity, ensuring stable and diverse representations. Extensive experiments on multiple benchmarks demonstrate that RFCMH achieves state-of-the-art retrieval performance. Code is available at https://github.com/XinchengSun/RFCMH.

## One-Sentence Claim

RFCMH makes cross-modal hashing robust to noisy labels by modeling label admissibility with fuzzy possibility/necessity measures and aligning representations at both cross-modal and instance granularity.

## Problem

Cross-modal hashing is attractive for multimodal retrieval because binary hashes reduce storage and accelerate search. Most methods assume clean annotations, but real labels often contain human or non-expert noise.

Existing robust methods tend to either separate and discard predicted noisy samples or smooth labels. Discarding wastes data, while smoothing can weaken discriminative signal from truly clean examples.

## Core Contribution

The paper proposes Robust Fuzzy Cross-modal Hashing, which uses fuzzy set theory to assign admissibility to labels rather than treating them as clean, noisy, or uniformly smoothed.

It introduces Fuzzy Admissibility Refinement to dynamically calibrate supervision and prevent false positives from misleading the model, plus Dual-Granularity Structural Alignment to enforce cross-modal alignment and instance-level uniformity.

## Method

RFCMH models noisy labels through possibility and necessity measures. These fuzzy measures represent uncertainty about whether a label should be treated as admissible supervision.

FAR adjusts supervision signals over training, while DGSA aligns modalities globally and maintains stable diverse instance-level representations. The goal is to use noisy data without either discarding too much or blurring class distinctions.

## Experiments and Evidence

The abstract reports state-of-the-art retrieval performance on multiple benchmarks. The code is available, suggesting reproducibility support.

Full-paper reading should verify benchmark names, noise models and rates, hash lengths, cross-modal pairs, ablations for FAR/DGSA, and performance under real versus synthetic label noise.

## Limits and Failure Modes

Fuzzy admissibility depends on whether possibility and necessity measures are well calibrated. If the model's early estimates are wrong, refinement could reinforce bad supervision.

Hashing compresses representations aggressively, so robustness gains must be balanced against the risk of losing fine-grained semantic distinctions needed for difficult retrieval queries.

## Deep Themes

- Noisy labels as graded admissibility: supervision is neither simply trusted nor discarded.
- Efficient multimodal retrieval: hashing remains valuable when retrieval scale matters.
- Dual-granularity alignment: representation learning must align modalities and preserve instance diversity.
- Robustness through calibrated supervision: dynamic label trust replaces static filtering.

## Subthemes

- Possibility and necessity measures provide asymmetric uncertainty about labels.
- False positives are especially harmful for retrieval supervision.
- Label smoothing can undermine discriminative structure.
- Cross-modal uniformity prevents collapsed hash spaces.

## Connections to Other Papers

RFCMH connects to JYP noisy-label learning, embedding translation, concept binding, and multimodal representation alignment. It also relates to ConFlux and TabSwift as structured-data efficiency work where deployment cost matters.

Its fuzzy supervision theme parallels ADEPT's treatment of minority emotion labels: ambiguous labels can be modeled instead of discarded.

## Notes for Cross-Paper Synthesis

The synthesis point is that label uncertainty is increasingly represented with structure. Across noisy labels, affect annotations, and causal adjustment, papers are moving beyond binary clean/noisy assumptions.
