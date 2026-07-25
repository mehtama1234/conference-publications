# ICML 2026 Spotlight Batch 028 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 136-140:

- Learning Unmasking Policies for Diffusion Language Models
- OC-space: a Unifying Perspective on Verification of Tree Ensembles
- HELIX: Hybrid Encoding with Learnable Identity and Cross-dimensional Synthesis for Time Series Imputation
- PaperBanana: Automating Academic Illustration for AI Scientists
- DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 135.

## Emerging Pattern 1: Decoding Policies Are Becoming Learned Controllers

Learning Unmasking Policies treats diffusion language-model sampling as an MDP. Rather than relying on confidence-threshold heuristics, a small policy learns which tokens to unmask from the dLLM's token confidences.

This connects to LoMDM, Flex-Forcing, ThreadWeaver, and MaxRL. A consistent direction is that inference procedures are being optimized as policies, not treated as static hand-coded schedules.

## Emerging Pattern 2: Verification Benefits from the Right Discrete Space

OC-space reframes tree-ensemble verification around output configurations: combinations of individual tree predictions. Robustness and fairness queries become searches in this space, with linear/quadratic algorithms in OC-space size and possible acceleration by spatial indexes.

This connects to CIRBench and other correctness-aware evaluation work. The pattern is that verification difficulty can change sharply when the right representation of the model's behavior is exposed.

## Emerging Pattern 3: Time-Series Models Need Persistent Feature Identity

HELIX argues that attention-based imputation should not rediscover feature relationships from scratch at every layer. Learnable feature identities provide anchors for cross-dimensional structure, enabling arbitrary feature dependencies without fixed graph topology.

This connects to time-series foundation-model redundancy and cross-domain saliency. Time-series papers in the corpus increasingly treat feature identity, domain transforms, and latent structure as core modeling objects.

## Emerging Pattern 4: AI-Scientist Workflows Are Expanding Beyond Text

PaperBanana targets publication-ready academic illustration. It uses specialized agents for reference retrieval, content/style planning, rendering, and self-critique, and benchmarks methodology-diagram generation with PaperBananaBench.

This connects to DR Tulu, CVE-Factory, and other agentic workflow papers. Research automation is moving from answering questions and writing text toward producing the visual and executable artifacts that scientific work actually requires.

## Emerging Pattern 5: Human Video Is Becoming a Robotics Pretraining Substrate

DreamDojo learns a generalist robot world model from 44k hours of egocentric human videos. Continuous latent actions bridge unlabeled human interaction data to robot action controllability, and distillation makes the model real-time enough for teleoperation, policy evaluation, and planning.

This links strongly to dWorldEval, RoboMME, SAW-Bench, SpatioLM, and SVL. The embodied AI cluster is converging on large-scale video as a source of physical interaction priors.

## Cross-Batch Links

- Learning Unmasking Policies, LoMDM, Flex-Forcing, and ThreadWeaver all optimize the inference process as a controllable policy.
- OC-space, CIRBench, and Jailbreak Foundry expose verification/evaluation through executable or enumerable structure.
- HELIX, TSFM redundancies, and cross-domain saliency show time-series ML becoming more interpretable and structure-aware.
- PaperBanana, DR Tulu, and CVE-Factory broaden agentic automation into complete research workflows.
- DreamDojo, dWorldEval, and SAW-Bench build an embodied world-model/evaluation stack around videos, actions, and physical context.

## Deep Theme Update

Batch 028 reinforces a process-design pattern: unmasking decisions, verification search spaces, feature identities, illustration workflows, and latent robot actions are all operational interfaces. The papers make progress by exposing a hidden process and turning it into something learnable, searchable, or orchestrated.
