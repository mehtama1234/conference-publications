const courseFiles = [
  ["course-map", "COURSE-MAP.md"],
  ["trace-information", "chapters/trace-information.md"],
  ["tool-cost-tradeoffs", "chapters/tool-cost-tradeoffs.md"],
  ["artifact-native-judging", "chapters/artifact-native-judging.md"],
  ["stand-in-score-drift", "chapters/stand-in-score-drift.md"],
  ["rare-risk-sampling", "chapters/rare-risk-sampling.md"],
  ["context-compression", "chapters/context-compression.md"],
  ["numerical-compression", "chapters/numerical-compression.md"],
  ["sample-making-paths", "chapters/sample-making-paths.md"],
  ["movement-rulers", "chapters/movement-rulers.md"],
  ["same-evidence-cause-stories", "chapters/same-evidence-cause-stories.md"],
  ["workbook", "WORKBOOK.md"],
  ["proof-packets", "PROOF-PACKETS.md"],
  ["quality-audit", "COURSE-QUALITY-AUDIT.md"]
];

function escapeHtml(text) {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function inlineMarkdown(text) {
  return escapeHtml(text).replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, label, href) => {
    return `<a href="${courseHref(href)}">${label}</a>`;
  });
}

function courseHref(href) {
  if (href === "COURSE-MAP.md") return "course.html#course-map";
  if (href === "WORKBOOK.md") return "course.html#workbook";
  if (href === "PROOF-PACKETS.md") return "course.html#proof-packets";
  if (href === "COURSE-QUALITY-AUDIT.md") return "course.html#quality-audit";
  const chapter = href.match(/^chapters\/([^#]+)\.md(#.*)?$/);
  if (chapter) return `course.html#${chapter[1]}${chapter[2] || ""}`;
  return href;
}

function renderMarkdown(markdown, id) {
  const lines = markdown.split(/\r?\n/);
  const html = [];
  let listType = null;

  function closeList() {
    if (listType) {
      html.push(`</${listType}>`);
      listType = null;
    }
  }

  for (const line of lines) {
    if (!line.trim()) {
      closeList();
      continue;
    }
    if (line.startsWith("# ")) {
      closeList();
      html.push(`<h2>${inlineMarkdown(line.slice(2))}</h2>`);
      continue;
    }
    if (line.startsWith("## ")) {
      closeList();
      html.push(`<h3>${inlineMarkdown(line.slice(3))}</h3>`);
      continue;
    }
    const ordered = line.match(/^\d+\.\s+(.*)$/);
    if (ordered) {
      if (listType !== "ol") {
        closeList();
        html.push("<ol>");
        listType = "ol";
      }
      html.push(`<li>${inlineMarkdown(ordered[1])}</li>`);
      continue;
    }
    const bullet = line.match(/^-\s+(.*)$/);
    if (bullet) {
      if (listType !== "ul") {
        closeList();
        html.push("<ul>");
        listType = "ul";
      }
      html.push(`<li>${inlineMarkdown(bullet[1])}</li>`);
      continue;
    }
    closeList();
    html.push(`<p>${inlineMarkdown(line)}</p>`);
  }
  closeList();
  return `<section class="course-section" id="${id}">${html.join("")}</section>`;
}

async function loadCourse() {
  const reader = document.getElementById("course-reader");
  try {
    const sections = await Promise.all(courseFiles.map(async ([id, path]) => {
      const response = await fetch(path, { cache: "no-cache" });
      if (!response.ok) throw new Error(`${path}: ${response.status}`);
      return renderMarkdown(await response.text(), id);
    }));
    reader.innerHTML = sections.join("");
    if (location.hash) {
      document.querySelector(location.hash)?.scrollIntoView();
    }
  } catch (error) {
    reader.innerHTML = `
      <section class="course-section">
        <h2>Course source files</h2>
        <p>The styled reader could not load the markdown files in this browser context. Open the course map directly or serve this folder over HTTP.</p>
        <p><a href="COURSE-MAP.md">Open COURSE-MAP.md</a></p>
        <p class="mono">${escapeHtml(error.message)}</p>
      </section>
    `;
  }
}

loadCourse();
