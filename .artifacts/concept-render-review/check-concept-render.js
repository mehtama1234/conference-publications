const { chromium } = require("playwright");

const pages = [
  "agent-trajectory-is-the-object.html",
  "boundaries-permissions-and-delegated-authority.html",
  "causality-starts-where-prediction-stops.html",
  "compression-preserves-or-destroys-capability.html",
  "data-as-training-pressure.html",
  "efficiency-changes-the-algorithm.html",
  "evaluation-is-becoming-execution.html",
  "feedback-signals-under-optimization-pressure.html",
  "formal-artifacts-need-native-checkers.html",
  "graph-learning-is-controlled-evidence-movement.html",
  "grounding-as-evidence-preservation.html",
  "human-facing-ai-is-hidden-state-estimation.html",
  "long-context-is-memory-design.html",
  "multimodal-models-need-modality-contracts.html",
  "privacy-and-unlearning-are-recoverable-information-claims.html",
  "retrieval-is-a-hypothesis-about-missing-evidence.html",
  "robotics-turns-perception-into-commitment.html",
  "safety-is-an-invariant-under-pressure.html",
  "scientific-generation-must-preserve-the-native-object.html",
  "spectra-rank-and-subspaces-as-working-objects.html",
  "synthetic-data-as-evidence-or-contamination.html",
  "test-time-compute-is-a-policy.html",
  "theory-is-useful-when-it-names-the-bottleneck.html",
  "uncertainty-as-a-decision-object.html",
  "world-models-are-only-useful-if-actions-stay-true.html",
];

const viewports = [
  { name: "desktop", width: 1440, height: 1100 },
  { name: "mobile", width: 390, height: 844 },
];

async function inspect(page) {
  return await page.evaluate(() => {
    const viewportWidth = document.documentElement.clientWidth;
    const bodyWidth = document.body.scrollWidth;
    const docWidth = document.documentElement.scrollWidth;
    const offenders = [];
    for (const el of document.querySelectorAll("body *")) {
      if (el.closest(".matrix-scroll")) continue;
      const rect = el.getBoundingClientRect();
      if (!rect.width || !rect.height) continue;
      if (rect.left < -2 || rect.right > viewportWidth + 2) {
        offenders.push({
          tag: el.tagName.toLowerCase(),
          cls: el.className || "",
          text: (el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 80),
          left: Math.round(rect.left),
          right: Math.round(rect.right),
        });
      }
      if (offenders.length >= 6) break;
    }
    const h1 = document.querySelector("h1")?.getBoundingClientRect();
    const stats = [...document.querySelectorAll(".stat .v")].map((el) => {
      const rect = el.getBoundingClientRect();
      return {
        text: el.textContent.trim(),
        clipped: el.scrollWidth > el.clientWidth + 1 || rect.width < 20,
      };
    });
    return {
      bodyOverflow: Math.max(bodyWidth, docWidth) - viewportWidth,
      offenders,
      h1Height: h1 ? Math.round(h1.height) : 0,
      stats,
    };
  });
}

(async () => {
  const browser = await chromium.launch();
  const results = [];
  for (const viewport of viewports) {
    const context = await browser.newContext({ viewport });
    const page = await context.newPage();
    for (const file of pages) {
      const url = `http://127.0.0.1:8000/themes/${file}`;
      await page.goto(url, { waitUntil: "networkidle" });
      const data = await inspect(page);
      results.push({ file, viewport: viewport.name, ...data });
    }
    await context.close();
  }
  await browser.close();

  const failures = results.filter((r) => r.bodyOverflow > 2 || r.offenders.length || r.stats.some((s) => s.clipped));
  console.log(JSON.stringify({ checked: results.length, failures }, null, 2));
  if (failures.length) process.exit(1);
})();
