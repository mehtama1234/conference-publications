# ICLR Oral Batch 016 Synthesis

## Papers Covered

- Actions Speak Louder than Prompts: A Large-Scale Study of LLMs for Graph Inference
- WAVE: Learning Unified & Versatile Audio-Visual Embeddings with Multimodal LLM
- Exploratory Causal Inference in SAEnce
- Coupling Experts and Routers in Mixture-of-Experts via an Auxiliary Loss
- One for Two: A Unified Framework for Imbalanced Graph Classification via Dynamic Balanced Prototype

## Shared Thesis

This batch is about representation interfaces: how models expose, align, or repair the intermediate structures they rely on. LLM graph inference improves when the interface shifts from prompts to executable actions. WAVE makes embeddings prompt-aware and any-to-any across text, audio, and video. Neural Effect Search turns sparse autoencoder features into causal discovery units. ERC loss couples MoE router geometry to expert capabilities. UniImb repairs graph representations under class and topological imbalance. Across these papers, progress comes from better control over the representation layer between raw data and downstream decisions.

## Deep Themes

### Interfaces Determine Effective Capability

The graph-inference study shows that prompting is not the only or even best way to expose LLM ability on structured data. Code generation and tool use let the model act over graph structure when prompt context becomes a bottleneck. This connects to agentic and systems papers: models often need the right action surface before their latent capability becomes useful.

### Conditional and Task-Aware Representation Spaces

WAVE and ERC both make representation spaces conditional. WAVE conditions embeddings on prompts so retrieval can adapt to user intent across modalities. ERC conditions sparse MoE computation by aligning router centers with expert capability. In both cases, static embeddings or routers are insufficient; the representation must reflect the task or the module it will activate.

### Interpretability as Scientific Instrumentation

Neural Effect Search is notable because it uses sparse autoencoder features not only to explain models, but to search for causal effects in scientific trials. This extends the interpretability theme from model diagnostics into scientific measurement: representations become candidate variables for empirical discovery.

### Balanced Geometry for Graph Learning

UniImb treats class imbalance and topological imbalance as representation-geometry problems. Its dynamic balanced prototypes counter majority dominance, while personalized perturbations diversify graph structure. This complements the graph-inference paper by showing that graph learning failures may come from both model interface and training-distribution geometry.

## Cross-Paper Pattern

The common pattern is that downstream behavior depends on intermediate alignment. Tokens must align with graph actions, prompts with multimodal embeddings, sparse features with causal effects, router rows with expert skills, and graph prototypes with balanced sample influence. These papers make hidden intermediate spaces more explicit and controllable.

## Subthemes to Track

- LLM interaction modes for structured graph tasks.
- Prompt-aware multimodal embeddings.
- Sparse autoencoders for exploratory causal inference.
- Router-expert coupling in sparse LLMs.
- Dynamic prototypes for imbalanced graph classification.

## Confidence and Source Depth

These notes are based on abstracts and local conference metadata. Implementation-level claims should be upgraded after official PDFs or high-confidence arXiv PDFs are available.
