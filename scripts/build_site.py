#!/usr/bin/env python3
"""Build the CVPR-style theme site for ICML/ICLR 2026 from the merged per-paper
analysis: index (landscape) + per-theme pages (paper cards) + hub ("the one
machine of ML") + idea-graph (themes wired by shared methods). Runs on whatever
is in data/analysis_merged.json, so it works incrementally.
Usage: python3 scripts/analyze_pipeline.py merge && python3 scripts/build_site.py"""
import json, os, re, html, collections, itertools

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "data"); SITE = os.path.join(ROOT, "site"); os.makedirs(SITE, exist_ok=True)
def esc(s): return html.escape(str(s), quote=False)
def slug(s): return re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-")

MERGED = json.load(open(f"{D}/analysis_merged.json"))
PAPERS = {p["id"]: p for p in json.load(open(f"{D}/papers_all.json"))}
BY_THEME = collections.defaultdict(list)
for r in MERGED: BY_THEME[r.get("theme","Other")].append(r)

# the one machine of modern ML: 7 stages the 18 themes fall into
STAGES = [
 ("Represent","turn raw data into learnable structure",
   ["Representation & Self-Supervised Learning","Graph & Geometric Learning","Multimodal"]),
 ("Train & optimize","the engines that make learning work and provable",
   ["Optimization","Learning Theory","Efficiency & Systems"]),
 ("Build models","the big model families of 2026",
   ["LLMs & Foundation Models","Computer Vision","Time Series & Sequential"]),
 ("Generate","create new data — images, molecules, video",
   ["Generative Models & Diffusion"]),
 ("Decide & act","learn behavior under reward",
   ["Reinforcement Learning","Robotics & Control","Agents & Tool Use"]),
 ("Trust & align","make models safe, fair, and understandable",
   ["Alignment, Safety & Fairness","Interpretability"]),
 ("Measure & apply","benchmark it and point it at the world",
   ["Datasets & Benchmarks & Evaluation","AI for Science","Other"]),
]
STAGE_OF = {t:i for i,(_,_,ts) in enumerate(STAGES) for t in ts}
COLORS = ["#4f46e5","#0e7490","#0f766e","#7c3aed","#b45309","#be185d","#15803d"]
FRAME = {
 "LLMs & Foundation Models":"The center of gravity of the conference: how to train, adapt, prompt, and understand large language and foundation models.",
 "Generative Models & Diffusion":"Learning to create — diffusion, flow matching, and friends that turn noise into images, molecules, and video.",
 "Computer Vision":"Teaching machines to see: recognition, detection, segmentation, and 3D understanding.",
 "Reinforcement Learning":"Learning by trial and error under a reward — the machinery of decision-making agents.",
 "Representation & Self-Supervised Learning":"Learning good features without labels, so everything downstream gets easier.",
 "Optimization":"The math of training itself — better, faster, more stable descent.",
 "Learning Theory":"Why learning works at all: generalization, sample complexity, and guarantees.",
 "Alignment, Safety & Fairness":"Making powerful models behave — safe, fair, private, and aligned with human intent.",
 "Interpretability":"Opening the black box: what has the model actually learned, and why did it decide that?",
 "Datasets & Benchmarks & Evaluation":"How we measure progress — and how the choice of measurement shapes the field.",
 "Robotics & Control":"Learning to move and manipulate in the physical world.",
 "AI for Science":"Turning machine learning loose on physics, chemistry, biology, and medicine.",
 "Efficiency & Systems":"Doing more with less — compression, quantization, and systems that make big models cheap.",
 "Graph & Geometric Learning":"Learning on graphs, meshes, and data with symmetry and structure.",
 "Multimodal":"Models that join vision, language, audio, and more into one understanding.",
 "Agents & Tool Use":"Wrapping models in loops and tools so they can plan, call functions, and act.",
 "Time Series & Sequential":"Learning from data that unfolds over time — forecasting, sequences, and dynamics.",
 "Other":"Everything that does not fit a single bucket — the long tail of the field.",
}

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title} · ICML + ICLR 2026</title>
<style>
:root{{--bg:#0d1117;--ink:#e6edf3;--soft:#9fb0c3;--dim:#7d8da3;--accent:#5b9bd5;--line:rgba(150,170,205,.14);--mono:ui-monospace,Menlo,Consolas,monospace}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}}
a{{color:var(--accent)}}main{{max-width:1080px;margin:0 auto;padding:26px 22px 80px}}
.top{{border-bottom:1px solid var(--line);padding:12px 22px;display:flex;flex-wrap:wrap;gap:14px;font-family:var(--mono);font-size:13px}}
.top .brand{{font-weight:700;color:var(--ink);text-decoration:none}}.top a{{text-decoration:none;color:var(--soft)}}.top a.on{{color:var(--accent)}}
.kick{{font-family:var(--mono);font-size:12px;color:var(--accent);text-transform:uppercase;letter-spacing:.08em}}
h1{{font-size:29px;margin:6px 0 10px}}.lead{{font-size:18px;color:var(--soft);max-width:820px}}
.grid{{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));margin-top:18px}}
.card{{border:1px solid var(--line);border-radius:12px;padding:14px 16px;background:rgba(255,255,255,.015);text-decoration:none;color:inherit;display:block}}
.card:hover{{border-color:var(--accent)}}.card h3{{margin:0 0 5px;font-size:16px;color:var(--ink)}}.card .n{{float:right;font-family:var(--mono);font-size:12px;color:var(--accent)}}
.card p{{margin:0;font-size:13.5px;color:var(--dim);line-height:1.45}}
.stage{{border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin:12px 0}}
.stage h3 .b{{font-family:var(--mono);font-size:12px;color:#0d1117;padding:2px 9px;border-radius:20px;margin-right:9px;font-weight:700}}
.chips{{display:flex;flex-wrap:wrap;gap:7px;margin-top:9px}}.chip{{text-decoration:none;border:1px solid var(--line);border-radius:20px;padding:4px 11px;background:rgba(255,255,255,.02);color:var(--soft);font-size:13px}}.chip:hover{{border-color:var(--accent);color:var(--accent)}}
.paper{{border-bottom:1px solid var(--line);padding:14px 0}}.paper h3{{margin:0 0 6px;font-size:16px}}.paper .meta{{font-family:var(--mono);font-size:11px;color:var(--dim);margin-bottom:6px}}
.paper .row{{font-size:14px;margin:3px 0}}.paper .row b{{color:var(--soft);font-weight:600}}
.tags{{margin-top:6px}}.tag{{font-family:var(--mono);font-size:11px;color:var(--accent);border:1px solid var(--line);border-radius:5px;padding:1px 6px;margin-right:5px}}
canvas{{width:100%;height:640px;border:1px solid var(--line);border-radius:12px;background:#0a0e14;display:block}}
.legend{{display:flex;flex-wrap:wrap;gap:12px;margin:14px 0;font-size:13px;color:var(--soft)}}.legend span{{display:inline-flex;align-items:center;gap:6px}}.dot{{width:11px;height:11px;border-radius:50%}}
</style></head><body>
<div class="top"><a class="brand" href="index.html">ICML + ICLR 2026</a>
<a class="{i}" href="index.html">Landscape</a><a class="{h}" href="hub.html">The Machine</a><a class="{g}" href="idea-graph.html">Idea Graph</a></div>
<main>
"""
FOOT = "</main></body></html>\n"

def paper_card(r):
    p = PAPERS.get(r["id"], {})
    title = esc(p.get("title", r["id"])); url = p.get("pdf_url") or p.get("url") or "#"
    conf = r["id"].split("-")[0].upper()
    tags = "".join(f'<span class="tag">{esc(m)}</span>' for m in r.get("methods",[])[:4])
    return (f'<div class="paper"><div class="meta">{conf} 2026</div>'
            f'<h3><a href="{esc(url)}">{title}</a></h3>'
            f'<div class="row"><b>Problem.</b> {esc(r.get("problem",""))}</div>'
            f'<div class="row"><b>Approach.</b> {esc(r.get("approach",""))}</div>'
            f'<div class="row"><b>Contribution.</b> {esc(r.get("contribution",""))}</div>'
            f'<div class="tags">{tags}</div></div>')

def build_theme_pages():
    for theme, rows in BY_THEME.items():
        o = [HEAD.format(title=esc(theme), i="", h="", g="")]
        o.append(f'<div class="kick">theme · {len(rows)} papers</div><h1>{esc(theme)}</h1>')
        o.append(f'<p class="lead">{esc(FRAME.get(theme,""))}</p>')
        o.append(f'<p style="margin-top:16px"><a href="index.html">&larr; all themes</a></p>')
        for r in sorted(rows, key=lambda r:r["id"]): o.append(paper_card(r))
        o.append(FOOT)
        open(f"{SITE}/theme-{slug(theme)}.html","w").write("\n".join(o))

def build_index():
    o = [HEAD.format(title="Landscape", i="on", h="", g="")]
    conf = collections.Counter(r["id"].split("-")[0].upper() for r in MERGED)
    o.append('<div class="kick">icml + iclr 2026 · theme landscape</div>')
    o.append(f'<h1>{len(MERGED):,} papers, mapped</h1>')
    o.append(f'<p class="lead">Every accepted paper read from its abstract and sorted into one of eighteen themes, with its problem, central move, and contribution. So far {len(MERGED):,} analyzed ({conf.get("ICLR",0):,} ICLR + {conf.get("ICML",0):,} ICML). Open a theme to read the papers; see <a href="hub.html">the one machine</a> for how the themes connect.</p>')
    o.append('<div class="grid">')
    for theme, rows in sorted(BY_THEME.items(), key=lambda kv:-len(kv[1])):
        o.append(f'<a class="card" href="theme-{slug(theme)}.html"><span class="n">{len(rows)}</span>'
                 f'<h3>{esc(theme)}</h3><p>{esc(FRAME.get(theme,""))}</p></a>')
    o.append('</div>'); o.append(FOOT)
    open(f"{SITE}/index.html","w").write("\n".join(o))

def build_hub():
    o = [HEAD.format(title="The Machine", i="", h="on", g="")]
    o.append('<div class="kick">the one machine of machine learning</div><h1>The 18 themes are one pipeline</h1>')
    o.append('<p class="lead">ICML and ICLR look like a thousand unrelated papers. Read as one system, they are the pipeline every ML result moves through: represent the data, train a model on it, generate or decide with it, make it trustworthy, and measure it against the world. Each theme is one stage; the tile shows its paper count.</p>')
    for i,(name,sub,themes) in enumerate(STAGES):
        c = COLORS[i]
        chips = "".join(f'<a class="chip" href="theme-{slug(t)}.html">{esc(t)} · {len(BY_THEME.get(t,[]))}</a>' for t in themes)
        o.append(f'<div class="stage"><h3><span class="b" style="background:{c}">{i+1:02d}</span>{esc(name)}</h3>'
                 f'<div style="color:var(--dim);font-size:14px">{esc(sub)}</div><div class="chips">{chips}</div></div>')
    o.append(FOOT); open(f"{SITE}/hub.html","w").write("\n".join(o))

def build_graph():
    # edges: two themes linked by how many method-tags they share
    meth = {t:collections.Counter(m for r in rows for m in r.get("methods",[])) for t,rows in BY_THEME.items()}
    themes = [t for t,_ in sorted(BY_THEME.items(), key=lambda kv:-len(kv[1]))]
    edges = []
    for a,b in itertools.combinations(themes,2):
        shared = sum(min(meth[a][m],meth[b][m]) for m in set(meth[a])&set(meth[b]))
        if shared>=2: edges.append({"s":a,"t":b,"w":min(shared,6)})
    nodes = [{"id":t,"n":len(BY_THEME[t]),"stage":STAGE_OF.get(t,6)} for t in themes]
    o = [HEAD.format(title="Idea Graph", i="", h="", g="on")]
    o.append('<div class="kick">the idea graph</div><h1>The themes, wired by shared methods</h1>')
    o.append('<p class="lead">Each theme is a dot, sized by paper count and colored by its stage in <a href="hub.html">the machine</a>. Two themes are linked when they lean on the same methods — the field\'s real cross-currents (diffusion crossing from generation into science, RL into alignment). Drag a dot; click to open the theme.</p>')
    o.append('<div class="legend">'+"".join(f'<span><i class="dot" style="background:{COLORS[i]}"></i>{esc(STAGES[i][0])}</span>' for i in range(len(STAGES)))+'</div>')
    o.append('<canvas id="g"></canvas>')
    o.append(f'<script>const NODES={json.dumps(nodes)};const EDGES={json.dumps(edges)};const COLORS={json.dumps(COLORS)};const SLUG={json.dumps({t:slug(t) for t in themes})};</script>')
    o.append(GRAPH_JS); o.append(FOOT)
    open(f"{SITE}/idea-graph.html","w").write("\n".join(o))

GRAPH_JS = r"""<script>
const cv=document.getElementById('g'),ctx=cv.getContext('2d');let W,H;
function size(){const r=cv.getBoundingClientRect();cv.width=r.width*devicePixelRatio;cv.height=r.height*devicePixelRatio;ctx.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);}
size();addEventListener('resize',size);const w=()=>cv.getBoundingClientRect().width,h=()=>cv.getBoundingClientRect().height;
NODES.forEach((n,i)=>{n.x=w()/2+Math.cos(i)*220+Math.random()*30;n.y=h()/2+Math.sin(i*1.6)*180+Math.random()*30;n.vx=0;n.vy=0;n.r=6+Math.sqrt(n.n)*1.3;});
const id2i={};NODES.forEach((n,i)=>id2i[n.id]=i);const E=EDGES.map(e=>({s:id2i[e.s],t:id2i[e.t],w:e.w}));let drag=null,hov=null;
function tick(){for(let i=0;i<NODES.length;i++){const a=NODES[i];for(let j=i+1;j<NODES.length;j++){const b=NODES[j];let dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy)||1;const rp=3200/(d*d);a.vx-=dx/d*rp;a.vy-=dy/d*rp;b.vx+=dx/d*rp;b.vy+=dy/d*rp;}}
for(const e of E){const a=NODES[e.s],b=NODES[e.t];let dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy)||1;const f=(d-140)*0.008*e.w;a.vx+=dx/d*f;a.vy+=dy/d*f;b.vx-=dx/d*f;b.vy-=dy/d*f;}
const cx=w()/2,cy=h()/2;for(const n of NODES){n.vx+=(cx-n.x)*0.003;n.vy+=(cy-n.y)*0.003;n.vx*=0.86;n.vy*=0.86;if(n!==drag){n.x+=n.vx;n.y+=n.vy;}n.x=Math.max(60,Math.min(w()-60,n.x));n.y=Math.max(30,Math.min(h()-30,n.y));}}
function draw(){ctx.clearRect(0,0,w(),h());for(const e of E){const a=NODES[e.s],b=NODES[e.t];ctx.strokeStyle='rgba(91,155,213,'+(0.08+0.13*e.w)+')';ctx.lineWidth=e.w;ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();}
for(const n of NODES){ctx.beginPath();ctx.arc(n.x,n.y,n===hov?n.r+2:n.r,0,7);ctx.fillStyle=COLORS[n.stage];ctx.fill();ctx.strokeStyle='#0a0e14';ctx.lineWidth=2;ctx.stroke();ctx.fillStyle=n===hov?'#e6edf3':'#9fb0c3';ctx.font=(n===hov?'700 ':'')+'12px system-ui';ctx.fillText(n.id,n.x+n.r+4,n.y+4);}}
function loop(){tick();draw();requestAnimationFrame(loop);}loop();
function at(x,y){for(const n of NODES)if(Math.hypot(n.x-x,n.y-y)<n.r+4)return n;return null;}
cv.addEventListener('mousemove',e=>{const r=cv.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;if(drag){drag.x=x;drag.y=y;}else{hov=at(x,y);cv.style.cursor=hov?'pointer':'default';}});
cv.addEventListener('mousedown',e=>{const r=cv.getBoundingClientRect();drag=at(e.clientX-r.left,e.clientY-r.top);});addEventListener('mouseup',()=>drag=null);
cv.addEventListener('click',e=>{const r=cv.getBoundingClientRect();const n=at(e.clientX-r.left,e.clientY-r.top);if(n)location.href='theme-'+SLUG[n.id]+'.html';});
</script>"""

if __name__=="__main__":
    build_theme_pages(); build_index(); build_hub(); build_graph()
    print(f"built site/: index + hub + idea-graph + {len(BY_THEME)} theme pages ({len(MERGED)} papers)")
