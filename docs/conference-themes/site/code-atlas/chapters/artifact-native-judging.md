# Artifact-Native Judging

## The Big Idea

The real object is the thing the user receives. If the user receives a website,
the website must be opened and used. If the user receives code, the code must
run. If the user receives a proof, the proof must be checked. If the user
receives a report with citations, the citations must support the sentences that
depend on them.

Reading an explanation is not the same as checking the artifact. A page can be
described well while its button is broken. A report can sound careful while a
link points to the wrong source. A proof can be written in confident prose while
one step does not follow.

## What Must Stay True

The protected thing is the user's actual claim about the artifact. The claim may
be "this page saves filters," "this patch fixes the failing test," "this chart
uses the right data," or "this proof establishes the result." The checker must
inspect the place where that claim can fail.

## The Failure

The hidden failure is a prose judge looking in the wrong place. It gives a high
score because the explanation is plausible. But the defect lives in the object:
a broken state transition, a wrong file path, a missing import, a fake citation,
or a proof step that cannot be verified.

That is not a small scoring mistake. It means the judge inspected the wrapper
instead of the thing people rely on.

## Why This Matters Outside The Demo

In software, the browser path or test run is the evidence. In scientific
notebooks, the result must rerun from the data. In legal or policy work, the
cited text must support the claim. In finance, a spreadsheet must calculate the
right number after inputs change.

In topology software, an artifact might be a mesh, a shape summary, or a
computed hole count. A pretty rendering can hide a broken connection or false
boundary. The checker has to inspect the shape property itself, not only the
description of the shape.

## What Client Data Makes It Real

Use real artifacts, expected behavior, execution logs, screenshots, tests,
proof-checker output, citation checks, and saved user paths. The evidence is
strong when the checker performs the same kind of action the user depends on.
