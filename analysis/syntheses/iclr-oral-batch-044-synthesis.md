# ICLR Oral Batch 044 Synthesis

## Papers Covered

- ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data
- Differentially Private Domain Discovery
- WoW!: World Models in a Closed-Loop World
- MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction
- The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm

## Shared Thesis

This batch is about infrastructure that turns capability into usable systems. ScaleCUA builds open cross-platform data for computer-use agents. Differentially Private Domain Discovery makes unknown domains usable under privacy constraints. WoW! evaluates world models through closed-loop task success rather than visual quality alone. MetaEmbed exposes retrieval quality/cost as a test-time knob. Polar Express optimizes a numerical linear-algebra primitive for low-precision GPU training. Each paper works below the surface of model outputs, changing the data, benchmark, retrieval, privacy, or numerical substrate that determines practical performance.

## Deep Themes

### Closed-Loop Usefulness Over Static Quality

ScaleCUA and WoW! both center interaction. ScaleCUA scales GUI agents through cross-platform data and closed-loop human-agent collection. WoW! tests whether world models help agents succeed in embodied environments. The shared point is that perceptual or benchmark snapshots are insufficient; agents and world models need to be evaluated in the loop where actions affect the next observation.

### Selective Exposure Under Constraints

Differentially Private Domain Discovery and MetaEmbed both manage what gets exposed. Private domain discovery decides which unknown items can be surfaced while preserving privacy. MetaEmbed decides how many representation vectors should be exposed to retrieval interaction at test time. Both papers treat selection as a first-class system design problem, trading utility against privacy, storage, or latency.

### Low-Level Substrates Matter

Polar Express shows that a numerical subroutine can improve deep-learning training when redesigned for GPU throughput and `bfloat16`. This connects to MetaEmbed's serving tradeoffs and ScaleCUA's data infrastructure: modern ML gains increasingly come from aligning low-level implementation details with the workload.

## Cross-Paper Pattern

The cross-paper pattern is operational realism. ScaleCUA asks whether agents can work across real GUI platforms. Differential privacy asks whether domain discovery remains useful under privacy. WoW! asks whether world models help agents act. MetaEmbed asks whether retrieval can adapt at serving time. Polar Express asks whether optimization primitives fit actual accelerator precision. The batch repeatedly replaces idealized evaluation with the constraints of deployment.

## Subthemes to Track

- Cross-platform computer-use data.
- Private unknown-domain discovery.
- Closed-loop world-model benchmarking.
- Test-time retrieval granularity.
- GPU-friendly matrix sign approximation.
- Operational constraints as drivers of ML method design.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Full-paper upgrades should inspect release status, privacy constants, environment design, retrieval latency/storage curves, numerical stability, and exact benchmark protocols.
