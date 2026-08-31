#!/usr/bin/env python3
"""Build Zenith_Sales_Models_and_WAVE_v1.xlsx — 2 initiatives."""
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
        "Role rates are PLACEHOLDERS — replace with the PayPal/FP&A rate card. Servicing S2 reference: "
        "$200,000/yr blended loaded delivery FTE (+10% delivery risk), $180,000/yr run-team FTE.",
        "Team composition mirrors the standard AAO delivery-pod thinking; adjust for vendor-heavy builds "
        "(PRM/orchestration) where internal pod may be smaller.",
        "Build/Test capitalization default of 80% follows a typical internal-use software policy — "
        "CONFIRM WITH FINANCE, especially for vendor/SaaS-heavy builds where treatment differs.",
    ],
)

COMMON_SOURCES = [
    "Workplan: 'Project Zenith Automation workplan and data requests vS_1.xlsx', Sales tab + Sales Data Requests tab",
    "Impact ranges: Aug 13 deck pp. 6, 14–15; Board deck pp. 9, 20, 52 (preliminary — Finance to validate)",
]

SALES1 = dict(
    code="SALES-1",
    short="Underwriting & Pricing — Front Book",
    name="Agentic underwriting and pricing for the front book — faster cycle times, freed seller capacity, RoS uplift",
    model_sheet="SALES-1 Model",
    wave_sheet="SALES-1 WAVE",
    workstream="Sales (ELT sponsor: Susan | WSL: Selwyn)",
    owner="Sales initiative owner — TBC",
    bu="Global Sales",
    status="Structure ready; NSR/seller baselines to populate from received datasets — see open items",
    golive=(2027, 4),
    ramp_months=9,
    tab_color="ED7D31",
    sources=COMMON_SOURCES,
    open_items=[
        "Baselines to populate: front-book NSR by segment (pending), TM% by BU/region (received 8/20 — "
        "reflects CEO ask on revenue-quality differences), FLC by region (received 8/21), seller counts & "
        "time-on-UW split (pending).",
        "Revenue-acceleration conversion factor (cycle time -> incremental NSR) must be defined with Finance — "
        "incremental vs pull-forward treatment per the Finance approval package requirements.",
        "Sales/Risk attribution and Risk & Compliance dependency (underwriting, credit decisioning, "
        "risk-based pricing) to be resolved.",
        "Interviews in flight (Pricing 8/27, Underwriting 8/27, Tech 8/26); build shape below is the "
        "standard AAO pod PLACEHOLDER — refine after tech workshop (W6).",
    ],
    assumptions=[
        ("#SUB", "Baseline / denominator  (populate from received datasets + pending requests)"),
        ("nsr_fb", "Front-book NSR in scope (annual)", 0, "$/yr", FMT_USD,
         PENDING + "NSR by segment — pending"),
        ("tm_pct", "Transaction margin (TM % of NSR) — blended in scope", 0, "%", FMT_PCT,
         "Received 8/20 by BU/region — populate blended in-scope value"),
        ("sellers", "# sellers in scope (UW/pricing-involved)", 0, "# FTE", FMT_NUM,
         PENDING + "Seller counts by segment — pending"),
        ("flc_seller", "Avg fully loaded cost per seller", 0, "$/yr", FMT_USD,
         "FLC by region received 8/21 — populate blended value"),
        ("time_uw", "% of seller time on UW, pricing & related activities", 0, "%", FMT_PCT0,
         PENDING + "Seller time-allocation — pending"),
        ("#SUB", "Impact drivers  (Aug 13 deck pp. 6, 14 — preliminary ranges, midpoints seeded)"),
        ("ct_red_uw", "UW cycle-time reduction", 0.70, "%", FMT_PCT0, "Source: 70%"),
        ("ct_red_pr", "Pricing cycle-time reduction", 0.25, "%", FMT_PCT0, "Source: 20–30% — midpoint"),
        ("rev_accel_factor", "Revenue-acceleration conversion (% incremental NSR from faster cycles)", 0, "%", FMT_PCT,
         PENDING + "Define with Finance: converts cycle-time reduction into incremental NSR; "
                   "keep incremental vs pull-forward split explicit"),
        ("rev_capture", "Capture rate — revenue acceleration", 0.75, "%", FMT_PCT0, "Source: 75%"),
        ("ros_uplift", "RoS / margin uplift", 0.025, "%", FMT_PCT, "Source: 2–3% — midpoint"),
        ("ros_capture", "Capture rate — RoS uplift", 0.75, "%", FMT_PCT0,
         "Assumed same as pricing capture — confirm"),
        ("cap_freed_uw", "Seller capacity freed — UW", 0.35, "%", FMT_PCT0, "Source: 30–40% — midpoint"),
        ("cap_freed_pr", "Seller capacity freed — pricing", 0.30, "%", FMT_PCT0, "Source: 25–35% — midpoint"),
        ("seller_capture", "Capture rate — seller capacity to cost", 0.65, "%", FMT_PCT0, "Source: 65%"),
        ("#SUB", "Investment uplifts (consistent with Servicing S2 standard)"),
        ("pm_pct", "Programme management, % of build", 0.08, "%", FMT_PCT0, None),
        ("cont_pct", "Contingency, % of build incl. PM", 0.10, "%", FMT_PCT0, None),
    ],
    calc=[
        ("margin_base", "In-scope margin base (NSR x TM%)",
         "={nsr_fb}*{tm_pct}", "$/yr", FMT_USD, None),
        ("rev_accel", "Revenue acceleration — UW + pricing cycle time",
         "={nsr_fb}*{tm_pct}*{rev_accel_factor}*{rev_capture}", "$/yr", FMT_USD,
         "Margin base x acceleration conversion x capture. Cycle-time reductions (70% UW / 25% pricing) "
         "inform the conversion factor — keep the factor honest about incremental vs pull-forward"),
        ("ros_ben", "RoS / pricing uplift benefit",
         "={nsr_fb}*{tm_pct}*{ros_uplift}*{ros_capture}", "$/yr", FMT_USD,
         "Margin base x RoS uplift x capture — confirm whether uplift applies to NSR or TM base"),
        ("seller_ben", "Seller capacity freed (bankable)",
         "={sellers}*{flc_seller}*{time_uw}*(({cap_freed_uw}+{cap_freed_pr})/2)*{seller_capture}",
         "$/yr", FMT_USD,
         "Sellers x FLC x % time on UW/pricing x avg capacity freed x capture"),
    ],
    benefit_lines=[
        dict(label="Revenue - Acceleration from UW & pricing cycle time", category="rev",
             runrate="{rev_accel}", baseline="={margin_base}/1000000",
             comment="Margin base uplift from faster cycle times (incremental share only)"),
        dict(label="Revenue - RoS / pricing uplift", category="rev",
             runrate="{ros_ben}", baseline="={margin_base}/1000000",
             comment="2–3% RoS uplift at 75% capture (midpoint seeded)"),
        dict(label="OPEX - Seller capacity freed (UW & pricing)", category="opex",
             runrate="{seller_ben}", baseline="={sellers}*{flc_seller}/1000000",
             comment="30–40% (UW) / 25–35% (pricing) seller capacity freed at 65% capture"),
    ],
    runcost_lines=[
        dict(label="OPEX - Token cost for agents", annual=0, scale="Y", start=(2027, 4),
             notes=PENDING + "Agent token consumption — scales with adoption/ramp"),
        dict(label="OPEX - Vendor / SaaS recurring", annual=0, scale="N", start=(2027, 4),
             notes=PENDING + "Recurring vendor/licence opex"),
        dict(label="OPEX - Support & maintenance", annual=0, scale="N", start=(2027, 4),
             notes=PENDING + "Ongoing support/maintenance"),
    ],
    milestones={
        "Plan / Design": dict(assump="PLACEHOLDER — standard AAO pod shape; refine after W6 tech workshop "
                                     "and vendor RFP decisions.",
                              team=4, months=2, cont=0.10, start=(2026, 10)),
        "Build / Test": dict(assump="PLACEHOLDER — one 8-FTE pod; vendor build (incl. integrations/data, API) "
                                    "carried in non-labor lines below.",
                             team=8, months=5, cont=0.10, start=(2026, 12)),
        "Pilot / Change Mgmt.": dict(assump="PLACEHOLDER — scale-up team of 5 through segment rollout; "
                                            "change management cost in non-labor below.",
                                     team=5, months=6, cont=0.10, start=(2027, 4)),
        "Scale / Run": dict(assump="Run-phase support carried as recurring run cost (Section 6).",
                            team=0, months=0, cont=0.10, start=(2027, 10)),
    },
    onetime_nonlabor=[
        dict(label="Vendor build (incl. integrations / data / API)", total=0, months=5, start=(2026, 12),
             cap=0.0, notes=PENDING + "Build cost incl. vendor — RFP W8"),
        dict(label="Change management", total=0, months=6, start=(2027, 4),
             cap=0.0, notes=PENDING + "Change management cost"),
        dict(label="Programme management (8% of build)",
             total="={pm_pct}*({MS_TOTAL}+{NL:1}+{NL:2})", months=9, start=(2026, 10), cap=0.0,
             notes="8% x (milestone labor + vendor + change mgmt) — Servicing S2 standard"),
        dict(label="Contingency (10% of build incl. PM)",
             total="={cont_pct}*({MS_TOTAL}+{NL:1}+{NL:2}+{NL:3})", months=9, start=(2026, 10), cap=0.0,
             notes="10% x (build subtotal incl. PM) — Servicing S2 standard"),
    ],
    wave_driver=dict(
        baseline=[
            ("Front-book NSR in scope", "={S:nsr_fb}/1000000", "$USD M", "TTM 6/1/26", FMT_USDM),
            ("Transaction margin (TM % of NSR)", "={S:tm_pct}", "%", "TTM 6/1/26", FMT_PCT),
            ("In-scope margin base", "={S:margin_base}/1000000", "$USD M", "TTM 6/1/26", FMT_USDM),
            ("Sellers in scope x FLC", "={S:sellers}*{S:flc_seller}/1000000", "$USD M", "TTM 6/1/26", FMT_USDM),
        ],
        goal=[
            ("UW / pricing cycle-time reduction", "={S:ct_red_uw}", "% (UW)", "Steady state", FMT_PCT0),
            ("Seller capacity freed x capture", "=(({S:cap_freed_uw}+{S:cap_freed_pr})/2)*{S:seller_capture}", "%", "Steady state", FMT_PCT0),
        ],
        incr=[
            ("Total annual benefit (run rate)", "=({S:rev_accel}+{S:ros_ben}+{S:seller_ben})/1000000",
             "$USD M", None, FMT_USDM),
        ],
    ),
)

SALES2 = dict(
    code="SALES-2",
    short="SMB Long Tail — Partner",
    name="SMB long-tail growth through partner-channel scaling and autonomous SDR outreach",
    model_sheet="SALES-2 Model",
    wave_sheet="SALES-2 WAVE",
    workstream="Sales (ELT sponsor: Susan | WSL: Selwyn)",
    owner="Sales initiative owner — TBC",
    bu="Global Sales",
    status="Structure ready; partner/SDR baselines to populate — see open items",
    golive=(2027, 4),
    ramp_months=9,
    tab_color="ED7D31",
    sources=COMMON_SOURCES,
    open_items=[
        "Partner-channel revenue % received 8/24 — populate the $ base. Attach-rate quartile distribution "
        "and partner SME interview still pending (requests #5–#6).",
        "Incrementality / cannibalization logic must be defined with Finance before S2 sign-off.",
        "SDR conversion & cycle-time baselines pending; seller time on lead mgmt pending.",
        "Cross-functional dependency: partner/channel org + PRM platform; watch overlap with broader "
        "SMB front-book growth (workplan flag).",
        "Seller time saved on lead mgmt is flagged as an ENABLER in source materials — confirm bankability "
        "before counting it in the S2 number.",
    ],
    assumptions=[
        ("#SUB", "Baseline / denominator  (populate from received datasets + pending requests)"),
        ("partner_rev", "Partner/referral-channel revenue (annual NSR)", 0, "$/yr", FMT_USD,
         "% revenue via partner received 8/24 — populate $ base"),
        ("tm_pct2", "Transaction margin (TM % of NSR) — SMB blended", 0, "%", FMT_PCT,
         "From TM% dataset received 8/20"),
        ("sdr_rev", "SDR-influenced revenue base (annual NSR)", 0, "$/yr", FMT_USD,
         PENDING + "SDR conversion & funnel data — pending"),
        ("sellers_lt", "# SMB sellers on lead management", 0, "# FTE", FMT_NUM, PENDING),
        ("flc_lt", "Avg fully loaded cost per SMB seller", 0, "$/yr", FMT_USD,
         "From FLC by region (received 8/21)"),
        ("time_leads", "% of seller time on lead mgmt & related", 0, "%", FMT_PCT0, PENDING),
        ("#SUB", "Impact drivers  (Aug 13 deck pp. 6, 14–15 — preliminary ranges, midpoints seeded)"),
        ("share_uplift", "Partner-channel share uplift", 1.00, "%", FMT_PCT0,
         "Source: ~100% partner-channel share uplift"),
        ("incrementality", "Incrementality factor (net of cannibalization)", 0, "%", FMT_PCT0,
         PENDING + "Define with Finance — cannibalization treatment required for approval package"),
        ("sdr_uplift", "SDR autonomous-outreach conversion uplift", 0.15, "%", FMT_PCT0, "Source: ~15%"),
        ("sdr_capture", "Capture rate — SDR uplift", 0.72, "%", FMT_PCT0, "Source: 72%"),
        ("pullfwd_days", "Cycle-time pull-forward", 12, "days", FMT_NUM,
         "Source: ~12 days revenue acceleration — treat as timing unless Finance agrees incremental; "
         "fold agreed value into the SDR line"),
        ("time_saved", "Seller time saved on lead management", 0.375, "%", FMT_PCT0,
         "Source: 35–40% — midpoint. ENABLER — confirm bankability"),
        ("lt_capture", "Capture rate — seller time saved", 0.65, "%", FMT_PCT0,
         "Assumed consistent with U&P seller capture — confirm"),
        ("#SUB", "Investment uplifts (consistent with Servicing S2 standard)"),
        ("pm_pct", "Programme management, % of build", 0.08, "%", FMT_PCT0, None),
        ("cont_pct", "Contingency, % of build incl. PM", 0.10, "%", FMT_PCT0, None),
    ],
    calc=[
        ("partner_ben", "Partner-channel share uplift benefit (margin)",
         "={partner_rev}*{tm_pct2}*{share_uplift}*{incrementality}", "$/yr", FMT_USD,
         "Partner margin base x share uplift x incrementality (net of cannibalization)"),
        ("sdr_ben", "SDR agent uplift benefit (margin)",
         "={sdr_rev}*{tm_pct2}*{sdr_uplift}*{sdr_capture}", "$/yr", FMT_USD,
         "SDR-influenced margin base x conversion uplift x capture; add agreed pull-forward value here"),
        ("lead_ben", "Seller time saved — lead management (enabler)",
         "={sellers_lt}*{flc_lt}*{time_leads}*{time_saved}*{lt_capture}", "$/yr", FMT_USD,
         "Sellers x FLC x % time on leads x time saved x capture — ENABLER, confirm bankability"),
    ],
    benefit_lines=[
        dict(label="Revenue - Partner-channel share uplift", category="rev",
             runrate="{partner_ben}", baseline="={partner_rev}*{tm_pct2}/1000000",
             comment="~100% share uplift x incrementality (net of cannibalization — Finance to agree)"),
        dict(label="Revenue - SDR agent uplift (conversion + acceleration)", category="rev",
             runrate="{sdr_ben}", baseline="={sdr_rev}*{tm_pct2}/1000000",
             comment="~15% conversion uplift at 72% capture; ~12-day pull-forward folded in once agreed"),
        dict(label="OPEX - Seller time saved on lead management (enabler)", category="opex",
             runrate="{lead_ben}", baseline="={sellers_lt}*{flc_lt}/1000000",
             comment="35–40% time saved at 65% capture — enabler; confirm bankability"),
    ],
    runcost_lines=[
        dict(label="OPEX - Token cost for SDR agents", annual=0, scale="Y", start=(2027, 4),
             notes=PENDING + "SDR agent token consumption — scales with ramp"),
        dict(label="OPEX - PRM / orchestration platform run", annual=0, scale="N", start=(2027, 4),
             notes=PENDING + "Recurring platform opex"),
        dict(label="OPEX - Support & maintenance", annual=0, scale="N", start=(2027, 4),
             notes=PENDING + "Ongoing support/maintenance"),
    ],
    milestones={
        "Plan / Design": dict(assump="PLACEHOLDER — standard AAO pod shape; refine after tech workshop "
                                     "and PRM build/buy decision.",
                              team=4, months=2, cont=0.10, start=(2026, 10)),
        "Build / Test": dict(assump="PLACEHOLDER — one 8-FTE pod; PRM/orchestration vendor build in "
                                    "non-labor lines.",
                             team=8, months=5, cont=0.10, start=(2026, 12)),
        "Pilot / Change Mgmt.": dict(assump="PLACEHOLDER — scale-up team of 5 through partner rollout; "
                                            "partner enablement in non-labor below.",
                                     team=5, months=6, cont=0.10, start=(2027, 4)),
        "Scale / Run": dict(assump="Run-phase support carried as recurring run cost (Section 6).",
                            team=0, months=0, cont=0.10, start=(2027, 10)),
    },
    onetime_nonlabor=[
        dict(label="PRM / orchestration build (vendor)", total=0, months=5, start=(2026, 12),
             cap=0.0, notes=PENDING + "Vendor RFP W8"),
        dict(label="Partner enablement & change management", total=0, months=6, start=(2027, 4),
             cap=0.0, notes=PENDING),
        dict(label="Programme management (8% of build)",
             total="={pm_pct}*({MS_TOTAL}+{NL:1}+{NL:2})", months=9, start=(2026, 10), cap=0.0,
             notes="8% x (milestone labor + vendor + enablement) — Servicing S2 standard"),
        dict(label="Contingency (10% of build incl. PM)",
             total="={cont_pct}*({MS_TOTAL}+{NL:1}+{NL:2}+{NL:3})", months=9, start=(2026, 10), cap=0.0,
             notes="10% x (build subtotal incl. PM) — Servicing S2 standard"),
    ],
    wave_driver=dict(
        baseline=[
            ("Partner/referral-channel NSR", "={S:partner_rev}/1000000", "$USD M", "TTM 6/1/26", FMT_USDM),
            ("SDR-influenced NSR base", "={S:sdr_rev}/1000000", "$USD M", "TTM 6/1/26", FMT_USDM),
            ("TM % of NSR (SMB blended)", "={S:tm_pct2}", "%", "TTM 6/1/26", FMT_PCT),
        ],
        goal=[
            ("Partner share uplift x incrementality", "={S:share_uplift}*{S:incrementality}", "%", "Steady state", FMT_PCT0),
            ("SDR conversion uplift x capture", "={S:sdr_uplift}*{S:sdr_capture}", "%", "Steady state", FMT_PCT0),
        ],
        incr=[
            ("Total annual benefit (run rate)", "=({S:partner_ben}+{S:sdr_ben}+{S:lead_ben})/1000000",
             "$USD M", None, FMT_USDM),
        ],
    ),
)

META = dict(
    title="PROJECT ZENITH — SALES WORKSTREAM | INITIATIVE MODELS & WAVE TEMPLATES",
    workstream="Sales — 2 priority initiatives: (1) Underwriting & Pricing for front book, (2) SMB Long Tail — "
               "Partner. ELT sponsor: Susan | WSL: Selwyn. LE and MM initiatives follow the Track 2 timeline.",
    purpose="One file per workstream: each initiative has a Model sheet (all logic and inputs) formula-linked "
            "into its own copy of the standard WAVE business-case template. S2 submission: Sep 4; S3: Sep 18.",
    version="v1 — structure complete; impact-driver rates seeded from Aug 13 / Board decks (midpoints), "
            "revenue/seller baselines to be populated from received + pending datasets (models compute $0 "
            "until baselines are entered).",
    prepared="Prepared by AAO model build, 31 Aug 2026. Sources: Project Zenith workplan vS_1; "
             "Zenith Business Case Template by Lever (WAVE); Aug 13 deck pp. 6, 14–15; Board deck pp. 9, 20, 52.",
    sources="Workplan Sales tab (initiative-specific data POV); Sales Data Requests tab (4 of 6 received); "
            "WAVE standard template (reference copy at the end of this file).",
    sheet_index=[
        ("Cover", "This sheet — orientation, legend, deviations, open items."),
        ("Instructions", "The WAVE template's own instruction sheet (as uploaded; dead broken-reference drop-down cells cleared)."),
        ("Rate Card", "Shared people-cost engine: rate basis, role table + blended rate, contingency reference, "
                      "capitalization policy."),
        ("Summary", "Portfolio roll-up of both initiatives (links to WAVE sheets)."),
        ("SALES-1 Model / SALES-1 WAVE", "Underwriting & Pricing front book — model + linked WAVE template."),
        ("SALES-2 Model / SALES-2 WAVE", "SMB Long Tail — Partner — model + linked WAVE template."),
        ("Standard Template", "Reference copy of the standard WAVE template (only error-guard fixes applied — see deviations)."),
    ],
    linking_notes=LINKING_NOTES,
    deviations=STD_DEVIATIONS,
    open_items=[
        "No Sales sizing model file was provided — only the workplan. Models are built from the workplan's "
        "initiative-specific data POV: impact-driver rates seeded (midpoints of stated ranges), baselines as "
        "explicit PENDING inputs (currently 0). Benefits read $0 until NSR/seller baselines are entered.",
        "Revenue-quality (TM%) differentiation by BU/region — per CEO feedback — is wired in as the margin "
        "base (NSR x TM%); populate TM% from the dataset received 8/20.",
        "Incrementality/cannibalization (SALES-2) and incremental-vs-pull-forward (SALES-1) treatments are "
        "explicit input factors set to 0 until Finance agrees them — deliberately conservative.",
        "Seller-time-saved line on SALES-2 is an ENABLER per source materials — confirm bankability.",
        "Investment: standard milestone people-cost table with the Servicing S2 uplift standard (PM 8%, "
        "contingency 10%, milestone contingency 10%); vendor build costs are separate non-labor lines (pending RFPs).",
        "Rate Card role rates are placeholders; capitalization defaults need Finance sign-off.",
    ],
)

CAP_NOTE = ("Capitalization policy note: this file defaults Build/Test labor to 80% capitalizable "
            "(Rate Card) pending Finance sign-off; the Servicing file defaults to 0% to mirror the S2 "
            "model's all-cash treatment. Align the policy across workstreams with Finance before the S2 gate.")

if __name__ == "__main__":
    assemble("Zenith_Sales_Models_and_WAVE_v1.xlsx", META, RC_DEFAULTS,
             [SALES1, SALES2], "SALES WORKSTREAM", cap_note=CAP_NOTE)
