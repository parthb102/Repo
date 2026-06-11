#!/usr/bin/env python3
"""Build the Platform Assessment Tracker workbook.

One tab per capability, each with a clickable tracker, one assessment table
per sub-capability (state / imperative-to-exit / exit-complexity dropdowns,
auto gray-out of target & exception rows, auto tranche) and a live
benefits-vs-complexity matrix that re-plots platform "bubbles" as scores
change. A Summary tab rolls up tranche counts with jump links.

Requires desktop Excel 2016+ (TEXTJOIN). No macros.
"""

import os
import re

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "Platform_Assessment_Tracker.xlsx")

N_ROWS = 10  # platform rows provisioned per sub-capability

CAPABILITIES = [
    ("Boarding", ["Boarding Experience", "Ingress", "Boarding Orchestration",
                  "Integration & Messaging", "Credit & Underwriting",
                  "CPQ / Quote-pricing"]),
    ("Single-in", ["Global API", "Payment Apps & SDKs", "Developer Experience",
                   "Hosted Solutions", "Unified Proposition"]),
    ("Sales & Servicing", ["CRM", "Servicing Tools", "Sales Automation",
                           "Risks"]),
    ("Payment Processing", ["Gateway", "Switch", "Clearing Back-end",
                            "Authorization Host", "Transaction monitoring",
                            "APMs/LPMs"]),
    ("VAS", ["Routing", "Networking Payment Tokens", "DCC eDCC", "Fraud",
             "Credential Management", "Gifts", "Managed Optimization",
             "3DS / exemptions", "FX"]),
    ("Unified Data and AI", ["Overall"]),
    ("Global Infrastructure", ["Data Centers", "Cloud", "Observability",
                               "Security", "AI Tools", "Design Systems"]),
    ("Single-out", ["Portal", "Reporting", "Billing", "Disputes", "Payouts",
                    "PFaaS Products"]),
]

TAB_COLORS = {
    "Summary": "1F4E79", "Boarding": "2E75B6", "Single-in": "00B0F0",
    "Sales & Servicing": "7030A0", "Payment Processing": "C00000",
    "VAS": "ED7D31", "Unified Data and AI": "00B050",
    "Global Infrastructure": "808080", "Single-out": "BF8F00",
}

# Illustrative rows from the source slide (Payment Processing -> Gateway)
# plus two demo rows for Boarding requested in the working session.
SEED = {
    ("Payment Processing", "Gateway"): [
        ("Edge", "Non-target state", "High", "High",
         "Illustrative example from the slide - plots as Tranche 3"),
        ("WP Total / Emboss", "Non-target state", "High", "Medium",
         "Illustrative example from the slide - plots as Tranche 2"),
        ("Innovo", "Non-target state", "Medium", "Low",
         "Illustrative example from the slide - plots as Tranche 1"),
        ("EWay", "Non-target state", "Medium", "Medium",
         "Illustrative example from the slide - plots as Tranche 2"),
        ("Unified Gateway (example)", "Target state", "", "",
         "Example of a target-state platform - row grays out and is "
         "excluded from the matrix"),
    ],
    ("Boarding", "Boarding Experience"): [
        ("Example platform A (illustrative)", "Non-target state", "High",
         "Low",
         "Illustrative only - high imperative, low complexity plots as "
         "Tranche 1. Replace with real data."),
        ("Example platform B (illustrative)", "Exception", "", "",
         "Illustrative exception - row grays out and is excluded from the "
         "matrix. Capture the reason for the exception here."),
    ],
}

# TAM 2.0 SPOC tracker extract: (capability, sub-capability, raw name cells
# across the Product / Tech / Architecture columns). Rows with no names are
# omitted. The empty Big Rock for Unified Data and AI maps to "Overall".
SPOC_ROWS = [
    ("Single-in", "Global API",
     ["Alexander Dewison <AD72624@globalpayments.com>"]),
    ("Single-in", "Payment Apps & SDKs",
     ["Stuart Taylor, Scott Moser"]),
    ("Single-in", "Developer Experience",
     ["Alexander Dewison <AD72624@globalpayments.com>"]),
    ("Single-in", "Hosted Solutions",
     ["Alexander Dewison <AD72624@globalpayments.com>"]),
    ("Single-in", "Unified Proposition",
     ["Alexander Dewison <AD72624@globalpayments.com>"]),
    ("Boarding", "Boarding Experience",
     ["Alan Johnson <AJ16933@globalpayments.com>",
      "Guthmiller, Lindsay (WP) <Lindsay.Guthmiller@worldpay.com>",
      "Fredrick Mjema <FM83866@globalpayments.com>"]),
    ("Boarding", "Boarding Experience",
     ["Pritchett, David (WP) <david.pritchett@worldpay.com>"]),
    ("Boarding", "Boarding Orchestration",
     ["Alan Johnson <AJ16933@globalpayments.com>",
      "Vivek Pujeri <VP16572@globalpayments.com>",
      "Bateman, Patrick (WP) <Patrick.Bateman@worldpay.com>"]),
    ("Boarding", "Boarding Orchestration",
     ["Fishel, Rebecca (WP) <rebecca.fishel@worldpay.com>"]),
    ("Boarding", "Boarding Orchestration",
     ["Bossenbroek, Bradley (WP) <Bradley.Bossenbroek@Worldpay.com>"]),
    ("Sales & Servicing", "CRM",
     ["White, Khali (WP) <khali.white@worldpay.com>; ",
      "Guthmiller, Lindsay (WP) <Lindsay.Guthmiller@worldpay.com>"]),
    ("Sales & Servicing", "CRM",
     ["Girard, Tuarai (WP) <Tuarai.Girard@Worldpay.com>",
      "Vivek Pujeri <VP16572@globalpayments.com>"]),
    ("Sales & Servicing", "CRM",
     ["Wright, Charlie (WP) <Charlie.Wright@Worldpay.com>",
      "Jason Randall <JR29366@globalpayments.com>"]),
    ("Sales & Servicing", "Servicing Tools",
     ["White, Khali (WP) <khali.white@worldpay.com>; ",
      "Guthmiller, Lindsay (WP) <Lindsay.Guthmiller@worldpay.com>"]),
    ("Sales & Servicing", "Servicing Tools",
     ["Girard, Tuarai (WP) <Tuarai.Girard@Worldpay.com>",
      "Vivek Pujeri <VP16572@globalpayments.com>"]),
    ("Sales & Servicing", "Servicing Tools",
     ["Wright, Charlie (WP) <Charlie.Wright@Worldpay.com>",
      "Jason Randall <JR29366@globalpayments.com>"]),
    ("Sales & Servicing", "Sales Automation",
     ["Jake Gwinn <jake.gwinn@globalpayments.com>"]),
    ("Payment Processing", "Clearing Back-end",
     ["Mike Clark <MC98382@globalpayments.com>",
      "Ringer, Philip (WP) <Philip.Ringer@worldpay.com>",
      "Beere, Jon (WP) <jon.beere@worldpay.com>"]),
    ("Payment Processing", "Clearing Back-end",
     ["Alan Bainbridge <AB61694@globalpayments.com>",
      "Jones, Richard (WP) <Richard.Jones@worldpay.com>"]),
    ("Payment Processing", "Clearing Back-end",
     ["Downey, Peter (WP) <Peter.Downey@worldpay.com>"]),
    ("Payment Processing", "Authorization Host",
     ["Mike Clark <MC98382@globalpayments.com>",
      "Ringer, Philip (WP) <Philip.Ringer@worldpay.com>",
      "Beere, Jon (WP) <jon.beere@worldpay.com>"]),
    ("Payment Processing", "Authorization Host",
     ["Anushree Kolhe <AK31134@globalpayments.com>"]),
    ("Payment Processing", "Authorization Host",
     ["Annunziata, James (WP) <James.Annunziata@worldpay.com>"]),
    ("VAS", "Routing",
     ["Harding, Jason (WP) <jason.harding@worldpay.com>",
      "Srini Turlapati <ST64774@globalpayments.com>",
      "Dubreuil, Andre (WP) <andre.dubreuil@worldpay.com>"]),
    ("VAS", "Routing",
     ["Thakkar, Sunny (WP) <sunny.thakkar@worldpay.com>"]),
    ("VAS", "Networking Payment Tokens",
     ["Harding, Jason (WP) <jason.harding@worldpay.com>",
      "Srini Turlapati <ST64774@globalpayments.com>"]),
    ("VAS", "DCC eDCC",
     ["Lang, Marcus (WP) <marcus.lang2@worldpay.com>",
      "Joshi, VikramSuhas (WP) <VikramSuhas.Joshi@worldpay.com>"]),
    ("VAS", "DCC eDCC",
     ["Jaroslav Farkas <jf61853@globalpayments.com>"]),
    ("VAS", "Fraud",
     ["Moore, Justin (WP) <justin.moore@worldpay.com>",
      "Srini Turlapati <ST64774@globalpayments.com>"]),
    ("VAS", "Credential Management",
     ["Harding, Jason (WP) <jason.harding@worldpay.com>",
      "Srini Turlapati <ST64774@globalpayments.com>",
      "Dubreuil, Andre (WP) <andre.dubreuil@worldpay.com>"]),
    ("VAS", "Gifts",
     ["Genessa Prictor <GP64946@globalpayments.com>",
      "Srini Turlapati <ST64774@globalpayments.com>"]),
    ("VAS", "Gifts",
     ["Nail, John (WP) <john.nail@worldpay.com>"]),
    ("VAS", "Managed Optimization",
     ["Harding, Jason (WP) <jason.harding@worldpay.com>",
      "Srini Turlapati <ST64774@globalpayments.com>",
      "Dubreuil, Andre (WP) <andre.dubreuil@worldpay.com>"]),
    ("VAS", "3DS / exemptions",
     ["Thakkar, Sunny (WP) <sunny.thakkar@worldpay.com>",
      "Srini Turlapati <ST64774@globalpayments.com>"]),
    ("VAS", "FX",
     ["Srini Turlapati <ST64774@globalpayments.com>"]),
    ("VAS", "FX",
     ["Joshi, VikramSuhas (WP) <VikramSuhas.Joshi@worldpay.com>"]),
    ("Unified Data and AI", "Overall",
     ["Heaton, Ryan (WP) <ryan.heaton@worldpay.com>"]),
    ("Unified Data and AI", "Overall",
     ["Shah, Himanshu (WP) <himanshu.shah@worldpay.com>"]),
    ("Single-out", "Portal",
     ["Jaemi Bremner <JB32645@globalpayments.com>",
      "Amutha Velayutham <AV14206@globalpayments.com>"]),
    ("Single-out", "Reporting",
     ["helen.ryan@worldpay.com",
      "Srini Turlapati <ST64774@globalpayments.com>"]),
    ("Single-out", "Reporting",
     ["Shaily Daftari <SD55321@globalpayments.com>",
      "Amutha Velayutham <AV14206@globalpayments.com>"]),
    ("Single-out", "Disputes",
     ["helen.ryan@worldpay.com",
      "Srini Turlapati <ST64774@globalpayments.com>"]),
    ("Single-out", "Disputes",
     ["Rosemary Kiley <rk67937@globalpayments.com>",
      "Dowden, Travis (WP) <Travis.Dowden@worldpay.com>"]),
    ("Single-out", "Disputes",
     ["Singleton, Kimberly (WP) <Kimberly.Singleton@worldpay.com>",
      "Neville DCosta <ND34475@globalpayments.com>"]),
    ("Single-out", "PFaaS Products",
     ["Blair, David (WP) <David.Blair@worldpay.com>",
      "Curtis Landry <CL78324@globalpayments.com>",
      "Dubreuil, Andre (WP) <andre.dubreuil@worldpay.com>"]),
    ("Single-out", "PFaaS Products",
     ["Soltan Nayabkhil <SN68225@globalpayments.com>"]),
]


def _parse_names(chunk):
    """Normalize one raw tracker entry to a list of 'First Last' names."""
    chunk = chunk.strip().rstrip(";").strip()
    if not chunk:
        return []
    if "@" in chunk and "<" not in chunk:
        # bare email -> derive name from the local part
        words = [w for w in re.split(r"[._\d]+", chunk.split("@", 1)[0]) if w]
        return [" ".join(w.capitalize() for w in words)]
    name = re.sub(r"<[^>]*>", "", chunk).replace("(WP)", "")
    name = name.strip().rstrip(";,").strip()
    if not name:
        return []
    if "," in name:
        parts = [p.strip() for p in name.split(",") if p.strip()]
        if all(" " in p for p in parts):
            return parts  # already a list of "First Last" names
        if len(parts) == 2:
            return [f"{parts[1]} {parts[0]}"]  # "Last, First" -> flip
    return [name]


def spoc_map():
    """(capability, sub-capability) -> ordered, de-duplicated name list."""
    out = {}
    for cap, sub, cells in SPOC_ROWS:
        names = out.setdefault((cap, sub), [])
        for cell in cells:
            for chunk in cell.split(";"):
                for n in _parse_names(chunk):
                    if n not in names:
                        names.append(n)
    return out


NAVY = "1F4E79"
HEADER_TINT = "DDEBF7"
LINK = "0563C1"
T1_FILL = "CDE4F5"
T2_FILL = "FFF2CC"
T3_FILL = "FBE2D5"
GRAY_FILL = "D9D9D9"
GRAYED_ROW_FILL = "F2F2F2"
GRAYED_ROW_FONT = "A6A6A6"
NOTE_GRAY = "595959"

CIRCLED = ["①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩"]

thin_gray = Side(style="thin", color="BFBFBF")
thin_blue = Side(style="thin", color="4472C4")
TABLE_BORDER = Border(left=thin_gray, right=thin_gray,
                      top=thin_gray, bottom=thin_gray)
MATRIX_BORDER = Border(left=thin_blue, right=thin_blue,
                       top=thin_blue, bottom=thin_blue)


def solid(color):
    return PatternFill(fill_type="solid", start_color=color, end_color=color)


# Matrix buckets: (imperative, complexity, matrix column, helper column,
#                  tranche label or None, fill)
BUCKETS = [
    ("High", "Low", "K", "O", "Tranche 1", T1_FILL),
    ("High", "Medium", "L", "P", "Tranche 2", T2_FILL),
    ("High", "High", "M", "Q", "Tranche 3", T3_FILL),
    ("Medium", "Low", "K", "R", "Tranche 1", T1_FILL),
    ("Medium", "Medium", "L", "S", "Tranche 2", T2_FILL),
    ("Medium", "High", "M", "T", None, GRAY_FILL),
    ("Low", "Low", "K", "U", None, GRAY_FILL),
    ("Low", "Medium", "L", "V", None, GRAY_FILL),
    ("Low", "High", "M", "W", None, GRAY_FILL),
]

# "Imperative to exit" is explicitly equated with the matrix Benefits axis
# so the two are never read as different dimensions.
TABLE_HEADERS = ["#", "Platform", "State", "Imperative to exit (= Benefits)",
                 "Exit complexity", "Supporting facts", "Tranche (auto)"]

COL_WIDTHS = {"A": 5, "B": 26, "C": 17, "D": 19, "E": 15, "F": 44, "G": 14,
              "H": 2, "I": 4, "J": 9, "K": 26, "L": 26, "M": 26, "N": 2}


def tranche_formula(r):
    return (
        f'=IF(OR($B{r}="",$D{r}="",$E{r}=""),"",'
        f'IF(OR($C{r}="Target state",$C{r}="Exception"),"Out of scope",'
        f'IF($D{r}="Low","No tranche",'
        f'IF($E{r}="Low","Tranche 1",'
        f'IF($E{r}="Medium","Tranche 2",'
        f'IF($D{r}="High","Tranche 3","No tranche"))))))'
    )


def helper_formula(r, imperative, complexity):
    return (
        f'=IF(AND($B{r}<>"",$C{r}<>"Target state",$C{r}<>"Exception",'
        f'$D{r}="{imperative}",$E{r}="{complexity}"),'
        f'$A{r}&"  "&$B{r},"")'
    )


def write_section(ws, sheet_name, s, subcap, dv_state, dv_score):
    """Write one sub-capability block whose header band sits on row s.

    Returns (first_data_row, last_data_row).
    """
    r1, r2 = s + 2, s + 1 + N_ROWS

    # --- section header band -------------------------------------------
    for col in "ABCDEFG":
        ws[f"{col}{s}"].fill = solid(NAVY)
    hc = ws[f"A{s}"]
    hc.value = subcap
    hc.font = Font(bold=True, size=11, color="FFFFFF")
    hc.alignment = Alignment(vertical="center", indent=1)
    ws.merge_cells(f"A{s}:F{s}")
    g = ws[f"G{s}"]
    g.value = f'=HYPERLINK("#\'{sheet_name}\'!A4","▲ tracker")'
    g.font = Font(size=9, color="FFFFFF", underline="single")
    g.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[s].height = 22

    # --- table column headers -------------------------------------------
    for i, h in enumerate(TABLE_HEADERS):
        c = ws.cell(row=s + 1, column=1 + i, value=h)
        c.fill = solid(HEADER_TINT)
        c.font = Font(bold=True, size=9, color=NAVY)
        c.alignment = Alignment(horizontal="center", vertical="center",
                                wrap_text=True)
        c.border = TABLE_BORDER
    ws.row_dimensions[s + 1].height = 26

    # --- data rows --------------------------------------------------------
    for i in range(N_ROWS):
        r = r1 + i
        ws.row_dimensions[r].height = 20
        a = ws[f"A{r}"]
        a.value = CIRCLED[i]
        a.alignment = Alignment(horizontal="center", vertical="center")
        a.font = Font(size=11, color=NAVY)
        ws[f"B{r}"].alignment = Alignment(vertical="center", indent=1)
        ws[f"B{r}"].font = Font(size=10)
        for col in "CDE":
            c = ws[f"{col}{r}"]
            c.alignment = Alignment(horizontal="center", vertical="center")
            c.font = Font(size=10)
        f = ws[f"F{r}"]
        f.alignment = Alignment(vertical="center", wrap_text=True, indent=1)
        f.font = Font(size=9)
        gcell = ws[f"G{r}"]
        gcell.value = tranche_formula(r)
        gcell.font = Font(size=9, italic=True, color=NAVY)
        gcell.alignment = Alignment(horizontal="center", vertical="center")
        for col in "ABCDEFG":
            ws[f"{col}{r}"].border = TABLE_BORDER
        # hidden helper cells feeding the matrix
        for imp, cpx, _mcol, hcol, _lbl, _fill in BUCKETS:
            ws[f"{hcol}{r}"] = helper_formula(r, imp, cpx)

    dv_state.add(f"C{r1}:C{r2}")
    dv_score.add(f"D{r1}:E{r2}")

    # gray out the whole row when the platform is target state or exception
    ws.conditional_formatting.add(
        f"A{r1}:G{r2}",
        FormulaRule(
            formula=[f'OR($C{r1}="Target state",$C{r1}="Exception")'],
            fill=PatternFill(start_color=GRAYED_ROW_FILL,
                             end_color=GRAYED_ROW_FILL, fill_type="solid"),
            font=Font(color=GRAYED_ROW_FONT),
        ),
    )

    # --- assessment matrix -----------------------------------------------
    t = ws[f"K{s}"]
    t.value = "Assessment Outcome"
    t.font = Font(bold=True, size=11, color=NAVY)
    t.alignment = Alignment(horizontal="center", vertical="center")
    ws.merge_cells(f"K{s}:M{s}")

    for col, lbl in zip("KLM", ["Low", "Medium", "High"]):
        c = ws[f"{col}{s + 1}"]
        c.value = lbl
        c.font = Font(bold=True, size=9, color=NOTE_GRAY)
        c.alignment = Alignment(horizontal="center", vertical="center")

    for bi, band in enumerate(["High", "Medium", "Low"]):
        top, bottom = s + 2 + 3 * bi, s + 4 + 3 * bi
        jc = ws[f"J{top}"]
        jc.value = band
        jc.font = Font(bold=True, size=10, color=NOTE_GRAY)
        jc.alignment = Alignment(horizontal="center", vertical="center")
        ws.merge_cells(f"J{top}:J{bottom}")
        for imp, cpx, mcol, hcol, lbl, fill in BUCKETS:
            if imp != band:
                continue
            # _xlfn. prefix is how post-2007 functions must be stored in
            # xlsx XML; Excel shows it as plain TEXTJOIN
            tj = f"_xlfn.TEXTJOIN(CHAR(10),TRUE,{hcol}${r1}:{hcol}${r2})"
            cell = ws[f"{mcol}{top}"]
            cell.value = f'="{lbl}"&CHAR(10)&{tj}' if lbl else f"={tj}"
            cell.font = Font(size=9, color="17375E" if lbl else "404040")
            cell.alignment = Alignment(wrap_text=True, vertical="top",
                                       horizontal="left", indent=1)
            for rr in range(top, bottom + 1):
                cc = ws[f"{mcol}{rr}"]
                cc.fill = solid(fill)
                cc.border = MATRIX_BORDER
            ws.merge_cells(f"{mcol}{top}:{mcol}{bottom}")

    ic = ws[f"I{s + 2}"]
    ic.value = "Benefits (= Imperative to exit)"
    ic.font = Font(bold=True, size=9, color=NOTE_GRAY)
    ic.alignment = Alignment(horizontal="center", vertical="center",
                             text_rotation=90)
    ws.merge_cells(f"I{s + 2}:I{s + 10}")

    cx = ws[f"K{s + 11}"]
    cx.value = "Complexity"
    cx.font = Font(bold=True, size=10, color=NOTE_GRAY)
    cx.alignment = Alignment(horizontal="center", vertical="center")
    ws.merge_cells(f"K{s + 11}:M{s + 11}")

    return r1, r2


def build_readme(wb):
    ws = wb.create_sheet("Read me", 0)
    ws.sheet_properties.tabColor = NAVY
    ws.sheet_view.showGridLines = False
    for col, w in {"A": 2.5, "B": 18, "C": 17, "D": 17, "E": 17,
                   "F": 17, "G": 17, "H": 17}.items():
        ws.column_dimensions[col].width = w

    body_font = Font(size=10, color="404040")
    lead_font = Font(size=10, bold=True, color=NAVY)

    def section(r, text):
        c = ws[f"B{r}"]
        c.value = text
        c.font = Font(bold=True, size=11, color=NAVY)
        for col in "BCDEFGH":
            ws[f"{col}{r}"].fill = solid(HEADER_TINT)
        return r + 1

    def line(r, text, font=None, indent=0):
        c = ws[f"B{r}"]
        c.value = text
        c.font = font or body_font
        c.alignment = Alignment(vertical="center", indent=indent)
        return r + 1

    ws["B1"] = "Exhibit B — Non-target platform tranching"
    ws["B1"].font = Font(bold=True, size=16, color=NAVY)
    ws["B2"] = ("TAM 2.0  ·  read this before filling in your capability "
                "tab — the exercise itself takes about 15 minutes per area.")
    ws["B2"].font = Font(size=10, italic=True, color=NOTE_GRAY)
    ws["B3"] = '=HYPERLINK("#\'Summary\'!A1","Open the Summary →")'
    ws["B3"].font = Font(size=10, color=LINK, underline="single")

    r = section(5, "What this is")
    r = line(r, "Every capability tab lists the current-state platforms per "
                "sub-capability. Mark each platform Target / Non-target / "
                "Exception, score the non-target ones High / Medium / Low on "
                "two dimensions, and the sheet dispositions them into "
                "Tranche 1 / 2 / 3 — the matrix and the Summary update "
                "automatically.")
    r = line(r, "This feeds the investment thesis (due end of June): which "
                "dollars and pods can be freed up right away to redirect, "
                "versus what takes longer. Classification only — pod sizing "
                "for the exits is a separate, later step.")

    r = section(r + 1, "The three states")
    r = line(r, "Target state — go-forward platform. No scoring needed; the "
                "row grays out and drops off the matrix.")
    r = line(r, "Non-target state — platform we intend to exit. Score both "
                "dimensions; it lands in a tranche.")
    r = line(r, "Exception — stays for now for a documented reason (capture "
                "it under Supporting facts); ideally exits eventually. Grays "
                "out like target state.")

    r = section(r + 1, "The tranches")
    for fill, txt in [
        (T1_FILL, "Tranche 1 — quick exits we can get out of fairly fast; "
                  "frees up dollars and pods right away."),
        (T2_FILL, "Tranche 2 — slightly more complex; some nuances and a "
                  "somewhat longer timeline."),
        (T3_FILL, "Tranche 3 — the most complex exits on a progressive "
                  "timeline (e.g., Edge)."),
        (GRAY_FILL, "No tranche — low imperative to exit, or medium "
                    "imperative with high exit complexity; revisit later. "
                    "Either way: no net-new investment on non-target "
                    "platforms — critical / high-priority maintenance only."),
    ]:
        c = ws[f"B{r}"]
        c.value = txt
        c.font = body_font
        c.alignment = Alignment(vertical="center", indent=1)
        for col in "BCDEFGH":
            ws[f"{col}{r}"].fill = solid(fill)
        r += 1

    r = section(r + 1, "How a platform lands in a tranche")
    grid_top = r + 1
    for col, lbl in zip("CDE", ["Low", "Medium", "High"]):
        c = ws[f"{col}{grid_top - 1}"]
        c.value = lbl
        c.font = Font(bold=True, size=9, color=NOTE_GRAY)
        c.alignment = Alignment(horizontal="center")
    legend = [("High", ["Tranche 1", "Tranche 2", "Tranche 3"],
               [T1_FILL, T2_FILL, T3_FILL]),
              ("Medium", ["Tranche 1", "Tranche 2", "—"],
               [T1_FILL, T2_FILL, GRAY_FILL]),
              ("Low", ["—", "—", "—"],
               [GRAY_FILL, GRAY_FILL, GRAY_FILL])]
    for i, (band, labels, fills) in enumerate(legend):
        rr = grid_top + i
        b = ws[f"B{rr}"]
        b.value = band
        b.font = Font(bold=True, size=9, color=NOTE_GRAY)
        b.alignment = Alignment(horizontal="right", vertical="center")
        for col, lbl, fill in zip("CDE", labels, fills):
            c = ws[f"{col}{rr}"]
            c.value = lbl
            c.font = Font(size=9, color="17375E")
            c.alignment = Alignment(horizontal="center", vertical="center")
            c.fill = solid(fill)
            c.border = MATRIX_BORDER
        ws.row_dimensions[rr].height = 18
    r = grid_top + 3
    r = line(r, "Rows: Imperative to exit (= Benefits)   ·   Columns: "
                "Exit complexity",
             Font(size=9, italic=True, color=NOTE_GRAY))

    r = section(r + 1, "Scoring guidance (assessment criteria)")
    r = line(r, "Imperative to exit (= Benefits) — cost savings / avoidance "
                "(pods freed up, vendor licensing eliminated, budgeted spend "
                "avoided), risk reduction (aging infrastructure, EOL "
                "posture, security / vendor risk), downstream enablement "
                "(migrations that can't proceed until the platform "
                "converges).")
    r = line(r, "Exit complexity — gap in target-platform readiness (target "
                "not yet live, capability gaps to close), migration effort "
                "(customer / transaction volume, partner involvement), tech "
                "& integration lift (incremental pods, migration length, "
                "integration depth into the heritage estate).")

    r = section(r + 1, "How to fill in your tab")
    steps = [
        "1.  Open the Summary, find your sub-capability and click Open → "
        "(or use the tracker at the top of each capability tab).",
        "2.  Check the platform list is complete for your area — include "
        "everything in current state, also platforms already flagged "
        "non-strategic in the TAM platform repository (those are exactly "
        "the ones to get rid of).",
        "3.  Set State for each platform: Target state / Non-target state / "
        "Exception.",
        "4.  For non-target platforms set Imperative to exit (= Benefits) "
        "and Exit complexity to High / Medium / Low — the Tranche column "
        "and the matrix update automatically.",
        "5.  Add one or two lines of backing rationale under Supporting "
        "facts.",
    ]
    for s_txt in steps:
        r = line(r, s_txt, indent=1)

    r = section(r + 1, "Ground rules")
    r = line(r, "Directionally correct beats precise — this is a first cut "
                "with brief backing facts, not a science project. Office "
                "hours are scheduled per domain to review and refine.")
    r = line(r, "Payment Processing → Gateway and Boarding → Boarding "
                "Experience contain illustrative examples — replace them "
                "with real data.")
    r = line(r, "Questions before your session: raise them in the domain "
                "office hours or drop them in Supporting facts.")


def build_capability_sheet(wb, cap, subcaps):
    ws = wb.create_sheet(cap)
    ws.sheet_properties.tabColor = TAB_COLORS[cap]
    ws.sheet_view.showGridLines = False
    for col, w in COL_WIDTHS.items():
        ws.column_dimensions[col].width = w
    for col in "OPQRSTUVW":
        ws.column_dimensions[col].hidden = True

    ws["A1"] = f"{cap} — Platform Assessment"
    ws["A1"].font = Font(bold=True, size=15, color=NAVY)
    ws["A2"] = '=HYPERLINK("#\'Summary\'!A1","← Back to Summary")'
    ws["A2"].font = Font(size=10, color=LINK, underline="single")
    ws["C2"] = ("Pick a State, score High / Medium / Low — the tranche, the "
                "matrix and the Summary update automatically.")
    ws["C2"].font = Font(size=9, italic=True, color=NOTE_GRAY)

    th = ws["A4"]
    th.value = "Tracker — jump to a sub-capability:"
    th.font = Font(bold=True, size=10, color=NAVY)
    th.fill = solid(HEADER_TINT)
    th.alignment = Alignment(vertical="center", indent=1)
    for col in "BC":
        ws[f"{col}4"].fill = solid(HEADER_TINT)
    ws.merge_cells("A4:C4")

    dv_state = DataValidation(
        type="list",
        formula1='"Target state,Non-target state,Exception"',
        allow_blank=True)
    dv_score = DataValidation(
        type="list", formula1='"High,Medium,Low"', allow_blank=True)
    ws.add_data_validation(dv_state)
    ws.add_data_validation(dv_score)

    n = len(subcaps)
    section_rows = [n + 6 + i * (N_ROWS + 4) for i in range(n)]

    sections = {}
    for i, (subcap, s) in enumerate(zip(subcaps, section_rows)):
        ws[f"A{5 + i}"] = f"{i + 1}."
        ws[f"A{5 + i}"].alignment = Alignment(horizontal="right")
        ws[f"A{5 + i}"].font = Font(size=10, color=NOTE_GRAY)
        link = ws[f"B{5 + i}"]
        link.value = f'=HYPERLINK("#\'{cap}\'!A{s}","{subcap}")'
        link.font = Font(size=10, color=LINK, underline="single")
        r1, r2 = write_section(ws, cap, s, subcap, dv_state, dv_score)
        sections[subcap] = (s, r1, r2)

    for (scap, ssub), rows in SEED.items():
        if scap != cap:
            continue
        _s, r1, _r2 = sections[ssub]
        for j, (name, state, imp, cpx, facts) in enumerate(rows):
            r = r1 + j
            ws[f"B{r}"] = name
            ws[f"C{r}"] = state
            ws[f"D{r}"] = imp
            ws[f"E{r}"] = cpx
            ws[f"F{r}"] = facts

    return sections


def build_summary(ws, all_sections):
    ws.sheet_properties.tabColor = TAB_COLORS["Summary"]
    ws.sheet_view.showGridLines = False
    for col, w in {"A": 5, "B": 22, "C": 28, "D": 30, "E": 14, "F": 11,
                   "G": 11, "H": 11, "I": 10}.items():
        ws.column_dimensions[col].width = w

    ws["A1"] = "Platform Assessment — Summary"
    ws["A1"].font = Font(bold=True, size=16, color=NAVY)
    ws["A2"] = "Tranche roll-up by capability and sub-capability — counts update automatically from each tab."
    ws["A2"].font = Font(size=10, italic=True, color=NOTE_GRAY)

    ws["A4"] = "How it works:"
    ws["A4"].font = Font(bold=True, size=10, color=NAVY)
    notes = [
        "Start with the Read me tab — state and tranche definitions, scoring guidance and step-by-step instructions.",
        "Every capability tab has a tracker at the top — click a sub-capability to jump straight to its section; each section links back.",
        "For each platform pick a State: Target state and Exception rows gray out automatically and drop off the matrix; Non-target rows stay lit.",
        "Score Imperative to exit (= Benefits) and Exit complexity (High / Medium / Low) — the Tranche column computes itself and the matrix bubbles (① + platform name) re-plot live.",
        "Tranche rules: Low complexity → Tranche 1  ·  Medium complexity → Tranche 2  ·  High complexity + High imperative → Tranche 3  ·  Low imperative (or Medium imperative + High complexity) → no tranche.",
        "Payment Processing → Gateway and Boarding → Boarding Experience are pre-seeded with illustrative examples — replace them with real data.",
        "Built for desktop Excel 2016 or later (no macros).",
    ]
    for i, txt in enumerate(notes):
        c = ws[f"A{5 + i}"]
        c.value = "•  " + txt
        c.font = Font(size=9, color=NOTE_GRAY)

    hdr_row = 13
    headers = ["#", "Capability", "Sub-capability", "SPOCs",
               "Platforms listed", "Tranche 1", "Tranche 2", "Tranche 3",
               "Open"]
    hdr_fills = {"F": T1_FILL, "G": T2_FILL, "H": T3_FILL}
    for i, h in enumerate(headers):
        col = chr(ord("A") + i)
        c = ws[f"{col}{hdr_row}"]
        c.value = h
        if col in hdr_fills:
            c.fill = solid(hdr_fills[col])
            c.font = Font(bold=True, size=10, color=NAVY)
        else:
            c.fill = solid(NAVY)
            c.font = Font(bold=True, size=10, color="FFFFFF")
        c.alignment = Alignment(horizontal="center", vertical="center",
                                wrap_text=True)
        c.border = TABLE_BORDER
    ws.row_dimensions[hdr_row].height = 24

    spocs = spoc_map()
    r = hdr_row + 1
    idx = 1
    for cap, subcaps in CAPABILITIES:
        group_start = r
        for subcap in subcaps:
            s, r1, r2 = all_sections[cap][subcap]
            ws[f"A{r}"] = idx
            ws[f"C{r}"] = subcap
            names = spocs.get((cap, subcap), [])
            d = ws[f"D{r}"]
            d.value = "\n".join(f"• {n}" for n in names)
            d.font = Font(size=9)
            d.alignment = Alignment(vertical="center", wrap_text=True,
                                    indent=1)
            ws[f"E{r}"] = f"=COUNTA('{cap}'!$B${r1}:$B${r2})"
            for col, lbl in zip("FGH", ["Tranche 1", "Tranche 2", "Tranche 3"]):
                ws[f"{col}{r}"] = (
                    f"=COUNTIF('{cap}'!$G${r1}:$G${r2},\"{lbl}\")")
            ws[f"I{r}"] = f'=HYPERLINK("#\'{cap}\'!A{s}","Open →")'
            ws[f"I{r}"].font = Font(size=10, color=LINK, underline="single")
            ws[f"A{r}"].font = Font(size=9, color=NOTE_GRAY)
            ws[f"A{r}"].alignment = Alignment(horizontal="center",
                                              vertical="center")
            ws[f"C{r}"].font = Font(size=10)
            ws[f"C{r}"].alignment = Alignment(vertical="center")
            for col in "EFGH":
                ws[f"{col}{r}"].alignment = Alignment(horizontal="center",
                                                      vertical="center")
                ws[f"{col}{r}"].font = Font(size=10)
            ws[f"I{r}"].alignment = Alignment(horizontal="center",
                                              vertical="center")
            for col in "ABCDEFGHI":
                ws[f"{col}{r}"].border = TABLE_BORDER
            ws.row_dimensions[r].height = max(18, 6 + 13 * len(names))
            r += 1
            idx += 1
        b = ws[f"B{group_start}"]
        b.value = cap
        b.font = Font(bold=True, size=10, color=NAVY)
        b.alignment = Alignment(horizontal="left", vertical="center",
                                indent=1)
        for rr in range(group_start, r):
            ws[f"B{rr}"].fill = solid("EDF2F8")
        if r - 1 > group_start:
            ws.merge_cells(f"B{group_start}:B{r - 1}")

    last_data = r - 1
    ws[f"D{r}"] = "Total"
    ws[f"D{r}"].font = Font(bold=True, size=10, color=NAVY)
    ws[f"D{r}"].alignment = Alignment(horizontal="right", indent=1)
    for col in "EFGH":
        c = ws[f"{col}{r}"]
        c.value = f"=SUM({col}{hdr_row + 1}:{col}{last_data})"
        c.font = Font(bold=True, size=10, color=NAVY)
        c.alignment = Alignment(horizontal="center")
    for col in "ABCDEFGHI":
        ws[f"{col}{r}"].border = Border(top=Side(style="medium", color=NAVY))

    ws.freeze_panes = f"A{hdr_row + 1}"


def main():
    wb = Workbook()
    summary = wb.active
    summary.title = "Summary"
    build_readme(wb)

    all_sections = {}
    for cap, subcaps in CAPABILITIES:
        all_sections[cap] = build_capability_sheet(wb, cap, subcaps)

    build_summary(summary, all_sections)

    wb.properties.title = "Platform Assessment Tracker"
    wb.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
