# Project Zenith — model build: QC findings & read-me

Prepared 31 Aug 2026 from: `Project_Zenith_Automation_workplan_and_data_requests_vS_1.xlsx`,
`20260828_Servicing_S2sizing_vDraft5.xlsb`, `Zenith_Business_Case_Template_by_Lever_1.xlsx`.

## What was delivered

One file per workstream, all built on the same chassis:

| File | Initiatives |
|---|---|
| `Zenith_SDLC_Models_and_WAVE_v1.xlsx` | SDLC-1 Agentic Loop Engineering; SDLC-2 PDLC Re-imagination |
| `Zenith_Sales_Models_and_WAVE_v1.xlsx` | SALES-1 Underwriting & Pricing — Front Book; SALES-2 SMB Long Tail — Partner |
| `Zenith_Servicing_Models_and_WAVE_v1.xlsx` | SVC-1 Contact Avoidance; SVC-2 Enhanced Chat/Self-Serve; SVC-3 Agentic Voice & AI Co-pilot; SVC-4 AI Workforce Mgmt; SVC-5 Back-Office Automation; SVC-6 Non-FTE Savings |

Each file: `Cover` (legend, deviations, open items) · `Instructions` (WAVE's own, untouched) ·
`Rate Card` (people-cost engine) · `Summary` (portfolio roll-up) · per initiative a `Model` sheet
formula-linked into its own `WAVE` sheet · pristine `Standard Template` at the end.

**Structure is parallel across all 12 initiative models**: §0 initiative & status → §1 sizing
assumptions → §2 benefit calculation → §3 ramp & phasing → §4 benefit feed rows ($M) →
§5 one-time investment (standard milestone people-cost table) → §6 recurring run costs →
§7 WAVE mapping → §8 flex/scratch. Model sheets share WAVE's time grid (L:P = FY2026–30,
T:CA = monthly Jan-26–Dec-30) so links are 1:1 and the WAVE monthly-vs-annual checks pass by
construction. All WAVE check counters (R1, CI1:CM1) are green in every sheet; LibreOffice full
recalc = 0 formula errors across ~50,400 formulas.

## Investment standard (consistent across every initiative)

- Milestone table exactly per spec: **Milestone | Assumptions | Team size | Billing months |
  Contingency Factor | Labor Costs** (+ Start month, Cap %, Rate override). Labor = team ×
  months × blended monthly rate × (1 + contingency). Contingency guide: Low 10% / Medium 15% /
  High 20% / Very high 50% (reference table on the Rate Card).
- Rate Card: rate basis switch (Yearly / Monthly / **Hourly = $/hr × 8 h/day × 21 d/mo**, all
  editable) + role table → **blended rate** per team member. Default team: 3 Eng, 2 QA, 1
  Architect, 1 PM, 1 Data Eng, 1 ML Eng, 1 Program Mgr (spare rows to add roles). Servicing's
  Rate Card uses the S2 8-FTE pod at $200k/yr so it ties to the S2 investment build exactly.
- On top of milestone labor, each model carries **PM 8%** and **contingency 10%** formula lines
  (the Servicing S2 standard) — Servicing one-time totals tie to S2 C2 row 35 to the cent.
- **Capitalization**: every milestone and non-labor line has a Cap % (defaults on the Rate Card)
  that splits spend into WAVE **CapEx** vs **OTC** rows automatically. SDLC/Sales default
  Build/Test = 80% (typical ASC 350-40 stance, flagged for Finance); Servicing defaults 0%
  because the S2 model is entirely cash/expensed — flip the policy cell when Finance confirms.
- Run phase: recurring run-cost table per model (token/inference w/ scales-with-ramp toggle,
  platform, run-team FTE × rate, vendor support, infra).
- Ramp: go-live date + months-to-full-run-rate, linear (the S2 convention). Annual = sum of
  monthly by construction.

## Servicing tie-out (seeded values vs S2 vDraft5 Base)

| Initiative | Annual benefit | One-time | Run cost |
|---|---|---|---|
| SVC-1 | $12,838,616 ✓ | $1,960,200 ✓ | $500k ✓ |
| SVC-2 | $14,771,230 ✓ | $2,504,700 ✓ | $2,340k ✓ |
| SVC-3 | $35,250,739 ✓ | $4,906,440 ✓ | $5,550k ✓ |
| SVC-4 | $7,654,450 ✓ | $3,536,280 ✓ | $1,350k ✓ |
| SVC-5 | $6,833,504 ✓ | $2,720,520 ✓ | $1,280k ✓ |
| SVC-6 | $4,039,547 ✓ | $0 ✓ | $0 ✓ |
| **Total** | **$81,388,085 ✓** | **$15,628,140 ✓** | **$11,020,000 ✓** |

Distillation: models run at difficulty-tier aggregates (back-office at workflow grain) with the
S2 waterfall openings as inputs; effective rates reproduce the 77-intent L2 engine exactly at
seed values. SVC-6's FTE inputs are live links to the other five models.

## QC findings — things wrong or at risk in the source materials

### A. Missing / mismatched inputs
1. **No SDLC or Sales model files were provided** — only the workplan. Those two workbooks are
   built from the workplan's data-POV/impact ranges: driver rates seeded (midpoints of stated
   ranges), baselines as explicit PENDING inputs (=0), so benefits read $0 until the baseline
   data requests land. If SDLC/Sales business-case v1 files exist (per W4 plan), send them and
   the baselines can be dropped in.
2. **Baseline reconciliations open (Servicing)**: S2 traces $156.0M front-office cost vs S1's
   $219.0M P&L view vs a $148M FP&A reference ("FP&A to confirm"); workplan cites 20.4M contacts
   vs S2's 37.7M offered (different basis); back-office covered is disputes-only $17.7M vs ~$41M
   workplan figure; FTE in scope 6.4k vs 7.8k total. All are documented in S2's bridge but must
   be closed before Finance sign-off.
3. **"AI coaching"** is named in board materials as one of the 6 accelerated areas, but the S2
   model has no coaching lever — it is re-scoped into co-pilot (3b) + routing (4a). Worth an
   explicit note in the S2 submission.

### B. Errors found in the WAVE standard template (fixed in our copies, documented on each Cover)
4. **K88 sign bug**: 'Recurring Benefits Total' run-rate column negates Revenue
   (`=SUM(-K68,K76,K84)`) while the annual columns sum straight — any revenue-bearing case
   (i.e. both Sales initiatives) would fail the template's own run-rate check. Fixed.
5. **Payback formula stalls** whenever a year's cumulative cash flow is exactly 0 — the
   template's own example shows "0 yrs" payback despite −$6.2M cumulative in 2027. Replaced
   with a robust per-year form (displays ">5" when payback isn't reached in the horizon).
6. **ROI cell divides the baseline column** (I117) by one-time cost instead of the run-rate NRB
   (K117); also #DIV/0! when blank. Fixed + IFERROR-guarded (IRR too).
7. **Row 79 monthly phasing is truncated** in the template (formulas stop Dec-2029 while the
   annual runs to 2030) — a latent check-failure trap. Our builds overwrite all 60 months, so
   not inherited.
8. The shipped **Business Case_Example fails its own checks** (CJ1=CK1=4: CAPEX row annual $5M
   in 2027 vs monthly $3M+$3M over 2027–28) and contains a rotten hidden dropdown block with 17
   `#REF!`s (also present on Instructions — cleared in our copies). The Example tab was dropped
   from the deliverables; Instructions (the annotated master) is kept.
9. Cosmetic: 'TTM TTM 6/1/26' double-label from a text period cell; row 103 in the costs block
   lacks check machinery (we avoid that row); template row 88/115 conventions differ.
10. One subtle deviation added for Excel-safety: on populated WAVE rows, the K "Ann. Run Rate"
   cell links the model's run-rate cell directly (J is derived from I and that same cell, so
   the arithmetic is identical). Recomputing K as I−J loses the last float bit and the
   template's own R-checks would flag spurious "Error"s in Excel (LibreOffice's fuzzy equality
   masks it).

### C. S2 model observations (no numeric errors found — it reconciles to the cent internally)
11. Cross-checked: C1=C2+C3 line-by-line; all lever headlines → Overall Summary; waterfall
    chains exactly; Summary-by-Intent ties to A0; Ramp aggregates 3a+3b and 4a+4b correctly.
    All 36 checks on its Checks tab pass. Two independent baseline builds differ −10.2%
    (inside its stated 25% tolerance; caused by missing L2 $/min data on ~half of
    messaging/email rows).
12. **Run cost is the least-evidenced area** (S2's own words): token/vendor lines are planning
    numbers under a $15M cap; no consumption forecasts. C2 "other one-time" lines have no
    documented basis. Build durations are not IO-validated; client costing sheet still pending.
13. **4a routing ceiling caveat**: PayPal's measured AHT spread (1.52×) is tighter than the
    1.7× GFCCP benchmark behind the 10% ceiling; S2's own check #33 says the ceiling should
    scale down and most intents run above the mix-shift cross-check. Least-defended $3.9M in
    the stack.
14. **3b co-pilot data faults**: after-call-work share is zero on every intent (the M10 split
    carries no ACW minutes despite the narrative claiming ACW moves furthest); 6 intents have
    talk-shares > 1; 5 intents ride flat fallback rates including the single largest voice
    benefit.
15. **Two FTE bases coexist**: "resource impacted" (A0 basis — used by the non-FTE flow-through,
    3,537 FTE total) vs residual-basis implied reduction (lower). Don't mix them when quoting
    headcount. (Models label which basis they carry.)
16. ~20% of the front-office base ($31.4M: NEI + unmappable "Others") is tiered ineligible for
    avoidance but still takes chat/voice/co-pilot benefit on tier-default rates — the
    lowest-confidence dollars in the stack.
16. Non-FTE lever applies one aggregate 55.2% share to every category, carries zero investment,
    and is excluded from S2's payback — confirm how Finance wants it treated in WAVE (it has its
    own model + WAVE sheet here so nothing is lost either way).
18. Minor S2 hygiene: Cover still says vDraft3 (Changelog says vDraft5); GCS Merchant outsourced
    pool is −$6,903; shrinkage target assumption is dormant in Base/Downside (only Upside banks
    it); the sensitivity table is a hard-coded snapshot.

### D. Workplan hygiene
19. Servicing master data-request log has empty Status/Date-received columns (status lives only
    in the priority-1 block and Dataset Links; e.g. FTE baseline is "Pending" while an OS-FTE
    file is already linked); priority-1 requests #7/#8 have no owner; Sales sheet stores
    "pending" strings in the date column; acronym glossary is missing WAVE, TM, FLC, GSA, DWH.

## How to use the flexibility that's built in

- Change any tier rate / driver / baseline on a Model sheet — WAVE, Summary, payback and NPV
  follow. WAVE check counters will catch anything that breaks phasing or run-rate consistency.
- Change rates or team mix on the Rate Card; type a per-milestone rate override where a
  milestone uses different people.
- Set capitalization: Rate Card policy cells (defaults documented), or per-line Cap % overrides.
- Ramp: go-live date + months to full run rate on each model (keep 100% reached before 2030 so
  the WAVE run-rate rule holds).
- Spare input rows and a flex section exist on every model sheet for owner refinements.

## Verification performed on the deliverables

- LibreOffice full recalculation: **0 formula errors** (SDLC 11,029 / Sales 11,821 / Servicing
  27,560 formulas).
- All WAVE internal checks green on all 10 initiative sheets (R1 = 0; CI1:CM1 = 0), with K vs
  2030 equality verified **bit-exact** so the checks also hold under Excel's exact comparison.
- Five independent adversarial review passes (formulas, S2 tie-outs, WAVE linkage, cross-file
  parallel structure) — all substantive findings fixed; Servicing benefits/one-time/run costs
  tie to the S2 model to the cent at seed values.
- Every model↔WAVE link verified row-by-row (labels, annual, monthly, baseline/goal columns);
  Summary sheets verified against WAVE Section IV metrics.
