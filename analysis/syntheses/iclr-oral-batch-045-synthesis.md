# ICLR Oral Batch 045 Synthesis

## Papers Covered

- RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments
- Depth Anything 3: Recovering the Visual Space from Any Views
- On The Surprising Effectiveness of a Single Global Merging in Decentralized Learning

## Shared Thesis

This final local ICLR oral batch is about robustness through the right operating frame. RedTeamCUA says agent safety must be tested in realistic hybrid web-OS environments where the environment itself can carry adversarial content. Depth Anything 3 says visual geometry can be unified through a simple depth-ray target across arbitrary views. The decentralized-learning paper says communication can be sparse if scheduled at the right phase, with a final global merge turning local diversity into global generalization. Each paper shifts attention from adding machinery to choosing the right evaluation, target, or synchronization frame.

## Deep Themes

### Environment-Aware Evaluation

RedTeamCUA and DA3 both build evaluation around the structure of the real task. RedTeamCUA uses hybrid OS/web sandboxes because CUA threats cross interface boundaries. DA3 introduces a benchmark that spans pose estimation, any-view geometry, and rendering because geometry recovery is broader than monocular depth alone.

### Minimal Interventions at High-Leverage Points

DA3 uses a single depth-ray prediction target instead of specialized multi-task machinery. The decentralized-learning paper uses a single late global merge instead of frequent synchronization. Both suggest that performance can improve when the intervention is simple but placed at the right representational or training point.

### Safety and Generalization Under Distribution Shift

RedTeamCUA studies hostile environmental shifts, DA3 studies arbitrary views and unknown poses, and decentralized merging studies heterogeneous local data. The common difficulty is not average-case performance but behavior when the operating distribution changes across interface, viewpoint, or device.

## Cross-Paper Pattern

The cross-paper pattern is framing as capability. RedTeamCUA reframes CUA safety around realistic adversarial environments. DA3 reframes visual-space recovery around depth rays and arbitrary views. Single global merging reframes decentralized disagreement as potentially constructive diversity. In all three cases, the key move is to set up the problem so the useful structure becomes visible.

## Subthemes to Track

- Hybrid web-OS adversarial testing.
- Indirect prompt injection for computer-use agents.
- Unified any-view geometry recovery.
- Depth-ray prediction.
- Late global model merging.
- Constructive local diversity in decentralized optimization.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Full-paper upgrades should inspect benchmark construction, release artifacts, exact security scenarios, geometry metrics, and decentralized-optimization assumptions.
