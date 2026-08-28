# Worked example — sizing an AI business case (Data Scientist)

`ds-sizing-example.pptx` contains the worked sizing example, the AI reviewer checklist, and an assumptions backup:

- **Slide 1** — the worked example page.
  - Left: sizing the benefit bottom-up — cost base (200 FTEs × $190K = $38M) → activity map with per-activity AI addressability → viability and capture haircuts down to ~$8.3M capturable → easy-first prioritization.
  - Right: sizing the investment for opportunity No. 1 (Data Prep & Quality Agent) — four phases (Plan / Build / Pilot / Deploy & Scale, ≈32 weeks), team and cost per phase, one-time ($0.95M) vs recurring ($585K/yr, tokens modeled explicitly), and returns (~$3.3M/yr steady state, ~5× running return).
- **Slide 2** — the AI reviewer checklist: five gates (AI creates the value, value math holds, full AI cost in, tech pressure-tested, standard stack) with what must be true and send-back triggers.
- **Slide 3** — backup: the assumptions behind every number, meant to be replaced with a real role's data before reuse.

All figures are illustrative. Rebuild with `node build_deck.js` (requires `pptxgenjs`).
