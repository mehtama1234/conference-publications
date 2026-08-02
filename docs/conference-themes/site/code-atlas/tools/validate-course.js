#!/usr/bin/env node
const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const publicRoot = path.resolve(root, "../../docs/conference-themes/site/code-atlas");
const manifest = JSON.parse(fs.readFileSync(path.join(root, "course-manifest.json"), "utf8"));

const topics = manifest.topics;

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
  for (const topic of topics) {
    const { chapter: file, title } = topic;
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
  assert(course.includes('["quality-audit", "COURSE-QUALITY-AUDIT.md"]'), "course.js missing quality audit");
  assert(courseHtml.includes('href="#workbook"'), "course.html missing workbook link");
  assert(courseHtml.includes('href="#proof-packets"'), "course.html missing proof-packets link");
  assert(courseHtml.includes('href="#quality-audit"'), "course.html missing quality-audit link");
  for (const topic of topics) {
    assert(map.includes(topic.chapter), `COURSE-MAP missing ${topic.slug}`);
    assert(course.includes(`["${topic.slug}", "${topic.chapter}"]`), `course.js missing ${topic.slug}`);
    assert(courseHtml.includes(`href="#${topic.slug}"`), `course.html missing nav ${topic.slug}`);
  }
}

function checkWorkbookAndPackets() {
  const workbook = read("WORKBOOK.md");
  const packets = read("PROOF-PACKETS.md");
  const audit = read("COURSE-QUALITY-AUDIT.md");
  assert(workbook.includes("## The One-Page Proof Worksheet"), "WORKBOOK missing worksheet");
  assert(workbook.includes("## Client Adapter Checklist"), "WORKBOOK missing adapter checklist");
  assert(workbook.includes("[PROOF-PACKETS.md](PROOF-PACKETS.md)"), "WORKBOOK missing proof packet link");
  assert(packets.includes("## Packet Template"), "PROOF-PACKETS missing template");
  for (const field of packetFields) {
    assert(packets.includes(field), `PROOF-PACKETS missing field ${field}`);
  }
  for (const topic of topics) {
    const heading = `## ${topic.packet_heading}`;
    assert(packets.includes(heading), `PROOF-PACKETS missing ${heading}`);
  }
  assert(countMatches(packets, /^## .* Packet$/gm) === 10, "PROOF-PACKETS should have 10 completed packets");
  assert(audit.includes("## Requirement 1"), "quality audit missing requirements");
  assert(audit.includes("## Known Boundary"), "quality audit missing known boundary");
  assert(countMatches(audit, /^## Requirement \d+:/gm) >= 10, "quality audit should cover at least 10 requirements");
}

function checkFixtures() {
  const fixturePath = path.join(root, "fixtures/client-shaped-fixtures.json");
  const fixtures = JSON.parse(fs.readFileSync(fixturePath, "utf8"));
  for (const topic of topics) {
    assert(Boolean(fixtures[topic.id]), `fixtures missing ${topic.id}`);
    if (!fixtures[topic.id]) continue;
    assert(Array.isArray(fixtures[topic.id].records), `fixtures ${topic.id} missing records`);
    assert(fixtures[topic.id].records.length >= 2, `fixtures ${topic.id} needs at least two records`);
    for (const [index, record] of fixtures[topic.id].records.entries()) {
      for (const field of ["input", "method", "evidence", "result"]) {
        assert(Boolean(record[field]), `fixtures ${topic.id} record ${index} missing ${field}`);
      }
    }
  }
}

function checkAtlasLinks() {
  const atlas = read("atlas.js");
  for (const topic of topics) {
    assert(atlas.includes(topic.course_anchor), `atlas.js missing course link for ${topic.slug}`);
  }
  assert(read("index.html").includes("course.html#proof-packets"), "index.html missing proof packet link");
  assert(read("README.md").includes("PROOF-PACKETS.md"), "README missing proof packets");
  assert(read("CLIENT-DEMO-GUIDE.md").includes("PROOF-PACKETS.md"), "guide missing proof packets");
}

function checkManifest() {
  assert(manifest.version === 1, "manifest version must be 1");
  assert(manifest.course.reader === "course.html", "manifest reader should be course.html");
  assert(manifest.course.demo === "index.html", "manifest demo should be index.html");
  assert(manifest.course.validation === "tools/validate-course.js", "manifest validation path mismatch");
  assert(topics.length === 10, "manifest should list 10 topics");
  for (const artifact of Object.values(manifest.artifacts)) {
    assert(exists(artifact), `manifest artifact missing ${artifact}`);
  }
  for (const topic of topics) {
    assert(topic.course_anchor === `course.html#${topic.slug}`, `manifest anchor mismatch for ${topic.id}`);
    assert(topic.chapter === `chapters/${topic.slug}.md`, `manifest chapter mismatch for ${topic.id}`);
    assert(exists(topic.chapter), `manifest chapter missing ${topic.chapter}`);
  }
}

function checkSourcePublicParity() {
  const files = [
    "CLIENT-DEMO-GUIDE.md",
    "COURSE-QUALITY-AUDIT.md",
    "COURSE-MAP.md",
    "PROOF-PACKETS.md",
    "README.md",
    "WORKBOOK.md",
    "atlas.js",
    "course-manifest.json",
    "course.html",
    "course.js",
    "fixtures/client-shaped-fixtures.json",
    "index.html",
    "styles.css",
    ...topics.map(topic => topic.chapter)
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

checkManifest();
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
