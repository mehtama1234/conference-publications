# ICLR Oral Batch 029 Synthesis

## Papers Covered

- Pre-training under Infinite Compute
- Multimodal Aligned Semantic Knowledge for Unpaired Image-text Matching
- Monocular Normal Estimation via Shading Sequence Estimation
- In-Place Test-Time Training
- Revela: Dense Retriever Learning via Language Modeling

## Shared Thesis

This batch is about extracting more value from constrained signals. Infinite-compute pretraining reuses fixed data with stronger regularization, ensembling, and distillation. MASK aligns image and text without pairs by using semantic prototypes. RoSE replaces direct normal prediction with shading-sequence estimation. In-Place TTT adapts fast weights from inference context. Revela trains retrievers without query-document labels by making retrieval help next-token prediction. The shared idea is to turn weak, scarce, or indirect signals into useful supervision by choosing the right intermediate structure.

## Deep Themes

### Data-Constrained Pretraining

Pre-training under infinite compute asks what happens when data, not compute, is scarce. Stronger regularization, ensembling, and distillation become ways to extract more from fixed text. This complements curriculum work: both papers show that data value depends on training dynamics.

### Prototype and Proxy Supervision

MASK and RoSE both introduce intermediate proxy structures. MASK uses word-derived prototypes for unpaired image-text matching, including OOD words. RoSE predicts shading sequences before solving for normals. In both cases, the proxy makes the target problem better conditioned.

### Test-Time Weight Adaptation

In-Place TTT pushes beyond static inference by updating fast weights inside normal LLM architecture. This is a different axis from retrieval or sampling: the model parameters themselves adapt to the current context stream.

### Self-Supervised Retrieval

Revela reframes dense retriever training as language modeling over cross-document dependencies. This is important because specialized and reasoning-heavy domains often lack labeled retrieval pairs. It turns next-token prediction into supervision for information access.

## Cross-Paper Pattern

The common pattern is indirect supervision made operational. Reused text, word embeddings, shading sequences, context chunks, and cross-document dependencies all become training signals once the right objective exposes their relevance. The broader theme is that useful learning increasingly comes from designing intermediate tasks that better match the hidden structure of the target capability.

## Subthemes to Track

- Data-constrained compute-rich pretraining.
- OOD prototype alignment for image-text matching.
- Shading-sequence proxy for normal estimation.
- In-place LLM test-time training.
- Language-modeling-based dense retrieval.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Details should be upgraded when PDFs are available.
