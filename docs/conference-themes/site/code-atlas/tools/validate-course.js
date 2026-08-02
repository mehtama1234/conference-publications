#!/usr/bin/env node
const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const publicRoot = path.resolve(root, "../../docs/conference-themes/site/code-atlas");

const topics = [
  ["trace", "trace-information", "Trace Information"],
  ["tool-cost", "tool-cost-tradeoffs", "Tool-Cost Tradeoffs"],
  ["artifact", "artifact-native-judging", "Artifact-Native Judging"],
  ["proxy", "stand-in-score-drift", "Stand-In Score Drift"],
  ["rare-risk", "rare-risk-sampling", "Rare-Risk Sampling"],
  ["context", "context-compression", "Context Compression"],
  ["numeric", "numerical-compression", "Numerical Compression"],
  ["path", "sample-making-paths", "Sample-Making Paths"],
  ["ruler", "movement-rulers", "Movement Rulers"],
  ["cause", "same-evidence-cause-stories", "Same-Evidence Cause Stories"]
];

const requiredChapterSections = [
  "## The Big Idea",
  "## What Must Stay True",
  "## The Failure",
  "## Why This Matters Outside The Demo",
  "## What Client Data Makes It Real"
];

const packetFields = [
  "Topic:",
  "Claim:",
  "Real object:",
  "Protected thing:",
  "Allowed change:",
  "Hold case:",
  "Fail case:",
  "Evidence:",
  "Decision:",
  "Next client replacement:"
];

const errors = [];

function read(file) {
  return fs.readFileSync(path.join(root, file), "utf8");
}

function exists(file) {
  return fs.existsSync(path.join(root, file));
}

function assert(condition, message) {
  if (!condition) errors.push(message);
}

function countMatches(text, pattern) {
  return [...text.matchAll(pattern)].length;
}

function checkChapters() {
  for (const [, slug, title] of topics) {
    const file = `chapters/${slug}.md`;
    assert(exists(file), `missing chapter ${file}`);
    if (!exists(file)) continue;
    const text = read(file);
    assert(text.startsWith(`# ${title}`), `${file} has wrong title`);
    for (const section of requiredChapterSections) {
      assert(text.includes(section), `${file} missing ${section}`);
    }
    assert(text.includes("topology") || text.includes("geometry"), `${file} missing topology/geometry application`);
    assert(text.length > 1500, `${file} is too thin (${text.length} chars)`);
  }
}

function checkCourseMapAndRenderer() {
  const map = read("COURSE-MAP.md");
  const course = read("course.js");
  const courseHtml = read("course.html");
  assert(map.includes("## The End-To-End Goal"), "COURSE-MAP missing end-to-end goal");
  assert(map.includes("## What Counts As Mastery"), "COURSE-MAP missing mastery test");
  assert(course.includes('["course-map", "COURSE-MAP.md"]'), "course.js missing course map");
  assert(course.includes('["workbook", "WORKBOOK.md"]'), "course.js missing workbook");
  assert(course.includes('["proof-packets", "PROOF-PACKETS.md"]'), "course.js missing proof packets");
  assert(courseHtml.includes('href="#workbook"'), "course.html missing workbook link");
  assert(courseHtml.includes('href="#proof-packets"'), "course.html missing proof-packets link");
  for (const [, slug] of topics) {
    assert(map.includes(`chapters/${slug}.md`), `COURSE-MAP missing ${slug}`);
    assert(course.includes(`["${slug}", "chapters/${slug}.md"]`), `course.js missing ${slug}`);
    assert(courseHtml.includes(`href="#${slug}"`), `course.html missing nav ${slug}`);
  }
}

function checkWorkbookAndPackets() {
  const workbook = read("WORKBOOK.md");
  const packets = read("PROOF-PACKETS.md");
  assert(workbook.includes("## The One-Page Proof Worksheet"), "WORKBOOK missing worksheet");
  assert(workbook.includes("## Client Adapter Checklist"), "WORKBOOK missing adapter checklist");
  assert(workbook.includes("[PROOF-PACKETS.md](PROOF-PACKETS.md)"), "WORKBOOK missing proof packet link");
  assert(packets.includes("## Packet Template"), "PROOF-PACKETS missing template");
  for (const field of packetFields) {
    assert(packets.includes(field), `PROOF-PACKETS missing field ${field}`);
  }
  for (const [, , title] of topics) {
    const heading = `## ${title} Packet`;
    assert(packets.includes(heading), `PROOF-PACKETS missing ${heading}`);
  }
  assert(countMatches(packets, /^## .* Packet$/gm) === 10, "PROOF-PACKETS should have 10 completed packets");
}

function checkFixtures() {
  const fixturePath = path.join(root, "fixtures/client-shaped-fixtures.json");
  const fixtures = JSON.parse(fs.readFileSync(fixturePath, "utf8"));
  for (const [id] of topics) {
    assert(Boolean(fixtures[id]), `fixtures missing ${id}`);
    if (!fixtures[id]) continue;
    assert(Array.isArray(fixtures[id].records), `fixtures ${id} missing records`);
    assert(fixtures[id].records.length >= 2, `fixtures ${id} needs at least two records`);
    for (const [index, record] of fixtures[id].records.entries()) {
      for (const field of ["input", "method", "evidence", "result"]) {
        assert(Boolean(record[field]), `fixtures ${id} record ${index} missing ${field}`);
      }
    }
  }
}

function checkAtlasLinks() {
  const atlas = read("atlas.js");
  for (const [, slug] of topics) {
    assert(atlas.includes(`course.html#${slug}`), `atlas.js missing course link for ${slug}`);
  }
  assert(read("index.html").includes("course.html#proof-packets"), "index.html missing proof packet link");
  assert(read("README.md").includes("PROOF-PACKETS.md"), "README missing proof packets");
  assert(read("CLIENT-DEMO-GUIDE.md").includes("PROOF-PACKETS.md"), "guide missing proof packets");
}

function checkSourcePublicParity() {
  const files = [
    "CLIENT-DEMO-GUIDE.md",
    "COURSE-MAP.md",
    "PROOF-PACKETS.md",
    "README.md",
    "WORKBOOK.md",
    "atlas.js",
    "course.html",
    "course.js",
    "fixtures/client-shaped-fixtures.json",
    "index.html",
    "styles.css",
    ...topics.map(([, slug]) => `chapters/${slug}.md`)
  ];
  for (const file of files) {
    const source = path.join(root, file);
    const published = path.join(publicRoot, file);
    assert(fs.existsSync(published), `published copy missing ${file}`);
    if (fs.existsSync(published)) {
      assert(fs.readFileSync(source, "utf8") === fs.readFileSync(published, "utf8"), `published copy differs for ${file}`);
    }
  }
}

checkChapters();
checkCourseMapAndRenderer();
checkWorkbookAndPackets();
checkFixtures();
checkAtlasLinks();
checkSourcePublicParity();

if (errors.length) {
  console.error("Code atlas course validation failed:");
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(`Code atlas course validation passed: ${topics.length} topics, chapters, fixtures, workbook, proof packets, and published copies.`);
