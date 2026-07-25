# ICLR 2026 Oral Batch 006 Synthesis

## Papers

- From movement to cognitive maps: recurrent neural networks reveal how locomotor development shapes hippocampal spatial coding
- A Scalable Distributed Framework for Multimodal GigaVoxel Image Registration
- Omni-Reward: Towards Generalist Omni-Modal Reward Modeling with Free-Form Preferences
- Taming Momentum: Rethinking Optimizer States Through Low-Rank Approximation
- Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments

## Source Depth

All five notes are abstract/metadata-only in the current local workspace. OpenReview remains the preferred source, and arXiv fallback should be retried for this ICLR oral range when access and rate limits clear.

## Shared Thesis

This batch is about scaling evaluation, representation, and infrastructure to match real deployment structure. Spatial maps emerge from embodied developmental movement; gigavoxel registration needs non-GEMM distributed systems; reward models must cover free-form preferences across modalities; optimizer states can be compressed by exploiting low-rank structure; and agents need asynchronous dynamic benchmarks.

The common pattern is that modern ML systems fail when their assumptions are too narrow: passive sensory exposure, single-GPU registration, text/image-only rewards, dense optimizer state, or static agent environments.

## Subthemes

### Embodied developmental representation

The hippocampal RNN paper shows that changing locomotor statistics can drive the emergence of spatially tuned units. The developmental distribution of action matters, not just sensory prediction.

### Scientific systems at native scale

FFDP demonstrates that biomedical inverse problems require systems work below the model level. IO-aware non-GEMM kernels and convolution-aware sharding make native-resolution human-brain registration feasible.

### Omni-modal reward modeling

Omni-Reward expands alignment infrastructure from fixed text/image pair preferences to free-form preferences across text, image, video, audio, and 3D.

### Low-rank optimizer state

LoRA-Pre reframes momentum as online linear learning and compresses it into a low-rank subspace. This extends low-rank thinking from model adaptation to optimizer memory.

### Asynchronous agent evaluation

Gaia2 moves agent evaluation toward dynamic environments that evolve independently of agent actions. Its write-action verifiers make these scenarios suitable for RLVR-style training.

## Cross-Batch Connections

The hippocampal RNN paper connects to PRISM, temporal superposition, GLANCE, and ICML linear recurrent memory through embodied and recurrent representation formation.

FFDP connects to ICML IO-aware GNNs, EntroKV, and scientific computing papers through bottleneck-aware systems design.

Omni-Reward connects to RACO, FRABench/UFEval, CounselBench, and multimodal alignment papers through richer preference and evaluation targets.

LoRA-Pre connects to Beyond Muon, SGD RLVR, Adam degeneracy, and efficient adaptation work through optimizer-state geometry.

Gaia2 connects to CyberGym, MiniAppBench, GLANCE, and RLVR papers because verifiable dynamic environments are becoming the training and evaluation substrate for agents.

## Emerging Pattern

The broader pattern is structural realism. Methods become more useful when they reflect the actual structure of experience, data scale, preference expression, optimizer memory, or deployment environments.
