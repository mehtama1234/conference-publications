# Initial Deep Theme Map

Scope: accepted ICML 2026 and ICLR 2026 records from local metadata manifests.

Status: preliminary. This is based on titles, abstracts, keywords, areas, and acceptance labels. It should be treated as a hypothesis map for the paper-by-paper reading pass.

## Corpus Shape

- ICLR 2026 accepted records: 5,343.
- ICML 2026 accepted records: 6,341.
- Combined accepted-publication metadata corpus: 11,684 records.
- ICLR accepted statuses in the local metadata: 5,120 Poster, 223 Oral.
- ICML accepted statuses in the local metadata: 5,805 Poster, 536 Spotlight.

The strongest visible macro-pattern is that both conferences are now heavily organized around foundation models, LLMs, multimodal models, generative models, evaluation, and applied scientific/robotic settings. Traditional ML concerns such as learning theory, optimization, uncertainty, causal reasoning, representation learning, and reinforcement learning remain active, but they frequently appear as infrastructure for larger systems rather than isolated topics.

## Theme 1: Inference Becomes a Compute Budget, Not a Single Forward Pass

Matched accepted records in first-pass query: 3,915.

The corpus shows a large shift toward treating inference as an active computational process. Papers are not only asking how to train better models; they are asking how to spend test-time compute through search, verification, branching, refinement, retrieval, debate, or adaptive decoding.

Subthemes:

- Test-time scaling for reasoning, coding, math, and synthesis.
- Verification loops that compare expected evidence against generated evidence.
- Search over generation trajectories, including tree search, stepwise refinement, and self-correction.
- Adaptive inference policies that vary computation by input difficulty.
- Reasoning benchmarks that stress long context, distractors, compositionality, or verifiability.

Representative metadata examples:

- `UnMaskFork: Test-Time Scaling for Masked Diffusion via Deterministic Action Branching` in ICML.
- `THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning` in ICLR.
- `Semantic-Aware Diffusion LLM Inference With Adaptive Block Size` in ICLR.
- `VERINA: Benchmarking Verifiable Code Generation` in ICLR.

Deeper hypothesis: the field is moving from model-centric intelligence to process-centric intelligence. The quality of an answer increasingly depends on the inference procedure around the model: search, verification, memory, tool calls, and compute allocation.

## Theme 2: Foundation Models Become Research Substrate

Across both conferences, LLM/foundation-model areas and keywords dominate: ICML lists `deep_learning->large_language_models` as the largest primary area, while ICLR's largest accepted area is `foundation or frontier models, including LLMs`.

Subthemes:

- LLMs as task solvers.
- LLMs as optimizers, planners, formalizers, and scientific assistants.
- LLMs as evaluators and data generators.
- LLM internals as objects of mechanistic study.
- LLM limitations as drivers of new benchmarks.

Deeper hypothesis: many papers are no longer introducing a standalone learner for a narrow task. They are building scaffolds around frontier models, measuring where those scaffolds fail, and proposing interventions at the levels of data, prompting, decoding, alignment, retrieval, or architecture.

## Theme 3: Evaluation Is Becoming a First-Class Research Object

Matched accepted records in first-pass query: 6,472.

Evaluation/benchmarking is one of the largest cross-cutting patterns. The benchmark papers are not just leaderboard construction; many are probing whether models possess verifiable reasoning, spatial understanding, grounded synthesis, robustness under distribution shift, fairness under sparsity, or reliable long-form generation.

Subthemes:

- Verifiable code, math, and formal reasoning.
- Multimodal diagnostic benchmarks.
- Agent and tool-use benchmarks.
- Safety and adversarial evaluations.
- Domain-specific benchmarks in science, medicine, robotics, and climate.
- Evaluation of process, not just answer accuracy.

Deeper hypothesis: the benchmark wave reflects a measurement crisis. As model outputs become fluent and multi-step, superficial accuracy is less trusted; the field is building stress tests for mechanism, robustness, grounding, and process validity.

## Theme 4: Data Quality and Synthetic Data Become Control Surfaces

Matched accepted records in first-pass query: 6,280.

The metadata shows broad attention to datasets, synthetic data, curation, annotation, filtering, and data sufficiency. This is not merely about more data; it is about targeted data that induces desired behavior or reveals failure.

Subthemes:

- Synthetic benchmarks with tunable difficulty.
- Data-only tests for retraining after drift.
- Dataset curation for reasoning, multimodal grounding, and scientific domains.
- Data selection and core-set methods for expensive evaluation.
- Annotation and feedback pipelines for alignment and preference learning.

Deeper hypothesis: data is being treated as an intervention mechanism. Researchers are using data construction to shape capabilities, expose limitations, and control downstream behavior more directly than architecture changes alone.

## Theme 5: Multimodal Models Shift Toward Grounded, Spatial, and Temporal Reasoning

Matched accepted records in first-pass query: 2,918.

Vision-language and multimodal work appears less centered on simple image-text matching and more on reasoning over video, spatial layouts, documents, surgical scenes, world models, live photos, and visual generation diagnostics.

Subthemes:

- Spatial mental models in VLMs.
- Video and long-horizon visual generation.
- Document understanding with multimodal agents.
- Medical and surgical visual understanding.
- Grounded image reasoning for diagnosing text-to-image generation.

Deeper hypothesis: multimodal research is moving from recognition to situated reasoning. The target capability is not just seeing objects; it is maintaining structured beliefs about scenes, time, intent, and physical or semantic constraints.

## Theme 6: Generative Modeling Expands Beyond Image Synthesis

Matched accepted records in first-pass query: 2,440.

Diffusion, flow matching, and related generative methods remain highly visible, but the application surface is broader: language inference, video, 3D shapes, climate data, combinatorial optimization, reward modeling, and controlled editing.

Subthemes:

- Diffusion and flow matching as general-purpose modeling tools.
- Efficient generation through latent spaces, adapters, pruning, or adaptive blocks.
- Preference optimization for generative systems.
- Domain-specific generative modeling in climate, science, and physical systems.
- Editing and control as central capabilities.

Deeper hypothesis: generative modeling is becoming a general algorithmic family rather than a media-specific technology. The same ideas are being reinterpreted for structured optimization, scientific simulation, reward learning, and language-model inference.

## Theme 7: Robustness, Safety, Privacy, and Unlearning Are Converging

Matched accepted records in first-pass query: 3,192 for safety/robustness/adversarial behavior and 2,539 for privacy/federated/security in the broader public-record scaffold.

Safety-related work spans adversarial behavior, jailbreaks, fairness, privacy, certified unlearning, hallucination rejection, and robust uncertainty. These topics are often coupled with LLMs, diffusion models, VLMs, and deployment-sensitive domains.

Subthemes:

- Certified unlearning and privacy-preserving updates.
- Adversarial generation and exploit discovery.
- Fairness and bias in large models.
- Hallucination rejection and reliability for long-form outputs.
- Robustness under distribution shift and sparse feedback.

Deeper hypothesis: the line between safety, privacy, robustness, and alignment is blurring. They increasingly share mechanisms: audits, verification, preference constraints, adversarial data, uncertainty estimates, and post-training interventions.

## Theme 8: Efficiency Is Now a Capability Enabler

Matched accepted records in first-pass query: 4,933.

Efficiency is not only compression for deployment; it enables longer contexts, more test-time search, personalized models, diffusion inference, robotics, and large-scale evaluation. The efficiency theme cuts across pruning, quantization, adapters, sparse attention, distillation, and data selection.

Subthemes:

- LLM layer pruning and sparsity.
- Quantized attention and efficient serving.
- Adapter and LoRA transfer.
- Efficient diffusion inference.
- Efficient benchmark and evaluation pipelines.
- Compute-aware test-time scaling.

Deeper hypothesis: compute efficiency is becoming entangled with capability. Better algorithms do not just reduce cost; they make new reasoning and evaluation regimes feasible.

## Theme 9: Scientific and Physical Domains Are No Longer Peripheral

Both conferences show substantial accepted work in chemistry, physics, earth sciences, biology, health, robotics, and neuroscience. ICML's metadata highlights chemistry/physics/earth sciences and health/medicine as prominent application areas; ICLR similarly has accepted work under physical sciences, robotics, neuroscience, and time-series/dynamical systems.

Subthemes:

- Scientific foundation models.
- Climate and earth-system modeling.
- Wavefunctions and density-functional theory.
- Bioactivity prediction and medical imaging.
- Robotics control, planning, and embodied learning.

Deeper hypothesis: scientific domains are functioning as high-pressure tests for general ML methods because they demand uncertainty, grounding, constraints, sample efficiency, and causal or mechanistic validity.

## Theme 10: Interpretability Is Moving From Explanation to Intervention

Interpretability remains prominent in both metadata summaries. The visible terms include mechanistic interpretability, explainability, fairness, pruning, internal readouts, and model diagnostics.

Subthemes:

- Mechanistic interpretability of LLMs and transformers.
- Explanations for neural additive and structured models.
- Diagnostics for visual generation and multimodal reasoning.
- Interpretability linked to pruning, safety, or alignment.
- Internal probes and readouts for distillation or robustness.

Deeper hypothesis: interpretability is becoming operational. Papers are less satisfied with explaining a trained model after the fact; they use interpretability to edit, compress, verify, align, debug, or certify behavior.

## Next Reading Priorities

1. Start with oral/spotlight papers, because they are smaller in number and likely reveal conference-level priorities.
2. Then sample high-density themes: test-time scaling, evaluation, multimodal grounding, safety/unlearning, and efficient adaptation.
3. For each paper, extract method, evidence, limitations, and theme links into a per-paper note.
4. Update `analysis/themes/theme-index.md` with evidence-backed subthemes only after reading full abstracts or PDFs.
5. Re-run theme synthesis after every batch of 25 to 50 paper notes.

