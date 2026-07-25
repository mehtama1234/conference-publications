# Veritas: Generalizable Deepfake Detection via Pattern-Aware Reasoning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 5VXJPS1HoM
- Authors: Hao Tan; jun lan; Zichang Tan; Senyuan Shi; Ajian Liu; Chuanbiao Song; Huijia Zhu; Weiqiang Wang; Jun Wan; Zhen Lei
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Deepfake Detection;MLLMs
- Source URL: https://openreview.net/forum?id=5VXJPS1HoM
- PDF URL: https://openreview.net/pdf?id=5VXJPS1HoM

## Abstract

Deepfake detection remains a formidable challenge due to the evolving nature of fake content in real-world scenarios. However, existing benchmarks suffer from severe discrepancies from industrial practice, typically featuring homogeneous training sources and low-quality testing images, which hinder the practical usage of current detectors. To mitigate this gap, we introduce **HydraFake**, a dataset that contains diversified deepfake techniques and in-the-wild forgeries, along with rigorous training and evaluation protocol, covering unseen model architectures, emerging forgery techniques and novel data domains. Building on this resource, we propose **Veritas**, a multi-modal large language model (MLLM) based deepfake detector. Different from vanilla chain-of-thought (CoT), we introduce *pattern-aware reasoning* that involves critical patterns such as "planning" and "self-reflection" to emulate human forensic process. We further propose a two-stage training pipeline to seamlessly internalize such deepfake reasoning capacities into current MLLMs. Experiments on HydraFake dataset reveal that although previous detectors show great generalization on cross-model scenarios, they fall short on unseen forgeries and data domains. Our Veritas achieves significant gains across different out-of-domain (OOD) scenarios, and is capable of delivering transparent and faithful detection outputs.

## One-Sentence Claim

Veritas improves deepfake detection under real-world distribution shifts by training an MLLM to perform pattern-aware forensic reasoning on the diverse HydraFake benchmark.

## Problem

Deepfake detectors often benchmark on homogeneous training sources and low-quality test images, leaving a gap between academic evaluation and industrial practice with unseen forgery models, new techniques, and novel domains.

## Core Contribution

The paper introduces HydraFake, a dataset/protocol with diversified deepfake techniques and in-the-wild forgeries, and Veritas, an MLLM-based detector with pattern-aware reasoning and a two-stage training pipeline.

## Method

Veritas replaces generic chain-of-thought with pattern-aware reasoning that includes planning and self-reflection to emulate human forensic analysis. The model internalizes this reasoning through a two-stage training pipeline.

## Experiments and Evidence

The abstract reports that prior detectors generalize to cross-model scenarios but fail on unseen forgeries and domains, while Veritas achieves significant gains across OOD scenarios and produces transparent, faithful detection outputs.

## Limits and Failure Modes

PDF checks needed: HydraFake composition, whether reasoning rationales are faithful, robustness to adversarial postprocessing, and deployment false-positive/false-negative tradeoffs.

## Deep Themes

- Detection is shifting toward reasoning over forensic patterns, not only artifacts.
- Benchmarks need to match in-the-wild generation diversity.
- Transparent outputs are becoming part of security evaluation.

## Subthemes

- Deepfake detection.
- Multimodal LLMs.
- Pattern-aware reasoning.
- OOD robustness.
- Forensic explanation.

## Connections to Other Papers

Connects to Spherical Watermark, Catch-22, and visual reasoning papers. It is part of the provenance/authenticity cluster from the detection side rather than the watermarking side.

## Notes for Cross-Paper Synthesis

Veritas supports the pattern that media authenticity research is splitting into complementary tools: watermarking generated content, detecting forged content, and reasoning transparently about evidence.

## Full-Text Upgrade

Source used: `conferences/iclr-2026/text/00017-veritas-generalizable-deepfake-detection-via-pattern-aware-reasoning-5VXJPS1HoM-arxiv.txt`.

Additional verified details:

- HydraFake contains 50K real and 50K fake images, including classic datasets, public/social-media deepfakes, and 10 advanced generator sources.
- The evaluation is hierarchical: in-domain, cross-model, cross-forgery, and cross-domain testing.
- Veritas structures outputs with tags such as fast assessment, planning, reasoning, reflection, conclusion, and answer.
- The training pipeline includes pattern-guided cold start and pattern-aware reinforcement learning.
- Pattern-aware rewards encourage helpful planning/reflection and penalize unnecessary overthinking.
- Pattern-aware reasoning improves OOD scenarios, with the text reporting 6.2% and 3.3% gains on cross-forgery and cross-domain testing.
- Self-reflection is especially important for cross-forgery settings, while planning is more effective for fully synthesized images.

Refined limits:

- Reasoning transparency depends on whether generated explanations are faithful rather than plausible post-hoc narratives.
- The benchmark is image-focused; video/audio deepfake generalization would need separate validation.
