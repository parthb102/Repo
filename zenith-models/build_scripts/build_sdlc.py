#!/usr/bin/env python3
"""Build Zenith_SDLC_Models_and_WAVE_v1.xlsx — 2 initiatives."""
from framework import FMT_USD, FMT_PCT, FMT_PCT0, FMT_NUM, FMT_USDM
from common import assemble, STD_DEVIATIONS, LINKING_NOTES

PENDING = "PENDING — placeholder, not data. "

RC_DEFAULTS = dict(
    basis="Yearly",
    hours_day=8, days_month=21,
    roles=[
        ("Engineer", 3, 180000),
        ("QA Engineer", 2, 140000),
        ("Solution Architect", 1, 220000),
        ("Product Manager", 1, 190000),
        ("Data Engineer", 1, 185000),
        ("ML Engineer", 1, 210000),
        ("Program Manager", 1, 170000),
    ],
    cap_pcts={"Plan / Design": 0.0, "Build / Test": 0.80,
              "Pilot / Change Mgmt.": 0.0, "Scale / Run": 0.0},
    cap_nonlabor=0.0,
    notes=[
        "Role rates are PLACEHOLDERS — replace with the PayPal/FP&A rate card. For reference, the "
        "Servicing S2 model uses a $200,000/yr blended loaded delivery FTE rate (+10% delivery risk) "
        "and $180,000/yr for run-team FTEs.",
        "Team composition mirrors the standard AAO delivery-pod thinking; add/remove roles as the "
        "initiative team shapes firm up (spare rows provided).",
        "Build/Test capitalization default of 80% follows a typical internal-use software policy "
        "(application development stage capitalizable) — CONFIRM WITH FINANCE before S3.",
    ],
)

COMMON_SOURCES = [
    "Workplan: 'Project Zenith Automation workplan and data requests vS_1.xlsx', SDLC tab + SDLC Data Requests tab",
    "Impact ranges: Aug 13 deck pp. 9, 19–21; Board deck pp. 12, 22 (preliminary — Finance to validate)",
]

SDLC1 = dict(
    code="SDLC-1",
    short="Agentic Loop Engineering",
    name="Agentic loop engineering — raise engineering throughput on the residual addressable base",
    model_sheet="SDLC-1 Model",
    wave_sheet="SDLC-1 WAVE",
    workstream="SDLC (ELT sponsor: Srini | WSL: Pooja | IOs: Pooja, Aruna)",
    owner="Pooja (WSL) — initiative owner TBC",
    bu="CTO / SDLC",
    status="Structure ready; baselines PENDING data requests — see open items",
    golive=(2027, 5),
    ramp_months=12,
    tab_color="4472C4",
    sources=COMMON_SOURCES,
    open_items=[
        "FTE/CW population and fully loaded cost baseline pending (SDLC data request #1 — Thom/Thanh (SDLC), ETO (PDLC)); all baseline inputs below are 0 until received.",
        "Banked Code Assist savings to reconcile so the residual addressable base nets them out (W3 objective).",
        "Adoption ramp by domain/role pending (request #3); 20-domain harness build plan shared by Pooja (request #12).",
        "Token consumption benchmark by role shared for SDLC (request #11) — to be validated, then wire into run costs.",
        "Build shape below mirrors the Servicing S2 delivery pod as a placeholder — refine with IOs before S3.",
    ],
    assumptions=[
        ("#SUB", "Baseline / denominator  (PENDING data request #1)"),
        ("sw_fte", "CTO SWE IC FTE population — in scope", 0, "# FTE", FMT_NUM,
         PENDING + "Data request #1 (Thom/Thanh)"),
        ("sw_cw", "CTO SWE CW population — in scope", 0, "# CW", FMT_NUM,
         PENDING + "Data request #1"),
        ("flc_fte", "Avg fully loaded cost per SWE FTE", 0, "$/yr", FMT_USD,
         PENDING + "Data request #1"),
        ("flc_cw", "Avg fully loaded cost per CW", 0, "$/yr", FMT_USD,
         PENDING + "Data request #1"),
        ("banked", "Code Assist savings already banked (annual)", 0, "$/yr", FMT_USD,
         PENDING + "Reconcile with Finance; netted out of the addressable base to avoid double count"),
        ("#SUB", "Impact drivers  (Aug 13 deck pp. 9, 19–21 — preliminary, Finance to validate)"),
        ("prod_uplift", "Incremental productivity uplift on residual base", 0.15, "%", FMT_PCT0,
         "PLACEHOLDER pending validation — source materials cite ~$173–204M total SDLC opportunity"),
        ("adoption", "Steady-state adoption (share of population on harness)", 0.80, "%", FMT_PCT0,
         "PLACEHOLDER — adoption ramp by domain/role pending (request #3)"),
        ("capture", "Capture rate — capacity converted to bankable cost", 0.65, "%", FMT_PCT0,
         "PLACEHOLDER — capacity-to-cost capture and redeployment logic to agree with Finance"),
        ("#SUB", "Investment uplifts (consistent with Servicing S2 standard)"),
        ("pm_pct", "Programme management, % of build", 0.08, "%", FMT_PCT0,
         "Same standard as Servicing S2 (8%)"),
        ("cont_pct", "Contingency, % of build incl. PM", 0.10, "%", FMT_PCT0,
         "Same standard as Servicing S2 (10%)"),
    ],
    calc=[
        ("base_total", "Total in-scope engineering labor base",
         "=({sw_fte}*{flc_fte}+{sw_cw}*{flc_cw})", "$/yr", FMT_USD,
         "FTE x cost + CW x cost"),
        ("base_resid", "Residual addressable base (net of banked Code Assist)",
         "=MAX({base_total}-{banked},0)", "$/yr", FMT_USD, None),
        ("cap_value", "Gross capacity value created",
         "={base_resid}*{prod_uplift}*{adoption}", "$/yr", FMT_USD,
         "Residual base x productivity uplift x adoption"),
        ("ben_loop", "Bankable annual benefit (steady state)",
         "={cap_value}*{capture}", "$/yr", FMT_USD,
         "x capture rate — the benefit line that feeds WAVE"),
    ],
    benefit_lines=[
        dict(sym="ben_loop", label="OPEX - Engineering capacity release (loop engineering)",
             category="opex", runrate="{ben_loop}", baseline="={base_total}/1000000",
             comment="Bankable share of capacity created on the residual addressable base"),
    ],
    runcost_lines=[
        dict(label="OPEX - Model / token consumption", annual=0, scale="Y", start=(2027, 5),
             notes=PENDING + "Per-developer consumption (request #11) x adopted developers; scales with ramp"),
        dict(label="OPEX - Harness platform & tooling run", annual=0, scale="N", start=(2027, 5),
             notes=PENDING + "Ongoing platform/support run cost"),
        dict(label="OPEX - Champion / coaching capacity", annual=0, scale="N", start=(2027, 5),
             notes=PENDING + "Champion/coaching capacity plan"),
    ],
    milestones={
        "Plan / Design": dict(assump="PLACEHOLDER shape mirroring the AAO delivery pod (Servicing S2: "
                                     "design team ≤4 for 1–2 months). Refine with IO.",
                              team=4, months=2, cont=0.10, start=(2026, 10)),
        "Build / Test": dict(assump="PLACEHOLDER — one 8-FTE pod (PO, PM/Scrum, Tech Lead, 2 AI Eng, "
                                    "DevOps, QA, FA/UX) for ~5 months.",
                             team=8, months=5, cont=0.10, start=(2026, 12)),
        "Pilot / Change Mgmt.": dict(assump="PLACEHOLDER — scale-up team of 5 (technical roles stay on) "
                                            "through domain rollout.",
                                     team=5, months=6, cont=0.10, start=(2027, 5)),
        "Scale / Run": dict(assump="Run-phase support carried as recurring run cost (Section 6), "
                                   "per the standard treatment — leave 0 here unless a dedicated "
                                   "scale team is planned.",
                            team=0, months=0, cont=0.10, start=(2027, 11)),
    },
    onetime_nonlabor=[
        dict(label="Vendor / integration / tooling set-up", total=0, months=3, start=(2026, 12),
             cap=0.0, notes=PENDING + "Build-vs-buy perspective due at W6 tech workshop"),
        dict(label="Programme management (8% of build)",
             total="={pm_pct}*({MS_TOTAL}+{NL:1})", months=9, start=(2026, 10), cap=0.0,
             notes="Formula: 8% x (milestone labor + non-labor build items) — Servicing S2 standard"),
        dict(label="Contingency (10% of build incl. PM)",
             total="={cont_pct}*({MS_TOTAL}+{NL:1}+{NL:2})", months=9, start=(2026, 10), cap=0.0,
             notes="Formula: 10% x (build subtotal incl. PM) — Servicing S2 standard"),
    ],
    wave_driver=dict(
        baseline=[
            ("Total in-scope engineering labor base", "={S:base_total}/1000000", "$USD M", "TTM 6/1/26", FMT_USDM),
            ("Code Assist savings already banked", "={S:banked}/1000000", "$USD M", "TTM 6/1/26", FMT_USDM),
            ("Residual addressable base", "={S:base_resid}/1000000", "$USD M", "TTM 6/1/26", FMT_USDM),
        ],
        goal=[
            ("Productivity uplift x steady-state adoption", "={S:prod_uplift}*{S:adoption}", "%", "Steady state", FMT_PCT0),
            ("Capture rate to bankable cost", "={S:capture}", "%", "Steady state", FMT_PCT0),
        ],
        incr=[
            ("Bankable annual benefit (run rate)", "={S:ben_loop}/1000000", "$USD M", None, FMT_USDM),
        ],
    ),
)

SDLC2 = dict(
    code="SDLC-2",
    short="PDLC Re-imagination",
    name="PDLC re-imagination — agentic product development lifecycle across product, program and design",
    model_sheet="SDLC-2 Model",
    wave_sheet="SDLC-2 WAVE",
    workstream="SDLC (ELT sponsor: Srini | WSL: Pooja | IOs: Pooja, Aruna)",
    owner="Aruna (IO) — TBC",
    bu="CTO / SDLC",
    status="Structure ready; baselines PENDING data requests — see open items",
    golive=(2027, 6),
    ramp_months=12,
    tab_color="4472C4",
    sources=COMMON_SOURCES,
    open_items=[
        "Product/program/design FTE population and cost pending (SDLC data request #1, PDLC side — ETO; "
        "'back on McK' for time-spent validation, request #2).",
        "PDLC output baseline (PRDs, epics, specs, releases) pending — request #4; converts uplift to capacity.",
        "PDLC tooling & spend baseline (Figma, PRD gen, Jira) pending — request #5; sizes investment and nets run cost.",
        "Build shape mirrors the Servicing S2 delivery pod as a placeholder — refine with IOs before S3.",
    ],
    assumptions=[
        ("#SUB", "Baseline / denominator  (PENDING data request #1 — PDLC side)"),
        ("pd_fte", "Product + program + design FTE population — in scope", 0, "# FTE", FMT_NUM,
         PENDING + "Data request #1 (ETO)"),
        ("pd_flc", "Avg fully loaded cost per PDLC FTE", 0, "$/yr", FMT_USD,
         PENDING + "Data request #1"),
        ("#SUB", "Impact drivers  (Aug 13 deck pp. 9, 19–21 — preliminary)"),
        ("pd_lift", "PDLC productivity lift across product/program/design", 0.20, "%", FMT_PCT0,
         "PLACEHOLDER — refine with time-spent-by-activity data (request #2)"),
        ("pd_adoption", "Steady-state adoption", 0.75, "%", FMT_PCT0, "PLACEHOLDER"),
        ("pd_capture", "Capture rate — capacity converted to bankable cost", 0.65, "%", FMT_PCT0,
         "PLACEHOLDER — align with SDLC-1 capture logic"),
        ("#SUB", "Investment uplifts (consistent with Servicing S2 standard)"),
        ("pm_pct", "Programme management, % of build", 0.08, "%", FMT_PCT0, None),
        ("cont_pct", "Contingency, % of build incl. PM", 0.10, "%", FMT_PCT0, None),
    ],
    calc=[
        ("pd_base", "Total in-scope PDLC labor base",
         "={pd_fte}*{pd_flc}", "$/yr", FMT_USD, None),
        ("pd_capval", "Gross capacity value created",
         "={pd_base}*{pd_lift}*{pd_adoption}", "$/yr", FMT_USD, None),
        ("ben_pdlc", "Bankable annual benefit (steady state)",
         "={pd_capval}*{pd_capture}", "$/yr", FMT_USD,
         "Feeds WAVE benefit line"),
    ],
    benefit_lines=[
        dict(sym="ben_pdlc", label="OPEX - Product/program/design capacity release (PDLC)",
             category="opex", runrate="{ben_pdlc}", baseline="={pd_base}/1000000",
             comment="Bankable share of PDLC capacity created"),
    ],
    runcost_lines=[
        dict(label="OPEX - PDLC harness / product tooling run", annual=0, scale="N", start=(2027, 6),
             notes=PENDING + "Net of tooling spend baseline (request #5)"),
        dict(label="OPEX - Model / token consumption", annual=0, scale="Y", start=(2027, 6),
             notes=PENDING + "PDLC-side consumption not yet available (request #11)"),
    ],
    milestones={
        "Plan / Design": dict(assump="PLACEHOLDER shape mirroring the AAO delivery pod — refine with IO.",
                              team=4, months=2, cont=0.10, start=(2026, 11)),
        "Build / Test": dict(assump="PLACEHOLDER — one 8-FTE pod for ~5 months.",
                             team=8, months=5, cont=0.10, start=(2027, 1)),
        "Pilot / Change Mgmt.": dict(assump="PLACEHOLDER — scale-up team of 5 through rollout.",
                                     team=5, months=6, cont=0.10, start=(2027, 6)),
        "Scale / Run": dict(assump="Run-phase support carried as recurring run cost (Section 6).",
                            team=0, months=0, cont=0.10, start=(2027, 12)),
    },
    onetime_nonlabor=[
        dict(label="Vendor / integration / tooling set-up", total=0, months=3, start=(2027, 1),
             cap=0.0, notes=PENDING + "Build-vs-buy due W6 tech workshop"),
        dict(label="Programme management (8% of build)",
             total="={pm_pct}*({MS_TOTAL}+{NL:1})", months=9, start=(2026, 11), cap=0.0,
             notes="8% x (milestone labor + non-labor build items)"),
        dict(label="Contingency (10% of build incl. PM)",
             total="={cont_pct}*({MS_TOTAL}+{NL:1}+{NL:2})", months=9, start=(2026, 11), cap=0.0,
             notes="10% x (build subtotal incl. PM)"),
    ],
    wave_driver=dict(
        baseline=[
            ("Product/program/design FTE in scope", "={S:pd_fte}", "# FTE", "TTM 6/1/26", FMT_NUM),
            ("Avg fully loaded cost per PDLC FTE", "={S:pd_flc}", "$ / FTE", "TTM 6/1/26", FMT_USD),
            ("Total in-scope PDLC labor base", "={S:pd_base}/1000000", "$USD M", "TTM 6/1/26", FMT_USDM),
        ],
        goal=[
            ("PDLC lift x steady-state adoption", "={S:pd_lift}*{S:pd_adoption}", "%", "Steady state", FMT_PCT0),
            ("Capture rate to bankable cost", "={S:pd_capture}", "%", "Steady state", FMT_PCT0),
        ],
        incr=[
            ("Bankable annual benefit (run rate)", "={S:ben_pdlc}/1000000", "$USD M", None, FMT_USDM),
        ],
    ),
)

META = dict(
    title="PROJECT ZENITH — SDLC WORKSTREAM | INITIATIVE MODELS & WAVE TEMPLATES",
    workstream="SDLC — Raise engineering throughput and reimagine PDLC through agentic loop engineering. "
               "ELT sponsor: Srini | WSL: Pooja | IOs: Pooja, Aruna.",
    purpose="One file per workstream: each initiative has a Model sheet (all logic and inputs) formula-linked "
            "into its own copy of the standard WAVE business-case template. S2 gate: Sep 3/4; S3: Sep 18.",
    version="v1 — structure complete; SDLC baselines pending data requests (models compute $0 until "
            "baseline inputs are populated; impact-driver rates are seeded from the Aug 13 / Board decks).",
    prepared="Prepared by AAO model build, 31 Aug 2026. Sources: Project Zenith workplan vS_1; "
             "Zenith Business Case Template by Lever (WAVE); Aug 13 deck pp. 9, 19–21; Board deck pp. 12, 22.",
    sources="Workplan SDLC tab (initiatives, data POV); SDLC Data Requests tab (12 requests, 4 shared by Pooja); "
            "WAVE standard template (reference copy at the end of this file).",
    sheet_index=[
        ("Cover", "This sheet — orientation, legend, deviations, open items."),
        ("Instructions", "The WAVE template's own instruction sheet (as uploaded; dead broken-reference drop-down cells cleared)."),
        ("Rate Card", "Shared people-cost engine: rate basis (yearly/monthly/hourly), role table + blended rate, "
                      "contingency reference, capitalization policy."),
        ("Summary", "Portfolio roll-up of both initiatives (links to WAVE sheets)."),
        ("SDLC-1 Model / SDLC-1 WAVE", "Agentic loop engineering — model + linked WAVE template."),
        ("SDLC-2 Model / SDLC-2 WAVE", "PDLC re-imagination — model + linked WAVE template."),
        ("Standard Template", "Reference copy of the standard WAVE template (only error-guard fixes applied — see deviations)."),
    ],
    linking_notes=LINKING_NOTES,
    deviations=STD_DEVIATIONS,
    open_items=[
        "No SDLC sizing model file was provided — only the workplan. These models are built from the workplan's "
        "data POV and impact-driver ranges; every baseline is an explicit PENDING input (currently 0), so "
        "benefits read $0 until data request #1 (FTE/cost baseline) lands.",
        "Productivity/adoption/capture rates are PLACEHOLDERS from preliminary deck ranges — validate with Finance.",
        "Investment build shape mirrors the Servicing S2 delivery pod (4/2mo plan, 8/5mo build, 5/6mo scale-up, "
        "PM 8%, contingency 10%, milestone contingency 10% = S2 risk adjustment) as the consistent standard — "
        "refine with IOs.",
        "Rate Card role rates are placeholders; Servicing S2 reference: $200k/yr blended delivery, $180k/yr run team.",
        "Capitalization %s (Build/Test 80% default) need Finance sign-off (ASC 350-40).",
    ],
)

CAP_NOTE = ("Capitalization policy note: this file defaults Build/Test labor to 80% capitalizable "
            "(Rate Card) pending Finance sign-off; the Servicing file defaults to 0% to mirror the S2 "
            "model's all-cash treatment. Align the policy across workstreams with Finance before the S2 gate.")

if __name__ == "__main__":
    assemble("Zenith_SDLC_Models_and_WAVE_v1.xlsx", META, RC_DEFAULTS,
             [SDLC1, SDLC2], "SDLC WORKSTREAM", cap_note=CAP_NOTE)
