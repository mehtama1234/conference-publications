# Numerical Compression

## The Big Idea

Cheaper numbers can make systems faster and less expensive. Lower precision can
save memory, reduce latency, and make deployment possible on smaller hardware.
That is valuable. But the real question is not whether the numbers are cheaper.
The real question is whether the behavior people rely on stays the same.

Rounding a restaurant bill to the nearest dollar may be fine for a quick
estimate. Rounding payroll over many repeated calculations can break the final
decision. The same idea applies to model serving and scientific computing.

## What Must Stay True

The protected thing is user-visible behavior: decisions, refusals, confidence,
long outputs, threshold cases, rare cases, and calculations people depend on.
The number format can change only if those behaviors survive.

## The Failure

The hidden failure is average-score cover. The headline score stays high because
most cases are easy. A small group of fragile cases breaks, and those cases are
where the real value lives. The model looks cheaper and nearly as accurate while
quietly damaging high-consequence behavior.

## Why This Matters Outside The Demo

This matters in model serving, embedded devices, robotics, medical scoring,
billing systems, search ranking, long reasoning, and scientific simulation. A
small numerical change can matter when it is repeated many times or when a
decision sits near a threshold.

In topology and geometry, rounding can close a tiny gap, open a false hole,
merge two nearby parts, or flip an inside-outside decision. The protected thing
is not the coordinate precision. It is the shape fact that the coordinates are
supposed to support.

## What Client Data Makes It Real

Use model versions, precision settings, hardware traces, latency, memory,
full-precision outputs, low-precision outputs, and regression cases. The proof
is that the cheaper run preserves fragile behavior, not only the average score.
