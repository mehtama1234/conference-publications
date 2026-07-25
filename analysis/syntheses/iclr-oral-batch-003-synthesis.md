# ICLR 2026 Oral Batch 003 Synthesis

Scope: ICLR oral notes 14-18.

Source depth: abstracts for all five papers; full extracted text for MomaGraph, Difficult Examples, Veritas, and Invisible Safety Threat.

## Papers Covered

- MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning.
- HATSolver: Learning Groebner Bases with Hierarchical Attention Transformers.
- Difficult Examples Hurt Unsupervised Contrastive Learning: A Theoretical Perspective.
- Veritas: Generalizable Deepfake Detection via Pattern-Aware Reasoning.
- Invisible Safety Threat: Malicious Finetuning for LLM via Steganography.

## Emerging Pattern 1: Intermediate Structure Is Becoming the Planner

MomaGraph makes the intermediate representation explicit: the VLM predicts a task-specific scene graph and then plans from it. The full text shows Graph-then-Plan improves performance across models, suggesting structured intermediate artifacts help with embodied reasoning.

This pattern connects to visual symbolic mechanisms, CompSLOT, and Base Models Know How to Reason. Across papers, models become more reliable when they expose or construct an intermediate structure that can be inspected, steered, or used for downstream reasoning.

## Emerging Pattern 2: Neural Methods Are Moving Into Formal Symbolic Domains

HATSolver applies hierarchical attention to Groebner basis computation. Its contribution is not just using a transformer, but adding a tree-structured inductive bias and curriculum learning for a formal algebraic problem.

This extends the hybrid neural-symbolic theme. Neural methods are being adapted to symbolic domains by matching the architecture to the structure of the formal object.

## Emerging Pattern 3: Data Difficulty Is Objective-Dependent

The contrastive-learning paper shows that examples considered useful or essential in supervised learning can harm unsupervised contrastive learning. The full-text theory models this through similarity graphs and linear probing bounds.

This deepens the data curation theme: data is not intrinsically good or bad. Its value depends on the learning objective, the representation geometry, and the downstream evaluation.

## Emerging Pattern 4: Media Authenticity Requires Both Detection and Provenance

Veritas complements watermarking papers by attacking the authenticity problem from the detector side. HydraFake introduces more realistic OOD testing, while Veritas uses pattern-aware reasoning with planning and self-reflection to improve deepfake detection.

Together with Spherical Watermark and Catch-22, this suggests a provenance/authenticity cluster with three linked strategies:

- watermark generated content;
- detect forged content under distribution shift;
- explain the forensic evidence behind judgments.

## Emerging Pattern 5: Safety Can Fail Through Invisible Channels

Invisible Safety Threat shows a covert-channel failure mode: a model can appear aligned in visible plaintext while exchanging malicious content through zero-width-character steganography. The full text reports that safety classifiers mark stegotext as safe before decoding while decoded interactions are usually unsafe.

This expands the safety theme beyond prompt jailbreaks. The safety surface includes encodings, UI rendering, fine-tuning data filters, and monitor assumptions.

## Cross-Batch Links

- MomaGraph and FlashWorld both point toward structured spatial/world representations, but MomaGraph focuses on task planning while FlashWorld focuses on fast 3D generation.
- HATSolver and LSFlow both combine neural modeling with formal constraints or structured algorithms.
- Difficult Examples and Common Corpus both treat data as an intervention, but at different levels: example selection versus corpus governance.
- Veritas and Spherical Watermark form a media authenticity pair: detection and watermarking.
- Invisible Safety Threat and SandboxEscapeBench both show agent/LLM safety depends on hidden system-level assumptions.

## Subthemes to Track

- Task-specific scene graphs.
- Graph-then-Plan embodied reasoning.
- Hierarchical attention for formal algebra.
- Objective-aware data pruning.
- Pattern-aware forensic reasoning.
- Hidden-channel safety attacks.
- Fine-tuning supply-chain risk.

