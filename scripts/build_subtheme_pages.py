#!/usr/bin/env python3
"""Render standalone subtheme pages: the subtheme's first-principles explanation +
a narrative that situates its real papers + the full list of papers (each with its
contribution and a link to its deep dive). Also re-points the theme-explained pages
and the field map at these standalone pages.
Usage: python3 scripts/build_subtheme_pages.py
"""
import json, os, glob, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_paper_explainer import CSS

def e(s): return html.escape(str(s), quote=True)

EXTRA = """
.hero{background:linear-gradient(#0d1314,#12201f);color:#EAF3F1}
.bigq{font-size:17px;color:#B8C4C7;max-width:80ch;margin:6px 0 0}
.dirs{display:flex;flex-wrap:wrap;gap:7px;margin:10px 0 4px}
.dir{font-family:var(--mono);font-size:12px;background:#EAF6F5;border:1px solid #CFE4E2;color:#0A5A62;border-radius:999px;padding:4px 11px}
.group{margin:26px 0;padding:2px 0 6px}.group h2{margin:6px 0 8px}
.plist.gp{margin:10px 0 0;border-top:1px dashed var(--line);background:#FAFBFA;border-radius:8px;padding:4px 12px}
.plist{margin:14px 0;border-top:1px solid var(--line)}
.prow{padding:13px 0;border-bottom:1px solid var(--line)}
.prow .t{font-size:15.5px;color:#111819;font-weight:600;line-height:1.4}
.prow .c{font-size:14px;color:#41524f;margin:3px 0 0;line-height:1.5}
.prow.deep{background:#FBFDFC;border-left:3px solid var(--accent);padding-left:12px;margin-left:-15px}
.dd{display:inline-block;font-family:var(--mono);font-size:11px;color:#0A5A62;text-decoration:none;border:1px solid #CFE4E2;border-radius:6px;padding:2px 8px;margin-top:5px}
.dd:hover{background:#EAF6F5}
.backlink{color:#6FE0E8;text-decoration:none;font-family:var(--mono);font-size:12px}
"""
NAV = ('<a href="themes.html">All themes</a><a href="map.html">Field map</a>'
       '<a href="math.html">Mathematics</a><a href="paper-explainers.html">All explainers</a>')

def shell(title, body):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{e(title)}</title><style>{CSS}{EXTRA}</style></head><body>{body}</body></html>')

def paper_row(p):
    dd = (f'<a class="dd" href="{e(p["slug"])}.html">read the deep dive →</a>' if p.get("deep") else "")
    contrib = f'<div class="c">{e(p["contribution"])}</div>' if p.get("contribution") else ""
    return (f'<div class="prow{" deep" if p.get("deep") else ""}">'
            f'<div class="t">{e(p["title"])}</div>{contrib}{dd}</div>')

def render(inp, spec):
    explain = "".join(f"<p>{e(p)}</p>" for p in inp.get("explain", []))
    papers = inp.get("papers", [])
    by_n = {p.get("n"): p for p in papers}
    used = set()
    groups_html = ""
    if spec:
        intro = f'<p class="lead">{e(spec.get("intro",""))}</p>' if spec.get("intro") else ""
        groups_html += intro
        for g in spec.get("groups", []):
            mem_ns = [n for n in g.get("members", []) if n in by_n][:6]  # safety cap: never nest >6
            members = [by_n[n] for n in mem_ns]
            for n in mem_ns: used.add(n)
            writeup = "".join(f"<p>{e(p)}</p>" for p in g.get("writeup", []))
            rows = "".join(paper_row(p) for p in members)
            groups_html += (f'<div class="group"><h2>{e(g.get("label",""))}</h2>{writeup}'
                            f'<div class="plist gp">{rows}</div></div>')
    rest = [p for p in papers if p.get("n") not in used]
    rest_html = ""
    if rest:
        rest_html = (f'<div class="eyebrow">More work in this subtheme ({len(rest)})</div>'
                     f'<div class="plist">{"".join(paper_row(p) for p in rest)}</div>')
    theme_link = f'theme-{e(inp["theme_slug"])}-explained.html'
    body = f"""
<header class="hero"><div class="wrap">
<div class="bug"><a class="backlink" href="{theme_link}">← {e(inp["theme"])}</a></div>
<h1>{e(inp["name"])}</h1><p class="bigq">{e(inp.get("gist",""))}</p></div></header>
<nav><div class="wrap">{NAV}</div></nav>
<div class="doc"><div class="wrap">
<div class="eyebrow">What this is</div>{explain}
<div class="eyebrow">How the work breaks down</div>
{groups_html if groups_html else '<p class="small">Grouped writeup pending.</p>'}
{rest_html}
<p class="small">{inp.get("n_papers",0)} papers in this subtheme · {inp.get("n_deep",0)} with a full deep dive.</p>
</div></div>"""
    return shell(inp["name"] + " — subtheme", body)

def main():
    ins = {os.path.basename(f)[:-5]: json.load(open(f)) for f in glob.glob("data/subtheme_pages_in/*.json")}
    specs = {os.path.basename(f)[:-5]: json.load(open(f)) for f in glob.glob("specs/subthemes/*.json")}
    n = 0
    for slug, inp in ins.items():
        open(f"site/subtheme-{slug}.html", "w").write(render(inp, specs.get(slug)))
        n += 1
    print(f"built {n} subtheme pages ({len(specs)} with narratives)")

if __name__ == "__main__":
    main()
