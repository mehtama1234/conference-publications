# FlashSketch: Sketch-Kernel Co-Design for Fast Sparse Sketching on GPUs

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: cCwxV6rSXF
- Authors: Rajat Vadiraj Dwaraknath; Sungyoon Kim; Mert Pilanci
- Primary area: general_machine_learning->scalable_algorithms
- Keywords: Randomized Numerical Linear Algebra;CUDA Kernels;Co-Design;Matrix Sketching;Sparse Johnson-Lindenstrauss Transform;Block permutationsGPU Acceleration
- Source URL: https://openreview.net/forum?id=cCwxV6rSXF
- PDF URL: https://openreview.net/pdf?id=cCwxV6rSXF

## Abstract

Sparse sketches such as the sparse Johnson–Lindenstrauss transform are a core primitive in randomized numerical linear algebra because they leverage random sparsity to reduce the arithmetic cost of sketching, while still offering strong approximation guarantees. Their random sparsity, however, is at odds with efficient implementations on modern GPUs, since it leads to irregular memory access patterns that degrade memory bandwidth utilization. Motivated by this tension, we pursue a sketch–kernel co-design approach: we design a new family of sparse sketches, BlockPerm-SJLT, whose sparsity structure is chosen to enable FlashSketch, a corresponding optimized CUDA kernel that implements these sketches efficiently. The design of BlockPerm-SJLT introduces a tunable parameter that explicitly trades off the tension between GPU-efficiency and sketching robustness. We provide theoretical guarantees for BlockPerm-SJLT under the oblivious subspace embedding (OSE) framework, and also analyze the effect of the tunable parameter on sketching quality. We empirically evaluate FlashSketch on standard RandNLA benchmarks, as well as an end-to-end ML data attribution pipeline called GraSS. FlashSketch pushes the Pareto frontier of sketching quality versus speed, across a range of regimes and tasks, and achieves a global geomean speedup of roughly $1.7 \times$ over the prior state-of-the-art GPU sketches.

## One-Sentence Claim

FlashSketch co-designs sparse Johnson-Lindenstrauss sketches and CUDA kernels so randomized linear algebra gets both approximation guarantees and GPU-efficient memory access.

## Problem

Sparse sketches reduce arithmetic cost in randomized numerical linear algebra, but random sparsity creates irregular memory accesses that underutilize GPU bandwidth. The mathematical sketch that is best for robustness may be poor for modern accelerators.

The paper asks how to design sketch distributions and kernels together rather than treating implementation as an afterthought.

## Core Contribution

The paper introduces BlockPerm-SJLT, a new sparse sketch family whose sparsity pattern is chosen for GPU efficiency, and FlashSketch, an optimized CUDA kernel for it. A tunable parameter explicitly trades off sketching robustness and GPU efficiency.

The authors provide oblivious subspace embedding guarantees and analyze how the parameter affects sketch quality. Empirically, FlashSketch improves the quality-speed Pareto frontier and gives about 1.7x global geomean speedup over prior GPU sketches.

## Method

BlockPerm-SJLT structures sparsity with block permutations so memory accesses become more regular. FlashSketch implements that structure directly in a CUDA kernel.

The theoretical side proves OSE-style approximation guarantees despite the hardware-friendly sparsity pattern, while experiments test standard RandNLA tasks and an ML data-attribution pipeline.

## Experiments and Evidence

Evidence reported in the abstract:

- New BlockPerm-SJLT sketch family.
- CUDA kernel co-designed with sketch sparsity.
- OSE theoretical guarantees.
- Analysis of the robustness-efficiency tuning parameter.
- Standard randomized numerical linear algebra benchmarks.
- End-to-end GraSS data attribution pipeline.
- Roughly 1.7x global geomean speedup over prior GPU sketches.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: matrix regimes, GPU models, OSE constants, and GraSS attribution quality impact.

## Limits and Failure Modes

- Structured sparsity may reduce robustness in regimes not covered by the chosen parameter.
- Speedups are GPU- and workload-dependent.
- Kernel maintenance may be required as accelerator architectures evolve.
- Sketching quality tradeoffs need task-level validation, not only projection error.

## Deep Themes

**Randomized algorithms need hardware-aware randomness.** Sparsity patterns are chosen for both theory and memory access.

**Approximation guarantees and kernels can be co-designed.** FlashSketch preserves OSE-style guarantees while changing implementation structure.

**Data attribution depends on scalable linear algebra.** Faster sketches make downstream attribution pipelines more practical.

## Subthemes

- Sparse Johnson-Lindenstrauss transforms.
- Block-permutation sparsity.
- CUDA sketch kernels.
- OSE guarantees.
- RandNLA for data attribution.

## Connections to Other Papers

Connects to FlashSinkhorn, MACKO-SpMV, WBMM, and FlashOptim through hardware-aware algorithm design. It also links to MDA and data attribution papers because scalable sketching supports mechanistic/data influence analysis.

## Notes for Cross-Paper Synthesis

FlashSketch adds another example where the mathematical primitive is redesigned so its structure matches accelerator memory behavior without dropping guarantees.
