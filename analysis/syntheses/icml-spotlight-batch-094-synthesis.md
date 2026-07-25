# ICML 2026 Spotlight Batch 094 Synthesis

Papers covered: 00466-00470.

## Batch Thesis

This batch is about making powerful model changes trustworthy by aligning them with the right control or explanation structure. Conformal Policy Control calibrates exploration against a safe reference policy; RFCMH models noisy retrieval labels as fuzzy admissibility rather than binary truth; any-order GPT decouples diffusion language modeling from architecture; Generative Wasserstein Flows unify generative algorithms as distributional gradient flows; and temporal-graph explanation backtracks both topology and memory.

The common theme is calibrated transformation. Policies, labels, generation orders, distributions, and graph memories can all be changed or interpreted safely only when the transformation preserves the relevant uncertainty, geometry, or information pathway.

## Cross-Paper Themes

### 1. Safety Requires Calibrated Deviation From a Trusted Baseline

Conformal Policy Control uses a safe reference policy as a probabilistic regulator for a new optimized policy. RFCMH similarly avoids trusting or discarding noisy labels outright, instead calibrating admissible supervision.

Both papers reject all-or-nothing conservatism. The goal is controlled departure: explore or learn more without letting unreliable signals dominate.

### 2. Fair Comparisons Require Decoupling Confounds

Any-order GPT argues that AR and masked diffusion comparisons are confounded by architectural differences. Its decoder-only MDM setup controls architecture to isolate modeling paradigm.

This resonates with AlgoVeri, MiniAppBench, and performative-misalignment work: evaluation must remove confounds before conclusions about capability, safety, or efficiency are credible.

### 3. Generative Modeling Is Becoming Geometric

Any-order GPT studies generation order and architecture; GWF studies generative algorithms as Wasserstein gradient flows and JKO schemes. XDLM from the prior batches unifies discrete diffusion kernels.

Together these papers show a shift from model-family labels toward the geometry and dynamics of generation: ordering, flows, divergences, transport, and discretization.

### 4. Explanations Must Track Real Information Flow

The temporal-graph paper makes this precise: explaining a TGN requires backtracking the memory module as well as graph topology. Static neighbor explanations miss the historical events that created current memory states.

This connects to Assistant Axis, categorical ANOVA, and Verified SHAP: explanations are becoming architecture- and distribution-aware rather than generic post-hoc overlays.

## Deep Subthemes

### Conformal Policy Regulation

Safe exploration can start at deployment if an optimized policy is constrained by conformal calibration from safe-policy data. The declared risk tolerance becomes a user-facing control knob.

### Fuzzy Label Admissibility

Noisy labels in cross-modal retrieval are better represented by possibility and necessity than by hard filtering or uniform smoothing. This preserves data use while limiting false-positive supervision.

### Decoder-Only Masked Diffusion

Any-order GPT puts MDMs into GPT-style architecture, showing that diffusion and autoregression can be compared without changing the backbone family.

### JKO as Generative Template

Generative Wasserstein Flows turn distributional optimization into a unifying algorithmic template, covering f-divergences, IPMs, MMD, and links to GANs.

### Memory Backtracking

TGN explanations need to account for how past events alter node memories. Faithfulness follows the actual computational graph through time.

## Common Pattern

The batch's shared lesson is that trust depends on respecting the object's native structure. A policy has a risk envelope, a noisy label has graded admissibility, a language model has architecture/order confounds, a generator has distributional geometry, and a temporal graph model has memory pathways.
