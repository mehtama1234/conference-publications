# Code Atlas Course Map

This course teaches one habit:

Before trusting a method, name the real thing it must protect.

The method may change wording, cost, samples, scores, memory, numbers, training
steps, or assumptions. Those changes are allowed only when the protected thing
still holds. A good demo makes that visible. A good client adapter replaces the
toy data with real records and keeps the same test.

## The End-To-End Goal

By the end of the course, a reader should be able to take a paper idea, a
client workflow, or a system failure and write a small proof plan in everyday
words:

1. This is the object people can inspect.
2. This is what must stay true.
3. This is what we are allowed to change.
4. This is the shallow check that would fool us.
5. This is the stronger evidence that would prove or disprove the claim.

That is the common shape behind the ten topics.

## How To Read The Course

Read the chapters in this order if you want the idea to build slowly.

1. [Trace Information](chapters/trace-information.md)
   The protected thing is the link between facts, middle work, and answer. The
   failure is a trace that looks careful but ignores the changed fact.

2. [Tool-Cost Tradeoffs](chapters/tool-cost-tradeoffs.md)
   The protected thing is decision quality after cost is counted. The failure is
   taking extra actions because they look careful, not because they pay for
   themselves.

3. [Artifact-Native Judging](chapters/artifact-native-judging.md)
   The protected thing is the object the user receives. The failure is judging
   the explanation while the page, code, proof, citation, or workflow is broken.

4. [Stand-In Score Drift](chapters/stand-in-score-drift.md)
   The protected thing is the real target behind the score. The failure is a
   system learning how to raise the number while the real outcome gets worse.

5. [Rare-Risk Sampling](chapters/rare-risk-sampling.md)
   The protected thing is the high-consequence bad case. The failure is average
   testing that looks safe because it almost never visits the risky region.

6. [Context Compression](chapters/context-compression.md)
   The protected thing is the answer supported by the full record. The failure
   is a summary that drops the quiet fact that later decides the answer.

7. [Numerical Compression](chapters/numerical-compression.md)
   The protected thing is user-visible behavior. The failure is a cheaper run
   that keeps average score high while damaging fragile cases.

8. [Sample-Making Paths](chapters/sample-making-paths.md)
   The protected thing is the full family of valid outputs. The failure is a
   generation path that makes common outputs cleaner while erasing rare valid
   kinds.

9. [Movement Rulers](chapters/movement-rulers.md)
   The protected thing is useful existing behavior. The failure is a training
   move that looks small by raw size but crosses a fragile behavior direction.

10. [Same-Evidence Cause Stories](chapters/same-evidence-cause-stories.md)
    The protected thing is honesty about what the records force. The failure is
    choosing one cause story while another story still explains the same data.

## Why Topology Belongs Here

Topology is useful as a clean example of the same habit. A shape can be bent,
stretched, redrawn, or measured with different coordinates. Some facts may still
survive: number of pieces, holes, boundaries, inside-outside relationships, or
whether two paths remain connected.

The course uses that same idea everywhere:

- A trace can change wording, but the changed fact must still move the work.
- A tool policy can change the number of actions, but the decision must improve
  enough to pay for them.
- A judge can change the scoring method, but the real artifact must be checked.
- A score can change, but the real target must not be replaced by the score.
- A sampler can change examples, but the rare bad case must be visible.
- A memory can shrink, but the decisive fact must survive.
- A computation can use cheaper numbers, but behavior must survive.
- A generator can steer outputs, but valid output families must remain
  reachable.
- A training update can move the model, but protected behavior must survive.
- A cause method can add assumptions, but the claim must not outrun the
  evidence.

The plain word for all of this is preservation. Not preservation as a slogan,
but preservation as a test: when we change the surface, does the thing we care
about still hold?

## What Counts As Mastery

A reader understands the course when they can do this without using special
vocabulary:

- Point to the real object.
- Say what has to survive.
- Say what can move.
- Name the failure that a shallow check would miss.
- Say what data would decide the question.
- Explain the same pattern in another field.

If they can do that, the paper idea has become usable.
