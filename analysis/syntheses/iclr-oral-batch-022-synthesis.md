# ICLR Oral Batch 022 Synthesis

## Papers Covered

- Let Features Decide Their Own Solvers: Hybrid Feature Caching for Diffusion Transformers
- DiffusionNFT: Online Diffusion Reinforcement with Forward Process
- LLMs Get Lost In Multi-Turn Conversation
- Mastering Sparse CUDA Generation through Pretrained Models and Deep Reinforcement Learning
- Reasoning with Sampling: Your Base Model is Smarter Than You Think

## Shared Thesis

This batch is about controlling expensive generation and interaction without assuming uniform behavior. HyCa assigns feature dimensions their own caching strategies. DiffusionNFT moves diffusion RL to the forward process to avoid likelihood and solver constraints. The multi-turn conversation paper shows that conversational state can derail models after early assumptions. SparseRL uses RL and sparse-structure inputs to generate fast CUDA kernels. Reasoning with Sampling elicits base-model reasoning through MCMC-style inference-time search. The common pattern is that better behavior comes from controlling the process around the model: feature reuse, reward fine-tuning path, conversation state, code-performance reward, or sampler dynamics.

## Deep Themes

### Fine-Grained Inference Efficiency

HyCa and ThinKV point in the same direction: internal features and tokens do not all deserve the same compute or memory. HyCa applies this to diffusion transformer hidden dimensions, while ThinKV applies it to reasoning-model KV caches. Both show that near-lossless acceleration increasingly depends on internal heterogeneity.

### Post-Training Beyond LLMs

DiffusionNFT extends RL-style reward optimization to diffusion models by reformulating it through forward-process flow matching. This is part of a broader shift from RLHF as an LLM-specific recipe toward reward-guided adaptation for different generative model families.

### Process Failures in Interaction

The multi-turn conversation paper identifies a key deployed-assistant failure: models make early assumptions and then fail to recover. This complements agent benchmarks that test planning, retrieval, and environment interaction. The main issue is not static aptitude, but error accumulation over conversational state.

### Program Synthesis as Systems Optimization

SparseRL pushes code generation beyond correctness into hardware performance. Sparse matrix structure becomes part of the prompt/input, and hierarchical rewards gate speed by correctness. This links code-generation research with compiler, kernel, and high-performance computing concerns.

### Sampling as Latent Capability Extraction

Reasoning with Sampling argues that base models may contain more reasoning ability than direct decoding reveals. MCMC-style sampling can expose this capability without RL, verifiers, or new data. This complicates claims that post-training creates all reasoning behavior.

## Cross-Paper Pattern

The shared pattern is process-level leverage. The papers improve outputs by changing how computation unfolds: feature dimensions choose solvers, diffusion rewards enter through forward training, conversations require recoverable state, CUDA generation optimizes against runtime, and reasoning improves through iterative sampling. The model weights are only one part of the system; process control is often the capability multiplier.

## Subthemes to Track

- Dimension-wise diffusion transformer caching.
- Forward-process reward fine-tuning for diffusion models.
- Multi-turn conversational unreliability.
- RL-generated sparse CUDA kernels.
- MCMC-style base-model reasoning.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Algorithmic details, empirical protocols, and formal guarantees should be upgraded after PDFs are available.
