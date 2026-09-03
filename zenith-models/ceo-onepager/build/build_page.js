// Emit the one-pager as a static HTML artifact from content.js (single source of copy).
const fs = require("fs");
const C = require("./content.js");
const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

const themes = C.themes.map((t) =>
  `<li><strong>${esc(t.lead)}</strong> ${esc(t.text)}</li>`).join("\n");
const layers = C.layers.map((l) =>
  `<li><strong>${esc(l.name)}</strong> <em>(${esc(l.tag)})</em>: ${esc(l.text)}</li>`).join("\n");
const deps = C.dependencies.map((d) =>
  `<li><strong>${esc(d.lead)}.</strong> ${esc(d.text)}</li>`).join("\n");
const thead = C.snapshot.cols.map((c) => `<th scope="col">${esc(c.name)}</th>`).join("");
const tbody = C.snapshot.rows.map((r, i) =>
  `<tr><th scope="row">${esc(r)}</th>${C.snapshot.cols.map((c) => `<td>${esc(c.cells[i])}</td>`).join("")}</tr>`).join("\n");

const html = `<title>Zenith Investment Themes</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap">
<style>
  :root {
    --paper: #FFFFFF; --ink: #1F2933; --muted: #5B6B7C; --ground: #EEF1F5; --line: #D3D9E1;
    --navy: #1B2A4A; --slate: #3D5A80; --amber: #B8741A; --amber-bg: #FBF3E6; --head-bg: #1B2A4A; --head-fg: #FFFFFF;
    --serif: "Source Serif 4", "Cambria", Georgia, serif;
    --sans: "IBM Plex Sans", "Calibri", "Segoe UI", Arial, sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --paper: #111827; --ink: #E5EAF1; --muted: #9AA7B8; --ground: #1B2537; --line: #2E3B52;
      --navy: #C9D6EA; --slate: #9DB4D6; --amber: #E0A24A; --amber-bg: #2A2114; --head-bg: #2A3A5C; --head-fg: #F3F6FA;
    }
  }
  :root[data-theme="dark"] {
    --paper: #111827; --ink: #E5EAF1; --muted: #9AA7B8; --ground: #1B2537; --line: #2E3B52;
    --navy: #C9D6EA; --slate: #9DB4D6; --amber: #E0A24A; --amber-bg: #2A2114; --head-bg: #2A3A5C; --head-fg: #F3F6FA;
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--paper); color: var(--ink); font-family: var(--sans); font-size: 15px; line-height: 1.5; }
  .page { max-width: 1180px; margin: 0 auto; padding: 40px 32px 48px; }
  .eyebrow { font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--slate); font-weight: 600; margin: 0 0 10px; }
  h1 { font-family: var(--serif); font-weight: 700; font-size: clamp(22px, 2.6vw, 30px); line-height: 1.25; color: var(--navy); margin: 0 0 10px; text-wrap: balance; max-width: 34ch; }
  .sub { color: var(--muted); margin: 0 0 28px; font-size: 14px; }
  .band { display: grid; grid-template-columns: minmax(0, 1.55fr) minmax(0, 1fr); gap: 20px; align-items: start; }
  .panel { padding: 22px 24px; border-radius: 6px; }
  .panel.themes { border: 1px solid var(--line); background: var(--paper); }
  .panel.shape { background: var(--ground); }
  .panel.deps { background: var(--amber-bg); }
  .stack { display: grid; gap: 20px; }
  h2 { font-family: var(--serif); font-size: 18px; font-weight: 700; color: var(--navy); margin: 0 0 12px; display: flex; align-items: center; gap: 10px; }
  .panel.deps h2 { color: var(--amber); }
  h2 .dot { width: 12px; height: 12px; border-radius: 50%; background: currentColor; flex: none; }
  ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 12px; }
  li { max-width: 68ch; }
  li strong { color: var(--navy); font-weight: 600; }
  .panel.deps li strong { color: var(--amber); }
  li em { color: var(--muted); }
  .panel.shape li, .panel.deps li { font-size: 14px; }
  .snapshot { margin-top: 24px; }
  .snapshot h2 { color: var(--slate); }
  .tablewrap { overflow-x: auto; border: 1px solid var(--line); border-radius: 6px; }
  table { border-collapse: collapse; width: 100%; min-width: 820px; font-size: 13.5px; }
  th, td { text-align: left; vertical-align: top; padding: 10px 12px; border-bottom: 1px solid var(--line); }
  thead th { background: var(--head-bg); color: var(--head-fg); font-family: var(--serif); font-size: 14px; font-weight: 600; }
  tbody th { background: var(--ground); color: var(--slate); font-weight: 600; white-space: nowrap; width: 12ch; }
  tbody tr:last-child th, tbody tr:last-child td { border-bottom: 0; }
  .foot { margin-top: 20px; font-size: 12.5px; color: var(--muted); font-style: italic; max-width: 100ch; }
  @media (max-width: 900px) { .band { grid-template-columns: 1fr; } h1 { max-width: none; } }
  @media (prefers-reduced-motion: reduce) { * { scroll-behavior: auto; } }
</style>
<main class="page">
  <p class="eyebrow">${esc(C.eyebrow)}</p>
  <h1>${esc(C.headline)}</h1>
  <p class="sub">${esc(C.subtitle)}</p>

  <section class="band">
    <div class="panel themes">
      <h2><span class="dot"></span>${esc(C.themes_title)}</h2>
      <ul>
${themes}
      </ul>
    </div>
    <div class="stack">
      <div class="panel shape">
        <h2><span class="dot"></span>${esc(C.shape_title)}</h2>
        <ul>
${layers}
        </ul>
      </div>
      <div class="panel deps">
        <h2><span class="dot"></span>${esc(C.deps_title)}</h2>
        <ul>
${deps}
        </ul>
      </div>
    </div>
  </section>

  <section class="snapshot">
    <h2><span class="dot"></span>${esc(C.snapshot_title)}</h2>
    <div class="tablewrap">
      <table>
        <thead><tr><th scope="col"></th>${thead}</tr></thead>
        <tbody>
${tbody}
        </tbody>
      </table>
    </div>
  </section>

  <p class="foot">${esc(C.footer)}</p>
</main>
`;
fs.writeFileSync(__dirname + "/Zenith_Investment_Themes.html", html);
console.log("wrote Zenith_Investment_Themes.html");
