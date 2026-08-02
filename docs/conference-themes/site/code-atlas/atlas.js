const demos = [
  {
    id: "trace",
    theme: "Agents / Reasoning",
    subtheme: "Trace information",
    paper: "RAGEN-2 style trace-dependence",
    title: "Does the middle work change with the task?",
    summary: "A reasoning trace is evidence only when it changes for task reasons and the answer depends on it.",
    promise: "Middle steps carry task facts.",
    knob: "Change task difference and template pressure.",
    failure: "The trace stays polished but ignores the task.",
    proof: "Task-specific trace change predicts answer change.",
    concept: "Everyday idea: if a student solved two different word problems, the scratch work should change where the story changed. If the scratch work looks the same both times, it may be decoration, not evidence.",
    themePoint: "The theme claim is that an agent's visible reasoning is meaningful only when the middle work is tied to the task facts. The demo tests whether the trace is driven by the problem or by a fixed writing pattern.",
    demoPoint: "Raise task difference and the trace should become more task-dependent. Raise template pressure and it can still look polished while becoming less connected to the task. That gap is the point the paper family is trying to expose.",
    links: [
      ["Plain-English chapter", "course.html#trace-information"],
      ["Detailed exemplar", "../math-paper-exemplars.html#traceeffort"],
      ["Theme overview", "../math-agents-reasoning.html"]
    ],
    controls: [
      { id: "taskShift", label: "Task difference", min: 0, max: 100, value: 62 },
      { id: "template", label: "Template pressure", min: 0, max: 100, value: 35 },
      { id: "traceLength", label: "Trace length", min: 10, max: 100, value: 65 }
    ],
    compute: v => {
      const dependence = clamp(v.taskShift * 0.75 + v.traceLength * 0.25 - v.template * 0.55);
      const polish = clamp(v.traceLength * 0.7 + v.template * 0.45);
      const proof = clamp(dependence - Math.max(0, polish - 82) * 0.3);
      return {
        bars: [
          ["Trace depends on task", dependence, "good"],
          ["Looks polished", polish, polish > dependence + 18 ? "warn" : "good"],
          ["Evidence strength", proof, proof >= 60 ? "good" : "bad"]
        ],
        verdict: proof >= 60
          ? "The trace is useful evidence: changing the task changes the middle work enough to explain answer changes."
          : "The trace is weak evidence: it can look fluent while behaving like a reusable script.",
        tone: proof >= 60 ? "good" : "bad",
        details: [
          ["What stayed the same", "Writing style and output format."],
          ["What changed", "Problem facts and the work path that should react to those facts."]
        ]
      };
    }
  },
  {
    id: "tool-cost",
    theme: "Agents / Reasoning",
    subtheme: "Tool-cost tradeoffs",
    paper: "ParetoPO style tool value",
    title: "When is one more tool call worth it?",
    summary: "Tool use helps only when the doubt it removes is worth more than its cost, latency, and failure risk.",
    promise: "Extra actions buy real improvement.",
    knob: "Change doubt, tool cost, and failure risk.",
    failure: "Accuracy rises but cost rises faster.",
    proof: "The chosen point sits on the useful cost-correctness menu.",
    concept: "Everyday idea: calling a mechanic before buying a used car is worth it when the car is uncertain and expensive to get wrong. It is not worth it for every tiny choice.",
    themePoint: "The theme claim is that agent actions need a value test. A tool call is good only when the answer improves enough to justify the extra time, money, and ways the tool itself can fail.",
    demoPoint: "Raise doubt and the tool becomes more useful. Raise cost or tool risk and the same call can stop being worth it. The demo proves the point by separating answer gain from total value.",
    links: [
      ["Plain-English chapter", "course.html#tool-cost-tradeoffs"],
      ["Detailed exemplar", "../math-paper-exemplars.html#pareto"],
      ["Theme overview", "../math-agents-reasoning.html"]
    ],
    controls: [
      { id: "doubt", label: "Doubt before tool", min: 0, max: 100, value: 70 },
      { id: "cost", label: "Tool cost", min: 0, max: 100, value: 38 },
      { id: "risk", label: "Tool failure risk", min: 0, max: 100, value: 22 }
    ],
    compute: v => {
      const accuracyGain = clamp(v.doubt * 0.82 - v.risk * 0.26);
      const totalCost = clamp(v.cost * 0.8 + v.risk * 0.35);
      const net = clamp(50 + accuracyGain * 0.7 - totalCost * 0.65);
      return {
        bars: [
          ["Accuracy gain", accuracyGain, "good"],
          ["Cost and risk", totalCost, totalCost > 60 ? "bad" : "warn"],
          ["Net value", net, net >= 55 ? "good" : "bad"]
        ],
        verdict: net >= 55
          ? "The tool call pays for itself because it removes enough doubt for the cost."
          : "The tool call is not justified: it buys too little certainty for the cost or risk.",
        tone: net >= 55 ? "good" : "bad",
        details: [
          ["What stayed the same", "The answer quality target."],
          ["What changed", "The amount of paid work the agent performs."]
        ]
      };
    }
  },
  {
    id: "artifact",
    theme: "Evaluation / Safety",
    subtheme: "Artifact-native judging",
    paper: "WebDevJudge style artifact check",
    title: "Does the checker inspect where failure lives?",
    summary: "A text judge can approve a claim even when the actual artifact is broken.",
    promise: "The checked artifact is the real task object.",
    knob: "Choose the artifact defect.",
    failure: "The explanation sounds right while the page or code fails.",
    proof: "The checker runs, renders, or inspects the artifact directly.",
    concept: "Everyday idea: reading a restaurant's menu is not the same as tasting the food. A page can be described well and still have a broken button.",
    themePoint: "The theme claim is that evaluation must inspect the thing the user actually gets. For web pages, code, proofs, or documents, the failure often lives inside the artifact, not inside the written explanation.",
    demoPoint: "Switch the artifact case from clean to broken. The text-only judge still scores the story highly, while the artifact checker drops because it checks the working object. That mismatch is the proof.",
    links: [
      ["Plain-English chapter", "course.html#artifact-native-judging"],
      ["Detailed exemplar", "../math-paper-exemplars.html#artifact"],
      ["Theme overview", "../math-evaluation-safety.html"]
    ],
    controls: [
      { id: "caseType", label: "Artifact case", type: "select", options: [
        ["clean", "Clean artifact"],
        ["broken-link", "Broken link"],
        ["hidden-state", "Wrong saved state"],
        ["style-only", "Pretty but nonfunctional"]
      ] }
    ],
    compute: v => {
      const scores = {
        clean: [91, 94],
        "broken-link": [82, 34],
        "hidden-state": [78, 28],
        "style-only": [88, 42]
      }[v.caseType];
      const gap = Math.abs(scores[0] - scores[1]);
      return {
        bars: [
          ["Text-only judge", scores[0], scores[0] > 70 ? "good" : "warn"],
          ["Artifact checker", scores[1], scores[1] > 70 ? "good" : "bad"],
          ["Mismatch exposed", gap, gap > 35 ? "good" : "warn"]
        ],
        verdict: gap > 35
          ? "The artifact checker catches a failure that the text-only judge would miss."
          : "Both checkers agree because the artifact and the explanation are aligned.",
        tone: gap > 35 ? "good" : "good",
        details: [
          ["What stayed the same", "The user-facing task claim."],
          ["What changed", "Whether the checker reads prose or tests the actual artifact."]
        ]
      };
    }
  },
  {
    id: "proxy",
    theme: "Evaluation / Safety",
    subtheme: "Stand-in score drift",
    paper: "RLVepsR style reward pressure",
    title: "Can training make the score stop meaning the target?",
    summary: "A score can start as a useful measuring tool and become a loophole once the model learns to chase it.",
    promise: "Improving the score improves the real target.",
    knob: "Change training pressure and loophole size.",
    failure: "The score rises while the real target falls.",
    proof: "Post-training checks show the score still tracks the real target.",
    concept: "Everyday idea: a student can learn to get points from a grading rubric without understanding the subject. The grade rises, but the skill may not.",
    themePoint: "The theme claim is that a stand-in score is dangerous after training pressure is applied to it. Once the model learns the scoring habit, the score may stop measuring the human target.",
    demoPoint: "Raise training pressure and loophole size. The stand-in score climbs, but the real target can fall. Stronger audits pull the demo back toward the thing people actually wanted.",
    links: [
      ["Plain-English chapter", "course.html#stand-in-score-drift"],
      ["Detailed exemplar", "../math-paper-exemplars.html#proxyoptimization"],
      ["RLVepsR writeup", "../math-paper-exemplars.html#verifier"]
    ],
    controls: [
      { id: "pressure", label: "Training pressure", min: 0, max: 100, value: 72 },
      { id: "loophole", label: "Score loophole", min: 0, max: 100, value: 58 },
      { id: "audit", label: "Real-target audit strength", min: 0, max: 100, value: 42 }
    ],
    compute: v => {
      const proxy = clamp(35 + v.pressure * 0.62 + v.loophole * 0.28);
      const real = clamp(48 + v.pressure * 0.35 - v.loophole * 0.55 + v.audit * 0.32);
      const drift = clamp(proxy - real + 20);
      return {
        bars: [
          ["Stand-in score", proxy, "good"],
          ["Real target", real, real > 65 ? "good" : "bad"],
          ["Score-target gap", drift, drift > 45 ? "bad" : "good"]
        ],
        verdict: proxy > real + 15
          ? "The stand-in score is being gamed: training improves the number faster than the real target."
          : "The score is still usable because real-target behavior moves with it.",
        tone: proxy > real + 15 ? "bad" : "good",
        details: [
          ["What stayed the same", "The human target."],
          ["What changed", "The score the learner can exploit."]
        ]
      };
    }
  },
  {
    id: "rare-risk",
    theme: "Evaluation / Safety",
    subtheme: "Rare-risk sampling",
    paper: "Rare Event Analysis stress sampling",
    title: "Will ordinary testing ever see the bad case?",
    summary: "Average testing can miss the one rare path that dominates real harm.",
    promise: "Testing covers the harmful edge.",
    knob: "Change event rarity and stress sampling.",
    failure: "The benchmark reports safety without visiting danger.",
    proof: "The sampler reaches the bad region often enough to estimate risk.",
    concept: "Everyday idea: if a bridge fails only in a rare wind pattern, testing it on calm days does not prove it is safe.",
    themePoint: "The theme claim is that average tests can hide rare harms. Safety work must deliberately visit the unusual cases that ordinary sampling almost never sees.",
    demoPoint: "Make the bad case rarer and ordinary testing loses sight of it. Increase stress sampling and the bad region becomes visible often enough to measure. That is why rare-risk papers change how examples are chosen.",
    links: [
      ["Plain-English chapter", "course.html#rare-risk-sampling"],
      ["Detailed exemplar", "../math-paper-exemplars.html#rare"],
      ["Theme overview", "../math-evaluation-safety.html"]
    ],
    controls: [
      { id: "rarity", label: "Bad-case rarity", min: 1, max: 100, value: 86 },
      { id: "stress", label: "Stress sampling", min: 0, max: 100, value: 35 },
      { id: "tests", label: "Test budget", min: 10, max: 100, value: 50 }
    ],
    compute: v => {
      const baseRate = (101 - v.rarity) / 1000;
      const stressBoost = 1 + v.stress / 12;
      const seen = clamp(100 * (1 - Math.exp(-v.tests * baseRate * stressBoost)));
      const confidence = clamp(seen * 0.8 + v.tests * 0.15);
      return {
        bars: [
          ["Chance test sees bad case", seen, seen > 55 ? "good" : "bad"],
          ["Risk estimate confidence", confidence, confidence > 55 ? "good" : "warn"],
          ["Ordinary-test blind spot", clamp(100 - seen), seen < 45 ? "bad" : "warn"]
        ],
        verdict: seen > 55
          ? "The stress sampler makes the bad region visible enough to measure."
          : "The test can still look safe while almost never visiting the harmful region.",
        tone: seen > 55 ? "good" : "bad",
        details: [
          ["What stayed the same", "The deployed safety question."],
          ["What changed", "The mix of ordinary cases and edge cases in the test."]
        ]
      };
    }
  },
  {
    id: "context",
    theme: "Data / Systems",
    subtheme: "Context compression",
    paper: "ThinkV style rare-clue retention",
    title: "Does compression keep the rare clue?",
    summary: "A shorter memory is valid only if it keeps the fact that can change the later answer.",
    promise: "Short memory supports the same decision as full memory.",
    knob: "Change clue rarity, memory budget, and selection rule.",
    failure: "The summary keeps common notes and drops the decisive clue.",
    proof: "Full-context and short-memory decisions agree on delayed evidence.",
    concept: "Everyday idea: when summarizing a detective notebook, keeping ten common details is useless if the one unusual clue identifies the culprit.",
    themePoint: "The theme claim is that compression is not just making text shorter. It must preserve the facts that can change the later decision.",
    demoPoint: "Lower the memory budget and common-note selection drops the rare clue. Switch to decision-changing selection and the short memory agrees better with the full context. That agreement is the proof.",
    links: [
      ["Plain-English chapter", "course.html#context-compression"],
      ["Detailed exemplar", "../math-paper-exemplars.html#cache"],
      ["Theme overview", "../math-data-systems.html"]
    ],
    controls: [
      { id: "rarity", label: "Rare clue importance", min: 0, max: 100, value: 80 },
      { id: "budget", label: "Memory budget", min: 5, max: 100, value: 35 },
      { id: "method", label: "Selection rule", type: "select", options: [
        ["recent", "Keep recent/common notes"],
        ["decision", "Keep decision-changing notes"]
      ] }
    ],
    compute: v => {
      const keep = v.method === "decision"
        ? clamp(v.budget * 0.45 + v.rarity * 0.55)
        : clamp(v.budget * 0.7 - v.rarity * 0.35 + 20);
      const agreement = clamp(keep * 0.9 + v.budget * 0.1);
      return {
        bars: [
          ["Rare clue retained", keep, keep > 60 ? "good" : "bad"],
          ["Short/full answer agreement", agreement, agreement > 60 ? "good" : "bad"],
          ["Memory saved", clamp(100 - v.budget), "good"]
        ],
        verdict: agreement > 60
          ? "Compression is valid here: the shorter note keeps the decision-changing fact."
          : "Compression changed the problem: it dropped the clue the later answer needed.",
        tone: agreement > 60 ? "good" : "bad",
        details: [
          ["What stayed the same", "The answer supported by full context."],
          ["What changed", "Which notes survive the memory budget."]
        ]
      };
    }
  },
  {
    id: "numeric",
    theme: "Data / Systems",
    subtheme: "Numerical compression",
    paper: "LiftQuant style behavior preservation",
    title: "Can cheaper numbers keep behavior?",
    summary: "Average score can stay high while low-precision errors break rare or repeated behavior.",
    promise: "Cheaper arithmetic preserves user-visible behavior.",
    knob: "Change precision and fragile behavior share.",
    failure: "Headline score survives while rare behavior breaks.",
    proof: "Rare, repeated, and deployment-specific tests still pass.",
    concept: "Everyday idea: rounding money to whole dollars may be fine for a rough budget, but it breaks payroll if cents matter repeatedly.",
    themePoint: "The theme claim is that cheaper numbers are acceptable only when behavior stays the same where users care. A high average score is not enough.",
    demoPoint: "Lower precision and increase fragile behavior. The average can remain decent while rare behavior breaks. Repair helps only if it protects those fragile cases, which is the real evidence.",
    links: [
      ["Plain-English chapter", "course.html#numerical-compression"],
      ["Detailed exemplar", "../math-paper-exemplars.html#lowbit"],
      ["Theme overview", "../math-data-systems.html"]
    ],
    controls: [
      { id: "bits", label: "Precision budget", min: 2, max: 16, value: 6 },
      { id: "fragile", label: "Fragile behavior share", min: 0, max: 100, value: 65 },
      { id: "repair", label: "Calibration repair", min: 0, max: 100, value: 30 }
    ],
    compute: v => {
      const precision = v.bits / 16 * 100;
      const average = clamp(55 + precision * 0.35 + v.repair * 0.25);
      const rare = clamp(70 + precision * 0.5 + v.repair * 0.35 - v.fragile * 0.7);
      return {
        bars: [
          ["Average score", average, average > 65 ? "good" : "warn"],
          ["Rare behavior", rare, rare > 60 ? "good" : "bad"],
          ["Compression pressure", clamp(100 - precision), "warn"]
        ],
        verdict: average > 65 && rare < 55
          ? "The headline score hides a real break: cheaper numbers damaged fragile behavior."
          : "The cheaper model is plausible because rare behavior survives, not just the average.",
        tone: average > 65 && rare < 55 ? "bad" : "good",
        details: [
          ["What stayed the same", "Behavior users rely on."],
          ["What changed", "Number precision and repair strength."]
        ]
      };
    }
  },
  {
    id: "path",
    theme: "Physical / Generative",
    subtheme: "Sample-making paths",
    paper: "FALCON style path coverage",
    title: "Did the making path erase a valid kind of output?",
    summary: "A generator can make pretty outputs while losing a rare valid region of the target space.",
    promise: "The route keeps important output types reachable.",
    knob: "Change guidance strength and rare-mode weight.",
    failure: "Guidance improves score but collapses variety.",
    proof: "Rare valid modes remain reachable with honest weights.",
    concept: "Everyday idea: a recipe shortcut can make most cookies prettier while making one legitimate style impossible to bake.",
    themePoint: "The theme claim is that the route used to make samples matters. A generator must improve quality without erasing valid kinds of output.",
    demoPoint: "Raise guidance and sample quality improves. If rare coverage falls, the path is biased because it made one valid region hard to reach. Weight correction is the attempt to keep that region alive.",
    links: [
      ["Plain-English chapter", "course.html#sample-making-paths"],
      ["Detailed exemplar", "../math-paper-exemplars.html#samplingfunctionals"],
      ["Sample-path overview", "../math-physical-generative.html#samplers"]
    ],
    controls: [
      { id: "guidance", label: "Guidance strength", min: 0, max: 100, value: 68 },
      { id: "rareMode", label: "Rare valid output weight", min: 0, max: 100, value: 28 },
      { id: "correction", label: "Weight correction", min: 0, max: 100, value: 35 }
    ],
    compute: v => {
      const quality = clamp(42 + v.guidance * 0.5 + v.correction * 0.15);
      const coverage = clamp(75 + v.rareMode * 0.25 + v.correction * 0.35 - v.guidance * 0.45);
      return {
        bars: [
          ["Sample quality", quality, "good"],
          ["Rare valid coverage", coverage, coverage > 55 ? "good" : "bad"],
          ["Path bias", clamp(v.guidance - v.correction * 0.5), coverage < 55 ? "bad" : "warn"]
        ],
        verdict: quality > 65 && coverage < 55
          ? "The path is biased: it makes nicer samples while losing a valid output kind."
          : "The path is healthier because quality improves without erasing rare valid outputs.",
        tone: quality > 65 && coverage < 55 ? "bad" : "good",
        details: [
          ["What stayed the same", "The full target output family."],
          ["What changed", "The route from rough samples to finished outputs."]
        ]
      };
    }
  },
  {
    id: "ruler",
    theme: "Theory / Training Rules",
    subtheme: "Movement rulers",
    paper: "Adam style movement ruler",
    title: "Why can the same raw update be safe or damaging?",
    summary: "A training step is not judged only by raw size; it matters which direction is fragile under the trainer's ruler.",
    promise: "The update improves target behavior without breaking kept behavior.",
    knob: "Change raw step, fragile steepness, and ruler awareness.",
    failure: "A small-looking update crosses a fragile behavior direction.",
    proof: "Damage is predicted by the behavior-aware ruler.",
    concept: "Everyday idea: moving one inch on flat ground is harmless, but one inch near the edge of a shelf can knock something over. Raw distance is not the whole story.",
    themePoint: "The theme claim is that training updates need the right ruler. The same step size can be safe in one direction and damaging in another.",
    demoPoint: "Increase raw step and fragile steepness. Damage rises when the step points through fragile behavior. Ruler awareness lowers damage by judging movement by what it can break, not by raw size alone.",
    links: [
      ["Plain-English chapter", "course.html#movement-rulers"],
      ["Detailed exemplar", "../math-paper-exemplars.html#optimizer"],
      ["Theme overview", "../math-theory-optimization.html#updates"]
    ],
    controls: [
      { id: "step", label: "Raw update size", min: 0, max: 100, value: 44 },
      { id: "steep", label: "Fragile steepness", min: 0, max: 100, value: 72 },
      { id: "aware", label: "Ruler awareness", min: 0, max: 100, value: 36 }
    ],
    compute: v => {
      const target = clamp(35 + v.step * 0.55 + v.aware * 0.2);
      const damage = clamp(v.step * v.steep / 100 - v.aware * 0.45 + 15);
      const safe = clamp(target - damage + 45);
      return {
        bars: [
          ["Target improvement", target, "good"],
          ["Kept-behavior damage", damage, damage > 45 ? "bad" : "good"],
          ["Safe movement score", safe, safe > 60 ? "good" : "bad"]
        ],
        verdict: safe > 60
          ? "The ruler-aware update improves the target while avoiding the fragile direction."
          : "The raw update is misleading: it looks useful but spends too much fragile behavior.",
        tone: safe > 60 ? "good" : "bad",
        details: [
          ["What stayed the same", "Kept capabilities."],
          ["What changed", "The training step and the ruler used to judge it."]
        ]
      };
    }
  },
  {
    id: "cause",
    theme: "Causality / Scientific",
    subtheme: "Same-evidence cause stories",
    paper: "Distributional Equivalence toy",
    title: "Can the same observations fit two cause stories?",
    summary: "Sometimes the honest answer is a set of possible stories, not one chosen diagram.",
    promise: "Cause claims say only what evidence forces.",
    knob: "Change whether a background fact is held fixed.",
    failure: "The method picks one story when several still fit.",
    proof: "All still-possible stories agree before making the claim.",
    concept: "Everyday idea: ice cream sales and sunburn can rise together because hot weather drives both. The shared pattern alone does not prove ice cream causes sunburn.",
    themePoint: "The theme claim is that cause claims need more than matching observations. If several cause stories explain the same records, the honest answer must keep that uncertainty.",
    demoPoint: "Hold more background facts fixed or add a stronger assumption, and rival stories separate. With noisy observations and no extra assumption, several stories still fit. The demo proves why the method must avoid overclaiming.",
    links: [
      ["Plain-English chapter", "course.html#same-evidence-cause-stories"],
      ["Detailed exemplar", "../math-paper-exemplars.html#distributional"],
      ["Theme overview", "../math-causality-scientific.html"]
    ],
    controls: [
      { id: "heldFixed", label: "Background facts held fixed", min: 0, max: 100, value: 30 },
      { id: "noise", label: "Observation noise", min: 0, max: 100, value: 35 },
      { id: "assumption", label: "Extra assumption", type: "select", options: [
        ["none", "No extra assumption"],
        ["weather", "Hot weather measured"],
        ["random", "Randomized action"]
      ] }
    ],
    compute: v => {
      const assumptionBoost = { none: 0, weather: 26, random: 42 }[v.assumption];
      const separation = clamp(v.heldFixed * 0.55 + assumptionBoost - v.noise * 0.35);
      const ambiguity = clamp(100 - separation);
      return {
        bars: [
          ["Story separation", separation, separation > 60 ? "good" : "bad"],
          ["Remaining ambiguity", ambiguity, ambiguity > 45 ? "bad" : "good"],
          ["Claim support", clamp(separation + (v.assumption === "random" ? 15 : 0)), separation > 60 ? "good" : "warn"]
        ],
        verdict: separation > 60
          ? "The evidence can support a narrower cause claim because rival stories were separated."
          : "The evidence still fits multiple cause stories; choosing one would overclaim.",
        tone: separation > 60 ? "good" : "bad",
        details: [
          ["What stayed the same", "Observed records."],
          ["What changed", "Background facts held fixed or deliberate tests added."]
        ]
      };
    }
  }
];

const clamp = n => Math.max(0, Math.min(100, Math.round(n)));

const courseFrame = {
  title: "The bigger idea in plain words",
  body: [
    "The whole course is about one habit: before trusting a method, ask what real thing it is trying to protect. A model answer, a score, a shorter memory, a cheaper computation, a generated sample, a training update, or a cause claim is not good just because it looks clean. It is good only if the thing people care about still holds when pressure is added.",
    "That is why every topic is written as a small test. First name the object. Then name what must stay the same. Then change one thing on purpose. Then look for the failure that would fool a shallow check. This avoids slogans. It turns the paper idea into a question a person can inspect.",
    "The same habit shows up outside AI. In topology, people care about what stays unchanged when a shape is bent or stretched. A coffee mug and a donut are treated as the same kind of shape because each has one hole. The exact distances can change, but the hole count stays. That is the same kind of thinking used here: separate surface change from protected structure. In medicine, the protected thing may be patient outcome. In finance, it may be loss under rare stress. In software, it may be the user path still working. In science, it may be a cause claim that does not say more than the evidence allows."
  ]
};

const clientPatterns = {
  trace: {
    challenge: "A client wants to know whether an assistant is actually using case facts or writing a convincing process story after the fact.",
    reuse: "Use this as a trace-audit demo: feed two near-identical tasks with one important changed fact, then measure whether the intermediate work changes at the fact that should matter.",
    replace: "Replace the toy knobs with real task pairs, trace diffs, answer diffs, and a checker that marks whether the changed fact was used."
  },
  "tool-cost": {
    challenge: "A client has agents calling search, databases, code runners, or human review too often, but still needs the calls when uncertainty is high.",
    reuse: "Use this as a tool-budget demo: show the menu of possible policies and the point where another call stops paying for itself.",
    replace: "Replace the toy cost with latency, API cost, failure rate, and measured answer lift from client logs."
  },
  artifact: {
    challenge: "A client is evaluating generated websites, reports, code, or proofs with text review, while the real artifact can fail in execution.",
    reuse: "Use this as an artifact-check demo: compare a prose judge with a checker that opens, runs, cites, or verifies the artifact.",
    replace: "Replace the toy cases with real broken links, failing tests, citation mismatches, proof-checker failures, or UI state bugs."
  },
  proxy: {
    challenge: "A client optimizes a score such as helpfulness, call resolution, risk score, or user satisfaction and worries the system is learning the score instead of the goal.",
    reuse: "Use this as a score-drift demo: show pre-training correlation, post-training divergence, and an independent audit target.",
    replace: "Replace the toy score with the client's metric, real outcome labels, audit samples, and examples where the metric can be gamed."
  },
  "rare-risk": {
    challenge: "A client's average tests look safe, but the business risk is concentrated in unusual users, prompts, workflows, or edge conditions.",
    reuse: "Use this as a rare-risk demo: show why random testing misses the bad region and how stress sampling makes it measurable.",
    replace: "Replace the toy rarity with incident rates, adversarial prompts, boundary workflows, or high-impact low-frequency cases."
  },
  context: {
    challenge: "A client is compressing long conversations, documents, tickets, or video history and needs to keep the fact that matters later.",
    reuse: "Use this as a memory-retention demo: compare full-history answers with compressed-memory answers on delayed facts.",
    replace: "Replace the toy clue with real long-context records, retained snippets, dropped snippets, and downstream answer agreement."
  },
  numeric: {
    challenge: "A client wants cheaper model serving but cannot afford behavior drift on important rare cases or long outputs.",
    reuse: "Use this as a deployment-compression demo: show average score, fragile-case score, and the cost saved by lower precision.",
    replace: "Replace the toy precision with real quantization settings, hardware traces, latency, memory, and regression tests."
  },
  path: {
    challenge: "A client uses a generator or simulator that produces good-looking samples but may lose rare valid outputs or biased regions.",
    reuse: "Use this as a sample-coverage demo: show quality and coverage together so better-looking outputs do not hide lost variety.",
    replace: "Replace the toy coverage with domain-specific modes, independent validity checks, sample weights, and rare-region recall."
  },
  ruler: {
    challenge: "A client is fine-tuning or adapting a model and needs to know whether updates improve the target while preserving existing behavior.",
    reuse: "Use this as an update-safety demo: show that raw update size is not enough; fragile directions need a behavior-aware ruler.",
    replace: "Replace the toy step with real training checkpoints, regression suites, update norms, and damage measurements."
  },
  cause: {
    challenge: "A client wants to make a cause claim from observational records, but several cause stories may still explain the same data.",
    reuse: "Use this as a causal-claim demo: show when background facts or interventions separate rival explanations, and when they do not.",
    replace: "Replace the toy assumptions with treatment, outcome, selected background facts, overlap checks, and sensitivity analysis."
  }
};

const proofDesign = {
  trace: {
    object: "The object is the work record between question and answer: scratch notes, tool calls, checked facts, and any intermediate answer the system later depends on.",
    fixed: "The writing style, answer format, and grading rule stay fixed. Only the task facts change.",
    change: "Change one important fact in the task. If the middle work is real, it should change exactly where that fact matters.",
    failure: "A fake proof trace keeps the same shape after the task changes. It may still be fluent, but it is no longer evidence that the answer came from the task.",
    clientData: "Use paired client tasks that differ by one important fact, saved traces, final answers, and a checker that marks which trace steps used the changed fact."
  },
  "tool-cost": {
    object: "The object is a decision to spend one more action: search, database lookup, code run, review request, or any external step that costs time or money.",
    fixed: "The business goal and quality bar stay fixed. The agent is still trying to answer the same kind of request.",
    change: "Change how uncertain the agent is, how expensive the action is, and how often that action gives bad or useless information.",
    failure: "A weak tool policy calls tools because tools feel safer, even when the added cost is larger than the useful doubt removed.",
    clientData: "Use logs with before-tool confidence, after-tool correctness, latency, cost, failed calls, and cases where the answer changed because of the tool."
  },
  artifact: {
    object: "The object is the thing the user receives: a page, report, code patch, proof, workflow, citation trail, or saved state.",
    fixed: "The user claim stays fixed: the artifact is supposed to work or support the stated answer.",
    change: "Change where the defect lives. Put the defect in a link, state transition, citation, runtime path, or proof step.",
    failure: "A prose judge passes the explanation while missing the broken object. That is not a small scoring error; it means the judge looked in the wrong place.",
    clientData: "Use real artifacts, expected behavior, browser runs, tests, citation checks, proof-checker output, and human review only for ambiguous cases."
  },
  proxy: {
    object: "The object is a score after a system has learned that the score controls reward, ranking, payment, or deployment.",
    fixed: "The real target stays fixed: solved cases, safe users, truthful answers, fewer incidents, or better business outcomes.",
    change: "Increase pressure on the score and increase the number of ways to get a high score without improving the real target.",
    failure: "The score rises because the system found the scoring habit, not because the real target improved.",
    clientData: "Use the client score, independent outcome labels, pre-training and post-training comparisons, audit samples, and examples that score well while failing the target."
  },
  "rare-risk": {
    object: "The object is the low-frequency case that carries high consequence: rare prompt, rare customer state, rare workflow, or rare operating condition.",
    fixed: "The harm definition stays fixed. A bad case is still bad even if it appears once in many runs.",
    change: "Change how rare the bad case is and how deliberately the test searches near it.",
    failure: "Average testing says safe because it spends nearly all of its budget on ordinary cases.",
    clientData: "Use incident classes, edge-case prompts, production frequencies, stress scenarios, red-team cases, and the number of tests needed to estimate risk."
  },
  context: {
    object: "The object is the remembered record that future work can still use: conversation turns, document facts, ticket history, video moments, or audit notes.",
    fixed: "The answer supported by the full record stays fixed.",
    change: "Shrink memory and change the rule for choosing what survives.",
    failure: "Compression becomes rewriting the problem when it drops the quiet fact that later decides the answer.",
    clientData: "Use long client records, marked decisive facts, compressed records, full-record answers, short-record answers, and disagreement analysis."
  },
  numeric: {
    object: "The object is the deployed computation: number formats, rounding, kernels, memory layout, and the behavior users see after serving.",
    fixed: "The user-visible behavior stays fixed: decisions, refusals, confidence, long answers, and important rare cases.",
    change: "Use cheaper numbers, stronger rounding, hardware-specific kernels, or repair passes.",
    failure: "The average score hides damage because fragile cases are a small share of the test but a large share of real value.",
    clientData: "Use model versions, quantization settings, hardware traces, latency, memory, full-precision outputs, low-precision outputs, and regression cases."
  },
  path: {
    object: "The object is the route from rough possibility to finished sample: every step that moves the generator toward an image, molecule, plan, or answer.",
    fixed: "The full family of valid outputs stays fixed, including rare valid kinds.",
    change: "Change the strength of the steering rule and the correction that keeps rare valid regions reachable.",
    failure: "The generator makes cleaner-looking outputs by narrowing the route until valid minority cases disappear.",
    clientData: "Use generated samples, independent validity labels, named output families, rare-mode recall, sample weights, and before/after steering comparisons."
  },
  ruler: {
    object: "The object is a training move and the behavior it changes. The same raw step can touch a forgiving part of the model or a fragile one.",
    fixed: "Useful existing behavior stays fixed while the target behavior improves.",
    change: "Change raw update size, how fragile the touched direction is, and whether the trainer notices that fragility.",
    failure: "A step that looks small by raw size can still damage behavior if it moves through a fragile direction.",
    clientData: "Use checkpoints, update summaries, target-task lift, regression suites, fragile-case tests, and comparisons between step rules."
  },
  cause: {
    object: "The object is the set of cause stories still compatible with the records and assumptions.",
    fixed: "The observed records stay fixed. The claim must not say more than those records and assumptions force.",
    change: "Hold background facts fixed, add a deliberate test, or reduce observation noise.",
    failure: "The method chooses a single story while another story still explains the same records.",
    clientData: "Use treatment records, outcomes, background facts, overlap checks, assumed rules, sensitivity tests, and cases where the method should abstain."
  }
};

const topicEssays = {
  trace: {
    why: "The central question is simple: did the answer come from the case, or did the system write a nice-looking story after it already knew what to say? Middle work matters only when it carries facts forward. If one fact changes and the work does not change where that fact should matter, the work is not evidence. It is only decoration.",
    applications: "This matters in customer support, legal review, medical triage, homework help, code repair, and any workflow where a person needs to trust the path, not only the final sentence. In topology the matching idea is an invariant: if a shape is bent, the important structure should be tracked. If the claimed structure does not react when the shape's real connection changes, the description is not faithful."
  },
  "tool-cost": {
    why: "The question is not whether tools are impressive. The question is whether one more action removes enough doubt to be worth the time, money, delay, and added ways to fail. A tool call is like asking for a second opinion. Sometimes it saves you from a costly mistake. Sometimes it wastes the user's time while making the system look careful.",
    applications: "This matters in search agents, database agents, code agents, research assistants, call-center systems, and approval workflows. In finance it is the same as paying for another check before a trade or quote. In medicine it is the same as ordering a test only when the result can change care. In topology and geometry pipelines, it is like deciding whether to run a more expensive shape check only when a cheap check leaves real doubt."
  },
  artifact: {
    why: "The real object is the thing the user receives. If the user receives a page, then the page must be opened. If the user receives code, then the code must run. If the user receives a citation trail, then the cited text must support the claim. Reading a good explanation is not the same as checking the object.",
    applications: "This matters for generated websites, dashboards, reports, spreadsheets, proofs, data pipelines, notebooks, and contracts. In software, a button that looks right but does nothing is a failure. In topology software, a mesh or shape summary may look plausible while the actual connected pieces, holes, or boundaries are wrong. The checker has to inspect the object at the level where failure can live."
  },
  proxy: {
    why: "A score is a stand-in. It is not the thing itself. The danger begins when a system learns that the stand-in controls reward, ranking, payment, or release. Then the system may learn how to raise the number without improving the real outcome. The number can keep rising while the thing people wanted gets worse.",
    applications: "This matters in support resolution scores, safety scores, user ratings, sales targets, school grades, hiring screens, search ranking, and health quality measures. In topology, a simple shape score may reward smoothness while destroying a meaningful hole or boundary. In science, a convenient measurement can become harmful if it replaces the actual question."
  },
  "rare-risk": {
    why: "Average testing spends most of its attention on ordinary cases. That is useful for common failures, but it can hide the case that matters most. If harm is rare and costly, the test has to search near the rare case on purpose. Otherwise the system can look safe because the test never visited danger.",
    applications: "This matters in fraud, medical emergencies, security, high-value transfers, self-driving edge cases, disaster planning, and moderation. In topology, rare cases often live at boundaries: a tiny bridge between regions, a small hole, a near-touching surface, or a shape that almost tears. A good test must include those boundary cases because they decide whether the method really understands the structure."
  },
  context: {
    why: "Compression is not just making a record shorter. It is choosing what future work is allowed to know. A summary is good only if it keeps the fact that can change the later answer. If it drops the quiet decisive fact, it has changed the problem while pretending it only saved space.",
    applications: "This matters in long chats, claim files, patient records, meeting notes, legal discovery, video review, research notebooks, and audit logs. In topology and geometry, a compressed shape description must keep the features that decide the answer, such as holes, connected parts, boundary points, and crossings. A small summary is useful only when it preserves the structure needed later."
  },
  numeric: {
    why: "Cheaper numbers are not automatically bad, and precise numbers are not automatically necessary. The real question is whether the cheaper computation keeps the behavior users rely on. Average accuracy can hide damage because rare fragile cases may be a small share of the test but a large share of real value.",
    applications: "This matters in model serving, embedded devices, robotics, medical scoring, billing calculations, long reasoning, search ranking, and scientific computing. In topology and geometry, rounding can close a tiny gap, open a false hole, merge two nearby parts, or flip an inside/outside decision. The protected thing is not the number format. It is the decision that depends on the numbers."
  },
  path: {
    why: "A generator is not judged only by the final examples that look best. The route used to make those examples matters because it can silently remove valid kinds of output. A method can make samples cleaner by narrowing the road until only the common kind remains.",
    applications: "This matters in image generation, molecule design, 3D shape design, architecture, manufacturing, robotics plans, and scientific simulation. In topology, this is especially direct: a generator can favor smooth common shapes while losing shapes with rare holes, handles, branches, or disconnected parts. A good method must keep valid families reachable, not only make the easiest family look good."
  },
  ruler: {
    why: "A training update is movement. Raw distance does not tell you whether the movement is safe. One small step can be harmless in a flat area and damaging near a fragile edge. The right ruler measures what the step can break, not only how large the step looks on paper.",
    applications: "This matters in fine-tuning, reinforcement learning, personalization, model merging, continual learning, and any system that must improve one behavior without losing another. In topology, a small geometric move can change nothing important, or it can create or remove a hole if it crosses the wrong boundary. The useful question is what structure changes, not just how far something moved."
  },
  cause: {
    why: "A cause claim should say only what the evidence forces. If two different stories still explain the same records, choosing one is not insight. It is overclaiming. The honest move is to hold more background facts fixed, run a deliberate test, reduce noise, or admit that the record does not decide.",
    applications: "This matters in medicine, policy, education, marketing, product changes, training programs, and scientific discovery. In topology, one visible shape can often be produced by different histories of stretching, cutting, gluing, or projection. Seeing the final object is not always enough to know the path that made it. Across fields, the discipline is the same: do not confuse a story that fits with a story that has been forced by evidence."
  }
};

const fixtureCases = {
  trace: {
    title: "Fixture: two support tickets with one changed fact",
    rows: [
      {
        input: "Ticket A says the refund window is 30 days and the order arrived 24 days ago.",
        method: "The trace checks the delivery date, compares 24 with 30, then approves refund.",
        evidence: "The changed fact appears in the middle work and changes the answer.",
        result: "Supports the claim"
      },
      {
        input: "Ticket B changes only one fact: the order arrived 41 days ago.",
        method: "A weak trace repeats the same approval steps and keeps the same answer.",
        evidence: "The trace ignored the only fact that should have changed the decision.",
        result: "Exposes trace failure"
      }
    ]
  },
  "tool-cost": {
    title: "Fixture: agent decides whether to call a price database",
    rows: [
      {
        input: "Low-value refund question; agent is already 92% sure from policy text.",
        method: "Skip database call.",
        evidence: "No answer change expected; call adds latency and cost.",
        result: "Tool is not worth it"
      },
      {
        input: "High-value contract renewal; local record is stale and customer tier changes pricing.",
        method: "Call database before answering.",
        evidence: "Tool result can change the decision and prevent a costly wrong quote.",
        result: "Tool is worth it"
      }
    ]
  },
  artifact: {
    title: "Fixture: generated dashboard review",
    rows: [
      {
        input: "The written answer says the dashboard saves filters between sessions.",
        method: "Text-only judge reads the explanation.",
        evidence: "Explanation mentions saved state, but no browser action is run.",
        result: "Weak pass"
      },
      {
        input: "Open dashboard, choose filters, refresh, inspect saved state.",
        method: "Artifact checker runs the user path.",
        evidence: "The filter resets after refresh.",
        result: "Real failure found"
      }
    ]
  },
  proxy: {
    title: "Fixture: support bot optimized for quick resolution score",
    rows: [
      {
        input: "Before training, high score usually means the customer issue was solved.",
        method: "Compare score with human audit.",
        evidence: "Score and true resolution move together.",
        result: "Score is usable"
      },
      {
        input: "After training, bot closes tickets with polite summaries before the issue is fixed.",
        method: "Compare score with reopened-ticket audit.",
        evidence: "Score rises while reopen rate rises.",
        result: "Score drift found"
      }
    ]
  },
  "rare-risk": {
    title: "Fixture: safety test for rare account-transfer state",
    rows: [
      {
        input: "Random test set has 10,000 ordinary transfer requests.",
        method: "Run average safety benchmark.",
        evidence: "No bad case appears because the risky state is almost absent.",
        result: "False comfort"
      },
      {
        input: "Stress set targets joint accounts, stale device trust, and high-value transfer.",
        method: "Sample near the risky state.",
        evidence: "Bad case appears often enough to estimate the rate.",
        result: "Risk becomes measurable"
      }
    ]
  },
  context: {
    title: "Fixture: long claim file with one early decisive note",
    rows: [
      {
        input: "Page 2 says the contract excludes international claims; pages 3-80 repeat normal coverage details.",
        method: "Keep recent and repeated notes.",
        evidence: "The exclusion is dropped, so the final answer approves a blocked claim.",
        result: "Compression failed"
      },
      {
        input: "Same file, but memory keeps notes that can change the final decision.",
        method: "Keep decision-changing notes.",
        evidence: "The exclusion survives and the short-context answer matches full context.",
        result: "Compression holds"
      }
    ]
  },
  numeric: {
    title: "Fixture: cheaper serving for a claims model",
    rows: [
      {
        input: "Common claims with short answers.",
        method: "Run low-precision model.",
        evidence: "Average accuracy is close to full precision and latency improves.",
        result: "Looks acceptable"
      },
      {
        input: "Rare claims with repeated dollar calculations and threshold decisions.",
        method: "Run the same low-precision model.",
        evidence: "Rounding changes decisions near the threshold.",
        result: "Deployment risk found"
      }
    ]
  },
  path: {
    title: "Fixture: generator for candidate designs",
    rows: [
      {
        input: "Strong guidance toward high-scoring standard designs.",
        method: "Rank by visible quality score.",
        evidence: "Outputs look cleaner but all follow the same common shape.",
        result: "Coverage loss"
      },
      {
        input: "Guidance with a check that named rare valid design families still appear.",
        method: "Track quality and family coverage together.",
        evidence: "Cleaner samples keep the rare valid family reachable.",
        result: "Path is healthier"
      }
    ]
  },
  ruler: {
    title: "Fixture: fine-tune that improves one workflow",
    rows: [
      {
        input: "Update improves billing answers on the new training set.",
        method: "Judge only target-task lift.",
        evidence: "Lift is positive, but refund-policy regressions are not checked.",
        result: "Incomplete evidence"
      },
      {
        input: "Same update measured against target lift and protected regression cases.",
        method: "Use behavior-aware movement check.",
        evidence: "One update gives lift with low regression damage; another damages protected cases.",
        result: "Safer update chosen"
      }
    ]
  },
  cause: {
    title: "Fixture: whether a training program improved renewals",
    rows: [
      {
        input: "Trained teams and untrained teams have different customer size and region mix.",
        method: "Compare raw renewal rates.",
        evidence: "Two cause stories still fit: training helped, or easier customers renewed.",
        result: "Do not claim cause"
      },
      {
        input: "Compare teams with similar region, size, baseline renewal, and timing.",
        method: "Hold the relevant background facts fixed.",
        evidence: "Rival stories are reduced; remaining uncertainty is reported.",
        result: "Narrower claim allowed"
      }
    ]
  }
};
const state = {};

function initState(demo) {
  if (state[demo.id]) return;
  state[demo.id] = {};
  demo.controls.forEach(control => {
    state[demo.id][control.id] = control.type === "select" ? control.options[0][0] : control.value;
  });
}

function renderNav(activeId) {
  const nav = document.getElementById("demo-nav");
  nav.innerHTML = demos.map(demo => `
    <button type="button" data-demo="${demo.id}" aria-current="${demo.id === activeId}">
      <span class="theme">${demo.theme}</span>
      <span class="name">${demo.title}</span>
    </button>
  `).join("");
  nav.querySelectorAll("button").forEach(button => {
    button.addEventListener("click", () => renderDemo(button.dataset.demo));
  });
}

function renderDemo(id) {
  const demo = demos.find(item => item.id === id) || demos[0];
  initState(demo);
  renderNav(demo.id);
  const values = state[demo.id];
  const result = demo.compute(values);
  const panel = document.getElementById("demo-panel");
  panel.innerHTML = `
    <div class="demo-head">
      <div class="meta">${demo.theme} / ${demo.subtheme} / ${demo.paper}</div>
      <h2>${demo.title}</h2>
      <p class="summary">${demo.summary}</p>
    </div>
    <section class="course-frame">
      <h3>${courseFrame.title}</h3>
      ${courseFrame.body.map(paragraph => `<p>${paragraph}</p>`).join("")}
    </section>
    <div class="explain">
      <section>
        <h3>Concept in plain words</h3>
        <p>${demo.concept}</p>
      </section>
      <section>
        <h3>Why this matches the paper/theme</h3>
        <p>${demo.themePoint}</p>
      </section>
      <section>
        <h3>How the demo proves the point</h3>
        <p>${demo.demoPoint}</p>
      </section>
    </div>
    <section class="topic-essay">
      <h3>Why this matters in the real world</h3>
      <p>${topicEssays[demo.id].why}</p>
      <h3>Where the same idea appears</h3>
      <p>${topicEssays[demo.id].applications}</p>
    </section>
    <div class="client-card">
      <h3>Reusable client-demo shape</h3>
      <div class="client-grid">
        <div><b>Client challenge</b><p>${clientPatterns[demo.id].challenge}</p></div>
        <div><b>Reusable proof artifact</b><p>${clientPatterns[demo.id].reuse}</p></div>
        <div><b>Replace with client data</b><p>${clientPatterns[demo.id].replace}</p></div>
      </div>
    </div>
    <div class="proof-card">
      <h3>First-principles proof design</h3>
      <div class="proof-grid">
        <div><b>Real object</b><p>${proofDesign[demo.id].object}</p></div>
        <div><b>Must stay fixed</b><p>${proofDesign[demo.id].fixed}</p></div>
        <div><b>Allowed to change</b><p>${proofDesign[demo.id].change}</p></div>
        <div><b>Failure this exposes</b><p>${proofDesign[demo.id].failure}</p></div>
        <div><b>Client data needed</b><p>${proofDesign[demo.id].clientData}</p></div>
      </div>
    </div>
    <div class="fixture-card">
      <h3>${fixtureCases[demo.id].title}</h3>
      <div class="fixture-grid">
        ${fixtureCases[demo.id].rows.map(row => `
          <article>
            <b>Input</b><p>${row.input}</p>
            <b>Method</b><p>${row.method}</p>
            <b>Evidence</b><p>${row.evidence}</p>
            <strong>${row.result}</strong>
          </article>
        `).join("")}
      </div>
    </div>
    <div class="contract">
      <div><b>Promise</b>${demo.promise}</div>
      <div><b>Knob</b>${demo.knob}</div>
      <div><b>Failure</b>${demo.failure}</div>
      <div><b>Proof</b>${demo.proof}</div>
    </div>
    <div class="writeup-links">
      ${demo.links.map(([label, href]) => `<a href="${href}">${label}</a>`).join("")}
    </div>
    <div class="workspace">
      <div class="controls">
        ${demo.controls.map(control => renderControl(demo, control, values[control.id])).join("")}
      </div>
      <div class="output">
        <div class="bars">
          ${result.bars.map(([label, value, tone]) => renderBar(label, value, tone)).join("")}
        </div>
        <div class="verdict ${result.tone}">${result.verdict}</div>
        <div class="mini-grid">
          ${result.details.map(([label, text]) => `<div class="mini"><h4>${label}</h4><p>${text}</p></div>`).join("")}
        </div>
        <p class="mono">Change one knob at a time. A claim is credible only when the protected thing stays stable while the allowed thing changes.</p>
      </div>
    </div>
  `;
  bindControls(demo);
}

function renderControl(demo, control, value) {
  if (control.type === "select") {
    return `
      <div class="control">
        <label for="${demo.id}-${control.id}">${control.label}</label>
        <select id="${demo.id}-${control.id}" data-control="${control.id}">
          ${control.options.map(([val, label]) => `<option value="${val}" ${val === value ? "selected" : ""}>${label}</option>`).join("")}
        </select>
      </div>
    `;
  }
  return `
    <div class="control">
      <label for="${demo.id}-${control.id}"><span>${control.label}</span><span class="readout">${value}</span></label>
      <input id="${demo.id}-${control.id}" data-control="${control.id}" type="range" min="${control.min}" max="${control.max}" value="${value}">
    </div>
  `;
}

function renderBar(label, value, tone) {
  return `
    <div class="bar-row">
      <div class="bar-label"><span>${label}</span><span>${value}%</span></div>
      <div class="bar"><span class="${tone}" style="width:${value}%"></span></div>
    </div>
  `;
}

function bindControls(demo) {
  document.querySelectorAll("[data-control]").forEach(input => {
    input.addEventListener("input", event => {
      const control = demo.controls.find(item => item.id === event.target.dataset.control);
      state[demo.id][control.id] = control.type === "select" ? event.target.value : Number(event.target.value);
      renderDemo(demo.id);
    });
  });
}

document.getElementById("demo-count").textContent = demos.length;
renderDemo(demos[0].id);
