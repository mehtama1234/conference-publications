#!/usr/bin/env python3
"""Build site/paper-explainers.html — the inventory table over every per-paper
explainer spec: title, approach family, first-principles mechanism, hidden
quantity, visual, math object, demo target, page status, implementation status.
Reads specs/*.json (+ checks site/<slug>.html for page status).
Usage: python3 scripts/build_inventory.py"""
import json, glob, os, html, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, "specs"); SITE = os.path.join(ROOT, "site")
def e(s): return html.escape(str(s or ""), quote=False)

def short(s, n=140):
    s = re.sub(r"<[^>]+>", "", s or "")
    return (s[:n] + "…") if len(s) > n else s

def visual_of(spec):
    if spec.get("comic"): return "5-panel story + " + (spec.get("mechanism", {}).get("visual", {}).get("kind", "diagram"))
    v = spec.get("mechanism", {}).get("visual", {})
    return v.get("kind", "—") if v else "—"

def rows():
    out = []
    for fp in sorted(glob.glob(os.path.join(SPECS, "*.json"))):
        if os.path.basename(fp).startswith("_"): continue
        s = json.load(open(fp))
        slug = s["slug"]
        page = os.path.exists(os.path.join(SITE, f"{slug}.html"))
        facts = os.path.exists(os.path.join(ROOT, "data", "facts", f"{slug}.txt"))
        out.append({
            "slug": slug, "title": s.get("title", slug), "family": s.get("family", ""),
            "mechanism": short(s.get("one_liner", "")),
            "hidden": s.get("hidden", {}).get("name", "—"),
            "object": s.get("object", {}).get("object", "—") if isinstance(s.get("object"), dict) else "—",
            "math": short(s.get("math", {}).get("equation", ""), 60),
            "visual": visual_of(s),
            "demo": short(s.get("demo", {}).get("metric_eq", ""), 55),
            "page": "live" if page else "spec only",
            "method": "real method" if facts else "from abstract",
        })
    return out

PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Paper explainers · inventory</title>
<style>
:root{{--ink:#111819;--paper:#F5F6F4;--line:#D7DCD9;--muted:#5F6C70;--accent:#0E7C86;--mono:ui-monospace,Menlo,Consolas,monospace}}
body{{margin:0;background:var(--paper);color:var(--ink);font:15px/1.5 -apple-system,system-ui,Segoe UI,Roboto,sans-serif}}
.wrap{{max-width:1400px;margin:0 auto;padding:26px 22px 70px}}
h1{{font-size:26px;margin:6px 0}} .sub{{color:var(--muted);max-width:70ch}}
.count{{font-family:var(--mono);font-size:13px;color:var(--accent);margin:8px 0 16px}}
table{{border-collapse:collapse;width:100%;background:#fff;font-size:13.5px}}
th,td{{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}}
th{{background:#EAF3F1;position:sticky;top:0;font-size:12px;text-transform:uppercase;letter-spacing:.04em}}
td.t a{{color:var(--accent);text-decoration:none;font-weight:600}} td.t a:hover{{text-decoration:underline}}
.tag{{font-family:var(--mono);font-size:11px;border-radius:5px;padding:1px 6px}}
.live{{background:#DFF0EF;color:#0A5A62}} .spec{{background:#FFF1F0;color:#B42318}}
.real{{background:#EAF6F5;color:#0A5A62}} .abs{{background:#FFF8E6;color:#8a531a}}
.hid{{font-family:var(--mono);font-size:12px;color:#8D3D8B}}
.mono{{font-family:var(--mono);font-size:11.5px;color:#415053}}
.fam{{font-size:12px;color:var(--muted)}}
</style></head><body><div class="wrap">
<p class="mono" style="font-size:12px"><a href="index.html" style="color:var(--accent)">← landscape</a></p>
<h1>Paper explainers — inventory</h1>
<p class="sub">Every paper we have opened into a first-principles explainer. Each row: what the paper really does, the hidden quantity it measures, the math object, and what a tiny demo would prove. Green = the page is live; a real-method tag means it was written from the paper's full text, not just the abstract.</p>
<div class="count">{n} explainers · {live} live · {real} from real method</div>
<table><tr>
<th>Paper</th><th>Family</th><th>First-principles mechanism</th><th>Hidden quantity</th><th>Object changed</th><th>Math object</th><th>Visual</th><th>Demo target</th><th>Page</th><th>Source</th></tr>
{body}
</table></div></body></html>
"""

def main():
    rs = rows()
    body = ""
    for r in rs:
        link = f'<a href="{e(r["slug"])}.html">{e(r["title"])}</a>' if r["page"] == "live" else e(r["title"])
        body += ("<tr>"
                 f'<td class="t">{link}</td>'
                 f'<td class="fam">{e(r["family"])}</td>'
                 f'<td>{e(r["mechanism"])}</td>'
                 f'<td class="hid">{e(r["hidden"])}</td>'
                 f'<td>{e(r["object"])}</td>'
                 f'<td class="mono">{e(r["math"])}</td>'
                 f'<td class="mono">{e(r["visual"])}</td>'
                 f'<td class="mono">{e(r["demo"])}</td>'
                 f'<td><span class="tag {"live" if r["page"]=="live" else "spec"}">{e(r["page"])}</span></td>'
                 f'<td><span class="tag {"real" if r["method"]=="real method" else "abs"}">{e(r["method"])}</span></td>'
                 "</tr>")
    html_out = PAGE.format(n=len(rs), live=sum(1 for r in rs if r["page"]=="live"),
                           real=sum(1 for r in rs if r["method"]=="real method"), body=body)
    open(os.path.join(SITE, "paper-explainers.html"), "w").write(html_out)
    print(f"wrote paper-explainers.html ({len(rs)} explainers)")

if __name__ == "__main__":
    main()
