#!/usr/bin/env python3
"""Mine the corpus for math primitives → per-primitive input files for the
Mathematics Capstone. Each primitive = a family, a diagram type, a seed equation,
and the real explainers that use it (so every capstone page links back into the
corpus). Grounded in what the 1,360 explainers actually contain, not a guess.
"""
import json, glob, re, collections, os

specs = glob.glob("specs/*-or-*.json")
blobs = []
for f in specs:
    try: d = json.load(open(f))
    except: continue
    if not isinstance(d, dict): continue
    m = d.get("math", {})
    txt = ""
    if isinstance(m, dict):
        txt = " ".join(str(m.get(k, "")) for k in ("h2", "words", "equation", "note"))
        for sym in m.get("symbols", []) or []:
            if isinstance(sym, list): txt += " " + " ".join(str(x) for x in sym)
        w = m.get("worked", {})
        if isinstance(w, dict): txt += " " + str(w.get("title", "")) + " " + " ".join(str(x) for x in w.get("lines", []))
    # also mine mechanism/hidden text for primitives that live outside the math box
    for k in ("mechanism", "hidden", "object"):
        sec = d.get(k, {})
        if isinstance(sec, dict): txt += " " + " ".join(str(p) for p in sec.get("paras", []) or [])
    blobs.append({"slug": os.path.basename(f)[:-5], "title": d.get("title", "")[:60],
                  "family": d.get("family", ""), "txt": txt.lower()})

# (slug, name, family, diagram_type, seed_equation, regex)
P = [
 # ---- Probability & Information
 ("softmax","Softmax","Probability & Information","softmax","p_i = e^{z_i} / \\sum_j e^{z_j}",r"softmax"),
 ("sigmoid","Sigmoid / logistic","Probability & Information","sigmoid","\\sigma(x)=1/(1+e^{-x})",r"sigmoid|logistic"),
 ("cross-entropy","Cross-entropy & log-likelihood","Probability & Information","crossentropy","L=-\\sum_i y_i \\log p_i",r"cross.?entropy|log.?likelihood|negative log|nll"),
 ("entropy","Entropy","Probability & Information","entropy","H(p)=-\\sum_i p_i \\log p_i",r"\bentropy\b"),
 ("kl-divergence","KL divergence","Probability & Information","kl","D_{KL}(p\\|q)=\\sum_i p_i \\log(p_i/q_i)",r"\bkl\b|kullback|divergence"),
 ("mutual-information","Mutual information & InfoNCE","Probability & Information","mutualinfo","I(X;Y)=H(X)-H(X|Y)",r"mutual info|infonce"),
 ("bayes","Bayes' rule & posteriors","Probability & Information","bayes","p(\\theta|x)=p(x|\\theta)p(\\theta)/p(x)",r"bayes|posterior"),
 ("gaussian","The Gaussian","Probability & Information","gaussian","\\mathcal{N}(x;\\mu,\\sigma^2)",r"gaussian|normal distribution|bell curve"),
 ("expectation","Expectation","Probability & Information","expectation","E[f(x)]=\\sum_x p(x) f(x)",r"expectation|\\mathbb\{?e\}?\[|expected value"),
 ("wasserstein","Wasserstein / optimal transport","Probability & Information","wasserstein","W(p,q)=\\inf_\\gamma E\\|x-y\\|",r"wasserstein|optimal transport|earth mover"),
 ("fisher","Fisher information","Probability & Information","fisher","F=E[\\nabla\\log p \\nabla\\log p^T]",r"fisher information|natural gradient"),
 # ---- Linear Algebra
 ("matmul","Matrix multiplication","Linear Algebra","matmul","(Wx)_i=\\sum_j W_{ij} x_j",r"matrix mult|matmul|weight matrix|\bwx\b"),
 ("dot-product","Dot product & cosine similarity","Linear Algebra","dotproduct","a\\cdot b=\\|a\\|\\|b\\|\\cos\\theta",r"dot product|inner product|cosine similar"),
 ("norm","Vector norms (L1 / L2)","Linear Algebra","norm","\\|x\\|_2=\\sqrt{\\sum_i x_i^2}",r"l2 norm|l1 norm|euclidean|\\ell_2|\\ell_1|magnitude"),
 ("low-rank","Low-rank factorization (LoRA)","Linear Algebra","lowrank","W \\approx A B, \\; A\\in R^{d\\times r}",r"low.?rank|factoriz|lora|rank-"),
 ("svd","SVD, eigenvectors & PCA","Linear Algebra","svd","A=U\\Sigma V^T",r"\bsvd\b|singular value|eigen|principal component|\bpca\b|spectral"),
 ("attention","Attention (QK^T)","Linear Algebra","attention","A=\\mathrm{softmax}(QK^T/\\sqrt{d})V",r"attention"),
 ("convolution","Convolution","Linear Algebra","convolution","(f*g)(t)=\\sum_\\tau f(\\tau)g(t-\\tau)",r"convolution|\bconv\b"),
 ("kernel","Kernels & the Gram matrix","Linear Algebra","kernel","K_{ij}=\\phi(x_i)\\cdot\\phi(x_j)",r"\bkernel\b|gram matrix|rkhs"),
 ("spectral-norm","Spectral norm & Lipschitz","Linear Algebra","spectralnorm","\\|W\\|_2=\\sigma_{max}(W)",r"spectral norm|lipschitz|largest singular"),
 # ---- Optimization & Calculus
 ("gradient","The gradient","Optimization & Calculus","gradient","\\nabla f=(\\partial f/\\partial x_1,\\dots)",r"gradient|\\nabla|partial derivative"),
 ("gradient-descent","Gradient descent","Optimization & Calculus","gd","\\theta \\leftarrow \\theta-\\eta\\nabla L",r"gradient descent|learning rate|step size|update rule"),
 ("momentum","Momentum & Adam","Optimization & Calculus","momentum","v\\leftarrow\\beta v+\\nabla L",r"momentum|\badam\b|rmsprop|adaptive learning"),
 ("hessian","Curvature: Jacobian & Hessian","Optimization & Calculus","hessian","H_{ij}=\\partial^2 L/\\partial\\theta_i\\partial\\theta_j",r"jacobian|hessian|second derivative|curvature"),
 ("argmax","Argmax & argmin","Optimization & Calculus","argmax","x^*=\\arg\\max_x f(x)",r"argmax|argmin|arg\\max|arg\\min"),
 ("regularization","Regularization & penalties","Optimization & Calculus","regularization","L=L_0+\\lambda\\|\\theta\\|^2",r"regulari|penalty|weight decay"),
 ("lagrangian","Constraints & Lagrangians","Optimization & Calculus","lagrangian","L=f(x)+\\lambda g(x)",r"lagrang|constraint|kkt|dual problem"),
 ("em","Expectation-Maximization","Optimization & Calculus","em","E-step then M-step",r"expectation.?maximiz|\bem\b algorithm|e-step|m-step"),
 # ---- Generative & Sampling
 ("diffusion","Diffusion & score matching","Generative & Sampling","diffusion","x_t=\\sqrt{\\bar\\alpha_t}x_0+\\sqrt{1-\\bar\\alpha_t}\\epsilon",r"diffusion|score function|denois|noise schedule|reverse process"),
 ("elbo","Variational inference & the ELBO","Generative & Sampling","elbo","\\log p(x)\\ge E_q[\\log p(x,z)-\\log q(z)]",r"elbo|variational|evidence lower"),
 ("reparam","The reparameterization trick","Generative & Sampling","reparam","z=\\mu+\\sigma\\odot\\epsilon",r"reparameteriz|z\\s*=\\s*\\mu"),
 ("contrastive","Contrastive learning (InfoNCE)","Generative & Sampling","contrastive","L=-\\log\\frac{e^{s_+}}{\\sum e^{s}}",r"contrastive|positive pair|negative pair|infonce"),
 ("importance-sampling","Importance sampling","Generative & Sampling","importance","E_p[f]=E_q[f\\,p/q]",r"importance sampling|importance weight|propensity"),
 ("gumbel","Gumbel-softmax & straight-through","Generative & Sampling","gumbel","y=\\mathrm{softmax}((\\log\\pi+g)/\\tau)",r"gumbel|straight.?through|discrete sampling"),
 # ---- Sequential & Reinforcement Learning
 ("value-function","Reward, value & Bellman","Sequential & RL","value","V(s)=E[\\sum_t \\gamma^t r_t]",r"reward|value function|bellman|discount"),
 ("policy-gradient","Policy gradient (REINFORCE)","Sequential & RL","policygrad","\\nabla J=E[\\nabla\\log\\pi\\,A]",r"policy gradient|reinforce|log.?prob.*reward"),
 ("advantage","Advantage & PPO clipping","Sequential & RL","ppo","\\min(r A,\\mathrm{clip}(r)A)",r"advantage|\bppo\b|gae|clip.*ratio"),
]

for slug, name, fam, dia, eq, rx in P:
    users = [b for b in blobs if re.search(rx, b["txt"], re.I)]
    links = [{"slug": b["slug"], "title": b["title"], "theme": b["family"]} for b in users[:12]]
    themes = collections.Counter(b["family"] for b in users)
    json.dump({"slug": slug, "name": name, "capstone_family": fam, "diagram": dia,
               "seed_equation": eq, "count": len(users),
               "themes": themes.most_common(6), "links": links},
              open(f"data/math_in/{slug}.json", "w"), indent=1)

print(f"wrote {len(P)} primitive input files across 5 families")
for fam in ["Probability & Information","Linear Algebra","Optimization & Calculus","Generative & Sampling","Sequential & RL"]:
    ps=[p for p in P if p[2]==fam]
    print(f"  {fam}: {len(ps)}")
