# ICLR 2026 Oral Batch 008 Synthesis

## Papers

- Task-free Adaptive Meta Black-box Optimization
- On the Reasoning Abilities of Masked Diffusion Language Models
- TRACE: Your Diffusion Model is Secretly an Instance Edge Detector
- InfoNCE Induces Gaussian Distribution
- WebDevJudge: Evaluating (M)LLMs as Critiques for Web Development Quality

## Source Depth

All five notes are abstract/metadata-only in the current local workspace. OpenReview remains the preferred source, and arXiv fallback should be retried for this ICLR oral range when access and rate limits clear.

## Shared Thesis

This batch is about hidden structure becoming usable: target-task populations train black-box optimizers online; masked diffusion language models hide parallel reasoning power; diffusion attention hides instance-edge signals; InfoNCE embeddings hide Gaussian geometry; and web-development judges hide large gaps behind fluent critiques.

The common pattern is diagnostic extraction. Each paper asks what can be inferred from an internal process or evaluation surface that standard usage would leave implicit.

## Subthemes

### Online optimizer adaptation

ABOM removes handcrafted meta-training tasks by turning optimization populations into the data used to adapt evolutionary operators. The optimizer learns while searching.

### Parallel diffusion reasoning

The masked diffusion language-model paper places MDMs in a formal reasoning hierarchy with CoT and padded looped transformers. It argues that parallel denoising can be an efficient reasoning substrate.

### Diffusion internals as labels

TRACE mines diffusion self-attention for instance boundary cues and distills them into a fast edge decoder. The diffusion model becomes a scalable annotation source.

### Gaussian contrastive geometry

The InfoNCE paper gives a probabilistic model for contrastive representations, arguing they approach multivariate Gaussian distributions under high-dimensional conditions.

### Judge reliability in web tasks

WebDevJudge shows that LLM/MLLM judges still miss functional equivalence, feasibility, and bias issues in web development. Evaluation quality requires interactive and expert-aligned checks.

## Cross-Batch Connections

ABOM connects to optimizer-state and RL adaptation papers such as LoRA-Pre, SGD RLVR, Beyond Muon, and JitRL.

Masked diffusion reasoning connects to XDLM, PonderLM-2, ASAG, Ctrl-R, and transformer expressivity papers through alternative computation structures for reasoning.

TRACE connects to DAVE, Motion Attribution, Information Flow, and Self-Soupervision because hidden internal signals become supervision or explanation.

InfoNCE Gaussianity connects to embedding collapse, Gaussian single-index learning, contrastive difficult-example theory, and phase-retrieval scaling.

WebDevJudge connects to FRABench/UFEval, CounselBench, Gaia2, MiniAppBench, and Copyright-Bench through the theme of evaluating evaluators under realistic workflows.

## Emerging Pattern

The broader pattern is that latent process structure is increasingly treated as an asset. Search populations, denoising steps, attention maps, embedding distributions, and judge failures become measurable objects that can be optimized, distilled, or governed.
