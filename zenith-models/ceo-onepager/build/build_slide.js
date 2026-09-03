// One-slide CEO read-out: investment requirements — themes, no figures.
const pptxgen = require("pptxgenjs");
const fs = require("fs");
const C = require("./content.js");

// ---- visual identity ----------------------------------------------------
const NAVY = "1B2A4A";     // dominant
const SLATE = "3D5A80";    // secondary
const INK = "1F2933";      // body text
const MUTED = "5B6B7C";    // captions
const GROUND = "EEF1F5";   // cool tinted panel
const AMBER = "B8741A";    // single accent: decisions in flight
const AMBER_BG = "FBF3E6";
const WHITE = "FFFFFF";
const LINE = "D3D9E1";
const HEAD = "Cambria";
const BODY = "Calibri";

// ---- icons (react-icons -> PNG) -------------------------------------------
let icons = {};
async function prep() {
  try {
    const React = require("react");
    const ReactDOMServer = require("react-dom/server");
    const sharp = require("sharp");
    const fi = require("react-icons/fi");
    const make = async (Icon) => {
      const svg = ReactDOMServer.renderToStaticMarkup(
        React.createElement(Icon, { size: 256, color: "#FFFFFF", strokeWidth: 2 }));
      const buf = await sharp(Buffer.from(svg)).png().toBuffer();
      return "image/png;base64," + buf.toString("base64");
    };
    icons.eye = await make(fi.FiEye);
    icons.layers = await make(fi.FiLayers);
    icons.flag = await make(fi.FiFlag);
    icons.grid = await make(fi.FiGrid);
  } catch (e) { icons = {}; }
}

function header(slide, x, y, w, text, key, color) {
  const c = color || NAVY;
  slide.addShape("ellipse", { x, y, w: 0.3, h: 0.3, fill: { color: c }, line: { color: c } });
  if (icons[key]) slide.addImage({ data: icons[key], x: x + 0.065, y: y + 0.065, w: 0.17, h: 0.17 });
  slide.addText(text, { x: x + 0.4, y: y - 0.03, w: w - 0.4, h: 0.36, fontFace: HEAD, fontSize: 13,
    bold: true, color: c, isTextBox: true, margin: 0, valign: "middle" });
}

async function build(out) {
  await prep();
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
  const s = pres.addSlide();
  s.background = { color: WHITE };
  const M = 0.5, W = 13.33 - 2 * M;

  // ---- eyebrow + headline + sub ----
  s.addText(C.eyebrow.toUpperCase(), { x: M, y: 0.2, w: W, h: 0.22, fontFace: BODY, fontSize: 9,
    color: SLATE, charSpacing: 1.5, isTextBox: true, margin: 0, valign: "middle" });
  s.addText(C.headline, { x: M, y: 0.42, w: W, h: 0.6, fontFace: HEAD, fontSize: 17, bold: true,
    color: NAVY, isTextBox: true, margin: 0, valign: "middle" });
  s.addText(C.subtitle, { x: M, y: 1.03, w: W, h: 0.22, fontFace: BODY, fontSize: 10,
    color: MUTED, isTextBox: true, margin: 0, valign: "middle" });

  // rough line estimator for content-sized blocks (Calibri ~ pt/140 inch per char)
  const est = (chars, widthIn, pt) => Math.ceil(chars / Math.floor(widthIn / (pt / 132)));
  const lineH = (pt) => pt * 1.22 / 72;

  // ---- main band: themes (left, wide) | shape + decisions (right, stacked) ----
  const top = 1.34, gap = 0.22;
  const wL = 6.3, wR = W - wL - gap;
  const xL = M, xR = M + wL + gap;
  const rPt = 8.6, rW = wR - 0.36;
  const lLines = C.layers.map((L) => est((L.name + " (" + L.tag + "): " + L.text).length, rW, rPt));
  const lGap = 0.07;
  const hA = 0.56 + lLines.reduce((a, n) => a + n * lineH(rPt) + lGap, 0) + 0.02;
  const dLines = C.dependencies.map((D) => est((D.lead + ".  " + D.text).length, rW, rPt));
  const dGap = 0.06;
  const hC = 0.52 + dLines.reduce((a, n) => a + n * lineH(rPt) + dGap, 0) + 0.06;
  const bandH = hA + 0.15 + hC;

  // Left: themes
  s.addShape("rect", { x: xL, y: top, w: wL, h: bandH, fill: { color: WHITE }, line: { color: LINE, width: 0.75 } });
  header(s, xL + 0.2, top + 0.17, wL - 0.4, C.themes_title, "eye");
  let y = top + 0.64;
  const tPt = 10, tW = wL - 0.4;
  const tLines = C.themes.map((T) => est((T.lead + "  " + T.text).length, tW, tPt));
  const tNeed = tLines.reduce((a, n) => a + n * lineH(tPt), 0);
  const tGap = Math.max(0.08, (bandH - 0.76 - tNeed) / C.themes.length);
  C.themes.forEach((T, i) => {
    const h = tLines[i] * lineH(tPt) + 0.04;
    s.addText([
      { text: T.lead + "  ", options: { bold: true, color: NAVY } },
      { text: T.text, options: { color: INK } },
    ], { x: xL + 0.2, y, w: tW, h, fontFace: BODY, fontSize: tPt, isTextBox: true, margin: 0, valign: "top" });
    y += h + tGap;
  });

  // Right top: what the investment looks like
  s.addShape("rect", { x: xR, y: top, w: wR, h: hA, fill: { color: GROUND }, line: { color: GROUND } });
  header(s, xR + 0.18, top + 0.15, rW, C.shape_title, "layers");
  y = top + 0.56;
  C.layers.forEach((L, i) => {
    const h = lLines[i] * lineH(rPt) + 0.02;
    s.addText([
      { text: L.name, options: { bold: true, color: NAVY } },
      { text: " (" + L.tag + "): ", options: { italic: true, color: MUTED } },
      { text: L.text, options: { color: INK } },
    ], { x: xR + 0.18, y, w: rW, h, fontFace: BODY, fontSize: rPt, isTextBox: true, margin: 0, valign: "top" });
    y += h + lGap;
  });

  // Right bottom: dependencies (accent)
  const yC = top + hA + 0.15;
  s.addShape("rect", { x: xR, y: yC, w: wR, h: hC, fill: { color: AMBER_BG }, line: { color: AMBER_BG } });
  header(s, xR + 0.18, yC + 0.13, rW, C.deps_title, "flag", AMBER);
  y = yC + 0.52;
  C.dependencies.forEach((D, i) => {
    const h = dLines[i] * lineH(rPt) + 0.02;
    s.addText([
      { text: D.lead + ".  ", options: { bold: true, color: AMBER } },
      { text: D.text, options: { color: INK } },
    ], { x: xR + 0.18, y, w: rW, h, fontFace: BODY, fontSize: rPt, isTextBox: true, margin: 0, valign: "top" });
    y += h + dGap;
  });

  // ---- snapshot table ----
  const ty = top + bandH + 0.14;
  const tblPt = 8, labW = 1.1, cw = (W - labW) / 4, cellW = cw - 0.14;
  const hdr = [{ text: C.snapshot_title, options: { bold: true, color: SLATE, fill: { color: GROUND }, fontSize: 9, fontFace: HEAD } }].concat(
    C.snapshot.cols.map((c) => ({ text: c.name, options: { bold: true, color: WHITE, fill: { color: NAVY },
      fontSize: 9.5, fontFace: HEAD } })));
  const rows = [hdr];
  const rowH = [0.26];
  C.snapshot.rows.forEach((rname, ri) => {
    const row = [{ text: rname, options: { bold: true, color: SLATE, fontSize: tblPt, fill: { color: GROUND } } }];
    let maxLines = 1;
    C.snapshot.cols.forEach((c) => {
      row.push({ text: c.cells[ri], options: { color: INK, fontSize: tblPt, fill: { color: WHITE } } });
      maxLines = Math.max(maxLines, est(c.cells[ri].length, cellW, tblPt));
    });
    rows.push(row);
    rowH.push(maxLines * lineH(tblPt) + 0.06);
  });
  s.addTable(rows, { x: M, y: ty, w: W, colW: [labW, cw, cw, cw, cw],
    fontFace: BODY, fontSize: tblPt, border: { type: "solid", color: LINE, pt: 0.5 },
    margin: [0.035, 0.06, 0.035, 0.06], valign: "top", autoPage: false, rowH });
  const tblBottom = ty + rowH.reduce((a, b) => a + b, 0);

  // ---- footer ----
  s.addText(C.footer, { x: M, y: Math.min(Math.max(tblBottom + 0.08, 6.9), 7.18), w: W, h: 0.24, fontFace: BODY, fontSize: 8, italic: true,
    color: MUTED, isTextBox: true, margin: 0, valign: "middle" });
  console.log("layout: bandH", bandH.toFixed(2), "table bottom", tblBottom.toFixed(2));

  // ---- speaker notes: Anshu's talking points ----
  s.addNotes(fs.readFileSync(__dirname + "/talking_points.txt", "utf8"));

  await pres.writeFile({ fileName: out });
  console.log("wrote", out);
}

if (require.main === module) build(process.argv[2] || "Zenith_Investment_Themes_CEO_onepager.pptx");
