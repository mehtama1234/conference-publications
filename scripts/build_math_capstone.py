#!/usr/bin/env python3
"""Render the Mathematics Capstone: one first-principles page per math primitive
(plain prose from Haiku + a live canvas diagram + the real explainers that use it)
plus the capstone index math.html grouping all primitives by family.
Usage: python3 scripts/build_math_capstone.py [--all]
"""
import json, glob, os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_paper_explainer import CSS

def e(s): return html.escape(str(s), quote=True)

EXTRA = """
.diagram{background:#0d1314;border:1px solid #000;border-radius:12px;padding:10px 10px 6px;margin:14px 0}
.diagram canvas{width:100%;height:250px;display:block}
.dcap{font-family:var(--mono);font-size:12px;color:#8fb0b3;text-align:center;padding:6px 0 2px}
.stat{display:inline-block;background:#F3FAF9;border:1px solid #CFE4E2;border-radius:999px;padding:4px 12px;font-family:var(--mono);font-size:12px;color:#0A5A62;margin:4px 6px 4px 0}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin:10px 0}
.chip{display:inline-block;background:#fff;border:1px solid var(--line);border-radius:999px;padding:5px 12px;font-size:13px;color:#243130;text-decoration:none}
.chip:hover{border-color:var(--accent);color:#0A5A62}
.chip small{color:var(--muted)}
.fam-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px;margin:16px 0}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;text-decoration:none;color:inherit;display:flex;flex-direction:column;transition:border-color .15s}
.card:hover{border-color:var(--accent)}
.card .mini{background:#0d1314;height:120px}.card .mini canvas{width:100%;height:120px;display:block}
.card .body{padding:12px 14px}.card .nm{font-weight:650;font-size:16px;letter-spacing:-.01em;color:#111819}
.card .ol{font-size:13.5px;color:#41524f;margin:5px 0 8px;line-height:1.5}
.card .ct{font-family:var(--mono);font-size:11px;color:var(--muted)}
.famhead{font-size:22px;margin:36px 0 4px;letter-spacing:-.01em}.famsub{color:var(--muted);font-size:14px;margin:0 0 6px}
.hero{background:linear-gradient(#0d1314,#12201f);color:#EAF3F1}
"""

NAVLINKS = ('<a href="math.html">← Mathematics capstone</a>'
            '<a href="map.html">Field map</a>'
            '<a href="hub.html">The one machine</a>'
            '<a href="paper-explainers.html">All explainers</a>')

def shell(title, body, extra_head=""):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{e(title)}</title><style>{CSS}{EXTRA}</style>{extra_head}</head><body>{body}'
            f'<script src="assets/math-anim.js"></script></body></html>')

def sym_table(symbols):
    rows = "".join(f'<tr><td>{e(s[0])}</td><td>{e(s[1])}</td></tr>'
                   for s in symbols if isinstance(s, list) and len(s) >= 2)
    return f'<table class="symtab">{rows}</table>' if rows else ""

def render_primitive(spec, name_by_slug):
    d = spec
    everyday = "".join(f"<p>{e(p)}</p>" for p in d.get("everyday", []))
    matters = "".join(f"<p>{e(p)}</p>" for p in d.get("matters", []))
    worked = d.get("worked", {}) or {}
    wlines = "".join(f'<div class="line">{e(l)}</div>' for l in worked.get("lines", []))
    worked_html = (f'<div class="worked"><b>{e(worked.get("title","Worked example"))}</b>{wlines}</div>'
                   if wlines else "")
    # where it shows up — linked explainers
    links = d.get("links", [])
    chips = "".join(f'<a class="chip" href="{e(l["slug"])}.html">{e(l["title"])}</a>' for l in links[:12])
    themes = d.get("themes", [])
    tstat = "".join(f'<span class="stat">{e(t[0])} · {t[1]}</span>' for t in themes[:6])
    # siblings
    conn = "".join(f'<a class="chip" href="math-{e(c)}.html">{e(name_by_slug.get(c,c))}</a>'
                   for c in d.get("connects", []) if c in name_by_slug)
    body = f"""
<header class="hero"><div class="wrap"><div class="bug">{e(d.get("capstone_family",""))}</div>
<h1>{e(d["name"])}</h1><p>{e(d.get("one_liner",""))}</p></div></header>
<nav><div class="wrap">{NAVLINKS}</div></nav>
<div class="doc"><div class="wrap">
<div class="diagram"><canvas data-anim="{e(d["diagram"])}"></canvas>
<div class="dcap">live diagram — watch the idea move</div></div>
<div class="eyebrow">In plain terms</div>{everyday}
<div class="eyebrow">The equation</div>
<div class="equation">{e(d.get("seed_equation",""))}</div>
{sym_table(d.get("symbols", []))}
{('<div class="eyebrow">Worked example</div>'+worked_html) if worked_html else ''}
<div class="eyebrow">Why it shows up</div>{matters}
<p class="small">This pattern appears in <b>{d.get("count",0)}</b> of the deep-dive explainers, across:</p>
<div>{tstat}</div>
<div class="chips">{chips}</div>
{('<div class="eyebrow">Connects to</div><div class="chips">'+conn+'</div>') if conn else ''}
</div></div>"""
    return shell(d["name"] + " — Mathematics Capstone", body)

def render_index(specs):
    FAM = ["Probability & Information", "Linear Algebra", "Optimization & Calculus",
           "Generative & Sampling", "Sequential & RL"]
    FSUB = {"Probability & Information": "measuring uncertainty, surprise, and belief",
            "Linear Algebra": "the geometry of weights, vectors, and matrices",
            "Optimization & Calculus": "how models search for better parameters",
            "Generative & Sampling": "turning noise into structure, and back",
            "Sequential & RL": "learning from reward over time"}
    total = sum(s.get("count", 0) for s in specs)
    sections = ""
    for fam in FAM:
        ps = sorted([s for s in specs if s.get("capstone_family") == fam], key=lambda s: -s.get("count", 0))
        if not ps: continue
        cards = ""
        for s in ps:
            cards += (f'<a class="card" href="math-{e(s["slug"])}.html">'
                      f'<div class="mini"><canvas data-anim="{e(s["diagram"])}"></canvas></div>'
                      f'<div class="body"><div class="nm">{e(s["name"])}</div>'
                      f'<div class="ol">{e(s.get("one_liner",""))}</div>'
                      f'<div class="ct">in {s.get("count",0)} explainers</div></div></a>')
        sections += f'<h2 class="famhead">{e(fam)}</h2><p class="famsub">{e(FSUB[fam])}</p><div class="fam-grid">{cards}</div>'
    body = f"""
<header class="hero"><div class="wrap"><div class="bug">ICML + ICLR 2026 · synthesis layer</div>
<h1>The mathematics under {len(specs)} primitives</h1>
<p>Nearly every paper in this corpus is built from the same small set of mathematical moves — a softmax here, a gradient there, a low-rank trick, a KL term. This capstone takes each recurring primitive, explains it from first principles in plain words, shows it moving, and links to the real explainers that use it.</p></div></header>
<nav><div class="wrap"><a href="map.html">Field map</a><a href="hub.html">The one machine</a><a href="paper-explainers.html">All explainers</a></div></nav>
<div class="doc"><div class="wrap">
<p class="lead">{len(specs)} primitives · grouped into 5 families · {total} total appearances across the deep dives. Start anywhere — each page stands alone.</p>
{sections}
</div></div>"""
    return shell("The Mathematics Capstone — ICML + ICLR 2026", body)

def main():
    ins = {os.path.basename(f)[:-5]: json.load(open(f)) for f in glob.glob("data/math_in/*.json")}
    specs = {}
    for slug in ins:
        sp = f"specs/math/{slug}.json"
        if os.path.exists(sp):
            d = json.load(open(sp)); d.update({k: ins[slug][k] for k in
                ("count", "themes", "links", "diagram", "seed_equation", "capstone_family", "name")})
            d["slug"] = slug
            specs[slug] = d
    name_by_slug = {s: specs[s]["name"] for s in specs}
    os.makedirs("site", exist_ok=True)
    for slug, d in specs.items():
        open(f"site/math-{slug}.html", "w").write(render_primitive(d, name_by_slug))
    open("site/math.html", "w").write(render_index(list(specs.values())))
    print(f"built {len(specs)} primitive pages + math.html")

if __name__ == "__main__":
    main()
