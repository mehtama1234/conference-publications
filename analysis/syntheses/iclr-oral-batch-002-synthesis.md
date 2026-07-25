# ICLR 2026 Oral Batch 002 Synthesis

Scope: ICLR oral notes 9-13.

Source depth: abstracts for all five papers; full extracted text for CyberGym, Quotient-Space Diffusion, Visual Symbolic Mechanisms, and Frozen-PINN.

## Papers Covered

- CyberGym: Evaluating AI Agents' Real-World Cybersecurity Capabilities at Scale.
- Spherical Watermark: Encryption-Free, Lossless Watermarking for Diffusion Models.
- Quotient-Space Diffusion Model.
- Visual symbolic mechanisms: Emergent symbol processing in Vision Language Models.
- Fast training of accurate physics-informed neural networks without gradient descent.

## Emerging Pattern 1: Evaluation Is Becoming Executable Infrastructure

CyberGym is not a static benchmark. It asks agents to interact with real codebases and generate proof-of-concept tests that are executed against pre-patch and post-patch versions. This makes evaluation closer to an operational environment.

The deeper theme is that benchmarks are becoming infrastructure for discovery. CyberGym is both a measuring instrument and a security tool, producing zero-day and incomplete-patch findings.

## Emerging Pattern 2: Provenance Is a Distribution-Design Problem

Spherical Watermark embeds provenance directly into diffusion sampling noise while trying to preserve the Gaussian prior. This connects to ICML's Catch-22 watermarking paper: watermarking is fundamentally about the statistical relationship between generated and unwatermarked distributions.

The common pattern is that provenance mechanisms now need to satisfy multiple constraints at once:

- traceability;
- visual or textual quality;
- robustness to edits;
- statistical stealth;
- low operational overhead.

## Emerging Pattern 3: Scientific Generation Is Moving Into the Right Mathematical Space

Quotient-Space Diffusion changes the sample space to remove redundant symmetry degrees of freedom. Rather than only making a network equivariant, it models the intrinsic quotient space and then lifts the process back for practical sampling.

This is a strong example of structure-first generative modeling. The model is not merely exposed to more data; the mathematical object being generated is reformulated so the learning problem is easier and the sampler remains valid.

## Emerging Pattern 4: Interpretability Is Becoming Mechanistic Debugging

The VLM symbolic-mechanism paper identifies content-independent spatial position IDs and attention-head stages that support object binding. Crucially, it ties binding failures to interference during ID retrieval.

This complements prior notes on CompSLOT and The Tell-Tale Norm. Interpretability is becoming a way to identify the internal mechanism behind a failure, not only a post-hoc explanation for an output.

## Emerging Pattern 5: Scientific ML Is Challenging Default Training Assumptions

Frozen-PINN rejects the assumption that PINNs must be trained through gradient descent over a monolithic PDE/BC/IC loss. It uses frozen random spatial features, time-dependent coefficients, PDE-to-ODE reformulation, and causality-by-construction.

This aligns with DS-TS from ICML: scientific computing workloads are forcing changes at the solver and computation level, not just the model architecture level.

## Cross-Batch Links

- CyberGym and RAGEN-2 both show that agent evaluation needs process-aware diagnostics, not just final outcomes.
- Spherical Watermark and Catch-22 form a provenance pair: one constructs a diffusion watermark, the other characterizes fundamental watermarking tradeoffs.
- Quotient-Space Diffusion, PAR, and FlashWorld all point to structured generative modeling for physical or spatial objects.
- Visual Symbolic Mechanisms, CompSLOT, and The Tell-Tale Norm all treat intermediate representations as useful explanatory and control surfaces.
- Frozen-PINN and DS-TS both replace a default computational paradigm to escape scientific solver bottlenecks.

## Subthemes to Track

- Executable benchmarks.
- Agent cybersecurity and dual-use evaluation.
- Distribution-preserving watermarking.
- Quotient-space and symmetry-aware generation.
- Mechanistic VLM object binding.
- Gradient-free scientific neural solvers.
- Temporal causality as solver structure.

