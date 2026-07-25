# ICLR Oral Batch 021 Synthesis

## Papers Covered

- How Learning Rate Decay Wastes Your Best Data in Curriculum-Based LLM Pretraining
- Quantitative Bounds for Length Generalization in Transformers
- Characterizing the Discrete Geometry of ReLU Networks
- UALM: Unified Audio Language Model for Understanding, Generation and Reasoning
- LLM DNA: Tracing Model Evolution via Functional Representations

## Shared Thesis

This batch is about hidden structure in training, architecture, modality, and model ancestry. Curriculum pretraining only works when the optimizer still lets late high-quality data matter. Transformer length generalization depends on whether long-sequence behavior is simulated by shorter training examples. ReLU networks have constrained connectivity in their polyhedral region complexes. UALM unifies audio understanding, generation, and reasoning in a shared token/model space. LLM DNA traces model evolution through functional fingerprints. Across the batch, the visible surface metric is not enough; the explanatory object is a schedule, internal behavior, geometric complex, modality-token interface, or lineage representation.

## Deep Themes

### Training Schedules as Data-Use Mechanisms

The curriculum pretraining paper makes a simple but important point: data ordering cannot be evaluated separately from learning-rate schedules. Late high-quality data is useful only if updates remain large enough to absorb it. This connects data curation to optimization design and makes training time itself part of data governance.

### Theory of Extrapolation and Geometry

The length-generalization and ReLU-geometry papers both characterize model behavior through internal structure rather than external performance alone. Length generalization depends on simulating long-sequence computation from shorter examples. ReLU behavior depends on connectivity among linear-region polyhedra, not just their count. Both papers refine what it means to understand a network theoretically.

### Unified Modality Spaces

UALM extends the multimodal unification trend into audio: the same model should understand audio, generate audio, reason over text, and use audio in intermediate reasoning. This makes audio tokens part of the language-model substrate rather than a separate generation pipeline.

### Functional Provenance

LLM DNA addresses model-lineage opacity by deriving low-dimensional fingerprints from functional behavior. This is increasingly necessary because fine-tuning, distillation, merging, and self-improvement can obscure ancestry even when behavior remains related.

## Cross-Paper Pattern

The shared pattern is that hidden coordinates explain observed behavior. Curriculum gains are explained by the interaction of quality order and learning-rate decay. Length extrapolation is explained by short-to-long internal simulation. ReLU complexity is explained by region connectivity. Audio capability is explained by shared tokenized modeling. Model ancestry is explained by functional representation. The batch adds depth to the broader theme that robust ML understanding requires the right coordinate system for the phenomenon.

## Subthemes to Track

- Curriculum and optimizer co-design.
- Quantitative transformer length generalization.
- Polyhedral connectivity of ReLU networks.
- Unified audio-language understanding, generation, and reasoning.
- Functional model-lineage fingerprints.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Implementation, theorem, and benchmark details should be upgraded when PDFs are available.
