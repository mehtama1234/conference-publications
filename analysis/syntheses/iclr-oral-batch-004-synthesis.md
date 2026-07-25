# ICLR 2026 Oral Batch 004 Synthesis

## Papers

- FRABench and UFEval: Unified Fine-grained Evaluation with Task and Aspect Generalization
- Temporal superposition and feature geometry of RNNs under memory demands
- OpenThoughts: Data Recipes for Reasoning Models
- Instilling an Active Mind in Avatars via Cognitive Simulation
- Seeing Through the Brain: New Insights from Decoding Visual Stimuli with fMRI

## Source Depth

All five notes are abstract/metadata-only in the current local workspace. OpenReview remains the preferred source, and arXiv fallback should be retried for this ICLR oral range when rate limits clear.

## Shared Thesis

This batch is about intermediate structure as the bridge between raw signals and higher-level judgment or behavior. UFEval uses aspect taxonomies to judge multimodal outputs; temporal superposition explains how RNNs pack memory into geometry; OpenThoughts treats reasoning data recipes as reproducible infrastructure; avatar generation inserts structured cognitive guidance between conditions and motion; and PRISM maps fMRI into structured text before image reconstruction.

The common pattern is that the most useful representation is neither raw input nor final output. It is an intermediate scaffold: aspects, feature geometry, data recipe stages, cognitive text plans, or structured semantic scene descriptions.

## Subthemes

### Generalizing evaluation criteria

FRABench/UFEval treats evaluation aspects as related concepts that can transfer across tasks. This reframes judging as a multi-task learning problem rather than a collection of isolated rubric-specific classifiers.

### Geometry of recurrent memory

Temporal superposition shows that memory demands alter RNN feature geometry. Dense and sparse regimes emerge depending on capacity pressure, with spectral and angular signatures revealing how interference is managed.

### Open reasoning data recipes

OpenThoughts emphasizes that reasoning capability depends on data-generation pipelines. Public recipe science, not only model release, is needed to reproduce reasoning-model progress.

### Cognitive simulation for avatars

The avatar paper uses MLLM-generated structured text to represent intent and emotion before video diffusion. This adds a semantic control layer between multimodal conditions and motion.

### Structured text as neural bridge

PRISM finds that fMRI visual signals align well with text-space structure. Object, attribute, and relationship descriptions become an intermediate format for reconstructing images from brain activity.

## Cross-Batch Connections

UFEval connects to ICML evaluation work such as MiniAppBench, Copyright-Bench, CounselBench, and MetaphorVU. All push evaluation toward richer criteria and generalization.

Temporal superposition connects to ICML linear recurrent memory, POPGym, LAMP, and path-dependent inference through memory under capacity and partial observability.

OpenThoughts connects to Ctrl-R, PonderLM-2, H1, RAGEN-2, and SGD RLVR through reasoning-model training and post-training pipelines.

Avatar cognitive simulation connects to PanoWorld-X, VectorWorld, EgoTactile, and MetaphorVU through temporally coherent multimodal generation with semantic control.

PRISM connects to BioX-Bridge, Mind-Omni, concept binding, and structured multimodal representation work through cross-modal latent alignment.

## Emerging Pattern

The broader cross-conference pattern is intermediate representation design. Robust models increasingly depend on choosing the right abstraction layer between data and decision.
