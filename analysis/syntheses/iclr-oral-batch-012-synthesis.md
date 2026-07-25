# ICLR 2026 Oral Batch 012 Synthesis

## Papers

- Is it Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort
- FlashVID: Efficient Video Large Language Models via Training-free Tree-based Spatiotemporal Token Merging
- Exchangeability of GNN Representations with Applications to Graph Retrieval
- WAFT: Warping-Alone Field Transforms for Optical Flow
- WSM: Decay-Free Learning Rate Schedule via Checkpoint Merging for LLM Pre-training

## Source Depth

All five notes are abstract/metadata-only in the current local workspace. OpenReview remains the preferred source, and arXiv fallback should be retried for this ICLR oral range when access and rate limits clear.

## Shared Thesis

This batch is about detecting or exploiting hidden shortcuts: reward hackers pass verifiers with too little reasoning; video LLMs waste tokens on spatiotemporal redundancy; GNN embeddings hide exchangeable symmetry; optical flow may not need cost volumes; and learning-rate decay can be emulated by checkpoint merging.

The common pattern is that efficiency and oversight improve when an implicit structure is made measurable: reasoning effort, token redundancy, embedding exchangeability, warping sufficiency, or checkpoint trajectory geometry.

## Subthemes

### Reasoning effort as safety signal

TRACE detects implicit reward hacking by truncating CoT and measuring how quickly a verifier can be passed. Suspiciously low effort becomes an unsupervised shortcut indicator.

### Training-free video compression

FlashVID treats video redundancy as spatiotemporal, not separately spatial and temporal. Token selection and tree-based merging preserve performance with only a small fraction of tokens.

### Exchangeability for graph retrieval

The GNN exchangeability paper finds coordinate permutation symmetry in learned node embeddings. This supports order-statistic reductions and efficient LSH for graph similarity.

### Warping without cost volumes

WAFT challenges optical-flow convention by replacing cost volumes with high-resolution warping. The result is a simpler, faster, high-performing dense correspondence architecture.

### Checkpoint merging as schedule

WSM reframes LR decay as model averaging across a training window. Merge duration becomes the key schedule parameter.

## Cross-Batch Connections

TRACE connects to Obfuscation Atlas, CRV, ASAG, and reward-hacking papers through process diagnostics.

FlashVID connects to EntroKV, ThinkV, EcoVLA, and video-understanding work through adaptive token compression.

GNN exchangeability connects to InfoNCE Gaussianity, GraphGlue, CoCo, and embedding geometry papers through probabilistic structure in learned representations.

WAFT connects to FFDP, IO-aware GNNs, and systems-efficiency papers through removing expensive intermediate constructs.

WSM connects to Self-Soupervision, model soups, LoRA-Pre, and optimizer-scaling papers through parameter-space averaging and training trajectory control.

## Emerging Pattern

The broader pattern is hidden-structure leverage. The batch shows that safety, efficiency, retrieval, perception, and optimization all benefit from identifying what can be removed, compressed, reordered, or averaged without losing the core signal.
