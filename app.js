/* Build It — static reader. Vanilla JS, no build step.
   Hero menu -> reader (sticky TOC + one calm step) -> deterministic check-my-code.
   Ambient starfield ties the chrome to what you're building. */

(function () {
  const SOT = window.BUILDIT_SOT;
  const app = document.getElementById("app");
  const topRight = document.getElementById("topRight");
  const progressFill = document.getElementById("progressFill");
  const KEY = "buildit:" + SOT.project;

  const load = () => { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch { return {}; } };
  const save = (s) => localStorage.setItem(KEY, JSON.stringify(s));
  let state = Object.assign({ view: "menu", chapter: 1, step: 0, unlocked: 1, doneChapters: [] }, load());

  const playable = (ch) => Array.isArray(ch.steps) && ch.steps.length > 0;
  const byId = (id) => SOT.chapters.find((c) => c.id === id);
  const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const totalCh = SOT.chapters.length;

  function setProgress() {
    progressFill.style.width = (state.doneChapters.length / totalCh) * 100 + "%";
  }

  function render() {
    save(state); setProgress();
    if (state.view === "menu") { topRight.innerHTML = "Learn by building"; return renderMenu(); }
    topRight.innerHTML = `<b>${esc(SOT.title)}</b> · Easy`;
    renderReader();
  }

  function renderMenu() {
    const ready = SOT.chapters.filter(playable).length;
    app.innerHTML = `
      <section class="hero">
        <div class="eyebrow">MoreSalamander StudioLabs Productions</div>
        <h1>Build something<br/>you'd show a friend.</h1>
        <p>Real projects, one calm page at a time. You always know exactly what to type, what you'll see, and what to do if it's not right.</p>
      </section>
      <div class="projects">
        <div class="card" id="proj">
          <span class="badge">✦ Easy · Python</span>
          <h2>${esc(SOT.title)}</h2>
          <p class="desc">${esc(SOT.pitch)}</p>
          <div class="meta"><span>${totalCh} chapters</span><span>·</span><span>${ready} ready</span><span class="go">Start building →</span></div>
        </div>
      </div>`;
    document.getElementById("proj").onclick = () => { state.view = "reader"; render(); };
  }

  function renderReader() {
    const ch = byId(state.chapter);

    const toc = SOT.chapters.map((c) => {
      const done = state.doneChapters.includes(c.id);
      const cur = c.id === state.chapter;
      const locked = c.id > state.unlocked;
      const cls = ["", locked ? "locked" : "is-unlocked", cur ? "current" : "", done ? "done" : ""].join(" ");
      const ic = done ? "✓" : locked ? "🔒" : c.id;
      return `<li class="${cls}" data-ch="${c.id}"><span class="ic">${ic}</span><span>${esc(c.title)}</span></li>`;
    }).join("");

    const sidebar = `
      <aside class="sidebar">
        <div class="proj-title">${esc(SOT.title)}</div>
        <div class="proj-sub">Easy · Python · ${totalCh} chapters</div>
        <ul class="toc">${toc}</ul>
      </aside>`;

    let main;
    if (!playable(ch)) {
      main = `<div>
        <div class="crumbs"><a id="home">← All projects</a></div>
        <div class="coming"><h3>Coming soon</h3><p>“${esc(ch.title)}” isn't in this preview yet.</p></div>
      </div>`;
    } else {
      const total = ch.steps.length;
      const idx = Math.min(state.step, total - 1);
      const s = ch.steps[idx];
      const last = idx === total - 1;
      const full = (window.BUILDIT_FULLS && BUILDIT_FULLS[ch.id - 1] && BUILDIT_FULLS[ch.id - 1][idx]) || s.full;
      main = `<div>
        <div class="crumbs"><a id="home">← All projects</a></div>
        <div class="chapter-head">
          <div class="ch-num">Chapter ${ch.id}</div>
          <h2>${esc(ch.title)}</h2>
          <p class="build">You'll build ${esc(ch.build)}</p>
        </div>
        <div class="step-meter"><span>Step ${idx + 1} of ${total}</span><span class="bar"><i style="width:${((idx + 1) / total) * 100}%"></i></span></div>

        <article class="step">
          <span class="kicker">Step ${idx + 1}</span>
          <h3>${esc(s.title)}</h3>

          <div class="label">What you're adding</div>
          <p class="adding">${esc(s.adding)}</p>

          <div class="label">The code</div>
          <div class="codewrap">
            <div class="chrome"><span class="d"></span><span class="d"></span><span class="d"></span><span class="fname">main.py</span></div>
            <pre class="language-python"><code class="language-python">${esc(s.code)}</code></pre>
          </div>
          ${full ? `<details class="fullcode"><summary>📄 Your whole file so far</summary><div class="codewrap"><div class="chrome"><span class="d"></span><span class="d"></span><span class="d"></span><span class="fname">main.py</span></div><pre class="language-python"><code class="language-python">${esc(full)}</code></pre></div></details>` : ""}

          <div class="label">What it does</div>
          <p>${esc(s.does)}</p>

          <div class="label">Why it matters</div>
          <p>${esc(s.why)}</p>

          <div class="label">Run it — what you'll see</div>
          <div class="callout see"><span class="ci">👁</span><span>${esc(s.see)}</span></div>

          <div class="label">Checkpoint</div>
          <div class="callout check"><span class="ci">✅</span><span>${esc(s.checkpoint)}</span></div>

          ${(s.recovery && s.recovery.length) ? `<details class="recovery"><summary>It's not right?</summary><ul>${s.recovery.map((r) => `<li>${esc(r)}</li>`).join("")}</ul></details>` : ""}
        </article>

        ${helperHTML()}

        <div class="nav">
          <button class="btn" id="prev" ${idx === 0 ? "disabled" : ""}>← Previous</button>
          <button class="btn primary" id="next">${last ? "Finish chapter ✓" : "Next step →"}</button>
        </div>
        ${last ? `<div class="beat"><h3>🎆 ${esc(ch.beat)}</h3><p>You can stop here — it runs.</p></div>` : ""}
      </div>`;
    }

    app.innerHTML = `<div class="reader">${sidebar}${main}</div>`;

    if (window.Prism) Prism.highlightAllUnder(app);
    wireTOC();
    const home = document.getElementById("home"); if (home) home.onclick = () => { state.view = "menu"; render(); };
    if (playable(ch)) wireStep(ch);
  }

  function wireStep(ch) {
    const total = ch.steps.length;
    const idx = Math.min(state.step, total - 1);
    const s = ch.steps[idx];
    const last = idx === total - 1;
    document.getElementById("prev").onclick = () => { if (idx > 0) { state.step = idx - 1; render(); } };
    document.getElementById("next").onclick = () => {
      if (!last) { state.step = idx + 1; render(); return; }
      if (!state.doneChapters.includes(ch.id)) state.doneChapters.push(ch.id);
      const nx = byId(ch.id + 1);
      if (nx) { state.unlocked = Math.max(state.unlocked, ch.id + 1); state.chapter = ch.id + 1; state.step = 0; }
      render();
    };
    wireHelper(s, ch);
  }

  function helperHTML() {
    return `<details class="helper">
      <summary>🛟 Helper — want a check, or stuck?</summary>
      <div class="body">
        <p class="hint">Paste your code (or the red error you got), then choose:</p>
        <textarea id="paste" placeholder="Paste your main.py — or an error message…"></textarea>
        <div class="hbtns">
          <button class="btn" id="check">Check my code</button>
          <button class="btn primary" id="help">Something's not right</button>
        </div>
        <div class="result" id="result"></div>
        <p class="note">Your code is checked instantly in your browser. When the live helper is on, it adds a plain-language hand.</p>
      </div>
    </details>`;
  }

  function wireHelper(s, ch) {
    const checkBtn = document.getElementById("check");
    const helpBtn = document.getElementById("help");
    const result = document.getElementById("result");
    if (!checkBtn) return;

    const norm = (t) => t.replace(/\s+/g, " ").trim();
    const br = (t) => esc(t).replace(/\n/g, "<br>");
    const ctx = { chapter: `${ch.id} — ${ch.title}`, stepTitle: s.title, code: s.code, see: s.see, recovery: s.recovery || [] };
    const set = (cls, html) => { result.className = "result " + cls; result.innerHTML = html; };

    function deterministic(pasted) {
      const lines = s.code.split("\n").map(norm).filter(Boolean);
      const hay = norm(pasted);
      const missing = lines.filter((ln) => !hay.includes(ln));
      return { ok: missing.length === 0, missing };
    }

    async function ask(payload) {
      const r = await fetch("/api/chat", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(payload) });
      if (!r.ok) throw new Error("http " + r.status);
      const d = await r.json();
      if (!d.text) throw new Error(d.error || "no text");
      return d.text;
    }

    checkBtn.onclick = async () => {
      const pasted = document.getElementById("paste").value || "";
      if (!pasted.trim()) { set("no", "Paste your code first and I'll check it."); return; }
      const f = deterministic(pasted);
      const verdict = f.ok
        ? "✓ This step's code is in there."
        : "I don't see this step's line yet — it should include:<br><code>" + esc(f.missing[0]) + "</code>";
      set(f.ok ? "ok" : "no", verdict + `<div class="voice" id="voice"><span class="spin"></span> checking with the helper…</div>`);
      const findings = f.ok ? "All of this step's lines are present." : ("Missing line(s): " + f.missing.join(" | "));
      try {
        const text = await ask({ mode: "check", ctx, pasted, findings });
        const v = document.getElementById("voice"); if (v) v.innerHTML = br(text);
      } catch {
        const v = document.getElementById("voice"); if (v) v.remove();
      }
    };

    helpBtn.onclick = async () => {
      const pasted = document.getElementById("paste").value || "";
      set("", `<span class="spin"></span> looking at it…`);
      try {
        const text = await ask({ mode: "help", ctx, pasted });
        set("ok", br(text));
      } catch {
        const fixes = (s.recovery && s.recovery.length)
          ? "<ul>" + s.recovery.map((r) => "<li>" + esc(r) + "</li>").join("") + "</ul>"
          : "Re-check this step's code against the snippet above.";
        set("no", "<b>The live helper is offline</b> — but here are the usual fixes for this step:" + fixes);
      }
    };
  }

  function wireTOC() {
    document.querySelectorAll(".toc li").forEach((el) => {
      const id = +el.dataset.ch;
      if (id > state.unlocked) return;
      el.onclick = () => { state.chapter = id; state.step = 0; render(); };
    });
  }

  /* ---------- ambient starfield ---------- */
  (function sky() {
    const c = document.getElementById("sky");
    const ctx = c.getContext("2d");
    let w, h, stars, bursts = [];
    function resize() {
      w = c.width = innerWidth; h = c.height = innerHeight;
      stars = Array.from({ length: 150 }, () => ({
        x: Math.random() * w, y: Math.random() * h,
        r: Math.random() * 1.3 + 0.3,
        a: Math.random() * 0.5 + 0.15,
        ph: Math.random() * 6.28, sp: Math.random() * 0.02 + 0.005
      }));
    }
    function spawnBurst() {
      const bx = w * (0.15 + Math.random() * 0.7), by = h * (0.1 + Math.random() * 0.3);
      const hue = Math.random() < 0.5 ? "245,189,84" : "142,123,255";
      const n = 26, parts = [];
      for (let i = 0; i < n; i++) {
        const ang = (i / n) * 6.28, sp = Math.random() * 1.6 + 0.6;
        parts.push({ x: bx, y: by, vx: Math.cos(ang) * sp, vy: Math.sin(ang) * sp });
      }
      bursts.push({ parts, life: 1, hue });
    }
    let t = 0;
    function frame() {
      ctx.clearRect(0, 0, w, h);
      t += 1;
      for (const s of stars) {
        s.ph += s.sp;
        const a = s.a * (0.6 + 0.4 * Math.sin(s.ph));
        ctx.globalAlpha = a; ctx.fillStyle = "#cdd2ff";
        ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, 6.28); ctx.fill();
      }
      for (const b of bursts) {
        b.life -= 0.012;
        for (const p of b.parts) { p.x += p.vx; p.y += p.vy; p.vy += 0.01; }
        ctx.globalAlpha = Math.max(0, b.life) * 0.5;
        ctx.fillStyle = "rgba(" + b.hue + ",1)";
        for (const p of b.parts) { ctx.beginPath(); ctx.arc(p.x, p.y, 1.4, 0, 6.28); ctx.fill(); }
      }
      bursts = bursts.filter((b) => b.life > 0);
      if (t % 360 === 0 && Math.random() < 0.8) spawnBurst();
      ctx.globalAlpha = 1;
      requestAnimationFrame(frame);
    }
    addEventListener("resize", resize);
    resize(); setTimeout(spawnBurst, 1200); frame();
  })();

  render();
})();
