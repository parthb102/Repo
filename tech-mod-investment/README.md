# Tech Modernization Investment — Triangulation Model

An interactive, single-file tool for structuring and defending the **one-time
(gross) investment ask** for a technology modernization & platform-consolidation
program, then bridging it to the **net** funding ask the investment committee sees.

Built for the profile in the EPA/QuantumBlack thread:

| Anchor | Value |
|---|---|
| Revenue | ~$10B |
| Technology spend | ~$1B (~10% of revenue) |
| Application estate | ~700 applications |
| Savings target | ~$250M run-rate (~2.5pp of revenue) |
| Tech workforce | ~13K FTE + ~10K contractors (~23K equivalent) |
| Horizon | 5 years |

## How to use it

Open `index.html` in any browser — no install, no build, no network needed.
Everything recalculates live as you drag a slider or edit a number. Use
**Export / Print** to drop it into a deck or PDF.

- **Scenario presets** (Lean / Base / Ambitious) move the cost-driver factors
  together for quick goalposts. Company anchors (revenue, spend, apps) stay fixed.
- **Include / exclude** any approach from the triangulation with its checkbox.
- **Distribution logic** toggles the 5-year funding profile (S-curve, front-,
  back-loaded, even, or custom weights).

## The triangulation logic

The number is built from **four independent lenses**, each sized against a
**different anchor** — so the answer can't be an artifact of any single
assumption. Two are top-down, two are bottom-up.

| Lens | Approach | Anchored to | Base output |
|---|---|---|---|
| Top-down A | Investment-to-savings multiple (payback) | $250M run-rate | $625M |
| Top-down B | Share of IT budget reinvested | $1B annual spend | $650M |
| Bottom-up A | 6Rs per-application disposition costing | 700-app estate | $714M |
| Bottom-up B | Delivery capacity & effort (+ GenAI uplift) | ~23K workforce | $717M |

**Base case triangulates to ~$677M gross** (range $625–717M across the four).

### Top-down A — Investment-to-savings multiple
Programs are underwritten against the run-rate savings they unlock. Large
efficiency-led IT modernization typically needs a gross investment of ~2–3× the
annual run-rate (a 2–3yr simple payback before phasing).
`gross = run-rate savings × multiple`

### Top-down B — Share of IT budget reinvested
During active transformation, leading firms ring-fence an elevated slice of the
IT budget for modernization (~10–18% of annual spend, on top of run-the-bank)
for the program's duration.
`gross = annual tech spend × horizon × modernization %`

### Bottom-up A — 6Rs per-application disposition costing
The Gartner/cloud-migration framework (also described by D. Cheida in the
thread). Segment the estate by disposition and apply a blended fully-loaded unit
cost per app (the unit cost bakes in the S/M/L size mix), then add program
overhead (EA, integration, data, security, PMO, cloud foundation).
`gross = Σ(apps × mix% × unit cost × complexity) × (1 + overhead%)`

Typical fully-loaded per-app ranges used as defaults:

| Disposition | $M / app |
|---|---|
| Retire (decommission) | 0.1–0.2 |
| Retain (low/no touch) | ~0.04 |
| Rehost (lift & shift) | 0.2–0.4 |
| Replatform | 0.5–1.0 |
| Repurchase (SaaS) | 1–2 |
| Refactor / rewrite | 2–5 |

### Bottom-up B — Delivery capacity & effort
Build from engineering effort: blended delivery capacity (internal + offshore +
SI/vendor) dedicated to modernization, sustained across the horizon, plus
non-labor (cloud, licenses, tooling, AI tokens), net of a GenAI productivity
benefit on eligible work (C. Barreto's build + token point).
`gross = FTE-equiv × horizon × loaded rate × (1 + non-labor%) × (1 − GenAI%)`

## Gross → Net bridge

> The number to come up with is the **gross**, not the net.

The model produces gross, then deducts **self-funding** to reach the net ask:

1. **Capacity released from non-target sunsets** — retiring non-target apps frees
   run/maintain capacity that is redeployed to target-state build (~60% of self-funding).
2. **Run-rate savings realized in-flight** — savings banked during the build,
   before steady state (~40%).

`net ask = gross × (1 − self-funding%)`

At the base **26%** self-funding, the **$677M gross** bridges to a **~$501M net**
ask — i.e. the net figure falls out of the independent logic rather than being
anchored to. Self-funding is deliberately **back-weighted** (savings ramp late),
so the net cash ask is more front-loaded than gross spend.

## 5-year funding profile

Gross is distributed across five years by the selected distribution logic;
self-funding is applied on a back-weighted realization curve. The result shows,
per year: gross spend, self-funded portion, net cash ask, and cumulative net.
Under the base S-curve, gross spend peaks in Year 3 while the **net cash ask
peaks earlier and tapers** as the program self-funds.

## Defensibility

The four lenses converge in a tight band from genuinely different starting
points, which is the argument: the order of magnitude is robust, not method-bound.
Every factor is editable, so the assumption set can be pressure-tested live in
the room. Ranges here are industry orders of magnitude for **structuring the
ask** — replace the unit costs and disposition mix with client-specific data
from the application-discovery exercise (dependencies, integrations, LoC/
complexity sizing) as it lands.

---
*All figures are illustrative and fully editable. Not a substitute for portfolio
discovery.*
