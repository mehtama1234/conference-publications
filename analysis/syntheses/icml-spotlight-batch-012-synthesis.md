# ICML 2026 Spotlight Batch 012 Synthesis

Scope: ICML spotlight notes 56-60.

Source depth: full extracted arXiv text for SCALE, Harnessing Non-Adversarial Robustness, TetraJet-v2, and Robust Causal Discovery with Power-Laws; abstract/metadata only for Conditional Equivalence of DPO and RLHF because no confident local PDF match is available yet.

## Papers Covered

- SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models.
- Harnessing Non-Adversarial Robustness in Large Language Models.
- Conditional Equivalence of DPO and RLHF.
- TetraJet-v2: Accurate NVFP4 Training for Large Language Models.
- Robust Causal Discovery in Real-World Time Series with Power-Laws.

## Emerging Pattern 1: Internal Signals Are Becoming Deployment Controls

SCALE uses self-uncertainty from the VLA output distribution to control both perception and action at inference time. Harnessing Non-Adversarial Robustness uses perturbation-induced module-output shifts as a target for debiasing and certification. TetraJet-v2 diagnoses quantized training through weight oscillation and activation outliers.

The shared theme is that model internals are operational signals. They are not only for interpretation; they drive inference control, robustness repair, and numerical stabilization.

## Emerging Pattern 2: Robustness Is Being Split Into More Specific Failure Classes

The robustness paper explicitly targets non-adversarial semantically neutral prompt perturbations, distinct from jailbreaks or worst-case attacks. SCALE targets perceptual/action ambiguity in robot execution. TetraJet-v2 targets numerical instability from FP4 quantization.

This is a useful maturation: "robustness" is decomposing into prompt distribution robustness, embodied uncertainty, numerical stability, and alignment objective correctness, each with different tools.

## Emerging Pattern 3: Popular Alignment Objectives Are Getting Assumption Audits

The DPO/RLHF equivalence paper argues that DPO's equivalence to RLHF depends on a hidden condition. When it fails, DPO can decrease its loss while preferring dispreferred responses. This connects to Beyond Log Likelihood and VALUEFLOW: post-training objectives are no longer treated as universally valid recipes.

The deeper pattern is objective auditing. Alignment methods need explicit conditions under which their guarantees actually apply.

## Emerging Pattern 4: Low-Precision Training Has Its Own Dynamics

TetraJet-v2 shows that FP4 training failures are not just static quantization error. Weight oscillation is a temporal failure mode, and outliers persist across activations and steps. The solution combines quantization design, reset dynamics, outlier handling, and CUDA kernels.

This links to low-precision transformer failure analysis, LiftQuant, and quantized diffusion error propagation: efficiency gains now require understanding error dynamics over training or generation trajectories.

## Emerging Pattern 5: Spectral Structure Keeps Reappearing Across Domains

Robust Causal Discovery with Power-Laws uses local power-law spectral features to denoise time-series causal discovery. This connects to attention spectra, Jacobian spectra, effective span dimension, spectral-sphere optimization, and IRNO's spectral loss.

The corpus is showing spectra as a cross-domain tool: for generalization, optimization, numerical stability, physical systems, and now causal discovery.

## Cross-Batch Links

- SCALE links with BehaviorVLA, HDFlow, and MomaGraph through embodied systems that use intermediate structure for robust action.
- Non-adversarial robustness links with Pressure Reveals Character and Rare Event Analysis through more granular robustness/evaluation categories.
- Conditional DPO/RLHF links with Beyond Log Likelihood, VALUEFLOW, and DMPO through post-training objective theory.
- TetraJet-v2 links with low-precision transformer training, LiftQuant, and diffusion quantization through numerical ML systems.
- Power-law causal discovery links with LC-PB-SCM and Linear CRL through causal discovery under realistic data assumptions.

## Subthemes to Track

- VLA self-uncertainty.
- Adaptive visual attention.
- Prompt-perturbation debiasing.
- Robustness certificates.
- DPO failure conditions.
- Constrained preference optimization.
- NVFP4 fully quantized training.
- Weight oscillation suppression.
- Power-law spectral features.
- Robust time-series causal discovery.
