# Code Atlas Course Quality Audit

This audit states what the course is supposed to prove and where the evidence
lives.

It is not a replacement for reading the course. It is the acceptance checklist
for keeping the course honest as it grows.

## Requirement 1: The Course Has One Clear End-To-End Goal

Requirement:
The course must teach one shared habit across all topics: name the real object,
name what must stay true, change one thing, expose the shallow failure, and
state the evidence that would decide the claim.

Evidence:
`COURSE-MAP.md` states the end-to-end goal and the mastery test. `course.html`
renders the course map as the first section. `tools/validate-course.js` checks
that the course map is present in the rendered course source.

Status:
Satisfied.

## Requirement 2: Every Topic Has A Plain-English Chapter

Requirement:
Each of the ten topics must have a chapter that can stand without the slider
demo. It must explain the everyday problem, what must stay true, the hidden
failure, why the idea matters outside the demo, and what client data makes the
claim real.

Evidence:
The `chapters/*.md` directory contains ten chapter files. The validator checks
for these required sections in every chapter:

- The Big Idea
- What Must Stay True
- The Failure
- Why This Matters Outside The Demo
- What Client Data Makes It Real

Status:
Satisfied.

## Requirement 3: The Writing Uses Everyday Words Before Labels

Requirement:
The course must not rely on labels such as robustness, alignment, optimization,
topology, or causality to carry the explanation. Those words can appear only
when the surrounding text explains the object in plain language.

Evidence:
`CLIENT-DEMO-GUIDE.md` defines the plain-English standard. `README.md` repeats
the rule for future maintainers. The chapters use concrete objects such as
tickets, traces, dashboards, scores, transfers, claim files, model outputs,
generated samples, checkpoints, and treatment records.

Status:
Satisfied by current source. This remains a human review requirement because no
simple script can fully judge clarity.

## Requirement 4: Topology And Other Fields Are Part Of The Explanation

Requirement:
The course must show why the same first-principles habit matters outside AI,
including topology or geometry where preserved structure is the natural
comparison.

Evidence:
`COURSE-MAP.md` has a "Why Topology Belongs Here" section. Each chapter includes
a topology or geometry application. The validator checks that every chapter
mentions topology or geometry.

Status:
Satisfied.

## Requirement 5: The Demos Remain Concrete And Client-Shaped

Requirement:
Every demo must include concrete records rather than only abstract sliders. Each
topic needs at least one hold case and one fail case, with input, method,
evidence, and result.

Evidence:
`fixtures/client-shaped-fixtures.json` contains fixture records for all ten
topics. `atlas.js` renders fixture sections in the public demo. The validator
checks that every topic has at least two fixture records and that each record
has input, method, evidence, and result.

Status:
Satisfied.

## Requirement 6: The Course Has A Practice Layer

Requirement:
A reader must have a way to apply the course habit to a new paper, client
workflow, or system failure.

Evidence:
`WORKBOOK.md` provides the one-page proof worksheet, worked examples, topic
prompts, client adapter checklist, and final self-test. `course.html` renders
the workbook as a course section and links to it from the header.

Status:
Satisfied.

## Requirement 7: The Course Has A Client-Facing Evidence Layer

Requirement:
The course must define what the final proof artifact looks like after a demo
run. The artifact must be reusable across all ten topics.

Evidence:
`PROOF-PACKETS.md` defines a packet template and ten completed proof-packet
examples. Each packet names the claim, real object, protected thing, allowed
change, hold case, fail case, evidence, decision, and client replacement.

Status:
Satisfied.

## Requirement 8: The Public Site Is Readable

Requirement:
The public course should not force readers to open raw markdown files one by
one. There should be a readable course page with navigation.

Evidence:
`course.html` and `course.js` render the course map, ten chapters, workbook,
and proof packets into one styled page. `index.html` links to the course,
workbook, and proof packets.

Status:
Satisfied.

## Requirement 9: The Course Has A Validation Gate

Requirement:
Future edits must have a command that checks the course structure before
publishing.

Evidence:
`tools/validate-course.js` checks chapters, fixtures, course-reader entries,
workbook, proof packets, links, and source-to-public-docs parity. `README.md`
and `CLIENT-DEMO-GUIDE.md` document the command:

```bash
node src/code-atlas/tools/validate-course.js
```

Current result:

```text
Code atlas course validation passed: 10 topics, chapters, fixtures, workbook, proof packets, and published copies.
```

Status:
Satisfied.

## Requirement 10: Published Source Matches Editable Source

Requirement:
The public `docs/conference-themes/site/code-atlas` copy must match
`src/code-atlas` for all course files that are published.

Evidence:
The validator checks source/public parity for the course map, workbook, proof
packets, chapters, fixtures, renderer, styles, and demo files.

Status:
Satisfied.

## Known Boundary

This course is now a strong first-principles teaching and demo package. It is
not yet a live adapter connected to a real client system. The next level would
replace fixture records with client exports, run the same proof-packet shape on
those exports, and save the resulting packet as evidence.

