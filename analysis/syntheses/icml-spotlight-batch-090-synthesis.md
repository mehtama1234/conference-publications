# ICML 2026 Spotlight Batch 090 Synthesis

Papers covered: 00446-00450.

## Batch Thesis

This batch shows that once models become active systems, static evaluation and static execution are insufficient. LLMs can develop novel social biases through adaptive exploration; non-Euclidean gradient methods need geometry-aware edge-of-stability diagnostics; PoLar changes the layer execution program at inference time; FIDIA aligns protein sequence training with Best-of-N selection; and MiniAppBench evaluates interactive HTML artifacts through browser automation.

The common pattern is that the important behavior emerges from how the system is run: exploration history, optimizer geometry, layer schedule, inference selection protocol, or browser interaction.

## Cross-Paper Themes

### 1. Deployment Turns Models Into Processes

The social-bias paper is the clearest example: bias can emerge after deployment through adaptive exploration, even for artificial groups with no inherent differences. JitRL from the previous batch makes this operationally attractive, but this paper shows why adaptive systems require dynamic fairness audits.

MiniAppBench similarly treats generated outputs as runtime artifacts. A MiniApp is not correct because its code looks plausible; it must behave correctly under interaction.

### 2. Inference-Time Control Is a New Capability Surface

PoLar shows that pretrained layers can be skipped or looped to form input-specific programs, unlocking computations outside the standard fixed forward pass. FIDIA optimizes for the Best-of-N inference protocol, where the selected sample, not the average sample, defines success.

This aligns with DHSA, TabSwift, JitRL, PLAINTAIN, and STAR-KV: inference is increasingly programmable, adaptive, and explicitly optimized.

### 3. Evaluation Must Match the Operational Protocol

FIDIA's main claim depends on aligning training with Best-of-N inference. MiniAppBench's benchmark depends on evaluating dynamic interaction rather than static output. The social-bias paper depends on repeated allocation behavior rather than one-shot stereotype probes.

Across the batch, a model evaluated under the wrong protocol can look safer, smarter, or more useful than it is.

### 4. Geometry and Dynamics Explain Empirical Regularities

The non-Euclidean edge-of-stability paper generalizes sharpness diagnostics to the geometry of the optimizer. This matches a broader theoretical thread: scaling laws, stochastic Transformer clustering, reasoning loops, and optimization stability all require modeling the underlying dynamics.

## Deep Subthemes

### Adaptive Bias Formation

Bias mitigation cannot stop at removing known stereotypes. Models may form novel group-level biases through under-exploration, especially when they are asked to allocate real opportunities.

### Geometry-Aware Optimization Diagnostics

Edge of stability should be measured in the geometry induced by the update rule. This reframes sharpness as optimizer-relative rather than a single Euclidean property.

### Programmable Layer Execution

PoLar treats a pretrained Transformer as a module library. Skipping and looping layers can improve accuracy and reduce computation, suggesting that fixed-depth inference underuses latent model capacity.

### Best-of-N Alignment for Scientific Generation

FIDIA highlights a general principle: if deployment selects the best candidate from a set, training should optimize the expected selected maximum rather than average likelihood.

### Runtime Evaluation for Generated Apps

MiniAppBench makes interaction part of the benchmark. Browser automation becomes necessary because static correctness misses state transitions, user intent, and dynamic behavior.

## Common Pattern

The shared design lesson is protocol fidelity. The model's true behavior is defined by the full protocol around it: exploration policy, optimizer, execution program, candidate selection, or runtime interaction. ICML 2026 repeatedly shows that better systems come from aligning training, inference, and evaluation with that protocol.
