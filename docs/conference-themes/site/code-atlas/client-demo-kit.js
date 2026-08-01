/*
Reusable helpers for turning a first-principles demo into a client proof.
Keep this dependency-free so a demo can run in a locked-down browser, a docs
site, or a client workshop without a build step.
*/

export function clampPercent(value) {
  return Math.max(0, Math.min(100, Math.round(value)));
}

export function weightedScore(parts) {
  const totalWeight = parts.reduce((sum, part) => sum + part.weight, 0);
  if (!totalWeight) return 0;
  return clampPercent(parts.reduce((sum, part) => sum + part.value * part.weight, 0) / totalWeight);
}

export function riskAdjustedValue({ gain, cost, failureRisk }) {
  return clampPercent(50 + gain * 0.7 - cost * 0.45 - failureRisk * 0.35);
}

export function rareEventSeenChance({ eventRate, trials, stressMultiplier = 1 }) {
  const chance = 1 - Math.exp(-trials * eventRate * stressMultiplier);
  return clampPercent(chance * 100);
}

export function compareJudgeScores({ standInScore, artifactScore }) {
  return {
    gap: clampPercent(Math.abs(standInScore - artifactScore)),
    missedByStandIn: standInScore >= 70 && artifactScore < 60
  };
}

export function retentionScore({ fullAnswerScore, compressedAnswerScore, rareClueKept }) {
  const agreement = 100 - Math.abs(fullAnswerScore - compressedAnswerScore);
  return weightedScore([
    { value: agreement, weight: 2 },
    { value: rareClueKept ? 100 : 0, weight: 3 }
  ]);
}

export function buildEvidencePacket({ claim, protectedThing, allowedChange, observedResult, failureCase }) {
  return {
    claim,
    protectedThing,
    allowedChange,
    observedResult,
    failureCase,
    decision: observedResult >= 60 ? "supports claim" : "claim not yet proven"
  };
}

export function validateDemoSpec(demo) {
  const required = [
    "id",
    "theme",
    "subtheme",
    "paper",
    "title",
    "summary",
    "promise",
    "knob",
    "failure",
    "proof",
    "concept",
    "themePoint",
    "demoPoint",
    "links",
    "controls",
    "compute"
  ];
  const missing = required.filter(key => demo[key] === undefined);
  if (missing.length) {
    throw new Error(`Demo ${demo.id || "(missing id)"} is missing: ${missing.join(", ")}`);
  }
  return true;
}
