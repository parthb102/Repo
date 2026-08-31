#!/usr/bin/env python3
"""Build Zenith_Servicing_Models_and_WAVE_v1.xlsx — 6 initiatives distilled
from the S2 sizing model (vDraft5), formula-linked into WAVE templates.

Tie-out targets (S2 Base scenario, verified against the source to the cent):
  SVC-1 12,838,616 | SVC-2 14,771,230 | SVC-3 35,250,739 | SVC-4 7,654,450 |
  SVC-5 6,833,504 | SVC-6 4,039,547 | TOTAL 81,388,085
  One-time 15,628,140 | Run 11,020,000
"""
import openpyxl
from framework import (FMT_USD, FMT_PCT, FMT_PCT0, FMT_NUM, FMT_NUM1, FMT_USDM,
                       TEMPLATE_PATH, f, fill, col, WHITE, DARKBLUE_FILL,
                       BORDER_ALL)
from builders import build_rate_card, build_cover
from builders2 import ModelBuilder, fill_wave, build_summary
from common import STD_DEVIATIONS, LINKING_NOTES

S2 = "Servicing S2 sizing model vDraft5 (28 Aug 2026), Base scenario. "

RC_DEFAULTS = dict(
    basis="Yearly",
    hours_day=8, days_month=21,
    roles=[
        ("Product Owner", 1, 200000),
        ("PM / Scrum Master", 1, 200000),
        ("Tech Lead", 1, 200000),
        ("AI Engineer", 2, 200000),
        ("DevOps Engineer", 1, 200000),
        ("QA Engineer", 1, 200000),
        ("FA / UX", 1, 200000),
    ],
    cap_pcts={"Plan / Design": 0.0, "Build / Test": 0.0,
              "Pilot / Change Mgmt.": 0.0, "Scale / Run": 0.0},
    cap_nonlabor=0.0,
    notes=[
        "Roles = the S2 model's standard 8-FTE build pod; every role priced at the S2 blended loaded "
        "delivery rate of $200,000/yr, so the blended rate ties to the S2 investment build exactly. "
        "Differentiate role rates here once the client rate card arrives (C1–C3 were designed for a "
        "rate-card drop-in).",
        "Milestone contingency of 10% in the initiative models = the S2 'risk adjustment on delivery "
        "labour'. PM (8%) and contingency (10%) uplifts are separate formula lines in each model's "
        "one-time non-labor table — total one-time per initiative ties to S2 C2 row 35.",
        "Capitalization defaults are 0% because the S2 model treats all one-time spend as cash/expensed "
        "(no CapEx split anywhere in C1–C3). Set Build/Test cap % here (e.g. 80%) once Finance confirms "
        "treatment — the CapEx/OTC split then flows to the WAVE sheets automatically.",
        "Run-team labor sits in each model's recurring run-cost table at $180,000/FTE/yr (S2 run rate).",
    ],
)

COMMON_SOURCES = [
    S2 + "Distilled to tier level; per-tier eligible bases and effective rates reproduce the S2 "
    "L2-intent engine output exactly (verified).",
    "Workplan: 'Project Zenith Automation workplan and data requests vS_1.xlsx', Servicing tabs",
]

WATERFALL_NOTE = ("Opening cost follows the S2 stacking waterfall (each lever opens on the prior "
                  "lever's closing baseline; order: 1 Avoidance → 2 Chat → 3a Voice → 3b Co-pilot → "
                  "4a SBR → 4b Utilisation). Tier-level bases below are snapshots of the S2 L2 engine — "
                  "refresh them from the S2 model if upstream levers or tiering change.")


# ---------------------------------------------------------------- helpers
def tier_table(mb, title, rows, prefix, rate_note="", fte=False):
    """rows: (tier, eligible_cost, eff_rate, note[, fte_open])"""
    sw = mb.sw
    sw.cell(sw.r, 2, title, f(bold=True, size=10, color="FF1F3864"))
    sw.skip(1)
    hr = sw.r
    heads = [(2, "Tier"), (4, "Eligible cost base ($/yr)"), (6, "Effective rate"),
             (8, "Benefit ($/yr)")]
    if fte:
        heads += [(10, "FTE base"), (11, "FTE released")]
    for c, h in heads:
        sw.cell(hr, c, h, f(bold=True, size=9, color=WHITE), fl=DARKBLUE_FILL,
                wrap=True, align="center")
    sw.cell(hr, 13, rate_note, f(italic=True, size=8, color="FF808080"), wrap=True)
    mb.ws.row_dimensions[hr].height = 26
    sw.skip(1)
    first = sw.r
    for k, row in enumerate(rows, start=1):
        tier, cost, rate, note = row[:4]
        r = sw.r
        sw.cell(r, 2, tier, f(bold=True), border=BORDER_ALL)
        sw.input_cell(r, 4, cost, num=FMT_USD)
        sw.input_cell(r, 6, rate, num=FMT_PCT)
        sw.formula_cell(r, 8, f"=D{r}*F{r}", num=FMT_USD)
        if note:
            sw.cell(r, 13, note, f(italic=True, size=8, color="FF595959"))
        if fte:
            sw.input_cell(r, 10, row[4], num=FMT_NUM1)
            sw.formula_cell(r, 11, f"=J{r}*F{r}", num=FMT_NUM1)
        mb.sym[f"{prefix}_r{k}_base"] = f"$D${r}"
        sw.skip(1)
    last = sw.r - 1
    r = sw.r
    sw.cell(r, 2, "Subtotal — " + title.split("(")[0].strip(), f(bold=True))
    sw.formula_cell(r, 4, f"=SUM(D{first}:D{last})", num=FMT_USD)
    sw.formula_cell(r, 8, f"=SUM(H{first}:H{last})", num=FMT_USD)
    if fte:
        sw.formula_cell(r, 11, f"=SUM(K{first}:K{last})", num=FMT_NUM1)
        sw.formula_cell(r, 10, f"=SUM(J{first}:J{last})", num=FMT_NUM1)
        mb.sym[prefix + "_fte"] = f"$K${r}"
        mb.sym[prefix + "_fteb"] = f"$J${r}"
    mb.sym[prefix + "_base"] = f"$D${r}"
    mb.sym[prefix + "_ben"] = f"$H${r}"
    sw.skip(2)


def runteam(fte, note=""):
    return dict(label="OPEX - Run team (keep-the-lights-on)", annual=None, fte=fte, notes=note)


# ================================================================= SVC-1
SVC1 = dict(
    code="SVC-1",
    short="Contact Avoidance",
    name="Prevent avoidable contacts at source through product fixes and upstream journey improvements",
    model_sheet="SVC-1 Model", wave_sheet="SVC-1 WAVE",
    workstream="Servicing (ELT sponsor: Aaron | WSL: Tahira | IOs: Jackie Yu, Matt Anderson, Bob Hurst)",
    owner="Servicing IO — TBC (pool: Jackie Yu, Matt Anderson, Bob Hurst)",
    bu="Global Servicing",
    status="Seeded 1:1 from S2 vDraft5 (Base) — benefit ties to $12.84M",
    golive=(2027, 8), ramp_months=6, tab_color="70AD47",
    sources=COMMON_SOURCES,
    open_items=[
        "Tier rates are the S2 assumptions (Easy 20% / Medium 10% / Hard 5% of eligible contacts); "
        "scenario variants in S2: Upside 28/18/8, Downside 12/7/3.",
        "$31.4M of opening cost is ineligible (NEI + unmappable 'Others' + no-product-fix rows) — "
        "~20% of the front-office base carries zero avoidance benefit; upside if taxonomy improves.",
        "S2 contact baseline is 37.7M offered contacts annualized from 7 months (x12/7), ~5% above the "
        "$148M FP&A reference — FP&A to confirm; workplan cites a different 20.4M baseline (basis differs).",
    ],
    assumptions=[
        ("#SUB", "Opening baseline (S2 waterfall position: first lever, opens on A0 baseline)"),
        ("open_cost", "Opening front-office cost baseline", 156024536.40, "$/yr", FMT_USD,
         S2 + "A0 intent cost baseline (annualized 7-mo actuals x 12/7). " + WATERFALL_NOTE),
        ("#SUB", "Investment uplifts (S2 standard)"),
        ("pm_pct", "Programme management, % of build", 0.08, "%", FMT_PCT0, "S2 COST_PMO"),
        ("cont_pct", "Contingency, % of build incl. PM", 0.10, "%", FMT_PCT0, "S2 COST_CONT"),
        ("run_fte", "Run team headcount", 2.0, "# FTE", FMT_NUM1, "S2 C3: keep-the-lights-on"),
        ("run_rate", "Run team loaded rate", 180000, "$/FTE/yr", FMT_USD, "S2 COST_RUN_RATE"),
    ],
    custom_section=lambda mb: tier_table(
        mb, "Eligible opening cost by difficulty tier (S2 Intent Tiering, avoidance column)",
        [("Easy (12 L2 intents)", 15982019.63, 0.20, "S2 rate: 20% of contacts avoidable", 738.162),
         ("Medium (43 L2 intents)", 84197499.77, 0.10, "S2 rate: 10%", 3579.664),
         ("Hard (19 L2 intents)", 24449245.62, 0.05, "S2 rate: 5%", 705.871),
         ("Ineligible (NEI / unmappable / no product fix)", 31395771.38, 0.0,
          "H='No' rows + NEI + 'Others' — no benefit booked", 897.612)],
        "t1", rate_note="Rates = S2 tier assumptions (CA_*). Bases = S2 eligible opening cost "
                        "aggregated from the 77-intent engine.", fte=True),
    calc=[
        ("ben_total", "Total annual benefit (steady state)", "={t1_ben}", "$/yr", FMT_USD,
         "Ties to S2 A1 benefit $12,838,616"),
        ("fte_out", "FTE impacted (feeds Non-FTE model SVC-6)", "={t1_fte}", "# FTE", FMT_NUM1,
         "Ties to S2: 540.9 FTE"),
        ("closing", "Closing cost (hand-off baseline to SVC-2)", "={open_cost}-{ben_total}",
         "$/yr", FMT_USD, "S2: $143,185,920"),
    ],
    benefit_lines=[
        dict(label="OPEX - Front-office cost reduction (avoided contacts)", category="opex",
             runrate="{ben_total}", baseline="={open_cost}/1000000",
             comment="Eligible cost x tier avoidance rates (S2 tier engine, distilled)"),
    ],
    runcost_lines=[
        dict(label="OPEX - Run team (keep-the-lights-on)", annual="={run_fte}*{run_rate}",
             scale="N", start=(2027, 8), notes="S2 C3: 2.0 FTE x $180k"),
        dict(label="OPEX - Vendor support & maintenance", annual=100000, scale="N", start=(2027, 8),
             notes="S2 C3 planning number"),
        dict(label="OPEX - Incremental infrastructure", annual=40000, scale="N", start=(2027, 8),
             notes="S2 C3 planning number"),
    ],
    milestones={
        "Plan / Design": dict(assump="S2 build shape: design team of 4 for 2 months. Durations are "
                                     "the S2 assumption, not IO-validated delivery plans.",
                              team=4, months=2, cont=0.10, start=(2027, 1)),
        "Build / Test": dict(assump="S2: one 8-FTE pod (PO, PM/Scrum, Tech Lead, 2 AI Eng, DevOps, QA, "
                                    "FA/UX) for 5 months.",
                             team=8, months=5, cont=0.10, start=(2027, 3)),
        "Pilot / Change Mgmt.": dict(assump="S2 scale-up & rollout: 5 FTE (product roles step down) for "
                                            "6 months — drives the benefit ramp.",
                                     team=5, months=6, cont=0.10, start=(2027, 8)),
        "Scale / Run": dict(assump="Run-phase support carried as recurring run cost (Section 6) — "
                                   "S2 treats run as a consolidated run team.",
                            team=0, months=0, cont=0.10, start=(2028, 2)),
    },
    onetime_nonlabor=[
        dict(label="Platform and licence set-up", total=0, months=2, start=(2027, 3), cap=0.0,
             notes="S2 C2 planning number ($0 for this initiative)"),
        dict(label="Hardware and infrastructure", total=120000, months=5, start=(2027, 3), cap=0.0,
             notes="S2 C2 planning number — no basis documented in S2; validate"),
        dict(label="Integration connectors", total=60000, months=5, start=(2027, 3), cap=0.0,
             notes="S2 C2 planning number"),
        dict(label="Cloud compute for build & evaluation", total=40000, months=5, start=(2027, 3), cap=0.0,
             notes="S2 C2 planning number"),
        dict(label="Programme management (8% of build)",
             total="={pm_pct}*({MS_TOTAL}+{NL:1}+{NL:2}+{NL:3}+{NL:4})", months=13, start=(2027, 1),
             cap=0.0, notes="S2 standard: 8% x (delivery labour + other one-time)"),
        dict(label="Contingency (10% of build incl. PM)",
             total="={cont_pct}*({MS_TOTAL}+{NL:1}+{NL:2}+{NL:3}+{NL:4}+{NL:5})", months=13,
             start=(2027, 1), cap=0.0, notes="S2 standard: 10% x subtotal incl. PM. "
             "Total one-time ties to S2: $1,960,200"),
    ],
    wave_driver=dict(
        baseline=[
            ("Front-office servicing cost baseline (annualized)", "={S:open_cost}/1000000", "$USD M",
             "Jan–Jul 2026 x 12/7", FMT_USDM),
            ("Eligible base (Easy+Medium+Hard tiers)",
             "=({S:open_cost}-{S:t1_r4_base})/1000000", "$USD M", "same", FMT_USDM),
            ("Implied front-office FTE (S2 A0)", "={S:t1_fteb}", "# FTE", "same", FMT_NUM1),
        ],
        goal=[
            ("Blended avoidance rate on opening cost", "={S:ben_total}/{S:open_cost}", "%",
             "Steady state", FMT_PCT),
            ("FTE impacted", "={S:fte_out}", "# FTE", "Steady state", FMT_NUM1),
        ],
        incr=[("Annual benefit (run rate)", "={S:ben_total}/1000000", "$USD M", None, FMT_USDM)],
    ),
)

# ================================================================= SVC-2
SVC2 = dict(
    code="SVC-2",
    short="Enhanced Chat / Self-Serve",
    name="Enhanced chat and self-serve containment on messaging and email demand",
    model_sheet="SVC-2 Model", wave_sheet="SVC-2 WAVE",
    workstream=SVC1["workstream"], owner=SVC1["owner"], bu="Global Servicing",
    status="Seeded 1:1 from S2 vDraft5 (Base) — benefit ties to $14.77M",
    golive=(2027, 9), ramp_months=7, tab_color="70AD47",
    sources=COMMON_SOURCES,
    open_items=[
        "Voice channel is out of scope for this lever (S2 channel gate: chat acts on messaging + email "
        "only — $39.0M of the $143.2M opening baseline).",
        "Effective rates embed the S2 ceiling logic (target containment capped at 90% of demand) and the "
        "30% funnel-hardening haircut — underlying target rates: Easy 50% / Medium 40% / Hard 20% of "
        "escalated demand.",
        "S2 books nothing where current PPA containment already beats the tier ceiling (2 intents).",
    ],
    assumptions=[
        ("#SUB", "Opening baseline (S2 waterfall: opens on SVC-1 closing)"),
        ("open_cost", "Opening cost baseline (all channels)", 143185920.21, "$/yr", FMT_USD,
         S2 + WATERFALL_NOTE),
        ("#SUB", "Investment uplifts (S2 standard)"),
        ("pm_pct", "Programme management, % of build", 0.08, "%", FMT_PCT0, None),
        ("cont_pct", "Contingency, % of build incl. PM", 0.10, "%", FMT_PCT0, None),
        ("run_fte", "Run team headcount", 3.0, "# FTE", FMT_NUM1, "S2 C3"),
        ("run_rate", "Run team loaded rate", 180000, "$/FTE/yr", FMT_USD, None),
        ("fte_out", "FTE impacted (A0 basis — feeds SVC-6)", 867.7176, "# FTE", FMT_NUM1,
         "S2 A2 'Resource impacted' (V column, A0 basis). Residual-basis reduction is 779.7 — "
         "S2 uses the A0 basis in the non-FTE flow-through; refresh from S2 if rates change"),
    ],
    custom_section=lambda mb: tier_table(
        mb, "Eligible opening cost by tier — messaging + email channels only (S2 chat-tier column)",
        [("Easy (68 L2 intents)", 27286882.49, 0.4311128666,
          "S2 target 50% of escalated demand; ceiling 90% binds on many rows -> effective 43.1%"),
         ("Medium (6 L2 intents)", 3525444.71, 0.3886586988, "S2 target 40%; effective 38.9% after ceiling/hardening"),
         ("Hard (3 L2 intents)", 8186544.37, 0.20000, "S2 target 20%")],
        "t2", rate_note="Effective rates implied from the S2 engine (benefit / eligible base per tier) — "
                        "they bundle target rate, 90% containment ceiling and funnel hardening. "
                        "Edit to test different containment ambitions."),
    calc=[
        ("ben_total", "Total annual benefit (steady state)", "={t2_ben}", "$/yr", FMT_USD,
         "Ties to S2 A2 benefit $14,771,230"),
        ("closing", "Closing cost (hand-off baseline to SVC-3)", "={open_cost}-{ben_total}",
         "$/yr", FMT_USD, "S2: $128,414,690"),
    ],
    benefit_lines=[
        dict(label="OPEX - Front-office cost reduction (chat/self-serve containment)", category="opex",
             runrate="{ben_total}", baseline="={open_cost}/1000000",
             comment="Messaging+email eligible cost x tier containment rates (S2 engine, distilled)"),
    ],
    runcost_lines=[
        dict(label="OPEX - Inference & token consumption", annual=1200000, scale="Y", start=(2027, 9),
             notes="S2 C3 planning assumption — replace with consumption forecast; scales with ramp"),
        dict(label="OPEX - AI platform subscription", annual=300000, scale="N", start=(2027, 9),
             notes="S2 C3 planning number"),
        dict(label="OPEX - Run team (keep-the-lights-on)", annual="={run_fte}*{run_rate}",
             scale="N", start=(2027, 9), notes="S2 C3: 3.0 FTE x $180k"),
        dict(label="OPEX - Vendor support & maintenance", annual=200000, scale="N", start=(2027, 9),
             notes="S2 C3 planning number"),
        dict(label="OPEX - Incremental infrastructure", annual=100000, scale="N", start=(2027, 9),
             notes="S2 C3 planning number"),
    ],
    milestones={
        "Plan / Design": dict(assump="S2 build shape: 4 FTE x 2 months.", team=4, months=2, cont=0.10,
                              start=(2027, 1)),
        "Build / Test": dict(assump="S2: 8-FTE pod x 6 months.", team=8, months=6, cont=0.10,
                             start=(2027, 3)),
        "Pilot / Change Mgmt.": dict(assump="S2 scale-up: 5 FTE x 7 months.", team=5, months=7,
                                     cont=0.10, start=(2027, 9)),
        "Scale / Run": dict(assump="Run-phase support in Section 6 run costs.", team=0, months=0,
                            cont=0.10, start=(2028, 4)),
    },
    onetime_nonlabor=[
        dict(label="Platform and licence set-up", total=80000, months=2, start=(2027, 3), cap=0.0,
             notes="S2 C2 planning number"),
        dict(label="Hardware and infrastructure", total=180000, months=6, start=(2027, 3), cap=0.0,
             notes="S2 C2 planning number"),
        dict(label="Integration connectors", total=120000, months=6, start=(2027, 3), cap=0.0,
             notes="S2 C2 planning number"),
        dict(label="Cloud compute for build & evaluation", total=60000, months=6, start=(2027, 3), cap=0.0,
             notes="S2 C2 planning number"),
        dict(label="Programme management (8% of build)",
             total="={pm_pct}*({MS_TOTAL}+{NL:1}+{NL:2}+{NL:3}+{NL:4})", months=15, start=(2027, 1),
             cap=0.0, notes="S2 standard"),
        dict(label="Contingency (10% of build incl. PM)",
             total="={cont_pct}*({MS_TOTAL}+{NL:1}+{NL:2}+{NL:3}+{NL:4}+{NL:5})", months=15,
             start=(2027, 1), cap=0.0, notes="Total one-time ties to S2: $2,504,700"),
    ],
    wave_driver=dict(
        baseline=[
            ("Opening cost baseline (post contact-avoidance)", "={S:open_cost}/1000000", "$USD M",
             "Post-upstream levers (S2 waterfall)", FMT_USDM),
            ("In-scope base (messaging + email)", "=({S:t2_base})/1000000", "$USD M", "same", FMT_USDM),
        ],
        goal=[
            ("Blended containment uplift on in-scope base", "={S:ben_total}/{S:t2_base}", "%",
             "Steady state", FMT_PCT),
            ("FTE impacted (A0 basis)", "={S:fte_out}", "# FTE", "Steady state", FMT_NUM1),
        ],
        incr=[("Annual benefit (run rate)", "={S:ben_total}/1000000", "$USD M", None, FMT_USDM)],
    ),
)

# ================================================================= SVC-3
def svc3_tables(mb):
    tier_table(
        mb, "S2 lever 3a — Agentic voice: voice-channel eligible cost by tier (voice-tier column)",
        [("Easy (27 L2 intents)", 22606259.48, 0.3594869467,
          "S2 target 40% of escalated voice demand; 80% ceiling + hardening -> effective 35.9%"),
         ("Medium (37 L2 intents)", 51560921.72, 0.2801101240, "S2 target 30%; effective 28.0%"),
         ("Hard (13 L2 intents)", 30019867.43, 0.1458922896, "S2 target 15%; effective 14.6%")],
        "t3a", rate_note="Voice channel only (messaging/email pass through). Effective rates implied "
                         "from the S2 engine — bundle target rate, 80% ceiling, funnel hardening.")
    tier_table(
        mb, "S2 lever 3b — AI co-pilot: voice residual (post-3a) cost by tier",
        [("Easy", 14479604.28, 0.1003572774, "Component-built: talk 10% + hold 35% x M10 minute shares, x hardening"),
         ("Medium", 37118185.55, 0.0777708163, "talk 8% / hold 30% components"),
         ("Hard", 25640200.24, 0.0615047249, "talk 5% / hold 20% components; 5 intents on flat fallback rates")],
        "t3bv", rate_note="Handle-time reduction on contacts that still reach an agent (voice).")
    tier_table(
        mb, "S2 lever 3b — AI co-pilot: text (messaging + email) cost by tier",
        [("Easy", 3311158.85, 0.1286418213, "S2 flat text rate 15% x hardening"),
         ("Medium", 12792360.67, 0.1052458323, "S2 flat 12%"),
         ("Hard", 8124122.30, 0.0753984194, "S2 flat 8%")],
        "t3bt", rate_note="Text handled-cost reduction (blended rate per tier).")

SVC3 = dict(
    code="SVC-3",
    short="Agentic Voice & AI Co-pilot",
    name="Agentic AI voice — end-to-end contact resolution plus AI co-pilot agent assist",
    model_sheet="SVC-3 Model", wave_sheet="SVC-3 WAVE",
    workstream=SVC1["workstream"], owner=SVC1["owner"], bu="Global Servicing",
    status="Seeded 1:1 from S2 vDraft5 (Base) — benefit ties to $35.25M (3a $26.95M + 3b $8.30M)",
    golive=(2027, 9), ramp_months=8, tab_color="70AD47",
    sources=COMMON_SOURCES,
    open_items=[
        "S2 splits this initiative into 3a (contact resolution/abatement, voice only) and 3b (co-pilot "
        "handle-time reduction on residual + text); check #9 in S2 enforces that they sum to the "
        "combined voice benefit. Both sub-levers modeled below; WAVE carries them as two benefit lines.",
        "3b QC from S2: after-call-work share is zero on every intent (M10 split carries no ACW minutes) "
        "— co-pilot voice rates are built from talk+hold only; 6 intents have talk shares >1 (data "
        "fault); 5 intents ride flat fallback rates incl. the largest single voice benefit ($0.7M).",
        "Sensitivity (S2): voice resolution rates ±30% swing total benefit $13.5M — largest driver in "
        "the model.",
    ],
    assumptions=[
        ("#SUB", "Opening baselines (S2 waterfall: 3a opens on SVC-2 closing; 3b on 3a closing)"),
        ("open_3a", "Opening cost — 3a (all channels)", 128414690.45, "$/yr", FMT_USD, S2 + WATERFALL_NOTE),
        ("open_3b", "Opening cost — 3b (post-3a residual)", 101465631.88, "$/yr", FMT_USD,
         "Equals 3a closing; refresh if 3a changes"),
        ("#SUB", "Investment uplifts (S2 standard)"),
        ("pm_pct", "Programme management, % of build", 0.08, "%", FMT_PCT0, None),
        ("cont_pct", "Contingency, % of build incl. PM", 0.10, "%", FMT_PCT0, None),
        ("run_fte", "Run team headcount (3a + 3b consolidated)", 5.5, "# FTE", FMT_NUM1,
         "S2 C3: 3.0 (3a) + 2.5 (3b)"),
        ("run_rate", "Run team loaded rate", 180000, "$/FTE/yr", FMT_USD, None),
        ("fte_3a", "FTE impacted — 3a (A0 basis, feeds SVC-6)", 1017.2846, "# FTE", FMT_NUM1,
         "S2 A3a V102"),
        ("fte_3b", "FTE impacted — 3b (A0 basis, feeds SVC-6)", 528.2645, "# FTE", FMT_NUM1,
         "S2 A3b V102"),
    ],
    custom_section=svc3_tables,
    calc=[
        ("ben_3a", "Benefit — S2 lever 3a (agentic voice resolution)", "={t3a_ben}", "$/yr", FMT_USD,
         "Ties to S2: $26,949,059"),
        ("ben_3b", "Benefit — S2 lever 3b (AI co-pilot, voice + text)", "={t3bv_ben}+{t3bt_ben}", "$/yr", FMT_USD,
         "Ties to S2: $8,301,681"),
        ("ben_total", "Total annual benefit (steady state)", "={ben_3a}+{ben_3b}", "$/yr", FMT_USD,
         "Ties to S2 combined: $35,250,739"),
        ("fte_out", "FTE impacted total (feeds SVC-6)", "={fte_3a}+{fte_3b}", "# FTE", FMT_NUM1, None),
        ("closing", "Closing cost (hand-off baseline to SVC-4)", "={open_3b}-{ben_3b}", "$/yr", FMT_USD,
         "S2: $93,163,951"),
    ],
    benefit_lines=[
        dict(label="OPEX - Agentic voice contact resolution (3a)", category="opex",
             runrate="{ben_3a}", baseline="={open_3a}/1000000",
             comment="Voice-eligible cost x tier resolution rates (S2 engine, distilled)"),
        dict(label="OPEX - AI co-pilot handle-time reduction (3b)", category="opex",
             runrate="{ben_3b}", baseline="={open_3b}/1000000",
             comment="Talk/hold component rates on voice residual + flat text rates"),
    ],
    runcost_lines=[
        dict(label="OPEX - Inference & token consumption", annual=3400000, scale="Y", start=(2027, 9),
             notes="S2 C3: $2.5M (3a) + $0.9M (3b) planning assumption; scales with ramp"),
        dict(label="OPEX - AI platform subscription", annual=480000, scale="N", start=(2027, 9),
             notes="S2 C3: $300k + $180k"),
        dict(label="OPEX - Run team (keep-the-lights-on)", annual="={run_fte}*{run_rate}",
             scale="N", start=(2027, 9), notes="S2 C3: 5.5 FTE x $180k"),
        dict(label="OPEX - Vendor support & maintenance", annual=450000, scale="N", start=(2027, 9),
             notes="S2 C3: $300k + $150k"),
        dict(label="OPEX - Incremental infrastructure", annual=230000, scale="N", start=(2027, 9),
             notes="S2 C3: $150k + $80k"),
    ],
    milestone_blocks=[
        dict(title="Build A — Agentic voice resolution (3a)", milestones={
            "Plan / Design": dict(assump="S2: 4 FTE x 2 months.", team=4, months=2, cont=0.10,
                                  start=(2027, 1)),
            "Build / Test": dict(assump="S2: 8-FTE pod x 6 months.", team=8, months=6, cont=0.10,
                                 start=(2027, 3)),
            "Pilot / Change Mgmt.": dict(assump="S2 scale-up: 5 FTE x 8 months.", team=5, months=8,
                                         cont=0.10, start=(2027, 9)),
            "Scale / Run": dict(assump="Run-phase in Section 6.", team=0, months=0, cont=0.10,
                                start=(2028, 5)),
        }),
        dict(title="Build B — AI co-pilot (3b)", milestones={
            "Plan / Design": dict(assump="S2: 4 FTE x 2 months.", team=4, months=2, cont=0.10,
                                  start=(2027, 1)),
            "Build / Test": dict(assump="S2: 8-FTE pod x 5 months.", team=8, months=5, cont=0.10,
                                 start=(2027, 3)),
            "Pilot / Change Mgmt.": dict(assump="S2 scale-up: 5 FTE x 6 months.", team=5, months=6,
                                         cont=0.10, start=(2027, 8)),
            "Scale / Run": dict(assump="Run-phase in Section 6.", team=0, months=0, cont=0.10,
                                start=(2028, 2)),
        }),
    ],
    onetime_nonlabor=[
        dict(label="Platform and licence set-up", total=180000, months=2, start=(2027, 3), cap=0.0,
             notes="S2 C2: $120k (3a) + $60k (3b)"),
        dict(label="Hardware and infrastructure", total=380000, months=6, start=(2027, 3), cap=0.0,
             notes="S2 C2: $280k + $100k"),
        dict(label="Integration connectors", total=260000, months=6, start=(2027, 3), cap=0.0,
             notes="S2 C2: $180k + $80k"),
        dict(label="Cloud compute for build & evaluation", total=120000, months=6, start=(2027, 3),
             cap=0.0, notes="S2 C2: $80k + $40k"),
        dict(label="Programme management (8% of build)",
             total="={pm_pct}*({MS_TOTAL}+{NL:1}+{NL:2}+{NL:3}+{NL:4})", months=16, start=(2027, 1),
             cap=0.0, notes="S2 standard"),
        dict(label="Contingency (10% of build incl. PM)",
             total="={cont_pct}*({MS_TOTAL}+{NL:1}+{NL:2}+{NL:3}+{NL:4}+{NL:5})", months=16,
             start=(2027, 1), cap=0.0,
             notes="Total one-time ties to S2: $4,906,440 ($2,874,960 3a + $2,031,480 3b)"),
    ],
    wave_driver=dict(
        baseline=[
            ("Opening cost — 3a (post chat/self-serve)", "={S:open_3a}/1000000", "$USD M",
             "Post-upstream levers (S2 waterfall)", FMT_USDM),
            ("Voice-channel in-scope base (3a)", "={S:t3a_base}/1000000", "$USD M", "same", FMT_USDM),
            ("Residual base for co-pilot (3b)", "={S:open_3b}/1000000", "$USD M", "same", FMT_USDM),
        ],
        goal=[
            ("3a blended resolution rate (voice base)", "={S:ben_3a}/{S:t3a_base}", "%", "Steady state", FMT_PCT),
            ("3b blended handle-time reduction", "={S:ben_3b}/{S:open_3b}", "%", "Steady state", FMT_PCT),
        ],
        incr=[("Annual benefit (run rate, 3a+3b)", "={S:ben_total}/1000000", "$USD M", None, FMT_USDM)],
    ),
)

# ================================================================= SVC-4
SVC4 = dict(
    code="SVC-4",
    short="AI Workforce Management",
    name="AI-driven workforce management — skill-based routing and occupancy-led utilisation uplift",
    model_sheet="SVC-4 Model", wave_sheet="SVC-4 WAVE",
    workstream=SVC1["workstream"], owner=SVC1["owner"], bu="Global Servicing",
    status="Seeded 1:1 from S2 vDraft5 (Base) — benefit ties to $7.65M (4a $3.92M + 4b $3.74M)",
    golive=(2027, 7), ramp_months=6, tab_color="70AD47",
    sources=COMMON_SOURCES,
    open_items=[
        "S2 caveat on 4a (check #33): PayPal queues show a tighter AHT spread (1.517x) than the GFCCP "
        "benchmark (1.7x) that earned the 10% ceiling — S2's own note says the ceiling should arguably "
        "scale down; most intents run above the mix-shift cross-check. Treat 4a as the least-defended "
        "benefit in the stack.",
        "4b banks occupancy only (80.8% -> 85.0%); shrinkage is held at the 2026 actual 40.9% in "
        "Base/Downside (upside case banks improvement to 36%) pending interval-level data.",
        "Interval-level WFM data was scoped down by the provider (2 years daily avg vs 15-min asked) — "
        "may limit refinement.",
    ],
    assumptions=[
        ("#SUB", "Opening baselines (S2 waterfall: 4a opens on SVC-3 closing; 4b on 4a closing)"),
        ("open_4a", "Opening cost — 4a skill-based routing", 93163951.04, "$/yr", FMT_USD,
         S2 + WATERFALL_NOTE),
        ("#SUB", "S2 lever 4a — skill-based routing drivers"),
        ("sbr_ceiling", "Routing ceiling (GFCCP diagnostic)", 0.10, "%", FMT_PCT0,
         "S2 SBR_CEILING — share of residual cost at benchmark spread"),
        ("sbr_expansion", "Target expansion (share of theoretical gain)", 0.75, "%", FMT_PCT0,
         "S2 SBR_EXPANSION"),
        ("sbr_spread", "Weighted spread position x hardening (implied)", 0.5608617199, "%", FMT_PCT,
         "Implied from S2 engine: per-intent MIN((P75/P25 - 1)/0.7, 1) weighted by cost x hardening"),
        ("#SUB", "S2 lever 4b — utilisation drivers"),
        ("occ_today", "Occupancy — 2026 YTD actual", 0.808142857142857, "%", FMT_PCT, "S2 WFM actuals"),
        ("occ_target", "Occupancy — target", 0.85, "%", FMT_PCT,
         "S2 OCC_TGT: bottom of 85–90% best-in-class band (Upside 87.5%)"),
        ("shrink", "Shrinkage — held at 2026 actual", 0.408571428571429, "%", FMT_PCT,
         "S2: no shrinkage improvement banked in Base (UT_SHRINK_IMPROVE = N)"),
        ("realisation", "Realisation haircut on occupancy gain", 0.85, "%", FMT_PCT0,
         "S2 UT_REALISE — service-level protection in low-volume intervals"),
        ("#SUB", "Investment uplifts (S2 standard)"),
        ("pm_pct", "Programme management, % of build", 0.08, "%", FMT_PCT0, None),
        ("cont_pct", "Contingency, % of build incl. PM", 0.10, "%", FMT_PCT0, None),
        ("run_fte", "Run team headcount (4a + 4b consolidated)", 4.0, "# FTE", FMT_NUM1,
         "S2 C3: 2.0 + 2.0"),
        ("run_rate", "Run team loaded rate", 180000, "$/FTE/yr", FMT_USD, None),
        ("fte_4a", "FTE impacted — 4a (A0 basis, feeds SVC-6)", 236.9179, "# FTE", FMT_NUM1, "S2 A4a V102"),
        ("fte_4b", "FTE impacted — 4b (feeds SVC-6)", 135.2216, "# FTE", FMT_NUM1, "S2 A4b D25 (net FTE)"),
    ],
    calc=[
        ("ben_4a", "Benefit — S2 lever 4a (skill-based routing)",
         "={open_4a}*{sbr_ceiling}*{sbr_expansion}*{sbr_spread}", "$/yr", FMT_USD,
         "Ties to S2: $3,918,907"),
        ("open_4b", "Opening cost — 4b (post-4a residual)", "={open_4a}-{ben_4a}", "$/yr", FMT_USD,
         "S2: $89,245,044"),
        ("util_today", "Utilisation today = (1 - shrinkage) x occupancy",
         "=(1-{shrink})*{occ_today}", "%", FMT_PCT, "S2: 47.80%"),
        ("util_target", "Utilisation target", "=(1-{shrink})*{occ_target}", "%", FMT_PCT, "S2: 50.27%"),
        ("gross_rate", "Gross capacity released", "=1-{util_today}/{util_target}", "%", FMT_PCT,
         "S2: 4.92%"),
        ("net_rate", "Net released rate (x realisation)", "={gross_rate}*{realisation}", "%", FMT_PCT,
         "S2: 4.19%"),
        ("ben_4b", "Benefit — S2 lever 4b (utilisation/occupancy)", "={open_4b}*{net_rate}", "$/yr", FMT_USD,
         "Ties to S2: $3,735,543"),
        ("ben_total", "Total annual benefit (steady state)", "={ben_4a}+{ben_4b}", "$/yr", FMT_USD,
         "Ties to S2 combined: $7,654,450"),
        ("fte_out", "FTE impacted total (feeds SVC-6)", "={fte_4a}+{fte_4b}", "# FTE", FMT_NUM1, None),
        ("closing", "Closing front-office residual", "={open_4b}-{ben_4b}", "$/yr", FMT_USD,
         "S2: $85,509,501"),
    ],
    benefit_lines=[
        dict(label="OPEX - Skill-based routing capacity release (4a)", category="opex",
             runrate="{ben_4a}", baseline="={open_4a}/1000000",
             comment="Residual cost x 10% ceiling x 75% expansion x weighted spread position"),
        dict(label="OPEX - Utilisation / occupancy uplift (4b)", category="opex",
             runrate="{ben_4b}", baseline="={open_4b}/1000000",
             comment="Occupancy 80.8%->85.0% at 85% realisation; shrinkage held flat"),
    ],
    runcost_lines=[
        dict(label="OPEX - AI platform subscription", annual=250000, scale="N", start=(2027, 7),
             notes="S2 C3: $100k + $150k"),
        dict(label="OPEX - Run team (keep-the-lights-on)", annual="={run_fte}*{run_rate}",
             scale="N", start=(2027, 7), notes="S2 C3: 4.0 FTE x $180k"),
        dict(label="OPEX - Vendor support & maintenance", annual=250000, scale="N", start=(2027, 7),
             notes="S2 C3: $100k + $150k"),
        dict(label="OPEX - Incremental infrastructure", annual=130000, scale="N", start=(2027, 7),
             notes="S2 C3: $50k + $80k"),
    ],
    milestone_blocks=[
        dict(title="Build A — Skill-based routing (4a)", milestones={
            "Plan / Design": dict(assump="S2: 3 FTE x 1 month.", team=3, months=1, cont=0.10,
                                  start=(2027, 1)),
            "Build / Test": dict(assump="S2: 8-FTE pod x 5 months.", team=8, months=5, cont=0.10,
                                 start=(2027, 2)),
            "Pilot / Change Mgmt.": dict(assump="S2 scale-up: 4 FTE x 6 months.", team=4, months=6,
                                         cont=0.10, start=(2027, 7)),
            "Scale / Run": dict(assump="Run-phase in Section 6.", team=0, months=0, cont=0.10,
                                start=(2028, 1)),
        }),
        dict(title="Build B — Utilisation (4b)", milestones={
            "Plan / Design": dict(assump="S2: 3 FTE x 1 month.", team=3, months=1, cont=0.10,
                                  start=(2027, 1)),
            "Build / Test": dict(assump="S2: 8-FTE pod x 5 months.", team=8, months=5, cont=0.10,
                                 start=(2027, 2)),
            "Pilot / Change Mgmt.": dict(assump="S2 scale-up: 4 FTE x 6 months.", team=4, months=6,
                                         cont=0.10, start=(2027, 7)),
            "Scale / Run": dict(assump="Run-phase in Section 6.", team=0, months=0, cont=0.10,
                                start=(2028, 1)),
        }),
    ],
    onetime_nonlabor=[
        dict(label="Platform and licence set-up", total=90000, months=2, start=(2027, 2), cap=0.0,
             notes="S2 C2: $40k (4a) + $50k (4b)"),
        dict(label="Hardware and infrastructure", total=200000, months=5, start=(2027, 2), cap=0.0,
             notes="S2 C2: $80k + $120k"),
        dict(label="Integration connectors", total=160000, months=5, start=(2027, 2), cap=0.0,
             notes="S2 C2: $60k + $100k"),
        dict(label="Cloud compute for build & evaluation", total=70000, months=5, start=(2027, 2),
             cap=0.0, notes="S2 C2: $30k + $40k"),
        dict(label="Programme management (8% of build)",
             total="={pm_pct}*({MS_TOTAL}+{NL:1}+{NL:2}+{NL:3}+{NL:4})", months=12, start=(2027, 1),
             cap=0.0, notes="S2 standard"),
        dict(label="Contingency (10% of build incl. PM)",
             total="={cont_pct}*({MS_TOTAL}+{NL:1}+{NL:2}+{NL:3}+{NL:4}+{NL:5})", months=12,
             start=(2027, 1), cap=0.0,
             notes="Total one-time ties to S2: $3,536,280 ($1,708,740 4a + $1,827,540 4b)"),
    ],
    wave_driver=dict(
        baseline=[
            ("Opening residual cost (post levers 1–3)", "={S:open_4a}/1000000", "$USD M",
             "Post-upstream levers (S2 waterfall)", FMT_USDM),
            ("Occupancy today", "={S:occ_today}", "%", "2026 YTD", FMT_PCT),
            ("Utilisation today", "={S:util_today}", "%", "2026 YTD", FMT_PCT),
        ],
        goal=[
            ("Occupancy target", "={S:occ_target}", "%", "Steady state", FMT_PCT),
            ("Net utilisation release rate", "={S:net_rate}", "%", "Steady state", FMT_PCT),
        ],
        incr=[("Annual benefit (run rate, 4a+4b)", "={S:ben_total}/1000000", "$USD M", None, FMT_USDM)],
    ),
)

# ================================================================= SVC-5
def svc5_table(mb):
    sw = mb.sw
    sw.cell(sw.r, 2, "Back-office disputes workflows (S2 grain — parent workflow level, pending "
                     "sub-workflow data)", f(bold=True, size=10, color="FF1F3864"))
    sw.skip(1)
    hr = sw.r
    for c, h in [(2, "Workflow"), (4, "Opening cost ($/yr)"), (5, "Tier"),
                 (6, "Current automation"), (7, "Tier rate"), (8, "Target (cap 95%)"),
                 (9, "Reduction of manual"), (10, "Benefit ($/yr)")]:
        sw.cell(hr, c, h, f(bold=True, size=9, color=WHITE), fl=DARKBLUE_FILL, wrap=True,
                align="center")
    mb.ws.row_dimensions[hr].height = 30
    sw.skip(1)
    rows = [
        ("Unauth Parent", 1631088.80, "Hard", 0.7611927106),
        ("Unauth Child", 1034618.79, "Easy", 0.9182717891),
        ("Chargeback", 2895665.62, "Easy", 0.8453057869),
        ("Unauth ACH (Reversal)", 417774.92, "Medium", 0.7050737281),
        ("Billing Errors", 1610134.92, "Medium", 0.6079754214),
        ("PPBP Claims", 7343551.07, "Medium", 0.8261161516),
        ("Issuance (PP only)", 2731500.87, "Hard", 0.6029094246),
    ]
    er, mr_, hr_ = mb.sym["r_easy"], mb.sym["r_med"], mb.sym["r_hard"]
    cap = mb.sym["auto_cap"]
    first = sw.r
    for wf, cost, tier, cur in rows:
        r = sw.r
        sw.cell(r, 2, wf, f(bold=True), border=BORDER_ALL)
        sw.input_cell(r, 4, cost, num=FMT_USD)
        sw.input_cell(r, 5, tier)
        sw.input_cell(r, 6, cur, num=FMT_PCT)
        sw.formula_cell(r, 7,
                        f'=IF(E{r}="Easy",{er},IF(E{r}="Medium",{mr_},{hr_}))', num=FMT_PCT0)
        sw.formula_cell(r, 8, f"=MIN(F{r}+G{r}*(1-F{r}),{cap})", num=FMT_PCT)
        sw.formula_cell(r, 9, f"=(H{r}-F{r})/(1-F{r})", num=FMT_PCT)
        sw.formula_cell(r, 10, f"=D{r}*I{r}", num=FMT_USD)
        sw.skip(1)
    last = sw.r - 1
    r = sw.r
    sw.cell(r, 2, "Subtotal — back-office disputes", f(bold=True))
    sw.formula_cell(r, 4, f"=SUM(D{first}:D{last})", num=FMT_USD)
    sw.formula_cell(r, 10, f"=SUM(J{first}:J{last})", num=FMT_USD)
    mb.sym["t5_base"] = f"$D${r}"
    mb.sym["t5_ben"] = f"$J${r}"
    sw.skip(2)

S5_SOURCES = [
    S2 + "Distilled at parent-workflow grain (7 disputes workflows); reproduces the S2 A5 tab "
    "exactly at seed values.",
    "Workplan: 'Project Zenith Automation workplan and data requests vS_1.xlsx', Servicing tabs",
]

SVC5 = dict(
    code="SVC-5",
    short="Back-Office Automation",
    name="Back-office automation across disputes workflows — reduce remaining manual case handling",
    model_sheet="SVC-5 Model", wave_sheet="SVC-5 WAVE",
    workstream=SVC1["workstream"], owner=SVC1["owner"], bu="Global Servicing",
    status="Seeded 1:1 from S2 vDraft5 (Base) — benefit ties to $6.83M",
    golive=(2027, 9), ramp_months=8, tab_color="70AD47",
    sources=S5_SOURCES,
    open_items=[
        "Scope is DISPUTES ONLY ($17.7M base) — the workplan cites a ~$41M back-office baseline; "
        "sub-workflow volume/cost/automation data is pending (priority-1 request #7, no owner assigned).",
        "Workflow data is at parent grain pending sub-workflow detail; back-office FTE conversion "
        "borrows the front-office utilisation constant (S2 QC flag — implies ~$32k/FTE, offshore-like).",
        "Tier rates (Easy 55% / Medium 40% / Hard 25% of remaining manual, 95% cap) are S2 assumptions "
        "gated by the Intent Tiering back-office tiers.",
    ],
    assumptions=[
        ("#SUB", "Automation rate assumptions (S2, editable)"),
        ("r_easy", "Tier rate — Easy (reduction of remaining manual)", 0.55, "%", FMT_PCT0,
         "S2 BO_R Easy (Upside 70% / Downside 40%)"),
        ("r_med", "Tier rate — Medium", 0.40, "%", FMT_PCT0, "S2 BO_R Medium"),
        ("r_hard", "Tier rate — Hard", 0.25, "%", FMT_PCT0, "S2 BO_R Hard"),
        ("auto_cap", "Automation ceiling (max target)", 0.95, "%", FMT_PCT0, "S2 BO_CAP"),
        ("#SUB", "Investment uplifts (S2 standard)"),
        ("pm_pct", "Programme management, % of build", 0.08, "%", FMT_PCT0, None),
        ("cont_pct", "Contingency, % of build incl. PM", 0.10, "%", FMT_PCT0, None),
        ("run_fte", "Run team headcount", 2.5, "# FTE", FMT_NUM1, "S2 C3"),
        ("run_rate", "Run team loaded rate", 180000, "$/FTE/yr", FMT_USD, None),
        ("fte_out", "FTE impacted (feeds SVC-6)", 210.8406, "# FTE", FMT_NUM1,
         "S2 A5 L13 — minutes saved / 59,649 productive min per FTE-yr"),
    ],
    custom_section=svc5_table,
    calc=[
        ("ben_total", "Total annual benefit (steady state)", "={t5_ben}", "$/yr", FMT_USD,
         "Ties to S2 A5 benefit $6,833,504"),
        ("closing", "Closing back-office cost", "={t5_base}-{ben_total}", "$/yr", FMT_USD,
         "S2: $10,830,831"),
    ],
    benefit_lines=[
        dict(label="OPEX - Back-office manual case-handling reduction", category="opex",
             runrate="{ben_total}", baseline="={t5_base}/1000000",
             comment="Per-workflow: target = min(current + tier rate x (1-current), 95%); "
                     "benefit = cost x reduction of remaining manual"),
    ],
    runcost_lines=[
        dict(label="OPEX - Inference & token consumption", annual=400000, scale="Y", start=(2027, 9),
             notes="S2 C3 planning assumption; scales with ramp"),
        dict(label="OPEX - AI platform subscription", annual=200000, scale="N", start=(2027, 9),
             notes="S2 C3 planning number"),
        dict(label="OPEX - Run team (keep-the-lights-on)", annual="={run_fte}*{run_rate}",
             scale="N", start=(2027, 9), notes="S2 C3: 2.5 FTE x $180k"),
        dict(label="OPEX - Vendor support & maintenance", annual=150000, scale="N", start=(2027, 9),
             notes="S2 C3 planning number"),
        dict(label="OPEX - Incremental infrastructure", annual=80000, scale="N", start=(2027, 9),
             notes="S2 C3 planning number"),
    ],
    milestones={
        "Plan / Design": dict(assump="S2: 4 FTE x 2 months.", team=4, months=2, cont=0.10,
                              start=(2027, 1)),
        "Build / Test": dict(assump="S2: 8-FTE pod x 6 months.", team=8, months=6, cont=0.10,
                             start=(2027, 3)),
        "Pilot / Change Mgmt.": dict(assump="S2 scale-up: 5 FTE x 8 months.", team=5, months=8,
                                     cont=0.10, start=(2027, 9)),
        "Scale / Run": dict(assump="Run-phase in Section 6.", team=0, months=0, cont=0.10,
                            start=(2028, 5)),
    },
    onetime_nonlabor=[
        dict(label="Platform and licence set-up", total=80000, months=2, start=(2027, 3), cap=0.0,
             notes="S2 C2 planning number"),
        dict(label="Hardware and infrastructure", total=220000, months=6, start=(2027, 3), cap=0.0,
             notes="S2 C2 planning number"),
        dict(label="Integration connectors", total=180000, months=6, start=(2027, 3), cap=0.0,
             notes="S2 C2 planning number"),
        dict(label="Cloud compute for build & evaluation", total=50000, months=6, start=(2027, 3),
             cap=0.0, notes="S2 C2 planning number"),
        dict(label="Programme management (8% of build)",
             total="={pm_pct}*({MS_TOTAL}+{NL:1}+{NL:2}+{NL:3}+{NL:4})", months=16, start=(2027, 1),
             cap=0.0, notes="S2 standard"),
        dict(label="Contingency (10% of build incl. PM)",
             total="={cont_pct}*({MS_TOTAL}+{NL:1}+{NL:2}+{NL:3}+{NL:4}+{NL:5})", months=16,
             start=(2027, 1), cap=0.0, notes="Total one-time ties to S2: $2,720,520"),
    ],
    wave_driver=dict(
        baseline=[
            ("Back-office disputes cost baseline", "={S:t5_base}/1000000", "$USD M",
             "Jan–Jul 2026 x 12/7", FMT_USDM),
            ("Manual cases per year (static S2 stat — not linked)", 8961568, "# cases", "same", FMT_NUM),
            ("Blended current automation (static S2 stat — not linked)", 0.7876, "%", "same", FMT_PCT),
        ],
        goal=[
            ("Blended reduction of remaining manual", "={S:ben_total}/{S:t5_base}", "%",
             "Steady state", FMT_PCT),
            ("FTE impacted", "={S:fte_out}", "# FTE", "Steady state", FMT_NUM1),
        ],
        incr=[("Annual benefit (run rate)", "={S:ben_total}/1000000", "$USD M", None, FMT_USDM)],
    ),
)

# ================================================================= SVC-6
def svc6_table(mb):
    sw = mb.sw
    sw.cell(sw.r, 2, "Non-FTE cost pool x variability with FTE reduction (S2 A6 / SACP ledger 2026)",
            f(bold=True, size=10, color="FF1F3864"))
    sw.skip(1)
    hr = sw.r
    for c, h in [(2, "Category"), (4, "2026 spend ($/yr)"), (6, "Variability with FTE"),
                 (8, "Savings ($/yr)")]:
        sw.cell(hr, c, h, f(bold=True, size=9, color=WHITE), fl=DARKBLUE_FILL, wrap=True,
                align="center")
    sw.cell(hr, 13, "Savings = spend x variability x FTE-impacted share",
            f(italic=True, size=8, color="FF808080"))
    sw.skip(1)
    rows = [
        ("Facilities / Networking", 9786003.65, 0.55,
         "Seat cost follows headcount as leases/footprints renegotiate"),
        ("D&A", 2095950.66, 0.10, "Only avoided future refresh is addressable"),
        ("SW Maintenance", 1930696.92, 0.75, "Per-seat/per-licence — most headcount-linked line"),
        ("Other", 792257.22, 0.35, "Mixed behaviour; mid-range factor pending breakdown"),
        ("Marketing", 55484.29, 0.0, "Campaign-driven, not headcount-driven"),
        ("Data Center & Rent", 3944.67, 0.20, "Largely fixed, immaterial"),
    ]
    share = mb.sym["fte_share"]
    first = sw.r
    for cat, spend, var, note in rows:
        r = sw.r
        sw.cell(r, 2, cat, f(bold=True), border=BORDER_ALL)
        sw.input_cell(r, 4, spend, num=FMT_USD)
        sw.input_cell(r, 6, var, num=FMT_PCT0)
        sw.formula_cell(r, 8, f"=D{r}*F{r}*{share}", num=FMT_USD)
        sw.cell(r, 13, note, f(italic=True, size=8, color="FF595959"))
        sw.skip(1)
    last = sw.r - 1
    r = sw.r
    sw.cell(r, 2, "Subtotal — non-FTE savings", f(bold=True))
    sw.formula_cell(r, 4, f"=SUM(D{first}:D{last})", num=FMT_USD)
    sw.formula_cell(r, 8, f"=SUM(H{first}:H{last})", num=FMT_USD)
    mb.sym["t6_base"] = f"$D${r}"
    mb.sym["t6_ben"] = f"$H${r}"
    sw.skip(2)

def make_svc6(fte_refs):
    """fte_refs: dict code -> cross-sheet ref string for that model's FTE-out cell."""
    return dict(
        code="SVC-6",
        short="Non-FTE Savings",
        name="Non-FTE cost flow-through from front- and back-office FTE reduction",
        model_sheet="SVC-6 Model", wave_sheet="SVC-6 WAVE",
        workstream=SVC1["workstream"], owner=SVC1["owner"], bu="Global Servicing",
        status="Seeded 1:1 from S2 vDraft5 (Base) — benefit ties to $4.04M; FTE inputs LINK to the "
               "other initiative models",
        golive=(2027, 7), ramp_months=9, tab_color="A9D08E",
        sources=[
            S2 + "Flow-through lever (S2 A6): non-FTE pool x variability x FTE-impacted share; "
            "FTE inputs are live links to the other five initiative models.",
            "Workplan: 'Project Zenith Automation workplan and data requests vS_1.xlsx', Servicing tabs",
        ],
        open_items=[
            "Flow-through lever: carries NO build or run cost in S2 (rides initiatives 1–5) and is "
            "excluded from the S2 payback calc — confirm WAVE treatment with Finance/AAO before "
            "submitting as a standalone business case.",
            "S2 applies one aggregate FTE-impacted share (55.2%) to every category — including "
            "facilities lines that arguably scale with front-office seats only (S2 QC flag).",
            "Non-FTE cost baseline granularity is a pending data request (#8, no owner assigned).",
            "Ramp approximates S2's 'follows the levers' quarterly profile with a 9-month linear ramp "
            "from Jul-2027.",
            "QC: 'Data Center & Rent' 2026 spend is $3,945/yr in the S2 source — 3-4 orders of "
            "magnitude below sibling categories. Faithfully reproduced, but verify it is not a "
            "$K-vs-$ slip in the SACP extract.",
        ],
        assumptions=[
            ("#SUB", "Baseline FTE in scope (S2 A6)"),
            ("fte_fo", "Front-office baseline FTE", 5921.3094, "# FTE", FMT_NUM1, "S2 A0 implied FTE"),
            ("fte_bo", "Back-office baseline FTE (disputes)", 486.5333, "# FTE", FMT_NUM1, "S2 M5 build"),
            ("#SUB", "FTE impacted by initiative (GREEN = linked to the other model sheets)"),
            ("i1", "SVC-1 Contact avoidance", f"={fte_refs['SVC-1']}", "# FTE", FMT_NUM1, "linked"),
            ("i2", "SVC-2 Enhanced chat / self-serve", f"={fte_refs['SVC-2']}", "# FTE", FMT_NUM1, "linked"),
            ("i3", "SVC-3 Agentic voice & co-pilot", f"={fte_refs['SVC-3']}", "# FTE", FMT_NUM1, "linked"),
            ("i4", "SVC-4 AI workforce management", f"={fte_refs['SVC-4']}", "# FTE", FMT_NUM1, "linked"),
            ("i5", "SVC-5 Back-office automation", f"={fte_refs['SVC-5']}", "# FTE", FMT_NUM1, "linked"),
        ],
        calc=[
            ("fte_base", "Total baseline FTE in scope", "={fte_fo}+{fte_bo}", "# FTE", FMT_NUM1,
             "S2: 6,407.8"),
            ("fte_imp", "Total FTE impacted", "={i1}+{i2}+{i3}+{i4}+{i5}", "# FTE", FMT_NUM1,
             "S2: 3,537.1"),
            ("fte_share", "FTE impacted as share of baseline", "={fte_imp}/{fte_base}", "%", FMT_PCT,
             "S2: 55.2%"),
        ],
        custom_section=None,   # replaced below — table needs fte_share sym first
        calc2_note="table depends on fte_share, so it renders after calc",
        benefit_lines=[
            dict(label="OPEX - Non-FTE cost flow-through", category="opex",
                 runrate="{t6_ben}", baseline="={t6_base}/1000000",
                 comment="Category spend x variability x FTE-impacted share (55.2%)"),
        ],
        runcost_lines=[],
        milestones={
            "Plan / Design": dict(assump="No build — flow-through of initiatives 1–5 (S2 carries zero "
                                         "one-time and run cost on this lever).",
                                  team=0, months=0, cont=0.10, start=(2027, 7)),
            "Build / Test": dict(assump="n/a", team=0, months=0, cont=0.10, start=(2027, 7)),
            "Pilot / Change Mgmt.": dict(assump="n/a", team=0, months=0, cont=0.10, start=(2027, 7)),
            "Scale / Run": dict(assump="n/a", team=0, months=0, cont=0.10, start=(2027, 7)),
        },
        onetime_nonlabor=[],
        wave_driver=dict(
            baseline=[
                ("Non-FTE cost pool (2026)", "={S:t6_base}/1000000", "$USD M", "FY2026 (SACP cost ledger)", FMT_USDM),
                ("Baseline FTE in scope", "={S:fte_base}", "# FTE", "2026", FMT_NUM1),
            ],
            goal=[
                ("FTE impacted (levers 1–5)", "={S:fte_imp}", "# FTE", "Steady state", FMT_NUM1),
                ("Blended savings rate on the non-FTE pool",
                 "={S:t6_ben}/{S:t6_base}", "%", "Steady state", FMT_PCT),
            ],
            incr=[("Annual benefit (run rate)", "={S:t6_ben}/1000000", "$USD M", None, FMT_USDM)],
        ),
    )


META = dict(
    title="PROJECT ZENITH — SERVICING WORKSTREAM | INITIATIVE MODELS & WAVE TEMPLATES",
    workstream="Servicing — Improve NPS and eliminate avoidable contacts through Prevent, Self-Serve and "
               "Optimize. ELT sponsor: Aaron | WSL: Tahira Adatia | IOs: Jackie Yu, Matt Anderson, Bob Hurst.",
    purpose="One file per workstream: the six S2 initiatives, each with a Model sheet (distilled from the "
            "S2 sizing model, tier-level) formula-linked into its own copy of the standard WAVE template. "
            "S2 submission: Fri 4 Sep 2026.",
    version="v1 — seeded 1:1 from the S2 sizing model vDraft5 (Base scenario, 28 Aug 2026). All initiative "
            "benefits, one-time and run costs tie to S2 to the cent at seed values (see tie-out targets on "
            "each model sheet).",
    prepared="Prepared by AAO model build, 31 Aug 2026. Sources: 20260828_Servicing_S2sizing_vDraft5.xlsb; "
             "Project Zenith workplan vS_1; Zenith Business Case Template by Lever (WAVE).",
    sources="S2 sizing model vDraft5 (77-intent L2 engine, A0–A6 waterfall, C1–C3 investment); distillation "
            "is at difficulty-tier level with per-tier bases and effective rates reproducing the L2 engine "
            "exactly at seed values.",
    sheet_index=[
        ("Cover", "This sheet — orientation, legend, deviations, open items."),
        ("Instructions", "The WAVE template's own instruction sheet (as uploaded; dead broken-reference drop-down cells cleared)."),
        ("Rate Card", "Shared people-cost engine — S2 8-FTE pod at $200k/yr blended (ties to S2 C2); "
                      "contingency reference; capitalization policy (0% = S2 cash treatment)."),
        ("Summary", "Portfolio roll-up of all six initiatives (links to WAVE sheets)."),
        ("SVC-1 Model / WAVE", "Contact Avoidance (S2 lever A1) — $12.84M."),
        ("SVC-2 Model / WAVE", "Enhanced Chat / Self-Serve (A2) — $14.77M."),
        ("SVC-3 Model / WAVE", "Agentic Voice & AI Co-pilot (A3a + A3b) — $35.25M."),
        ("SVC-4 Model / WAVE", "AI Workforce Management (A4a + A4b) — $7.65M."),
        ("SVC-5 Model / WAVE", "Back-Office Automation (A5) — $6.83M."),
        ("SVC-6 Model / WAVE", "Non-FTE Savings flow-through (A6) — $4.04M; FTE inputs link to the "
                               "other five models."),
        ("Standard Template", "Reference copy of the standard WAVE template (only error-guard fixes applied — see deviations)."),
    ],
    linking_notes=LINKING_NOTES + [
        "Waterfall de-duplication: each model's opening cost is the prior lever's closing baseline "
        "(S2 stacking order). Openings are seeded inputs — refresh from the S2 L2 engine if upstream "
        "levers or intent tiering change (tier-level bases cannot re-derive themselves).",
    ],
    deviations=STD_DEVIATIONS,
    open_items=[
        "Distillation grain: models run at difficulty-tier aggregates (SVC-5 at workflow grain); the S2 "
        "77-intent L2 engine remains the source of the tier bases. At seed values every headline ties to "
        "S2 to the cent; after editing rates here, re-tier in S2 for the L2-exact answer.",
        "S2's own caveats carried over: run cost is the least-evidenced part (planning numbers under a "
        "$15M cap; token lines lack consumption forecasts); build durations are not IO-validated; "
        "client costing sheet still pending (C1–C3 built for a rate-card drop-in).",
        "S2 4a routing ceiling may need scaling down (PayPal spread 1.52x vs 1.7x benchmark — S2 check "
        "#33 note); most intents run above the mix-shift cross-check.",
        "Baseline reconciliations open: S2 traces $156M front-office (S1 view $219M; FP&A reference "
        "$148M); back-office covers disputes only ($17.7M of ~$41M workplan figure); 6.4k of 7.8k FTE.",
        "Capitalization: S2 treats all one-time as cash/expensed; cap % machinery is in place (Rate Card "
        "defaults 0%) — set Build/Test % once Finance confirms treatment.",
        "FTE-impacted figures use the S2 'A0 basis' (as consumed by the non-FTE flow-through); "
        "residual-basis reductions are lower (S2 QC flag) — do not mix bases when quoting headcount.",
    ],
)


def assemble_servicing(out_path):
    wb = openpyxl.load_workbook(TEMPLATE_PATH)
    del wb["Business Case_Example"]
    ins = wb["Instructions"]
    for r in range(176, 212):
        cc = ins[f"E{r}"]
        if isinstance(cc.value, str) and "#REF!" in cc.value:
            cc.value = None
    st = wb["Standard Template"]
    st["G163"] = '=IFERROR(I117/-SUM(L149:P149),"n/a")'
    st["G164"] = '=IFERROR(IRR($L$159:$P$159, 0.2),"n/a")'
    st["L161"] = "=IF(L160<0,1,0)"
    for cur, prev in [("M", "L"), ("N", "M"), ("O", "N"), ("P", "O")]:
        st[f"{cur}161"] = (f"=IF({cur}160<0,1,IF(AND({prev}160<0,{cur}159>0),"
                           f"-{prev}160/{cur}159,0))")

    rc = build_rate_card(wb, "Rate Card", RC_DEFAULTS)
    specs = [SVC1, SVC2, SVC3, SVC4, SVC5]
    pair_names, fte_refs, built = [], {}, []
    for spec in specs:
        mb = ModelBuilder(wb, spec, rc)
        feed = mb.build()
        fill_wave(wb, spec, feed, mb.sym)
        fte_refs[spec["code"]] = f"'{spec['model_sheet']}'!{mb.sym['fte_out']}"
        pair_names += [spec["model_sheet"], spec["wave_sheet"]]
        built.append(spec)
    svc6 = make_svc6(fte_refs)
    # SVC-6: the category table needs fte_share (defined in calc), so hook it
    # into calc-then-table order by putting the table into a custom hook that
    # ModelBuilder calls after assumptions; instead we append table rendering
    # after calc via a wrapper build.
    mb6 = ModelBuilder(wb, svc6, rc)
    mb6.header(); mb6.status_block(); mb6.assumptions(); mb6.calc()
    svc6_table(mb6)
    mb6.ramp(); mb6.benefits(); mb6.investment(); mb6.runcosts(); mb6.mapping_note()
    fill_wave(wb, svc6, mb6.feed, mb6.sym)
    pair_names += [svc6["model_sheet"], svc6["wave_sheet"]]
    built.append(svc6)

    build_summary(wb, built, "SERVICING WORKSTREAM", cap_note="""Capitalization policy note: this file defaults ALL cap % to 0% to mirror the S2 model's all-cash treatment; the SDLC/Sales files default Build/Test labor to 80%. Align the policy across workstreams with Finance before the S2 gate.""")
    build_cover(wb, META)
    order = ["Cover", "Instructions", "Rate Card", "Summary"] + pair_names + ["Standard Template"]
    wb._sheets = [wb[n] for n in order if n in wb.sheetnames] + \
                 [ws for ws in wb._sheets if ws.title not in order]
    wb["Standard Template"].sheet_properties.tabColor = "808080"
    wb["Instructions"].sheet_properties.tabColor = "808080"
    wb.active = 0
    wb.save(out_path)
    print("saved", out_path)


if __name__ == "__main__":
    assemble_servicing("Zenith_Servicing_Models_and_WAVE_v1.xlsx")
