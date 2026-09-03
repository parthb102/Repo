/* eslint-disable */
// Generator for "AI & Automation big bets" discussion document (Enrique / Jaime, Friday; ELT, Tuesday).
// Run: node build.js  -> Enrique_AI_Automation_Big_Bets.pptx
const pptxgen = require('pptxgenjs');
const path = require('path');

const OUT = process.argv[2] || path.join(__dirname, 'Enrique_AI_Automation_Big_Bets.pptx');

// ---------- palette (client template not received; neutral consulting palette) ----------
const C = {
  navy: '051C2C',      // dominant text / dark fills
  blue: '2251FF',      // accent
  blueLt: 'E8EEFF',    // light accent fill
  ink: '1F2937',       // body text
  grey: '6B7280',      // muted text
  greyLt: 'F2F4F7',    // card fill
  greyMid: 'D1D5DB',   // lines
  white: 'FFFFFF',
  green: '1E9E5A',
  amber: 'E3A008',
  red: 'D0342C',
};
const FONT = 'Arial';

const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE'; // 13.333 x 7.5 in
pres.author = 'Enterprise Transformation Office';
pres.title = 'AI & Automation big bets - discussion document';

const W = 13.333, H = 7.5, ML = 0.55, MR = 0.55, CW = W - ML - MR; // content width 12.23
let pageNo = 0;

// ---------- helpers ----------
function txt(slide, text, o) {
  slide.addText(text, Object.assign({ fontFace: FONT, color: C.ink, isTextBox: true, margin: 0, valign: 'top' }, o));
}
function rect(slide, x, y, w, h, o) {
  slide.addShape(pres.ShapeType.rect, Object.assign({ x, y, w, h, line: { color: C.greyMid, width: 0 } }, o));
}
function rrect(slide, x, y, w, h, o) {
  slide.addShape(pres.ShapeType.roundRect, Object.assign({ x, y, w, h, rectRadius: 0.08, line: { color: C.greyMid, width: 0 } }, o));
}
function oval(slide, x, y, w, h, o) {
  slide.addShape(pres.ShapeType.ellipse, Object.assign({ x, y, w, h, line: { color: C.greyMid, width: 0 } }, o));
}
function hline(slide, x, y, w, o) {
  slide.addShape(pres.ShapeType.line, Object.assign({ x, y, w, h: 0, line: { color: C.greyMid, width: 0.75 } }, o));
}
function numCircle(slide, x, y, n, d = 0.36, fill = C.navy) {
  oval(slide, x, y, d, d, { fill: { color: fill } });
  txt(slide, String(n), { x, y, w: d, h: d, align: 'center', valign: 'middle', color: C.white, bold: true, fontSize: 11 });
}
function ryg(slide, x, y, status, d = 0.2) {
  const col = status === 'G' ? C.green : status === 'A' ? C.amber : status === 'R' ? C.red : C.greyMid;
  oval(slide, x, y, d, d, { fill: { color: col } });
}
function base(slide, { section, title, subtitle, source, notes, prelim = true }) {
  pageNo += 1;
  // tracker + stamp
  txt(slide, section.toUpperCase(), { x: ML, y: 0.22, w: 7, h: 0.22, fontSize: 9, color: C.grey, charSpacing: 1 });
  if (prelim) txt(slide, 'PRELIMINARY - WORKING DRAFT FOR DISCUSSION', { x: W - MR - 5, y: 0.22, w: 5, h: 0.22, fontSize: 8, color: C.grey, align: 'right', charSpacing: 1 });
  // action title
  txt(slide, title, { x: ML, y: 0.5, w: CW, h: 0.95, fontSize: 21, bold: true, color: C.navy, valign: 'top', lineSpacingMultiple: 1.0 });
  if (subtitle) txt(slide, subtitle, { x: ML, y: 1.42, w: CW, h: 0.3, fontSize: 11, color: C.grey });
  // footer
  hline(slide, ML, H - 0.5, CW);
  txt(slide, source ? 'Source: ' + source : '', { x: ML, y: H - 0.44, w: 9.5, h: 0.3, fontSize: 8, color: C.grey });
  txt(slide, 'Enterprise Transformation Office | AI & Automation', { x: W - MR - 4.4, y: H - 0.44, w: 3.8, h: 0.3, fontSize: 8, color: C.grey, align: 'right' });
  txt(slide, String(pageNo), { x: W - MR - 0.5, y: H - 0.44, w: 0.5, h: 0.3, fontSize: 8, color: C.grey, align: 'right' });
  if (notes) slide.addNotes(notes);
}
function bullets(slide, items, o) {
  const arr = items.map((t, i) => {
    const isObj = typeof t === 'object';
    const s = isObj ? t.text : t;
    const opts = { bullet: isObj && t.sub ? { indent: 14 } : { indent: 12 }, breakLine: i < items.length - 1, paraSpaceAfter: 4 };
    if (isObj && t.sub) { opts.indentLevel = 1; opts.fontSize = (o.fontSize || 11) - 1; opts.color = '4B5563'; }
    if (isObj && t.bold) opts.bold = true;
    return { text: s, options: opts };
  });
  txt(slide, arr, Object.assign({ fontSize: 11, color: C.ink, valign: 'top' }, o));
}
function label(slide, text, x, y, w, o) {
  txt(slide, text, Object.assign({ x, y, w, h: 0.3, fontSize: 11, bold: true, color: C.navy }, o));
}
function card(slide, x, y, w, h, { head, body, fill = C.greyLt, headColor = C.navy, fontSize = 10.5, n, headH = 0.52, headSize = 11.5 }) {
  rrect(slide, x, y, w, h, { fill: { color: fill } });
  let ty = y + 0.14;
  if (n !== undefined) { numCircle(slide, x + 0.15, y + 0.15, n, 0.32); }
  if (head) { txt(slide, head, { x: x + (n !== undefined ? 0.58 : 0.18), y: ty, w: w - (n !== undefined ? 0.75 : 0.36), h: headH - 0.02, fontSize: headSize, bold: true, color: headColor, valign: 'top' }); ty += headH; }
  if (body) {
    if (Array.isArray(body)) bullets(slide, body, { x: x + 0.18, y: ty, w: w - 0.36, h: h - (ty - y) - 0.1, fontSize });
    else txt(slide, body, { x: x + 0.18, y: ty, w: w - 0.36, h: h - (ty - y) - 0.1, fontSize });
  }
}
function tableStyle(extra) {
  return Object.assign({
    fontFace: FONT, fontSize: 9.5, color: C.ink, valign: 'top', margin: [4, 6, 4, 6],
    border: [{ type: 'none' }, { type: 'none' }, { type: 'solid', pt: 0.5, color: C.greyMid }, { type: 'none' }],
    autoPage: false,
  }, extra);
}
function th(text, o) { return { text, options: Object.assign({ bold: true, color: C.white, fill: { color: C.navy }, fontSize: 9.5, valign: 'middle' }, o) }; }
function td(text, o) { return { text, options: Object.assign({}, o) }; }
function tdb(text, o) { return { text, options: Object.assign({ bold: true, color: C.navy }, o) }; }
function stampBox(slide, x, y, w, h, text) {
  rrect(slide, x, y, w, h, { fill: { color: C.blueLt } });
  txt(slide, text, { x: x + 0.15, y: y + 0.1, w: w - 0.3, h: h - 0.2, fontSize: 10, color: C.navy, valign: 'middle' });
}

// =====================================================================================
// 1. TITLE
// =====================================================================================
{
  const s = pres.addSlide();
  rect(s, 0, 0, W, H, { fill: { color: C.navy }, line: { color: C.navy, width: 0 } });
  txt(s, 'AI & Automation big bets', { x: 0.8, y: 1.6, w: 11, h: 0.6, fontSize: 18, color: 'A9C1FF', charSpacing: 2 });
  txt(s, 'Where we are, how we are resourcing the work, and how we propose to sequence and fund it', { x: 0.8, y: 2.2, w: 11.5, h: 1.8, fontSize: 34, bold: true, color: C.white, valign: 'top' });
  txt(s, 'Discussion document for Enrique and Jaime | Friday, September 4, 2026\nAlso serves the ELT session on Tuesday, September 8 (pipeline tracking, POC progress, CEO/CFO follow-ups, sequencing approach)', { x: 0.8, y: 4.45, w: 11.5, h: 0.9, fontSize: 13, color: 'CADCFC' });
  txt(s, 'Enterprise Transformation Office  |  Presented by Anshu', { x: 0.8, y: 6.3, w: 8, h: 0.4, fontSize: 12, color: C.white });
  txt(s, 'PRELIMINARY - WORKING DRAFT. Figures are pre-S2 submission and have not yet been reviewed with Finance or sponsors; numeric detail is held in speaker notes only.', { x: 0.8, y: 6.7, w: 11.5, h: 0.5, fontSize: 10, color: 'B8C4D6' });
  s.addNotes('Cover. This deck is a shell-plus: every page has an action title and page content in Anshu\'s voice; numeric detail that has not yet been seen by Jaime or sponsors is confined to the speaker notes. Review with Anshu on Sep 3 (first half of day), iterate to end of day, send V1 to Anshu with a one-line note on what will be populated. Srini\'s technology resourcing framework page to be inserted by Anshu/Srini.');
  pageNo += 1;
}

// =====================================================================================
// 2. OBJECTIVES FOR TODAY
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Objectives for today',
    title: 'Today is a level-set ahead of S2 pencils-down: orient you on where the pipeline stands and what delivery will take, so nothing next week is a surprise',
    source: 'ETO working team; agenda items requested for the Friday session (tech resourcing capacity, cost and investment, sequencing and prioritization, accounting treatment)',
    notes: [
      'TALK TRACK (Anshu):',
      '- Frame: we are mid-S2. Numbers are being refined with SMEs, tech POCs and Finance this week; Finance review is scheduled and Jaime pressure-tests business cases next week. Today is deliberately about shape, magnitude and method, not dollars.',
      '- Plant the seed: based on what I am seeing across the pipeline, delivery will need dedicated resourcing and incremental funding at a magnitude of tens of millions, not single-digit millions. I will bring sized numbers next week after the Finance review.',
      '- Why no dollars today: S2 submissions are not done, sponsors have not signed off on their S2 estimates, and Jaime has not yet seen the numbers. Sharing a figure with Enrique and Jaime before sponsors and Finance creates downstream fire drills.',
      '- Ask for breathing room: the pipeline snapshot and methodology can go to the ELT on Tuesday; initiative-level numbers should wait for S2 close and Finance alignment.',
    ].join('\n'),
  });
  // three objective cards
  const y = 1.9, h = 2.15, gap = 0.25, w = (CW - 2 * gap) / 3;
  card(s, ML, y, w, h, { n: 1, head: 'Level-set on where we are', body: ['Snapshot of the big-bet pipeline we are tracking and its S2 status', 'Where Wave 1 org changes are affecting baselines and sizing', 'What has been engaged with technology, Finance and HR so far'] });
  card(s, ML + w + gap, y, w, h, { n: 2, head: 'Share resourcing and propose sequencing', body: ['Current working model and the typical build-and-run team we are sizing against', 'Technology resourcing capacity view (Srini\'s framework, to be inserted)', 'Proposed criteria for sequencing and prioritization across levers'] });
  card(s, ML + 2 * (w + gap), y, w, h, { n: 3, head: 'Preview investment themes, not dollars', body: ['Shape and magnitude of the investment we expect to request', 'Where the savings actually come from, and what that implies', 'Accounting treatment and funding-source questions being worked with Finance'] });
  // what this is / is not
  label(s, 'What today is', ML, 4.35, 5.8);
  bullets(s, ['An orientation and a preview of the asks we expect to make after S2 closes', 'A chance to align on method (sequencing, resourcing, funding) before numbers land'], { x: ML, y: 4.67, w: 5.8, h: 1.2, fontSize: 10.5 });
  label(s, 'What today is not', ML + 6.2, 4.35, 5.8);
  bullets(s, ['A request to approve investment cases: S2 submissions close this week and are reviewed with Finance and Jaime next week', 'An initiative-level readout: numbers will come to you consolidated after sponsor and Finance alignment'], { x: ML + 6.2, y: 4.67, w: 5.8, h: 1.2, fontSize: 10.5 });
  stampBox(s, ML, 6.15, CW, 0.5, 'Next two weeks:  S2 pencils-down (this week)  >  Finance review  >  Jaime pressure-test sessions (next week)  >  ELT update (Tuesday)  >  S3 in ~2.5 weeks');
}

// =====================================================================================
// 3. EXECUTIVE SUMMARY
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Executive summary',
    title: 'Executive summary: the big-bet pipeline is converging in S2, proven use cases can move first, and delivery will need dedicated capacity and a clear funding path',
    source: 'ETO working team; sizing sessions with servicing, sales, technology, Finance and HR (Aug 13 - Sep 2)',
    notes: [
      'TALK TRACK (Anshu): keep this page to 60 seconds and move to the pages with substance.',
      'Numbers for reference only (do not read out unless asked, and caveat as pre-Finance-review):',
      '- Big-bet value profile shared with Finance/HR on Sep 2: roughly 13% of run-rate in H1 2027, 30% in H2 2027, 75% in H1 2028, 100% in H2 2028 (gross, big bets only).',
      '- Big bets currently sum to roughly $225M gross against an automation lever target of roughly $320M; the remainder comes from bottom-up initiatives already in Wave (close to $300M in total when those are included).',
      '- Investment: expect tens of millions across one-time build and recurring run cost. Helix alone is a mega-investment (order of $200M with ~200 people) and is the biggest execution-capacity question.',
      '- Seller productivity: three fast-tracked initiatives (underwriting, pricing, SMB long tail) with roughly 3.5-4x return on one-time investment on a transaction-margin basis; Susan wants to reinvest the cost-out into revenue rather than take it as headcount.',
    ].join('\n'),
  });
  const items = [
    ['Pipeline', 'We are tracking roughly 15-16 big-bet initiatives across five areas (servicing, seller productivity, SDLC, PDLC, risk and compliance). Most are in S2 sizing; the remainder of the automation lever is bottom-up initiatives already in Wave.'],
    ['Where we are', 'S1 sizing was shared with sponsors in mid-August. Since then we have run the three seller-productivity initiatives to ground with the sales working team, aligned the servicing model with ops leaders, and brought Finance and HR into the business cases. S2 pencils-down is this week; S3 is roughly 2.5 weeks out.'],
    ['Org change impacts', 'Wave 1 actions moved the ground under the sizing: baselines (servicing headcount, product and engineering ratios) are being re-cut, and several SMEs and finance partners who supported S1 are no longer here. We are re-baselining rather than carrying stale assumptions.'],
    ['Resourcing', 'Today the work is carried by a core ETO team with consulting support, workstream leads, tech POCs, Finance and HR. Delivery will need dedicated, funded build and run teams; we are sizing against a standard team archetype and phase plan and will bring Srini\'s tech capacity view.'],
    ['Sequencing', 'We propose to sequence on confidence, timing of value, investment intensity, dependencies across levers, and execution capacity, and to tier investment to confidence: proven use cases (servicing, SDLC) move left now; less proven ones (for example PDLC) get design-and-pilot funding gated on evidence.'],
    ['Investment', 'Investment will be material and front-loaded into build, with recurring run cost (inference, run teams) as the swing factor. Within servicing most savings come from contact avoidance; how seller-productivity value is taken is an open sponsor and Finance question. Sized numbers follow the Finance review next week.'],
  ];
  let y = 1.8; const rowH = 0.82;
  items.forEach(([k, v], i) => {
    numCircle(s, ML, y + 0.04, i + 1, 0.34);
    txt(s, k, { x: ML + 0.5, y, w: 1.9, h: rowH - 0.1, fontSize: 11.5, bold: true, color: C.navy });
    txt(s, v, { x: ML + 2.45, y, w: CW - 2.45, h: rowH - 0.1, fontSize: 10.5 });
    if (i < items.length - 1) hline(s, ML + 0.5, y + rowH - 0.06, CW - 0.5, { line: { color: C.greyLt, width: 0.75 } });
    y += rowH;
  });
}

// =====================================================================================
// 4. WHERE WE ARE: STAGE GATES
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Where we are',
    title: 'We are mid-way through S2 with S3 roughly 2.5 weeks out; each gate raises confidence from theoretical sizing to piloted evidence, so estimates will keep moving until S4',
    source: 'ETO stage-gate process; working-team calendar as of Sep 2',
    notes: [
      'TALK TRACK (Anshu):',
      '- Level-set for Enrique and Jaime, who cannot track this level of detail week to week: S1 sizing was shared with sponsors in mid-August; we are in the middle of S2; S3 comes in roughly 2.5 weeks; S4 is where POCs and pilots teach us real implementation timelines.',
      '- Every automation initiative is iterative by design: S3 gives the best theoretical understanding, S4 pilots reveal timelines, and S5 sizing reflects that. Numbers may be better or worse than assumed; that is what the process is for.',
      '- Engagement so far: sizing sessions with servicing ops leaders (Sep 2), sales working team (sponsor review Sep 3), PDLC and checkout teams, tech POCs on build phases and roles, Finance (Tom) on business-case input and the value profile, HR (John, Alex) on milestones and headcount counting. Controllership has NOT yet been consulted: FP&A flagged that a sit-down is needed on capitalization rules; do not imply a ruling exists.',
      '- Note: "tech POCs" here means technology points of contact; "POC" on the ELT agenda means proofs of concept. Keep the two apart when speaking.',
    ].join('\n'),
  });
  // stage-gate chevrons
  const gates = [
    ['S1', 'Initial sizing', 'Mid-August readouts to sponsors: initiative long-list with preliminary revenue, cost and investment', 'done'],
    ['S2', 'Refined cases', 'SME interviews and data; tech POC input on build phases; Finance review; pencils-down this week', 'now'],
    ['S3', 'Holistic plan', 'Full business cases stacked across levers without double counting; sequencing and resourcing plan', 'next'],
    ['S4', 'Pilot and POC', 'Proofs of concept and pilots reveal implementation timelines and adoption; org-design stage gates', 'later'],
    ['S5', 'Scale and commit', 'Sizing updated on pilot evidence; scale funding released against confidence', 'later'],
  ];
  const gy = 1.95, gh = 0.6, gw = CW / 5 - 0.08;
  gates.forEach((g, i) => {
    const x = ML + i * (gw + 0.1);
    const fill = g[3] === 'done' ? C.navy : g[3] === 'now' ? C.blue : C.greyMid;
    s.addShape(pres.ShapeType.chevron, { x, y: gy, w: gw, h: gh, fill: { color: fill }, line: { color: fill, width: 0 } });
    txt(s, g[0] + '  ' + g[1], { x: x + 0.35, y: gy, w: gw - 0.6, h: gh, fontSize: 11, bold: true, color: (g[3] === 'later' || g[3] === 'next') ? C.navy : C.white, valign: 'middle' });
    txt(s, g[2], { x: x + 0.05, y: gy + gh + 0.12, w: gw - 0.1, h: 1.1, fontSize: 9.5, color: C.ink });
  });
  txt(s, 'YOU ARE HERE', { x: ML + (gw + 0.1) * 1 + 0.2, y: gy - 0.3, w: 2, h: 0.25, fontSize: 8, bold: true, color: C.blue, charSpacing: 1 });
  // engagement strip
  label(s, 'Who has been engaged in the sizing so far, and who is still to be engaged', ML, 3.85, 9);
  const eng = [
    ['Workstream leads and sponsors', 'Servicing ops leaders, sales working team (sponsor review Sep 3), PDLC and checkout teams, risk leads'],
    ['Technology points of contact', 'Roles per build, phase durations, parallelization, early view of which roles could be capitalized'],
    ['Finance (Tom and team)', 'Input into the S2 cases; challenge of the value profile by quarter; Jaime pressure-test sessions next week'],
    ['HR (John, Alex)', 'Milestones, counting of people and partial capacity, org-design implications after Wave 1'],
    ['Controllership (to engage)', 'Sit-down still to be scheduled on capitalization by job family and build type and on amortization'],
  ];
  const ew = (CW - 4 * 0.18) / 5;
  eng.forEach((e, i) => {
    const x = ML + i * (ew + 0.18);
    card(s, x, 4.2, ew, 1.75, { head: e[0], body: e[1], fontSize: 9.5, fill: i === 4 ? C.white : C.greyLt, headH: 0.5 });
    if (i === 4) rrect(s, x, 4.2, ew, 1.75, { fill: { color: C.white, transparency: 100 }, line: { color: C.greyMid, width: 1, dashType: 'dash' } });
  });
  stampBox(s, ML, 6.25, CW, 0.5, 'Implication: numbers shown between now and S4 are directional by design. We re-baseline at each gate on the organization we actually have after Wave 1, rather than freezing early estimates.');
}

// =====================================================================================
// 5. PIPELINE SNAPSHOT
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Pipeline snapshot',
    title: 'We are tracking roughly 15-16 big-bet initiatives across five areas; most are in S2 sizing, and the profile is weighted to proven use cases in servicing and SDLC',
    subtitle: 'Status is the ETO read as of Sep 2, to be confirmed with sponsors before the ELT session; counts to be confirmed from the Wave export; initiative-level investment is intentionally not shown',
    source: 'Wave pipeline; ETO working-team sessions Aug 13 - Sep 2',
    notes: [
      'TALK TRACK (Anshu): this is a snapshot of what is in the system, in my own words. Counts are approximate: roughly 15-16 big-bet initiatives (confirm from the Wave export); the rest of the automation lever is bottom-up initiatives already in Wave (for example the sales integration cost-out, which is direct savings but not a big bet).',
      'OFF-PAGE: seller productivity - Susan wants to reinvest the net benefit into revenue rather than take headcount; Finance wants the cost-out component tight. Do not present either position as settled before the Sep 3 sponsor review.',
      'Colour rationale (do not put on page):',
      '- Servicing GREEN: contact avoidance, enhanced chat/self-service, agentic voice, skill-based routing and workforce management aligned with ops leaders on Sep 2; copilot handle-time benefit folded back into the avoidance line at the ops leaders\' request; open headroom at top of funnel (help center, self-resolve) noted for S3, not sized.',
      '- Seller productivity GREEN/AMBER: underwriting, pricing, SMB long tail refined to higher confidence with the sales working team; SMB long-tail attach and contra not yet sized pending SME interviews; Finance review pending; Susan wants the cost-out reinvested into revenue.',
      '- SDLC AMBER: proven use case with a large share of big-bet value, but recurring inference (token) cost is the highest of any initiative and can erode gross savings; efficiency work with Puja under way.',
      '- PDLC AMBER: managed centrally as one parent big bet with BU children; checkout zeroed its placeholder dollar value until McKinsey validation on new baselines; role-ratio actions change the PM population baseline; value ramps late (design and pilots first).',
      '- Risk and compliance AMBER: collections already submitted for S2; financial-crimes cases straightforward; AML small; compliance itself is no longer an item in this lever. OFF-PAGE, not yet seen by Jaime: Helix is a mega-investment (order of $200M, ~200 people, from the Finance/HR session) with execution-capacity doubts; contract-worker lever tracked separately.',
    ].join('\n'),
  });
  const rows = [
    [th('Big-bet area'), th('# (approx.)'), th('What it covers'), th('S2 status'), th('Status', { align: 'center' }), th('ETO commentary')],
    [tdb('Servicing'), td('5-6'), td('Contact avoidance; enhanced chat and self-service; agentic voice; skill-based routing; workforce management; non-FTE costs'), td('Sizing aligned with ops leaders Sep 2; submission tracking to Friday'), td(''), td('Best-understood, well-trodden use cases; savings dominated by contact avoidance. Top-of-funnel headroom flagged for S3')],
    [tdb('Seller productivity'), td('3 fast-tracked'), td('Underwriting, pricing, SMB long tail (plus sales integration cost-out running as a bottom-up initiative)'), td('Pressure-tested with sales working team; sponsor (Susan) review Sep 3; Finance review pending'), td(''), td('Cost-out versus reinvestment treatment is an open sponsor and Finance question; two components not yet sized pending SME input')],
    [tdb('SDLC'), td('1 (confirm)'), td('AI-assisted software development lifecycle across engineering'), td('In S2 sizing with tech POCs'), td(''), td('Well-trodden, high-value use case; recurring inference cost is the swing factor and efficiency work is under way')],
    [tdb('PDLC'), td('1 parent + BU children'), td('Standardized product-development lifecycle with AI tooling for product, design and adjacent roles'), td('Baseline being re-cut post Wave 1 and role-ratio actions; BU placeholders zeroed pending validation'), td(''), td('Centrally managed to avoid double counting; value ramps late (design and pilots first)')],
    [tdb('Risk and compliance'), td('3-4'), td('Financial crimes, collections, Helix platform, AML (small)'), td('Collections submitted for S2; financial-crimes cases in Finance review; Helix case on its own track'), td(''), td('Smaller cases are straightforward; the Helix case needs its execution plan reviewed before it is sequenced with the rest')],
  ];
  s.addTable(rows, tableStyle({ x: ML, y: 1.85, w: CW, colW: [1.55, 1.15, 3.2, 2.55, 0.55, 3.23], rowH: [0.34, 0.75, 0.75, 0.75, 0.75, 0.75] }));
  // RYG dots (positions align to rows)
  const dotX = ML + 1.55 + 1.15 + 3.2 + 2.55 + 0.18;
  const statuses = ['G', 'G', 'A', 'A', 'A'];
  statuses.forEach((st, i) => ryg(s, dotX, 1.85 + 0.34 + i * 0.75 + 0.26, st, 0.2));
  // legend + bottom note
  const ly = 6.45;
  ryg(s, ML, ly + 0.05, 'G', 0.16); txt(s, 'On track for S2', { x: ML + 0.22, y: ly, w: 1.6, h: 0.25, fontSize: 9, color: C.grey });
  ryg(s, ML + 1.9, ly + 0.05, 'A', 0.16); txt(s, 'Open dependency or validation before S3', { x: ML + 2.12, y: ly, w: 3, h: 0.25, fontSize: 9, color: C.grey });
  ryg(s, ML + 5.2, ly + 0.05, 'R', 0.16); txt(s, 'At risk (none today)', { x: ML + 5.42, y: ly, w: 2, h: 0.25, fontSize: 9, color: C.grey });
  txt(s, 'Bottom-up automation initiatives outside the big bets continue through the standard S2 process in Wave and are not shown here.', { x: ML + 7.4, y: ly, w: CW - 7.4, h: 0.4, fontSize: 9, color: C.grey, italic: true });
}

// =====================================================================================
// 6. ORG CHANGE IMPACTS (talk track)
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Org change impacts',
    title: 'Wave 1 org actions changed the ground under the sizing: baselines and the people who built them have moved, so we are re-baselining rather than carrying stale assumptions',
    source: 'ETO working team; PDLC and servicing sizing sessions Sep 2; HR discussion on org-design ripple effects',
    notes: [
      'TALK TRACK (Anshu): this page is a talk track more than a readout; it is important to say it out loud rather than leave it implicit.',
      '- The layoffs are having an impact right now. People we worked with on S1 sizing, including finance partners, are no longer here. That costs us time and continuity. (Do not name individuals; do not claim sponsor changes unless you can name one.)',
      '- Servicing: roughly 900 agents moved to contractors at the start of the year; the automation model now starts from a post-Wave-1 baseline (roughly 46M contacts today, of which avoidance takes a large share out of the human queue). Once contacts leave the system, the supervisory and management structure has to be cleaned up too, as we did in Wave 1.',
      '- PDLC: role-ratio actions (engineer to PM to design) change the PM population that PDLC automation acts on; we are re-cutting the baseline and treating PDLC as one parent initiative with BU children so nothing is counted twice against Frank\'s target.',
      '- Other levers: we intend to apply the same one-number-per-lever principle (parent/child in Wave was agreed for PDLC; extend it where overlaps exist).',
    ].join('\n'),
  });
  const cols = [
    ['What changed', ['Wave 1 org actions executed (servicing agents moved to contractors; layoffs across functions)', 'Role-ratio actions under way for product, engineering and design', 'Several SMEs and finance partners who supported S1 sizing have left', 'Baselines that S1 sizing used no longer describe the organization']],
    ['What it means for sizing', ['Denominators moved: contact volumes, agent headcount and PM populations must be re-cut before applying automation assumptions', 'Higher double-count risk between automation and other levers (role ratios, contract-worker lever, follow-on org actions)', 'Continuity gap: new SMEs need to re-validate assumptions, which slows S2 in places', 'Each removal of work creates a ripple into supervisory and management structures that also needs to be planned']],
    ['How we are handling it', ['Re-baseline at each gate on the current organization, not the S1 snapshot', 'Parent/child initiative structure in Wave so each lever\'s value is counted once (PDLC as the model)', 'Placeholders zeroed until validated; no number goes into Wave that a sponsor cannot execute against', 'Org-design stage gates with HR to re-adjust structures as automation removes work', 'Dedicated delivery capacity rather than side-of-desk effort from teams that just absorbed cuts']],
  ];
  const gap = 0.22, w = (CW - 2 * gap) / 3;
  cols.forEach((c, i) => {
    const x = ML + i * (w + gap);
    rrect(s, x, 1.85, w, 0.5, { fill: { color: i === 2 ? C.blue : C.navy } });
    txt(s, c[0], { x: x + 0.18, y: 1.85, w: w - 0.36, h: 0.5, fontSize: 12, bold: true, color: C.white, valign: 'middle' });
    rrect(s, x, 2.42, w, 2.2, { fill: { color: C.greyLt } });
    bullets(s, c[1], { x: x + 0.18, y: 2.54, w: w - 0.36, h: 2.05, fontSize: 10 });
    if (i < 2) { s.addShape(pres.ShapeType.chevron, { x: x + w + 0.03, y: 1.97, w: gap - 0.06, h: 0.26, fill: { color: C.greyMid }, line: { color: C.greyMid, width: 0 } }); }
  });
  label(s, 'Where we see it today', ML, 4.72, 6);
  const ex = [
    ['Servicing', 'Agents moved to contractors at the start of the year; the automation model now starts from the post-Wave-1 contact and headcount baseline, and removing contacts ripples into the supervisory structure'],
    ['Product and engineering', 'Role-ratio actions change the population that PDLC automation acts on; PDLC is re-baselined and run as one parent initiative with BU children so nothing is counted twice'],
    ['SMEs and finance partners', 'Several SMEs and finance partners who supported S1 sizing have left; we are re-sourcing SME and finance input where people have gone, which slows S2 validation in places'],
  ];
  ex.forEach((e, i) => card(s, ML + i * (w + gap), 5.02, w, 1.3, { head: e[0], body: e[1], fontSize: 9.5, fill: C.greyLt, headH: 0.38, headSize: 11 }));
  stampBox(s, ML, 6.42, CW, 0.32, 'Ask: acknowledge that S2 numbers reflect a moving organization, and that some re-validation time is the cost of not double counting.');
}

// =====================================================================================
// 7. HOW WE ARE RESOURCING
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'How we are resourcing',
    title: 'Today a core ETO team carries the work with technology, Finance and HR; delivery will need dedicated, funded build and run teams sized to a typical team model',
    subtitle: 'Placeholder: Srini\'s technology resourcing framework (already shared with Jaime) to be inserted as the following page once obtained',
    source: 'ETO working team; cost-sizing approach aligned with technology POCs',
    notes: [
      'TALK TRACK (Anshu):',
      '- How we are resourced today: ETO core with McKinsey support; workstream leads own their business cases; tech POCs give us roles per build and phase durations; Finance and HR are now in the room for the S2 cases.',
      '- What delivery will need: for each initiative a build team (product management, engineering, QA, DevOps, UX) through plan and design, build and test, pilot, and scale, and then a run team (typically an engineer plus an operations owner) plus inference and platform costs. Each team has sized 2-5 people per role; that is being refined now, so speak in ranges, not totals.',
      '- Capacity reality: teams that just absorbed Wave 1 cuts cannot deliver this from the side of their desk. I will be asking for dedicated resourcing and incremental funding. OFF-PAGE magnitude, verbal only: tens of millions, not single-digit millions, across the portfolio (never by initiative).',
      '- Tech capacity: Srini has a framework on technology resourcing and prioritization that has already gone to Jaime (the transcript garbles its name); that is the next page once we have it from Srini. Promise only what is in hand by the Sep 3 review.',
      '- OFF-PAGE, not yet seen by Jaime, only if asked: one platform case (Helix) is the outlier at roughly 200 people and of the order of $200M requested (figures from the Finance/HR session, not reconciled); they have barely spent this year, so execution capacity rather than intent is the constraint.',
      '- OFF-PAGE: capitalization by role (engineering typically yes, product management no) is an early view from FP&A and the tech POCs, pending Controllership.',
    ].join('\n'),
  });
  // left: current model
  label(s, 'How the work is resourced today', ML, 1.85, 5.6);
  const lx = ML, ly = 2.2, lw = 5.6;
  const rings = [
    ['ETO core team', 'Program management, pipeline tracking in Wave, sponsor and ELT cadence; McKinsey support on sizing, models and business cases', C.navy, C.white],
    ['Workstream leads and sponsors', 'Own the business cases; provide SMEs, data and sign-off at each gate', C.blue, C.white],
    ['Technology points of contact', 'Roles per build, phase durations, parallelization, early view of which roles could be capitalized', C.blueLt, C.navy],
    ['Finance, HR, Controllership', 'Business-case review, headcount counting, accounting treatment', C.greyLt, C.navy],
  ];
  rings.forEach((r, i) => {
    const y = ly + i * 1.05;
    rrect(s, lx, y, lw, 0.95, { fill: { color: r[2] } });
    txt(s, r[0], { x: lx + 0.18, y: y + 0.1, w: lw - 0.36, h: 0.3, fontSize: 11, bold: true, color: r[3] });
    txt(s, r[1], { x: lx + 0.18, y: y + 0.4, w: lw - 0.36, h: 0.5, fontSize: 9.5, color: r[3] });
  });
  // right: delivery archetype
  const rx = ML + 6.1, rw = CW - 6.1;
  label(s, 'What delivery will need: a typical build-and-run team per initiative', rx, 1.85, rw);
  const phases = ['Plan & design', 'Build & test', 'Pilot', 'Scale', 'Run'];
  const pw = (rw - 4 * 0.06) / 5;
  phases.forEach((p, i) => {
    const x = rx + i * (pw + 0.06);
    const fill = i === 4 ? C.blue : C.navy;
    s.addShape(pres.ShapeType.chevron, { x, y: 2.25, w: pw, h: 0.5, fill: { color: fill }, line: { color: fill, width: 0 } });
    txt(s, p, { x: x + 0.28, y: 2.25, w: pw - 0.48, h: 0.5, fontSize: 8.5, bold: true, color: C.white, valign: 'middle', align: 'center' });
  });
  card(s, rx, 2.95, rw / 2 - 0.08, 2.0, { head: 'Build team (one-time)', body: ['Product management, engineering, QA, DevOps, UX at a blended cost per person', 'Teams and duration set per phase with tech POCs; some phases run in parallel', 'Which roles can be capitalized is being worked with Finance and Controllership'], fontSize: 9.5, headH: 0.4 });
  card(s, rx + rw / 2 + 0.08, 2.95, rw / 2 - 0.08, 2.0, { head: 'Run team and platform (recurring)', body: ['Typically one engineer plus one operations owner per initiative', 'Inference and token usage sized by use-case complexity against external benchmarks', 'Platform and vendor contracts (for example telephony minimums) do not flex with volume'], fontSize: 9.5, headH: 0.4 });
  card(s, rx, 5.1, rw, 1.6, { head: 'What we expect to ask for', body: ['Dedicated build capacity per big bet, funded rather than side-of-desk, starting with the well-trodden use cases', 'An agreed run model (engineer plus operations owner) for each initiative before scale', 'A technology capacity view (Srini) that shows what can start in Q4 2026 versus H1 2027'], fontSize: 9.5, fill: C.blueLt, headH: 0.4 });
}

// =====================================================================================
// 8. SEQUENCING CRITERIA
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Proposed sequencing methodology',
    title: 'We propose to sequence on five criteria and to tier investment to confidence: proven use cases move first, unproven ones earn scale funding through pilots',
    source: 'ETO working team',
    notes: [
      'TALK TRACK (Anshu): confirm you are comfortable owning these criteria in the Sep 3 review before presenting them as your method.',
      '- We do not need to settle sequencing to the dollar today; we need agreement on the criteria we will apply when S2 cases come in, so that S3 produces one holistic plan rather than 15 competing asks.',
      '- Confidence: servicing and SDLC are well-trodden use cases where everyone doing AI successfully is gaining value; PDLC and the largest platform case are the less proven ones. Investment should follow confidence: invest fast where we know what we can do, fund design-and-pilot only where we do not.',
      '- Timing: the committed profile needs value in H1 2027; the bottom-up ramp is slower (OFF-PAGE: roughly 13% of run-rate in H1 2027 rising to 100% by H2 2028; Finance will pressure-test it next week). That is why we are looking at shifting proven initiatives left.',
      '- Dependencies: one number per lever; PDLC parent/child; role ratios and contract-worker lever counted once.',
      '- Fail fast: stage gates need explicit kill criteria. Only if you are comfortable: the Finance/HR session noted we have been slow to pull the plug in the past; PayPal World was cited as the example.',
    ].join('\n'),
  });
  const rows = [
    [th('Criterion'), th('What we assess'), th('Evidence we use at S2/S3'), th('How it drives sequencing')],
    [tdb('1  Confidence in the use case'), td('Is this a proven pattern at scale elsewhere, or a hypothesis for us?'), td('External reference cases; tech POC view of integration effort; pilot results (S4)'), td('Proven: build now. Unproven: fund design and pilot only, scale on evidence')],
    [tdb('2  Timing of value'), td('When does run-rate value land against the committed profile, especially H1 2027?'), td('Value-realization profile by quarter agreed with workstreams; pressure-tested with Finance next week'), td('Pull left initiatives that can land in H1 2027; compress build durations where tech POCs agree')],
    [tdb('3  Investment intensity and treatment'), td('One-time build versus recurring run cost; capex versus opex; central pool versus BU'), td('Cost sizing by phase and role; token cost by complexity; controllership rules'), td('Tier investment to confidence; watch initiatives whose recurring cost erodes gross savings')],
    [tdb('4  Dependencies and double counting'), td('Overlap with role ratios, contract-worker lever, Wave 1 actions and other big bets'), td('Parent/child structure in Wave; common baselines per gate'), td('One number per lever; sequence enablers (for example PDLC) after the actions they depend on')],
    [tdb('5  Execution capacity'), td('Can the team actually build and absorb this given post-Wave-1 capacity?'), td('Tech capacity view (Srini); spend to date versus spend requested'), td('Do not fund beyond demonstrated ability to spend; add kill criteria at each gate')],
  ];
  s.addTable(rows, tableStyle({ x: ML, y: 1.75, w: CW, colW: [2.5, 3.1, 3.3, 3.33], rowH: [0.34, 0.64, 0.64, 0.64, 0.64, 0.64] }));
  // principles strip
  const py = 5.45, pw = (CW - 3 * 0.18) / 4;
  const principles = [
    ['Tiered investment', 'Release funding in tranches tied to confidence and gate evidence, not to the full business case up front'],
    ['One holistic plan', 'Stack S2 cases across all levers into a single implementation plan at S3 with no double counting'],
    ['Triangulate, then choose', 'The investment pool is finite: weigh financial commitments, customer (NPS) goals and available dollars together'],
    ['Fail fast', 'Explicit continue, pivot or stop criteria at each gate, so a bet that will not deliver is stopped early and its funding redirected'],
  ];
  principles.forEach((p, i) => card(s, ML + i * (pw + 0.18), py, pw, 1.3, { head: p[0], body: p[1], fontSize: 9.5, fill: C.blueLt, headH: 0.4, headSize: 11 }));
}

// =====================================================================================
// 9. SEQUENCING APPLIED (ILLUSTRATIVE)
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Proposed sequencing methodology',
    title: 'Applied to today\'s pipeline, the criteria point to three horizons: push proven use cases left now, pilot the rest through H1 2027, and gate scale on evidence',
    subtitle: 'Illustrative placement by the ETO working team as of Sep 2, for discussion; to be confirmed with sponsors and at S3 once business cases are stacked across levers',
    source: 'ETO working team; sizing sessions with servicing, sales, technology and PDLC teams',
    notes: [
      'TALK TRACK (Anshu): this is directional. It shows how the criteria sort today\'s pipeline; the S3 plan will confirm it.',
      '- Accelerate: servicing (contact avoidance, chat, agentic voice) and SDLC are proven; we are working with Matt on an aggressive scenario for agentic voice and with tech POCs on compressing build durations. Build spend for all initiatives is currently assumed to start Q4 2026; pulling it into H2 2026 is possible if treatment allows.',
      '- Validate then build: seller productivity is refined and awaiting Finance review; financial-crimes and collections cases are straightforward; skill-based routing and workforce management are aligned on cost takeout.',
      '- Design and pilot first: PDLC needs roughly four months of design plus one or two pilots, then six to eight teams across a couple of BUs, then scale; little value in the first 12 months. Helix cannot spend at the requested rate; fund to demonstrated capacity.',
      '- Kill criteria apply everywhere; the earlier we know an initiative will not deliver, the more of the pool we can redirect.',
    ].join('\n'),
  });
  const lanes = [
    ['Accelerate now', 'Well-trodden use cases, high confidence, value can land in H1 2027', C.navy, C.white, ['Servicing: contact avoidance, enhanced chat and self-service, agentic voice', 'SDLC: AI-assisted engineering'], 'Start build in Q4 2026, or earlier if accounting treatment allows; compress build durations; front-load funding'],
    ['Validate, then build', 'Cases submitted or refined; awaiting Finance review and sponsor sign-off', C.blue, C.white, ['Seller productivity: underwriting, pricing, SMB long tail', 'Servicing efficiency: skill-based routing, workforce management', 'Risk: financial crimes, collections'], 'Confirm at Finance and Jaime reviews next week; build in H1 2027 with the run model agreed'],
    ['Design and pilot first', 'Less proven for us, long ramp, or execution plan still to be reviewed', C.greyLt, C.navy, ['PDLC: standardized lifecycle and tooling, one parent initiative', 'Platform-scale cases whose execution plans are still under review (placed at S3)'], 'Fund design and pilots; scale funding gated on pilot evidence and demonstrated ability to spend'],
  ];
  const gap = 0.22, w = (CW - 2 * gap) / 3;
  lanes.forEach((l, i) => {
    const x = ML + i * (w + gap);
    rrect(s, x, 1.9, w, 0.78, { fill: { color: l[2] } });
    txt(s, l[0], { x: x + 0.18, y: 1.95, w: w - 0.36, h: 0.32, fontSize: 12.5, bold: true, color: l[3] });
    txt(s, l[1], { x: x + 0.18, y: 2.27, w: w - 0.36, h: 0.4, fontSize: 9, color: l[3] });
    rrect(s, x, 2.82, w, 1.55, { fill: { color: C.greyLt } });
    txt(s, 'Initiatives', { x: x + 0.18, y: 2.92, w: w - 0.36, h: 0.25, fontSize: 9, bold: true, color: C.grey, charSpacing: 1 });
    bullets(s, l[4], { x: x + 0.18, y: 3.19, w: w - 0.36, h: 1.15, fontSize: 10.5 });
    rrect(s, x, 4.52, w, 1.05, { fill: { color: C.blueLt } });
    txt(s, 'What we do next', { x: x + 0.18, y: 4.6, w: w - 0.36, h: 0.25, fontSize: 9, bold: true, color: C.grey, charSpacing: 1 });
    txt(s, l[5], { x: x + 0.18, y: 4.86, w: w - 0.36, h: 0.68, fontSize: 10 });
    rrect(s, x, 5.72, w, 0.5, { fill: { color: C.white }, line: { color: C.greyMid, width: 0.75 } });
    txt(s, [{ text: 'Proposed funding logic at S3: ', options: { bold: true, color: C.navy } }, { text: ['build tranche', 'build tranche after reviews', 'design and pilot tranche only'][i] }], { x: x + 0.18, y: 5.72, w: w - 0.36, h: 0.5, fontSize: 9.5, valign: 'middle' });
  });
  stampBox(s, ML, 6.35, CW, 0.4, 'Across all three horizons: one number per lever, an agreed run model before scale, and explicit continue, pivot or stop criteria at each gate.');
}

// =====================================================================================
// 10. INVESTMENT THEMES
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Investment requirements: themes and observations',
    title: 'Investment will be material and front-loaded into build, with recurring run cost as the swing factor; sized numbers follow the Finance review next week',
    subtitle: 'Observations across the portfolio; individual initiative figures are deliberately not shown until sponsors and Finance have reviewed them',
    source: 'ETO working team; cost-sizing sessions with technology POCs; Finance and HR discussion Sep 2',
    notes: [
      'TALK TRACK (Anshu): these are observations, not sanctioned numbers. If asked for figures, give ranges and caveat that Finance has not reviewed them. Everything marked OFF-PAGE has not been seen by Jaime or sponsors.',
      '- OFF-PAGE magnitude, verbal only: tens of millions across the portfolio for build plus recurring run cost; not single-digit millions. Resourcing: teams have sized roles at two to five people each across five or six roles per build; share only as an aggregate range, never by initiative.',
      '- OFF-PAGE, seller productivity (sponsor review Sep 3, Finance not aligned): one-time investment returns roughly 3.5-4x on transaction margin and 6.5x-plus on revenue; three initiatives at roughly $24M cost takeout, about $20M one-time and $4.5M recurring, roughly $20M net run-rate benefit. Susan wants to reinvest into revenue rather than take headcount; Finance wants the cost-out tight. Separate roughly $23M direct integration cost-out is not a big bet.',
      '- OFF-PAGE, servicing: 70-80% of the value is contact avoidance (taking contacts out of the human queue entirely); the rest is efficiency. Contact economics: hard contacts cost around $8, easy around $2, average around $4.7.',
      '- OFF-PAGE, SDLC: recurring token cost is the highest in the portfolio; engineering already spends heavily on tokens this year (figure garbled in the source, do not quote), so gross savings can erode quickly without efficiency work (Puja).',
      '- Helix (do not name on the page; sponsor has not pre-aligned): order of $200M one-time with roughly 200 people; barely spent this year, so Finance doubts the requested run-rate of spend can be executed.',
      '- Portfolio (approximate, pre-Finance review): big bets roughly $225M gross against an automation target of roughly $320M; close to $300M once bottom-up initiatives in Wave are included. The sub-splits of the target in the transcript are garbled; do not quote them. The value profile today is gross and excludes one-time and recurring cost.',
    ].join('\n'),
  });
  const obs = [
    ['Magnitude', 'The ask will be material and multi-year: one-time build across roughly 15-16 initiatives plus recurring run cost. We will bring ranges next week, not point estimates.'],
    ['Shape of the cost', 'One-time cost is people by phase (plan and design, build and test, pilot, scale). Recurring cost is run teams plus inference; for SDLC recurring inference is the largest line and can erode gross savings.'],
    ['Where the value comes from', 'Within servicing, value is dominated by contact avoidance rather than agent efficiency. How seller-productivity value is taken, cost-out versus reinvestment into revenue, is an open question with the sponsor and Finance.'],
    ['Accounting treatment', 'Capitalization is decided at role level and by build type (from-scratch internal builds versus enhancements to vendor products). Rules and the amortization period to be confirmed with Controllership.'],
    ['Funding source', 'Open question of how much is funded through the central pool versus BU budgets, and the capex/opex split. Build spend is assumed to start Q4 2026; an earlier start is being tested if treatment allows.'],
    ['Scale and timing outliers', 'A small number of cases are on a different scale from the rest of the portfolio and should be sequenced to demonstrated ability to spend; PDLC value ramps late by design. Detail in the talk track, not on the page.'],
  ];
  const gap = 0.2, w = (CW - 2 * gap) / 3, h = 1.8;
  obs.forEach((o, i) => {
    const x = ML + (i % 3) * (w + gap), y = 1.95 + Math.floor(i / 3) * (h + 0.2);
    card(s, x, y, w, h, { n: i + 1, head: o[0], body: o[1], fontSize: 10 });
  });
  stampBox(s, ML, 6.0, CW, 0.45, 'Implication: budget for tranches released against gate evidence; initiative-level figures follow once S2 submissions close and sponsors and Finance have reviewed them.');
}

// =====================================================================================
// 11. FINANCE AND ACCOUNTING
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Finance engagement and accounting treatment',
    title: 'Finance and HR are now inside the business cases, and accounting treatment is being worked with Controllership so that S3 cases arrive with a defensible funding view',
    source: 'Finance (Tom) and HR (John, Alex) working session on the value-realization model, Sep 2; servicing cost-sizing session with FP&A, Sep 2; technology POC input on roles',
    notes: [
      'TALK TRACK (Anshu):',
      '- Finance is not reviewing at the end; Tom\'s team gives input as S2 cases land and will run the pressure-test sessions with Jaime next week. That is the corrective mechanism for ramp, assumptions and timing.',
      '- HR (John, Alex) have asked to align on how milestones translate into counting people and partial capacity, and on org-design stage gates as automation removes work; John will be in the Jaime sessions. Do not claim HR alignment is complete.',
      '- Accounting: FP&A\'s working assumption is capitalization over three years by job family (engineering yes, product management no) and by build type (from scratch for internal use versus adapting a vendor product); a sit-down with Controllership is still to be scheduled. Benefits are not capitalized and land linearly when realized. The value-realization model itself carries gross benefits only, with no cost in it yet.',
      '- Tom\'s remark in the Sep 2 working session (do not present as a Finance commitment): if we need to invest in H2 2026 to shift proven initiatives left, capacity exists in the second half; the question is how much benefit that pulls into Q1 2027.',
      '- The full models will go to John and Alex via ETO SharePoint. Open: whether ETO helps prepare Finance and HR for the Jaime sessions or stays out, since Finance and HR are meant to be the independent control and ETO represents the business.',
    ].join('\n'),
  });
  label(s, 'How Finance and HR are engaged', ML, 1.85, 6);
  const rows = [
    [th('Partner'), th('Role in the business cases'), th('Next touchpoint')],
    [tdb('Finance (Tom and team)'), td('Gives input as S2 cases land; challenges the value-realization profile by quarter, the ramp and the assumptions'), td('Finance input this week; review and challenge next week feeding the Jaime pressure-test sessions')],
    [tdb('HR (John, Alex)'), td('Translates milestones into headcount and partial capacity; to plan org-design implications (supervisory and management structures) as work is removed'), td('Receives full models via ETO SharePoint; joins the Jaime sessions')],
    [tdb('Controllership'), td('Rules on capitalization by job family and build type; amortization period'), td('Sit-down to be scheduled; target a ruling before S3')],
    [tdb('Technology points of contact'), td('Roles per build, phase durations, what can be compressed or parallelized'), td('Build-duration challenge sessions before S3')],
  ];
  s.addTable(rows, tableStyle({ x: ML, y: 2.2, w: 6.2, colW: [1.5, 2.9, 1.8], rowH: [0.32, 0.8, 0.8, 0.7, 0.7] }));
  const rx = ML + 6.55, rw = CW - 6.55;
  label(s, 'Accounting treatment: working principles', rx, 1.85, rw);
  card(s, rx, 2.2, rw, 3.32, { body: [
    { text: 'Capitalization is decided at role level, not initiative level', bold: true }, { text: 'Engineering and similar build roles typically qualify; product management does not', sub: true },
    { text: 'Build type matters', bold: true }, { text: 'From-scratch internal builds and enhancements to a vendor product are treated differently', sub: true },
    { text: 'Amortization', bold: true }, { text: 'Models carry a working assumption on the period; Controllership to confirm', sub: true },
    { text: 'Benefits', bold: true }, { text: 'Not capitalized; recognized linearly as realized', sub: true },
    { text: 'Timing', bold: true }, { text: 'Build spend assumed from Q4 2026; an earlier start is being tested if treatment allows', sub: true },
  ], fontSize: 10 });
  card(s, ML, 5.72, CW, 1.03, { head: 'Open questions we are working before S3', body: ['Share of investment funded from the central pool versus BU budgets, and the capex/opex split once role-level capitalization is ruled', 'Whether an earlier build start accelerates enough benefit into Q1 2027 to justify the earlier spend, and how shared contract minimums (for example telephony) are allocated as contact volume falls'], fontSize: 9.5, fill: C.blueLt, headH: 0.36, headSize: 11 });
}

// =====================================================================================
// 12. CEO/CFO FOLLOW-UPS + RAMP CHART
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Follow-ups from the CEO/CFO readout',
    title: 'Follow-ups from the CEO/CFO readout and the Finance model review centre on pace: the committed profile needs value in H1 2027, so we are shifting proven work left',
    subtitle: 'Items being worked with Finance and HR after the readout; list and status to be confirmed against the readout notes with Gilad and Tawanda before the ELT session',
    source: 'Finance and HR working session on the value-realization model, Sep 2; ETO working team',
    notes: [
      'TALK TRACK (Anshu):',
      '- The chart is deliberately unlabelled: the profile has not been reviewed with Jaime and is for next week\'s pressure-test. For your own reference, the bottom-up profile agreed with workstreams after several rounds is roughly 13% of big-bet run-rate value in H1 2027, 30% in H2 2027, 75% in H1 2028 and 100% in H2 2028; gross (no one-time or recurring cost) and big bets only. The profile originally shown to Enrique was more aggressive; if asked, say the workstreams have landed on a slower bottom-up ramp and Finance will pressure-test it next week.',
      '- Finance\'s reaction in the Sep 2 working session (do not attribute on the page): the total is fine if it lands within the horizon, but the H1 2027 profile is too slow against the committed savings; roughly a quarter of realization falls past the mid-year commitment. Options being worked: accelerate proven initiatives, push investment to H2, hold hiring timelines.',
      '- Do not raise: Finance and HR\'s views on the historic hit rate of big bets, the "Plan B" over-banking idea and its size, performance-management ideas, and HR\'s next-year selection dates. These were working-session remarks and are not for this audience.',
      '- Portfolio context (approximate, not on page): big bets roughly $225M gross against a roughly $320M automation target; close to $300M when bottom-up initiatives in Wave are included.',
    ].join('\n'),
  });
  // chart left
  label(s, 'Shape of the big-bet value build-up (illustrative, not to scale; profile under Finance review)', ML, 1.85, 5.6);
  s.addChart(pres.ChartType.bar, [{ name: 'Value build-up', labels: ['H1 2027', 'H2 2027', 'H1 2028', 'H2 2028'], values: [13, 30, 75, 100] }], {
    x: ML, y: 2.2, w: 5.6, h: 3.0, barDir: 'col', chartColors: [C.navy], barGapWidthPct: 60,
    showValue: false,
    catAxisLabelFontSize: 10, catAxisLabelColor: C.ink, catAxisLineShow: false, valAxisHidden: true, valAxisMaxVal: 115, valAxisMinVal: 0,
    valGridLine: { style: 'none' }, catGridLine: { style: 'none' }, showLegend: false, showTitle: false, fontFace: FONT,
  });
  txt(s, 'Value builds through 2027 and reaches run-rate in 2028; the committed profile front-loads savings into H1 2027. The workstream-aligned profile goes to the Finance and Jaime pressure-test next week; percentages are deliberately not shown here.', { x: ML, y: 5.25, w: 5.6, h: 0.8, fontSize: 9.5, color: C.grey, italic: true });
  // follow-ups table right
  const rx = ML + 6.0, rw = CW - 6.0;
  const rows = [
    [th('Follow-up'), th('What we are doing'), th('', { align: 'center' }), th('ETO comment')],
    [tdb('Ramp is too slow for H1 2027'), td('Faster scenario for servicing (agentic voice) and SDLC; challenge build durations with tech POCs'), td(''), td('In progress with tech POCs')],
    [tdb('Investment timing'), td('Test an earlier build start; confirm treatment with Controllership; Finance reviewing hiring timing'), td(''), td('Depends on treatment')],
    [tdb('Confidence and contingency'), td('Tier investment to confidence; keep the bottom-up pipeline filling in parallel; explicit gate criteria'), td(''), td('For S3')],
    [tdb('Platform-scale investments'), td('Review spend plans against spend to date before sequencing'), td(''), td('Review with Finance')],
    [tdb('Seller productivity framing'), td('Finalize the cost-out versus reinvestment framing with the sponsor and Finance'), td(''), td('Sponsor review Sep 3')],
    [tdb('Recurring inference cost (SDLC)'), td('Token-efficiency approach with the SDLC lead so recurring cost does not erode gross savings'), td(''), td('In progress')],
    [tdb('Fail-fast discipline'), td('Define continue, pivot or stop criteria per gate so a bet that will not deliver is stopped early'), td(''), td('For S3')],
  ];
  const rh = [0.32, 0.56, 0.56, 0.56, 0.5, 0.56, 0.56, 0.56];
  s.addTable(rows, tableStyle({ x: rx, y: 1.85, w: rw, colW: [1.75, 2.85, 0.4, 1.23], rowH: rh, fontSize: 9 }));
  const st12 = ['A', 'A', 'G', 'A', 'A', 'A', 'G'];
  let yy = 1.85 + rh[0];
  st12.forEach((st, i) => { ryg(s, rx + 1.75 + 2.85 + 0.11, yy + 0.12, st, 0.18); yy += rh[i + 1]; });
  stampBox(s, ML, 6.28, CW, 0.45, 'Bottom line: Finance can live with the ramp only if the total lands within the horizon and H1 2027 moves earlier; every option we are working either moves proven value earlier or moves spend later.');
}

// =====================================================================================
// 13. PROGRESS AND POC UPDATES
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Progress and updates on big bets and proofs of concept',
    title: 'Servicing sizing is aligned with ops leaders and seller productivity goes to its sponsor this week; PDLC and risk are in validation, and pilots begin at S4',
    subtitle: 'Status is the ETO read as of Sep 2; the proof-of-concept column is to be confirmed with ETO leadership before the ELT session',
    source: 'Working sessions Aug 13 - Sep 2 with servicing ops leaders, sales working team, PDLC and checkout teams, technology POCs',
    notes: [
      'TALK TRACK (Anshu): this is the ELT "progress and POC" page. Keep it to what changed in the last three weeks and what happens next.',
      '- Servicing: on Sep 2 we aligned the model with ops leaders: contact avoidance baseline and assumptions agreed (with a headroom callout for top-of-funnel and help center); enhanced chat and agentic voice assumptions accepted with containment caps by complexity (roughly 90/80/70 for easy/medium/hard); copilot handle-time line folded back into avoidance at the ops leaders\' request; skill-based routing and workforce management aligned (OFF-PAGE: roughly $7M cost takeout); non-FTE costs (telephony, software) kept simple. NPS: ETO working view, not yet reviewed with ops leaders: expected constant to slightly improved; a data-driven ACR-to-ASA-to-NPS method is available for S3 if the 18-month volume forecast is provided.',
      '- Seller productivity: three fast-tracked initiatives refined over three weeks with the sales working team; S1-to-S2 deltas prepared for the Susan review on Sep 3; SMB long-tail attach and contra not yet sized.',
      '- PDLC: agreed with checkout to manage centrally as a parent initiative; placeholder value zeroed until validation on new baselines; approach is roughly four months of design plus one or two pilots, then six to eight teams, then scale.',
      '- Risk and compliance: collections submitted for S2; financial-crimes cases ready for Friday finance calls; Helix under challenge.',
      '- POCs proper start at S4; until then "proof" is the sizing alignment and the pilot design.',
      '- Open point: the working team was not sure what "proof of concept" on the ELT agenda refers to (client-run POCs, S4 pilots, or something else). Confirm with Tawanda and Gilad before Tuesday and adjust the right-hand column.',
      '- Helix (do not characterize on the page): investment request is large relative to spend to date; Finance shares the execution-capacity concern; the case is being handled on its own track.',
    ].join('\n'),
  });
  const rows = [
    [th('Area'), th('', { align: 'center' }), th('What happened since the last update'), th('What is next'), th('Proof point / pilot (to confirm)')],
    [tdb('Servicing'), td(''), td('Model aligned with ops leaders on Sep 2 across contact avoidance, enhanced chat and self-service, agentic voice, skill-based routing and workforce management; copilot benefit folded into avoidance; non-FTE costs simplified'), td('S2 submission this week; faster scenario for agentic voice; top-of-funnel headroom (help center, self-resolve) and support-function and leadership-span efficiencies sized for S3'), td('Pilot design at S4; NPS impact stated qualitatively (expected constant to slightly improved); data-driven method ready when the volume forecast is available')],
    [tdb('Seller productivity'), td(''), td('Three fast-tracked initiatives (underwriting, pricing, SMB long tail) pressure-tested with the sales working team; S1-to-S2 deltas prepared for the sponsor review on Sep 3'), td('Sponsor and Finance review; size remaining components (SMB long-tail attach, contra) after SME input'), td('Cost-out versus reinvestment framing to be finalized with sponsor and Finance')],
    [tdb('SDLC'), td(''), td('Sizing with tech POCs; recurring inference cost identified as the key sensitivity'), td('Token-efficiency approach; build-duration challenge'), td('Well-trodden use case; early pilot candidate for push-left')],
    [tdb('PDLC'), td(''), td('Agreed with checkout to run as one centrally managed parent initiative; BU placeholder zeroed pending validation on re-cut baselines'), td('Re-baseline with role-ratio actions; deeper dive with BU teams once numbers are ready'), td('Design-and-pilot phase before any scale decision; value builds after the first year')],
    [tdb('Risk'), td(''), td('Collections submitted for S2; financial-crimes cases prepared for Finance calls; Helix case handled on its own track'), td('Finance calls this week; Helix savings case still being clarified and investment request to be reviewed with Finance'), td('Pilots for the smaller cases at S4; platform case sequenced after its execution plan is reviewed')],
  ];
  const rh13 = [0.32, 0.95, 0.78, 0.55, 0.68, 0.8];
  s.addTable(rows, tableStyle({ x: ML, y: 1.85, w: CW, colW: [1.35, 0.4, 4.15, 3.3, 3.03], rowH: rh13, fontSize: 9 }));
  const st13 = ['G', 'G', 'A', 'A', 'A'];
  let y13 = 1.85 + rh13[0];
  st13.forEach((st, i) => { ryg(s, ML + 1.35 + 0.11, y13 + 0.12, st, 0.18); y13 += rh13[i + 1]; });
  stampBox(s, ML, 6.22, CW, 0.45, 'Read-across: sizing alignment with workstream leaders is the proof point available before S4; formal proofs of concept and pilots start once S3 fixes scope and funding.');
}

// =====================================================================================
// 14. NEXT STEPS AND ASKS
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Next steps and what we need from you',
    title: 'Next two weeks: close S2, run the Finance and Jaime reviews, and stack the cases into one S3 plan; we need your alignment on the criteria and a path on resourcing',
    source: 'ETO working team, Sep 2',
    notes: [
      'TALK TRACK (Anshu): close on the asks, not on the timeline. Confirm the criteria list in the Sep 3 review before presenting it as your method.',
      '- Ask 1: align on the criteria I propose to use when the S2 cases come in, and on tiered investment, so S3 comes back as one plan.',
      '- Ask 2: sponsor the dedicated-resourcing conversation with Srini (her technology resourcing framework) so well-trodden initiatives can start build in Q4 2026 or earlier.',
      '- Ask 3: support the Finance and Controllership path on treatment and central pool versus BU funding.',
      '- Ask 4: breathing room. Let us close S2 and the Finance review before initiative-level numbers go beyond the sponsor and Finance review; that is how we avoid fire drills next week.',
      '- Then: next time I come to you I will have dollar amounts and more substance, with Finance having seen them first.',
    ].join('\n'),
  });
  label(s, 'Timeline', ML, 1.85, 6);
  const steps = [
    ['This week', ['S2 pencils-down on big-bet business cases', 'Finance and HR input into the servicing and sales cases; sponsor review of seller productivity', 'Servicing and seller-productivity submissions finalized']],
    ['Next week', ['Finance review and challenge of submitted cases (Tom, John) feeding the Jaime pressure-test sessions', 'ELT update on Tuesday: pipeline, POC progress, CEO/CFO follow-ups, sequencing approach', 'Tech POC sessions on build-duration compression']],
    ['In ~2.5 weeks (S3)', ['Cases stacked across levers into one implementation plan', 'Sequencing confirmed against the agreed criteria', 'Resourcing and funding request with sized ranges']],
    ['Then (S4)', ['Pilots and proofs of concept for the accelerate horizon', 'Org-design stage gates with HR', 'Kill or scale decisions on evidence']],
  ];
  const sw = (CW - 3 * 0.15) / 4;
  steps.forEach((st, i) => {
    const x = ML + i * (sw + 0.15);
    const fill = i === 0 ? C.blue : i === 1 ? C.navy : C.greyMid;
    s.addShape(pres.ShapeType.chevron, { x, y: 2.2, w: sw, h: 0.5, fill: { color: fill }, line: { color: fill, width: 0 } });
    txt(s, st[0], { x: x + 0.3, y: 2.2, w: sw - 0.5, h: 0.5, fontSize: 10.5, bold: true, color: i < 2 ? C.white : C.navy, valign: 'middle' });
    bullets(s, st[1], { x: x + 0.05, y: 2.85, w: sw - 0.1, h: 1.5, fontSize: 9.5 });
  });
  label(s, 'What we need from you', ML, 4.45, 6);
  const asks = [
    ['Align on the criteria', 'The sequencing criteria I propose to apply when S2 cases come in, with investment tiered to gate evidence, so S3 returns one holistic plan'],
    ['Open the resourcing path', 'Sponsor the dedicated build-and-run capacity conversation with Srini so proven initiatives can start build in Q4 2026 or earlier'],
    ['Back the funding path', 'Support Finance and Controllership on treatment and on central pool versus BU funding ahead of S3'],
    ['Give us breathing room', 'Hold initiative-level numbers until S2 closes and Finance has reviewed, so next week brings substance rather than fire drills'],
  ];
  const aw = (CW - 3 * 0.15) / 4;
  asks.forEach((a, i) => card(s, ML + i * (aw + 0.15), 4.8, aw, 1.9, { n: i + 1, head: a[0], body: a[1], fontSize: 10, fill: i === 3 ? C.blueLt : C.greyLt }));
}

// =====================================================================================
// APPENDIX DIVIDER
// =====================================================================================
{
  const s = pres.addSlide();
  rect(s, 0, 0, W, H, { fill: { color: C.navy } });
  txt(s, 'Appendix', { x: 0.8, y: 2.8, w: 10, h: 0.9, fontSize: 36, bold: true, color: C.white });
  txt(s, 'A1  Stage-gate definitions\nA2  Cost-sizing methodology\nA3  Servicing big-bet architecture and NPS approach\nA4  Seller productivity: from S1 long list to three fast-tracked S2 cases\nA5  PDLC: one centrally managed parent initiative\nA6  Mapping of this document to the Friday and Tuesday agendas\nA7  Glossary', { x: 0.8, y: 3.8, w: 10, h: 2.4, fontSize: 13, color: 'CADCFC' });
  pageNo += 1;
}

// =====================================================================================
// A1. STAGE GATES
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Appendix A1: stage-gate definitions',
    title: 'Stage gates S1 to S5 move each initiative from a theoretical sizing to committed scale funding; automation initiatives are inherently iterative across these gates',
    subtitle: 'Working definitions used by the ETO working team; to be confirmed against the ETO stage-gate process document',
    source: 'ETO stage-gate process as applied to the AI & Automation lever',
    notes: 'Reference page. Use if Enrique or Jaime ask what changes between S2 and S3, or why numbers keep moving. Key line: at S3 we have the best theoretical understanding; S4 pilots teach us implementation timelines; S5 reflects that learning. This is true for every automation initiative, unlike role ratios or spans and layers where actions are clearer up front.',
  });
  const rows = [
    [th('Gate'), th('Purpose'), th('Inputs'), th('Outputs'), th('Confidence in numbers')],
    [tdb('S1'), td('Identify and size the long-list of opportunities'), td('Outside-in benchmarks; initial baselines; sponsor interviews'), td('Initiative list with preliminary value and investment'), td('Directional; ranges wide')],
    [tdb('S2'), td('Refine business cases with SMEs, data and technology'), td('SME interviews; actual data at intent or role level; tech POC roles and phases; Finance review'), td('Submitted business cases in Wave with one-time and recurring cost'), td('Higher; still pre-pilot')],
    [tdb('S3'), td('Stack cases across levers into one implementation plan'), td('All S2 cases; parent/child structure; sequencing criteria; capacity view'), td('Holistic plan; sequencing; resourcing and funding request'), td('Best theoretical view')],
    [tdb('S4'), td('Prove through pilots and proofs of concept'), td('Pilot results; adoption; real build durations; org-design ripple effects'), td('Evidence-based timelines; kill or scale decisions'), td('Evidence-based')],
    [tdb('S5'), td('Commit scale funding and targets'), td('Updated sizing on pilot evidence; treatment confirmed'), td('Committed run-rate and investment by initiative'), td('Committed')],
  ];
  s.addTable(rows, tableStyle({ x: ML, y: 1.85, w: CW, colW: [0.8, 2.9, 3.4, 3.0, 2.13], rowH: [0.32, 0.6, 0.66, 0.6, 0.6, 0.6] }));
  const wq = (CW - 2 * 0.2) / 3;
  card(s, ML, 5.45, wq, 1.2, { head: 'Why numbers move between gates', body: 'Baselines, SME input and technology effort are refined at each gate; S4 pilots replace assumptions with evidence', fontSize: 9.5, fill: C.blueLt, headH: 0.4, headSize: 11 });
  card(s, ML + wq + 0.2, 5.45, wq, 1.2, { head: 'What is fixed at S3', body: 'Scope, sequencing, resourcing plan and the funding request, with continue, pivot or stop criteria per initiative', fontSize: 9.5, fill: C.blueLt, headH: 0.4, headSize: 11 });
  card(s, ML + 2 * (wq + 0.2), 5.45, wq, 1.2, { head: 'What is fixed at S5', body: 'Committed run-rate and investment by initiative once pilot evidence and accounting treatment are in (to confirm against the ETO process)', fontSize: 9.5, fill: C.blueLt, headH: 0.4, headSize: 11 });
}

// =====================================================================================
// A2. COST SIZING METHODOLOGY
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Appendix A2: cost-sizing methodology',
    title: 'Investment is sized bottom-up as people cost by phase plus non-people run cost, using a typical build team and token benchmarks by use-case complexity',
    source: 'ETO working team; approach walked through with Finance and HR on Sep 2',
    notes: 'Reference page for Finance questions. People cost: a set of roles that constitute a build team (product management, engineering, QA, DevOps, UX) at a blended cost per person; activities broken into plan and design, build and test, pilot, scale; teams and duration per phase aligned with tech POCs; some parallelization assumed. Non-people cost: run cost driven by token usage, sized by defining use-case complexity and applying industry benchmarks for average token usage at that complexity. Run team typically one engineer plus one operations owner. Capitalization by job family to be confirmed with Controllership; models currently assume three-year amortization. Benefits are not capitalized.',
  });
  const w = (CW - 0.25) / 2;
  card(s, ML, 1.9, w, 2.85, { head: 'One-time cost: people by phase', body: [
    'Standard build team: product management, engineering, QA, DevOps, UX',
    'Blended cost per person applied across the team',
    'Work broken into phases: plan and design, build and test, pilot, scale',
    'For each phase, number of teams or people and duration agreed with technology POCs',
    'Parallelization assumed where phases can overlap; build-duration compression being tested for the faster scenario',
    'Capitalization assessed at role level and by build type; rules to be confirmed with Controllership',
  ], fontSize: 10.5 });
  card(s, ML + w + 0.25, 1.9, w, 2.85, { head: 'Recurring cost: run team and inference', body: [
    'Run team per initiative, typically one engineer plus one operations owner',
    'Token and inference usage sized by defining the complexity of each use case',
    'Industry benchmarks for average token usage at that complexity applied per use case',
    'SDLC carries the highest inference load (tokens consumed continuously while writing code); efficiency work under way',
    'Platform and vendor contracts with monthly minimums (for example telephony) do not fall with volume; how shared contract cost is allocated across initiatives is still to be agreed',
    'Benefits are not capitalized and are recognized linearly as realized',
  ], fontSize: 10.5 });
  label(s, 'Working assumptions currently in the models (to be confirmed at the Finance review)', ML, 4.98, CW);
  const wa = (CW - 3 * 0.18) / 4;
  [
    ['Build start', 'All initiatives assumed to start build in Q4 2026; an earlier start is being tested where treatment allows'],
    ['Amortization', 'Working assumption on the period for capitalizable roles; Controllership to confirm'],
    ['Benefit haircuts', 'Conservative haircuts applied to benefit assumptions, with upside noted rather than sized'],
    ['Run cost', 'Token usage per use case from complexity benchmarks; SDLC the largest recurring line'],
  ].forEach((a, i) => card(s, ML + i * (wa + 0.18), 5.3, wa, 1.15, { head: a[0], body: a[1], fontSize: 9.5, fill: C.blueLt, headH: 0.38, headSize: 11 }));
  txt(s, 'Outputs feed Wave as one-time and recurring cost per initiative; net run-rate benefit in Wave must include both, with assumptions noted for the Finance review.', { x: ML, y: 6.55, w: CW, h: 0.25, fontSize: 9, color: C.grey, italic: true });
}

// =====================================================================================
// A3. SERVICING ARCHITECTURE + NPS
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Appendix A3: servicing big-bet architecture',
    title: 'The servicing big bet works down the contact funnel: avoid the contact, self-serve it, resolve it with an AI agent, then run the remaining human queue more efficiently',
    source: 'Levers 1-4: servicing sizing alignment with ops leaders, Sep 2; NPS position: ETO working team',
    notes: [
      'Reference page. Sequence and logic agreed with ops leaders on Sep 2 (the NPS position is the ETO working view and has not been reviewed with ops leaders):',
      '1. Contact avoidance: remove the need for the contact (policy, product, journey fixes) - baseline and assumptions aligned; headroom at top of funnel (help center is the starting point for many customers; surfacing known data such as dispute status or merchant aliases before chat) noted but not sized, to stay conservative in Wave.',
      '2. Enhanced chat and self-service: chat-based on the post-avoidance baseline; containment capped by complexity (roughly 90/80/70 easy/medium/hard).',
      '3. Agentic voice: takes calls end to end; copilot handle-time benefit folded back into this line at ops leaders\' request so that no separate 700-plus FTE efficiency claim sits on the ops leader.',
      '4. Efficiency: skill-based routing (faster, higher first-call resolution; slight ASA increase within service level) and workforce management (right people, right place, right time); aligned at roughly $7M cost takeout. Non-FTE: telephony and software maintenance only; contract minimums do not flex.',
      'NPS: qualitatively constant to slightly improved across levers; a waterfall is a separate exercise. Method available for S3: plot abandoned call rate against ASA, then ASA against NPS from historical data; project abandoned rate from forecast contacts, AHT, FTE, shrink and occupancy. Requires the 18-month contact forecast and headcount plan from the business.',
      'Contact economics for talking points only: hard contacts roughly $8, easy roughly $2, average roughly $4.7; contacts roughly 46M today.',
    ].join('\n'),
  });
  const stages = [
    ['1  Avoid the contact', 'Policy, product and journey fixes so the need never arises; top-of-funnel headroom (help center, surfacing known data) flagged for S3', C.navy],
    ['2  Self-serve it', 'Enhanced chat and self-service on the post-avoidance baseline, with containment capped by complexity', C.navy],
    ['3  Resolve with an AI agent', 'Agentic voice takes contacts end to end; assistant-style benefits folded in rather than counted separately', C.blue],
    ['4  Run the rest efficiently', 'Skill-based routing and workforce management; non-FTE costs (telephony, software) simplified', C.blue],
  ];
  const fw = CW, fy = 1.9;
  stages.forEach((st, i) => {
    const inset = i * 0.55;
    const x = ML + inset, w = fw - 2 * inset, y = fy + i * 0.82;
    rrect(s, x, y, w, 0.72, { fill: { color: st[2] } });
    txt(s, st[0], { x: x + 0.2, y: y + 0.06, w: 3.2, h: 0.6, fontSize: 12, bold: true, color: C.white, valign: 'middle' });
    txt(s, st[1], { x: x + 3.5, y: y + 0.06, w: w - 3.7, h: 0.6, fontSize: 10, color: C.white, valign: 'middle' });
  });
  card(s, ML, 5.3, CW / 2 - 0.12, 1.4, { head: 'NPS position (ETO working view, not yet reviewed with ops leaders)', body: 'Expected constant to slightly improved across the levers; a quantified waterfall is a separate exercise for S3 and needs the 18-month contact forecast and headcount plan', fontSize: 9.5 });
  card(s, ML + CW / 2 + 0.12, 5.3, CW / 2 - 0.12, 1.4, { head: 'Guardrails agreed with ops leaders', body: 'Conservative sizing in Wave with upside noted; one line per lever; no separate efficiency claim that depends on unproven tooling; initiatives that generate contacts carry that cost in the momentum case', fontSize: 9.5 });
}

// =====================================================================================
// A4. SELLER PRODUCTIVITY JOURNEY
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Appendix A4: seller productivity big bet',
    title: 'Seller productivity moved from the mid-August long list to three fast-tracked S2 cases refined with the sales working team over three weeks; two inputs remain open',
    source: 'Sales working-team sessions Aug 13 - Sep 2; sponsor review scheduled Sep 3',
    notes: [
      'Reference page. Numbers for talking points only (pre-Finance review, not on page):',
      '- Three initiatives: underwriting, pricing, SMB long tail. Roughly $24M cost take-out, about $20M one-time and $4.5M recurring, roughly $20M net run-rate benefit; 3.5-4x return on one-time investment on a transaction-margin basis and 6.5x-plus on revenue.',
      '- Sponsor intent: Susan wants to reinvest the net benefit into revenue rather than take headcount out; Finance will want the cost-out component tight either way.',
      '- A separate integration cost-out (roughly $23M, not a big bet) runs through the normal S2 process and is the most direct sales saving.',
      '- Not yet sized: SMB long-tail attach (pending SME interviews and data) and contra (sized at a 2-5% reduction but not validated with the contra team).',
    ].join('\n'),
  });
  const steps = [
    ['S1: long list', 'Mid-August readout identified the sales automation opportunity set with preliminary revenue, cost and one-time investment', C.greyMid, C.navy],
    ['Fast-track selection', 'Three initiatives selected with Enrique for S2: underwriting, pricing, SMB long tail; the rest continue through the normal process', C.navy, C.white],
    ['S2 refinement', 'Three weeks of interviews and data with the sales working team; sizing refined to higher confidence; S1-to-S2 deltas documented', C.navy, C.white],
    ['Sponsor and Finance review', 'Sponsor review Sep 3; Finance review of the business cases; alignment on the cost-out versus reinvestment framing', C.blue, C.white],
    ['S2 submission', 'Formal submission with one-time and recurring cost; open items carried as explicit assumptions', C.blue, C.white],
  ];
  const sw = (CW - 4 * 0.1) / 5;
  steps.forEach((st, i) => {
    const x = ML + i * (sw + 0.1);
    s.addShape(pres.ShapeType.chevron, { x, y: 1.95, w: sw, h: 0.55, fill: { color: st[2] }, line: { color: st[2], width: 0 } });
    txt(s, st[0], { x: x + 0.28, y: 1.95, w: sw - 0.5, h: 0.55, fontSize: 10, bold: true, color: st[3], valign: 'middle' });
    txt(s, st[1], { x: x + 0.05, y: 2.62, w: sw - 0.1, h: 1.5, fontSize: 9.5 });
  });
  const cw2 = (CW - 0.25) / 2;
  card(s, ML, 4.0, cw2, 2.3, { head: 'What the three initiatives do', body: ['Underwriting: automate the analysis and decision support behind merchant underwriting', 'Pricing: automate pricing analysis and proposal preparation for sellers', 'SMB long tail: agent-assisted outreach so partners and sellers can serve the long tail of merchants', 'All three release seller and support capacity; how that capacity is taken (cost-out or reinvestment) is to be agreed with the sponsor and Finance'], fontSize: 10.5 });
  card(s, ML + cw2 + 0.25, 4.0, cw2, 2.3, { head: 'Open items carried into S2', body: ['SMB long-tail attach component: sizing pending SME interviews and data', 'Contra-revenue effect: assumption not yet validated with the contra team', 'Cost-out versus reinvestment framing to be agreed with the sponsor before Finance review', 'A separate sales integration cost-out runs as a bottom-up initiative, not as a big bet'], fontSize: 10.5, fill: C.blueLt });
  stampBox(s, ML, 6.42, CW, 0.33, 'Detail on revenue, cost and one-time investment stays in the sponsor and Finance materials until S2 is submitted and reviewed.');
}

// =====================================================================================
// A5. PDLC STRUCTURE
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Appendix A5: PDLC big bet',
    title: 'PDLC is now one centrally managed big bet with a company-level parent initiative and BU child views, re-baselined for Wave 1 and role-ratio actions and phased design-first',
    source: 'PDLC and checkout alignment session, Sep 2',
    notes: [
      'Reference page. Talking points (not on page):',
      '- Why central: a standardized product-development lifecycle with common tooling and harnesses for product managers, with BU context built in, mirrors what engineering is doing in SDLC. Managed as one program so the impact is counted once and rolled up.',
      '- Sizing approach: day-in-the-life view of product managers and adjacent roles, activity-level automation potential informed by other clients and tool maturity, a productivity assumption (roughly 25% before haircuts) applied to the population, then haircuts on capture. Rough earlier sizing was of the order of $48M and was deliberately withheld pending new baselines.',
      '- Re-baselining: Wave 1 actions and forward-looking role-ratio actions (engineer to PM to design) change the PM population; sizing assumes partial achievement of target ratios.',
      '- Roadmap: roughly four months of design plus one or two pilots; then six to eight teams across a couple of BUs building the technology backbone, governance and change model (roughly eight months in total); then twelve months to scale. Little value in the first six to eight months; ramp after stabilization.',
      '- Checkout: kept the initiative in Wave but zeroed the dollar placeholder until validation, because an unvalidated number shows against their target and gives a false sense of attainment. ETO agreed: no number in Wave that the team cannot execute against.',
    ].join('\n'),
  });
  // parent/child structure (left)
  label(s, 'Structure in Wave', ML, 1.85, 5.6);
  rrect(s, ML, 2.2, 5.6, 0.85, { fill: { color: C.navy } });
  txt(s, 'Parent initiative: PDLC program (company level, managed by ETO)', { x: ML + 0.18, y: 2.2, w: 5.24, h: 0.45, fontSize: 11, bold: true, color: C.white, valign: 'middle' });
  txt(s, 'Standard lifecycle, tooling and harnesses; one impact number for the lever', { x: ML + 0.18, y: 2.6, w: 5.24, h: 0.4, fontSize: 9.5, color: C.white });
  const kids = ['Checkout (placeholder held at zero pending validation)', 'Other BUs (portion of program value, BU context built in)', 'Enablers: role-ratio actions and SDLC tooling (counted once)'];
  kids.forEach((k, i) => {
    const x = ML + i * (5.6 / 3 + 0.02);
    const w = 5.6 / 3 - 0.08;
    s.addShape(pres.ShapeType.line, { x: x + w / 2, y: 3.05, w: 0, h: 0.25, line: { color: C.greyMid, width: 1 } });
    rrect(s, x, 3.3, w, 1.05, { fill: { color: i === 0 ? C.blueLt : C.greyLt } });
    txt(s, k, { x: x + 0.1, y: 3.38, w: w - 0.2, h: 0.9, fontSize: 9.5, color: C.navy });
  });
  card(s, ML, 4.55, 5.6, 1.7, { head: 'Re-baselining principles', body: ['Start from the post-Wave-1 organization, not the S1 snapshot', 'Net out planned role-ratio actions before applying automation assumptions', 'No number enters Wave that the BU cannot execute against; placeholders stay at zero until validated'], fontSize: 9.5 });
  // roadmap (right)
  const rx = ML + 6.0, rw = CW - 6.0;
  label(s, 'Phased, design-first roadmap', rx, 1.85, rw);
  const ph = [
    ['1  Define and prove', 'Define the target lifecycle, technology backbone and KPIs; run one or two pilots to prove value in detail', C.navy],
    ['2  Build across teams', 'Extend to a handful of teams across a couple of BUs; harden the agentic tooling, governance and change model', C.navy],
    ['3  Scale and improve', 'Roll out broadly; value ramps only after stabilization, so little is expected in the first year', C.blue],
  ];
  ph.forEach((p, i) => {
    const y = 2.2 + i * 1.36;
    rrect(s, rx, y, rw, 1.25, { fill: { color: p[2] } });
    txt(s, p[0], { x: rx + 0.18, y: y + 0.12, w: rw - 0.36, h: 0.35, fontSize: 11.5, bold: true, color: C.white });
    txt(s, p[1], { x: rx + 0.18, y: y + 0.48, w: rw - 0.36, h: 0.72, fontSize: 10, color: C.white });
  });
  stampBox(s, ML, 6.4, CW, 0.35, 'Implication for sequencing: PDLC is an enabler that follows role-ratio actions and is funded design-and-pilot first; scale funding is gated on pilot evidence.');
}

// =====================================================================================
// A6. MAPPING TO AGENDAS
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Appendix A6 (working-team page, remove before circulation): how this document maps to the two sessions',
    title: 'One storyline serves both sessions: Friday uses the full document; Tuesday\'s ELT update reuses the pages mapped to its four agenda items with the pipeline snapshot refreshed',
    source: 'Agenda items requested for the Friday session and the Tuesday ELT session',
    notes: 'Internal page for the working team; remove before sending to Enrique. Friday agenda items requested: tech resourcing capacity; cost and investment; approach to sequencing and prioritization; accounting treatment. Tuesday ELT agenda: overall pipeline tracking; progress and status on big bets including proofs of concept; follow-ups from the CEO/CFO readout; approach to sequencing, resourcing and prioritization.',
  });
  const rows = [
    [th('Agenda item'), th('Friday (Enrique, Jaime, Anshu)'), th('Tuesday ELT'), th('Pages')],
    [tdb('Snapshot of initiatives and where we are'), td('Level-set; status with ETO commentary'), td('Overall pipeline tracking'), td('4, 5')],
    [tdb('Org change impacts'), td('Talk track'), td('Context only'), td('6')],
    [tdb('How we are resourcing; tech capacity'), td('Core topic; Srini framework page to insert'), td('Approach to resourcing'), td('7 (+ Srini page)')],
    [tdb('Sequencing and prioritization'), td('Proposed criteria and illustrative horizons'), td('Approach to sequencing and prioritization'), td('8, 9')],
    [tdb('Investment themes; accounting treatment'), td('Observations and themes; sized numbers follow the Finance review'), td('Not covered until Finance review'), td('10, 11')],
    [tdb('CEO/CFO readout follow-ups'), td('Preview'), td('Follow-ups from CEO/CFO readout'), td('12')],
    [tdb('Progress and proofs of concept'), td('Reference'), td('Progress and status on big bets including POC'), td('13')],
    [tdb('Next steps and asks'), td('Asks to Enrique and Jaime'), td('Next steps'), td('14')],
  ];
  s.addTable(rows, tableStyle({ x: ML, y: 1.85, w: CW, colW: [3.2, 3.6, 3.6, 1.83], rowH: [0.32, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] }));
}

// =====================================================================================
// A5. GLOSSARY
// =====================================================================================
{
  const s = pres.addSlide();
  base(s, {
    section: 'Appendix A7: glossary',
    title: 'Glossary of terms used in this document',
    source: 'ETO working team',
    notes: 'Reference only.',
  });
  const rows = [
    [th('Term'), th('Meaning'), th('Term'), th('Meaning')],
    [tdb('Big bet'), td('Large, centrally tracked automation initiative; roughly 15-16 across five areas'), tdb('Wave'), td('Initiative tracking tool for business cases; also Wave 1 (org actions completed) versus Wave 2')],
    [tdb('S1 to S5'), td('Stage gates from initial sizing to committed scale (definitions to confirm against the ETO process)'), tdb('Tech POC'), td('Technology point of contact per initiative (distinct from proof of concept)')],
    [tdb('One-time cost'), td('Build cost: people by phase plus set-up'), tdb('Recurring cost'), td('Run team (typically one engineer plus one operations owner) plus inference and token usage; shared vendor contracts tracked separately')],
    [tdb('Contact avoidance'), td('Removing the need for a customer contact entirely'), tdb('Containment'), td('Share of contacts resolved in a digital channel without a human')],
    [tdb('Agentic voice'), td('AI agent that handles voice contacts end to end'), tdb('Copilot'), td('AI assistant that supports a human agent during a contact')],
    [tdb('PDLC / SDLC'), td('Product / software development lifecycle'), tdb('Parent / child initiative'), td('Structure in Wave that counts a lever once at company level with BU views beneath')],
    [tdb('Central pool'), td('Company-level funding for transformation investment, versus BU budgets'), tdb('Run-rate value'), td('Annualized gross benefit once an initiative is fully ramped')],
  ];
  s.addTable(rows, tableStyle({ x: ML, y: 1.85, w: CW, colW: [1.7, 4.4, 1.7, 4.43], rowH: [0.32, 0.55, 0.55, 0.55, 0.55, 0.55, 0.55, 0.55] }));
}

pres.writeFile({ fileName: OUT }).then(f => console.log('wrote', f, 'slides:', pageNo));
