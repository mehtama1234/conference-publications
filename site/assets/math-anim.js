/* Mathematics Capstone — live canvas diagrams, one per primitive.
   Each <canvas data-anim="TYPE"> gets an animated first-principles picture.
   No libraries; pure 2D canvas. Colours pull from the site's dark-cream theme. */
(function () {
  const CREAM = "#e9e2d0", INK = "#1a1712", MUT = "#a99", HOT = "#d98a3d",
        GOOD = "#6ea36e", BAD = "#c96a5a", LINE = "#7c6f57", COOL = "#6b8fb5";
  const TAU = Math.PI * 2;

  function setup(cv) {
    const dpr = Math.min(2, window.devicePixelRatio || 1);
    const w = cv.clientWidth || 520, h = cv.clientHeight || 260;
    cv.width = w * dpr; cv.height = h * dpr;
    const c = cv.getContext("2d"); c.scale(dpr, dpr);
    c.__small = h < 160;   // card mini: suppress long descriptive captions
    return { c, w, h };
  }
  function clear(c, w, h) { c.clearRect(0, 0, w, h); }
  function txt(c, s, x, y, col, size, al) {
    if (c.__small && String(s).length > 16) return;   // skip captions on card minis
    c.fillStyle = col || MUT; c.font = `${size || 12}px ui-monospace,monospace`;
    c.textAlign = al || "left"; c.fillText(s, x, y);
  }
  const lerp = (a, b, t) => a + (b - a) * t;
  const ease = t => 0.5 - 0.5 * Math.cos(Math.min(1, Math.max(0, t)) * Math.PI);

  // ---- registry of drawers: fn(ctx) → draw(t) where t is seconds ----
  const D = {};

  // Probability & Information -------------------------------------------------
  D.softmax = ({ c, w, h }) => {
    const z = [2.0, 0.5, 1.3, -0.4, 0.9], n = z.length, bw = w / (n * 2);
    return (t) => { clear(c, w, h); const T = ease((t % 4) / 2.4);
      const ex = z.map(v => Math.exp(v * T)); const s = ex.reduce((a, b) => a + b, 0);
      for (let i = 0; i < n; i++) { const p = ex[i] / s, x = w * 0.12 + i * bw * 1.7;
        const raw = (z[i] + 1) / 4;
        c.fillStyle = LINE; c.fillRect(x, h - 30 - raw * 60, bw, raw * 60);
        c.fillStyle = HOT; const bh = p * 150 * T; c.fillRect(x, h - 30 - bh - (1 - T) * raw * 0, bw, bh);
        txt(c, p.toFixed(2), x + bw / 2, h - 12, CREAM, 11, "center"); }
      txt(c, "raw scores  →  exp  →  shares that sum to 1", w / 2, 22, MUT, 12, "center"); };
  };
  D.sigmoid = ({ c, w, h }) => (t) => { clear(c, w, h);
    c.strokeStyle = LINE; c.beginPath(); c.moveTo(30, h / 2); c.lineTo(w - 20, h / 2); c.stroke();
    c.strokeStyle = HOT; c.lineWidth = 2; c.beginPath();
    for (let i = 0; i <= 100; i++) { const x = -6 + 12 * i / 100, y = 1 / (1 + Math.exp(-x));
      const px = 30 + (i / 100) * (w - 50), py = h - 30 - y * (h - 60); i ? c.lineTo(px, py) : c.moveTo(px, py); } c.stroke();
    const xx = Math.sin(t * 1.1) * 5, yy = 1 / (1 + Math.exp(-xx));
    const px = 30 + ((xx + 6) / 12) * (w - 50), py = h - 30 - yy * (h - 60);
    c.fillStyle = CREAM; c.beginPath(); c.arc(px, py, 5, 0, TAU); c.fill();
    txt(c, "squashes any number into 0…1", w / 2, 20, MUT, 12, "center"); c.lineWidth = 1; };
  D.crossentropy = ({ c, w, h }) => (t) => { clear(c, w, h); const T = ease((t % 5) / 3);
    const pred = [lerp(0.25, 0.9, T), lerp(0.3, 0.05, T), lerp(0.25, 0.03, T), lerp(0.2, 0.02, T)];
    const bw = 46; for (let i = 0; i < 4; i++) { const x = 60 + i * 70;
      c.strokeStyle = i === 0 ? GOOD : LINE; c.lineWidth = i === 0 ? 2 : 1; c.strokeRect(x, h - 30 - 90, bw, 90);
      c.fillStyle = i === 0 ? GOOD : LINE; c.fillRect(x, h - 30 - pred[i] * 90, bw, pred[i] * 90);
      txt(c, pred[i].toFixed(2), x + bw / 2, h - 12, CREAM, 11, "center"); }
    const loss = -Math.log(pred[0]); txt(c, "true class = green box", 60, 24, MUT, 12);
    txt(c, "loss = -log(p_true) = " + loss.toFixed(2), w - 20, 24, HOT, 13, "right"); c.lineWidth = 1; };
  D.entropy = ({ c, w, h }) => (t) => { clear(c, w, h); const u = 0.5 + 0.5 * Math.sin(t * 0.7);
    const base = [0.7, 0.15, 0.1, 0.05], n = 4; let H = 0;
    const p = base.map(b => lerp(b, 0.25, u)); const s = p.reduce((a, b) => a + b); const pn = p.map(x => x / s);
    pn.forEach(x => H -= x * Math.log2(x)); const bw = 60;
    for (let i = 0; i < n; i++) { const x = 60 + i * 80; c.fillStyle = COOL;
      c.fillRect(x, h - 30 - pn[i] * 150, bw, pn[i] * 150); }
    txt(c, "peaked = low surprise ⟷ flat = high surprise", w / 2, 22, MUT, 12, "center");
    txt(c, "H = " + H.toFixed(2) + " bits", w - 20, h - 12, HOT, 13, "right"); };
  D.kl = ({ c, w, h }) => (t) => { clear(c, w, h); const sh = Math.sin(t * 0.6) * 1.4;
    const bell = (mu, sd, x) => Math.exp(-((x - mu) ** 2) / (2 * sd * sd));
    const draw = (mu, col) => { c.strokeStyle = col; c.lineWidth = 2; c.beginPath();
      for (let i = 0; i <= 120; i++) { const x = -6 + 12 * i / 120, y = bell(mu, 1.3, x);
        const px = 20 + (i / 120) * (w - 40), py = h - 26 - y * (h - 60); i ? c.lineTo(px, py) : c.moveTo(px, py); } c.stroke(); };
    // shaded divergence
    c.fillStyle = "rgba(217,138,61,0.18)"; c.beginPath(); c.moveTo(20, h - 26);
    for (let i = 0; i <= 120; i++) { const x = -6 + 12 * i / 120; const d = Math.abs(bell(0, 1.3, x) - bell(sh, 1.3, x));
      c.lineTo(20 + (i / 120) * (w - 40), h - 26 - d * (h - 60)); } c.lineTo(w - 20, h - 26); c.fill();
    draw(0, COOL); draw(sh, HOT); txt(c, "p", 40, 30, COOL, 13); txt(c, "q", 60, 30, HOT, 13);
    txt(c, "KL = area between the two curves", w / 2, h - 10, MUT, 12, "center"); c.lineWidth = 1; };
  D.mutualinfo = ({ c, w, h }) => (t) => { clear(c, w, h); const o = 40 + 30 * (1 + Math.sin(t * 0.6));
    const cx = w / 2, cy = h / 2, r = 70;
    c.fillStyle = "rgba(107,143,181,0.25)"; c.beginPath(); c.arc(cx - o / 2, cy, r, 0, TAU); c.fill();
    c.fillStyle = "rgba(217,138,61,0.25)"; c.beginPath(); c.arc(cx + o / 2, cy, r, 0, TAU); c.fill();
    txt(c, "H(X)", cx - o / 2 - r + 20, cy, COOL, 12); txt(c, "H(Y)", cx + o / 2 + 20, cy, HOT, 12);
    txt(c, "overlap = shared information I(X;Y)", w / 2, h - 12, MUT, 12, "center"); };
  D.bayes = ({ c, w, h }) => (t) => { clear(c, w, h); const T = ease((t % 5) / 3);
    const bars = (arr, x0, lab, col) => { arr.forEach((v, i) => { const x = x0 + i * 34;
      c.fillStyle = col; c.fillRect(x, h - 40 - v * 90, 26, v * 90); }); txt(c, lab, x0 + 40, h - 16, MUT, 12, "center"); };
    const prior = [.5, .3, .2], like = [.2, .5, .8]; const post0 = prior.map((p, i) => p * like[i]);
    const s = post0.reduce((a, b) => a + b); const post = post0.map(x => lerp(1 / 3, x / s, T));
    bars(prior, 40, "prior", LINE); bars(like, 190, "evidence", COOL); bars(post, 350, "posterior", HOT);
    txt(c, "belief updated by evidence", w / 2, 22, MUT, 12, "center"); };
  D.gaussian = ({ c, w, h }) => (t) => { clear(c, w, h); const mu = Math.sin(t * 0.6) * 2, sd = 1 + 0.6 * (1 + Math.sin(t * 0.9));
    c.strokeStyle = HOT; c.lineWidth = 2; c.beginPath();
    for (let i = 0; i <= 140; i++) { const x = -6 + 12 * i / 140, y = Math.exp(-((x - mu) ** 2) / (2 * sd * sd));
      const px = 20 + (i / 140) * (w - 40), py = h - 26 - y * (h - 60); i ? c.lineTo(px, py) : c.moveTo(px, py); } c.stroke();
    txt(c, "μ shifts the centre · σ sets the width", w / 2, 22, MUT, 12, "center"); c.lineWidth = 1; };
  D.expectation = ({ c, w, h }) => { let sum = 0, n = 0; return (t) => { clear(c, w, h);
    if (Math.random() < 0.3) { sum += Math.random() * 6 - 1; n++; } const avg = n ? sum / n : 0;
    c.strokeStyle = LINE; c.beginPath(); c.moveTo(30, h - 40); c.lineTo(w - 20, h - 40); c.stroke();
    for (let i = 0; i < 40; i++) { const x = 30 + Math.random() * (w - 50); c.fillStyle = "rgba(107,143,181,0.5)";
      c.fillRect(x, h - 42, 2, 2); } const ax = 30 + ((avg + 1) / 6) * (w - 50);
    c.fillStyle = HOT; c.fillRect(ax, h - 60, 3, 40); txt(c, "running average → E[x] = " + avg.toFixed(2), w / 2, 24, MUT, 12, "center"); }; };
  D.wasserstein = ({ c, w, h }) => (t) => { clear(c, w, h); const T = (t % 5) / 5;
    for (let i = 0; i < 5; i++) { const x0 = 60 + i * 24, x1 = w - 200 + i * 24;
      const x = lerp(x0, x1, ease(T)); c.fillStyle = HOT; c.fillRect(x, h - 40 - 40, 18, 40);
      c.strokeStyle = LINE; c.strokeRect(x0, h - 40 - 40, 18, 40); c.strokeRect(x1, h - 40 - 40, 18, 40); }
    txt(c, "least total 'dirt moved' from pile p to pile q", w / 2, 24, MUT, 12, "center"); };
  D.fisher = ({ c, w, h }) => (t) => { clear(c, w, h); const sharp = 1 + 1.5 * (1 + Math.sin(t * 0.7));
    c.strokeStyle = HOT; c.lineWidth = 2; c.beginPath();
    for (let i = 0; i <= 120; i++) { const x = -3 + 6 * i / 120, y = Math.exp(-sharp * x * x);
      const px = 30 + (i / 120) * (w - 60), py = h - 30 - y * (h - 70); i ? c.lineTo(px, py) : c.moveTo(px, py); } c.stroke();
    txt(c, "sharper peak = more information about the parameter", w / 2, 22, MUT, 12, "center"); c.lineWidth = 1; };

  // Linear Algebra ------------------------------------------------------------
  D.matmul = ({ c, w, h }) => (t) => { clear(c, w, h); const row = Math.floor(t % 3);
    const gx = 60, gy = 60, cell = 34;
    for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++) { c.strokeStyle = LINE;
      c.fillStyle = i === row ? "rgba(217,138,61,0.3)" : "transparent"; c.fillRect(gx + j * cell, gy + i * cell, cell, cell);
      c.strokeRect(gx + j * cell, gy + i * cell, cell, cell); }
    for (let i = 0; i < 3; i++) { c.strokeStyle = i === row ? HOT : LINE; c.strokeRect(gx + 3.4 * cell, gy + i * cell, cell, cell); }
    txt(c, "W", gx + cell, gy - 12, MUT, 12); txt(c, "x", gx + 3.4 * cell + 8, gy - 12, MUT, 12);
    txt(c, "each output row = that row of W · the vector x", w / 2, h - 16, MUT, 12, "center"); };
  D.dotproduct = ({ c, w, h }) => (t) => { clear(c, w, h); const cx = w / 2, cy = h - 40, a = t * 0.6;
    const L = 90; const draw = (ang, col) => { c.strokeStyle = col; c.lineWidth = 3; c.beginPath();
      c.moveTo(cx, cy); c.lineTo(cx + Math.cos(ang) * L, cy - Math.sin(ang) * L); c.stroke(); };
    draw(0.6, COOL); draw(0.6 + 0.8 + 0.5 * Math.sin(t), HOT);
    const th = 0.8 + 0.5 * Math.sin(t); txt(c, "cos θ = " + Math.cos(th).toFixed(2) + "  (1=aligned, 0=orthogonal)", w / 2, 24, MUT, 12, "center"); c.lineWidth = 1; };
  D.norm = ({ c, w, h }) => (t) => { clear(c, w, h); const cx = w / 2, cy = h / 2, R = 70;
    c.strokeStyle = COOL; c.lineWidth = 2; c.beginPath(); c.arc(cx, cy, R, 0, TAU); c.stroke();
    c.strokeStyle = HOT; c.beginPath(); c.moveTo(cx, cy - R); c.lineTo(cx + R, cy); c.lineTo(cx, cy + R); c.lineTo(cx - R, cy); c.closePath(); c.stroke();
    txt(c, "L2 = circle (spread)", cx + R + 6, cy - 10, COOL, 12); txt(c, "L1 = diamond (sparse)", cx + R + 6, cy + 14, HOT, 12); c.lineWidth = 1; };
  D.lowrank = ({ c, w, h }) => (t) => { clear(c, w, h); const r = 1 + Math.floor(2 + 2 * Math.sin(t * 0.5));
    c.strokeStyle = LINE; c.strokeRect(40, 50, 110, 110); txt(c, "W  (d×d)", 95, 40, MUT, 12, "center");
    c.fillStyle = "rgba(217,138,61,0.25)"; c.fillRect(40, 50, 110, 110);
    c.strokeStyle = HOT; c.strokeRect(200, 50, r * 14, 110); txt(c, "A", 200 + r * 7, 40, HOT, 12, "center");
    c.strokeRect(200 + r * 14 + 20, 50, 110, r * 14); txt(c, "B", 200 + r * 14 + 75, 40, HOT, 12, "center");
    txt(c, "store two thin slabs (rank r=" + r + ") instead of the full square", w / 2, h - 14, MUT, 12, "center"); };
  D.svd = ({ c, w, h }) => (t) => { clear(c, w, h); const cx = w / 2, cy = h / 2;
    for (let i = 0; i < 60; i++) { const a = (i / 60) * TAU; const x = Math.cos(a) * 90, y = Math.sin(a) * 40;
      const r = t * 0.4; const rx = x * Math.cos(r) - y * Math.sin(r), ry = x * Math.sin(r) + y * Math.cos(r);
      c.fillStyle = "rgba(107,143,181,0.6)"; c.fillRect(cx + rx, cy + ry, 2.5, 2.5); }
    const r = t * 0.4; c.strokeStyle = HOT; c.lineWidth = 2; c.beginPath(); c.moveTo(cx, cy);
    c.lineTo(cx + Math.cos(r) * 90, cy + Math.sin(r) * 90); c.stroke();
    txt(c, "principal axis = direction of most spread", w / 2, 22, MUT, 12, "center"); c.lineWidth = 1; };
  D.attention = ({ c, w, h }) => (t) => { clear(c, w, h); const n = 6, cell = 28, gx = w / 2 - n * cell / 2, gy = 50;
    const q = Math.floor(t % n); for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) {
      const s = i === q ? Math.exp(-Math.abs(i - j) * 0.6) : 0.05; c.fillStyle = `rgba(217,138,61,${s})`;
      c.fillRect(gx + j * cell, gy + i * cell, cell - 2, cell - 2); c.strokeStyle = "#3a332a"; c.strokeRect(gx + j * cell, gy + i * cell, cell - 2, cell - 2); }
    txt(c, "one query row lights up which keys it attends to", w / 2, h - 16, MUT, 12, "center");
    txt(c, "softmax(QKᵀ)", w / 2, 32, MUT, 12, "center"); };
  D.convolution = ({ c, w, h }) => (t) => { clear(c, w, h); const g = 40, cell = 22, K = Math.floor(t * 3) % 6;
    for (let i = 0; i < 6; i++) for (let j = 0; j < 6; j++) { c.strokeStyle = LINE;
      c.strokeRect(g + j * cell, 50 + i * cell, cell, cell); }
    const kr = Math.floor(K / 4), kc = K % 4; c.strokeStyle = HOT; c.lineWidth = 2;
    c.strokeRect(g + kc * cell, 50 + kr * cell, cell * 3, cell * 3); c.lineWidth = 1;
    txt(c, "a small kernel slides across, summing a local patch", w / 2, h - 14, MUT, 12, "center"); };
  D.kernel = ({ c, w, h }) => (t) => { clear(c, w, h); const T = ease((t % 5) / 3);
    for (let i = 0; i < 24; i++) { const a = (i / 24) * TAU, inner = i % 2 === 0;
      const r = inner ? 40 : 90; const x = w / 2 + Math.cos(a) * r, y0 = h - 40, lift = inner ? 0 : 70 * T;
      c.fillStyle = inner ? HOT : COOL; c.beginPath(); c.arc(x, y0 - Math.sin(a) * r * 0.3 - lift, 4, 0, TAU); c.fill(); }
    txt(c, "lift points to a higher dimension where a line can split them", w / 2, 22, MUT, 12, "center"); };
  D.spectralnorm = ({ c, w, h }) => (t) => { clear(c, w, h); const cx = w / 2, cy = h / 2, s = 1.4 + 0.5 * Math.sin(t * 0.7);
    c.strokeStyle = LINE; c.beginPath(); c.arc(cx, cy, 50, 0, TAU); c.stroke();
    c.strokeStyle = HOT; c.lineWidth = 2; c.beginPath(); c.ellipse(cx, cy, 50 * s, 50 / s, 0, 0, TAU); c.stroke();
    txt(c, "W stretches the unit circle; biggest stretch = spectral norm", w / 2, 22, MUT, 12, "center"); c.lineWidth = 1; };

  // Optimization & Calculus ---------------------------------------------------
  const bowl = (x, y) => (x * x + y * y);
  D.gradient = ({ c, w, h }) => (t) => { clear(c, w, h);
    for (let gx = 40; gx < w - 20; gx += 46) for (let gy = 40; gy < h - 20; gy += 46) {
      const x = (gx - w / 2) / 90, y = (gy - h / 2) / 60; const dx = 2 * x, dy = 2 * y, m = Math.hypot(dx, dy) + 1e-6;
      c.strokeStyle = HOT; c.beginPath(); c.moveTo(gx, gy); c.lineTo(gx + dx / m * 14, gy + dy / m * 14); c.stroke();
      c.fillStyle = HOT; c.fillRect(gx + dx / m * 14 - 1.5, gy + dy / m * 14 - 1.5, 3, 3); }
    txt(c, "arrows point uphill; gradient descent walks the other way", w / 2, 20, MUT, 12, "center"); };
  D.gd = ({ c, w, h }) => { let x = 5; return (t) => { clear(c, w, h);
    c.strokeStyle = LINE; c.lineWidth = 2; c.beginPath();
    for (let i = 0; i <= 120; i++) { const xx = -6 + 12 * i / 120, y = 0.12 * xx * xx;
      const px = 30 + (i / 120) * (w - 50), py = h - 40 - y * 30; i ? c.lineTo(px, py) : c.moveTo(px, py); } c.stroke();
    x -= 0.12 * (2 * 0.12 * x) * 8; if (Math.abs(x) < 0.05) x = 5 * (Math.random() > .5 ? 1 : -1);
    const px = 30 + ((x + 6) / 12) * (w - 50), py = h - 40 - 0.12 * x * x * 30;
    c.fillStyle = HOT; c.beginPath(); c.arc(px, py, 6, 0, TAU); c.fill();
    txt(c, "θ ← θ − η·slope : roll downhill by small steps", w / 2, 22, MUT, 12, "center"); c.lineWidth = 1; }; };
  D.momentum = ({ c, w, h }) => { let x = 5, v = 0; return (t) => { clear(c, w, h);
    c.strokeStyle = LINE; c.lineWidth = 2; c.beginPath();
    for (let i = 0; i <= 120; i++) { const xx = -6 + 12 * i / 120, y = 0.1 * xx * xx;
      const px = 30 + (i / 120) * (w - 50), py = h - 40 - y * 30; i ? c.lineTo(px, py) : c.moveTo(px, py); } c.stroke();
    v = 0.9 * v - 0.1 * (2 * 0.1 * x); x += v; if (Math.abs(x) > 6) { x = 5; v = 0; }
    const px = 30 + ((x + 6) / 12) * (w - 50), py = h - 40 - 0.1 * x * x * 30;
    c.fillStyle = HOT; c.beginPath(); c.arc(px, py, 6, 0, TAU); c.fill();
    txt(c, "velocity builds up → rolls through small bumps", w / 2, 22, MUT, 12, "center"); c.lineWidth = 1; }; };
  D.hessian = ({ c, w, h }) => (t) => { clear(c, w, h); const saddle = Math.sin(t * 0.5) > 0;
    for (let i = 0; i < 30; i++) { const a = (i / 30) * TAU;
      for (let r = 10; r < 80; r += 20) { const x = w / 2 + Math.cos(a) * r, z = saddle ? (r * r * Math.cos(2 * a)) : r * r;
        const y = h / 2 - z / 90; c.fillStyle = COOL; c.fillRect(x, y, 2, 2); } }
    txt(c, saddle ? "saddle: curves up one way, down another" : "bowl: curves up everywhere (positive curvature)", w / 2, 22, MUT, 12, "center"); };
  D.argmax = ({ c, w, h }) => (t) => { clear(c, w, h); let best = 0, bx = 0;
    c.strokeStyle = LINE; c.lineWidth = 2; c.beginPath();
    for (let i = 0; i <= 160; i++) { const xx = i / 160; const y = Math.sin(xx * 9) * 0.4 + Math.sin(xx * 3 + 1) * 0.5 + 1;
      if (y > best) { best = y; bx = xx; } const px = 30 + xx * (w - 50), py = h - 30 - y * 60;
      i ? c.lineTo(px, py) : c.moveTo(px, py); } c.stroke();
    const px = 30 + bx * (w - 50), py = h - 30 - best * 60; c.fillStyle = HOT; c.beginPath(); c.arc(px, py, 6, 0, TAU); c.fill();
    txt(c, "argmax = the input where the curve is highest", w / 2, 20, MUT, 12, "center"); c.lineWidth = 1; };
  D.regularization = ({ c, w, h }) => (t) => { clear(c, w, h); const lam = 0.5 + 0.5 * Math.sin(t * 0.6);
    const ws = [0.9, -0.7, 0.6, -0.4, 0.8, -0.5]; ws.forEach((wv, i) => { const x = 60 + i * 64;
      const shrunk = wv * (1 - lam * 0.8); c.fillStyle = LINE; c.fillRect(x, h / 2, 30, -wv * 60);
      c.fillStyle = HOT; c.fillRect(x, h / 2, 30, -shrunk * 60); });
    c.strokeStyle = MUT; c.beginPath(); c.moveTo(40, h / 2); c.lineTo(w - 20, h / 2); c.stroke();
    txt(c, "bigger λ pulls every weight toward zero", w / 2, 24, MUT, 12, "center"); };
  D.lagrangian = ({ c, w, h }) => (t) => { clear(c, w, h); const cx = w / 2, cy = h / 2;
    for (let r = 20; r < 100; r += 20) { c.strokeStyle = LINE; c.beginPath(); c.arc(cx - 40, cy, r, 0, TAU); c.stroke(); }
    c.strokeStyle = HOT; c.lineWidth = 2; c.beginPath(); c.moveTo(cx + 40, 40); c.lineTo(cx - 20, h - 30); c.stroke();
    const a = t * 0.5; c.fillStyle = GOOD; c.beginPath(); c.arc(cx + 10, cy - 20, 6, 0, TAU); c.fill();
    txt(c, "best point sits where the contours just touch the constraint line", w / 2, 22, MUT, 12, "center"); c.lineWidth = 1; };
  D.em = ({ c, w, h }) => (t) => { clear(c, w, h); const phase = Math.floor(t) % 2;
    const c1 = [w / 2 - 70, h / 2], c2 = [w / 2 + 70, h / 2];
    for (let i = 0; i < 40; i++) { const x = 60 + (i * 37) % (w - 120), y = 60 + (i * 53) % (h - 100);
      const d1 = Math.hypot(x - c1[0], y - c1[1]), d2 = Math.hypot(x - c2[0], y - c2[1]);
      c.fillStyle = d1 < d2 ? "rgba(107,143,181,0.7)" : "rgba(217,138,61,0.7)"; c.beginPath(); c.arc(x, y, 3, 0, TAU); c.fill(); }
    [c1, c2].forEach((cc, i) => { c.strokeStyle = i ? HOT : COOL; c.lineWidth = 2; c.beginPath(); c.arc(cc[0], cc[1], 50, 0, TAU); c.stroke(); });
    txt(c, phase ? "M-step: refit each blob to its points" : "E-step: assign points to nearest blob", w / 2, 22, MUT, 12, "center"); c.lineWidth = 1; };

  // Generative & Sampling -----------------------------------------------------
  D.diffusion = ({ c, w, h }) => { const pts = Array.from({ length: 60 }, (_, i) => ({ a: (i / 60) * TAU })); return (t) => { clear(c, w, h);
    const ph = (t % 6) / 6; const noise = ph < 0.5 ? ph * 2 : (1 - ph) * 2; const cx = w / 2, cy = h / 2;
    pts.forEach(p => { const r = 60; const nx = (Math.sin(p.a * 7) * 40) * noise, ny = (Math.cos(p.a * 5) * 40) * noise;
      c.fillStyle = HOT; c.beginPath(); c.arc(cx + Math.cos(p.a) * r + nx, cy + Math.sin(p.a) * r + ny, 2.5, 0, TAU); c.fill(); });
    txt(c, ph < 0.5 ? "forward: shape dissolves into noise" : "reverse: learn to denoise back to the shape", w / 2, 22, MUT, 12, "center"); }; };
  D.elbo = ({ c, w, h }) => (t) => { clear(c, w, h); const gap = 0.5 + 0.5 * (1 - ease((t % 5) / 3));
    const top = 60; c.fillStyle = LINE; c.fillRect(80, top, 40, 140); txt(c, "log p(x)", 100, top - 8, MUT, 12, "center");
    c.fillStyle = HOT; c.fillRect(200, top + gap * 100, 40, 140 - gap * 100); txt(c, "ELBO", 220, top - 8, HOT, 12, "center");
    txt(c, "maximise a lower bound we CAN compute; it rises to meet log p(x)", w / 2, h - 14, MUT, 12, "center"); };
  D.reparam = ({ c, w, h }) => (t) => { clear(c, w, h); const eps = Math.sin(t * 1.3);
    txt(c, "ε ~ N(0,1)  (fixed noise)", 40, 40, COOL, 13); txt(c, "z = μ + σ·ε", 40, 70, HOT, 14);
    const cx = 300, cy = h / 2 + 20; c.strokeStyle = LINE; c.beginPath(); c.moveTo(cx - 100, cy); c.lineTo(cx + 100, cy); c.stroke();
    c.fillStyle = COOL; c.beginPath(); c.arc(cx + eps * 40, cy, 5, 0, TAU); c.fill();
    c.fillStyle = HOT; c.beginPath(); c.arc(cx + 20 + eps * 70, cy - 40, 6, 0, TAU); c.fill();
    txt(c, "randomness moved outside → gradients can flow through μ,σ", w / 2, h - 12, MUT, 12, "center"); };
  D.contrastive = ({ c, w, h }) => (t) => { clear(c, w, h); const T = ease((t % 5) / 3); const cx = w / 2, cy = h / 2;
    c.fillStyle = INK; c.strokeStyle = CREAM; c.beginPath(); c.arc(cx, cy, 7, 0, TAU); c.stroke(); txt(c, "anchor", cx + 10, cy - 10, MUT, 11);
    for (let i = 0; i < 3; i++) { const a = i * 2; const r = lerp(110, 40, T); c.fillStyle = GOOD;
      c.beginPath(); c.arc(cx + Math.cos(a) * r, cy + Math.sin(a) * r, 5, 0, TAU); c.fill(); }
    for (let i = 0; i < 4; i++) { const a = i * 1.6 + 1; const r = lerp(70, 130, T); c.fillStyle = BAD;
      c.beginPath(); c.arc(cx + Math.cos(a) * r, cy + Math.sin(a) * r, 5, 0, TAU); c.fill(); }
    txt(c, "pull matches (green) in · push non-matches (red) away", w / 2, 22, MUT, 12, "center"); };
  D.importance = ({ c, w, h }) => (t) => { clear(c, w, h); const bell = (mu, x) => Math.exp(-((x - mu) ** 2) / 2);
    const drawC = (mu, col) => { c.strokeStyle = col; c.lineWidth = 2; c.beginPath();
      for (let i = 0; i <= 120; i++) { const x = -5 + 10 * i / 120, y = bell(mu, x);
        const px = 20 + (i / 120) * (w - 40), py = h - 30 - y * (h - 70); i ? c.lineTo(px, py) : c.moveTo(px, py); } c.stroke(); };
    drawC(-1.2, COOL); drawC(1.2, HOT);
    txt(c, "q", 90, 40, COOL, 13); txt(c, "p (target)", w - 120, 40, HOT, 13);
    txt(c, "sample from easy q, reweight by p/q to estimate under p", w / 2, h - 12, MUT, 12, "center"); c.lineWidth = 1; };
  D.gumbel = ({ c, w, h }) => (t) => { clear(c, w, h); const tau = 0.2 + 1.6 * (1 + Math.sin(t * 0.7));
    const logits = [1.2, 0.4, 0.9, 0.1]; const ex = logits.map(v => Math.exp(v / tau)); const s = ex.reduce((a, b) => a + b);
    ex.forEach((e, i) => { const x = 80 + i * 90, p = e / s; c.fillStyle = HOT; c.fillRect(x, h - 40 - p * 120, 46, p * 120);
      txt(c, p.toFixed(2), x + 23, h - 16, CREAM, 11, "center"); });
    txt(c, "low temperature → nearly a hard pick; high → soft blend", w / 2, 24, MUT, 12, "center"); };

  // Sequential & RL -----------------------------------------------------------
  D.value = ({ c, w, h }) => (t) => { clear(c, w, h); const g = 6, cell = 30, gx = w / 2 - g * cell / 2, gy = 40;
    const goal = [5, 0]; for (let i = 0; i < g; i++) for (let j = 0; j < g; j++) {
      const d = Math.abs(i - goal[1]) + Math.abs(j - goal[0]); const v = Math.max(0, 1 - d / 10) * (0.5 + 0.5 * Math.sin(t * 0.8 - d * 0.3 + 3));
      c.fillStyle = `rgba(110,163,110,${0.15 + v})`; c.fillRect(gx + j * cell, gy + i * cell, cell - 2, cell - 2); }
    c.fillStyle = HOT; c.fillRect(gx + goal[0] * cell, gy + goal[1] * cell, cell - 2, cell - 2);
    txt(c, "value = expected future reward; it flows out from the goal", w / 2, h - 14, MUT, 12, "center"); };
  D.policygrad = ({ c, w, h }) => (t) => { clear(c, w, h); const cx = 40, cy = h / 2;
    for (let k = 0; k < 5; k++) { const good = k % 2 === 0; c.strokeStyle = good ? GOOD : BAD;
      c.lineWidth = good ? 3 : 1; c.globalAlpha = good ? 0.9 : 0.4; c.beginPath(); c.moveTo(cx, cy);
      let x = cx, y = cy + (k - 2) * 20; for (let s = 0; s < 6; s++) { x += 60; y += (good ? -1 : 1) * (Math.random() * 20 - 5); c.lineTo(x, y); } c.stroke(); }
    c.globalAlpha = 1; c.lineWidth = 1; txt(c, "make high-reward trajectories more likely, low-reward less", w / 2, 22, MUT, 12, "center"); };
  D.ppo = ({ c, w, h }) => (t) => { clear(c, w, h); const cx = w / 2, cy = h / 2 + 20; const eps = 0.2;
    c.fillStyle = "rgba(110,163,110,0.15)"; c.fillRect(cx - 200 * eps, 40, 400 * eps, h - 80);
    c.strokeStyle = LINE; c.beginPath(); c.moveTo(60, cy); c.lineTo(w - 40, cy); c.stroke();
    const r = 1 + Math.sin(t * 0.8) * 0.6; const clipped = Math.max(1 - eps, Math.min(1 + eps, r));
    const px = cx + (clipped - 1) * 200; c.fillStyle = HOT; c.beginPath(); c.arc(px, cy, 7, 0, TAU); c.fill();
    txt(c, "clip the update ratio to [1−ε, 1+ε] so no step is too big", w / 2, 24, MUT, 12, "center"); };

  // ---- boot ----
  function run(cv) {
    const type = cv.getAttribute("data-anim"); if (!D[type]) { return; }
    const ctx = setup(cv); const draw = D[type](ctx); const t0 = performance.now();
    let alive = true;
    const io = new IntersectionObserver(es => es.forEach(e => alive = e.isIntersecting));
    io.observe(cv);
    function frame(now) { if (alive) draw((now - t0) / 1000); requestAnimationFrame(frame); }
    requestAnimationFrame(frame);
  }
  function init() { document.querySelectorAll("canvas[data-anim]").forEach(run); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
