// Worked-example sizing exhibit v4: three-activity teaching example, self-contained funnel
const pptxgen = require("pptxgenjs");

/* tokens */
const INK = "1F2A33", MUTED = "5C6B77", FAINT = "8B98A2", LINE = "DCE3E8";
const TEAL = "129682", TEAL_DK = "0B6B5D", TEAL_LT = "BFE0D8", TEAL_BG = "EFF6F3";
const INDIGO_DK = "3D4BB5", INDIGO_BG = "EFF1FA";
const AMBER_DK = "9A5A0B", AMBER = "C77414", AMBER_LT = "EFD9B8";
const ROSE_DK = "9A4E58", ROSE_LT = "EBD3D6";
const WHITE = "FFFFFF";
const F = "Arial";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.author = "AI Transformation Program";

const T = (s, txt, o) => s.addText(txt, Object.assign({ isTextBox: true, fontFace: F, margin: 0, color: INK }, o));

/* ================================ SLIDE 1 ================================= */
const s = pres.addSlide();
s.background = { color: WHITE };
s.addNotes("Worked example: how to size an AI business case bottom-up, using three activities to keep it simple. Left: cost base -> map the week -> add the pools and haircut -> prioritize. Right: what the first build costs, one-time and recurring. All numbers illustrative.");

/* header */
T(s, "AI TRANSFORMATION  ·  HOW TO SIZE A BUSINESS CASE  ·  WORKED EXAMPLE", { x: 0.55, y: 0.26, w: 8.6, h: 0.22, fontSize: 9, bold: true, color: MUTED, charSpacing: 2 });
T(s, [
  { text: "Data scientists: three activities yield ", options: {} },
  { text: "~$3M capturable", options: { color: AMBER, bold: true } },
  { text: " — for a ~$1M build", options: {} },
], { x: 0.55, y: 0.48, w: 10.4, h: 0.5, fontSize: 20, bold: true, color: INK });
s.addShape("roundRect", { x: 11.0, y: 0.40, w: 1.83, h: 0.34, rectRadius: 0.17, fill: { color: INK } });
T(s, "ILLUSTRATIVE", { x: 11.0, y: 0.40, w: 1.83, h: 0.34, fontSize: 9, bold: true, color: WHITE, align: "center", valign: "middle", charSpacing: 2 });

/* numbered step header */
function step(x, y, n, label) {
  s.addShape("ellipse", { x, y: y + 0.02, w: 0.24, h: 0.24, fill: { color: TEAL_DK } });
  T(s, String(n), { x, y: y + 0.02, w: 0.24, h: 0.24, fontSize: 11, bold: true, color: WHITE, align: "center", valign: "middle" });
  T(s, label, { x: x + 0.34, y, w: 6.0, h: 0.28, fontSize: 13.5, bold: true, color: INK, valign: "middle" });
}

const LX = 0.55;

/* 1 — cost base */
step(LX, 1.30, 1, "Start from the current cost base");
T(s, [
  { text: "$38.0M", options: { fontSize: 28, bold: true, color: TEAL_DK } },
  { text: "   (e.g., 200 data-scientist FTEs × $190K fully loaded)", options: { fontSize: 11, color: MUTED } },
], { x: LX + 0.34, y: 1.62, w: 6.1, h: 0.48, valign: "middle" });

/* 2 — map the week (three example activities) */
step(LX, 2.32, 2, "Map the week — how much of each activity can AI address?");
T(s, "bar = share of the week  ·  dark fill = what AI can address today  ·  $ = that pool per year", { x: LX + 0.34, y: 2.60, w: 6.0, h: 0.2, fontSize: 9, italic: true, color: FAINT });
const ACT = [
  { name: "Data prep & cleaning",  time: 30, addr: 60, poolM: 3, dk: TEAL_DK,  lt: TEAL_LT },
  { name: "Exploratory analysis",  time: 15, addr: 40, poolM: 2, dk: AMBER_DK, lt: AMBER_LT },
  { name: "Stakeholder alignment", time: 12, addr: 10, poolM: 1, dk: ROSE_DK,  lt: ROSE_LT },
];
{
  const y0 = 2.88, rh = 0.46, bx = LX + 2.42, scale = 2.5 / 30;
  ACT.forEach((r, i) => {
    const y = y0 + i * rh;
    T(s, r.name, { x: LX + 0.34, y, w: 2.02, h: 0.34, fontSize: 12.5, color: INK, valign: "middle" });
    const wT = r.time * scale, wA = wT * r.addr / 100;
    s.addShape("rect", { x: bx, y: y + 0.06, w: wT, h: 0.22, fill: { color: r.lt } });
    s.addShape("rect", { x: bx, y: y + 0.06, w: wA, h: 0.22, fill: { color: r.dk } });
    T(s, "$" + r.poolM + "M", { x: bx + wT + 0.12, y, w: 0.95, h: 0.34, fontSize: 13, bold: true, color: r.dk, valign: "middle" });
  });
}

/* 3 — add up, then haircut */
step(LX, 4.50, 3, "Add the pools up — then haircut to what you can capture");
{
  const bx = LX + 2.42, scale = 2.5 / 6.0;
  let y = 4.82;
  // sum bar: the three pools from step 2, stacked in the same colours
  T(s, "The three pools together", { x: LX + 0.34, y, w: 2.02, h: 0.26, fontSize: 11, color: INK, valign: "middle" });
  let sx = bx;
  ACT.forEach(r => {
    s.addShape("rect", { x: sx, y: y + 0.045, w: r.poolM * scale - 0.02, h: 0.18, fill: { color: r.dk } });
    sx += r.poolM * scale;
  });
  T(s, "$6M", { x: sx + 0.08, y, w: 2.2, h: 0.26, fontSize: 11.5, bold: true, color: TEAL_DK, valign: "middle" });
  y += 0.28;
  const items = [
    { cut: "− you already cover some of this today — tools in place, learned via interviews  (−25%)" },
    { label: "Truly new opportunity", vM: 4.5, txt: "$4.5M", fill: TEAL, lc: TEAL_DK },
    { cut: "− not everything gets captured — people adopt gradually, freed time is reinvested  (−35%)" },
    { label: "Capturable", vM: 3.0, txt: "~$3M / yr", fill: AMBER, lc: AMBER_DK, bold: true },
  ];
  items.forEach(it => {
    if (it.cut) {
      T(s, it.cut, { x: bx - 1.3, y, w: 5.4, h: 0.2, fontSize: 9.5, italic: true, color: MUTED, valign: "middle" });
      y += 0.20; return;
    }
    T(s, it.label, { x: LX + 0.34, y, w: 2.02, h: 0.26, fontSize: 11, bold: !!it.bold, color: it.bold ? AMBER_DK : INK, valign: "middle" });
    s.addShape("rect", { x: bx, y: y + 0.045, w: it.vM * scale, h: 0.18, fill: { color: it.fill } });
    T(s, it.txt, { x: bx + it.vM * scale + 0.1, y, w: 2.2, h: 0.26, fontSize: 11.5, bold: true, color: it.lc, valign: "middle" });
    y += 0.28;
  });
}

/* 4 — prioritize the same three */
step(LX, 6.22, 4, "Prioritize by size × ease — go easy-first");
{
  const rows = [
    ["1.", "Data prep & cleaning", "$3M pool, easy — the agent build starts here", TEAL_DK],
    ["2.", "Exploratory analysis", "$2M pool, medium — fast follow on the same backbone", AMBER_DK],
    ["3.", "Stakeholder alignment", "$1M pool, hard and human-led — don’t build here yet", ROSE_DK],
  ];
  const y0 = 6.50, rh = 0.25;
  rows.forEach((r, i) => {
    const y = y0 + i * rh;
    T(s, r[0], { x: LX + 0.36, y, w: 0.24, h: 0.22, fontSize: 10.5, bold: true, color: r[3], valign: "middle" });
    T(s, [
      { text: r[1] + "   ", options: { bold: true } },
      { text: r[2], options: { color: MUTED } },
    ], { x: LX + 0.62, y, w: 6.0, h: 0.22, fontSize: 10.5, color: INK, valign: "middle" });
  });
}

/* RHS — investment panel */
const RXP = 7.05, RWP = 5.75;
s.addShape("roundRect", { x: RXP, y: 1.30, w: RWP, h: 6.06, rectRadius: 0.07, fill: { color: INDIGO_BG } });
const RX = RXP + 0.32, RW = RWP - 0.64;

T(s, "SIZING THE INVESTMENT", { x: RX, y: 1.56, w: RW, h: 0.26, fontSize: 12.5, bold: true, color: INDIGO_DK, charSpacing: 1.5 });
T(s, "e.g., build a Data Prep Agent to go after opportunity No. 1", { x: RX, y: 1.84, w: RW, h: 0.24, fontSize: 11, color: MUTED });

/* build & test */
T(s, [
  { text: "BUILD & TEST      ", options: { fontSize: 11, bold: true, color: MUTED, charSpacing: 1.5 } },
  { text: "$0.95M", options: { fontSize: 26, bold: true, color: INDIGO_DK } },
  { text: "  one-time", options: { fontSize: 11, color: MUTED } },
], { x: RX, y: 2.34, w: RW, h: 0.44, valign: "middle" });
{
  const phases = [["PLAN", 4], ["BUILD", 10], ["PILOT", 6], ["DEPLOY", 12]];
  const shades = ["8E9AE8", "7583E4", "5A6BE0", "3D4BB5"];
  const totW = 32, gap = 0.04, availW = RW - gap * 3, y = 2.92, h = 0.42;
  let x = RX;
  phases.forEach((p, i) => {
    const w = (p[1] / totW) * availW;
    s.addShape("rect", { x, y, w, h, fill: { color: shades[i] } });
    T(s, p[0], { x, y: y + 0.04, w, h: 0.18, fontSize: 8.5, bold: true, color: WHITE, align: "center", valign: "middle" });
    T(s, `${p[1]} wks`, { x, y: y + 0.21, w, h: 0.16, fontSize: 8, color: WHITE, align: "center", valign: "middle" });
    x += w + gap;
  });
  T(s, "A ~4-person team — product, AI engineers, data engineering, a DS expert — for ~7½ months", { x: RX, y: 3.46, w: RW, h: 0.22, fontSize: 10, color: MUTED });
  const rows = [
    ["Build team", "$550K"],
    ["Platform, integration & pilot tokens", "$280K"],
    ["Change management & training", "$120K"],
  ];
  let ry = 3.82;
  rows.forEach(r => {
    T(s, r[0], { x: RX, y: ry, w: RW - 0.9, h: 0.24, fontSize: 11, color: INK, valign: "middle" });
    T(s, r[1], { x: RX + RW - 0.85, y: ry, w: 0.85, h: 0.24, fontSize: 11, bold: true, color: INK, align: "right", valign: "middle" });
    ry += 0.30;
  });
}

s.addShape("line", { x: RX, y: 4.90, w: RW, h: 0, line: { color: "C9CFEA", width: 1 } });

/* run */
T(s, [
  { text: "RUN      ", options: { fontSize: 11, bold: true, color: MUTED, charSpacing: 1.5 } },
  { text: "$585K", options: { fontSize: 26, bold: true, color: INDIGO_DK } },
  { text: "  per year", options: { fontSize: 11, color: MUTED } },
], { x: RX, y: 5.10, w: RW, h: 0.44, valign: "middle" });
{
  const rows = [
    ["Model & token consumption", "$300K"],
    ["Licensing & tooling", "$120K"],
    ["Run team (~0.75 FTE)", "$165K"],
  ];
  let ry = 5.66;
  rows.forEach(r => {
    T(s, r[0], { x: RX, y: ry, w: RW - 0.9, h: 0.24, fontSize: 11, color: INK, valign: "middle" });
    T(s, r[1], { x: RX + RW - 0.85, y: ry, w: 0.85, h: 0.24, fontSize: 11, bold: true, color: INK, align: "right", valign: "middle" });
    ry += 0.30;
  });
  T(s, "Tokens sized explicitly (~200 users × ~$6.50/day × 230 days) — the line business cases forget", { x: RX, y: 6.64, w: RW, h: 0.4, fontSize: 9.5, italic: true, color: MUTED, valign: "top" });
}

/* footnote */
T(s, "Illustrative — a walkthrough of the method, not a plan of record. Detailed assumptions: backup slide.", { x: 0.55, y: 7.30, w: 12.3, h: 0.18, fontSize: 8, color: FAINT });

/* ================================ SLIDE 2 ================================= */
const s2 = pres.addSlide();
s2.background = { color: WHITE };
s2.addNotes("Backup: the assumptions behind every number on the worked example. Reuse the structure, not the numbers - replace each assumption with your own role's data.");

T(s2, "BACKUP  ·  WORKED EXAMPLE — DATA SCIENTIST", { x: 0.55, y: 0.26, w: 8.6, h: 0.22, fontSize: 9, bold: true, color: MUTED, charSpacing: 2 });
T(s2, "Key assumptions — replace these with your role’s data before reusing the math", { x: 0.55, y: 0.48, w: 10.4, h: 0.5, fontSize: 19, bold: true, color: INK });
s2.addShape("roundRect", { x: 11.0, y: 0.40, w: 1.83, h: 0.34, rectRadius: 0.17, fill: { color: INK } });
T(s2, "ILLUSTRATIVE", { x: 11.0, y: 0.40, w: 1.83, h: 0.34, fontSize: 9, bold: true, color: WHITE, align: "center", valign: "middle", charSpacing: 2 });

const LHS_A = [
  ["Cost base", "200 data-scientist FTEs × $190K fully loaded = $38M/yr. The benefit is sized bottom-up from activities — never top-down from a benchmark percentage."],
  ["Time allocation", "Anchored to industry surveys (Anaconda, Kaggle): data prep and cleaning consistently absorbs 30–45% of a data scientist’s week."],
  ["Addressability", "Anchored to observed tool performance: 30–50% coding-assistant speedups, production-proven genAI reporting, near-zero for relationship work."],
  ["Haircut 1 — already covered today (−25%)", "What existing tools and automations already handle — learned through interviews and usage data — plus data-access and governance constraints."],
  ["Haircut 2 — capture (−35%)", "People adopt gradually (20–40% is typical unmanaged), and freed capacity is often reinvested in backlog rather than released."],
  ["Capturable ≠ cost-out", "Capturable value is capacity — realized as hiring avoidance, throughput, or redeployment. Releasing vs reinvesting it is a leadership decision. Three activities are shown for clarity; a full sizing maps the whole week."],
];
const RHS_A = [
  ["Team cost", "Blended fully-loaded ~$220K/yr (~$4,200 per FTE-week) across product, AI/ML engineering, data engineering, SME and change roles; phase costs = FTE-weeks × rate."],
  ["Timeline", "≈32 weeks: Plan 4 · Build 10 · Pilot 6 · Deploy 12. Waves roll out easy datasets and teams first, building the reusable agentic backbone."],
  ["Tokens modeled explicitly", "~$300K/yr in production (200 DS × ~$6.50/day blended × 230 days) plus $30K pre-production, inside the $280K platform line. The pilot measures real cost per workflow."],
  ["Change management is funded", "$120K one-time, because unmanaged adoption benchmarks at 20–40% — the single biggest driver of the capture haircut."],
  ["No double counting", "This build targets the data-prep pool only; adjacent capabilities added during deploy (documentation, feature prep) are credited to the wave-2 cases, not this one."],
];

function assumptionCol(x, title, color, bg, items) {
  s2.addShape("roundRect", { x, y: 1.16, w: 6.0, h: 5.9, rectRadius: 0.06, fill: { color: bg } });
  T(s2, title, { x: x + 0.26, y: 1.34, w: 5.48, h: 0.24, fontSize: 11, bold: true, color, charSpacing: 1.5 });
  let y = 1.76;
  items.forEach(it => {
    T(s2, it[0], { x: x + 0.26, y, w: 5.48, h: 0.22, fontSize: 10, bold: true, color });
    T(s2, it[1], { x: x + 0.26, y: y + 0.22, w: 5.48, h: 0.56, fontSize: 9, color: INK, valign: "top" });
    y += 0.87;
  });
}
assumptionCol(0.55, "BENEFIT SIDE", TEAL_DK, TEAL_BG, LHS_A);
assumptionCol(6.83, "INVESTMENT SIDE", INDIGO_DK, INDIGO_BG, RHS_A);

s2.addShape("line", { x: 0.55, y: 7.20, w: 12.3, h: 0, line: { color: LINE, width: 0.75 } });
T(s2, "All figures illustrative. The model is most sensitive to the baseline (headcount × loaded cost × time allocation) — validate that with Finance before the automation percentages.", { x: 0.55, y: 7.26, w: 12.3, h: 0.22, fontSize: 8, color: FAINT });

pres.writeFile({ fileName: "ds-sizing-example.pptx" }).then(() => console.log("written"));
