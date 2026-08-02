#!/usr/bin/env python3
import html
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "docs" / "conference-themes" / "site"
sys.path.insert(0, str(ROOT))

from course_spine import COURSE_SUBTITLE, COURSE_TITLE, INTRO, READING_PATH, SECTIONS


def esc(value):
    return html.escape(str(value or ""), quote=True)


def render_intro():
    return "".join(f"<p>{esc(p)}</p>" for p in INTRO)


def render_path():
    return "".join(f'<a href="{esc(href)}">{esc(label)}</a>' for href, label in READING_PATH)


def render_nav():
    return "".join(
        f'<a href="#s{idx}">{idx}. {esc(section["kicker"])}</a>'
        for idx, section in enumerate(SECTIONS, 1)
    )


def render_sections():
    parts = []
    for idx, section in enumerate(SECTIONS, 1):
        body = "".join(f"<p>{esc(p)}</p>" for p in section["body"])
        apps = "".join(f"<li>{esc(app)}</li>" for app in section["applications"])
        parts.append(
            f"""
<section id="s{idx}" class="part">
  <div class="kicker">{esc(section["kicker"])}</div>
  <h2>{idx}. {esc(section["title"])}</h2>
  <p class="summary">{esc(section["summary"])}</p>
  <div class="essay">{body}</div>
  <div class="uses"><h3>Where this shows up</h3><ul>{apps}</ul></div>
</section>"""
        )
    return "\n".join(parts)


PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
:root{--ink:#101719;--paper:#f3f5f4;--panel:#fbfcfb;--line:#d5dcda;--muted:#647073;--accent:#0e7c86;--deep:#0a5860;--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,Roboto,Arial,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:17px;line-height:1.64}.wrap{max-width:960px;margin:0 auto;padding:0 28px}a{color:var(--deep);text-decoration:none;border-bottom:1px solid #0e7c8650}a:hover{border-bottom-color:var(--accent)}h1,h2,h3{margin:0;line-height:1.12;letter-spacing:0;text-wrap:balance}.hero{background:#101719;color:#edf3f3;padding:72px 0 42px;border-bottom:1px solid #000}.eyebrow,.kicker{font-family:var(--mono);font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#55c8d0;font-weight:700}h1{font-size:clamp(42px,7vw,76px);max-width:14ch;margin-top:14px;font-weight:760}.lede{max-width:84ch;margin-top:22px;color:#bdc8ca;font-size:20px;line-height:1.55}nav{position:sticky;top:0;z-index:2;background:rgba(243,245,244,.96);border-bottom:1px solid var(--line)}.navwrap{display:flex;gap:8px;overflow:auto;padding-top:10px;padding-bottom:10px}nav a{white-space:nowrap;background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:5px 9px;font-family:var(--mono);font-size:11px}.intro,.path,.part{background:var(--panel);border:1px solid var(--line);border-radius:5px}.intro{border-left:4px solid var(--accent);padding:20px 22px;margin:28px 0 18px}.intro p{margin:0 0 13px;color:#25312f}.intro p:last-child{margin-bottom:0}.path{padding:16px 18px;margin:18px 0 24px}.path b{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}.path a{display:inline-block;margin:4px 12px 4px 0}.part{border-left:4px solid var(--accent);padding:24px 26px;margin:20px 0}h2{font-size:clamp(28px,4vw,38px);font-weight:750;margin-top:8px}.summary{font-size:19px;color:#25312f;margin:9px 0 17px}.essay p{margin:0 0 13px;color:#25312f}.uses{border-top:1px solid var(--line);padding-top:13px;margin-top:15px}.uses h3{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}.uses ul{margin:0;padding-left:20px}.uses li{color:#25312f;margin:5px 0}.footer{padding:34px 0 60px}.footer p{font-family:var(--mono);font-size:12px;color:var(--muted)}@media(max-width:760px){.wrap{padding:0 20px}.part{padding:20px}}
</style></head><body>
<header class="hero"><div class="wrap"><div class="eyebrow">ICML / ICLR course spine</div><h1>__TITLE__</h1><p class="lede">__SUBTITLE__</p></div></header>
<nav><div class="wrap navwrap">__NAV__</div></nav>
<main class="wrap">
  <div class="intro">__INTRO__</div>
  <div class="path"><b>Read next</b>__PATH__</div>
  __SECTIONS__
  <footer class="footer"><p>Part of the local ICML / ICLR 2026 conference theme atlas. Continue to <a href="index.html">theme map</a>, <a href="math-concepts.html">math atlas</a>, or <a href="paper-atlas.html">publication concept atlas</a>.</p></footer>
</main></body></html>
"""


def main():
    page = (
        PAGE.replace("__TITLE__", esc(COURSE_TITLE))
        .replace("__SUBTITLE__", esc(COURSE_SUBTITLE))
        .replace("__NAV__", render_nav())
        .replace("__INTRO__", render_intro())
        .replace("__PATH__", render_path())
        .replace("__SECTIONS__", render_sections())
    )
    SITE.mkdir(parents=True, exist_ok=True)
    (SITE / "course.html").write_text(page, encoding="utf-8")
    print(f"wrote docs/conference-themes/site/course.html ({len(page) // 1024} KB, {len(SECTIONS)} sections)")


if __name__ == "__main__":
    main()
