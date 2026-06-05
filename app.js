/* ===================================================================
   Human Diseases Master — app.js
   Vanilla SPA. Hash router, lazy JSON loading, five learning modes +
   randomised mock exam engine. No frameworks, no backend.
   =================================================================== */

'use strict';

/* ---------- Theme registry (mirrors CLAUDE.md; counts let the landing
   and theme pages show progress without fetching every file) -------- */
const THEMES = [
  { id: 1, title: 'Clinical Examination & History Taking',      difficulty: 'easy',    lectures: 1,  clusters: 3  },
  { id: 2, title: 'Principles of Infection & Infection Control', difficulty: 'medium',  lectures: 11, clusters: 7  },
  { id: 3, title: 'Immunological Disease',                       difficulty: 'hard',    lectures: 5,  clusters: 5  },
  { id: 4, title: 'Pain & Anxiety Control',                      difficulty: 'medium',  lectures: 5,  clusters: 5  },
  { id: 5, title: 'Cardiovascular Diseases',                     difficulty: 'hardest', lectures: 12, clusters: 10 },
  { id: 6, title: 'Haematological Disorders',                    difficulty: 'hard',    lectures: 4,  clusters: 4  },
  { id: 7, title: 'Diabetes & Endocrinology',                   difficulty: 'easy',    lectures: 4,  clusters: 4  },
  { id: 8, title: 'Respiratory Medicine',                        difficulty: 'easy',    lectures: 5,  clusters: 5  },
];
const themeMeta = (id) => THEMES.find(t => t.id === Number(id));

const MODES = [
  { key: 'ground', title: 'Ground It', tag: 'Understand',      desc: 'Read it in plain prose, then explain it back in your own words.' },
  { key: 'recall', title: 'Recall It', tag: 'Retrieve',        desc: 'Flashcard-style active recall. The single most effective technique.' },
  { key: 'apply',  title: 'Apply It',  tag: 'Clinical SBAs',   desc: 'Case-based single-best-answer questions with full explanations.' },
  { key: 'write',  title: 'Write It',  tag: 'Structured',      desc: 'Practice SSA answers, then self-mark against the scheme.' },
];

/* ---------- Data loading (cached in memory) ---------- */
const cache = {};
async function loadTheme(id) {
  if (cache[id]) return cache[id];
  const res = await fetch(`data/theme-${id}.json`);
  if (!res.ok) throw new Error(`Failed to load theme ${id} (${res.status})`);
  cache[id] = await res.json();
  return cache[id];
}

/* ---------- Helpers ---------- */
const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

function esc(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function shuffle(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

const letter = (i) => String.fromCharCode(65 + i);

/** Prose with \n\n paragraph breaks → escaped <p> blocks. */
function prose(text) {
  return String(text).split(/\n\s*\n/).map(p =>
    `<p>${esc(p.trim()).replace(/\n/g, '<br>')}</p>`).join('');
}

/** "anticoagulant-drugs" → "Anticoagulant drugs" */
function prettyTag(tag) {
  const s = String(tag).replace(/-/g, ' ');
  return s.charAt(0).toUpperCase() + s.slice(1);
}

/* localStorage — wrapped so a disabled store never crashes the app */
const store = {
  get(k, fallback = null) {
    try { const v = localStorage.getItem(k); return v === null ? fallback : v; }
    catch { return fallback; }
  },
  set(k, v) { try { localStorage.setItem(k, v); } catch {} },
  getJSON(k, fallback) { try { return JSON.parse(localStorage.getItem(k)) ?? fallback; } catch { return fallback; } },
  setJSON(k, v) { this.set(k, JSON.stringify(v)); },
};

const groundKey = (themeId, k) => `hd_ground_t${themeId}-c${k}`;
const groundTextKey = (clusterId) => `hd_groundtext_${clusterId}`;
const writeKey = (id) => `hd_write_${id}`;

function groundProgress(theme) {
  let done = 0;
  for (let k = 1; k <= theme.clusters; k++) {
    if (store.get(groundKey(theme.id, k)) === 'complete') done++;
  }
  return { done, total: theme.clusters };
}

async function copyToClipboard(text) {
  try { await navigator.clipboard.writeText(text); return true; }
  catch {
    try {
      const ta = document.createElement('textarea');
      ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      const ok = document.execCommand('copy'); ta.remove(); return ok;
    } catch { return false; }
  }
}

function flashButton(btn, msg, ms = 1600) {
  const orig = btn.textContent;
  btn.textContent = msg; btn.disabled = true;
  setTimeout(() => { btn.textContent = orig; btn.disabled = false; }, ms);
}

/* Shared fragments */
function loadingHTML(label = 'Loading content…') {
  return `<div class="view"><div class="loading"><div class="spinner"></div><p>${esc(label)}</p></div></div>`;
}
function errorHTML() {
  return `<div class="view"><div class="error-state card">
    <h2>Content couldn't be loaded</h2>
    <p>Check your connection and refresh the page.</p>
    <a class="btn" href="#/">Back to home</a></div></div>`;
}
function badge(difficulty) {
  return `<span class="badge badge-${difficulty}">${esc(difficulty)}</span>`;
}
function breadcrumb(parts) {
  return `<nav class="breadcrumb" aria-label="Breadcrumb">${
    parts.map((p, i) => p.href
      ? `<a href="${p.href}">${esc(p.label)}</a>${i < parts.length - 1 ? '<span>›</span>' : ''}`
      : `<span>${esc(p.label)}</span>`).join('')
  }</nav>`;
}

/* SVG icons */
const ICON = {
  home:   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/></svg>',
  master: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M12 12l8-4.5M12 12v9M12 12 4 7.5"/></svg>',
  chart:  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19V5"/><path d="M4 19h16"/><path d="m7 14 3-3 3 2 4-5"/></svg>',
  book:   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h11a2 2 0 0 1 2 2v14H7a2 2 0 0 1-2-2z"/><path d="M18 6h1v14"/></svg>',
  ground: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16M4 5v14M4 19h16"/><path d="M8 9h8M8 13h6"/></svg>',
  recall: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 4v4h4"/></svg>',
  apply:  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l2 2 4-4"/><rect x="3" y="4" width="18" height="16" rx="2"/></svg>',
  write:  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>',
  modeIcon(key) { return this[key] || this.book; },
};

/* ===================================================================
   Router
   =================================================================== */
const routes = [
  { pattern: /^\/?$/,                    handler: renderLanding },
  { pattern: /^\/theme\/(\d+)$/,         handler: renderTheme },
  { pattern: /^\/theme\/(\d+)\/ground$/, handler: renderGround },
  { pattern: /^\/theme\/(\d+)\/recall$/, handler: renderRecall },
  { pattern: /^\/theme\/(\d+)\/apply$/,  handler: renderApply },
  { pattern: /^\/theme\/(\d+)\/write$/,  handler: renderWrite },
  { pattern: /^\/master$/,               handler: renderMasterConfig },
  { pattern: /^\/master\/exam$/,         handler: renderMasterExam },
  { pattern: /^\/master\/results$/,      handler: renderMasterResults },
  { pattern: /^\/progress$/,             handler: renderProgress },
  { pattern: /^\/citations$/,            handler: renderCitations },
];

function currentPath() {
  return window.location.hash.replace(/^#/, '') || '/';
}

/** Clear anything (timers) left running by the previous view. */
function teardown() {
  if (mockState && mockState.timerId) {
    clearInterval(mockState.timerId);
    mockState.timerId = null;
  }
}

function router() {
  teardown();
  closeSidebar();
  const path = currentPath();
  const app = $('#app');

  for (const route of routes) {
    const match = path.match(route.pattern);
    if (match) {
      window.scrollTo(0, 0);
      route.handler(app, ...match.slice(1));
      updateActiveNav(path);
      return;
    }
  }
  renderLanding(app);
  updateActiveNav('/');
}

/* ---------- Sidebar nav ---------- */
function buildNav() {
  $('#sidebar-nav').innerHTML = `
    <a href="#/" class="nav-link" data-path="/">${ICON.home}<span>Home</span></a>
    <a href="#/master" class="nav-link" data-path="/master">${ICON.master}<span>Master It — Mock</span></a>
    <a href="#/progress" class="nav-link" data-path="/progress">${ICON.chart}<span>Score History</span></a>
    <a href="#/citations" class="nav-link" data-path="/citations">${ICON.book}<span>Sources &amp; Citations</span></a>
    <p class="sidebar-section-label">Themes</p>
    ${THEMES.map(t => `
      <a href="#/theme/${t.id}" class="nav-link" data-path="/theme/${t.id}">
        <span class="nav-num">${t.id}</span><span>${esc(t.title)}</span>
      </a>`).join('')}`;
}
function updateActiveNav(path) {
  $$('.nav-link').forEach(a => {
    const p = a.getAttribute('data-path');
    const active = p === '/' ? path === '/' : path.startsWith(p);
    a.classList.toggle('active', active);
  });
}

/* ---------- Mobile sidebar ---------- */
function openSidebar()  { $('#sidebar').classList.add('open'); $('#backdrop').classList.add('show'); $('#hamburger').setAttribute('aria-expanded','true'); }
function closeSidebar() { $('#sidebar').classList.remove('open'); $('#backdrop').classList.remove('show'); $('#hamburger').setAttribute('aria-expanded','false'); }
function toggleSidebar(){ $('#sidebar').classList.contains('open') ? closeSidebar() : openSidebar(); }

/* ===================================================================
   STEP 2 — Landing
   =================================================================== */
function renderLanding(app) {
  const cards = THEMES.map(t => {
    const gp = groundProgress(t);
    const pct = gp.total ? Math.round((gp.done / gp.total) * 100) : 0;
    const caption = gp.done === 0 ? 'Not started yet'
      : gp.done === gp.total ? 'All topics grounded ✓'
      : `${gp.done}/${gp.total} topics grounded`;
    return `
      <a class="theme-card" href="#/theme/${t.id}">
        <div class="theme-card-top">
          <span class="theme-num">Theme ${t.id}</span>
          ${badge(t.difficulty)}
        </div>
        <h3 class="theme-card-title">${esc(t.title)}</h3>
        <p class="theme-card-meta">${t.lectures} lecture${t.lectures > 1 ? 's' : ''} · ${t.clusters} topics</p>
        <div class="theme-card-progress">
          <div class="progress" role="progressbar" aria-valuenow="${pct}" aria-valuemin="0" aria-valuemax="100" aria-label="Ground It progress">
            <div class="progress-fill" style="width:${pct}%"></div>
          </div>
          <span class="theme-card-caption">${caption}</span>
        </div>
      </a>`;
  }).join('');

  const howto = MODES.concat([{ key: 'master', title: 'Master It', tag: 'Mock exam', desc: 'A randomised, interleaved mock from every theme, timed or untimed.' }])
    .map(m => `
      <div class="howto-item">
        <span class="howto-icon">${ICON.modeIcon(m.key)}</span>
        <div><strong>${esc(m.title)}</strong> — <span>${esc(m.desc)}</span></div>
      </div>`).join('');

  app.innerHTML = `
    <div class="view">
      <div class="page-head landing-head">
        <p class="eyebrow">Newcastle BDS Year 3</p>
        <h1>Human Diseases Master</h1>
        <p class="lede">Your complete Human Diseases revision toolkit — eight themes, five evidence-based learning modes, and a full randomised mock exam engine.</p>
      </div>

      <details class="howto" open>
        <summary>How to use Human Diseases Master — five modes, any order</summary>
        <div class="howto-grid">${howto}</div>
        <p class="howto-foot">Use the modes in any order. Ground It builds understanding; Recall, Apply and Write test it; Master It rehearses the real exam.</p>
      </details>

      <h2 class="section-title">Choose a theme</h2>
      <div class="theme-grid">${cards}</div>

      <div class="footer-links">
        <a href="#/master">Master It — Full Mock</a>
        <a href="#/progress">Score History</a>
        <a href="#/citations">Sources &amp; Citations</a>
      </div>
    </div>`;
}

/* ===================================================================
   STEP 3 — Theme page
   =================================================================== */
async function renderTheme(app, id) {
  const meta = themeMeta(id);
  if (!meta) { app.innerHTML = errorHTML(); return; }
  app.innerHTML = loadingHTML();
  let data;
  try { data = await loadTheme(id); }
  catch { app.innerHTML = errorHTML(); return; }

  const counts = {
    ground: data.groundIt.length,
    recall: data.recallIt.length,
    apply:  data.applyIt.length,
    write:  data.writeIt.length,
  };
  const countLabel = {
    ground: `${counts.ground} topics`,
    recall: `${counts.recall} cards`,
    apply:  `${counts.apply} questions`,
    write:  `${counts.write} prompts`,
  };
  const gp = groundProgress(meta);
  const writeDone = data.writeIt.filter(w => store.get(writeKey(w.id)) === 'attempted').length;
  const progressNote = {
    ground: gp.done ? `${gp.done}/${gp.total} done` : '',
    write:  writeDone ? `${writeDone}/${counts.write} attempted` : '',
  };

  const modeCards = MODES.map(m => `
    <a class="mode-card" href="#/theme/${id}/${m.key}">
      <span class="mode-icon">${ICON.modeIcon(m.key)}</span>
      <div class="mode-card-body">
        <div class="mode-card-head">
          <h3>${esc(m.title)}</h3>
          <span class="mode-pill">${esc(m.tag)}</span>
        </div>
        <p>${esc(m.desc)}</p>
        <div class="mode-card-foot">
          <span>${countLabel[m.key]}</span>
          ${progressNote[m.key] ? `<span class="mode-progress">${progressNote[m.key]}</span>` : ''}
        </div>
      </div>
    </a>`).join('');

  const outcomes = (data.theme.learningOutcomes || [])
    .map(o => `<span class="outcome-tag">${esc(o)}</span>`).join('');

  app.innerHTML = `
    <div class="view">
      ${breadcrumb([{ label: 'Home', href: '#/' }, { label: `Theme ${id}` }])}
      <div class="page-head">
        <div class="theme-head-row">
          <p class="eyebrow">Theme ${id}</p>
          ${badge(meta.difficulty)}
        </div>
        <h1>${esc(data.theme.title)}</h1>
        <p class="theme-head-meta">${meta.lectures} lecture${meta.lectures > 1 ? 's' : ''}${outcomes ? ' · Learning outcomes:' : ''} ${outcomes}</p>
      </div>

      <div class="mode-grid">${modeCards}</div>

      <div class="theme-master-cta card">
        <div>
          <h3>Ready to test everything together?</h3>
          <p>Master It interleaves questions from this and every other theme into a randomised mock exam.</p>
        </div>
        <a class="btn" href="#/master">Go to Master It</a>
      </div>
    </div>`;
}

/* ===================================================================
   STEP 4 — Ground It
   =================================================================== */
let groundState = null;

async function renderGround(app, id) {
  const meta = themeMeta(id);
  app.innerHTML = loadingHTML();
  let data;
  try { data = await loadTheme(id); }
  catch { app.innerHTML = errorHTML(); return; }
  groundState = { id, clusters: data.groundIt, index: 0, title: data.theme.title };
  drawGround(app);
}

function drawGround(app) {
  const { id, clusters, index, title } = groundState;
  const c = clusters[index];
  const k = index + 1;
  const complete = store.get(groundKey(id, k)) === 'complete';
  const savedText = store.get(groundTextKey(c.clusterId), '');

  const chips = clusters.map((cl, i) => {
    const done = store.get(groundKey(id, i + 1)) === 'complete';
    return `<button class="cluster-chip ${i === index ? 'current' : ''} ${done ? 'done' : ''}"
      data-idx="${i}" aria-current="${i === index}">
      ${done ? '<span class="tick">✓</span>' : `<span class="chip-num">${i + 1}</span>`}
      <span class="chip-label">${esc(cl.clusterTitle)}</span>
    </button>`;
  }).join('');

  const doneCount = clusters.filter((_, i) => store.get(groundKey(id, i + 1)) === 'complete').length;

  app.innerHTML = `
    <div class="view">
      ${breadcrumb([{ label: 'Home', href: '#/' }, { label: `Theme ${id}`, href: `#/theme/${id}` }, { label: 'Ground It' }])}
      <div class="page-head">
        <p class="eyebrow">Ground It · ${esc(title)}</p>
        <h1>Build the understanding first</h1>
        <p class="lede">Read each topic as plain prose, then explain it back in your own words. ${doneCount}/${clusters.length} topics complete.</p>
      </div>

      <div class="cluster-chips">${chips}</div>

      <article class="card ground-reader">
        <div class="ground-reader-head">
          <h2>${esc(c.clusterTitle)} ${complete ? '<span class="done-flag">✓ Complete</span>' : ''}</h2>
          <span class="reader-count">Topic ${k} of ${clusters.length}</span>
        </div>
        <div class="prose">${prose(c.content)}</div>

        <div class="self-explain">
          <label for="se-box"><strong>Write it in your own words</strong> — this is just for you, not marked.</label>
          <p class="self-explain-prompt">${esc(c.selfExplainPrompt)}</p>
          <textarea id="se-box" rows="4" placeholder="Type your explanation…">${esc(savedText)}</textarea>
        </div>

        <div class="reader-nav">
          <button class="btn btn-secondary" id="g-prev" ${index === 0 ? 'disabled' : ''}>← Previous</button>
          <button class="btn" id="g-continue">${index < clusters.length - 1 ? 'Mark complete & continue →' : 'Mark complete ✓'}</button>
        </div>
      </article>
    </div>`;

  // Persist self-explanation as the student types
  $('#se-box').addEventListener('input', (e) => store.set(groundTextKey(c.clusterId), e.target.value));

  $$('.cluster-chip').forEach(btn => btn.addEventListener('click', () => {
    groundState.index = Number(btn.dataset.idx);
    drawGround(app);
  }));

  $('#g-prev').addEventListener('click', () => {
    if (groundState.index > 0) { groundState.index--; drawGround(app); }
  });

  $('#g-continue').addEventListener('click', () => {
    store.set(groundKey(id, k), 'complete');
    if (groundState.index < clusters.length - 1) groundState.index++;
    drawGround(app);
  });
}

/* ===================================================================
   STEP 5 — Recall It
   =================================================================== */
let recallState = null;

async function renderRecall(app, id) {
  app.innerHTML = loadingHTML();
  let data;
  try { data = await loadTheme(id); }
  catch { app.innerHTML = errorHTML(); return; }
  startRecall(app, id, data);
}

function startRecall(app, id, data) {
  recallState = {
    id, title: data.theme.title,
    cards: shuffle(data.recallIt),
    index: 0, revealed: false, got: 0, missed: [],
  };
  drawRecall(app, data);
}

function drawRecall(app, data) {
  const s = recallState;
  if (s.index >= s.cards.length) return drawRecallEnd(app, data);

  const card = s.cards[s.index];
  const n = s.cards.length;
  const pct = Math.round((s.index / n) * 100);

  app.innerHTML = `
    <div class="view">
      ${breadcrumb([{ label: 'Home', href: '#/' }, { label: `Theme ${s.id}`, href: `#/theme/${s.id}` }, { label: 'Recall It' }])}
      <div class="page-head">
        <p class="eyebrow">Recall It · ${esc(s.title)}</p>
        <h1>Active recall</h1>
      </div>

      <div class="quiz-status">
        <span>Card ${s.index + 1} of ${n}</span>
        <span class="quiz-score">Got ${s.got} · Missed ${s.missed.length}</span>
      </div>
      <div class="progress" role="progressbar" aria-valuenow="${pct}" aria-valuemin="0" aria-valuemax="100" aria-label="Recall progress">
        <div class="progress-fill" style="width:${pct}%"></div>
      </div>

      <article class="card recall-card">
        <p class="recall-q-label">Question</p>
        <p class="recall-question">${esc(card.question)}</p>

        <div id="recall-answer" class="recall-answer" hidden>
          <p class="recall-a-label">Answer</p>
          <p>${esc(card.answer)}</p>
        </div>

        <div class="recall-actions">
          <button class="btn" id="reveal-btn">Reveal answer</button>
          <div id="judge" class="judge" hidden>
            <button class="btn btn-judge got" id="got-btn">✓ Got it</button>
            <button class="btn btn-judge miss" id="miss-btn">✗ Didn't get it</button>
          </div>
        </div>
      </article>
    </div>`;

  $('#reveal-btn').addEventListener('click', () => {
    $('#recall-answer').hidden = false;
    $('#reveal-btn').hidden = true;
    $('#judge').hidden = false;
  });
  const advance = (gotIt) => {
    if (gotIt) s.got++; else s.missed.push(card.question);
    s.index++;
    drawRecall(app, data);
  };
  $('#got-btn').addEventListener('click', () => advance(true));
  $('#miss-btn').addEventListener('click', () => advance(false));
}

function drawRecallEnd(app, data) {
  const s = recallState;
  const n = s.cards.length;
  const pct = Math.round((s.got / n) * 100);
  const missedList = s.missed.length
    ? `<ul class="missed-list">${s.missed.map(q => `<li>${esc(q)}</li>`).join('')}</ul>`
    : `<p class="all-clear">Nothing missed — every card recalled. 🎯</p>`;

  app.innerHTML = `
    <div class="view">
      ${breadcrumb([{ label: 'Home', href: '#/' }, { label: `Theme ${s.id}`, href: `#/theme/${s.id}` }, { label: 'Recall It' }])}
      <div class="page-head"><h1>Recall complete</h1></div>

      <div class="result-hero card">
        <div class="result-score">${s.got}<span>/${n}</span></div>
        <p>${pct}% recalled</p>
      </div>

      <div class="card">
        <div class="missed-head">
          <h3>Missed items${s.missed.length ? ` (${s.missed.length})` : ''}</h3>
          ${s.missed.length ? '<button class="btn btn-secondary" id="copy-missed">Copy missed items</button>' : ''}
        </div>
        ${missedList}
      </div>

      <div class="btn-row" style="margin-top:1.25rem">
        <button class="btn" id="recall-restart">Restart (reshuffled)</button>
        <a class="btn btn-secondary" href="#/theme/${s.id}">Back to theme</a>
      </div>
    </div>`;

  if (s.missed.length) {
    $('#copy-missed').addEventListener('click', async (e) => {
      const text = `Human Diseases Master — Recall misses (${s.title})\n` + s.missed.map(q => `- ${q}`).join('\n');
      flashButton(e.target, (await copyToClipboard(text)) ? 'Copied ✓' : 'Copy failed');
    });
  }
  $('#recall-restart').addEventListener('click', () => startRecall(app, s.id, data));
}

/* ===================================================================
   STEP 6 — Apply It
   =================================================================== */
let applyState = null;

async function renderApply(app, id) {
  app.innerHTML = loadingHTML();
  let data;
  try { data = await loadTheme(id); }
  catch { app.innerHTML = errorHTML(); return; }
  startApply(app, id, data);
}

function startApply(app, id, data) {
  applyState = { id, title: data.theme.title, qs: shuffle(data.applyIt), index: 0, score: 0, answered: false };
  drawApply(app, data);
}

function drawApply(app, data) {
  const s = applyState;
  if (s.index >= s.qs.length) return drawApplyEnd(app, data);
  const q = s.qs[s.index];
  const n = s.qs.length;
  const pct = Math.round((s.index / n) * 100);

  const opts = q.options.map((o, i) => `
    <button class="option" data-letter="${letter(i)}">
      <span class="option-key">${letter(i)}</span>
      <span class="option-text">${esc(o.replace(/^[A-E]\.\s*/, ''))}</span>
    </button>`).join('');

  app.innerHTML = `
    <div class="view">
      ${breadcrumb([{ label: 'Home', href: '#/' }, { label: `Theme ${s.id}`, href: `#/theme/${s.id}` }, { label: 'Apply It' }])}
      <div class="page-head">
        <p class="eyebrow">Apply It · ${esc(s.title)}</p>
        <h1>Clinical SBAs</h1>
      </div>

      <div class="quiz-status">
        <span>Question ${s.index + 1} of ${n}</span>
        <span class="quiz-score">Score ${s.score}/${s.index}</span>
      </div>
      <div class="progress" role="progressbar" aria-valuenow="${pct}" aria-valuemin="0" aria-valuemax="100" aria-label="Apply progress">
        <div class="progress-fill" style="width:${pct}%"></div>
      </div>

      <article class="card sba">
        <p class="sba-scenario">${esc(q.scenario)}</p>
        <div class="options" id="apply-opts">${opts}</div>
        <div id="apply-explain" class="explain" hidden>
          <p class="explain-verdict" id="apply-verdict"></p>
          <p>${esc(q.explanation)}</p>
          <button class="btn" id="apply-next">${s.index < n - 1 ? 'Next question →' : 'See results →'}</button>
        </div>
      </article>
    </div>`;

  $$('#apply-opts .option').forEach(btn => btn.addEventListener('click', () => {
    if (s.answered) return;
    s.answered = true;
    const chosen = btn.dataset.letter;
    const correct = q.correctAnswer;
    $$('#apply-opts .option').forEach(b => {
      b.disabled = true;
      if (b.dataset.letter === correct) b.classList.add('correct');
      else if (b.dataset.letter === chosen) b.classList.add('wrong');
    });
    const right = chosen === correct;
    if (right) s.score++;
    const v = $('#apply-verdict');
    v.textContent = right ? '✓ Correct' : `✗ Incorrect — correct answer is ${correct}`;
    v.className = `explain-verdict ${right ? 'is-correct' : 'is-wrong'}`;
    $('#apply-explain').hidden = false;
    $('#apply-next').focus();
  }));

  const nextBtn = $('#apply-next');
  if (nextBtn) nextBtn.addEventListener('click', () => {
    s.index++; s.answered = false; drawApply(app, data);
  });
}

function drawApplyEnd(app, data) {
  const s = applyState;
  const n = s.qs.length;
  const pct = Math.round((s.score / n) * 100);
  app.innerHTML = `
    <div class="view">
      ${breadcrumb([{ label: 'Home', href: '#/' }, { label: `Theme ${s.id}`, href: `#/theme/${s.id}` }, { label: 'Apply It' }])}
      <div class="page-head"><h1>Apply It complete</h1></div>
      <div class="result-hero card">
        <div class="result-score">${s.score}<span>/${n}</span></div>
        <p>${pct}% correct</p>
      </div>
      <div class="btn-row" style="margin-top:1.25rem">
        <button class="btn" id="apply-retry">Try again (reshuffled)</button>
        <a class="btn btn-secondary" href="#/theme/${s.id}">Back to theme</a>
      </div>
    </div>`;
  $('#apply-retry').addEventListener('click', () => startApply(app, s.id, data));
}

/* ===================================================================
   STEP 7 — Write It
   =================================================================== */
let writeState = null;

async function renderWrite(app, id) {
  app.innerHTML = loadingHTML();
  let data;
  try { data = await loadTheme(id); }
  catch { app.innerHTML = errorHTML(); return; }
  writeState = { id, title: data.theme.title, prompts: data.writeIt, view: 'list', current: null };
  drawWrite(app);
}

function drawWrite(app) {
  const s = writeState;
  if (s.view === 'list') return drawWriteList(app);
  return drawWritePrompt(app);
}

function drawWriteList(app) {
  const s = writeState;
  const items = s.prompts.map((p, i) => {
    const attempted = store.get(writeKey(p.id)) === 'attempted';
    return `
      <button class="write-list-item" data-idx="${i}">
        <span class="write-list-meta">
          <span class="write-list-mark">${attempted ? '<span class="tick">✓</span>' : '<span class="chip-num">' + (i + 1) + '</span>'}</span>
          <span>${esc(p.prompt)}</span>
        </span>
        <span class="write-list-total">${p.totalMarks} marks${attempted ? ' · attempted' : ''}</span>
      </button>`;
  }).join('');

  app.innerHTML = `
    <div class="view">
      ${breadcrumb([{ label: 'Home', href: '#/' }, { label: `Theme ${s.id}`, href: `#/theme/${s.id}` }, { label: 'Write It' }])}
      <div class="page-head">
        <p class="eyebrow">Write It · ${esc(s.title)}</p>
        <h1>Structured answer practice</h1>
        <p class="lede">Write a full structured answer, then reveal the mark scheme and self-mark honestly.</p>
      </div>
      <div class="write-list">${items}</div>
    </div>`;

  $$('.write-list-item').forEach(btn => btn.addEventListener('click', () => {
    s.current = Number(btn.dataset.idx); s.view = 'prompt'; drawWrite(app);
  }));
}

function drawWritePrompt(app) {
  const s = writeState;
  const p = s.prompts[s.current];
  const checks = p.markScheme.map((m, i) => `
    <li class="mark-point">
      <label>
        <input type="checkbox" class="mark-check" data-marks="${m.marks}" aria-checked="false">
        <span class="mark-text">${esc(m.point)}</span>
        <span class="mark-value">${m.marks}</span>
      </label>
    </li>`).join('');

  app.innerHTML = `
    <div class="view">
      ${breadcrumb([{ label: 'Home', href: '#/' }, { label: `Theme ${s.id}`, href: `#/theme/${s.id}` }, { label: 'Write It', href: `#/theme/${s.id}/write` }, { label: `Q${s.current + 1}` }])}
      <div class="page-head">
        <p class="eyebrow">Write It · ${p.totalMarks} marks</p>
        <h1>Question ${s.current + 1}</h1>
      </div>

      <article class="card">
        <p class="write-prompt">${esc(p.prompt)}</p>
        <label class="write-label" for="write-area">Your structured answer</label>
        <textarea id="write-area" class="write-area" rows="10" placeholder="Write your answer here…"></textarea>

        <div id="ms-wrap">
          <button class="btn" id="reveal-ms">Reveal mark scheme</button>
        </div>

        <div id="markscheme" hidden>
          <div class="ms-head">
            <h3>Mark scheme — tick each point you covered</h3>
            <div class="ms-score" id="ms-score" aria-live="polite">0 / ${p.totalMarks}</div>
          </div>
          <ul class="mark-list">${checks}</ul>
          <div class="btn-row">
            <a class="btn btn-secondary" href="#/theme/${s.id}/write" id="back-list">Back to prompts</a>
          </div>
        </div>
      </article>
    </div>`;

  $('#reveal-ms').addEventListener('click', () => {
    $('#ms-wrap').hidden = true;
    $('#markscheme').hidden = false;
    store.set(writeKey(p.id), 'attempted');
  });

  const recalc = () => {
    let sum = 0;
    $$('.mark-check').forEach(c => {
      c.setAttribute('aria-checked', c.checked ? 'true' : 'false');
      c.closest('.mark-point').classList.toggle('ticked', c.checked);
      if (c.checked) sum += Number(c.dataset.marks);
    });
    $('#ms-score').textContent = `${sum} / ${p.totalMarks}`;
  };
  $$('.mark-check').forEach(c => c.addEventListener('change', recalc));

  // back-list handled by hash link; ensure list reflects new "attempted"
  $('#back-list').addEventListener('click', () => { writeState.view = 'list'; });
}

/* ===================================================================
   STEP 8 — Master It (mock exam engine)
   =================================================================== */
let mockState = null;
const MOCK_COUNTS = [20, 35, 50, 70];
const SECONDS_PER_Q = 90;

function renderMasterConfig(app) {
  const themeChecks = THEMES.map(t => `
    <label class="check-row">
      <input type="checkbox" class="mock-theme" value="${t.id}" checked>
      <span class="check-box"></span>
      <span class="check-label"><strong>Theme ${t.id}</strong> — ${esc(t.title)} ${badge(t.difficulty)}</span>
    </label>`).join('');

  const countRadios = MOCK_COUNTS.map(c => `
    <label class="radio-pill">
      <input type="radio" name="qcount" value="${c}" ${c === 70 ? 'checked' : ''}>
      <span>${c}</span>
    </label>`).join('');

  app.innerHTML = `
    <div class="view">
      ${breadcrumb([{ label: 'Home', href: '#/' }, { label: 'Master It' }])}
      <div class="page-head">
        <p class="eyebrow">Master It</p>
        <h1>Build your mock exam</h1>
        <p class="lede">Randomised and interleaved across every theme you select — the closest rehearsal to the real HD paper.</p>
      </div>

      <div class="card config-block">
        <div class="config-head">
          <h3>Themes to include</h3>
          <div class="config-bulk">
            <button class="btn btn-ghost" id="select-all">Select all</button>
            <button class="btn btn-ghost" id="select-none">Clear</button>
          </div>
        </div>
        <div class="check-grid">${themeChecks}</div>
      </div>

      <div class="card config-block">
        <h3>Number of questions</h3>
        <div class="radio-row">${countRadios}</div>
        <p class="config-note" id="pool-note"></p>
      </div>

      <div class="card config-block">
        <h3>Timing</h3>
        <label class="toggle-row">
          <input type="checkbox" id="timed-toggle">
          <span class="toggle-track"><span class="toggle-thumb"></span></span>
          <span>Timed — ${SECONDS_PER_Q} seconds per question (auto-advances)</span>
        </label>
      </div>

      <div class="btn-row config-actions">
        <button class="btn btn-lg" id="start-mock">Start mock exam</button>
      </div>
      <p class="config-error" id="config-error" hidden></p>
    </div>`;

  const selectedThemes = () => $$('.mock-theme:checked').map(c => Number(c.value));

  async function updatePool() {
    const ids = selectedThemes();
    const note = $('#pool-note');
    if (!ids.length) { note.textContent = ''; return; }
    try {
      const datas = await Promise.all(ids.map(loadTheme));
      const pool = datas.reduce((sum, d) => sum + d.mockBank.length, 0);
      note.textContent = `${pool} questions available across ${ids.length} theme${ids.length > 1 ? 's' : ''}.`;
    } catch { note.textContent = ''; }
  }

  $('#select-all').addEventListener('click', () => { $$('.mock-theme').forEach(c => c.checked = true); updatePool(); });
  $('#select-none').addEventListener('click', () => { $$('.mock-theme').forEach(c => c.checked = false); updatePool(); });
  $$('.mock-theme').forEach(c => c.addEventListener('change', updatePool));
  updatePool();

  $('#start-mock').addEventListener('click', async (e) => {
    const ids = selectedThemes();
    const err = $('#config-error');
    if (!ids.length) { err.textContent = 'Select at least one theme.'; err.hidden = false; return; }
    const count = Number($$('input[name="qcount"]:checked')[0].value);
    const timed = $('#timed-toggle').checked;
    err.hidden = true;
    const btn = e.target; btn.disabled = true; btn.textContent = 'Building…';
    try {
      const datas = await Promise.all(ids.map(loadTheme));
      const pool = datas.flatMap(d => d.mockBank);
      const questions = shuffle(pool).slice(0, Math.min(count, pool.length));
      mockState = {
        config: { ids, count, timed },
        questions, index: 0,
        answers: new Array(questions.length).fill(null),
        timerId: null, remaining: SECONDS_PER_Q,
      };
      window.location.hash = '#/master/exam';
    } catch {
      btn.disabled = false; btn.textContent = 'Start mock exam';
      err.textContent = 'Could not load questions. Check your connection and try again.';
      err.hidden = false;
    }
  });
}

function renderMasterExam(app) {
  if (!mockState || !mockState.questions.length) { window.location.hash = '#/master'; return; }
  drawExamQuestion(app);
}

function drawExamQuestion(app) {
  const s = mockState;
  const q = s.questions[s.index];
  const n = s.questions.length;
  const pct = Math.round(((s.index) / n) * 100);
  const chosen = s.answers[s.index];

  const opts = q.options.map((o, i) => {
    const L = letter(i);
    return `<button class="option ${chosen === L ? 'chosen' : ''}" data-letter="${L}">
      <span class="option-key">${L}</span>
      <span class="option-text">${esc(o.replace(/^[A-E]\.\s*/, ''))}</span>
    </button>`;
  }).join('');

  const answeredCount = s.answers.filter(a => a !== null).length;

  app.innerHTML = `
    <div class="view exam-view">
      <div class="exam-bar">
        <div class="exam-progress-info">
          <strong>Question ${s.index + 1} of ${n}</strong>
          <span>${answeredCount} answered</span>
        </div>
        ${s.config.timed ? `<div class="exam-timer" id="exam-timer">${SECONDS_PER_Q}s</div>` : '<div class="exam-untimed">Untimed</div>'}
      </div>
      <div class="progress" role="progressbar" aria-valuenow="${pct}" aria-valuemin="0" aria-valuemax="100" aria-label="Exam progress">
        <div class="progress-fill" style="width:${pct}%"></div>
      </div>

      <article class="card sba exam-card">
        <p class="sba-scenario">${esc(q.question)}</p>
        <div class="options" id="exam-opts">${opts}</div>
      </article>

      <div class="exam-nav">
        <button class="btn btn-secondary" id="exam-prev" ${s.index === 0 ? 'disabled' : ''}>← Previous</button>
        ${s.index < n - 1
          ? '<button class="btn" id="exam-next">Next →</button>'
          : '<button class="btn" id="exam-submit">Submit exam</button>'}
      </div>
    </div>`;

  $$('#exam-opts .option').forEach(btn => btn.addEventListener('click', () => {
    s.answers[s.index] = btn.dataset.letter;
    $$('#exam-opts .option').forEach(b => b.classList.toggle('chosen', b === btn));
  }));

  const prev = $('#exam-prev');
  if (prev) prev.addEventListener('click', () => { stopTimer(); s.index--; drawExamQuestion(app); });
  const next = $('#exam-next');
  if (next) next.addEventListener('click', () => { stopTimer(); s.index++; drawExamQuestion(app); });
  const submit = $('#exam-submit');
  if (submit) submit.addEventListener('click', () => { stopTimer(); finishExam(); });

  if (s.config.timed) startTimer(app);
}

function startTimer(app) {
  const s = mockState;
  s.remaining = SECONDS_PER_Q;
  const el = $('#exam-timer');
  const tick = () => {
    s.remaining--;
    if (el) {
      el.textContent = `${s.remaining}s`;
      el.classList.toggle('urgent', s.remaining <= 10);
    }
    if (s.remaining <= 0) {
      clearInterval(s.timerId); s.timerId = null;
      // unanswered stays null (counts as wrong); auto-advance
      if (s.index < s.questions.length - 1) { s.index++; drawExamQuestion(app); }
      else finishExam();
    }
  };
  s.timerId = setInterval(tick, 1000);
}
function stopTimer() {
  if (mockState && mockState.timerId) { clearInterval(mockState.timerId); mockState.timerId = null; }
}

function finishExam() {
  const s = mockState;
  const n = s.questions.length;
  let score = 0;
  const byTheme = {};   // themeId → {correct,total}
  const byTopic = {};   // topicTag → {correct,total}

  s.questions.forEach((q, i) => {
    const right = s.answers[i] === q.correctAnswer;
    if (right) score++;
    (byTheme[q.theme] ??= { correct: 0, total: 0 });
    byTheme[q.theme].total++; if (right) byTheme[q.theme].correct++;
    (byTopic[q.topicTag] ??= { correct: 0, total: 0 });
    byTopic[q.topicTag].total++; if (right) byTopic[q.topicTag].correct++;
  });

  const breakdown = Object.entries(byTheme).map(([id, v]) => ({
    themeId: Number(id), title: themeMeta(id)?.title || `Theme ${id}`,
    correct: v.correct, total: v.total, pct: Math.round((v.correct / v.total) * 100),
  })).sort((a, b) => a.themeId - b.themeId);

  const weakTopics = Object.entries(byTopic)
    .filter(([, v]) => v.correct / v.total < 0.5)
    .map(([tag, v]) => ({ tag, label: prettyTag(tag), correct: v.correct, total: v.total }))
    .sort((a, b) => (a.correct / a.total) - (b.correct / b.total));

  const record = {
    date: new Date().toISOString(),
    dateLabel: new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }),
    themes: s.config.ids, totalQ: n, score,
    pct: Math.round((score / n) * 100),
    timed: s.config.timed,
    breakdown, weakTopics: weakTopics.map(w => w.label),
  };
  const all = store.getJSON('hd_mock_scores', []);
  all.push(record);
  store.setJSON('hd_mock_scores', all);

  mockState.result = { record, breakdown, weakTopics, score, n };
  window.location.hash = '#/master/results';
}

function renderMasterResults(app) {
  if (!mockState || !mockState.result) { window.location.hash = '#/master'; return; }
  const { record, breakdown, weakTopics, score, n } = mockState.result;

  const rows = breakdown.map(b => `
    <tr>
      <td>Theme ${b.themeId} — ${esc(b.title)}</td>
      <td class="num">${b.correct}/${b.total}</td>
      <td class="num"><span class="pct-pill ${b.pct < 50 ? 'low' : b.pct < 75 ? 'mid' : 'high'}">${b.pct}%</span></td>
    </tr>`).join('');

  const weakHTML = weakTopics.length
    ? `<ul class="weak-list">${weakTopics.map(w => `<li><span class="weak-tag">${esc(w.label)}</span><span class="weak-frac">${w.correct}/${w.total}</span></li>`).join('')}</ul>`
    : `<p class="all-clear">No weak topics — you scored 50%+ on every topic tested. 🎯</p>`;

  app.innerHTML = `
    <div class="view">
      ${breadcrumb([{ label: 'Home', href: '#/' }, { label: 'Master It', href: '#/master' }, { label: 'Results' }])}
      <div class="page-head"><h1>Mock results</h1></div>

      <div class="result-hero card big">
        <div class="result-score">${score}<span>/${n}</span></div>
        <p class="result-pct">${record.pct}%</p>
        <p class="result-sub">${record.dateLabel} · ${record.themes.length} theme${record.themes.length > 1 ? 's' : ''} · ${record.timed ? 'Timed' : 'Untimed'}</p>
      </div>

      <div class="card">
        <h3>Theme breakdown</h3>
        <table class="data-table">
          <thead><tr><th>Theme</th><th class="num">Score</th><th class="num">%</th></tr></thead>
          <tbody>${rows}</tbody>
        </table>
      </div>

      <div class="card">
        <div class="missed-head">
          <h3>Weak topics ${weakTopics.length ? `(<50% correct)` : ''}</h3>
          ${weakTopics.length ? '<button class="btn btn-secondary" id="copy-weak">Copy weak topics</button>' : ''}
        </div>
        ${weakHTML}
      </div>

      <div class="btn-row" style="margin-top:1.25rem">
        <button class="btn" id="try-again">Try again (same config)</button>
        <a class="btn btn-secondary" href="#/master">New mock</a>
        <a class="btn btn-ghost" href="#/progress">View score history</a>
      </div>
    </div>`;

  if (weakTopics.length) {
    $('#copy-weak').addEventListener('click', async (e) => {
      const text = `Human Diseases Master — Weak Topics (Mock on ${record.dateLabel})\n` +
        weakTopics.map(w => `- ${w.label}`).join('\n');
      flashButton(e.target, (await copyToClipboard(text)) ? 'Copied ✓' : 'Copy failed');
    });
  }

  $('#try-again').addEventListener('click', async (e) => {
    const btn = e.target; btn.disabled = true; btn.textContent = 'Building…';
    const { ids, count, timed } = record.themes
      ? { ids: record.themes, count: record.totalQ, timed: record.timed } : {};
    try {
      const datas = await Promise.all(ids.map(loadTheme));
      const pool = datas.flatMap(d => d.mockBank);
      const questions = shuffle(pool).slice(0, Math.min(count, pool.length));
      mockState = { config: { ids, count, timed }, questions, index: 0,
        answers: new Array(questions.length).fill(null), timerId: null, remaining: SECONDS_PER_Q };
      window.location.hash = '#/master/exam';
    } catch { btn.disabled = false; btn.textContent = 'Try again (same config)'; }
  });
}

/* ===================================================================
   STEP 9 — Score history + Canvas chart
   =================================================================== */
function renderProgress(app) {
  const scores = store.getJSON('hd_mock_scores', []);

  if (!scores.length) {
    app.innerHTML = `
      <div class="view">
        ${breadcrumb([{ label: 'Home', href: '#/' }, { label: 'Score History' }])}
        <div class="page-head"><h1>Score history</h1></div>
        <div class="empty-state card">
          <p>No mock exams yet.</p>
          <p>Complete a mock in <strong>Master It</strong> and your scores will be tracked here over time.</p>
          <a class="btn" href="#/master">Start your first mock</a>
        </div>
      </div>`;
    return;
  }

  const rows = scores.slice().reverse().map((r, i) => {
    const num = scores.length - i;
    return `<tr>
      <td class="num">#${num}</td>
      <td>${esc(r.dateLabel)}</td>
      <td class="num">${r.themes.length}</td>
      <td class="num">${r.totalQ}</td>
      <td class="num">${r.score}/${r.totalQ}</td>
      <td class="num"><span class="pct-pill ${r.pct < 50 ? 'low' : r.pct < 75 ? 'mid' : 'high'}">${r.pct}%</span></td>
    </tr>`;
  }).join('');

  const best = Math.max(...scores.map(r => r.pct));
  const latest = scores[scores.length - 1].pct;
  const avg = Math.round(scores.reduce((s, r) => s + r.pct, 0) / scores.length);

  app.innerHTML = `
    <div class="view">
      ${breadcrumb([{ label: 'Home', href: '#/' }, { label: 'Score History' }])}
      <div class="page-head">
        <h1>Score history</h1>
        <p class="lede">${scores.length} mock${scores.length > 1 ? 's' : ''} completed.</p>
      </div>

      <div class="stat-row">
        <div class="stat card"><span class="stat-num">${latest}%</span><span class="stat-label">Latest</span></div>
        <div class="stat card"><span class="stat-num">${best}%</span><span class="stat-label">Best</span></div>
        <div class="stat card"><span class="stat-num">${avg}%</span><span class="stat-label">Average</span></div>
      </div>

      <div class="card">
        <h3>Score over time</h3>
        <div class="chart-wrap"><canvas id="score-chart" height="260"></canvas></div>
      </div>

      <div class="card">
        <div class="missed-head">
          <h3>All mocks</h3>
          <button class="btn btn-ghost" id="clear-history">Clear history</button>
        </div>
        <table class="data-table">
          <thead><tr><th class="num">#</th><th>Date</th><th class="num">Themes</th><th class="num">Q</th><th class="num">Score</th><th class="num">%</th></tr></thead>
          <tbody>${rows}</tbody>
        </table>
      </div>
    </div>`;

  drawScoreChart(scores);

  $('#clear-history').addEventListener('click', () => {
    if (confirm('Clear all saved mock scores? This cannot be undone.')) {
      store.setJSON('hd_mock_scores', []);
      router();
    }
  });
}

function drawScoreChart(scores) {
  const canvas = $('#score-chart');
  if (!canvas) return;
  const ratio = window.devicePixelRatio || 1;
  const cssW = canvas.parentElement.clientWidth;
  const cssH = 260;
  canvas.width = cssW * ratio;
  canvas.height = cssH * ratio;
  canvas.style.width = cssW + 'px';
  canvas.style.height = cssH + 'px';
  const ctx = canvas.getContext('2d');
  ctx.scale(ratio, ratio);

  const pad = { l: 38, r: 16, t: 16, b: 28 };
  const W = cssW - pad.l - pad.r;
  const H = cssH - pad.t - pad.b;
  const pts = scores.map(r => r.pct);
  const n = pts.length;

  ctx.clearRect(0, 0, cssW, cssH);
  // Gridlines + y labels (0,25,50,75,100)
  ctx.strokeStyle = '#e2e8f0'; ctx.fillStyle = '#64748b';
  ctx.font = '11px Inter, sans-serif'; ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
  ctx.lineWidth = 1;
  [0, 25, 50, 75, 100].forEach(v => {
    const y = pad.t + H - (v / 100) * H;
    ctx.beginPath(); ctx.moveTo(pad.l, y); ctx.lineTo(pad.l + W, y); ctx.stroke();
    ctx.fillText(v + '%', pad.l - 6, y);
  });

  const x = (i) => n === 1 ? pad.l + W / 2 : pad.l + (i / (n - 1)) * W;
  const y = (v) => pad.t + H - (v / 100) * H;

  // Area fill
  if (n > 1) {
    ctx.beginPath();
    ctx.moveTo(x(0), y(pts[0]));
    pts.forEach((v, i) => ctx.lineTo(x(i), y(v)));
    ctx.lineTo(x(n - 1), pad.t + H);
    ctx.lineTo(x(0), pad.t + H);
    ctx.closePath();
    ctx.fillStyle = 'rgba(59,130,246,0.10)';
    ctx.fill();
  }
  // Line
  ctx.beginPath();
  pts.forEach((v, i) => i === 0 ? ctx.moveTo(x(i), y(v)) : ctx.lineTo(x(i), y(v)));
  ctx.strokeStyle = '#3b82f6'; ctx.lineWidth = 2.5; ctx.lineJoin = 'round';
  ctx.stroke();
  // Points + x labels
  ctx.textAlign = 'center'; ctx.textBaseline = 'top';
  pts.forEach((v, i) => {
    ctx.beginPath(); ctx.arc(x(i), y(v), 4, 0, Math.PI * 2);
    ctx.fillStyle = '#2563eb'; ctx.fill();
    ctx.strokeStyle = '#fff'; ctx.lineWidth = 2; ctx.stroke();
    ctx.fillStyle = '#64748b';
    ctx.fillText('#' + (i + 1), x(i), pad.t + H + 8);
  });
}

/* ===================================================================
   STEP 10 — Citations
   =================================================================== */
function renderCitations(app) {
  app.innerHTML = `
    <div class="view">
      ${breadcrumb([{ label: 'Home', href: '#/' }, { label: 'Sources & Citations' }])}
      <div class="page-head">
        <p class="eyebrow">References</p>
        <h1>Sources &amp; Citations</h1>
        <p class="lede">All Human Diseases Master content is derived from the sources below and validated by the course owner.</p>
      </div>

      <div class="card">
        <h3>Textbooks</h3>
        <ul class="cite-list">
          <li><em>Essentials of Human Disease in Dentistry</em>, 2nd Edition. Mark Greenwood. John Wiley &amp; Sons, 2018.</li>
          <li><em>Robbins and Kumar Basic Pathology</em>, 11th Edition. Vinay Kumar, Abul K. Abbas, Jon C. Aster, Andrea T. Deyrup.</li>
          <li><em>Underwood's Pathology: A Clinical Approach</em>, 7th Edition. S. Cross.</li>
          <li><em>Conscious Sedation for Dentistry</em>, 2nd Edition. Girdler N, Hill M and Wilson K.</li>
          <li><em>Pain and Anxiety Control for the Conscious Dental Patient</em>. Meechan JG, Robb ND, Seymour RA.</li>
        </ul>
      </div>

      <div class="card disclaimer">
        <h3>Disclaimer</h3>
        <p>Human Diseases Master is a free, non-commercial student revision tool built by a Newcastle BDS Year 3 student. All content is derived from the above sources and validated by the course owner. No clinical facts are invented. This app is not a replacement for the official teaching materials.</p>
      </div>
    </div>`;
}

/* ===================================================================
   Boot
   =================================================================== */
function init() {
  buildNav();
  $('#hamburger').addEventListener('click', toggleSidebar);
  $('#backdrop').addEventListener('click', closeSidebar);
  $('.skip-link').addEventListener('click', (e) => { e.preventDefault(); $('#app').focus(); });
  window.addEventListener('hashchange', router);
  window.addEventListener('resize', () => {
    if (currentPath() === '/progress') {
      const scores = store.getJSON('hd_mock_scores', []);
      if (scores.length) drawScoreChart(scores);
    }
  });
  router();
}
document.addEventListener('DOMContentLoaded', init);
