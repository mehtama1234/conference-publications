# $PhyWorldBench$: A Comprehensive Evaluation of Physical Realism in Text-to-Video Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: rlZeILv3fm
- Authors: Jing Gu; Xian Liu; Yu Zeng; Ashwin Nagarajan; Fangrui Zhu; Daniel Hong; Yue Fan; Qianqi Yan; Kaiwen Zhou; Ming-Yu Liu; Xin Eric Wang
- Primary area: datasets and benchmarks
- Keywords: Video Generation;Video Evaluation
- Source URL: https://openreview.net/forum?id=rlZeILv3fm
- PDF URL: https://openreview.net/pdf?id=rlZeILv3fm

## Abstract

Video generation models have achieved remarkable progress in creating high-quality, photorealistic content. However, their ability to accurately simulate physical phenomena remains a critical and unresolved challenge. This paper presents $PhyWorldBench$
, a comprehensive benchmark designed to evaluate video generation models based on their adherence to the laws of physics. The benchmark covers multiple levels of physical phenomena, ranging from fundamental principles like object motion and energy conservation to more complex scenarios involving rigid body interactions and human or animal motion. Additionally, we introduce a novel "Anti-Physics" category, where prompts intentionally violate real-world physics, enabling the assessment of whether models can follow such instructions while maintaining logical consistency. Besides large-scale human evaluation, we also design a simple yet effective method that could utilize current MLLM to evaluate the physics realism in a zero-shot fashion. We evaluate 10 state-of-the-art text-to-video generation models, including five open-source and five proprietary models, with a detailed comparison and analysis. we identify pivotal challenges models face in adhering to real-world physics. Through systematic testing of their outputs across 1,050 curated prompts—spanning fundamental, composite, and anti-physics scenarios—we identify pivotal challenges these models face in adhering to real-world physics. We then rigorously examine their performance on diverse physical phenomena with varying prompt types, deriving targeted recommendations for crafting prompts that enhance fidelity to physical principles.

## One-Sentence Claim

PhyWorldBench evaluates whether text-to-video models obey physical principles across curated fundamental, composite, and anti-physics prompt categories.

## Problem

Text-to-video models can produce photorealistic clips while still violating object motion, conservation, interaction, and embodied dynamics. Existing evaluations often emphasize visual quality or prompt alignment rather than physical realism and logical consistency under physically unusual instructions.

## Core Contribution

The paper introduces PhyWorldBench, a 1,050-prompt benchmark for physical realism in video generation, including an Anti-Physics category for prompts that intentionally violate normal physical laws. It also proposes a zero-shot MLLM-based evaluator alongside human evaluation.

## Method

The benchmark organizes prompts by physical phenomenon level, generates outputs from ten open-source and proprietary text-to-video models, evaluates physical adherence with large-scale human judgments and an MLLM evaluator, and analyzes performance by phenomenon and prompt type.

## Experiments and Evidence

The abstract reports evaluation of ten state-of-the-art models, five open-source and five proprietary, over 1,050 prompts. The analysis identifies major challenges in obeying real-world physics and derives prompting recommendations to improve physical fidelity.

## Limits and Failure Modes

Physical realism judgments can be subjective when short generated videos are ambiguous. MLLM-based evaluators may miss subtle dynamics or share model biases with generators. Full-text review should check prompt taxonomy, human annotation protocol, evaluator calibration, model versions, and whether anti-physics tasks measure instruction following separately from realism.

## Deep Themes

- Physical realism evaluation for generated video.
- Benchmarking beyond photorealism.
- MLLM evaluators for media physics.
- Prompting effects on physical fidelity.

## Subthemes

- Fundamental versus composite physical phenomena.
- Anti-physics prompting.
- Human and automated video evaluation.
- Text-to-video model failure taxonomy.
- Physics-aware prompt design.

## Connections to Other Papers

Connects to SANA-Video and MotionStream through video generation, to RadioGS and physics-aware visual modeling through physical constraints, and to evaluation papers that move beyond surface quality into functional realism.

## Notes for Cross-Paper Synthesis

PhyWorldBench shows that generative media evaluation is moving toward world-model competence: the output must not only look plausible but behave according to the requested physical logic.
