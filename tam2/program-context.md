# TAM 2.0 — programme context

## What TAM 2.0 is

Post-merger platform-consolidation programme across **heritage Global Payments
(hGP)** and **heritage Worldpay (hWP)**. "TAM" = the target architecture model
("target architecture module/map" in speech; never expanded formally in these
materials). Jonathan Rigaud (JR) leads the sequencing effort; he presented TAM
2.0 target-state decisions to the ELT on ~2026-06-30, and the ELT asked for the
"now / next / later" — which is what the sequencing workshops produce.

North star: **single-in** (one integration front door: Global API / API 2.0) and
**single-out** (one merchant/partner experience: portal, reporting, billing,
disputes, payouts) per segment, with consolidated processing rails in between
(Global Gateway → RAFT/Core in NA, PowerZac/NAP in RoW).

Governing stance (JR, repeatedly): anything not on the sequencing pages is
subject to a start/stop/continue challenge — constrain development on
non-target platforms to free capacity for target work.

## Segments and workshop structure

Three segment workbooks, one sheet per geo/channel:

- **Enterprise** — NA; RoW (excl. LATAM)
- **Integrated** (platforms/ISV/payfac business) — NA; RoW
- **SMB** — UK&I; NA Direct / NA Wholesale / NA Indirect / NA ISO; RoW (excl. UK&I)

Grid columns (same across workbooks):
`Boulder` (capability family, numbered 1–8) → `Rock` (sub-capability) →
`Current Platforms` → `Build/Migrate/Decomm (Now)` → `Interim Platforms
(~H2 '27)` → `Build/Migrate/Decomm (Next)` → `Target Platforms (~2029)` →
notes/dependencies, plus business & corporate priorities columns.

Boulders: 1·Single-in, 2·Boarding, 3·Payment processing, 4·Sales & servicing,
5·VAS, 6·Single-out, 7·Data, 8·Infrastructure (where present).

The Integrated workbook adds a Sell / Support-Maintain / EOL framing for the
interim state. Consolidated per-boulder dependency rollups exist for Enterprise
NA (col P), Integrated NA (col K), SMB NA (`NA>>` sheet) and SMB RoW (`RoW>>`
sheet).

## Operating principles (Index sheet, all three workbooks)

1. **Payment flows are the critical path** — migrate merchants by moving how
   they are funded (BIN/ICA); boarding, servicing, CRM follow.
2. **No net-new on non-target platforms** (named: Evo/e-service, GMAS Europe,
   Greenhouse).
3. **Work on exiting platforms needs an exception** process.
4. **Parity is not the goal** — accept a small tail of capabilities never
   rebuilt before sunset.
5. **Consolidation is not decommissioning** — commit to switching platforms
   off so the estate actually shrinks.
6. **Resiliency scales with consolidation** — invest in resiliency,
   observability, fail-over on target platforms.

## Back-book migration considerations (Index sheet)

Funding windows must not shift; fixed pricing / interchange-plus cost must not
rise; segment the book by MCC and CP-vs-CNP volume and confirm capability usage
from data; statement transparency; re-papering generally not required & avoid
repeat CDD; merchant retraining (matters most for stable businesses); use the
migration to accelerate the homogenised data/statements work (BFS data
programme); settlement options may save money but can force re-papering;
account for banking relationships (HSBC, BOI); decide disposition of
third-party-gateway merchants (sell / migrate / other); e-commerce software
determines migratability; plan for trailing activity (chargebacks, refunds)
after migration.

## Key programme dates (as of 2026-07-07)

| When | What |
|---|---|
| 2026-07-02 | Segment sequencing workshops (SMB NA, SMB RoW, Integrated; Enterprise held same week) |
| 2026-07-13 | Curtis Landry in Australia — IntegraPay/TakePayments convergence mapping |
| ~2026-07-20 (wk) | JR in UK; follow-up with Lucy Anderson (APTM 1.0 remap for Australia) |
| 2026-07-20/21 | Cross-segment interdependency workshops: CRM, boarding+servicing, single-in/gateways, payment apps — segment-agnostic sequencing |
| 2026-07-24 | Board presentation — funding guidance for TAM (outside feature work; incremental funding ahead of '27 budget cycle) |
| Early Aug 2026 | Boarding deep-dive workshop with Maegan Cardillo's team (Utah); platforms represented (Soltan, Curtis) |
| 2026-09-21 | GPI SF.com → hCorp/USI Salesforce consolidation cutover (surcharging + auto-boarding enablement) |
| ~H2 2027 | Interim-platform state in the grids |
| ~2029 | Target-platform state in the grids |
