#!/usr/bin/env python3
"""Generic first-principles paper-explainer renderer.

One renderer, one per-paper spec JSON -> one rich page. Replaces the bespoke
per-paper scripts (build_ewc..., build_actta...) with a repeatable framework
that enforces the 7-part shape and adds depth (named hidden quantity, one real
equation with every symbol unpacked + a worked mini-example, real failures, a
concrete demo).

Usage:
  python3 scripts/build_paper_explainer.py specs/<slug>.json    # one
  python3 scripts/build_paper_explainer.py --all                # every spec in specs/
"""
import json, sys, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPECS = ROOT / "specs"
OUT = ROOT / "site"
def e(s): return html.escape(str(s), quote=False)

CSS = """
:root{--ink:#111819;--paper:#F5F6F4;--panel:#FFFFFF;--soft:#EAF3F1;--line:#D7DCD9;--muted:#5F6C70;--accent:#0E7C86;--accent2:#B36B22;--good:#217A4D;--bad:#B42318;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,Roboto,Arial,sans-serif}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);line-height:1.68}.wrap{max-width:1040px;margin:0 auto;padding:0 26px}
header{background:var(--ink);color:#ECF2F3;padding:46px 0 38px;border-bottom:1px solid #000}.bug{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#6FE0E8}h1{font-size:34px;line-height:1.12;margin:10px 0 8px;letter-spacing:-.03em}header p{max-width:74ch;color:#B8C4C7;margin:0;font-size:16px}
nav{position:sticky;top:0;z-index:4;background:rgba(17,24,25,.96);border-bottom:1px solid #273538}nav .wrap{display:flex;gap:6px;flex-wrap:wrap;padding:9px 26px}nav a{color:#B8C4C7;text-decoration:none;font-family:var(--mono);font-size:12px;padding:6px 10px;border-radius:6px}nav a:hover{background:#203034;color:#fff}
.doc{padding:28px 0 60px}.eyebrow{font-family:var(--mono);font-size:11px;text-transform:uppercase;letter-spacing:.16em;color:var(--accent);margin:28px 0 6px}h2{font-size:23px;margin:34px 0 10px;letter-spacing:-.01em}h3{font-size:17px;margin:18px 0 6px}p{font-size:16px;color:#243130;margin:10px 0}a{color:#0A5A62}.lead{font-size:18px;color:#243130;max-width:78ch}.small{font-size:13px;color:var(--muted)}ul{font-size:16px;color:#243130}
.toc,.card,.visual,.deep{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:16px 0}.toc a{display:inline-block;border:1px solid var(--line);background:#fff;border-radius:999px;padding:5px 11px;margin:4px;font-size:13px;text-decoration:none}
.comic{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin:18px 0}.panel{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px;min-height:200px;position:relative;overflow:hidden}.panel b{display:block;font-family:var(--mono);font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:var(--accent);margin-bottom:7px}.caption{font-size:13px;color:#334341;line-height:1.45}
.brain{height:74px;border:2px solid #202B2D;border-radius:45% 55% 52% 48%;background:linear-gradient(135deg,#E6F4F2,#fff);position:relative;margin:8px auto 12px;width:110px}.brain:before,.brain:after{content:"";position:absolute;border:1px solid #99B7B4;border-radius:50%;width:40px;height:26px;top:20px}.brain:before{left:15px}.brain:after{right:15px}
.weights{display:flex;gap:5px;align-items:end;justify-content:center;height:72px;margin:8px 0}.w{width:16px;background:#CFD8D6;border:1px solid #AEBBB8;border-radius:4px 4px 2px 2px}.hot{background:#0E7C86;border-color:#095E66}.warm{background:#67B9B6}.free{background:#DCE4E2}.moved{background:#B42318;border-color:#8D1C13}.rubber{border:2px solid var(--accent2)}
.box{border:1px dashed #9FB6B3;border-radius:8px;padding:10px;font-family:var(--mono);font-size:12px;color:#20514f;text-align:center;background:#F3FAF9;margin:8px 0}
.flow{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;align-items:stretch}.step{background:#fff;border:1px solid var(--line);border-radius:8px;padding:12px;position:relative}.step:not(:last-child):after{content:"->";position:absolute;right:-16px;top:42%;font-family:var(--mono);color:var(--accent);font-weight:700}.step b{display:block;color:#0A5A62}
.equation{font-family:var(--mono);font-size:14px;background:#111819;color:#EAF3F1;border-radius:8px;padding:14px;overflow:auto;margin:12px 0}
.symtab{width:100%;border-collapse:collapse;margin:10px 0}.symtab td{border:1px solid var(--line);padding:8px 11px;vertical-align:top;font-size:15px}.symtab td:first-child{font-family:var(--mono);font-size:13px;color:#0A5A62;white-space:nowrap;width:1%;background:#F3FAF9}
.worked{background:#FFFDF7;border:1px solid #E7DCC3;border-left:3px solid var(--accent2);border-radius:0 8px 8px 0;padding:12px 16px;margin:14px 0}.worked b{color:#8a531a}.worked .line{font-family:var(--mono);font-size:13px;color:#3a3a3a;margin:4px 0}
.landscape{height:250px;position:relative;background:linear-gradient(#FDFEFE,#EAF3F1);border:1px solid var(--line);border-radius:10px;overflow:hidden;margin:12px 0}.valley{position:absolute;border:2px solid #9BB7B3;border-radius:50%}.v1{width:320px;height:140px;left:70px;top:56px;transform:rotate(-18deg)}.v2{width:320px;height:140px;right:64px;top:48px;transform:rotate(18deg)}.label{position:absolute;font-family:var(--mono);font-size:12px;color:#415053}.path{position:absolute;height:4px;border-radius:999px;transform-origin:left center}.dot{position:absolute;width:13px;height:13px;border-radius:50%;background:#111819}.legend{display:flex;gap:14px;flex-wrap:wrap;margin-top:8px}.legend span{font-size:13px;color:var(--muted)}.sw{display:inline-block;width:18px;height:4px;border-radius:999px;margin-right:5px;vertical-align:middle}.red{background:var(--bad)}.green{background:var(--good)}
.pipeline{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;align-items:center;margin:12px 0}.stage{background:#fff;border:1px solid var(--line);border-radius:8px;padding:12px;text-align:center;position:relative}.stage:not(:last-child):after{content:"->";position:absolute;right:-14px;top:40%;color:var(--accent);font-family:var(--mono);font-weight:700}.stage.hl{border-color:var(--accent);background:#EAF6F5}.stage small{display:block;color:var(--muted);font-size:12px;margin-top:4px}
.heat{display:grid;grid-template-columns:repeat(12,1fr);gap:6px;margin:12px 0}.cell{height:44px;border-radius:7px;border:1px solid #BFCBC8;background:#EDF2F1;display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:12px;color:#203034}.f1{background:#DFF0EF}.f2{background:#9FD1CE}.f3{background:#49A7A5;color:#fff}.f4{background:#0E7C86;color:#fff}
.bars{display:grid;grid-template-columns:1fr 1fr;gap:18px}.chart{background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px}.barrow{display:grid;grid-template-columns:130px 1fr 48px;align-items:center;gap:8px;margin:10px 0}.bar{height:18px;background:#E8EEEC;border-radius:999px;overflow:hidden}.fill{height:100%;background:var(--accent);border-radius:999px}.fill.bad{background:var(--bad)}.fill.good{background:var(--good)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px}.callout{border-left:3px solid var(--accent);background:#EAF6F5;border-radius:0 8px 8px 0;padding:12px 16px}.warn{border-left-color:var(--bad);background:#FFF1F0}
@media(max-width:900px){.comic,.flow,.bars,.grid2,.pipeline{grid-template-columns:1fr}.step:after,.stage:after{display:none}}
"""

def paras(items): return "".join(f"<p>{p}</p>" for p in items or [])

def viz(kind, args):
    if kind == "brain": return '<div class="brain"></div>'
    if kind == "weights":
        return '<div class="weights">' + "".join(
            f'<div class="w {c}" style="height:{h}px"></div>' for c,h in ((r[0],r[1]) for r in (args or []))) + '</div>'
    if kind == "box": return f'<div class="box">{e(args)}</div>'
    return ""

def render_comic(c):
    if not c: return ""
    panels = "".join(
        f'<div class="panel"><b>{e(p["title"])}</b>{viz(p.get("viz",""),p.get("viz_args"))}'
        f'<p class="caption">{p["caption"]}</p></div>' for p in c["panels"])
    return (f'<section id="visual-story"><div class="eyebrow">Visual story</div>'
            f'<h2>{e(c.get("h2",""))}</h2><div class="comic">{panels}</div></section>')

def render_flow(f):
    if not f: return ""
    steps = "".join(f'<div class="step"><b>{e(s["b"])}</b><p>{s["text"]}</p></div>' for s in f["steps"])
    return (f'<section class="visual"><div class="eyebrow">The algorithm as a flow</div>'
            f'<h2>{e(f.get("h2",""))}</h2><div class="flow">{steps}</div></section>')

def render_heat(h):
    if not h: return ""
    cells = "".join(f'<div class="cell f{lvl}{" rubber" if mark else ""}">{e(lab)}</div>'
                    for _c in h["cells"] for lab,lvl,mark in [(list(_c)+[1,False])[:3]])
    cap = f'<p class="small">{h["caption"]}</p>' if h.get("caption") else ""
    return f'<div class="heat">{cells}</div>{cap}'

def render_hidden(h):
    if not h: return ""
    reads = "".join(f'<div class="callout"><b>{e(r["b"])}</b> {r["html"]}</div>' for r in h.get("reads",[]))
    reads = f'<div class="grid2">{reads}</div>' if reads else ""
    return (f'<section id="hidden" class="deep"><div class="eyebrow">The hidden quantity</div>'
            f'<h2>{e(h.get("h2",""))}</h2>'
            f'<div class="box">measured quantity &nbsp;=&nbsp; {e(h["name"])}</div>'
            f'{paras(h.get("paras"))}{render_heat(h.get("heat"))}{reads}</section>')

def render_mechanism(m):
    if not m: return ""
    v = m.get("visual") or {}
    vis = ""
    if v.get("kind") == "landscape":
        labels = "".join(f'<div class="label" style="{l["css"]}">{e(l["text"])}</div>' for l in v.get("labels",[]))
        paths = "".join(f'<div class="path {p}" style="{css}"></div>' for p,css in v.get("paths",[]))
        dots = "".join(f'<div class="dot" style="{css}"></div>' for css in v.get("dots",[]))
        leg = "".join(f'<span><i class="sw {c}"></i>{e(t)}</span>' for c,t in v.get("legend",[]))
        vis = (f'<div class="landscape"><div class="valley v1"></div><div class="valley v2"></div>'
               f'{labels}{paths}{dots}</div><div class="legend">{leg}</div>')
    elif v.get("kind") == "pipeline":
        stages = "".join(f'<div class="stage {"hl" if s.get("hl") else ""}">{e(s["t"])}<small>{e(s.get("s",""))}</small></div>'
                         for s in v.get("stages",[]))
        vis = f'<div class="pipeline">{stages}</div>'
    return (f'<section id="mechanism" class="visual"><div class="eyebrow">Why it works</div>'
            f'<h2>{e(m.get("h2",""))}</h2>{paras(m.get("paras"))}{vis}</section>')

def render_math(m):
    if not m: return ""
    syms = "".join(f'<tr><td>{e(s[0])}</td><td>{s[1]}</td></tr>' for s in m.get("symbols",[]))
    syms = f'<table class="symtab">{syms}</table>' if syms else ""
    worked = ""
    if m.get("worked"):
        wl = "".join(f'<div class="line">{e(l)}</div>' for l in m["worked"]["lines"])
        worked = f'<div class="worked"><b>{e(m["worked"]["title"])}</b>{wl}</div>'
    note = f'<p>{m["note"]}</p>' if m.get("note") else ""
    return (f'<section id="math" class="deep"><div class="eyebrow">Math after the picture</div>'
            f'<h2>{e(m.get("h2",""))}</h2><p>First in words:</p><div class="equation">{e(m["words"])}</div>'
            f'<p>Then the compact form:</p><div class="equation">{e(m["equation"])}</div>'
            f'<p>Every symbol:</p>{syms}{worked}{note}</section>')

def render_bars(b):
    if not b: return ""
    charts = ""
    for c in b["charts"]:
        rows = "".join(
            f'<div class="barrow"><span>{e(lab)}</span><div class="bar"><div class="fill {tone}" '
            f'style="width:{val}%"></div></div><b>{e(val)}</b></div>'
            for _r in c["rows"] for lab,val,tone in [(list(_r)+[50,""])[:3]])
        note = f'<p class="small">{c["note"]}</p>' if c.get("note") else ""
        charts += f'<div class="chart"><h3>{e(c["title"])}</h3>{rows}{note}</div>'
    return (f'<section class="visual"><div class="eyebrow">What the result should look like</div>'
            f'<h2>{e(b.get("h2",""))}</h2><div class="bars">{charts}</div></section>')

def render_failures(f):
    if not f: return ""
    items = "".join(f'<div class="callout {"warn" if i.get("warn") else ""}"><b>{e(i["b"])}</b> {i["html"]}</div>'
                    for i in f["items"])
    return (f'<section id="failures" class="deep"><div class="eyebrow">What can go wrong</div>'
            f'<h2>{e(f.get("h2",""))}</h2><div class="grid2">{items}</div></section>')

def render_demo(d):
    if not d: return ""
    eq = f'<div class="equation">{e(d["metric_eq"])}</div>' if d.get("metric_eq") else ""
    close = f'<p>{d["closing"]}</p>' if d.get("closing") else ""
    return (f'<section id="demo" class="deep"><div class="eyebrow">What a runnable demo should prove</div>'
            f'<h2>{e(d.get("h2",""))}</h2>{paras(d.get("paras"))}{eq}{close}</section>')

def render(spec):
    nav = "".join(f'<a href="{e(h)}">{e(l)}</a>' for h,l in spec.get("nav",[]))
    toc = "".join(f'<a href="#{a}">{e(l)}</a>' for a,l in spec.get("toc",[]))
    prob = spec["problem"]
    cal = f'<div class="callout"><b>{e(prob["callout"]["b"])}</b> {prob["callout"]["html"]}</div>' if prob.get("callout") else ""
    problem = (f'<section id="zero" class="deep"><div class="eyebrow">Zero assumption version</div>'
               f'<h2>{e(prob.get("h2",""))}</h2>{paras(prob.get("paras"))}{cal}</section>')
    obj = ""
    if spec.get("object"):
        o = spec["object"]
        obj = (f'<section id="object" class="card"><div class="eyebrow">What the paper changes</div>'
               f'<h2>{e(o.get("h2",""))}</h2>{paras(o.get("paras"))}'
               + (f'<div class="box">the object it moves &nbsp;=&nbsp; {e(o["object"])}</div>' if o.get("object") else "") + '</section>')
    body = "".join([problem, render_comic(spec.get("comic")), render_flow(spec.get("flow")), obj,
                    render_hidden(spec.get("hidden")), render_mechanism(spec.get("mechanism")),
                    render_math(spec.get("math")), render_bars(spec.get("bars")),
                    render_failures(spec.get("failures")), render_demo(spec.get("demo"))])
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(spec["title"])}, From First Principles</title>
<style>{CSS}</style></head><body>
<header><div class="wrap"><div class="bug">paper first-principles page · {e(spec.get("family",""))}</div>
<h1>{e(spec["title"])}</h1><p>{spec["one_liner"]}</p></div></header>
<nav><div class="wrap"><a href="paper-explainers.html">Paper explainers</a><a href="index.html">All themes</a>{nav}</div></nav>
<main class="wrap doc">
<p class="lead">{spec["lead"]}</p>
<div class="toc">{toc}</div>
{body}
</main></body></html>"""

def build(spec_path):
    spec = json.loads(Path(spec_path).read_text())
    out = OUT / f'{spec["slug"]}.html'
    out.write_text(render(spec), encoding="utf-8")
    words = len(__import__("re").sub("<[^>]+>"," ",out.read_text()).split())
    print(f'  built {out.name}  ({words} words)')
    return spec

def main():
    if len(sys.argv) < 2:
        print("usage: build_paper_explainer.py specs/<slug>.json | --all"); return
    if sys.argv[1] == "--all":
        for p in sorted(SPECS.glob("*.json")):
            if not p.name.startswith("_"): build(p)
    else:
        build(sys.argv[1])

if __name__ == "__main__":
    main()
