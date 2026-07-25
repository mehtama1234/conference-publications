# ICLR 2026 Oral Batch 011 Synthesis

## Papers

- Softmax Transformers are Turing-Complete
- VibeVoice: Expressive Podcast Generation with Next-Token Diffusion
- Non-Convex Federated Optimization under Cost-Aware Client Selection
- EditBench: Evaluating LLM Abilities to Perform Real-World Instructed Code Edits
- Multi-Domain Transferable Graph Gluing for Building Graph Foundation Models

## Source Depth

All five notes are abstract/metadata-only in the current local workspace. OpenReview remains the preferred source, and arXiv fallback should be retried for this ICLR oral range when access and rate limits clear.

## Shared Thesis

This batch is about matching method structure to the actual computational or deployment substrate: softmax attention has formal computational power under the right positional/CoT structure; podcast generation needs long-form conversational audio tokens; federated optimization needs cost-aware client selection; code-edit benchmarks need real user context; and graph foundation models need geometric multi-domain transfer.

The common pattern is substrate specificity. The relevant object is not an abstract model class alone, but the computation, modality, communication regime, workflow, or manifold on which it operates.

## Subthemes

### Formal sequence computation

The softmax transformer paper proves that length-generalizable CoT softmax transformers can be Turing-complete. Positional encoding is not cosmetic; it changes the computational class.

### Long-form conversational audio

VibeVoice uses ultra-low-frame-rate continuous speech tokens and next-token diffusion to generate long-form multi-speaker podcast audio with turn-taking and non-lexical cues.

### Federated optimization cost realism

The non-convex federated optimization paper argues that client-selection strategies must be priced explicitly. RG-SAGA uses similarity-aware variance reduction under a cost-aware model.

### Real-world code-edit evaluation

EditBench tests code editing as users actually invoke assistants: instructions plus code context, highlighted code, and cursor position. Context changes outcomes substantially.

### Geometric graph foundation models

GraphGlue frames multi-domain graph pretraining as gluing local graph geometries into a smoother global manifold. Transferability becomes a geometric consistency property.

## Cross-Batch Connections

Softmax Turing-completeness connects to masked diffusion reasoning, Rational Transductors, accessible sequence bounds, and transformer association dynamics.

VibeVoice connects to avatar cognitive simulation, Omni-Reward, and diffusion language/audio generation through long-form multimodal output.

Cost-aware federated optimization connects to MV-FGAD, SmartFed, SpineFL, and optimization-memory papers through realistic distributed constraints.

EditBench connects to WebDevJudge, Gaia2, CyberGym, MiniAppBench, and code-generation evaluation work through real workflow benchmarking.

GraphGlue connects to CoCo, MV-FGAD, LAMP, Relational Lottery Tickets, and foundation-model scaling work through representation geometry across graph domains.

## Emerging Pattern

The emerging pattern is that abstractions become useful only when they preserve the operational substrate: sequence computation, audio timing, client communication, developer context, or graph-domain geometry.
