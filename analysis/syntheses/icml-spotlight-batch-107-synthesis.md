# ICML 2026 Spotlight Batch 107 Synthesis

## Papers

- Motion Attribution for Video Generation
- Stop When Further Reasoning Won't Help: Attention-State Adaptive Generation in Reasoning Models
- What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity
- Initialization is Half the Battle: Generating Diverse Images from a Guidance Potential Posterior
- Diffusion Flow Matching: Dimension-Improved KL Bounds and Wasserstein Guarantees

## Source Depth

All five notes are abstract/metadata-only. arXiv acquisition remains deferred after repeated 429/503 failures across preceding exact-batch attempts. Full-paper details should be verified later from official PDFs or high-confidence arXiv matches.

## Shared Thesis

This batch is about controlling generative and reasoning processes at the right intervention point. Motive controls video motion through data attribution; ASAG controls reasoning length through attention state; GLANCE controls exploration through visual-linguistic prediction error; DivIn controls diversity through initialization; and DFM theory controls reliability through discretization bounds.

The common pattern is targeted process control. The papers do not merely optimize final outputs; they identify where in the pipeline a specific failure begins: fine-tuning data for motion, redundant reasoning continuation, passive exploration, mode-collapsing initial noise, or finite-step flow approximation.

## Subthemes

### Data attribution for motion

Motive separates motion influence from static appearance. This is important because video quality failures often live in dynamics: smoothness, physical plausibility, and temporal consistency. Motion-specific attribution turns data curation into a control lever.

### Attention-state stopping

ASAG treats attention distributions as evidence of reasoning state. Its core idea is that test-time compute should be adaptive: longer chain-of-thought is useful only while it improves the solution. Past that point, overthinking wastes tokens and can reduce accuracy.

### Curiosity from cross-modal mismatch

GLANCE uses disagreement between linguistic prediction and visual reality as intrinsic reward. This turns exploration into world-model repair: the agent seeks states where what it thinks and what it sees diverge.

### Initialization as diversity control

DivIn argues that diversity can be lost before the denoising path starts. Sampling initial noise from a guidance-potential posterior steers generation away from dominant-mode basins while remaining compatible with trajectory interventions.

### Convergence guarantees for flow generation

The DFM theory paper supplies a reliability layer for diffusion flow matching. Improved KL and Wasserstein bounds make the discretization behavior of Brownian-motion DFMs more understandable in high-dimensional settings.

## Cross-Batch Connections

Motive connects to DAVE, NASH, and Self-Soupervision through attribution and data curation. It also connects to PanoWorld-X and VectorWorld through generated motion quality.

ASAG connects to PonderLM-2, Ctrl-R, H1, and reasoning dimensionality. Together these papers define a spectrum of reasoning compute control: add latent steps, guide trajectories, or stop visible thought.

GLANCE connects to Learning-to-Theorize, POPGym, linear recurrent memory, and VectorWorld through partial observability and active world-model improvement.

DivIn connects to Reverse Flow Matching, AGSM, GoodDiffusion, and PanoWorld-X as another inference-time control mechanism for generative models.

DFM convergence connects to Reverse Flow Matching, diffusion RL policies, and theoretical optimization papers because diffusion/flow models are becoming infrastructure for sampling, control, and simulation.

## Emerging Pattern

The larger pattern is intervention-point specificity. Robust improvement requires locating the stage that causes the failure, then intervening there: data, attention state, exploration reward, initial noise, or discretization.
