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
    <div class="contract">
      <div><b>Promise</b>${demo.promise}</div>
      <div><b>Knob</b>${demo.knob}</div>
      <div><b>Failure</b>${demo.failure}</div>
      <div><b>Proof</b>${demo.proof}</div>
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
