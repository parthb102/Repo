// Worked-example sizing exhibit: Data Scientist role
// Slide 1: benefit sizing (LHS) + investment sizing (RHS). Slide 2: assumptions backup.
const pptxgen = require("pptxgenjs");

/* ---------------------------------- data ---------------------------------- */
const D = {
  role: "Data Scientist",
  headcount: 200, loadedK: 190, costBaseM: 38.0,
  activities: [ // timePct sums to 100; poolM = costBase * time% * addressable%
    { name: "Data prep & cleaning",      time: 30, addr: 60, poolM: 6.8, ease: "E" },
    { name: "Model build & experiments", time: 20, addr: 35, poolM: 2.7, ease: "M" },
    { name: "Exploratory analysis",      time: 15, addr: 40, poolM: 2.3, ease: "M" },
    { name: "Reporting & documentation", time: 15, addr: 60, poolM: 3.4, ease: "E" },
    { name: "Stakeholder alignment",     time: 12, addr: 10, poolM: 0.5, ease: "H" },
    { name: "Ad-hoc requests",           time:  8, addr: 45, poolM: 1.4, ease: "M" },
  ],
  potentialM: 17.0, viabilityCut: 25, viableM: 12.8, captureCut: 35, capturableM: 8.3,
  priorities: [
    { rank: 1, name: "Data prep & cleaning", poolM: 6.8, ease: "E", note: "most mature tooling — the agentic backbone starts here" },
    { rank: 2, name: "Reporting & documentation", poolM: 3.4, ease: "E", note: "production-proven genAI — fast follow on the backbone" },
    { rank: 3, name: "Model build & experiments", poolM: 2.7, ease: "M", note: "real coding-assistant lift, judgment-heavy — wave 2" },
  ],
  useCase: {
    name: "Data Prep & Quality Agent",
    desc: "Agentic profiling, cleaning, joining and validation with human-review checkpoints, embedded in the DS workflow (warehouse, catalog, pipelines).",
    target: "Attacks pool No.1: $6.8M addressable, ~30% of every DS week",
  },
  phases: [
    { name: "Plan",           wks: 4,  fte: 3.75, costK: 65  },
    { name: "Build",          wks: 10, fte: 4.25, costK: 180 },
    { name: "Pilot",          wks: 6,  fte: 4.5,  costK: 115 },
    { name: "Deploy & scale", wks: 12, fte: 3.75, costK: 190 },
  ],
  team: "Product owner ×0.5  ·  2 AI/ML engineers  ·  Data engineer  ·  DS expert  ·  Change lead",
  oneTime: {
    totalM: 0.95,
    rows: [
      ["Build team (all four phases)", "$550K"],
      ["Platform & integration", "$250K"],
      ["Change management & training", "$120K"],
      ["Pre-production token spend", "$30K"],
    ],
  },
  recurring: {
    totalK: 585,
    rows: [
      ["Model / token consumption", "$300K"],
      ["Licensing & tooling ($50/user/mo)", "$120K"],
      ["Run team (~0.75 FTE)", "$165K"],
    ],
    note: "Tokens ≈ 200 DS × ~$6.50/day blended (heavy users well above) × 230 days — the line business cases forget",
  },
  value: {
    steadyM: 3.3, rampNote: "Ramp starts 1–3 mo post-deploy", yr1: 40,
    stats: [
      { big: "$3.3M/yr", small: "steady-state = pool No.1 × 75% viability × 65% capture — a subset of the $8.3M, not additive" },
      { big: "~40%", small: "captured in year 1; ramp starts 1–3 mo post-deploy → payback ≈12 mo gross, ~14 mo net of run cost" },
      { big: "~5×", small: "running return: $3.3M/yr value vs $0.59M/yr run cost" },
    ],
  },
};

/* --------------------------------- tokens ---------------------------------- */
const INK = "1F2A33", MUTED = "5C6B77", FAINT = "8B98A2", LINE = "DCE3E8";
const TEAL = "129682", TEAL_DK = "0B6B5D", TEAL_LT = "A9D8CE", TEAL_BG = "EFF6F3";
const INDIGO = "5A6BE0", INDIGO_DK = "3D4BB5", INDIGO_LT = "C3CBF2", INDIGO_BG = "EFF1FA";
const AMBER = "C77414", AMBER_LT = "F2DBBC";
const WHITE = "FFFFFF";
const EASE = { E: { t: "EASY", fg: "0B6B5D", bg: "D9EEE7" }, M: { t: "MED", fg: "8A5407", bg: "F4E3C6" }, H: { t: "HARD", fg: "7A4040", bg: "EFDBDB" } };
const F = "Arial";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.author = "AI Transformation Program";

const t = (s, txt, o) => s.addText(txt, Object.assign({ isTextBox: true, fontFace: F, margin: 0, color: INK }, o));

/* ================================ SLIDE 1 ================================= */
const s = pres.addSlide();
s.background = { color: WHITE };
s.addNotes("Worked example used in office hours: how to size an AI business case bottom-up. Left: the benefit chain for one role (cost base -> addressable -> capturable -> prioritized). Right: the investment for the No.1 opportunity, one-time vs recurring, with tokens explicitly modeled. All numbers illustrative.");

/* header */
t(s, "AI TRANSFORMATION  ·  HOW TO SIZE A BUSINESS CASE  ·  WORKED EXAMPLE", { x: 0.45, y: 0.26, w: 8.6, h: 0.22, fontSize: 9, bold: true, color: MUTED, charSpacing: 2 });
t(s, [
  { text: "Data scientists: a $38M cost base yields ", options: {} },
  { text: "~$8.3M capturable", options: { color: AMBER, bold: true } },
  { text: " — and the first agent build returns ~5× its run cost", options: {} },
], { x: 0.45, y: 0.48, w: 10.4, h: 0.62, fontSize: 19, bold: true, color: INK });
// illustrative pill
s.addShape("roundRect", { x: 11.05, y: 0.38, w: 1.83, h: 0.34, rectRadius: 0.17, fill: { color: INK } });
t(s, "ILLUSTRATIVE", { x: 11.05, y: 0.38, w: 1.83, h: 0.34, fontSize: 9, bold: true, color: WHITE, align: "center", valign: "middle", charSpacing: 2 });

/* panels */
const PL = { x: 0.45, w: 6.0 }, PR = { x: 6.88, w: 6.0 }, PY = 1.16, PH = 5.78;
s.addShape("roundRect", { x: PL.x, y: PY, w: PL.w, h: PH, rectRadius: 0.06, fill: { color: TEAL_BG } });
s.addShape("roundRect", { x: PR.x, y: PY, w: PR.w, h: PH, rectRadius: 0.06, fill: { color: INDIGO_BG } });

const LX = PL.x + 0.22, LW = PL.w - 0.44; // 0.67, 5.56
const RX = PR.x + 0.22, RW = PR.w - 0.44; // 7.10, 5.56

t(s, "SIZING THE BENEFIT — BOTTOM-UP, NOT TOP-DOWN", { x: LX, y: PY + 0.14, w: LW, h: 0.24, fontSize: 11, bold: true, color: TEAL_DK, charSpacing: 1.5 });
t(s, "SIZING THE INVESTMENT — FOR OPPORTUNITY No.1", { x: RX, y: PY + 0.14, w: RW, h: 0.24, fontSize: 11, bold: true, color: INDIGO_DK, charSpacing: 1.5 });

/* step chip helper (numbered: the method is a sequence) */
function step(x, y, n, label, color) {
  s.addShape("ellipse", { x, y: y + 0.015, w: 0.21, h: 0.21, fill: { color } });
  t(s, String(n), { x, y: y + 0.015, w: 0.21, h: 0.21, fontSize: 10, bold: true, color: WHITE, align: "center", valign: "middle" });
  t(s, label, { x: x + 0.29, y, w: 5.3, h: 0.24, fontSize: 10.5, bold: true, color: INK, valign: "middle" });
}

/* ---- L1: cost base ---- */
step(LX, 1.52, 1, "Start from the current cost base", TEAL_DK);
t(s, "$38.0M", { x: LX, y: 1.80, w: 1.62, h: 0.44, fontSize: 26, bold: true, color: TEAL_DK });
t(s, "annual cost base  =  200 data-scientist FTEs × $190K fully loaded", { x: LX + 1.72, y: 1.84, w: 3.85, h: 0.38, fontSize: 9.5, color: MUTED, valign: "middle" });

/* ---- L2: activity bars ---- */
step(LX, 2.38, 2, "Map the week — how much of each activity can AI address?", TEAL_DK);
t(s, "bar = share of week · dark fill = AI-addressable · $ = addressable pool / yr", { x: LX + 0.29, y: 2.60, w: 5.2, h: 0.18, fontSize: 7.5, italic: true, color: FAINT });
{
  const y0 = 2.84, rh = 0.265, bx = LX + 1.78, bmax = 2.52, scale = bmax / 30; // 30% = widest bar
  D.activities.forEach((a, i) => {
    const y = y0 + i * rh;
    t(s, a.name, { x: LX, y, w: 1.72, h: 0.22, fontSize: 8.5, color: INK, valign: "middle" });
    const wTime = a.time * scale, wAddr = wTime * a.addr / 100;
    s.addShape("rect", { x: bx, y: y + 0.035, w: wTime, h: 0.15, fill: { color: TEAL_LT } });
    s.addShape("rect", { x: bx, y: y + 0.035, w: wAddr, h: 0.15, fill: { color: TEAL_DK } });
    t(s, `${a.time}%`, { x: bx + wTime + 0.05, y, w: 0.42, h: 0.22, fontSize: 7.5, color: FAINT, valign: "middle" });
    t(s, `$${a.poolM.toFixed(1)}M`, { x: LX + 4.62, y, w: 0.52, h: 0.22, fontSize: 8.5, bold: true, color: TEAL_DK, align: "right", valign: "middle" });
    const e = EASE[a.ease];
    s.addShape("roundRect", { x: LX + 5.24, y: y + 0.025, w: 0.40, h: 0.17, rectRadius: 0.05, fill: { color: e.bg } });
    t(s, e.t, { x: LX + 5.24, y: y + 0.025, w: 0.40, h: 0.17, fontSize: 6.5, bold: true, color: e.fg, align: "center", valign: "middle" });
  });
}

/* ---- L3: haircut waterfall ---- */
step(LX, 4.54, 3, "Haircut potential down to what you can actually capture", TEAL_DK);
{
  const rows = [
    { label: "Theoretical potential", vM: 17.0, txt: "$17.0M", fill: TEAL, dim: false },
    { cut: "− 25% viability — data access, tooling maturity, governance" },
    { label: "Viable potential", vM: 12.8, txt: "$12.8M", fill: TEAL, dim: false },
    { cut: "− 35% capture — adoption ramp; assumes funded change mgmt (unmanaged = 20–40%)" },
    { label: "Capturable  (≈22% of cost base)", vM: 8.3, txt: "$8.3M", fill: AMBER, bold: true },
  ];
  let y = 4.80; const bx = LX + 1.98, bmax = 2.55, scale = bmax / 17.0;
  rows.forEach(r => {
    if (r.cut) { t(s, r.cut, { x: bx + 0.1, y, w: 3.5, h: 0.17, fontSize: 7.5, italic: true, color: MUTED, valign: "middle" }); y += 0.185; return; }
    t(s, r.label, { x: LX, y, w: 1.92, h: 0.21, fontSize: 8.5, bold: !!r.bold, color: r.bold ? AMBER : INK, valign: "middle" });
    s.addShape("rect", { x: bx, y: y + 0.025, w: r.vM * scale, h: 0.155, fill: { color: r.fill } });
    t(s, r.txt, { x: bx + r.vM * scale + 0.06, y, w: 0.62, h: 0.21, fontSize: 8.5, bold: true, color: r.bold ? AMBER : TEAL_DK, valign: "middle" });
    y += 0.235;
  });
}

/* ---- L4: prioritize ---- */
step(LX, 5.94, 4, "Prioritize by size × ease — go easy-first", TEAL_DK);
{
  const y0 = 6.20, rh = 0.235;
  D.priorities.forEach((p, i) => {
    const y = y0 + i * rh;
    t(s, `${p.rank}.`, { x: LX + 0.02, y, w: 0.2, h: 0.2, fontSize: 8.5, bold: true, color: TEAL_DK, valign: "middle" });
    t(s, [
      { text: `${p.name}  `, options: { bold: true } },
      { text: `$${p.poolM.toFixed(1)}M pool — ${p.note}`, options: { color: MUTED } },
    ], { x: LX + 0.24, y, w: 5.3, h: 0.2, fontSize: 8, color: INK, valign: "middle" });
  });
}

/* ---- R: use case banner ---- */
s.addShape("roundRect", { x: RX, y: 1.50, w: RW, h: 0.66, rectRadius: 0.05, fill: { color: INDIGO_DK } });
t(s, [
  { text: "BUILD:  ", options: { color: INDIGO_LT, bold: true } },
  { text: D.useCase.name + "  —  ", options: { color: WHITE, bold: true } },
  { text: D.useCase.target, options: { color: INDIGO_LT } },
], { x: RX + 0.14, y: 1.50, w: RW - 0.28, h: 0.40, fontSize: 10, valign: "middle" });
t(s, D.useCase.desc, { x: RX + 0.14, y: 1.86, w: RW - 0.28, h: 0.28, fontSize: 7.5, color: "D9DEF5", valign: "top" });

/* ---- R1: phase timeline ---- */
t(s, "FOUR PHASES  ·  ≈32 WEEKS (~7½ MONTHS)", { x: RX, y: 2.30, w: RW, h: 0.2, fontSize: 9.5, bold: true, color: INDIGO_DK, charSpacing: 1 });
{
  const totW = D.phases.reduce((a, p) => a + p.wks, 0);
  const gap = 0.03, availW = RW - gap * 3, y = 2.56, h = 0.34;
  const shades = ["8E9AE8", "7583E4", "5A6BE0", "3D4BB5"];
  let x = RX;
  D.phases.forEach((p, i) => {
    const w = (p.wks / totW) * availW;
    s.addShape("rect", { x, y, w, h, fill: { color: shades[i] } });
    t(s, `${p.name.toUpperCase()}`, { x, y, w, h: 0.2, fontSize: 7, bold: true, color: WHITE, align: "center", valign: "middle" });
    t(s, `${p.wks} wks`, { x, y: y + 0.16, w, h: 0.16, fontSize: 6.5, color: WHITE, align: "center", valign: "middle" });
    t(s, `${p.fte} FTE`, { x, y: y + 0.38, w, h: 0.16, fontSize: 7.5, bold: true, color: INK, align: "center" });
    t(s, `$${p.costK}K`, { x, y: y + 0.53, w, h: 0.16, fontSize: 7.5, color: MUTED, align: "center" });
    x += w + gap;
  });
  t(s, "Team:  " + D.team, { x: RX, y: 3.30, w: RW, h: 0.18, fontSize: 7.5, color: MUTED });
}

/* ---- R2: cost cards ---- */
t(s, "WHAT IT COSTS", { x: RX, y: 3.58, w: RW, h: 0.2, fontSize: 9.5, bold: true, color: INDIGO_DK, charSpacing: 1 });
{
  const cy = 3.82, ch = 1.66, cw = (RW - 0.14) / 2;
  const card = (x, title, total, rows, note) => {
    s.addShape("roundRect", { x, y: cy, w: cw, h: ch, rectRadius: 0.05, fill: { color: WHITE }, line: { color: LINE, width: 1 } });
    t(s, [
      { text: title + "   ", options: { bold: true, color: MUTED, fontSize: 8 } },
      { text: total, options: { bold: true, color: INDIGO_DK, fontSize: 13 } },
    ], { x: x + 0.12, y: cy + 0.08, w: cw - 0.24, h: 0.26, valign: "middle" });
    let y = cy + 0.40;
    rows.forEach(r => {
      t(s, r[0], { x: x + 0.12, y, w: cw - 0.75, h: 0.19, fontSize: 8, color: INK, valign: "middle" });
      t(s, r[1], { x: x + cw - 0.66, y, w: 0.54, h: 0.19, fontSize: 8, bold: true, color: INK, align: "right", valign: "middle" });
      y += 0.21;
    });
    if (note) t(s, note, { x: x + 0.12, y: cy + ch - 0.40, w: cw - 0.24, h: 0.36, fontSize: 6.8, italic: true, color: MUTED, valign: "bottom" });
  };
  card(RX, "ONE-TIME", "$0.95M", D.oneTime.rows, "People cost = FTE-weeks \u00d7 ~$4,200 blended loaded rate, by phase");
  card(RX + cw + 0.14, "RECURRING / YR", "$585K", D.recurring.rows, D.recurring.note);
}

/* ---- R3: returns ---- */
t(s, "WHAT IT RETURNS", { x: RX, y: 5.66, w: RW, h: 0.2, fontSize: 9.5, bold: true, color: INDIGO_DK, charSpacing: 1 });
{
  const cy = 5.90, ch = 0.88, cw = (RW - 0.28) / 3;
  D.value.stats.forEach((st, i) => {
    const x = RX + i * (cw + 0.14);
    s.addShape("roundRect", { x, y: cy, w: cw, h: ch, rectRadius: 0.05, fill: { color: i === 2 ? AMBER_LT : WHITE }, line: { color: i === 2 ? AMBER : LINE, width: 1 } });
    t(s, st.big, { x: x + 0.1, y: cy + 0.06, w: cw - 0.2, h: 0.3, fontSize: 16, bold: true, color: i === 2 ? "8A5407" : INDIGO_DK });
    t(s, st.small, { x: x + 0.1, y: cy + 0.36, w: cw - 0.2, h: 0.48, fontSize: 7, color: MUTED, valign: "top" });
  });
}

/* footnote */
s.addShape("line", { x: 0.45, y: 7.06, w: 12.43, h: 0, line: { color: LINE, width: 0.75 } });
t(s, "Illustrative walkthrough of the sizing method — not a plan of record. Activity pools are pre-haircut addressable value, rounded to $0.1M (rounded pools sum to $17.1M vs the $17.0M unrounded potential). Capturable value is capacity (hiring avoidance, throughput, redeployment), not automatic cost-out. Token costs are explicitly modeled, one-time and recurring.", { x: 0.45, y: 7.12, w: 12.43, h: 0.30, fontSize: 7.5, color: FAINT });

/* ================================ SLIDE 2 ================================= */
const s2 = pres.addSlide();
s2.background = { color: WHITE };
s2.addNotes("Backup: the assumptions behind every number on the worked example. Reuse the structure, not the numbers - replace each assumption with your own role's data.");

t(s2, "BACKUP  ·  WORKED EXAMPLE — DATA SCIENTIST", { x: 0.45, y: 0.26, w: 8.6, h: 0.22, fontSize: 9, bold: true, color: MUTED, charSpacing: 2 });
t(s2, "Key assumptions — replace these with your role’s data before reusing the math", { x: 0.45, y: 0.48, w: 11.0, h: 0.5, fontSize: 19, bold: true, color: INK });
s2.addShape("roundRect", { x: 11.05, y: 0.38, w: 1.83, h: 0.34, rectRadius: 0.17, fill: { color: INK } });
t(s2, "ILLUSTRATIVE", { x: 11.05, y: 0.38, w: 1.83, h: 0.34, fontSize: 9, bold: true, color: WHITE, align: "center", valign: "middle", charSpacing: 2 });

const LHS_A = [
  ["Cost base", "200 data-scientist FTEs × $190K fully loaded = $38M/yr. Benefit is sized bottom-up from activities — never top-down from a benchmark percentage."],
  ["Time allocation", "Anchored to industry surveys (Anaconda, Kaggle): data prep and cleaning consistently absorbs 30–45% of a data scientist’s week."],
  ["Addressability", "Anchored to observed tool performance: 30–50% coding-assistant speedups, production-proven genAI reporting, near-zero for relationship work."],
  ["Haircut 1 — viability (−25%)", "Data-access gaps, tooling maturity, and model-governance / regulatory constraints."],
  ["Haircut 2 — capture (−35%)", "Adoption ramp (20–40% early adoption is typical unmanaged) and capacity reinvested in backlog rather than released."],
  ["Capturable ≠ cost-out", "$8.3M (~22% of cost base) is capacity — realized as hiring avoidance, throughput, or redeployment. Releasing vs reinvesting it is a leadership decision, not a model output."],
];
const RHS_A = [
  ["Team cost", "Blended fully-loaded ~$220K/yr (~$4,200 per FTE-week) across product, AI/ML engineering, data engineering, SME and change roles; phase costs = FTE-weeks × rate."],
  ["Timeline", "≈32 weeks: Plan 4 · Build 10 · Pilot 6 · Deploy & scale 12. Waves roll out easy datasets and teams first, building the reusable agentic backbone."],
  ["Tokens modeled explicitly", "~$300K/yr in production (200 DS × ~$6.50/day × 230 days) plus $30K pre-production — the cost line business cases most often miss. Pilot measures real cost per workflow."],
  ["Change management is funded", "$120K one-time, because unmanaged adoption benchmarks at 20–40% — the single biggest driver of the capture haircut."],
  ["Value ties to the left side", "Steady-state $3.3M/yr = the $6.8M data-prep pool after both haircuts (×0.75 × 0.65). No double counting: adjacent capabilities added during deploy (documentation, feature prep) are credited to the wave-2 cases, not this one."],
  ["Run costs", "~0.75-FTE run team + licensing + tokens = $585K/yr, under 20% of steady-state value — a ~5× running return. Payback ≈12 months gross, ~14 months net of run costs."],
];

function assumptionCol(x, title, color, bg, items) {
  s2.addShape("roundRect", { x, y: 1.16, w: 6.0, h: 5.78, rectRadius: 0.06, fill: { color: bg } });
  t(s2, title, { x: x + 0.22, y: 1.30, w: 5.56, h: 0.24, fontSize: 11, bold: true, color, charSpacing: 1.5 });
  let y = 1.70;
  items.forEach(it => {
    t(s2, it[0], { x: x + 0.22, y, w: 5.56, h: 0.2, fontSize: 9.5, bold: true, color });
    t(s2, it[1], { x: x + 0.22, y: y + 0.20, w: 5.56, h: 0.56, fontSize: 8.5, color: INK, valign: "top" });
    y += 0.87;
  });
}
assumptionCol(0.45, "BENEFIT SIDE", TEAL_DK, TEAL_BG, LHS_A);
assumptionCol(6.88, "INVESTMENT SIDE", INDIGO_DK, INDIGO_BG, RHS_A);

s2.addShape("line", { x: 0.45, y: 7.06, w: 12.43, h: 0, line: { color: LINE, width: 0.75 } });
t(s2, "All figures illustrative, for the method walkthrough. Sensitivity: the model is most sensitive to the baseline (headcount × loaded cost × time allocation) — validate the baseline with Finance before the automation percentages.", { x: 0.45, y: 7.12, w: 12.43, h: 0.30, fontSize: 7.5, color: FAINT });

pres.writeFile({ fileName: "ds-sizing-example.pptx" }).then(() => console.log("written"));
